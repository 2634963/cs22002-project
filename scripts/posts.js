// Script to handle post display

// Display a specific post in the grid
async function displayPost(id, title, content, approval) {
    console.log("Displaying post '" + title + "'");

    let card = document.createElement("div");
    card.id = "card-" + id;
    card.classList.add("card");

    // Create content for card
    card.innerHTML = '<h2>' + title + '</h2> <p>' + content + '</p>';

    if(approval) {
        card.innerHTML += '<button class="approve-button" onclick="setPostApproval(' + id + ', true)">Approve</button> <button class="deny-button" onclick="setPostApproval(' + id + ', false)">Deny</button> <div class="admin-card-footer">Posted by ID: ' + id + '</div>';
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

async function setPostApproval(id, approved) {
    // TODO: Use UPDATE
    const approveResponse = await fetch("/api/adminSetPostApproval?postId=" + id + "&approved=" + (approved ? 1 : 0));

    if(!(await approveResponse.ok)) {
        console.log("Error: failed to set post approval for post " + id + "\nReason: " + await approveResponse.text());
    }
    else {
        document.getElementById("card-" + id).remove();
    }
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
            displayPost(posts[i].postId, posts[i].title, posts[i].content, true)
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
