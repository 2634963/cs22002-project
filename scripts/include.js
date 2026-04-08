// Include HTML code within a specific element
async function includeHTML(sourceFile, destElementId) {
    // Load the HTML to insert
    let includeText = "";

    const includeResponse = await fetch(sourceFile)
          .then(response => response.text())
          .then(text => {
              includeText = text
          });

    // Insert the HTML into the destination element
    document.getElementById(destElementId).innerHTML = includeText;
}
