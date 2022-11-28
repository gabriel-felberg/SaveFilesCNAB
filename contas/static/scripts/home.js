const inputFile = document.querySelector("#arquivo");
const paragraph = document.querySelector("#paragrafo");
paragraph.innerText = "";

inputFile.addEventListener("change", function (e) {
  const inputTarget = e.target;
  const file = inputTarget.files[0];


  if (file) {
    paragraph.innerText = "Arquivo Selecionado: " + file["name"];
  } else {
    paragraph.innerText = "Arquivo não Selecionado";
  }
});
