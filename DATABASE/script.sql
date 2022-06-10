CREATE DATABASE Klas;
USE Klas;

-- INTEGRANTES DO TRABALHO -- 

CREATE TABLE GrupoKlas(
	idAluno INT AUTO_INCREMENT PRIMARY KEY,
    nmeAluno VARCHAR(100) NOT NULL,
    descAluno VARCHAR(150) NOT NULL,
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
    descPlataformas VARCHAR(200) NOT NULL,
	dsc_path_imagem_plataformas VARCHAR(1000) NOT NULL,
	link_plataformas varchar(1000) not null

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

INSERT INTO GrupoKlas(nmeAluno, raAluno, descAluno, dsc_path_imagem_aluno) VALUES
("Lucas Zoser Nunes Costa", "22105593", "FRONT-END", "\\static\\imagens\\lucasz.png"),
("Leonardo Benttes Almeida Placido dos Santos", "22103833", "BACK-END","\\static\\imagens\\leob.png"),
("Leonardo Areias Rodovalho", "221570", "FRAMEWORKS", "\\static\\imagens\\leos.png"),
("Pedro Henrique Moreira da Silva", "22201914", "BANCO DE DADOS","\\static\\imagens\\pedrom.png"),
("Matheus Soares Accioly", "22908908", "HTML/CSS","\\static\\imagens\\matheusa.png");


SELECT * FROM GrupoKlas;