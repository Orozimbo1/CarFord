from database import Base, engine, session
from sqlalchemy import Column, String, Integer

class CorModel(Base):
    __tablename__ = 'cores'

    cor_id = Column(Integer)
    nome_cor = Column(String(80), primary_key=True)
    

    def __init__(self, nome_cor, cor_id):
        self.nome_cor = nome_cor
        self.cor_id = cor_id
    
    def json(self):
        return {
            'cor_id': self.cor_id,
            'nome_cor': self.nome_cor
        }
    

    @classmethod
    def buscar_todas_cores(cls):
        resultado = session.query(CorModel).all()
        cores = [cor.json() for cor in resultado]
        return cores

    @classmethod
    def buscar_cor(cls, cor_id):
        cor = session.query(CorModel).filter_by(cor_id=cor_id).first()

        if cor:
            return cor
        return None
    
    def atualizar_cor(self, nome_cor):
        self.nome_cor = nome_cor

    def salvar_cor(self):
        session.add(self)
        session.commit()

    def deletar_cor(self):
        
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
