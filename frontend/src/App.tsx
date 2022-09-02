import GlobalStyle from './Styles/global';
import NavBar from './Components/NavBar';
import { ThemeProvider } from "@material-ui/core/styles";
import { theme } from './Styles/theme';

function App() {
    return (
    <>
        <ThemeProvider theme={theme}>
            <GlobalStyle />
            <NavBar />
        </ThemeProvider>
    </>
    );
}

export default App;

