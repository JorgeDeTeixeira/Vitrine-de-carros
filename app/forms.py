# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CarroForm(FlaskForm):
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    ano = IntegerField('Ano', validators=[DataRequired(), NumberRange(min=1800, max=3000)])
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    img = StringField('URL da Imagem', validators=[DataRequired()])
    submit = SubmitField('Adicionar Carro')
