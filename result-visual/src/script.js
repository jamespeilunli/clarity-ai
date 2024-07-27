document.addEventListener('DOMContentLoaded', () => {
    // Simulate backend input
    const backendPercentage = 'INSERTBACKENDROUTEHERE'; // Example percentage value from backend

    const percentageDisplay = document.querySelector('.percentage-display');
    const graphContainer = document.querySelector('.graph-container');

    let currentPercentage = 0;
    const duration = 2000; // Duration of the animation in milliseconds
    const interval = 10; // Update interval in milliseconds
    const step = backendPercentage / (duration / interval);

    const intervalId = setInterval(() => {
        if (currentPercentage >= backendPercentage) {
            clearInterval(intervalId);
        } else {
            currentPercentage += step;
            percentageDisplay.textContent = `${Math.round(currentPercentage)}%`;
            graphContainer.style.setProperty('--rating', (currentPercentage / 20));
        }
    }, interval);
});
