const submit_key = document.querySelector("#submit_key");
const input_key = document.querySelector("#input_key");
const cursor_input = document.querySelector("#circle_cursor");
const form = document.getElementById("myForm");
const pop_error = document.getElementById("error_popup");
const textElement = document.getElementById("error_key_p");
const container_popup = document.getElementsByClassName("container_popup"); // Exemple d'ID du texte

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
  console.log("tett");
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
        console.log(processData);

        input_key.classList.remove("animate__shakeX", "errorKey", "succesKey"); // Supprime toutes les classes d'état précédent
        pop_error.classList.remove("error_popup");

        if (processData.status === "success") {
          console.log(processData.status);
          input_key.classList.add("succesKey");
        } else if (processData.status === "error") {
          console.log(processData.status);
          pop_error.classList.add("error_popup");
          pop_error.classList.add("error_popup_1");
          input_key.classList.add("errorKey");
          input_key.classList.add("animate__shakeX");
          pop_error.addEventListener("click", () => {
            console.log("popup error");
          });

          pop_error.addEventListener("click", handlePopupClick);
          textElement.addEventListener("click", handlePopupClick);

          // setTimeout(() => {
          //   console.log("Réinitialisation du popup d'erreur");
          //   pop_error.classList.add("error_popup");
          //   pop_error.classList.remove("error_popup_1");
          // }, 7000);
        }

        // Nettoyer localStorage après traitement
        localStorage.removeItem("inputKey1");
        // } catch (error) {
        //   console.log("Erreur:", error); // Gérer les erreurs
        function handlePopupClick() {
          console.log("Pop error clicked");
          // Actions spécifiques lors du clic sur le popup
          pop_error.classList.add("error_popup");
          pop_error.classList.remove("error_popup_1");
        }
      } catch (error) {
        console.log("error 1 :", error);
      }
    }
  } else if (currentURL.includes("check_update")) {
    console.log("tete");
    try {
      // Envoyer la requête POST pour le traitement
      const processResponse = await fetch("/check_update", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ key: inputKey }),
      });
      const processData = await processResponse.json();
      console.log(processData);

      if (processData.status === "success") {
        window.location.href("/confirmation_key");
      }
    } catch (error) {
      console.log("error 1 :", error);
    }
  }
});
