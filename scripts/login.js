// login script for admin login page

console.log("Login script loaded");

const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

//check against backend (eventually)
loginForm.addEventListener('login', function(event) {
    event.preventDefault(); 
    const username = usernameInput.value;
    const password = passwordInput.value;

    console.log('Username:', username);
    console.log('Password:', password);

    location.replace("/pages/adminDashboard.html");

});

//create login function
function login() {
    const username = usernameInput.value;
    const password = passwordInput.value;

    console.log('Username:', username);
    console.log('Password:', password);

    location.replace("/pages/adminDashboard.html");
}