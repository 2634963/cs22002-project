// login script for login page

console.log("Login script loaded");

const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    // Send login details to backend and store the response
    let loginResponseText = "";
    
    const loginResponse = await fetch("/api/login", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        method: "POST",
        body: JSON.stringify({username: username,
                              password: password})
    });

    if(!(await loginResponse.ok)) {
        // Login details were incorrect, error
        document.getElementById('error').textContent = "Error: " + await loginResponse.text();
    }
    else {
        // Send user to the main page
        console.log("Login successful");
        window.location.href = "/pages/main.html";
    }
});
