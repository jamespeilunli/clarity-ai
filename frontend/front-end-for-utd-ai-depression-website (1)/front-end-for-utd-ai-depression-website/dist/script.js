// Add your JavaScript here
document.getElementById("cards").onmousemove = e => {
    for(const card of document.getElementsByClassName("card")) {
        const rect = card.getBoundingClientRect(),
              x = e.clientX - rect.left,
              y = e.clientY - rect.top;

        card.style.setProperty("--mouse-x", `${x}px`);
        card.style.setProperty("--mouse-y", `${y}px`);
    }
};

function showForm(title) {
    const formContainer = document.getElementById('form-container');
    const formTitle = document.getElementById('form-title');
    formTitle.textContent = title;
    formContainer.style.display = 'block';
    formContainer.style.animation = 'slideUp 0.5s forwards'; // Trigger the slide-up animation
    document.body.classList.add('blur');
}

function closeForm() {
    const formContainer = document.getElementById('form-container');
    formContainer.style.display = 'none';
    document.body.classList.remove('blur');
}

// Backend connection point
function handleSubmit(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input').value;
    console.log("User Input:", userInput); // For debugging purposes

    // Replace 'your-backend-endpoint' with the actual backend endpoint
    fetch('your-backend-endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        closeForm();  // Close the form after successful submission
        displayPercentage(data.percentage);  // Display and animate the percentage
    })
    .catch((error) => {
        console.error('Error:', error);
        closeForm();
    });
}

// Function to animate percentage display
function displayPercentage(percentage) {
    const percentageDisplay = document.getElementById('percentage-display');
    const percentageText = document.getElementById('percentage');
    percentageDisplay.style.display = 'block';

    let currentPercentage = 0;
    const interval = setInterval(() => {
        if (currentPercentage < percentage) {
            currentPercentage++;
            percentageText.textContent = currentPercentage + '%';
        } else {
            clearInterval(interval);
        }
    }, 20); // Adjust the interval time to speed up or slow down the animation
}