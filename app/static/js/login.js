document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const username = document.getElementById('username').value
            const password = document.getElementById('password').value

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },

                    body: JSON.stringify({username, password}),

                });

                const data = await response.json();

                if (data.success) { // se o login existir e as crendenciais estiverem certas, o usuário é redirecionado á página inicial do blog
                    redirectTo('/inicial')
                }

                else {
                    showMessage(data.message || 'Credênciais Inválidas', true);
                }

            } catch (error) {
                showMessage('Erro ao conectar com o servidor', true);
                console.error('Erro: ', error);
            }

        });
    }
});