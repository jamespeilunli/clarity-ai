// JavaScript

document.addEventListener("DOMContentLoaded", () => {
    const formContainer = document.getElementById("form-container");
    const inputForm = document.getElementById("input-form");

    inputForm.addEventListener("submit", handleSubmit);
});

function handleSubmit(event) {
    event.preventDefault();
    const userInput = document.getElementById("user-input").value;
    const inputType = document.getElementById("form-title").innerText;
    localStorage.setItem(
        "inputData",
        JSON.stringify({
            input: userInput,
            inputType: inputType,
        })
    );

    console.log("0 User Input:", userInput);
    console.log("0 Input Type:", inputType);

    if (inputType === "Mastodon Account Handle" || inputType === "Reddit Account Handle") {
        window.location.href = "/anxiety/results";
    } else {
        window.location.href = "/results";
    }
}

function showForm(title) {
    const formContainer = document.getElementById("form-container");
    const formTitle = document.getElementById("form-title");
    const formInput = document.getElementById("user-input");
    formTitle.textContent = title;
    formContainer.style.display = "block";
    formInput.value = "";
    if (formTitle.textContent == "Account Handle") {
        formInput.placeholder = "Enter a Mastodon handle";
    } else {
        formInput.placeholder = "Enter text here";
    }
    document.body.classList.add("blur");
    document.body.classList.add("no-scroll");
}

function closeForm() {
    const formContainer = document.getElementById("form-container");
    formContainer.style.display = "none";
    document.body.classList.remove("blur");
    document.body.classList.remove("no-scroll");

    canShowForm = false;
    setTimeout(() => {
        canShowForm = true;
    }, 1); // 0.5 seconds cooldown
}

// Magic star animation
let index = 0,
    interval = 1000;

// Function to show the modal
function showModal() {
    document.querySelector(".modal").style.display = "block";
    document.body.classList.add("no-scroll");
}

// Function to hide the modal
function hideModal() {
    document.querySelector(".modal").style.display = "none";
    document.body.classList.remove("no-scroll");
}

// Example event listeners
document.querySelector(".close").addEventListener("click", hideModal);
window.addEventListener("click", function (event) {
    if (event.target.classList.contains("modal")) {
        hideModal();
    }
});
