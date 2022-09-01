import styled from "styled-components";
import { IconButton } from "@material-ui/core";

export const Wrapper = styled.div`
    
    margin-left: 60px;
    margin-right: 60px;

    .header-banner {
        padding-bottom: 40px;
        text-align: center;

        img {
            padding-top: 100px;
            max-width:100% !important;
        }
    }
    
    .bottom-banner {
        padding-bottom: 40px;
        text-align: center;

        img {
            padding-top: 100px;
            max-width:100% !important;
        }
    }
`;

export const StyledButton = styled(IconButton)`
    position: fixed;
    z-index: 1000;
    right: 20px;
    top: 100px
`;