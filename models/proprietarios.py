from database import Base, engine, session
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class ProprietarioModel(Base):
    __tablename__ = 'proprietarios'

    proprietario_id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    sobrenome = Column(String(80))
    carros = relationship('CarroModel', backref="proprietarios")
    

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def json(self):
        return {
            'proprietario_id': self.proprietario_id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'carros': [carro.json() for carro in self.carros]
        }
    

    @classmethod
    def buscar_todos_proprietarios(cls):
        resultado = session.query(ProprietarioModel).all()
        proprietarios = [proprietario.json() for proprietario in resultado]
        return proprietarios

    @classmethod
    def buscar_proprietario(cls, proprietario_id):
        proprietario = session.query(ProprietarioModel).filter_by(proprietario_id=proprietario_id).first()

        if proprietario:
            return proprietario
        return None

    def salvar_proprietario(self):
        session.add(self)
        session.commit()

    def atualizar_usuario(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def deletar_proprietario(self):
        [carro.deletar.carro() for carro in self.carros]
        
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
