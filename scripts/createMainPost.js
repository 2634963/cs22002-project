//Create post for dynamic container on dynamic main page

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