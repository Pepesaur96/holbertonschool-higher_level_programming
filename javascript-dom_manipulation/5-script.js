// Wait until the DOM content is fully loaded.
document.addEventListener('DOMContentLoaded', (event) => {
    // Select the element with the ID 'add_item' and assign it to the constant 'updatebutton'
    const updatebutton = document.getElementById('update_header');

    // Add a click event listener to the 'updatebutton' element
    updatebutton.addEventListener('click', () => {
        // Select the header elemet you want to update and assign it to the constant 'header'
        const header = document.querySelector('header');

        // Update the text content of the 'header' element
        header.textContent = 'New Header!!!';
    });
});