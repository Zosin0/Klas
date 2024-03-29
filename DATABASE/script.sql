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
	salarioLinguagem VARCHAR (60) NOT NULL,
    descLinguagem VARCHAR(500) NOT NULL,
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
    descCursoGratis VARCHAR(1000) NOT NULL,
	link_curso_gratis VARCHAR(300) NOT NULL,

    codPlataforma INT,
    codLinguagem INT,

    foreign key (codPlataforma) references tbPlataformas(idPlataformas),
    foreign key (codLinguagem) references linguagens(idLinguagem)

);

-- CURSOS PAGOS --
CREATE TABLE tbCursoPago(
	idCursoPago INT AUTO_INCREMENT PRIMARY KEY,
    nmeCursoPago VARCHAR(50) NOT NULL,
    descCursoPago VARCHAR(500) NOT NULL,
	link_curso_pago VARCHAR(300) NOT NULL,
    cod_plataforma INT,
	cod_linguagem INT,

    foreign key (cod_plataforma) references tbPlataformas(idPlataformas),
    foreign key (cod_linguagem) references linguagens(idLinguagem)

);


-- INSERT ALUNOS (COMPLETO) --
INSERT INTO GrupoKlas(nmeAluno, raAluno, descAluno, dsc_path_imagem_aluno) VALUES
("Lucas Zoser", "22105593", "Project Management: Apto a organizar o grupo dentro dos prazos, e ajudar em todas as etapas de códigos para que o projeto progrida e consiga ser entregue a tempo."
, "/static/imagens/lucasz.png"),
("Leonardo Benttes", "22103833", "Back-End Developer: Apto a entregar a main.py com todas as funcionalidades especificadas e ajudar todos os integrantes com o funcionamento do site"
, "/static/imagens/leob.png"),
("Leonardo Areias", "22101570", "Test Analyst DBA: Apto a separar os conteúdos do site, e popular as tabelas do banco de dados, fazendo assim as integrações entre linguagens da aplicação."
, "/static/imagens/leos.png"),
("Pedro Henrique Moreira", "22201914", "Front-End Analyst: Apto a auxiliar todo o grupo em todas partes do site, garantindo que ele tenha todas as funções/conteúdos que foram especificados."
,"/static/imagens/pedrom.png"),
("Matheus Soares", "22908908", "Front-End Developer: Apto a dar vida ao esqueleto do projeto, tornar o site utilizável e agradável para o usuário final, entregar os códigos de HTML e CSS dentro do que foi especificado."
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
INSERT INTO linguagens(nmeLinguagem, popularidadeLinguagem, salarioLinguagem, descLinguagem, dsc_path_imagem_linguagem) VALUES
("JavaScript", 1, "Média de Salário no Mundo: $55.690", "JavaScript é uma das principais linguagens utilizadas na Internet. É usada para desenvolver aplicações em formato web, pelo computador, e mobile, pelo celular. Para quem busca aprender, deve saber que quase todos os navegadores contêm um código JavaScript.  ",
"/static/imagens/javas.png"),
("Phyton", 2, "Média de Salário no Mundo: $56.670", "Python é uma linguagem de código aberto de forma fácil e acessível de aprender. Ela também é eficiente para projetos complexos, pois sua legibilidade e sua sintaxe são simples e diretas. Entendendo-a é possível programar para computadores, celulares e jogos, entre aplicações básicas e avançadas. Sua capacidade de processar grandes bases de dados acaba a levando para o meio da computação científica, ciência de dados e Inteligência Artificial.",
"/static/imagens/python.png"),
("Java ", 3, "Média de Salário no Mundo: $55.690", "Java é uma linguagem de programação orientada a objetos. Por ser popular no desenvolvimento de sites e aplicativos para qualquer tipo de hardware, é uma das linguagens mais relevantes do meio. Ela pode ser usada no desenvolvimento de apps móveis, web, desktop e em qualquer sistema operacional ou hardware. ",
"/static/imagens/java.png"),
("PHP", 4, "Média de Salário no Mundo: $64.000", "PHP é uma linguagem de script de uso geral, principalmente na escrita de códigos HTML. É uma das mais popularizadas por gerenciadores de conteúdo como Wordpress. Através de sua programação, sites dinâmicos, lojas virtuais, blogs e plataformas de cursos online podem ser criados. ",
"/static/imagens/php.png"),
("C#", 5, "Média de Salário no Mundo: $58.469", "C#, ou C-Sharp, é a linguagem orientada a objetos, simples, moderna e de uso geral. Criada para substituir o Java na plataforma NET da Microsoft, pode ser usada para construir aplicativos de computador e celular, jogos e softwares corporativos. É a principal linguagem da Microsoft para o desenvolvimento de aplicações para Windows.",
"/static/imagens/csharp.png"),
("C/C++", 6, "Média de Salário no Mundo: $55.363", "C++ é a extensão da linguagem C, porém completa. É rápida e estável para aplicativos e sistemas com gráficos avançados, mas seu aprendizado pode ser mais demorado devido à sua complexidade. A linguagem é bastante usada para desenvolver aplicações mais pesadas e de alto desempenho.",
"/static/imagens/c.png");

INSERT INTO tbCursoPago(nmeCursoPago, descCursoPago, link_curso_pago, cod_plataforma, cod_linguagem) VALUES
("Python Completo - UDEMY", "Curso completo de Python na Udemy- Algoritmos, estruturas de dados, fundamentos, orientação a objeto, programação funcional e muito mais...",
"https://www.udemy.com/course/curso-python-3-completo/", 10, 2),
("JavaScript Completo - UDEMY", "Domine Web com 15 Cursos + Projetos: Javascript, Angular, React, Next Vue, Node, HTML, CSS, jQuery, Bootstrap, Webpack, Gulp, MySQL...",
"https://www.udemy.com/course/curso-web/", 10, 1),
("Java Completo - UDEMY", "Curso mais didático e completo de Java e OO, UML, JDBC, JavaFX, Spring Boot, JPA, Hibernate, MySQL, MongoDB e muito mais...",
"https://www.udemy.com/course/java-curso-completo/", 10, 3),
("C/C++ Completo - ALURA", "Conheça os recursos da linguagem C, desde a programação com if, else, while e funções até manipulação de arrays, ponteiros, tipos e recursão. Do gcc ao seu executável!",
"https://www.alura.com.br/cursos-online-programacao/linguagem-c", 9, 6),
("C# Completo - UDEMY", "Aprenda C# em um só curso, Algoritmos, Estrutura de Dados, Fundamentos, OO, Coleções, Lambdas, LINQ e vários recursos!",
"https://www.udemy.com/course/curso-c-sharp/", 10, 5),
("PHP - ALURA", "Você vai desenvolver com uma das linguagens mais populares no mercado que evoluiu muito em todos os requisitos nos últimos anos. Use corretamente a orientação a objetos com o PHP. Aprenda a lidar com as coleções. Aproveite o Composer e muito mais!",
"https://www.alura.com.br/cursos-online-programacao/php", 9, 4);

INSERT INTO tbCursoGratis(nmeCursoGratis, descCursoGratis, link_curso_gratis) VALUES
("Python - Curso em Vídeo",
"Python é uma linguagem ultra moderna, utilizada por grandes empresas como Google, YouTube, Industrial Light & Magic, Globo e muitas outras. Fácil de aprender, com código limpo e organizado, Python vem ganhando cada vez mais espaço, e chegou a sua hora de aprender. Curso criado pelo Prof. Gustavo Guanabara com uma temática divertida de vídeo-game para motivar seus alunos, é dividido em mundos para facilitar o estudo.",
"https://www.youtube.com/embed/videoseries?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0"),
("JavaScript- Curso em Vídeo ",
"Curso de linguagem JavaScript, voltado para iniciantes e para quem quiser aprender mais sobre ECMAScript, a versão padronizada do JS. Em um curso patrocinado pelo Google, o professor Gustavo Guanabara vai ensinar o conteúdo básico em 6 módulos que vão desde o conhecimento da linguagem até o uso de funções.",
"https://www.youtube.com/embed/videoseries?list=PLntvgXM11X6pi7mW0O4ZmfUI1xDSIbmTm"),
("Java - Curso em Vídeo",
"Este curso é indicado para qualquer pessoa que já possua bons conhecimentos de algoritmos e lógica de programação. Se não possuir esses requisitos, recomendamos que faça primeiro o Curso de Algoritmo para se preparar para este curso.
Caso você já domine a construção de algoritmos e a lógica de programação, o professor Gustavo Guanabara vai mostrar a história, introdução e explicação do funcionamento da linguagem, assim como suas sintaxes e estruturas de maneira fácil e descontraída.",
"https://www.youtube.com/embed/videoseries?list=PLJH2yd19u4hzRtpzm2dDCWZx58UrE85ye"),
("C - Programe seu Futuro",
"Curso de programação com a linguagem C do básico ao avançado. No curso serão abordados os seguintes tópicos:
Instruções de entrada e saída, Variáveis, Tipos de dados, Operadores relacionais e lógicos, Estruturas de decisão, Estruturas de repetição, Vetor e matriz, Strings, Funções e procedimentos, Struct,
Ponteiros, Listas encadeadas, Pilhas, Filas, Árvores, Tabela hash, e Grafos.",
"https://www.youtube.com/embed/videoseries?list=PLqJK4Oyr5WSjjEQCKkX6oXFORZX7ro3DA"),
("C++ - CFBcursos",
"C++ é uma das linguagens mais usadas no mundo, considero que todo programador deve saber usar C++. É uma linguagem poderosa, rápida e empregada  em muitos sistemas, além de ser a linguagem de maior emprego em cursos superiores da área de informática.
Neste curso iremos aprender desde os conceitos básicos de programação, até conceitos de programação orientada a objetos, trabalhar com arquivos, bibliotecas e atualizações da linguagem como C++11.
Se você quer aprender programação, quer se tornar um programador de qualidade você precisa aprender C++ e este é curso certo.",
"https://www.youtube.com/embed/videoseries?list=PLx4x_zx8csUjczg1qPHavU1vw1IkBcm40"),
("C# - CFBcursos",
"Curso de programação completo em C#, venha aprender criar programas para Windows em uma das linguagens mais usadas comercialmente. Se você que ser um programador de verdade e que tenha colocação no mercado de trabalho você precisa aprender C#.",
"https://www.youtube.com/embed/videoseries?list=PLx4x_zx8csUglgKTmgfVFEhWWBQCasNGi"),
("PHP - Programação WEB",
"Neste Curso de PHP Completo vamos aprender uma das linguagens de programação mais utilizadas no mundo. O PHP é uma excelente linguagem de programação para aprender por que é completa, open source e muito fácil de entender para quem é iniciante.",
"https://www.youtube.com/embed/videoseries?list=PL2Fdisxwzt_cOvOTUJhwEOxNV59wTs3ac");


SELECT C.idCursoPago, C.nmeCursoPago, C.descCursoPago, C.link_curso_pago, P.dsc_path_imagem_plataformas, L.dsc_path_imagem_linguagem FROM tbCursoPago C
INNER JOIN tbPlataformas P
ON P.idPlataformas = C.cod_plataforma
INNER JOIN  linguagens L
ON L.idLinguagem = C.cod_linguagem;


SELECT idAluno, nmeAluno, dsc_path_imagem_aluno, raAluno, descAluno FROM GrupoKlas;



