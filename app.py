from flask import Flask, render_template, flash, url_for, redirect, request
import os
import cgi

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': 'Evolux <3 Python',
    'DEBUG': True
})

@app.route("/<nome>")
def hello(nome):
    return "Bar Cadastrado com Sucesso! <br/> %s" % nome

@app.route("/", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        if request.form.get('nome'):
            salvar()                                       
        else:
            flash('Insira os Dados para Cadastrar')
    return render_template("index.html")

def salvar():
    with open("db/db.txt", "a") as text_file:
        text_file.write('\n')
        text_file.write('Cadastro do Bar')
        text_file.write('\n')
        text_file.write(request.form.get('nome'))
        text_file.write('\n')
        text_file.write(request.form.get('endereco'))
        text_file.write('\n')
        text_file.write(request.form.get('funcionamento'))
        text_file.write('\n')
        text_file.write(request.form.get('especialidade'))
        text_file.write('\n')
        text_file.write('----------------------------------')
        
        
if __name__ == "__main__":
    app.run(debug=True)