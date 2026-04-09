//sign up scripts

// Sign up script for login page

console.log("sing up script loaded");

const loginForm = document.getElementById('signup-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    // Send sign up details to backend and store the response
    let signUpResponseText = "";
    
    const signupResponse = await fetch("/api/signup.py", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        method: "POST",
        body: JSON.stringify({username: usernameInput,
                              password: passwordInput})
    });

    if(!(await signupResponse.ok)) {
        // sign up details were already exist
        document.getElementById('error').textContent = " username already exists";
    }
    else {
        console.log("Sign Up successful");

        let signUpResponseText = await signupResponse.text();

        const element = document.getElelmentById('signup-id');
        element.remove();
    }
});