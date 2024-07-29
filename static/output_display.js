document.addEventListener('DOMContentLoaded', () => {
    const status = document.getElementById("status");
    status.innerText = "Computing...";

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

    // Initialize the current percentage and animation parameters
    let currentPercentage = 0;
    const duration = 2000; // Duration of the animation in milliseconds
    const interval = 10; // Update interval in milliseconds
    const step = percentage / (duration / interval); // Amount to increment each interval

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
