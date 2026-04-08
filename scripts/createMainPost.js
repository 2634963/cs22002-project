//Create post for dynamic container on dynamic main page

var postCount = 0;

function createPost() {
    console.log('Create Post Pressed');

    var card = document.createElement("div");
    card.classList.add("card");

    //Creat content for card
    var cardContent = '<h2>Title</h2> <p>Content</p>'
    ;

    card.innerHTML = cardContent;

    //append onto the grid
    var container = document.getElementById("cardContainer");
    container.appendChild(card);

}

function createNumberedPost() {
    console.log('Create Post Pressed');

    let postNumber = postCount + 1;
    let text = 'This is post number ' + postNumber;
    postCount++;

    var card = document.createElement("div");
    card.classList.add("card");

    //Creat content for card
    var cardContent = '<h2>' + text + '</h2> <p>Content</p>'
    ;

    card.innerHTML = cardContent;

    //append onto the grid
    var container = document.getElementById("cardContainer");
    container.appendChild(card);

}

function createPostWithComment() {
    console.log('Create Post Pressed');

    let postNumber = postCount + 1;
    let text = 'This is post number ' + postNumber;
    postCount++;

    var card = document.createElement("div");
    card.classList.add("card");

    //Creat content for card
    var cardContent = '<h2>' + text + '</h2> <p>Content</p> <button class="comment-button" onclick="comment()">Comments</button>'
    ;

    card.innerHTML = cardContent;

    //append onto the grid
    var container = document.getElementById("cardContainer");
    container.appendChild(card);
}

function createInfinitePosts() {
    for (let i = 0; i < 10; i++) {
        createNumberedPost();
    }
}

function loadPosts() {
    console.log('loading posts');

    fetch('127.0.0.1:5500/api/')
}

function comment () {
    console.log('Comment button pressed');

    var modal = document.getElementById("commentModal");
    var span = document.getElementsByClassName("close")[0];

    modal.style.display = "block";

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}