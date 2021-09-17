import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
    render() {
        return (

            <
            div class = "login-page" >
            <
            div class = "form" >
            <
            div class = "login" >
            <
            div class = "login-header" >
            <
            h3 > LOGIN < /h3>  <
            p > Please enter your credentials to login. < /p> < /
            div > < /div> <form class = "login-form"  method ='POST' action ='login'> <
            input type = "text"
            placeholder = "username"
            name = 'username' / >
            <
            input type = "password"
            placeholder = "password"
            name = 'password' / >
            <
            button type = 'submit' > login < /button> <
            p class = "message" > Not registered ? < a href = "#" > Create an account < /a></p >
            <
            /form> < /
            div > <
            /div>
        );
    }

}
export default App;