document.addEventListener('DOMContentLoaded', () => {
    const status = document.getElementById("status");
    status.innerText = "Computing...";
    // Select the elements where the percentage and graph are displayed
    const percentageDisplay = document.querySelector('.percentage-display');
    const graphContainer = document.querySelector('.graph-container');
    const sadPage = document.querySelector('.sad-page');
    const happyPage = document.querySelector('.happy-page'); // Ensure this element is defined
    // Hide all elements initially
    sadPage.style.display = 'none';
    happyPage.style.display = 'none';
    percentageDisplay.style.display = 'block';
    graphContainer.style.display = 'block';

    let inputData = localStorage.getItem("inputData");
    if (!inputData) throw new Error("input data is null"); // add error handling later

    fetch("/model", {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: inputData,
    })
    .then((response) => response.json())
    .then((data) => {
        status.innerText = "Done!";
        console.log("Success:", data);
        displayPercentage(parseInt(data.percentage, 10));
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});
function displayPercentage(percentage) {
    // Select the elements where the percentage and graph are displayed
    const percentageDisplay = document.querySelector('.percentage-display');
    const graphContainer = document.querySelector('.graph-container');
    const sadPage = document.querySelector('.sad-page');
    const happyPage = document.querySelector('.happy-page'); // Ensure this element is defined
    // Hide all elements initially
    sadPage.style.display = 'none';
    happyPage.style.display = 'none';
    percentageDisplay.style.display = 'block';
    graphContainer.style.display = 'blcok';
    let inputType = JSON.parse(localStorage.getItem('inputData')).inputType;

    console.log(inputType);
    if (inputType === "Single Post"){
        // Handle non "Account Handle" inputType

        percentageDisplay.style.display = 'none';
        graphContainer.style.display = 'none';
        if (percentage > 50) {
            sadPage.style.display = 'block';
        } else {
            happyPage.style.display = 'block'; // Ensure happy page element is defined
        }
    }

    if (inputType === "Account Handle") {
        // Initialize the current percentage and animation parameters
        let currentPercentage = 0;
        const duration = 2000; // Duration of the animation in milliseconds
        const interval = 10; // Update interval in milliseconds
        const step = percentage / (duration / interval); // Amount to increment each interval

        // Ensure the elements are visible
        percentageDisplay.style.display = 'block';
        graphContainer.style.display = 'block';

        // Set up an interval to gradually update the percentage display and graph
        const intervalId = setInterval(() => {
            if (currentPercentage >= percentage) {
                // Stop the interval when the target percentage is reached
                clearInterval(intervalId);
            } else {
                // Increment the current percentage
                currentPercentage += step;
                // Update the text content to display the current percentage
                percentageDisplay.textContent = `${Math.round(currentPercentage)}%`;
                // Update the CSS variable for the graph's rating
                graphContainer.style.setProperty('--rating', currentPercentage / 20);
            }
        }, interval);
    } 
    
}

