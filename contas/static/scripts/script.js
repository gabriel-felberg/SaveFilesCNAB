const table = document.getElementById("table");

async function render() {
  let response = await fetch(`http://127.0.0.1:8000/api/dados/`);
  let userData = await response.json();
  console.log(userData);
  for (let i = 0; i < userData.length; i++) {
    let tr = table.insertRow();
    let td_tipo = tr.insertCell(0);
    let td_data = tr.insertCell(1);
    let td_cpf = tr.insertCell(2);
    let td_cartao = tr.insertCell(3);
    let td_hora = tr.insertCell(4);
    let td_valor = tr.insertCell(5);
    let td_DonoDaLoja = tr.insertCell(6);
    let td_NomeLoja = tr.insertCell(7)
    td_tipo.innerText = userData[i]["Tipo"];
    td_data.innerText = userData[i]["Data"];
    td_cpf.innerText = userData[i]["CPF"];
    td_cartao.innerText = userData[i]["Cartão"];
    td_hora.innerText = userData[i]["Hora"];
    td_valor.innerText = userData[i]["Valor"];
    td_DonoDaLoja.innerText = userData[i]["DonoDaLoja"];
    td_NomeLoja.innerText = userData[i]["NomeLoja"]
  }
}
render();

const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  window.location.href = "http://127.0.0.1:8000/api/dados/";
});
