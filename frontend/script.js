// JavaScript

document.addEventListener("DOMContentLoaded", () => {
  const formContainer = document.getElementById("form-container");
  const inputForm = document.getElementById("input-form");
  const percentageScreen = document.getElementById("percentage-screen");
  const percentageText = document.getElementById("percentage-text");

  function redirectToForm(title) {
    const formTitle = document.getElementById("form-title");
    formTitle.textContent = title;
    formContainer.style.display = "block";
    formContainer.style.animation = "slideUp 0.5s forwards";
    document.body.classList.add("blur");
  }

  inputForm.addEventListener("submit", handleSubmit);

  function handleSubmit(event) {
    event.preventDefault();
    const userInput = document.getElementById("user-input").value;
    console.log("User Input:", userInput);

    fetch("your-backend-endpoint", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ input: userInput })
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        displayPercentageAndGraph(data.percentage, data.graph);
      })
      .catch((error) => {
        console.error("Error:", error);
        closeForm();
      });
  }

  // JavaScript to handle the backend output
  function displayPercentageAndGraph(percentage, graph) {
    const percentageScreen = document.getElementById("percentage-screen");
    const percentageText = document.getElementById("percentage-text");
    const graphContainer = document.getElementById("graph-container");

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

    // Assuming `graph` is the HTML or SVG content for the graph
    graphContainer.innerHTML = graph;
  }
});

function handleSubmit(event) {
  event.preventDefault();
  const userInput = document.getElementById("user-input").value;
  console.log("User Input:", userInput);

  fetch("your-backend-endpoint", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ input: userInput })
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
  formTitle.textContent = title;
  formContainer.style.display = "block";
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