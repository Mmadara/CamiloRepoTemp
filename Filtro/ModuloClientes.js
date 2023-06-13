var listaClientes=[];

function addClientes(id,nombre,apellidos,telefono,correo,fecha,nacionalidad){
    var newClient={
        documento:id,
        nombre:nombre,
        apellidos:apellidos,
        telefono:telefono,
        correo:correo,
        fecha:fecha,
        nacionalidad:nacionalidad
    };
    console.log(newClient);
    listaClientes.push(newClient);
    LocalStorageCLientList(listaClientes);
}

function getClientList(){
    var storedList=localStorage.getItem('clientList');
    //Si esta vacia la lista del localstorage, entrega una lista vacias
    //si no, reemplaza por lo que este guardado en el localstorage
    if (storedList==null){
        listaClientes=[];
    }else{
        listaClientes=JSON.parse(storedList);
    }
    return listaClientes;
}

function LocalStorageCLientList(plist){
    localStorage.setItem('clientList',JSON.stringify(plist));
}