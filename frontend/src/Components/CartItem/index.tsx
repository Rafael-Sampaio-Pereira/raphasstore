import { Button } from "@material-ui/core";

// Types
import { CartItemType } from '../../Resources/Types';

// Styles
import { Wrapper } from "./styles";

// Images
import DefaultShirt from '../../assets/images/default_shirt.png'

type Props = {
    item: CartItemType;
    addToCart: (clickedItem: CartItemType) => void;
    removeFromCart: (id: number) => void;
}

const CartItem: React.FC<Props> = ({ item, addToCart, removeFromCart}) => (
    <Wrapper>
        <div>
            <h3>{item.title}</h3>
            <div className="information">
                <p>Preço R$ {item.price}</p>
                <p>Total: R$ {(item.amount * item.price).toFixed(2)}</p>
            </div>
            <div className="buttons">
                <Button
                    color="primary"
                    size="small"
                    disableElevation
                    variant="contained"
                    onClick={() => removeFromCart(item.id)}
                >
                    -
                </Button>
                <p>{item.amount}</p>
                <Button
                    color="primary"
                    size="small"
                    disableElevation
                    variant="contained"
                    onClick={() => addToCart(item)}
                >
                    +
                </Button>
            </div>
        </div>
        <img src={item.image ? item.image : DefaultShirt} alt={item.title} /> 
    </Wrapper>
)

export default CartItem;