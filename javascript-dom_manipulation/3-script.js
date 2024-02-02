// Wait for the entire content of the page to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', (event) => {

    // Select the element with the ID 'toggle_header' and assign it to toggleHeader
    const toggleHeader = document.querySelector('#toggle_header');

    // Select the first 'header' element in the document and assign it to header
    const header = document.querySelector('header');

    // Add a click event listener to the 'toggleHeader' element
    toggleHeader.addEventListener('click', () => {
        // Check if the 'header' element currently has the class 'red'
        if (header.classList.contains('red')) {
            // If it does, remove the 'red' class
            header.classList.remove('red');
            // And then add the 'green' class
            header.classList.add('green');
        }
        // Check if the 'header' element currently has the class 'green'
        else if (header.classList.contains('green')) {
            // If it does, remove the 'green' class
            header.classList.remove('green');
            // And then add the 'red' class
            header.classList.add('red');
        }
    });
});