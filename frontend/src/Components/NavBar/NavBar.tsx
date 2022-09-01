import React from 'react';
import {
    AppBar,
    Toolbar,
    IconButton,
    Typography,
    useMediaQuery,
    Button,
    Menu,
    MenuItem,
    ListItemIcon
} from '@material-ui/core';

import { makeStyles, Theme, useTheme } from '@material-ui/core/styles';
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';

import MenuIcon from '@material-ui/icons/Menu';
import HomeIcon from '@material-ui/icons/Home';
// import SchoolIcon from '@material-ui/icons/School';
import PersonIcon from '@material-ui/icons/Person';
import { ReactComponent as Logo } from '../../assets/images/logo.svg'

import HomePage from '../../Pages/HomePage/HomePage';
// import ContactPages from '../../Pages/ContactsPage/ContactsPage';
import AboutPage from '../../Pages/AboutPage/AboutPage';

// styles
const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1
    },
    menuButton: {
        marginRight: theme.spacing(2)
    },
    title: {
        flexGrow: 1,
        color: 'white'
    }
}));



const NavBar = (props: any) => {
    const classes = useStyles();
    const [anchor, setAnchor] = React.useState(null);
    const open = Boolean(anchor);
    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
    const handleMenu = (event: any) => {
    setAnchor(event.currentTarget);
    };
    return (
    <div className={classes.root}>
        <BrowserRouter>
            <AppBar>
            <Toolbar>
                <IconButton 
                    size='medium'
                    edge='start'
                    color='inherit'
                    aria-label='logo'
                    component={Link}
                    to='/'
                >
                    <Logo fill='white' height={70} width={70} />
                </IconButton>
                <Typography
                    variant='h5'
                    component='p'
                    color='textSecondary'
                    className={classes.title}
                >
                    RaphasStore
                </Typography>
                {isMobile ? (
                <>
                    <IconButton
                        color='secondary'
                        className={classes.menuButton}
                        edge='start'
                        aria-label='menu'
                        onClick={handleMenu}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Menu
                        id='menu-appbar'
                        anchorEl={anchor}
                        anchorOrigin={{
                            vertical: 'top',
                            horizontal: 'right'
                        }}
                        keepMounted
                        transformOrigin={{
                            vertical: 'top',
                            horizontal: 'right'
                        }}
                        open={open}
                    >
                        <MenuItem
                            onClick={() => setAnchor(null)}
                            component={Link}
                            to='/'
                        >
                            <ListItemIcon>
                                <HomeIcon />
                            </ListItemIcon>
                            <Typography variant='h6'> Home</Typography>
                        </MenuItem>
                        <MenuItem
                            onClick={() => setAnchor(null)}
                            component={Link}
                            to='/About'
                        >
                            <ListItemIcon>
                                <PersonIcon />
                            </ListItemIcon>
                            <Typography variant='h6'> About</Typography>
                        </MenuItem>
                    </Menu>
                </>
                ) : (
                <div style={{ marginRight: '2rem' }}>
                    <Button
                    variant='text'
                    component={Link}
                    to='/'
                    color='inherit'
                    >
                    <HomeIcon />
                    Home
                    </Button>
                    <Button
                    variant='text'
                    component={Link}
                    to='/About'
                    color='inherit'
                    >
                    <PersonIcon />
                    About
                    </Button>
                </div>
                )}
            </Toolbar>
            </AppBar>
            <Routes>
                <Route path='/' element={<HomePage />} />
                <Route path='/about' element={<AboutPage />} />
            </Routes>
        </BrowserRouter>
    </div>
    );
};

export default NavBar;