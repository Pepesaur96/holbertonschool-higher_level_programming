// Wait for the entire content of the page to be loaded
document.addEventListener('DOMContentLoaded', (event) => {
    // Select the element with the ID 'red_header'
    let redHeader = document.querySelector('#red_header');

    // Select the first 'header' element
    let header = document.querySelector('header');

    // Add a click event listener to the 'redHeader' element
    redHeader.addEventListener('click', () => {
        // When 'redHeader' is clicked, add the class 'red' to the 'header' element
        header.classList.add('red');
    });
});