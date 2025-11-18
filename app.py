from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Olá, mundo!</h1>'
    return render_template('index.html')


@app.route('/sobre_equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

@app.route('/lista_termos')
def lista_termos():
    return render_template('glossario.html')

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')
app.run()