from flask_restful import Resource, reqparse
from models.cor_carro import CorModel


argumentos = reqparse.RequestParser()
argumentos.add_argument('nome_cor', type=str, required=True, help="O campo 'nome_cor' não pode ser deixado em branco.")

class Cores(Resource):

    def get(self):
        cores = CorModel.buscar_todas_cores
        return cores

class Cor(Resource):

    def get(self, cor_id):
        
        cor = CorModel.buscar_cor(cor_id)
        if cor:
            return cor.json()
        return {'mensagem': 'Cor não encontrada.'}, 404

    def put(self, cor_id):
        
        dados = argumentos.parse_args()

        cor_encontrado = CorModel.buscar_cor(cor_id)
        if cor_encontrado:
            try:
                cor_encontrado.atualizar_cor(**dados)
                cor_encontrado.salvar_cor()
            except:
                return {'mensagem': 'Houve um erro tentando atualizar a cor.'}, 500
            return cor_encontrado.json(), 200

    def delete(self, cor_id):
        cor = CorModel.buscar_cor(cor_id)

        if cor:
            try:
                cor.deletar_cor()
            except:
                return {'mensagem': 'Houve um erro tentando deletar a cor.'}, 500
            return {"mensagem":"Cor deletada com sucesso"}, 200
        return {'mensagem': 'Cor não encontrada.'}, 404

class CorCadastro(Resource):

    def post(self):

        dados = argumentos.parse_args()
        cor = CorModel(**dados)
        try:
            cor.salvar_cor()
        except:
            return {"mensagem":"Ocorreu um erro interno"}, 500
        return cor.json()