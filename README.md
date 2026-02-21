# IA WhatsApp Bot

Esse projeto é um bot de WhatsApp que responde automaticamente as mensagens que outras pessoas enviam, usando inteligência artificial.

O bot recebe a mensagem pelo WhatsApp, envia para o backend em Python, a IA gera a resposta e o bot devolve a resposta para o contato.

---

## O que o bot faz

- Lê mensagens recebidas no WhatsApp
- Envia a mensagem para a IA
- Gera uma resposta automática
- Responde o usuário no WhatsApp

---

## Como usar

### Backend (Python)

Entre na pasta do backend:

```bash
cd backend

Configure o arquivo .env com as variáveis necessárias.

Depois rode:

python app.py
Bot (Node.js)

Entre na pasta do bot:

cd bot

Instale as dependências:

npm install

Inicie o bot:

node index.js

Na primeira vez, vai aparecer um QR Code no terminal.
Escaneie com o WhatsApp para conectar.

Estrutura do projeto
IA-WhatsApp-Bot/
├── backend/
│   ├── app.py
│   └── .env
├── bot/
│   ├── index.js
│   ├── package.json
│   └── package-lock.json
├── .gitignore
└── README.md
