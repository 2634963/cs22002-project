//approve disapprove button code

//TEST POST DATA SAMPLE (based off Aidens Schemea)
const postData = {
    id: 1,
    title: 'Sample Post Title',
    content: 'Sample post content',
    posterId: 512,
    approved: false
}

//button variables
const approveButton = document.getElementById('approve');
const denyButton = document.getElementById('deny');

//event listener for approve button
approveButton.addEventListener('click', function() {
    console.log('Approve button clicked');
});

//event listener for deny button
denyButton.addEventListener('click', function() {
    console.log('Deny button clicked');
});



//create post... 
function createPost() {
    console.log('Post created');

    //create dynamic post element
    var post = document.createElement('div');

    //add CSS Card styling to post
    post.style.border = '3px solid #999999';
    post.style.borderRadius = '3px';
    post.style.display = 'grid';
    post.style.gridTemplateRows = 'max-content 200px 1fr';
    post.style.textAlign = 'center';
    
    
}

//delete post (DELETES POST FROM DATABASE) (IMPLEMENT LATER)
function deletePost() {
    console.log('Post deleted');
}