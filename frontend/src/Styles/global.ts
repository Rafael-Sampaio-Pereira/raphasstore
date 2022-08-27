import { createGlobalStyle } from 'styled-components';
import colors from './colors';

export default createGlobalStyle`

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    outline: 0;
    font-family: 'Red Hat Text', sans-serif;
  }
  
  body {
    
    -webkit-font-smoothing: antialiased;
    background: ${colors.background_primary};
    color: ${colors.font_primary_color};

  }

  h1, h2, h3, h4, h5, h6, strong {
    font-weight: 500;
  }
  button {
    outline: none;
    border: none;

    font-size: 18px;

    cursor: pointer;
  }
  
  a {
    text-decoration: none;
  }

  ::-webkit-scrollbar {
        width: 10px
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
        background: #888;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
`;