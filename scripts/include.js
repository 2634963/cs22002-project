// Include HTML code within a specific element
async function includeHTML(sourceFile, destElementId) {
    // Load the HTML to insert
    const includeResponse = await fetch(sourceFile);

    // Error out if we couldn't load it
    if(!(await includeResponse.ok))
    {
        console.log("Error: failed to load HTML from '" + sourceFile + "'");
        return;
    }

    // Insert the HTML into the destination element
    document.getElementById(destElementId).innerHTML = await includeResponse.text();
}
