import {
    AppBar,
    Toolbar,
    Typography,
    Grid,
    Link
} from "@material-ui/core";
import {
    Security,
    Info
} from "@material-ui/icons";

const Footer = () => <>
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
            </Grid>
        </Grid>
        <AppBar position="static" elevation={0} component="footer" color="default">
            <Toolbar style={{ justifyContent: "center" }}>
                <Typography variant="caption">©2020 - Rafael Sampaio</Typography>
            </Toolbar>
        </AppBar>
    </>

export default Footer;