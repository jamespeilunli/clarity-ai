const statusElement = document.getElementById("status");

let inputData = localStorage.getItem("inputData");
if (!inputData) {
    statusElement.innerText = "Error: input data is null";
    throw new Error("input data is null");
}

fetch("/model", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: inputData,
})
    .then((response) => {
        if (!response.ok) {
            return response.text().then((text) => { throw new Error(text) });
        }
        else {
            return response.json();
        }
    })
    .then((data) => {
        statusElement.innerText = "Done!";
        console.log("Success:", data);
        displayOutput(parseInt(data.percentage, 10));
    })
    .catch((error) => {
        statusElement.innerText = error;
        throw new Error(error);
    });

function displayOutput(percentage) {
    // Select the elements where the percentage and graph are displayed
    const percentageDisplay = document.querySelector('.percentage-display');
    const graphContainer = document.querySelector('.graph-container');
    const sadPage = document.querySelector('.sad-page');
    const happyPage = document.querySelector('.happy-page');

    let inputType = JSON.parse(localStorage.getItem('inputData')).inputType;
    console.log(inputType);

    if (inputType === "Single Post") {
        if (percentage > 50) {
            sadPage.style.display = 'block';
        } else {
            happyPage.style.display = 'block';
        }
    } if (inputType === "Account Handle") {
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

    statusElement.innerText = "";
    console.log(statusElement)
}
