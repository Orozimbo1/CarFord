from database import Base, engine, session
from sqlalchemy import Column, String, Integer

class ModeloModel(Base):
    __tablename__ = 'modelos'

    nome_modelo = Column(String(80), primary_key=True)
    

    def __init__(self, nome_modelo):
        self.nome_modelo = nome_modelo
    
    def json(self):
        return {
            'nome_modelo': self.nome_modelo
        }
    

    @classmethod
    def buscar_todos_modelos(cls):
        resultado = session.query(ModeloModel).all()
        modelos = [modelo.json() for modelo in resultado]
        return modelos

    @classmethod
    def buscar_modelo(cls, nome_modelo):
        modelo = session.query(ModeloModel).filter_by(nome_modelo=nome_modelo).first()

        if modelo:
            return modelo
        return None
    
    def atualizar_modelo(self, nome_modelo):
        self.nome_modelo = nome_modelo

    def salvar_modelo(self):
        session.add(self)
        session.commit()

    def deletar_modelo(self):
        
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
