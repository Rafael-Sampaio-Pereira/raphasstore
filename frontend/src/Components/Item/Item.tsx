import { Button } from "@material-ui/core";
import React from "react";

// Types
import { CartItemType } from '../../Resources/Types';

// Styles
import { Wrapper } from "./Item.styles";

type Props = {
    item: CartItemType;
    handleAddToCart: (clickedItem: CartItemType) => void;
}

const Item: React.FC<Props> = ({ item, handleAddToCart }) => (
    <Wrapper>
        <img src={item.image} alt={item.title} />
        <div>
            <p className="title">{item.title}</p>
            <p className="price">R$ {item.price}</p>
            <p>{item.description}</p>
        </div>
        <Button onClick={() => handleAddToCart(item)}>
            Adicionar ao Carrinho
        </Button>
    </Wrapper>
);

export default Item;