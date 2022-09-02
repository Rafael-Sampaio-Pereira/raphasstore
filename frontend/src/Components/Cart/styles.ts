import styled from "styled-components";
import colors from "../../Styles/colors";

export const Wrapper = styled.aside`
    font-family: Arial, Helvetica, sans-serif;
    width: 500px;
    padding: 20px;

    .cart-title {
        font-weight: bold;
        font-size: 25px;
        color: ${colors.font_titles};
        padding-bottom: 10px;
    }
`;