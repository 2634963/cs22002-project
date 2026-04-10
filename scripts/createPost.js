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
