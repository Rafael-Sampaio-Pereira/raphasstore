import styled from "styled-components";
import { IconButton } from "@material-ui/core";

export const Wrapper = styled.div`
    margin: 40px;

    .header-banner {
        padding-bottom: 40px;
        text-align: center;
    }
`;

export const StyledButton = styled(IconButton)`
    position: fixed;
    z-index: 100;
    right: 20px;
    top: 20px
`;