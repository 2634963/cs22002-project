//Create post JS for post.html

//get element form
const postForm = document.getElementById('postForm');

//event listener for form submission
postForm.addEventListener('submit', function(event) {
    event.preventDefault(); 
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    //console log
    console.log('Title:' + title + ' content: ' + content);

    //turn message to variable
    const contents = 'New post created with title: ' + title + ' and content: ' + content;

    //transmit to api
    fetch('/api/log?message=' + encodeURIComponent(contents))
    .catch(error => console.error(error));

});
