import warnings

from util import bd
from flask import render_template, flash, request, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from __init__ import create_app, db
from classes import User


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

main = Blueprint('main', __name__)
app = create_app()



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/')
def menu():
    return render_template('home.html', user=current_user)


@main.route('/times')
@login_required
def times():
    # Consultando dados na tabela
    sql = bd.SQL("root", "1234", "Klas")
    comando = "SELECT * FROM GrupoKlas;"
    imagens = ""
    cs = sql.consultar(comando, [])
    headings = ("Nome", "RA", "Função", "Foto")
    for (idt, nome, desc, ra, path) in cs:
        imagens += "<TR>\n"
        imagens += f"<TD>{nome}</TD>\n"
        imagens += f"<TD>{ra}</TD>\n"
        imagens += f"<TD>{desc}</TD>\n"
        imagens += f"<TD><IMG SRC={path}></TD>\n"
        imagens += "</TR>\n"
    return render_template('times.html', imagens=imagens, headings=headings, user=current_user)


@main.route('/plataformas')
@login_required
def plataformas():
    sql = bd.SQL("root", "1234", "Klas")
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

    return render_template('plataformas.html', dados=dados, user=current_user)


@main.route('/linguagens')
@login_required
def linguagens():
    sql = bd.SQL("root", "1234", "Klas")
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

    return render_template('linguagens.html', infos=infos, user=current_user)


@main.route('/cursos')
@login_required
def cursos():
    return render_template('cursos.html', cursos=cursos, user=current_user)


@main.route('/cursos_pagos')
@login_required
def cursos_pagos():
    sql = bd.SQL("root", "1234", "Klas")
    comando = 'SELECT C.nmeCursoPago, C.descCursoPago, C.link_curso_pago, P.dsc_path_imagem_plataformas FROM tbcursopago C INNER JOIN tbplataformas P ON P.idPlataformas = C.cod_plataforma;'
    cs = sql.consultar(comando, [])
    cursosp=''
    for (idt, nome, desc, link, path) in cs:
        cursosp = '''
              <div class="curso-2">
                <h1>{}</h1>
                <h3>{}</h3>
                <a href={}><img src={}/>  </a>
            </div>
        
        '''.format(nome, desc, link, path)

    return render_template('cursos_pagos.html', cursosp=cursosp, user=current_user)


@main.route('/cursos_gratis')
@login_required
def cursos_gratis():
    sql = bd.SQL("root", "1234", "Klas")
    comando = 'select idCursoGratis, nmeCursoGratis, descCursoGratis, link_curso_Gratis from tbCursoGratis;'
    cs = sql.consultar(comando, [])
    cursosg = ''

    for (idt, nome, desc, link) in cs:
        cursosg+='''
        <div class ="curso-1">
        <h1 style="text-align: justify; padding-bottom: 20px;"> {} </h1>
        <h3 style="text-align: justify; padding-bottom: 20px;"> {} </h3>
        <iframe
        width = "560"
        height = "315"
        src = "{}"
        title = "YouTube video player"
        frameborder = "0"
        allow = "accelerometer; autoplay;
        clipboard - write;
        encrypted - media;
        gyroscope;
        picture - in -picture"
        allowfullscreen></iframe>
        </div>
     '''.format(nome, desc, link)


    return render_template('cursos_gratis.html', cursosg=cursosg, user=current_user)


@main.route('/registro', methods=['GET', 'POST'])
def registro():
    sql = bd.SQL('root', '1234', 'Klas')
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email já cadastrado.', category='erro')

        elif len(email) < 4:
            flash('Email inválido!', category='erro')

        elif len(firstName) < 2:
            flash('O nome precisa conter mais de duas letras!', category='erro')

        elif len(password1) < 8:
            flash('A senha deve conter pelo menos 8 caracteres!', category='erro')

        elif password2 != password1:
            flash('Senhas diferentes!', category='erro')

        else:
            novo_usuario = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Conta criada com sucesso!', category='sucesso')
            return redirect('/')


    return render_template('sign_up.html', user=current_user)


@main.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        sql = bd.SQL('root', '1234', 'Klas')
        email = request.form.get('email')
        senha = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, senha):
                flash('Login efetuado com sucesso!', category='sucesso')
                login_user(user, remember=True)
                return redirect('/')

            else:
                flash('Email ou senha inválidos.', category='erro')

        else:
            flash('Email ou senha inválidos.', category='erro')

    return render_template('login.html', user=current_user)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
