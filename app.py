from flask import Flask, render_template, redirect, request
import random

app= Flask(__name__)


@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobre", methods=["GET"])
def sobre_mim ():
    return render_template("sobre.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
   usuario = request.form.get ("usuario")
   senha= request.form.get ("senha")

   if usuario == "Helena" and senha == "1234":
       return "Voce acessou a pagina restrita"
   else: 
       return render_template ("login.html", erro = "Acesso Negado!")
   





app.run(debug=True)

