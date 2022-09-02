import React from 'react';
import { render, act, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import MockAdapter from 'axios-mock-adapter';
import api from '../../Services/api';
import {useQuery, QueryClient, QueryClientProvider } from 'react-query'
import AboutPage from '../../Pages/AboutPage';

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
describe('Test About Page', () => {
  it('should be testing AboutPage', async () => {
    const renderResult = render(
      <Router>
          <AboutPage />
      </Router>,
    );

    expect(renderResult.queryByText('Principais tecnologias empregadas (Backend):')).toBeInTheDocument;
    expect(renderResult.queryByText('Principais tecnologias empregadas (Frontend):')).toBeInTheDocument;
});
});
