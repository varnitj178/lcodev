import React from "react"
import {BrowserRouter,Switch,Route} from "react-router-dom";
import PrivateRoutes from "./auth/helper/privateroutes";
import Home from "./core/Home";
import Signin from "./user/Signin";
import Signup from "./user/Signup";

import UserDashboard from "./user/UserDasboard"

const Routes = () =>{
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component ={Home} /> 
                <Route path="/signup" exact component ={Signup} /> 
                <Route path="/signin" exact component ={Signin} /> 
             <PrivateRoutes path ="/user/dashboard" exact component={UserDashboard}/>   
            </Switch>
        </BrowserRouter>
    )
}

export default Routes;