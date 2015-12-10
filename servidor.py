from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
		return render_template("taquitosIndex.html")

@app.route("/taquitosIndex.html")
def taquitos():
		return render_template("taquitosIndex.html")

@app.route("/Inicio.html")
def inicio():
		return render_template("inicio.html")

@app.route("/Promociones.html")
def promociones():
		return render_template("promociones.html")

@app.route("/Contacto.html")
def contacto():
		return render_template("contacto.html")

if __name__=='__main__':
	app.run(debug=True)

		
