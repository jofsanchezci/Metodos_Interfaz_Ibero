// script.js

let data = [];
const form = document.getElementById('crudForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const dataTable = document.getElementById('dataTable');
const editIndexInput = document.getElementById('editIndex');

// Función para renderizar los datos en la tabla
function renderTable() {
    dataTable.innerHTML = '';
    data.forEach((item, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.email}</td>
            <td>
                <button class="edit" onclick="editRecord(${index})">Edit</button>
                <button class="delete" onclick="deleteRecord(${index})">Delete</button>
            </td>
        `;
        dataTable.appendChild(row);
    });
}

// Función para agregar o actualizar un registro
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = nameInput.value;
    const email = emailInput.value;
    const editIndex = editIndexInput.value;

    if (editIndex === '') {
        // Crear nuevo registro
        data.push({ name, email });
    } else {
        // Actualizar registro existente
        data[editIndex] = { name, email };
        editIndexInput.value = '';
    }

    form.reset();
    renderTable();
});

// Función para editar un registro
function editRecord(index) {
    nameInput.value = data[index].name;
    emailInput.value = data[index].email;
    editIndexInput.value = index;
}

// Función para eliminar un registro
function deleteRecord(index) {
    data.splice(index, 1);
    renderTable();
}

// Inicializar la tabla al cargar la página
renderTable();
