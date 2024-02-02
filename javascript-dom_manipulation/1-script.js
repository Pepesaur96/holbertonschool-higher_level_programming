// wait for dom to be loaded
document.addEventListener('DOMContentLoaded', (event) => {
    //Select the element with the id "red_header"
    const redHeader = document.getElementById('red_header');

    // add a click event to the element
    redHeader.addEventListener('click', () => {
        // Set the color of the text to red (#FF0000)
        const header = document.querySelector('header');


    // Set the color of the text to red (#FF0000)
    header.style.color = '#FF0000';
    });

});