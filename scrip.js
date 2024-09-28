let users = {};
let currentUser = null;

function showLogin() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('change-password-form').style.display = 'none';
}

function showRegister() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
    document.getElementById('change-password-form').style.display = 'none';
}

function showChangePassword() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('change-password-form').style.display = 'block';
}

function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    if (users[username] && users[username] === password) {
        currentUser = username;
        alert(`Bienvenido ${username}`);
        document.getElementById('auth-container').style.display = 'none';
        document.getElementById('task-container').style.display = 'block';
    } else {
        alert('Usuario o contraseña incorrectos');
    }
}

function register() {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;

    if (!users[username]) {
        users[username] = password;
        alert('Usuario registrado exitosamente');
        showLogin();
    } else {
        alert('El usuario ya existe');
    }
}

function changePassword() {
    const newPassword = document.getElementById('new-password').value;
    if (currentUser) {
        users[currentUser] = newPassword;
        alert('Contraseña cambiada exitosamente');
        showLogin();
    }
}

function createTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-description').value;
    const dueDate = document.getElementById('task-due-date').value;
    const priority = document.getElementById('task-priority').value;

    const taskList = document.getElementById('task-list');
    const taskDiv = document.createElement('div');
    taskDiv.className = 'task';
    taskDiv.innerHTML = `<strong>${title}</strong><br>${description}<br>Fecha Límite: ${dueDate}<br>Prioridad: ${priority}`;
    taskList.appendChild(taskDiv);

    document.getElementById('task-title').value = '';
    document.getElementById('task-description').value = '';
    document.getElementById('task-due-date').value = '';
    document.getElementById('task-priority').value = 'alta';
}