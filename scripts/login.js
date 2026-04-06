// login script for admin login page

console.log("Login script loaded");

//connect to james api
fetch('http://127.0.0.1:5500/api/log?message=hello');

const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

//check against backend (eventually)
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    console.log('Username:', username);
    console.log('Password:', password);

    window.location.href = "/pages/admin/adminDashboard.html";
});

//create login function
function login() {
    const username = usernameInput.value;
    const password = passwordInput.value;

    console.log('Username:', username);
    console.log('Password:', password);

    window.location.href = "/pages/admin/adminDashboard.html";
}