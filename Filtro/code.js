let btnAdd=document.querySelector('#btnAdd');
let cont=0;
btnAdd.addEventListener('click',saveClient)


function saveClient(){
    let form=document.querySelector('#form');
    let sId = form.id.value;
        sName = form.nombre.value;   
        sApellido = form.apellido.value; 
        sTelefono = form.telefono.value;
        sCorreo = form.correo.value;  
        sFecha = form.fecha.value  
        sNacionalidad = form.nacionalidad.value;
        
        addClientes(sId,sName,sApellido,sTelefono,sCorreo,sFecha,sNacionalidad)
        mostrarClientes();
} 
jk
function mostrarClientes(){
    cont+=1;
    let list=getClientList();
        tbody=document.querySelector('#clientes tbody');
    tbody.innerHTML='';

    for(let i=0;i<list.length;i++){
        var  row=tbody.insertRow(i),
            docCell=row.insertCell(0),
            nameCell=row.insertCell(1),
            apellidoCell=row.insertCell(2),
            telCell=row.insertCell(3),
            correoCell=row.insertCell(4),
            fechaCell=row.insertCell(5),
            nacioCell=row.insertCell(6),
            selectCell =row.insertCell(7);

        docCell.innerHTML=list[i].documento;
        nameCell.innerHTML=list[i].nombre;
        apellidoCell.innerHTML=list[i].apellidos;
        telCell.innerHTML=list[i].telefono;
        correoCell.innerHTML=list[i].correo;
        fechaCell.innerHTML=list[i].fecha;
        nacioCell.innerHTML=list[i].nacionalidad;
        
        var inputSelect=document.createElement('input'); 
        inputSelect.type='radio';
        inputSelect.value=list[i].cont;
        selectCell.appendchild(inputSelect);
        tbody.appendchild(row);
    }

}

