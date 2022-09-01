import {
    Typography,
    Grid,
    Link
} from "@material-ui/core";
import {
    Security,
    Info
} from "@material-ui/icons";

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import ListSubheader from '@mui/material/ListSubheader';

import { Wrapper } from './AboutPage.styles';

const AboutPage = () => {

    return (
        <Wrapper>
            <Grid container justify="center" style={{minHeight: "212px"}}>
                <Grid container item sm={6} xs={11} justify="space-between">
                    <Grid item sm={5} xs={12}>
                        <Security color="action" />
                        <Typography paragraph>
                            Esta aplicação faz parte de um desafio de 7 dias cumprido por Rafael Sampaio durante processo seletivo para ingresso na Dafiti.
                        </Typography>
                    </Grid>
                    <Grid item sm={5} xs={11}>
                        <Info color="action" />
                        <Typography paragraph>
                            Encontre mais projetos do autor em seu repositorio oficial no <Link href="https://github.com/Rafael-Sampaio-Pereira/" target="_blank">github</Link>.
                        </Typography>
                    </Grid>
                    <Grid item sm={5} xs={11}>
                        <Typography paragraph>
                            <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
                                <Divider />
                                <nav aria-label="main mailbox folders">
                                    <List
                                        aria-labelledby="main-tecs"
                                        subheader={
                                        <ListSubheader component="div" id="main-tecs">
                                            Principais tecnologias empregadas (Backend):
                                        </ListSubheader>
                                        }
                                    >
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Python" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Django" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Django Rest Framework" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="JWT" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Gunicorn" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="CoreAPI" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Docker" />
                                            </ListItemButton>
                                        </ListItem>
                                    </List>
                                </nav>
                            </Box>
                        </Typography>
                    </Grid>
                    <Grid item sm={5} xs={11}>
                        <Typography paragraph>
                            <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
                                <Divider />
                                <nav aria-label="main mailbox folders">
                                    <List
                                        aria-labelledby="main-tecs"
                                        subheader={
                                        <ListSubheader component="div" id="main-tecs">
                                            Principais tecnologias empregadas (Frontend):
                                        </ListSubheader>
                                        }
                                    >
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Javascript" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Reactjs" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Styled-components" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="React-router-dom" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Material UI" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="Nginx" />
                                            </ListItemButton>
                                        </ListItem>
                                        <ListItem disablePadding>
                                            <ListItemButton>
                                            <ListItemText primary="TypeScript" />
                                            </ListItemButton>
                                        </ListItem>
                                    </List>
                                </nav>
                            </Box>
                        </Typography>
                    </Grid>
                </Grid>
            </Grid>
        </Wrapper>
    );
}

export default AboutPage;
