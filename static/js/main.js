const submit_key = document.querySelector("#submit_key");
const input_key = document.querySelector("#input_key");
const cursor_input = document.querySelector("#circle_cursor");
const form = document.getElementById("myForm");
const pop_error = document.getElementById("error_popup");

function data_input() {
  document.addEventListener("DOMContentLoaded", () => {
    const storedValue = localStorage.getItem("inputKey1");
    if (storedValue) {
      input_key.value = storedValue;
    }
  });
}

// Fonction pour mettre à jour le style en fonction du contenu de l'input
function updateInputStyle() {
  if (input_key.value.trim() === "") {
    // Ajouter la classe pour un input vide
    input_key.className = "";
    input_key.classList.add("input_key111");
  } else {
    // Réinitialiser le style si l'input contient du texte
    input_key.classList = "";
  }
}

// Fonction pour gérer les erreurs
function handleErrorState() {
  input_key.classList.remove("animate__shakeX", "input_key111");
  void input_key.offsetWidth; // Force le reflow/repaint
  input_key.classList.add("animate__shakeX", "input_key111");
}

// Événements sur le bouton de soumission
submit_key.addEventListener("mouseover", () => {
  submit_key.classList.add("mm");
});

submit_key.addEventListener("mouseout", () => {
  submit_key.classList.remove("mm");
});

input_key.addEventListener("mousemove", () => {
  input_key.classList.add("nn", "nn1");
});

input_key.addEventListener("mouseout", () => {
  input_key.classList.remove("nn", "nn1");
});

input_key.addEventListener("click", () => {
  input_key.classList.add("nn", "nn1");
});

// Ajouter un gestionnaire d'événement pour surveiller les changements dans l'input
input_key.addEventListener("input", updateInputStyle);

// Ajouter un écouteur d'événement pour intercepter la soumission du formulaire
form.addEventListener("submit", async function (event) {
  event.preventDefault(); // Empêche le rechargement de la page

  const inputKey = input_key.value;

  if (inputKey === "") {
    handleErrorState();
    return;
  }

  try {
    // Stocker la valeur de l'input dans localStorage
    localStorage.setItem("inputKey1", inputKey);

    // Rediriger vers la page de login Discord
    window.location.href = "/login"; // Changez cela en redirection normale
  } catch (error) {
    console.log("Erreur:", error); // Gérer les erreurs
  }
});

// Sur la page d'accueil (localhost), ajouter ce script pour traiter le login et la requête
document.addEventListener("DOMContentLoaded", async () => {
  const currentURL = window.location.href;
  if (currentURL.includes("confirmation_key")) {
    const inputKey = localStorage.getItem("inputKey1");
    input_key.value = inputKey;
    if (inputKey) {
      try {
        // Envoyer la requête POST pour le traitement
        const processResponse = await fetch("/process-data", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ key: inputKey }),
        });

        const processData = await processResponse.json();
        input_key.classList.remove("animate__shakeX", "errorKey", "succesKey"); // Supprime toutes les classes d'état précédent

        if (processData.status === "success") {
          console.log(processData.status);
          input_key.classList.add("succesKey");
        } else if (processData.status === "error") {
          // Ajout des classes pour l'erreur
          pop_error.classList.add("error_popup_1");
          pop_error.classList.remove("error_popup");
          // Animation d'erreur et réinitialisation après 2 secondes
          // setTimeout(() => {
          //   // console.log("Réinitialisation de l'erreur");
          //   // pop_error.classList.remove("error_popup_1");
          //   // pop_error.classList.add("error_popup");
          // }, 2000);
          console.log("233");
          // Ajout des classes pour indiquer l'erreur et l'animation
          input_key.classList.add("errorKey");
          input_key.classList.add("animate__shakeX");
        }

        // Nettoyer localStorage après traitement
        localStorage.removeItem("inputKey1");
      } catch (error) {
        console.log("Erreur:", error); // Gérer les erreurs
      }
    } else {
      localStorage.removeItem("inputKey1");
    }
  }
});
