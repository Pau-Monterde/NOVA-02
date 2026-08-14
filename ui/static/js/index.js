alert('Eo tamo ativo papi')
function receive_event(event) {
    document.getElementById("event").textContent = "Evento recibido: " + event
}

async function send_input() {
    var input_str = document.getElementById("input_str").value 
    pywebview.api.put_input(input_str)
    document.getElementById("input_str").value = ""
    document.getElementById("messages").innerHTML += `<div class="user_input-container"><p class="user_input-p">${input_str}</p></div>`
}

function write_response(response) {
    document.getElementById("messages").innerHTML += `<div class="nova_response-container"><p class="nova_response-p">${response}</p></div>`
    
}