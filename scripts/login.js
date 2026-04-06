// login script for admin login page

const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

//check against backend (eventually)
loginForm.addEventListener('submit', function(event) {
    event.preventDefault(); 
    const username = usernameInput.value;
    const password = passwordInput.value;

});