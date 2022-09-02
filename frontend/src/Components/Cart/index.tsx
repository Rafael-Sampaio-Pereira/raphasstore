import CartItem from "../CartItem";

// Styles
import { Wrapper } from "./styles";

// Types
import { CartItemType } from '../../Resources/Types';

type Props = {
    cartItems: CartItemType[];
    addToCart: (clickedItem: CartItemType) => void;
    removeFromCart: (id: number) => void;
}

const Cart: React.FC<Props> = ({ cartItems, addToCart, removeFromCart }) => {
const calculateTotal = (items: CartItemType[]) =>
    items.reduce((ack: number, item) => ack + item.amount * item.price, 0)

    return (
        <Wrapper>
            <p className="cart-title">Seu Carrinho</p>
            {cartItems.length === 0 ? <p>Não há itens no carrinho.</p> : null}
            {cartItems.map(item => (
                <CartItem 
                    key={item.id}
                    item={item}
                    addToCart={addToCart}
                    removeFromCart={removeFromCart}
                />
            ))}
            <h2>Total R$ {calculateTotal(cartItems).toFixed(2)}</h2>
        </Wrapper>
    )
}

export default Cart;