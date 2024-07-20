document.getElementById('fetch-message').addEventListener('click', async () => {
    const response = await fetch('/api/hello');
    const data = await response.json();
    document.getElementById('message').innerText = data.message;
});

