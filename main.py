from util import bd
import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\temp\\Klas\\Klas\\static\\imagens'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def menu():
    return render_template('home.html')


@app.route('/times')
def times():
    # Consultando dados na tabela
    mysql = bd.SQL("lucas", "1234", "Klas")
    comando = "SELECT * FROM GrupoKlas;"
    imagens = ""
    cs = mysql.consultar(comando, [])
    for (idt, nme, desc, ra, path) in cs:
        imagens += "<TR>\n"
        imagens += "<TD>" + nme + "</TD>\n"
        imagens += "<TD>" + ra + "</TD>\n"
        imagens += "<TD>" + desc + "</TD>\n"
        imagens += "<TD><IMG SRC='" + path + "'></TD>\n"
        imagens += "</TR>\n"
    return render_template('times.html', imagens=imagens)


@app.route('/plataformas')
def plataformas():
    mysql = bd.SQL("lucas", "1234", "Klas")
    comando = 'select * from tbPlataformas;'
    cs = mysql.consultar(comando, [])
    dados = ''

    for (idt, nome, tipo, desc, link, path) in cs:
        dados += "<TR>\n"
        dados += "<TD>" + nome + "</TD>\n"
        dados += "<TD>" + tipo + "</TD>\n"
        dados += "<TD>" + desc + "</TD>\n"
        dados += "<TD><IMG SRC=" + path + "></TD>\n"
        dados += "</TR>\n"

    return render_template('plataformas.html', dados=dados)


app.run(debug=True)
