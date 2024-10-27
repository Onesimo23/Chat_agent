# Agente de Chat para Consultas de Cultura Moçambicana

Esta é uma aplicação de agente de chat desenvolvida em Python, projetada para responder a perguntas de cultura geral moçambicana. O agente verifica as respostas em uma base de dados local e consulta o ChatGPT ou o Google, caso necessário. 

## Funcionalidades

- **Respostas em múltiplas fontes**: o agente busca respostas primeiro na base de dados local, depois no ChatGPT e, em último caso, no Google.
- **Fallback automático**: caso o ChatGPT ou o Google estejam indisponíveis, o agente ajusta-se automaticamente para a próxima fonte.
- **Interface de chat personalizada**: layout com margens, espaçamento entre mensagens e uma mensagem de boas-vindas personalizada.

## Pré-requisitos

Para rodar o projeto, você precisará de:

- Python 3.9 ou superior
- Conta no OpenAI e chave de API para integração com o ChatGPT
- Pacotes listados no `requirements.txt`

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/Onesimo23/Agent_chat-.git
    cd Agent_chat-
    ```

2. Crie um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` com sua chave de API do OpenAI:

    ```plaintext
    OPENAI_API_KEY='sua_chave_aqui'
    ```

5. Execute a aplicação:

    ```bash
    python src/main.py
    ```

## Configuração do `.gitignore`

Certifique-se de que o `.gitignore` contém o seguinte para evitar o upload de arquivos indesejados:

```plaintext
__pycache__/
*.pyc
.env
