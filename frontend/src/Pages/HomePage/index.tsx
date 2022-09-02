import { useState } from 'react'
import {useQuery, QueryClient, QueryClientProvider } from 'react-query'

// Components
import Item from '../../Components/Item';
import Cart from '../../Components/Cart';
import { Drawer } from '@material-ui/core';
import { LinearProgress } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import { AddShoppingCart } from '@material-ui/icons';
import Badge from '@material-ui/core/Badge';
import Divider from '@mui/material/Divider';
import Footer from '../../Components/Footer';

// Styles
import { Wrapper, StyledButton } from './styles';

// Services
// import api from '../../Services/fakestoreapi';
import api from '../../Services/api';

// Types
import { CartItemType } from '../../Resources/Types';

// Images
import HeaderBanner from '../../assets/images/header_banner.png'
import BottomBanner from '../../assets/images/bottom_banner.png'

const getProducts = async (): Promise<CartItemType[]> =>
    api
      .get('/product/all')
      .then(response => {
          return response.data
      });

const queryClient = new QueryClient()

const HomePage: React.FC = () => {
  const [cartOpen, setCartOpen] = useState(false);
  const [cartItems, setCartItems] = useState([] as CartItemType[]);
  const { data, isLoading, error } = useQuery<CartItemType[]>(
    'products',
    getProducts
  )
  const getTotalItems = (items: CartItemType[]) =>
    items.reduce((ack: number, item) => ack + item.amount, 0)
  const handleAddToCart = (clickedItem: CartItemType) => {
    setCartItems(prev => {
      // 1. Is the item already added in the cart?
      const isItemInCart = prev.find(item => item.id === clickedItem.id)

      if (isItemInCart) {
        return prev.map(item => 
          item.id === clickedItem.id
            ? { ...item, amount: item.amount + 1 }
            : item
        );
      }
      // First time the item is added
      return [ ...prev, { ...clickedItem, amount: 1}]
    })
  };
  const handleRemoveFromCart = (id: number) => {
    setCartItems(prev =>(
      prev.reduce((ack, item) => {
        if (item.id === id) {
          if(item.amount === 1) return ack;
          return [...ack, { ...item, amount: item.amount - 1}];
        }else {
          return [...ack, item];
        }
      }, [] as CartItemType[])
    ))
  };

  if (isLoading) return <LinearProgress/>;
  if (error) return <div>Ops, houve um erro inesperado ...</div>

  return (
    <QueryClientProvider client={queryClient} contextSharing={true}>
      <Wrapper>
        <Drawer anchor='right' open={cartOpen} onClose={() => setCartOpen(false)}>
          <Cart 
            cartItems={cartItems}
            addToCart={handleAddToCart}
            removeFromCart={handleRemoveFromCart}
          />
        </Drawer>
        <StyledButton data-testid='show-cart-button' color='secondary' size='medium' onClick={() => setCartOpen(true)}>
          <Badge overlap='rectangular' badgeContent={getTotalItems(cartItems)} color='error'>
            <AddShoppingCart fontSize='large' />
          </Badge>
        </StyledButton>
        <Grid container spacing={3}>
            <Grid item className='header-banner' data-testid='header-banner' key='header_banner' xl={12} lg={12} md={12} sm={12} xs={12}>
              <img src={HeaderBanner} alt='RaphasStore. Sua camiseta Sport está aqui!' />
            </Grid>
            <Grid item key='serach_area' xl={12} lg={12} md={12} sm={12} xs={12}>
              <Divider />
            </Grid>
          {data?.map(item => (
            <Grid item key={item.id} xl={2} lg={2} md={4} sm={6} xs={12}>
              <Item item={item} data-testid={`product-${item.id}`} handleAddToCart={handleAddToCart}/>
            </Grid>
          ))}
          <Grid item className='bottom-banner' data-testid="bottom-banner" key='bottom_banner' xl={12} lg={12} md={12} sm={12} xs={12}>
              <img src={BottomBanner} alt='RaphasStore. Sua camiseta Sport está aqui!' />
          </Grid>
          <Grid item key='serach_area' xl={12} lg={12} md={12} sm={12} xs={12}>
              <Divider />
          </Grid>
          <Footer />
        </Grid>
      </Wrapper>
    </QueryClientProvider>
  );
}

export default HomePage;
