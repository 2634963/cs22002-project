postForm.addEventListener('submit', async function(event) {
    // HTML forms don't send JSON, so suppress it and do it ourselves
    event.preventDefault();

    // POST the post :D
    const postResponse = await fetch("/api/createPost", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        method: "POST",
        body: JSON.stringify({title: document.getElementById("title").value,
                              content: document.getElementById("content").value,
                              extraInfo: document.getElementById("extraInfo").value})
    });

    if(!(await postResponse.ok)) {
        document.getElementById('error').textContent = "Error: " + await postResponse.text();
    }
    else {
        console.log("POST post post successful! :D");
        document.getElementById('error').textContent = "";
        document.getElementById('success').textContent = "Post added to moderation queue!"
    }
});


//create comment
async function createComment(id, content) {
    console.log('Creating comment for post ' + id + ' with content: ' + content);

    // POST the comment
    const commentResponse = await fetch("/api/postComment", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({postId: id, content: content})
    });

    if (commentResponse.ok) {
        console.log("Comment posted successfully!");
        // Optionally refresh comments or update UI
    } else {
        console.error("Failed to post comment: " + await commentResponse.text());
    }
}
async function showComments(id) {
    console.log('Comment button pressed for post ' + id);

    let modal = document.getElementById("commentModal");
    let span = document.getElementsByClassName("close")[0];
    let button = document.getElementById("commentSubmitButton");

    // Fetch existing comments from database
    const commentsResponse = await fetch("/api/viewPostWithComments?postId=" + id);
    
    if (commentsResponse.ok) {
        const comments = await commentsResponse.json();
        const commentsArray = Object.values(comments);
        console.log("Loaded " + commentsArray.length + " comments");
        
        //llog existing comments
        console.log("Comments for post " + id + ":");
        commentsArray.forEach(comment => {
            console.log("- " + comment.content);
        });
        
        //dsplay existing comments
        let commentsHtml = '';
        if (commentsArray.length === 0) {
            commentsHtml = '<p>nada comments</p>';
        } else {
            for (let comment of commentsArray) {
                commentsHtml += '<div class="comment"><p>' + comment.content + '</p></div>';
            }
        }
        
        document.getElementById("comments").innerHTML = commentsHtml;
    } else {
        console.error("failed to load comments");
    }

    button.onclick = function() {
        let content = document.getElementById("commentPoster").value;
        if (content.trim()) {
            createComment(id, content);
            //removes modal so you can refersh it (prefer it over thingy refersh)
            modal.style.display = "none";
        }
    }

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
