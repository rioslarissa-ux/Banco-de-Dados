CREATE DATABASE escolas;
USE escolas;
Tabela: escolas
CREATE TABLE escolas (
    id_escola INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150),
    telefone VARCHAR(20)
);
Tabela: alunos
CREATE TABLE alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    id_escola INT,
    FOREIGN KEY (id_escola) REFERENCES escolas(id_escola)
);
Tabela: professores
CREATE TABLE professores (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    disciplina VARCHAR(50),
    id_escola INT,
    FOREIGN KEY (id_escola) REFERENCES escolas(id_escola)
);
Tabela: turmas
CREATE TABLE turmas (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano INT,
    id_escola INT,
    id_professor INT,
    FOREIGN KEY (id_escola) REFERENCES escolas(id_escola),
    FOREIGN KEY (id_professor) REFERENCES professores(id_professor)
);
Tabela: matrículas
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    id_turma INT,
    data_matricula DATE,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (id_turma) REFERENCES turmas(id_turma)
);
