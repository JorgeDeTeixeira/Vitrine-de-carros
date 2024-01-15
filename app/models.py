from app import db


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Carro {self.marca} {self.modelo} ({self.ano})'
