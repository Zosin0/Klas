import warnings

from util import bd
from flask import render_template, flash, request, redirect, Blueprint, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from __init__ import create_app, db, mail
from classes import User
from flask_mail import Message



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
    sql = bd.SQL("root", "uniceub", "Klas")
    comando = "SELECT idAluno, nmeAluno, dsc_path_imagem_aluno, raAluno, descAluno FROM GrupoKlas;"
    imagens = ""
    cs = sql.consultar(comando, [])
    headings = ("Nome", "RA", "Função", "Foto")
    for (idt, nome, path, ra, desc) in cs:
        imagens += f'''
                <div class="fotos-desc">
                      <div class="itens-3">
                          <h2 class="nome-aluno">{nome}</h2>
                          <img class="foto-aluno" src="{path}"/>
                          <p class="ra-aluno">{ra}</p>
                      </div>
                      <div class="main-desc">
                          <h3 class="descricao-aluno">
                            {desc}
                          </h3>
                      </div>
                </div>  
        '''


    return render_template('times.html', imagens=imagens, headings=headings, user=current_user)


@main.route('/plataformas')
@login_required
def plataformas():
    sql = bd.SQL("root", "uniceub", "Klas")
    comando = 'select * from tbPlataformas;'
    dados = ""
    cs = sql.consultar(comando, [])
    for (idt, nome, tipo, desc, link, path) in cs:
        dados += f'''
                            <div class="texto-x-imagem">
                            <div class="textos-cursop">
                                <div class="nome-cursop"><a href="">
                                    <h1>{nome}</h1></a></div>
                                <div class="desc-cursop"><h2>{desc}</h2> </div> <br/>
                                <div class="link-cursop"><h3>{tipo}</h3></div>
                            </div>
                            <div class="imagens-cursop">
                                <a href= "{link}">
                                <img style="height: auto; widht: auto;"
                                     src="{path}"/> </a>
                            </div>
                        </div>
                    <div class="linha-baixo"></div>

                            '''

    return render_template('plataformas.html', dados=dados, user=current_user)


@main.route('/linguagens')
@login_required
def linguagens():
    sql = bd.SQL("root", "uniceub", "Klas")
    comando = 'select idLinguagem, nmeLinguagem, dsc_path_imagem_linguagem, popularidadeLinguagem, salarioLinguagem, descLinguagem from linguagens;'
    cs = sql.consultar(comando, [])
    infos = ""

    for (idt, nome, path, pop, sal, desc) in cs:
        infos += f'''
       <div class="ling-all">
            <div class="ling-texto-img">
                <div>
                    <h1 class="ling-titulo">{nome}</h1>
                    <img class="ling-logo" src="{path}"/>
                </div>
            </div>
            <div class="ling-texto">
                    <h2 class="ling-pop">Popularidade no Mercado: {pop}</h2>
                    <h2 class="ling-salario">
                        Média de Salário no Mundo: {sal}
                    </h2>
                    <h3 class="ling-desc">
                        {desc}
                    </h3>
            </div>
        </div>
        '''

    return render_template('linguagens.html', infos=infos, user=current_user)


@main.route('/cursos')
@login_required
def cursos():
    return render_template('cursos.html', cursos=cursos, user=current_user)


@main.route('/cursos_pagos')
@login_required
def cursos_pagos():
    sql = bd.SQL("root", "uniceub", "Klas")
    comando = 'SELECT C.idCursoPago, C.nmeCursoPago, C.descCursoPago, C.link_curso_pago, P.dsc_path_imagem_plataformas, L.dsc_path_imagem_linguagem FROM tbCursoPago C INNER JOIN tbPlataformas P ON P.idPlataformas = C.cod_plataforma INNER JOIN  linguagens L ON L.idLinguagem = C.cod_linguagem;'
    cs = sql.consultar(comando, [])
    cursosp=''
    for (idt, nome, desc, link, path, path2) in cs:
        cursosp += f'''
                    <div class="texto-x-imagem">
                    <div class="textos-cursop">
                        <div class="nome-cursop"><a href="">
                            <h1>{nome}</h1></a></div>
                        <div class="desc-cursop"><h2>{desc}</h2> </div>
                        <div class="link-cursop"><a href="{link}" target="_blank"><h3>CLIQUE AQUI PARA CONHECER O CURSO</h3></a></div>
                    </div>
                    <div class="imagens-cursop">
                        <img style="height: 150px; widht: auto;"
                             src="{path}"/>
                        <img style="height: 150px; widht: auto;"
                            src="{path2}"/>
                    </div>
                </div>
            <div class="linha-baixo"></div>
        
                    '''

    return render_template('cursos_pagos.html', cursosp=cursosp, user=current_user)


@main.route('/cursos_gratis')
@login_required
def cursos_gratis():
    sql = bd.SQL("root", "uniceub", "Klas")
    comando = 'select idCursoGratis, nmeCursoGratis, descCursoGratis, link_curso_Gratis from tbCursoGratis;'
    cs = sql.consultar(comando, [])
    cursosg = ''

    for (idt, nome, desc, link) in cs:
        cursosg += f'''
           <div class="texto-imagem-cursog">
                <div class="texto-cursog">
                    <div class="titulo-cursog"><a><h1>{nome}</h1></a></div>
                    <div class="desc-cursog"><h3>{desc}</h3></div>
                </div>
                <div class="imagens-cursog">
                    <div class="assista-cursog"><h3>ASSISTA AQUI:</h3></div>
                    <div class="espaço-cursog"><iframe
                        width = "560"
                        height = "315"
                        src = "{link}"
                        title = "YouTube video player"
                        frameborder = "0"
                        allow = "accelerometer; autoplay;
                        clipboard - write;
                        encrypted - media;
                        gyroscope;
                        picture - in -picture"
                        allowfullscreen></iframe></div>
                </div>
     '''


    return render_template('cursos_gratis.html', cursosg=cursosg, user=current_user)


@main.route('/registro', methods=['GET', 'POST'])
def registro():
    sql = bd.SQL('root', 'uniceub', 'Klas')
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
            flash('Conta criada com sucesso!', category='contac')
            return redirect('/login')


    return render_template('sign_up.html', user=current_user)


@main.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        sql = bd.SQL('root', 'uniceub', 'Klas')
        email = request.form.get('email')
        senha = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, senha):
                flash('Login efetuado com sucesso!', category='sucesso')
                login_user(user, remember=True)
                return redirect('/')

            else:
                flash('Email ou senha inválidos.', category='emaili')

        else:
            flash('Email ou senha inválidos.', category='emaili')

    return render_template('login.html', user=current_user)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')



@main.route('/password-recover', methods=['GET', 'POST'])
def password_recover():

    global email_global
    if request.method == 'POST':
        email_global = request.form.get('email-recover')

        user = User.query.filter_by(email=email_global).first()

        if user:
            msg = Message('Klas: Redefinição de senha.', sender='projetoceub@gmail.com', recipients=[email_global])
            link = url_for('main.password_retype', _external=True)
            msg.body = f'Siga o link para a redefinição da senha. {link}'
            mail.send(msg)
            flash('Email Enviado com sucesso!', category='sucesso')
            return redirect('/')

        else:
            flash('Este email não está cadastrado no nosso sistema.', category='emailnc')


    return render_template('password-recover.html', user=current_user)



@main.route('/password-retype', methods=['GET', 'POST'])
def password_retype():

    try:
        user = User.query.filter_by(email=email_global).first()

        if request.method == 'POST':

            new_password = request.form.get('password-recover')
            confirm_password = request.form.get('confirm-password')

            if len(new_password) < 8:
                flash('A senha deve ter pelo menos 8 caracteres.', category='senhai')

            elif confirm_password != new_password:
                flash('A senhas são diferentes.', category='senhai')

            else:
                user.password = generate_password_hash(new_password, method='sha256')
                db.session.commit()
                flash('A senha foi alterada com sucesso!', category='senhas')
                return redirect('/login')

    except NameError:
        return redirect('/password-recover')


    return render_template('password-retype.html', user=current_user)



if __name__ == '__main__':
    app.run(debug=True)
