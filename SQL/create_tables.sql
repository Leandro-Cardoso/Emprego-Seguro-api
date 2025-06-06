-- Criando a tabela usuarios --

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    phone VARCHAR(100)UNIQUE NOT NULL,
    location VARCHAR(100) NOT NULL,
    description TEXT
);

-- Criando a tabela servicos --
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL, -- Título do trabalho postado --
    descrition TEXT,
    category VARCHAR(100),
    location VARCHAR(100) NOT NULL,
    id_user INT NOT NULL, -- Quem fez a publicação --
    publication_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES usuarios(id_user)
);

-- Criando a tabela mensagens --
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    id_sender INT NOT NULL,
    id_recipient INT NOT NULL,
    content TEXT NOT NULL,
    shipping_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (id_recipient) REFERENCES usuarios(id_user) ON DELETE CASCADE,
FOREIGN KEY (id_sender) REFERENCES usuarios(id_user) ON DELETE CASCADE
);