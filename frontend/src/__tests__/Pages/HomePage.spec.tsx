import React from 'react';
import { render, act, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import MockAdapter from 'axios-mock-adapter';
import api from '../../Services/api';
import {useQuery, QueryClient, QueryClientProvider } from 'react-query'
import HomePage from '../../Pages/HomePage';

const apiMock = new MockAdapter(api);
const wait = (amount = 0): Promise<void> => {
  return new Promise(resolve => setTimeout(resolve, amount));
};
const actWait = async (amount = 0): Promise<void> => {
  await act(async () => {
    await wait(amount);
  });
};
const queryClient = new QueryClient()
describe('Test Home Page', () => {
  it('should be testing HomePage', async () => {
    const renderResult = render(
      <Router>
        <QueryClientProvider client={queryClient} contextSharing={true}>
          <HomePage />
        </QueryClientProvider>
      </Router>,
    );

    const data = [
      {
        "id":7,
        "title":"Camisa Alfonzo Manieto T-Shirt",
        "category":"T-shirt",
        "price":49.99,
        "description":"camisa algodão lisa, fio 30 temperado em verniz",
        "image":"http://127.0.0.1:8000/media/media/352-3528694_plain-blue-t-shirt-png-image-background-blue.png",
        "brand":"Dafiti"
      },
      {
        "id":6,
        "title":"Camisa Alma Americana",
        "category":"T-shirt",
        "price":45.5,
        "description":"camisa algodão lisa fio 30, estilho slimfit",
        "image":"http://127.0.0.1:8000/media/media/1484410852-27953600.png",
        "brand":"Dafiti"
      }
    ]

    const get = apiMock.onGet('/pruduct/all').reply(200, data);
    await actWait();
    expect(renderResult.queryByTestId('header-banner')).toBeVisible;
    expect(renderResult.queryByTestId('bottom-banner')).toBeVisible;
    expect(renderResult.queryByTestId('product-6')).toBeInTheDocument;
    expect(renderResult.queryByTestId('product-7')).toBeInTheDocument;
    expect(renderResult.queryByTestId('add-shopping-cart-icon')).toBeDefined();

    // Testing open cart button click
    const addToCartButton = renderResult.queryByTestId('show-cart-button');
    if (addToCartButton){
      fireEvent.click(addToCartButton) 
      expect(addToCartButton).toHaveBeenCalledTimes(1);
    }
});
});
