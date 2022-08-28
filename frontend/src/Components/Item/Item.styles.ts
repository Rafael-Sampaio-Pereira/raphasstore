import styled from 'styled-components';
import colors from '../../Styles/colors';

export const Wrapper = styled.div`
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    width: 100%;
    border: 1px solid #E0E0E0;
    border-radius: 20px;
    height: 100%;
    background: ${colors.background_secondary};

    button {
        border-radius: 0 0 20px 20px;
        background: ${colors.background_button};
        color: #FAFAFA;
    }

    .title {
        font-weight: bold;
        font-size: 20px;
        color: ${colors.font_titles};
        padding-bottom: 10px;
    }

    .price {
        font-weight: bold;
        color: ${colors.font_prices_primary};
        padding-bottom: 20px;
    }

    img {
        max-height: 250px;
        object-fit: cover;
        border-radius: 20px 20px 0 0;
    }

    div {
        font-family: Arial, Helvetica, sans-serif;
        padding: 1rem;
        height: 100%;
    }
`;