from flask_restful import Resource, reqparse
from models.carros import CarroModel
from models.proprietarios import ProprietarioModel


argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_carro', type=str, required=True, help="O campo 'nome_carro' não pode ser deixado em branco.")
argumentos.add_argument('modelo_id', type=str, required=True, help="O campo 'modelo_id' não pode ser deixado em branco.")
argumentos.add_argument('cor_id', type=str, required=True, help="O campo 'cor_id' não pode ser deixado em branco.")
argumentos.add_argument('ano', type=int, required=True, help="O campo 'ano' não pode ser deixado em branco.")
argumentos.add_argument('proprietario_id', type=int, required=True, help="O campo 'proprietario_id' não pode ser deixado em branco.")

class Carros(Resource):

    def get(self):
        carros = CarroModel.buscar_todos_carros()
        return carros

class Carro(Resource):

    def get(self, carro_id):
        
        carro = CarroModel.buscar_carro(carro_id)
        if carro:
            return carro.json()
        return {'mensagem': 'Carro não encontrado.'}, 404

    def put(self, carro_id):
        
        dados = argumentos.parse_args()

        carro_encontrado = CarroModel.buscar_carro(carro_id)
        if carro_encontrado:
            try:
                carro_encontrado.atualizar_carro(**dados)
                carro_encontrado.salvar_carro()
            except:
                return {'mensagem': 'Houve um erro tentando atualizar o carro.'}, 500
            return carro_encontrado.json(), 200

    def delete(self, carro_id):
        carro = CarroModel.buscar_carro(carro_id)

        if carro:
            try:
                carro.deletar_carro()
            except:
                return {'mensagem': 'Houve um erro tentando deletar o carro.'}, 500
            return {"mensagem":"Carro deletado com sucesso"}, 200
        return {'mensagem': 'Carro não encontrado.'}, 404

class CarroCadastro(Resource):

    def post(self):

        dados = argumentos.parse_args()
        carro = CarroModel(**dados)
        proprietario = ProprietarioModel.buscar_proprietario(dados.get('proprietario_id'))
        if proprietario:
            try:
                carro.salvar_carro()
            except:
                return {"mensagem":"Ocorreu um erro interno"}, 500
            return carro.json()
        return {"mensagem": "Esse proprietario não existe. Por favor insira um 'id' válido."}