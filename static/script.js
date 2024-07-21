async function process_input() {
    let a = parseInt(document.getElementById("first-number").value);
    let b = parseInt(document.getElementById("second-number").value);

    const response = await fetch(`/api/add?a=${a}&b=${b}`);
    const data = await response.json();
    
    document.getElementById("output").innerText = data.message;
}
