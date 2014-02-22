from flask import Flask, render_template, flash, url_for, redirect, request

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'Evolux <3 Python',
    'DEBUG': True
})

@app.route("/", methods=['GET', 'POST'])
def cadastro():
    if request.methods == 'POST':
	 	if request.form.get('nome'):
			return redirect(
				url_for(
					'Bar Cadastrado!', nome=request.form.get('nome')  
				)
			)
		else:
			flash('Insira os Dados Para Cadastro')

    return render_template("index.html")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
