# Emprego Seguro API

API para o aplicativo Emgrego Seguro.

## Descrição

Trabalho sobre o projeto do app Emprego Seguro.
Trabalho realizado para a disciplina de Práticas Extensionistas Integradoras IV, 4º período, turma A, curso de Engenharia de Software da Universidade de Vassouras (Univassouras), ministrado pelo professor Dr. Diego Ramos Inácio.

## Como usar a API

Porta: 5001

* Login

    `POST /login`

    ```
    {
        "username" : <string>,
        "password" : <string>
    }
    ```

* Usuário

    * Pegar todos os usuários:
    
        `GET /users`

    * Pega um usuário por id:

        `GET /users/<int>`

    * Inserir usuário:

        `POST /users`

        ```
        {
            "username" : <string>,
            "email" : <string>,
            "password" : <string>,
            "phone" : <string>,
            "location" : <string>,
            "description" : <string>
        }
        ```
    
    * Editar usuário:

        `PUT /users/<int>`

        ```
        {
            "username" : <string>,
            "email" : <string>,
            "password" : <string>,
            "phone" : <string>,
            "location" : <string>,
            "description" : <string>
        }
        ```
    
    * Deletar usuário:

        `DELETE /users/<int>`

* Verviço

    * Pegar todos os serviços:
    
        `GET /services`

    * Pega um serviço por id:

        `GET /services/<int>`
    
    * Pega um serviço por palavras chave:

        `GET /services/search?q=<string>+<string>`

    * Inserir serviço:

        `POST /services`

        ```
        {
            "user_id" : <int>,
            "title" : <string>,
            "description" : <string>,
            "category" : <string>,
            "price" : <float>,
            "location" : <string>
        }
        ```
    
    * Editar serviço:

        `PUT /services/<int>`

        ```
        {
            "user_id" : <int>,
            "title" : <string>,
            "description" : <string>,
            "category" : <string>,
            "price" : <float>,
            "location" : <string>
        }
        ```

    * Deletar serviço:

        `DELETE /services/<int>`

* Mensagem

    * Pegar todos as mensagens:
    
        `GET /messages`

    * Pega uma mensagem por id:

        `GET /messages/<int>`
    
    * Pega mensagens recebidas:

        `GET /user/messages/in/<int>`
    
    * Pega mensagens enviadas:

        `GET /user/messages/out/<int>`

    * Inserir mensagem:

        `POST /messages`

        ```
        {
            "sender_id" : <int>,
            "receiver_id" : <int>,
            "content" : <string>
        }
        ```
    
    * Editar mensagem:

        `PUT /messages/<int>`

        ```
        {
            "sender_id" : <int>,
            "receiver_id" : <int>,
            "content" : <string>
        }
        ```
    
    * Deletar mensagem:

        `DELETE /messages/<int>`

## Como inicializar o projeto

Depois de clonar o repositorio do GitHub e acessar o terminal na pasta do projeto, siga os passos a seguir.

1. Crie um ambiente virtual:

`python -m venv venv`

2. Ative o ambiente:

`venv\Scripts\activate.bat`

3. Instale as dependencias:

`pip install -r requirements.txt`

Agora é só rodar o **app.py**.

## Requisitos

* blinker - 1.9.0
* click - 8.2.1
* colorama - 0.4.6
* Flask - 3.1.1
* Flask-SQLAlchemy - 3.1.1
* greenlet - 3.2.3
* itsdangerous - 2.2.0
* Jinja2 - 3.1.6
* MarkupSafe - 3.0.2
* psycopg2 - 2.9.10
* SQLAlchemy - 2.0.41
* typing_extensions - 4.14.0
* Werkzeug - 3.1.3
