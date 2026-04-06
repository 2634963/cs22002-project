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

function createInfinitePosts() {
    for (let i = 0; i < 100; i++) {
        createNumberedPost();
    }
}