// NAVBAR
window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

// SENTIMENT JS
function validateForm() {
    var textInput = document.getElementById('text_input').value;
    var regex = /\d/; // Regular expression to check for numbers
    
    if (textInput.trim() == '') {
        alert('Please enter text for analysis.');
        return false; // Prevent form submission
    }
    
    // Check if input contains numbers
    if (regex.test(textInput)) {
        alert("Numbers are not allowed in the input text. Please remove them.");
        return false; // Prevent form submission
    }
    
    return true; // Allow form submission
}
