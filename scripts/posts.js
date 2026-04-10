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

        // Display each post
        for(const [key, post] of Object.entries(posts)) {
            displayPost(post.postId, post.title, post.content, false);
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

        // Display each post
        for(const [key, post] of Object.entries(posts)) {
            displayPost(post.postId, post.title, post.content, true);
        }
    }
}

// Display the comments for a specific post
async function showComments(id) {
    console.log('Comment button pressed ' + id );

    //fetchg commetns 
    const commentDict = await fetch("/api/viewPostWithComments?postId=" + id);

    console.log(commentDict.keys);

    if (!(await commentDict.ok)) {
        console.log(commentDict);
        console.log("Failed to load comments")
    }
    else {
        const commentsJson = JSON.parse(await commentDict.text());
        console.log(commentsJson)
        console.log("comments: " + id + ": " + JSON.stringify(commentsJson));
        
        const commentsContainer = document.getElementById("comments");
        commentsContainer.innerHTML = "";
        document.getElementById("commentPostId").value = id;

        // if no comments exist
        if (Object.keys(commentsJson).length === 0) {
            const commentDiv = document.createElement("div");
            commentDiv.className = "comment";
            commentDiv.textContent = "There are no comments yet :(";
            commentsContainer.appendChild(commentDiv);
        } 
        //append all to modal conteainer
        else {
            for (const [key, comment] of Object.entries(commentsJson)) {
                const commentDiv = document.createElement("div");
                commentDiv.className = "comment";
                commentDiv.textContent = comment.content;
                commentsContainer.appendChild(commentDiv);
            }
        }
    }
    
    let modal = document.getElementById("commentModal");
    let span = document.getElementsByClassName("close")[0];

    modal.style.display = "block";

    if (span) {
        span.onclick = function() {
            modal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    const commentSubmitButton = document.getElementById("commentSubmitButton");
    commentSubmitButton.onclick = function() {
        createPostComment(id);
    };

}

async function createPostComment(id) {
    console.log("Create comment button presserd")

    //get comment text from 
    const commentInput = document.getElementById("commentPoster");
    const commentText = commentInput.value;
    const postId = id;

    console.log(postId);
    console.log(commentText);

    //go to back end
    const res = await fetch("/api/postComment?postId=" + postId + "&content=" + encodeURIComponent(commentText));

    if (!(await res.ok)) {
        console.log("comment wasnt made")
    } else {
        console.log("comment was made "  + commentText)
    }
}

// Display comments for approval (admin)
async function loadCommentsForApproval() {
    console.log("Loading comments for approval")

    // GET coments
    const commentsResponse = await fetch("/api/adminViewCommentApprovalList");

    if(!(await commentsResponse.ok)) {
        // For some reason the endpoint did not succeed, error
        console.log("Failed to retrieve posts from /adminViewPostApprovalList endpoint");
    }
    else {
        console.log("Got comments from /adminViewPostApprovalList endpoint");
        const comments = JSON.parse(await postsResponse.text());

        // Display each post
        for(const [key, comment] of Object.entries(comments)) {
            displayPost(comment.postId, comment.title, comment.content, true);
        }
    }
}