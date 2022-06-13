DROP DATABASE IF EXISTS Klas;
CREATE DATABASE Klas;
USE Klas;

-- INTEGRANTES DO TRABALHO --

CREATE TABLE GrupoKlas(
	idAluno INT AUTO_INCREMENT PRIMARY KEY,
    nmeAluno VARCHAR(100) NOT NULL,
    descAluno VARCHAR(500) NOT NULL,
    raAluno VARCHAR(10) NOT NULL,
	dsc_path_imagem_aluno VARCHAR(100) NOT NULL
);

-- LINGUAGENS DE PROGRAMAÇÃO FALADAS --

CREATE TABLE linguagens(
	idLinguagem INT AUTO_INCREMENT PRIMARY KEY,
	nmeLinguagem VARCHAR(50) NOT NULL,
	popularidadeLinguagem INT NOT NULL,
	dsc_path_imagem_linguagem VARCHAR(50) NOT NULL

);
-- TODAS AS PLATAFORMAS --

CREATE TABLE tbPlataformas(
	idPlataformas INT AUTO_INCREMENT PRIMARY KEY,
    nmePlataformas VARCHAR(50) NOT NULL,
    tipoCursos VARCHAR(60) NOT NULL,
    descPlataformas VARCHAR(500) NOT NULL,
    link_plataformas varchar(1000) not null,
	dsc_path_imagem_plataformas VARCHAR(1000) NOT NULL

);
-- CURSOS GRATIS --

CREATE TABLE tbCursoGratis(
	idCursoGratis INT AUTO_INCREMENT PRIMARY KEY,
    nmeCursoGratis VARCHAR(50) NOT NULL,
	vlrCursoGratis DECIMAL(10, 2) NOT NULL,
    descCursoGratis VARCHAR(200) NOT NULL
);

-- CURSOS PAGOS --
CREATE TABLE tbCursoPago(
	idCursoPago INT AUTO_INCREMENT PRIMARY KEY,
    nmeCursoPago VARCHAR(50) NOT NULL,
	vlrCursoPago DECIMAL(10, 2) NOT NULL,
    descCursoPago VARCHAR(200) NOT NULL
);
-- INSERT ALUNOS (COMPLETO) --
INSERT INTO GrupoKlas(nmeAluno, raAluno, descAluno, dsc_path_imagem_aluno) VALUES
("Lucas Zoser Nunes Costa", "22105593", "Project Management: Apto a organizar o grupo dentro dos prazos, e ajudar em todas as etapas de códigos para que o projeto progrida e consiga ser entregue a tempo."
, "/static/imagens/lucasz.png"),
("Leonardo Benttes Almeida Placido dos Santos", "22103833", "Back-End Developer: Apto a entregar a main.py com todas as funcionalidades especificadas e ajudar todos os integrantes com o funcionamento do site"
, "/static/imagens/leob.png"),
("Leonardo Areias Rodovalho", "221570", "Test Analyst DBA: Apto a separar os conteúdos do site, e popular as tabelas do banco de dados, fazendo assim as integrações entre linguagens da aplicação."
, "/static/imagens/leos.png"),
("Pedro Henrique Moreira da Silva", "22201914", "Front-End Analyst: Apto a auxiliar todo o grupo em todas partes do site, garantindo que ele tenha todas as funções/conteúdos que foram especificados."
,"/static/imagens/pedrom.png"),
("Matheus Soares Accioly", "22908908", "Front-End Developer: Apto a dar vida ao esqueleto do projeto, tornar o site utilizável e agradável para o usuário final, entregar os códigos de HTML e CSS dentro do que foi especificado."
,"/static/imagens/matheusa.png");


-- INSERT PLATAFORMAS--

INSERT INTO tbPlataformas(nmePlataformas, tipoCursos, descPlataformas, link_plataformas, dsc_path_imagem_plataformas) VALUES
("BitDegree", "GRÁTIS/PAGOS", "Plataforma completa com vários tipos de cursos, incluindo cursos gratuitos de Desenvolvimento Web, perfeito pra quem quer aprender HTML, CSS, e Javascript.",
"https://www.bitdegree.org/learn/", "/static/imagens/bitd.png"),
("Code Academy", "GRÁTIS/PAGOS", "Plataforma perfeita pra quem está começando na programação, pois mostra a saída do código em tempo real, além de contar com um vasto catálogos de cursos.",
"https://www.codecademy.com/", "/static/imagens/codea.png"),
("Khan Academy", "GRÁTIS", "Além da infinidade de conteúdo escolar, oferece vários conceitos essenciais sobre lógica de programação e o básico das  várias linguagens importantes para o mercado.",
"https://www.khanacademy.org/computing/computer-programming", "/static/imagens/khana.png"),
("W3Schools", "GRÁTIS", "Com foco nos tutoriais, vai ensinar ensinar a estruturação e a semântica de quase qualquer linguagem de programação",
"https://www.w3schools.com/", "/static/imagens/w3s.png"),
("Codewars", "GRÁTIS", "Plataforma que conta com uma comunidade própria, com cursos, tutoriais e desafios de programação.",
"https://www.codewars.com/", "/static/imagens/codew.png"),
("Curso em vídeo", "GRÁTIS", "Conhecido pela excelente didática das aulas, oferece muitos cursos de programação, com a possibilidade de ganhar certificados.",
"https://www.cursoemvideo.com/", "/static/imagens/cursoe.png"),
("Free Code Camp", "GRÁTIS", "Plataforma Web de aprendizagem interativa, um fórum de comunidade on-line, salas de bate-papo, publicações Medium e organizações locais que pretendem tornar a aprendizagem de desenvolvimento web acessível à qualquer pessoa.",
 "https://www.freecodecamp.org/", "/static/imagens/freec.png"),
("DankiCode", "PAGOS", "Plataforma que oferece vários pacotes com cursos de qualidade, cobrindo várias áreas da programação, e incluí a possibilidade de você mesmo ensinar!", 
"https://cursos.dankicode.com/", "/static/imagens/dankic.png"),
("Alura", "PAGOS", "Possui um custo-benefício e qualidade inigualável, uma das melhores plataformas para se aprender programação.", 
"https://www.alura.com.br/", "/static/imagens/alura.png"),
("Udemy", "PAGOS", "Não só oferece cursos de programação, mas de todas as ferramentas possíveis, contando com ótima qualidade e preço acessível.", 
"https://www.udemy.com/", "/static/imagens/udemy.png"),
("RocketSeat", "PAGOS/GRATIS", "Conta com 3 programas que ensinam muitos conceitos e linguagens de programação, focando principalmente no desenvolvimento web, inclusive o (discover) que é gratuito.", 
"https://www.rocketseat.com.br/", "/static/imagens/rocketseat.png"),
("Pluralsight", "PAGOS", "É uma opção mais cara, contudo conta com cursos em inglês e profissionais de alto nível.", 
"https://www.pluralsight.com/", "/static/imagens/pluralsight.png"),
("Udacity", "PAGOS", "Oferece cursos dos mais complexos assuntos de programação, aulas em inglês e conteúdo de qualidade.", 
"https://www.udacity.com/", "/static/imagens/udacity.png");

-- INSERT LINGUAGENS --

SELECT * FROM GrupoKlas;
