// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    // Use the Fetch API to retrieve data from the given URL
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(response => {
            // Check if the response is OK (status 200)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            // Parse the JSON body of the response
            return response.json();
        })
        .then(data => {
            // Extract the character name from the data
            const characterName = data.name;

            // Select the HTML tag with the id 'character' and update its text content with the character name
            document.getElementById('character').textContent = characterName;
        })
        .catch(error => {
            // Log any errors to the console
            console.error('Fetch Error:', error);
        });
});