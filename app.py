from flask import Flask, render_template
import random

app= Flask(__name__)


@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobre")
def sobre_mim ():
    return render_template("sobre.html")



app.run(debug=True)

