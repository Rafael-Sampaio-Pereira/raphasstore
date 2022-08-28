/* material shell also provide the colors we can import them like these */
import { green, orange } from "@material-ui/core/colors";

// these are for customizing the theme
import { createTheme } from "@material-ui/core/styles";

export const theme = createTheme({
    typography: {
        h1: {
            /* this will change the font size for h1, we can also do 
                it for others, */
            fontSize: "3rem",
        },
    },
    palette: {
        /* this is used to turn the background dark, but we have 
          to use Paper for this inOrder to use it. */
        // type: "dark",
        type: "light",
        primary: {
            // main: colorName[hue],
            // we have to import the color first to use it
            main: '#4A148C',
        },
        secondary: {
            main: orange[400],
        },
    },
});