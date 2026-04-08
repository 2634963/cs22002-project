//Cookies for the Cooked

function createCookie(name, value, days){
    console.log("create cookie function called");

    const cook = new date();
    cook.setTime(cook.getTime() + (days * 24 * 60 * 60 * 1000));

    const expires = "expires=" + cook.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(pname){
    console.log("get cookie function called");

    let name = pname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i < ca.length; i++){
        let c = ca[i];
        while (c.charAt(0) == ' '){
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0){
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie(name){
    let username = getCookie(name);
    if (username != ""){
        alert(username);
    }

    else {
        username = prompt("Please enter your name:", "");
        if (username != "" && username != null){
            createCookie("usrename", username, 365);
        }
    }
}


checkCookie("username");





