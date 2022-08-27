import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Sidebar from '../components/Sidebar';
import Header from '../components/Header';
import Homepage from '../pages/Homepage';
import Autocam from '../pages/Autopages/Autocam';
import Auto360 from '../pages/Autopages/Auto360';
import Autother from '../pages/Autopages/Autother';
import Automap from '../pages/Autopages/Automap';
import Historypage from '../pages/Historypage';
import Operadacam from '../pages/Operadapages/Operadacam';
import Stoppage from '../pages/Stoppage';
import Alertroundpage from '../pages/Alertroundpage';
import Operadamensagem from '../pages/Operadapages/Operadamensagem';
import Operada360 from '../pages/Operadapages/Operada360';
import Operadather from '../pages/Operadapages/Operadather';
import Operadamap from '../pages/Operadapages/Operadamap';
import Configcampage from '../pages/Configcampage';
import Configthermpage from '../pages/Configthermpage';
import Roundpage from '../pages/Roundpage';

import { Container } from './styles';

const Routes: React.FC = () => {
  return (
    <BrowserRouter>
      <Container>
        <Sidebar />
        <div id="page-container">
          <Header />
          <Switch>
            <Route exact path="/" component={Homepage} />
            <Route exact path="/auto" component={Autocam} />
            <Route exact path="/auto/360" component={Auto360} />
            <Route exact path="/auto/ther" component={Autother} />
            <Route exact path="/auto/mapa" component={Automap} />
            <Route exact path="/historico" component={Historypage} />
            <Route exact path="/operada" component={Operadacam} />
            <Route exact path="/stop" component={Stoppage} />
            <Route exact path="/alert-round" component={Alertroundpage} />
            <Route exact path="/operada/alerta" component={Operadamensagem} />
            <Route exact path="/operada/360" component={Operada360} />
            <Route exact path="/operada/ther" component={Operadather} />
            <Route exact path="/operada/mapa" component={Operadamap} />
            <Route exact path="/configure/cam" component={Configcampage} />
            <Route exact path="/configure/therm" component={Configthermpage} />
            <Route path="/ronda" component={Roundpage} />
            <Route path="/ronda/:id" component={Roundpage} />
          </Switch>
        </div>
      </Container>
    </BrowserRouter>
  );
};

export default Routes;
