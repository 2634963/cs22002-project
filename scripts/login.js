// login script for admin login page

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
        body: JSON.stringify({username: usernameInput,
                              password: passwordInput})
    });

    if(!(await loginResponse.ok)) {
        // Login details were incorrect, error
        document.getElementById('error').textContent = "Invalid username or password.";
    }
    else {
        console.log("Login successful");

        let loginResponseText = await loginResponse.text();

        // Store session token in a cookie
        document.cookie = "sessionToken=" + loginResponseText;

        // Load admin dashboard
        window.location.href = "/pages/admin/adminDashboard.html";
    }
});
