/**
 * MÓDULO DE COMPRAS
 */


/**
 * INICIANDO...
 */
let rutas = [];
let editando = false;
let LS = window.localStorage;


// -- Traer rutas del Local Storage si existen
if (LS.getItem('rutas')) {
    rutas = JSON.parse(LS.getItem('rutas'));
}

imprimirTabla(rutas);


// Traer el form principal
const form = document.querySelector('#form-anadir');
form.addEventListener('submit', e => {
    e.preventDefault(); // Prevenir que se recargue la página enviando el form

    anadirRuta();
});


/**
 * FUNCIONES
 */

function anadirRuta() {
    const nombreRuta = document.querySelector('#nombreRuta').value;
    const valorTicket = document.querySelector('#valorTicket').value;
    const ciudadOrigen = document.querySelector('#ciudadOrigen').value;
    const ciudadDestino = document.querySelector('#ciudadDestino').value;
    const puntos = document.querySelector('#puntos').value;


    // Agregar al array
    const nuevoRuta = {
        id: editando === false ? Date.now() : editando, // Condición ternaria
        nombreRuta,
        valorTicket,
        ciudadOrigen,
        ciudadDestino,
        puntos
    }

    if (editando) {
        nuevoRuta.id = editando
        rutas = rutas.map(ruta => ruta.id === editando ? nuevoRuta : ruta)

        // Revierto los cambios en los titulos
        document.querySelector('#form-title').textContent = 'Añadir rutas'
        document.querySelector('#form-button').textContent = 'Añadir';

        editando = false;
    } else {
        rutas.push(nuevoRuta);
    }

    editando = false;

    // Guardar en LocalStorage
    LS.setItem('rutas', JSON.stringify(rutas));

    // Borra los inputs
    form.reset();

    // Imprimir tabla
    imprimirTabla(rutas);
}



function eliminarRuta(id) {
    rutas = rutas.filter(ruta => ruta.id !== id);

    // Guardar en LocalStorage
    LS.setItem('rutas', JSON.stringify(rutas));

    // Imprimir tabla
    imprimirTabla(rutas);

}



function cargarDatos(id) {
    // Cambiar titulos form
    document.querySelector('#form-title').textContent = 'Editar'
    document.querySelector('#form-button').textContent = 'Guardar Cambios';

    rutas.forEach(ruta => {
        if (ruta.id === id) {
            nombreRuta.value = ruta.nombreRuta
            valorTicket.value = ruta.valorTicket;
            ciudadOrigen.value = ruta.ciudadOrigen;
            ciudadDestino.value = ruta.ciudadDestino;
            puntos.value = ruta.puntos;
        }
    });

    editando = id;

}


function imprimirTabla(datos) {
    // Limpiar la tabla anterior
    const tabla = document.querySelector('#tabla-rutas');
    tabla.innerHTML = '';

    // Imprimir
    datos.forEach(ruta => {
        tabla.innerHTML += `
        <tr>
        <td>${ruta.id}</td>
        <td>${ruta.nombreRuta}</td>
        <td>${ruta.valorTicket}</td>
        <td>${ruta.ciudadOrigen}</td>
        <td>${ruta.ciudadDestino}</td>
        <td>${ruta.puntos}</td>
        <td>
            <div class="d-flex justify-content-center align-items-center">
                <button class="btn btn-primary me-1" onclick="cargarDatos(${ruta.id})">
                    <i class="bi bi-pencil-square"></i>
                </button>
                <button class="btn btn-danger" onclick="eliminarRuta(${ruta.id})">
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </td>
        </tr>
    `
    });
}