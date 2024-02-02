// Add a click event listener to the element with the ID 'add_item'
document.getElementById('add_item').addEventListener('click', function() {
    // Select the first unordered list (ul) element with the class 'my_list' and assign it to the constant 'ul'
    const ul = document.querySelector('.my_list');

    // Create a new list item (li) element and assign it to the constant 'li'
    const li = document.createElement('li');

    // Set the text content of the new list item (li) to 'Item'
    li.textContent = 'Item';

    // Append the new list item (li) as a child to the unordered list (ul), effectively adding it to the list
    ul.appendChild(li);
});