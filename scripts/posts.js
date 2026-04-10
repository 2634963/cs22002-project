// Script to handle post display

// Display a specific post in the grid
async function displayPost(id, title, content, approval) {
    console.log("Displaying post '" + title + "'");

    let card = document.createElement("div");
    card.classList.add("card");

    // Create content for card
    card.innerHTML = '<h2>' + title + '</h2> <p>' + content + '</p>';

    if(approval) {
        card.innerHTML += '<button class="approve-button" onclick="approve(this)">Approve</button> <button class="deny-button" onclick="deny(this)">Deny</button> <div class="admin-card-footer">Posted by ID: ' + id + '</div>';
    }

    card.innerHTML += '<button class="comment-button" onclick="showComments(' + id + ')">Comments</button>';

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
            displayPost(posts[i].postId, posts[i].title, posts[i].content, false)
        }
    }
}

async function approvePost(id) {

}

// Display posts for approval (admin)
async function loadPostsForApproval() {
    console.log("Loading posts for approval")

    // GET posts
    const postsResponse = await fetch("/api/adminViewPostApprovalList");

    if(!(await postsResponse.ok)) {
        // For some reason the endpoint did not succeed, error
        console.log("Failed to retrieve posts from /adminViewPostApprovalList endpoint");
    }
    else {
        console.log("Got posts from /adminViewPostApprovalList endpoint");
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
            displayPost(posts[i].postId, posts[i].title, posts[i].content, false)
        }
    }
}

// Display the comments for a specific post
async function showComments(id) {
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
