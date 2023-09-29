// Get modal and button elements
var modal = document.getElementById("myModal");
var closeModalBtn = document.getElementById("closeModalBtn");

// Open the modal by default when the page is loaded
modal.style.display = "block";

// Close the modal when the close button is clicked
closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
