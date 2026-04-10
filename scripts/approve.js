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

//create approval request (lacking backend connection) (its making stuff up) (totally legit) (scratch that, ts hardcoded to f)
function createApprovalRequest() {
    console.log('Approval request created for post ID: ' + postData.id);

    var card = document.createElement("div");
    card.classList.add("admin-card");

    //Creat content for card
    var cardContent = '<h2>' + postData.title + '</h2> <p>' + postData.content + '</p> <button class="approve-button" id = "approve" onclick="approve(this)">Approve</button> <button class="deny-button" id="deny" onclick="deny(this)">Deny</button> <div class="admin-card-footer">Posted by ID: ' + postData.posterId + '</div>';

    card.innerHTML = cardContent;

    //append onto the grid
    var container = document.getElementById("cardContainer");
    container.appendChild(card);
}


//delete post (DELETES POST FROM DATABASE) (IMPLEMENT LATER)
function deny(element) {
    console.log('Post deleted');

    var card = element.parentElement;
    card.remove();
}

//approve post (+3999 sociall credit)#
function approve(element) {
    console.log('Post approved');

    var card = element.parentElement;
    card.remove();
}
