// Script to handle post display

// Display a specific post in the grid
async function displayPost(id, title, content, extraInfo, extraInfoPurchased, approval) {
    console.log("Displaying post '" + title + "'");

    let card = document.createElement("div");
    card.id = "card-" + id;
    card.classList.add("card");

    // Create content for card
    card.innerHTML = '<h2>' + title + '</h2> <p>' + content + '</p><p>Extra Info:</p><p>' + extraInfo + '</p>';

    if(approval) {
        card.innerHTML += '<button class="approve-button" onclick="setPostApproval(' + id + ', true)">Approve</button> <button class="deny-button" onclick="setPostApproval(' + id + ', false)">Deny</button> <div class="admin-card-footer">Posted by ID: ' + id + '</div>';
    }

    card.innerHTML += '<button class="comment-button" onclick="showComments(' + id + ')">Comments</button>';

    if(!extraInfoPurchased && !approval)
    {
        card.innerHTML += '<button class="comment-button" onclick="showExtraInfoModal(' + id + ')">Buy Extra Info</button>'
    }
    
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
            // GET extra info, if the user has access
            const extraInfoResponse = await fetch("/api/getExtraInformation?postId=" + post.postId);
            let extraInfoPurchased = (await extraInfoResponse.ok ? true : false);

            displayPost(post.postId, post.title, post.content, await extraInfoResponse.text(), extraInfoPurchased, false);
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
            const extraInfoResponse = await fetch("/api/getExtraInformation?postId=" + post.postId);
            let extraInfoPurchased = (await extraInfoResponse.ok ? true : false);

            displayPost(post.postId, post.title, post.content, await extraInfoResponse.text(), extraInfoPurchased, true);
        }
    }
}

//set comment approval
async function setCommentApproval(id, approved) {
    // TODO: Use UPDATE
    const approveResponse = await fetch("/api/adminGiveCommentApproval?commentId=" + id + "&approved=" + (approved ? 1 : 0));

    if(!(await approveResponse.ok)) {
        console.log("Error: failed to set post approval for post " + id + "\nReason: " + await approveResponse.text());
    }
    else {
        document.getElementById("card-" + id).remove();
    }
}

// Display a specific post in the grid
async function displayCommentPost(id, title, content) {
    console.log("Displaying post '" + id + "'");

    let card = document.createElement("div");
    card.id = "card-" + id;
    card.classList.add("card");

    // Create content for card
    card.innerHTML = '<h2>' + title + '</h2> <p>' + content + '</p>';

    card.innerHTML += '<button class="approve-button" onclick="setCommentApproval(' + id + ', true)">Approve</button> <button class="deny-button" onclick="setCommentApproval(' + id + ', false)">Deny</button> <div class="admin-card-footer">Comment ID: ' + id + '</div>';

    card.innerHTML += '<button class="comment-button" onclick="showComments(' + id + ')">Comments</button>';
    
    // Append onto the grid
    let container = document.getElementById("cardContainer");
    container.appendChild(card);
}

// Display comments for approval (admin)
async function loadCommentsForApproval() {
    console.log("Loading Comments for approval")

    // GET comments
    const commentsResponse = await fetch("/api/adminViewCommentApprovalList");

    if(!(await commentsResponse.ok)) {
        // For some reason the endpoint did not succeed, error
        console.log("Failed to retrieve Comments from /adminViewCommentsApprovalList endpoint");
    }
    else {
        console.log("Got Comments from /adminViewCommentsApprovalList endpoint");
        const comments = JSON.parse(await commentsResponse.text());

        // Display each comment
        for(const [key, comment] of Object.entries(comments)) {
            let com = "comment"
            console.log(comment.commentId)
            displayCommentPost(comment.commentId, com, comment.content);
        }
    }
}

// Display posts for approval (admin)
async function loadCommentsForApproval2() {
    console.log("Loading posts for approval")

    // GET posts
    const postsResponse = await fetch("/api/adminViewCommentApprovalList");

    if(!(await postsResponse.ok)) {
        // For some reason the endpoint did not succeed, error
        console.log("Failed to retrieve posts from /adminViewPostApprovalList endpoint");
    }
    else {
        console.log("Got posts from /adminViewPostApprovalList endpoint");
        const posts = JSON.parse(await postsResponse.text());

        // Display each post
        for(const [key, post] of Object.entries(posts)) {
            console.log(post.postId)
            displayCommentPost(post.postId, post.content, post.content);
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
    let span = document.getElementById("closeCommentModal");

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

// Display the purchase modal
async function showExtraInfoModal(id) {
    console.log('Purchase model displayed for post ' + id);

    let modal = document.getElementById("extraInfoModal");
    let span = document.getElementById("closeExtraInfoModal");

    modal.style.display = "block";

    // Set submit function to use purchase info for current post ID
    document.getElementById("extraInfoForm").addEventListener('submit', async function(event) {
        event.preventDefault();
        document.getElementById('purchaseError').textContent = "";

        // Send card details to backend and store the response
        const purchaseResponse = await fetch("/api/purchaseExtraInformation", {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },

            method: "POST",
            body: JSON.stringify({postId: id,
                                  cardNumber: document.getElementById('cardNumber').value,
                                  expireMonth: document.getElementById('expireMonth').value,
                                  expireYear: document.getElementById('expireYear').value,
                                  ccv: document.getElementById('ccv').value})
        });

        if(!(await purchaseResponse.ok)) {
            document.getElementById('purchaseError').textContent = "Error: " + await purchaseResponse.text();
        }
        else {
            console.log("Purchase successful");
            window.location.href = "/pages/main.html";
        }
    });

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
}
