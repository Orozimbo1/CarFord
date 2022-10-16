function app() {
    let cardUsuario = document.querySelector("#cardUsuario")
    let cardCarro = document.querySelector("#cardCarro")
    let carProp = document.querySelector("#carProp")
    let cadastroProprietario = document.querySelector("#cadastroProprietario")
    let cadastroCarro = document.querySelector("#cadastroProprietario")
    let dadosProprietario = document.querySelector("#dadosProprietario")
    let dadosCarro = document.querySelector("#dadosCarro")
    let formProprietario = document.querySelector("#formProprietario")
    let formCarro = document.querySelector("#formCarro")
    let cor_carro = document.querySelector("#cor_carro")
    let modelo_carro = document.querySelector("#modelo_carro")
    let btnCarro = document.querySelector("#btn-carro")
    let btnProp = document.querySelector("#btn-prop")

    const proprietarios = (resultado) => {
        for (let elemento of resultado) {
            let proprietarios = []
            let div = document.createElement("div")
            let h5 = document.createElement("h5")
            for (let topico in elemento) {
                proprietarios.push(elemento[topico])
            }
            h5Text = document.createTextNode(proprietarios[1] + " " + proprietarios[2])
            h5.appendChild(h5Text)
            div.appendChild(h5)
            carros(proprietarios[3], div, "col-10")
            cardUsuario.appendChild(div)
        }
    }

    function apiProprietarios() {
        let url = 'http://127.0.0.1:5000/proprietarios'

        const options = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        }

        fetch(url, options)
            .then((response) => {
                response.json()
                    .then(data => {
                        proprietarios(data)
                    })
            }).catch((e) => {
                console.log(e)
            })
    }

    const carros = (resultado, divPar, width) => {
        for (let elemento of resultado) {
            let div = document.createElement("div")
            div.classList.add(width)
            let ul = document.createElement("ul")
            div.appendChild(ul)
            for (let topico in elemento) {
                let li = document.createElement("li")
                liText = document.createTextNode(elemento[topico])
                li.appendChild(liText)
                ul.appendChild(li)
            }
            divPar.appendChild(div)
        }
    }

    function apiCarros() {
        let url = 'http://127.0.0.1:5000/carros'

        const options = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        }

        fetch(url, options)
            .then((response) => {
                response.json()
                    .then(data => {
                        carros(data, cardCarro, "col-6")
                    })
            }).catch((e) => {
                console.log(e)
            })
    }

    const modelos = (resultado) => {
        for (let elemento of resultado) {
            let option = document.createElement("option")
            let optionText = document.createTextNode(elemento.nome_modelo)
            option.appendChild(optionText)
            modelo_carro.appendChild(option)
        }
    }

    function apiModelos() {
        let url = 'http://127.0.0.1:5000/modelos'

        const options = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        }

        fetch(url, options)
            .then((response) => {
                response.json()
                    .then(data => {
                        modelos(data)
                    })
            }).catch((e) => {
                console.log(e)
            })
    }

    const cores = (resultado) => {
        for (let elemento of resultado) {
            let option = document.createElement("option")
            let optionText = document.createTextNode(elemento.nome_cor)
            option.appendChild(optionText)
            cor_carro.appendChild(option)
        }
    }

    function apiCores() {
        // Consumindo api cores
        let url = 'http://127.0.0.1:5000/cores'

        const options = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        }

        fetch(url, options)
            .then((response) => {
                response.json()
                    .then(data => {
                        cores(data)
                    })
            }).catch((e) => {
                console.log(e)
            })
    }

    function apiCadastroProp() {
        event.preventDefault()
        let url = 'http://127.0.0.1:5000/proprietario-cadastro'

        let nome = document.querySelector("#nome").value
        let sobrenome = document.querySelector("#sobrenome").value

        body = {
            "nome": nome,
            "sobrenome": sobrenome
        }

        let request = new XMLHttpRequest()
        request.open("POST", url, true)
        request.setRequestHeader("Content-type", "application/json")
        request.send(JSON.stringify(body))

        request.onload = function () {

            console.log(this.responseText)
        }
        return request.responseText
    }


    function apiCadastroCarro() {
        event.preventDefault()
        let url = 'http://127.0.0.1:5000/carro-cadastro'

        let nome_carro = document.querySelector("#nome_carro").value
        let ano_carro = document.querySelector("#ano_carro").value
        let proprietario_carro = document.querySelector("#proprietario_carro").value
        console.log(nome_carro, ano_carro, proprietario_carro)

        body = {
            "nome_carro": nome_carro,
            "modelo_carro": modelo_carro.value,
            "cor_carro": cor_carro.value,
            "ano": ano_carro,
            "proprietario_id": proprietario_carro
        }

        let request = new XMLHttpRequest()
        request.open("POST", url, true)
        request.setRequestHeader("Content-type", "application/json")
        request.send(JSON.stringify(body))

        request.onload = function () {
            console.log(this.responseText)

        }
        return request.responseText
    }

    btnProp.addEventListener("click", () => {
        apiCadastroProp()
    })

    btnCarro.addEventListener("click", () => {
        apiCadastroCarro()
    })

    apiCores()
    apiModelos()
    apiCarros()
    apiProprietarios()

}

app()