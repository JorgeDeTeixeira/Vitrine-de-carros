import logging
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from app import app, db
from app.forms import CarroForm
from app.models import Carro

# Configurar o sistema de logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

ITENS_POR_PAGINA = 6

def handle_error_and_redirect(route, error_message, redirect_route='index', log_error=True):
    flash(error_message, 'error')

    if log_error:
        logger.error(f'Error in {route}: {error_message}')

    return redirect(url_for(redirect_route))


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/carros')
def listarCarros():
    try:
        # Obter o número da página a partir dos parâmetros da requisição
        pagina = request.args.get('pagina', 1, type=int)

        # Paginação dos carros
        carros_paginados = Carro.query.paginate(page=pagina, per_page=ITENS_POR_PAGINA, error_out=False)

        return render_template('carros.html', carros=carros_paginados)
    except SQLAlchemyError as e:
        return handle_error_and_redirect('listarCarros', f'Erro ao listar carros: {str(e)}', log_error=True)


@app.route('/carro/<int:carro_id>')
def visualizarCarro(carro_id):
    try:
        carro = Carro.query.get(carro_id)
        if not carro:
            raise Exception(f'Carro com ID {carro_id} não encontrado')
        return render_template('carro.html', carro=carro)
    except SQLAlchemyError as e:
        return handle_error_and_redirect('visualizarCarro', f'Erro ao visualizar carro: {str(e)}', 'listarCarros')


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionarCarro():
    form = CarroForm()

    try:
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
    except SQLAlchemyError as e:
        return handle_error_and_redirect('adicionarCarro', f'Erro ao adicionar carro: {str(e)}', log_error=True)

    return render_template('adicionar.html', form=form)


@app.route('/editar/<int:carro_id>', methods=['GET', 'POST'])
def editarCarro(carro_id):
    carro = Carro.query.get(carro_id)
    form = CarroForm(obj=carro)

    try:
        if not carro:
            raise Exception(f'Carro com ID {carro_id} não encontrado')

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
    except SQLAlchemyError as e:
        return handle_error_and_redirect('editarCarro', f'Erro ao editar carro: {str(e)}', log_error=True)

    return render_template('editar.html', carro=carro, form=form)


@app.route('/deletar/<int:carro_id>')
def deletarCarro(carro_id):
    try:
        carro = Carro.query.get(carro_id)
        if not carro:
            raise Exception(f'Carro com ID {carro_id} não encontrado')

        db.session.delete(carro)
        db.session.commit()

        flash('Carro deletado com sucesso!', 'success')
        return redirect(url_for('listarCarros'))
    except SQLAlchemyError as e:
        return handle_error_and_redirect('deletarCarro', f'Erro ao deletar carro: {str(e)}', 'listarCarros')
