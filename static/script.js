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
  console.log("User Input:", userInput);
  console.log("Input Type:", inputType);

  fetch("/model", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      input: userInput,
      inputType: inputType
    })
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      closeForm();
      displayPercentage(data.percentage);
    })
    .catch((error) => {
      console.error("Error:", error);
      closeForm();
    });
}

function displayPercentage(percentage) {
  const percentageScreen = document.getElementById("percentage-screen");
  const percentageText = document.getElementById("percentage-text");
  percentageScreen.style.display = "flex";

  let currentPercentage = 0;
  const interval = setInterval(() => {
    if (currentPercentage < percentage) {
      currentPercentage++;
      percentageText.textContent = currentPercentage + "%";
    } else {
      clearInterval(interval);
    }
  }, 20);
}

function showForm(title) {
  const formContainer = document.getElementById("form-container");
  const formTitle = document.getElementById("form-title");
  const formInput = document.getElementById("user-input");
  formTitle.textContent = title;
  formContainer.style.display = "block";
  formInput.value = "";
  document.body.classList.add("blur");
}

function closeForm() {
  const formContainer = document.getElementById("form-container");
  formContainer.style.display = "none";
  document.body.classList.remove("blur");
  canShowForm = false;
  setTimeout(() => {
    canShowForm = true;
  }, 1); // 0.5 seconds cooldown
}

// Magic star animation
let index = 0,
  interval = 1000;
