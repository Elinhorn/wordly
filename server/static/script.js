document.querySelector("#myForm").addEventListener("submit", function (event) {
  event.preventDefault();

  let formData = new FormData(this);
  const userInput = document.getElementById("user_input");

  fetch("/process", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.game_over) {
        document.querySelector("#game-over").style.display = "block";
        document.querySelector("#myForm").style.display = "none";
        document.querySelector("#response-correct").style.display = "none";
        document.querySelector("#attempts-left").innerText = data.attempts;
      } else {
        document.querySelector("#attempts-left").innerText = data.attempts;
        document.querySelector("#response-right").innerText = data.right;
        document.querySelector("#response-wrong").innerText = data.wrong;
        if (data.correct) {
          document.querySelector("#response-correct").style.display = "block";
          document.querySelector("#correct-word").innerText =
            formData.get("user_input");
          document.querySelector("#myForm").style.display = "none";
        }
      }
      userInput.value = "";
    })
    .catch((error) => console.log("Error: ", error));
});

document.getElementById("try-again").addEventListener("click", function () {
  window.location.href = "/";
});

document.getElementById("next-word").addEventListener("click", function () {
  window.location.href = "/";
});
