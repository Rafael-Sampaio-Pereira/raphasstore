import { Button } from "@material-ui/core";
import React from "react";

// Types
import { CartItemType } from "../../App";

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
            <h3>{item.title}</h3>
            <h3>R$ {item.price}</h3>
            <p>{item.description}</p>
        </div>
        <Button onClick={() => handleAddToCart(item)}>
            Adicionar ao Carrinho
        </Button>
    </Wrapper>
);

export default Item;