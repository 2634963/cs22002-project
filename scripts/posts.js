// Script to handle post display

let postCount = 0;

// Display a specific post in the grid
async function displayPost(id, title, content) {
    console.log("Displaying post '" + title + "'");
    console.log('This is post number ' + postCount++);

    let card = document.createElement("div");
    card.classList.add("card");

    // Create content for card
    card.innerHTML = '<h2>' + title + '</h2> <p>' + content + '</p> <button class="comment-button" onclick="showComments(' + id + ')">Comments</button>';

    // Append onto the grid
    let container = document.getElementById("cardContainer");
    container.appendChild(card);
}

// Display all posts
async function loadPosts() {
    console.log('Loading posts');

    // GET posts
    const postsResponse = await fetch("/api/viewPostList");

    if(!(await postsResponse.ok)) {
        // For some reason the endpoint did not succeed, error
        console.log("Failed to retrieve posts from /viewPostList endpoint");
    }
    else {
        console.log("Got posts from /viewPostList endpoint");
        const posts = JSON.parse(await postsResponse.text());

        // Determine post count
        let postCount = 0;

        for(let i = 0; i < Object.keys(posts).length; i++) {
            postCount += Object.keys(posts)[i].length;
        }

        console.log("Post count: " + postCount);

        // Display each post
        for(let i = 0; i < postCount; i++)
        {
            displayPost(i, posts[i].title, posts[i].content)
        }
    }
}

// Display the comments for a specific post
async function showComments() {
    console.log('Comment button pressed');

    let modal = document.getElementById("commentModal");
    let span = document.getElementsByClassName("close")[0];

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
