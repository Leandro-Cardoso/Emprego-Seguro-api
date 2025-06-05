-- Criando a tabela usuarios --
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario VARCHAR(30) -- Cliente ou Prestador de serviço --
);

-- Criando a tabela servicos --
CREATE TABLE servicos (
    id_servico SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL, -- Título do trabalho postado --
    descricao TEXT,
    categoria VARCHAR(100),
    localizacao VARCHAR(100) NOT NULL,
    id_usuario INT NOT NULL, -- Quem fez a publicação --
    data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Criando a tabela mensagens --
CREATE TABLE mensagens (
    id_mensagem SERIAL PRIMARY KEY,
    id_remetente INT NOT NULL,
    id_destinatario INT NOT NULL,
    conteudo TEXT NOT NULL,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (id_remetente) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
FOREIGN KEY (id_destinatario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);