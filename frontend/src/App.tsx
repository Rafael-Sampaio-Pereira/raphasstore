import GlobalStyle from './Styles/global';
import HomePage from './Pages/HomePage/HomePage';
import NavBar from './Components/NavBar/NavBar';
import { ThemeProvider } from "@material-ui/core/styles";
import { theme } from './Styles/theme';

function App() {
    return (
    <>
        <ThemeProvider theme={theme}>
            <GlobalStyle />
            <NavBar />
            {/* <HomePage /> */}
        </ThemeProvider>
    </>
    );
}

export default App;

