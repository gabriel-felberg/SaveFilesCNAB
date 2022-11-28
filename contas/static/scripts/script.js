const table = document.getElementById("table");

async function render() {
  let response = await fetch(`http://127.0.0.1:8000/api/dados/`);
  let userData = await response.json();

  for (let i = 0; i < userData.length; i++) {
    let tr = table.insertRow();
    let td_typo = tr.insertCell(0);
    let td_data = tr.insertCell(1);
    let td_cpf = tr.insertCell(2);
    let td_card = tr.insertCell(3);
    let td_horn = tr.insertCell(4);
    let td_value = tr.insertCell(5);
    let td_woner_store = tr.insertCell(6);
    let td_store = tr.insertCell(7);
    td_typo.innerText = userData[i]["Tipo"];
    td_data.innerText = userData[i]["Data"];
    td_cpf.innerText = userData[i]["CPF"];
    td_card.innerText = userData[i]["Cartão"];
    td_horn.innerText = userData[i]["Hora"];
    td_value.innerText = userData[i]["Valor"];
    td_woner_store.innerText = userData[i]["DonoDaLoja"];
    td_store.innerText = userData[i]["NomeLoja"];
  }
}
render();

const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  window.location.href = "http://127.0.0.1:8000/api/dados/";
});
