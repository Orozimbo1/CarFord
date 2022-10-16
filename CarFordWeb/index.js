let proprietarios = document.querySelector("#proprietarios")
let carros = document.querySelector("#carros")
let cadastroProprietario = document.querySelector("#cadastroProprietario")
let cadastroCarro = document.querySelector("#cadastroProprietario")
let dadosProprietario = document.querySelector("#dadosProprietario")
let dadosCarro = document.querySelector("#dadosCarro")
let formProprietario = document.querySelector("#formProprietario")
let formCarro = document.querySelector("#formCarro")
let topicos = document.querySelectorAll(".topicos")
let conteudo = document.querySelectorAll(".conteudo")
let aoba = document.querySelector(".aoba")

function desativarTopicos(){
    for(let i=0; i <= topicos.length; i++){
        topicos[i].classList.remove("active")
    }
}

aoba.addEventListener("click", () => {
    ocultarConteudo()
})

// desativarTopicos()

function ocultarConteudo(){
    for(let i = 0; i <= conteudo.length; i++){
        conteudo[i].classList.add("d-none")
    }
}

proprietarios.addEventListener("click", () => {
    // desativarTopicos()
    // ocultarConteudo()
    // proprietarios.classList.add("active")
    formCarro.classList.remove("d-none")
})
let url = 'http://127.0.0.1:5000/cores'

fetch(url)
    .then((data) => {
        data.json    
    }).catch((e) => {
        console.log(e)
    })