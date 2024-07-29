document.addEventListener('DOMContentLoaded', () => {
    // Simulate backend input
    let backendPercentage = '50'; 
    // Remove the percentage symbol and convert the value to an integer
    backendPercentage = parseInt(backendPercentage.replace('%', ''), 10);

    // Select the elements where the percentage and graph are displayed
    const percentageDisplay = document.querySelector('.percentage-display');
    const graphContainer = document.querySelector('.graph-container');

    // Initialize the current percentage and animation parameters
    let currentPercentage = 0;
    const duration = 2000; // Duration of the animation in milliseconds
    const interval = 10; // Update interval in milliseconds
    const step = backendPercentage / (duration / interval); // Amount to increment each interval

    // Set up an interval to gradually update the percentage display and graph
    const intervalId = setInterval(() => {
        if (currentPercentage >= backendPercentage) {
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
});