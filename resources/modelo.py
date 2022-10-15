from flask_restful import Resource, reqparse
from models.modelo import ModeloModel


argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_modelo', type=str, required=True, help="O campo 'nome_modelo' não pode ser deixado em branco.")

class Modelos(Resource):

    def get(self):
        modelos = ModeloModel.buscar_todos_modelos()
        return modelos

class Modelo(Resource):

    def get(self, modelo_id):
        
        modelo = ModeloModel.buscar_modelo(modelo_id)
        if modelo:
            return modelo.json()
        return {'mensagem': 'Modelo não encontrado.'}, 404

    def put(self, modelo_id):
        
        dados = argumentos.parse_args()

        modelo_encontrado = ModeloModel.buscar_modelo(modelo_id)
        if modelo_encontrado:
            try:
                modelo_encontrado.atualizar_modelo(**dados)
                modelo_encontrado.salvar_modelo()
            except:
                return {'mensagem': 'Houve um erro tentando atualizar o modelo.'}, 500
            return modelo_encontrado.json(), 200

    def delete(self, modelo_id):
        modelo = ModeloModel.buscar_modelo(modelo_id)

        if modelo:
            try:
                modelo.deletar_modelo()
            except:
                return {'mensagem': 'Houve um erro tentando deletar o modelo.'}, 500
            return {"mensagem":"Modelo deletado com sucesso"}, 200
        return {'mensagem': 'Modelo não encontrado.'}, 404

class ModeloCadastro(Resource):

    def post(self):

        dados = argumentos.parse_args()
        modelo = ModeloModel(**dados)
        try:
            modelo.salvar_modelo()
        except:
            return {"mensagem":"Ocorreu um erro interno"}, 500
        return modelo.json()