from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import CarroForm
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
    form = CarroForm()

    if form.validate_on_submit():
        novo_carro = Carro(
            marca=form.marca.data,
            modelo=form.modelo.data,
            nome=form.nome.data,
            ano=form.ano.data,
            preco=form.preco.data,
            img=form.img.data
        )
        db.session.add(novo_carro)
        db.session.commit()

        flash('Carro adicionado com sucesso!', 'success')
        return redirect(url_for('listarCarros'))

    return render_template('adicionar.html', form=form)


@app.route('/editar/<int:carro_id>', methods=['GET', 'POST'])
def editarCarro(carro_id):
    carro = Carro.query.get(carro_id)
    form = CarroForm(obj=carro)

    if form.validate_on_submit():
        carro.marca = form.marca.data
        carro.modelo = form.modelo.data
        carro.nome = form.nome.data
        carro.ano = form.ano.data
        carro.preco = form.preco.data
        carro.img = form.img.data

        db.session.commit()

        flash('Carro editado com sucesso!', 'success')
        return redirect(url_for('listarCarros'))

    return render_template('editar.html', carro=carro, form=form)


@app.route('/deletar/<int:carro_id>')
def deletarCarro(carro_id):
    carro = Carro.query.get(carro_id)
    db.session.delete(carro)
    db.session.commit()

    flash('Carro deletado com sucesso!', 'success')
    return redirect(url_for('listarCarros'))
