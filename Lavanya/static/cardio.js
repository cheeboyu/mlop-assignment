function toggleImage(tdElement) {
    var image = tdElement.querySelector('img');
    if (!image) return; // Check if image exists within the table cell
    if (image.style.display === "none") {
        image.style.display = "block";
    } else {
        image.style.display = "none";
    }
}





document.addEventListener('DOMContentLoaded', function() {
    const numericFields = ['Age', 'Weight', 'Height', 'Ap_lo', 'Ap_hi', 'Heart_rate', 'Blood_oxygen_level', 'Body_temp'];

    numericFields.forEach(function(fieldId) {
        const field = document.getElementById(fieldId);
        field.addEventListener('input', function(event) {
            // Remove any non-numeric characters from the input value
            this.value = this.value.replace(/[^0-9.]/g, '');
        });

        field.addEventListener('keypress', function(event) {
            const keyCode = event.keyCode || event.which;
            const keyValue = String.fromCharCode(keyCode);

            // Check if the entered key is a number or a dot
            if (!/[\d.]/.test(keyValue)) {
                event.preventDefault();
                alert('Please only enter numbers.');
            }
        });
    });

    const form = document.getElementById('prediction-form');
    const errorMessages = document.getElementById('error-messages');

    form.addEventListener('submit', function(event) {
        // Clear previous error messages
        errorMessages.innerHTML = '';

        // Perform client-side validation
        let isValid = true;
        numericFields.forEach(function(fieldId) {
            const field = document.getElementById(fieldId);
            const value = parseFloat(field.value);

            // Check if the value is a valid number
            if (isNaN(value)) {
                displayError(field, 'Please enter a valid number.');
                isValid = false;
            } else {
                // Additional validation for specific fields (age, weight, height, etc.)
                if (fieldId === 'Age' && (value <= 0 || value > 150)) {
                    displayError(field, 'Please enter a valid age.');
                    isValid = false;
                }
                if (fieldId === 'Weight' && (value <= 0 || value > 300)) {
                    displayError(field, 'Please enter a valid weight.');
                    isValid = false;
                }
                if (fieldId === 'Height' && (value <= 0 || value > 300)) {
                    displayError(field, 'Please enter a valid height.');
                    isValid = false;
                }

                if (fieldId === 'Ap_lo' && (value <= 0 || value > 400)) {
                    displayError(field, 'Please enter a valid diastolic blood pressure value (1 - 400).');
                    isValid = false;
                }
                if (fieldId === 'Ap_hi' && (value <= 0 || value > 400)) {
                    displayError(field, 'Please enter a valid systolic blood pressure value (1 - 400).');
                    isValid = false;
                }
                if (fieldId === 'Heart_rate' && (value <= 0 || value > 250)) {
                    displayError(field, 'Please enter a valid heart rate value (1 - 250).');
                    isValid = false;
                }
                if (fieldId === 'Blood_oxygen_level' && (value <= 0 || value > 100)) {
                    displayError(field, 'Please enter a valid blood oxygen level value (1 - 100).');
                    isValid = false;
                }
                if (fieldId === 'Body_temp' && (value <= 0 || value > 45)) {
                    displayError(field, 'Please enter a valid body temperature value (1 - 45).');
                    isValid = false;
                }
            }
        });

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    function displayError(field, message) {
        const error = document.createElement('div');
        error.classList.add('alert', 'alert-danger');
        error.textContent = message;
        errorMessages.appendChild(error);

        // Highlight the invalid field
        field.classList.add('is-invalid');
    }

    // Remove validation error when user starts typing again
    form.addEventListener('input', function(event) {
        if (event.target.classList.contains('is-invalid')) {
            event.target.classList.remove('is-invalid');
            errorMessages.innerHTML = ''; // Clear error messages
        }
    });
});