from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from database import engine
from resources.carros import Carros, Carro, CarroCadastro
from resources.proprietarios import Proprietarios, Proprietario, ProprietarioCadastro
from resources.cor_carro import Cores, Cor, CorCadastro
from resources.modelo import Modelos, Modelo, ModeloCadastro


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.route('/')
def Hello():
    return '<h1>Olá, Sejam bem vindos à CarFord!</h1>'

api.add_resource(Carros, '/carros')
api.add_resource(Carro, '/carro/<int:carro_id>')
api.add_resource(CarroCadastro, '/carro-cadastro')
api.add_resource(Proprietarios, '/proprietarios')
api.add_resource(Proprietario, '/proprietario/<int:propriedade_id>')
api.add_resource(ProprietarioCadastro, '/proprietario-cadastro')
api.add_resource(Cores, '/cores')
api.add_resource(Cor, '/cor/<int:cor_id>')
api.add_resource(CorCadastro, '/cor-cadastro')
api.add_resource(Modelos, '/modelos')
api.add_resource(Modelo, '/modelo/<int:modelo_id>')
api.add_resource(ModeloCadastro, '/modelo-cadastro')

if __name__ == '__main__':
    app.run(debug=True)