import mysql.connector
from util import bd
import os
from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

UPLOAD_FOLDER = 'C:\\temp\\Klas\\Klas\\static\\imagens'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

main = Blueprint('main', __name__)
app.secret_key = 'projetinho pai'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def menu():
    return render_template('home.html')


@app.route('/times')
def times():
    # Consultando dados na tabela
    sql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
    comando = "SELECT * FROM GrupoKlas;"
    imagens = ""
    cs = sql.consultar(comando, [])
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
    sql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
    comando = 'select * from tbPlataformas;'
    cs = sql.consultar(comando, [])
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
    sql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
    comando = 'select * from linguagens;'
    cs = sql.consultar(comando, [])
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


@app.route('/cursos')
def cursos():
    return render_template('cursos.html', cursos=cursos)


@app.route('/cursos_pagos')
def cursos_pagos():
    sql = bd.SQL("lucas", "1234", "Klas")
    comando = 'select idCursoPago, nmeCursoPago, descCursoPago, link_curso_pago from tbCursoPago;'
    cs = sql.consultar(comando, [])
    cursosp = ''

    for (idt, nome, desc, link) in cs:
        cursosp += f"<TR>\n"
        cursosp += f"<TD>{nome}</TD>\n"
        cursosp += f"<TD>#{desc}</TD>\n"
        cursosp += f"<TD>{link}</TD>\n"
        cursosp += "</TR>\n"

    return render_template('cursos_pagos.html', cursosp=cursosp)


@app.route('/cursos_gratis')
def cursos_gratis():
    sql = bd.SQL("lucas", "1234", "Klas")
    comando = 'select idCursoGratis, nmeCursoGratis, descCursoGratis, link_curso_Gratis from tbCursoGratis;'
    cs = sql.consultar(comando, [])
    cursosg = ''

    for (idt, nome, desc, link) in cs:
        cursosg += f"<TR>\n"
        cursosg += f"<TD>{nome}</TD>\n"
        cursosg += f"<TD>#{desc}</TD>\n"
        cursosg += f"<TD>{link}</TD>\n"
        cursosg += "</TR>\n"

    return render_template('cursos_gratis.html', cursosg=cursosg)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    sql = bd.SQL('root', 'a3m5vKu6vznNXTp', 'Klas')
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email inválido!', category='erro')

        elif len(firstName) < 2:
            flash('O nome precisa conter mais de duas letras!', category='erro')

        elif len(password1) < 8:
            flash('A senha deve conter pelo menos 8 caracteres!', category='erro')

        elif password2 != password1:
            flash('Senhas diferentes!', category='erro')

        else:
            sql = bd.SQL("root", "a3m5vKu6vznNXTp", "Klas")
            comando = 'insert into tbUsuarios(email_usuario, nome_usuario, senha_usuario) values(%s, %s, %s)'
            try:
                cs = sql.executar(comando, (email, firstName, password1))
                flash('Conta criada!', category='sucesso')
                return redirect('/login')

            except mysql.connector.IntegrityError:
                flash('Email já cadastrado!', category='erro')

    return render_template('sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Ainda precisa de requintes

    if request.method == 'POST':
        sql = bd.SQL('root', 'a3m5vKu6vznNXTp', 'Klas')
        email = request.form.get('email')
        senha = request.form.get('password')
        row = sql.consultar('select * from tbUsuarios where email_usuario=%s and senha_usuario=%s',
                            (email, senha)).fetchone()

        if row:
            flash('Login efetuado com sucesso!', category='sucesso')
            return redirect('/')

        else:
            flash('Email ou senha inválidos.', category='erro')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
