// Requisição no Frontend com JS
const api = 'http://127.0.0.1:8000/'

let btnUserAccess = document.querySelector('button#btnUserAccess')

// a div que mostra as informações do usuário
let divUserAll = document.querySelector('div.client')
let divUserName = document.querySelector('label#userName')

// Inputs de usuário
let nameInp = document.getElementById('name')
let cpfInp = document.getElementById('cpf')
let emailInput = document.querySelector('input#email')
let dateInp = document.querySelector('input#date')
let passInp = document.querySelector("input#password")

async function getUser(data){
    try{
    const response = await fetch(`http://127.0.0.1:8000/users/${data.id}`,{
        method: 'GET',
        headers: {"Content-Type":'application/json'}
    }
    
)
       if(!response.ok){
            const jsonError = await response.json()
            console.error('Erro! ',jsonError.status)
            return
       }
   
        return response.json()
}catch(err){
    console.error("Erro durante o retorno da requisição:  ",err.message)
}
}


async function loginUser(){
    const response = await fetch(api,{
        method: 'POST',
        headers:{'Content-type':'application/json;charset=UTF-8'},
        body: JSON.stringify({
            name: nameInp.value,
            cpf: cpfInp.value,
            email: emailInput.value,
            date_nasc: dateInp.value,
            password: passInp
        })
    })

    if(!response.ok){
        let response_json = await response.json()
        throw new Error(`erro detectado durante o acesso ${response.status}:${response_json.message} `)
    }
    
    return await response.json()
}


async function registerUser(){
    const response = await fetch(api,{
        method:"POST",
        headers: {"Content-type":"application/json;charset=UTF-8"},
        body: JSON.stringify(data)
    })

}

btnUserAccess.onclick = async() => {
    try{
        window.alert("Bem vindo ao Finance!!")
    }catch(error){
        window.alert(`Erro: ${error.message} `)
    }
}