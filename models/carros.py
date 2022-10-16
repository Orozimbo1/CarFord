from ast import Str
from database import Base, engine, session
from sqlalchemy import Column, String, Integer, ForeignKey
from models.modelo import ModeloModel
from models.cor_carro import CorModel
from models.proprietarios import ProprietarioModel

class CarroModel(Base):
    __tablename__ = 'carros'

    carro_id = Column(Integer, primary_key=True)
    nome_carro = Column(String(80))
    modelo_carro = Column(String, ForeignKey(ModeloModel.nome_modelo))
    cor_carro = Column(String, ForeignKey(CorModel.nome_cor))
    ano = Column(Integer)
    proprietario_id = Column(Integer, ForeignKey(ProprietarioModel.proprietario_id))    

    def __init__(self, nome_carro, modelo_carro, cor_carro, ano, proprietario_id):
        self.nome_carro = nome_carro
        self.modelo_carro = modelo_carro
        self.cor_carro = cor_carro
        self.ano = ano
        self.proprietario_id = proprietario_id
    
    def json(self):
        return {
            'carro_id': self.carro_id,
            'nome_carro': self.nome_carro,
            'modelo_carro': self.modelo_carro,
            'cor_carro': self.cor_carro,
            'ano': self.ano,
            'proprietario_id': self.proprietario_id
        }
    

    @classmethod
    def buscar_todos_carros(cls):
        resultado = session.query(CarroModel).all()
        carros = [carro.json() for carro in resultado]
        return carros

    @classmethod
    def buscar_carro(cls, carro_id):
        carro = session.query(CarroModel).filter_by(carro_id=carro_id).first()

        if carro:
            return carro
        return None

    @classmethod
    def buscar_carros_por_usuario(cls, proprietario_id):
        resultado = session.query(CarroModel).filter_by(proprietario_id=proprietario_id).all()
        carros = [carro.json() for carro in resultado]
        return carros
    
    def atualizar_carro(self, nome_carro, modelo_carro, cor_carro, ano, proprietario_id):
        self.nome_carro = nome_carro
        self.modelo_carro = modelo_carro
        self.cor_carro = cor_carro
        self.ano = ano
        self.proprietario_id = proprietario_id

    def salvar_carro(self):
        session.add(self)
        session.commit()

    def deletar_carro(self):
        
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
