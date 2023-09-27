import React, {useState} from "react";

export interface ErrorMessages{
    name?: string,
    message?: string
}
export interface UserLogin{
    username?: string,
    password?: string,
    role?: string
}

export interface LoginProps{
    setUserLoginCallback : (data: UserLogin) => void
}

const Login : React.FC<LoginProps> = ({setUserLoginCallback}) => {

    // React States
    const [errorMessages , setErrorMessages] = useState<ErrorMessages>({});
    const [isSubmitted, setIsSubmitted] = useState(false);

    // User Login info
    const database = [
        {
            username: "user1",
            password: "pass1",
            role: "admin"
        },
        {
            username: "user2",
            password: "pass2",
            role: "admin"

        },
        {
            username: "user3",
            password: "pass3",
            role: "user"

        },
        {
            username: "user4",
            password: "pass4",
            role: "user"

        },
        {
            username: "user5",
            password: "pass5",
            role: "admin"

        },
        {
            username: "user6",
            password: "pass6",
            role: "user"

        }
    ];

    const errors = {
        uname: "Invalid Username!",
        pass: "Invalid Password!"
    };

    const handleSubmit = (event : any) => {
        //Prevent page reload
        event.preventDefault();

        let { uname, pass } = document.forms[0];

        // Find user login info
        const userData = database.find((user) => user.username === uname.value);

        // Compare user info
        if (userData) {
            if (userData.password !== pass.value) {
                // Invalid password
                setErrorMessages({ name: "pass", message: errors.pass });
            } else {
                setIsSubmitted(true);
                console.log("Authentication successful!")
                setUserLoginCallback(userData);
            }
        } else {
            // Username not found
            setErrorMessages({ name: "uname", message: errors.uname });
        }
    };

    // Generate JSX code for error message
    const renderErrorMessage = (name : any) =>
        name === errorMessages.name && (
            <div className="error">{errorMessages.message}</div>
        );

    // JSX code for login form
    return (
        <div className="form">
            <form onSubmit={handleSubmit}>
                <div className="input-container">
                    <label>Username </label>
                    <input type="text" name="uname" required />
                    {renderErrorMessage("uname")}
                </div>
                <div className="input-container">
                    <label>Password </label>
                    <input type="password" name="pass" required />
                    {renderErrorMessage("pass")}
                </div>
                <div className="button-container">
                    <input type="submit" />
                </div>
            </form>
        </div>
    );

}

export default Login;