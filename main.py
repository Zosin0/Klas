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
    mysql = bd.SQL("root", "1234", "Klas")
    comando = "SELECT * FROM GrupoKlas;"
    imagens = ""
    cs = mysql.consultar(comando, [])
    for (idt, nome, desc, ra, path) in cs:
        imagens += "<TR>\n"
        imagens += f"<TD>{nome}</TD>\n"
        imagens += f"<TD>{ra}</TD>\n"
        imagens += f"<TD>{desc}</TD>\n"
        imagens += f"<TD><IMG SRC={path}></TD>\n"
        imagens += "</TR>\n"
    return render_template('times.html', imagens=imagens)


@app.route('/plataformas')
def plataformas():
    mysql = bd.SQL("root", "1234", "Klas")
    comando = 'select * from tbPlataformas;'
    cs = mysql.consultar(comando, [])
    dados = ''

    for (idt, nome, tipo, desc, link, path) in cs:
        dados += f"<TR>\n"
        dados += f"<TD>{nome}</TD>\n"
        dados += f"<TD>{tipo}</TD>\n"
        dados += f"<TD>{desc}</TD>\n"
        dados += f"<TD><a target=_blank href={link}\n"
        dados += f"<TD><IMG SRC={path} alt={nome}></TD></a>\n"
        dados += "</TR>\n"


    return render_template('plataformas.html', dados=dados)

@app.route('/linguagens')
def linguagens():
    mysql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
    comando = 'select * from linguagens;'
    cs = mysql.consultar(comando, [])
    infos = ''

    for (idt, nome, pop, sal, desc, path) in cs:
        infos += f"<TR>\n"
        infos += f"<TD>{nome}</TD>\n"
        infos += f"<TD>#{pop}</TD>\n"
        infos += f"<TD>{sal}</TD>\n"
        infos += f"<TD>{desc}</TD>\n"
        infos += f"<TD><IMG SRC={path} alt={nome}></TD>\n"
        infos += "</TR>\n"


    return render_template('linguagens.html', infos=infos)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    app.secret_key = 'não fale para ninguém!'
    email = firstName = password1 = password2 = None
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        # Terminar mensagens de erro.(Léo)
        if len(email) < 4:
            flash('Email inválido!', category='erro')

        elif len(firstName) < 2:
            flash('O nome precisa conter mais de duas letras!', category='erro')

        elif len(password1) < 8:
            flash('A senha deve conter pelo menos 8 caracteres!', category='erro')

        elif password2 != password1:
            flash('Senhas diferentes!', category='erro')

        else:
            flash('Conta criada!', category='sucesso')

        mysql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
        comando = 'insert into tbUsuarios(email_usuario, nome_usuario, senha_usuario) values(%s, %s, %s)'
        cs = mysql.executar(comando, (email, firstName, password1))


    return render_template('sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    dados = request.form

    return render_template('login.html', dados=dados)


app.run(debug=True)
