import React, {createContext, useContext, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import {HashRouter, Route, Routes} from "react-router-dom";
import VideoGames from "./Pages/VideoGames";
import Filter from "./Pages/Filter";
import Login from "./Pages/Login";

export interface UserLogin {
    username?: string,
    password?: string
    role?: string
}

function App() {
    const LoginContext = createContext<UserLogin>({username: "", password: ""});
    const LoginMode = useContext(LoginContext);
    const [userLogin, setUserLogin] = useState(LoginMode)

    const handleUserLogin = (u: UserLogin) => {
        setUserLogin(u);
    }

    return (
        <LoginContext.Provider value={userLogin}>
            {JSON.stringify(userLogin) !== JSON.stringify({username: '', password: ''}) ?
                <HashRouter>
                    <div>{userLogin.username} : {userLogin.role}</div>
                    <Routes>
                        <Route path="/" Component={VideoGames}/>
                        <Route path="/videogames" Component={VideoGames}/>
                        <Route path="/platforms" Component={VideoGames}/>
                        <Route path="/savefiles" Component={VideoGames}/>
                        <Route path="/players" Component={VideoGames}/>
                        <Route path="/filter" Component={Filter}/>
                    </Routes>
                </HashRouter> : <Login setUserLoginCallback={(userData) => handleUserLogin(userData)}></Login>}
        </LoginContext.Provider>
    );
}

export default App;
