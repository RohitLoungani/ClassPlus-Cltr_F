
import React, { useEffect, useState } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';


//BOOTSTRAP
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';

import './App.css';
import Login from './components/Login.js';
import Register from './components/Register.js';
import Checks from './components/Checks.js';
import Verify from './components/Verify.js';
import Lecture from './components/Lecture.js';
import { Button } from 'reactstrap';


function App() {
  return (
    <Container fluid style={{ padding: '0px' }}>
      <BrowserRouter>
        <Switch>
          <Route exact path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/check" component={Checks} />
          <Route path="/verify" component={Verify} />          
          <Route path="/lecture" component={Lecture} />          
          <Route component={Login} />
        </Switch>
      </BrowserRouter>
    </Container>
    // <div className="App">
    //   <Login/>
    //   {/* <Register /> */}
    // </div>
  );
}

export default App;
