const inputFile = document.querySelector("#arquivo");
const paragrafo = document.querySelector("#paragrafo");
paragrafo.innerText = "";
inputFile.addEventListener("change", function (e) {
  const inputTarget = e.target;
  const file = inputTarget.files[0];
  console.log(file);

  if (file) {
    paragrafo.innerText = "Arquivo Selecionado: " + file["name"];
  } else {
    paragrafo.innerText = "Arquivo não Selecionado";
  }
});
