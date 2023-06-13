/**
 * MÓDULO DE CLIENTES
 */


/**
 * INICIANDO...
 */
let clientes = [];
let editando = false;
let LS = window.localStorage;


// -- Traer registros del Local Storage si existen
if (LS.getItem('clientes')) {
    clientes = JSON.parse(LS.getItem('clientes'));
}

imprimirTabla(clientes);


// Traer el form principal
const form = document.querySelector('#form-anadir');
form.addEventListener('submit', e => {
    e.preventDefault(); // Prevenir que se recargue la página enviando el form

    anadirCliente();
});

const inputBuscar = document.querySelector('#buscar');
inputBuscar.addEventListener('keyup', buscarClientes);

/**
 * FUNCIONES
 */

function anadirCliente() {
    const identificacion = document.querySelector('#identificacion').value;
    const nombres = document.querySelector('#nombres').value;
    const apellidos = document.querySelector('#apellidos').value;
    const telefono = document.querySelector('#telefono').value;
    const email = document.querySelector('#email').value;
    const fechaNacimiento = document.querySelector('#fechaNacimiento').value
    const nacionalidad = document.querySelector('#nacionalidad').value


    // Agregar al array
    const nuevoCliente = {
        id: editando === false ? Date.now() : editando, // Condición ternaria
        identificacion,
        nombres,
        apellidos,
        telefono,
        email,
        fechaNacimiento,
        nacionalidad,
        puntos: 0
    }

    if (editando) {
        nuevoCliente.id = editando
        clientes = clientes.map(cliente => cliente.id === editando ? nuevoCliente : cliente)

        // Revierto los cambios en los titulos
        document.querySelector('#form-title').textContent = 'Añadir Clientes'
        document.querySelector('#form-button').textContent = 'Añadir';

        editando = false;
    } else {
        clientes.push(nuevoCliente);
    }

    editando = false;

    // Guardar en LocalStorage
    LS.setItem('clientes', JSON.stringify(clientes));

    // Borra los inputs
    form.reset();

    // Imprimir tabla
    imprimirTabla(clientes);
}



function eliminarCliente(id) {
    clientes = clientes.filter(cliente => cliente.id !== id);

    // Guardar en LocalStorage
    LS.setItem('clientes', JSON.stringify(clientes));

    // Imprimir tabla
    imprimirTabla(clientes);

}



function cargarDatos(id) {
    // Cambiar titulos form
    document.querySelector('#form-title').textContent = 'Editar'
    document.querySelector('#form-button').textContent = 'Guardar Cambios';

    clientes.forEach(cliente => {
        if (cliente.id === id) {
            identificacion.value = cliente.identificacion
            nombres.value = cliente.nombres;
            apellidos.value = cliente.apellidos;
            telefono.value = cliente.telefono;
            email.value = cliente.email;
            fechaNacimiento.value = cliente.fechaNacimiento;
            nacionalidad.value = cliente.nacionalidad;
        }
    });

    editando = id;

}

function buscarClientes() {
    // Verificar que no esté vacío
    if (inputBuscar.value === '') {
        imprimirTabla(clientes);
    } else {
        if (isNaN(inputBuscar.value)) { // Estudiar!!!
            let busqueda = clientes.filter(function (cliente) {
                return (
                    cliente.apellidos.toLowerCase().includes(inputBuscar.value.toLowerCase()) ||
                    cliente.nombres.toLowerCase().includes(inputBuscar.value.toLowerCase())
                );
            });

            imprimirTabla(busqueda);
        } else {
            let busqueda = clientes.filter(function (cliente) {
                return cliente.identificacion.includes(inputBuscar.value);
            });

            imprimirTabla(busqueda);
        }
    }
}


function imprimirTabla(datos) {
    // Limpiar la tabla anterior
    const tabla = document.querySelector('#tabla-clientes');
    tabla.innerHTML = '';

    // Imprimir
    datos.forEach(cliente => {
        tabla.innerHTML += `
        <tr>
        <td>${cliente.identificacion}</td>
        <td>${cliente.nombres}</td>
        <td>${cliente.apellidos}</td>
        <td>${cliente.telefono}</td>
        <td>${cliente.email}</td>
        <td>${cliente.fechaNacimiento}</td>
        <td>${cliente.nacionalidad}</td>
        <td>
            <div class="d-flex justify-content-center align-items-center">
                <button class="btn btn-primary me-1" onclick="cargarDatos(${cliente.id})">
                    <i class="bi bi-pencil-square"></i>
                </button>
                <button class="btn btn-danger" onclick="eliminarCliente(${cliente.id})">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </td>
        </tr>
    `
    });
}