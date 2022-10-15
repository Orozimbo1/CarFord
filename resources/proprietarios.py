from flask_restful import Resource, reqparse
from models.proprietarios import ProprietarioModel


argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser deixado em branco.")
argumentos.add_argument('sobrenome', type=str, required=True, help="O campo 'sobrenome' não pode ser deixado em branco.")

class Proprietarios(Resource):

    def get(self):
        proprietarios = ProprietarioModel.buscar_todos_proprietarios()
        return proprietarios

class Proprietario(Resource):

    def get(self, proprietario_id):
        
        proprietario = ProprietarioModel.buscar_proprietario(proprietario_id)
        if proprietario:
            return proprietario.json()
        return {'mensagem': 'Usuário  não encontrado.'}, 404

    def put(self, proprietario_id):
        
        dados = argumentos.parse_args()

        proprietario_encontrado = ProprietarioModel.buscar_proprietario(proprietario_id)
        if proprietario_encontrado:
            try:
                proprietario_encontrado.atualizar_proprietario(**dados)
                proprietario_encontrado.salvar_proprietario()
            except:
                return {'mensagem': 'Houve um erro tentando atualizar o usuário.'}, 500
            return proprietario_encontrado.json(), 200

    def delete(self, proprietario_id):
        proprietario = ProprietarioModel.buscar_proprietario(proprietario_id)

        if proprietario:
            try:
                proprietario.deletar_proprietario()
            except:
                return {'mensagem': 'Houve um erro tentando deletar o proprietário.'}, 500
            return {"mensagem":"Proprietário deletado com sucesso"}, 200
        return {'mensagem': 'Proprietário não encontrado.'}, 404


class ProprietarioCadastro(Resource):

    def post(self):

        dados = argumentos.parse_args()
        proprietario = ProprietarioModel(**dados)
        try:
            proprietario.salvar_proprietario()
        except:
            return {"mensagem":"Ocorreu um erro interno"}, 500
        return proprietario.json()