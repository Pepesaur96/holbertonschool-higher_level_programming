// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    // Use the Fetch API to retrieve data from the given URL
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => {
            // Check if the response is OK (status 200)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            // Parse the JSON body of the response
            return response.json();
        })
        .then(data => {
            // Select the HTML element with the id 'hello'
            const helloElement = document.getElementById('hello');

            // Update the text content of the 'helloElement' with the 'hello' value from the fetched data
            helloElement.textContent = data.hello;
        })
        .catch(error => {
            // Log any errors to the console
            console.error('Fetch Error:', error);
        });
});