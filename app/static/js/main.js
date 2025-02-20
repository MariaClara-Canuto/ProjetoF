function redirectTo(url) {
    window.location.href = url; //redireciona o usuário após o login ou sign in
}

function showMessage(message, isError = true) { // Exibe uma messagem de erro ou sucesso
    const messageDiv = document.createElement('div');
    messageDiv.className = isError ? 'error message' : 'success message';
    messageDiv.textContent = message;
    document.body.prepend(messageDiv)

    setTimeout(() => {
        messageDiv.remove();
    }, 4000); //A mensagem some depois de 4s
}

function checkLogged() { //verifica se o usuario esta logado
    fetch('/check_session', {
        method: 'GET',
    })

    .then(response => response.json())
    .then(data => {
        if (data.logged) {
            console.log('Usuário logado:', data.username);
        } 
        
        else {
            console.log('Usuário não logado');
        } 
    });
}

document.addEventListener('DOMContentLoaded', checkLogged);