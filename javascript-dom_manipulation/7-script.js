// Wait until the DOM content is fully loaded.
document.addEventListener('DOMContentLoaded', (event) => {
    // Use the Fetch API to retrieve data from the given URL
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        // Check if the response is OK (status 200)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Parse the JSON body of the response
        return response.json();
    })
    .then(data => {
        //Select the HTML ul element with the id 'list_movies'
        const list_movies = document.getElementById('list_movies');

        //loop over each film in the received data
        data.results.forEach(film => {
            // Create a new list item (li) element and assign it to the constant 'li'
            const li = document.createElement('li');

            // Set the text content of the new list item (li) to the film's title
            li.textContent = film.title;

            // Append the new list item (li) as a child to the unordered list (ul), effectively adding it to the list
            list_movies.appendChild(li);
        });
    })
    .catch(error => {
        // Log any errors to the console
        console.error('Fetch Error:', error);
    });
});