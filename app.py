import re
from datetime import datetime

from pegaversao import x

from zabbix import zabbix
from pagina_item import gera_pagina_item
from flask import (Flask ,render_template)


#from flask import (Flask, redirect, render_template, request,jsonify,
#                   send_from_directory, url_for)

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/grafico")
def pagina_grafico():
    return(render_template("teste_grafico.html"))


@app.route("/teste_api")
def pagina_oi():
    tabela = x()
    return(render_template("teste_api.html", tabela= tabela))

@app.route("/zabbix")
def pagina_zabbix():
    #tabela = x()
    return(zabbix())

@app.route("/item")
def pagina_item():
    pagina=gera_pagina_item()
    return(pagina)




@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content




