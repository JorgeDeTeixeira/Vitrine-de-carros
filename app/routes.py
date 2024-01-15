from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Carro


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/carros')
def listarCarros():
    carros = Carro.query.all()
    return render_template('carros.html', carros=carros)


@app.route('/carro/<int:carro_id>')
def visualizarCarro(carro_id):
    carro = Carro.query.get(carro_id)
    return render_template('carro.html', carro=carro)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionarCarro():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        nome = request.form['nome']
        ano = int(request.form['ano'])
        preco = float(request.form['preco'])
        img = request.form['img']

        novo_carro = Carro(marca=marca, modelo=modelo,
                           nome=nome, ano=ano, preco=preco, img=img)
        db.session.add(novo_carro)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adicionar.html')


@app.route('/editar/<int:carro_id>', methods=['GET', 'POST'])
def editarCarro(carro_id):
    carro = Carro.query.get(carro_id)

    if request.method == 'POST':
        carro.marca = request.form['marca']
        carro.modelo = request.form['modelo']
        carro.nome = request.form['nome']
        carro.ano = int(request.form['ano'])
        carro.preco = float(request.form['preco'])
        carro.img = request.form['img']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', carro=carro)


@app.route('/deletar/<int:carro_id>')
def deletarCarro(carro_id):
    carro = Carro.query.get(carro_id)
    db.session.delete(carro)
    db.session.commit()

    return redirect(url_for('index'))

