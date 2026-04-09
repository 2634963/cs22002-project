//sign up scripts

// Sign up script for login page

console.log("signup script loaded");

const loginForm = document.getElementById('signup-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    // Send sign up details to backend and store the response
    let signUpResponseText = "";

    const signupResponse = await fetch("/api/signup", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        method: "POST",
        body: JSON.stringify({username: username,
                              password: password})
    });

    if(!(await signupResponse.ok)) {
        // sign up details were already exist
        document.getElementById('error').textContent = "Error: " + await signupResponse.text();
    }
    else {
        // Inform the user that they were successfully registered
        console.log("Signup successful");
        document.getElementById('error').textContent = "";
        document.getElementById('success').textContent = "Signup successful!";
    }
});
