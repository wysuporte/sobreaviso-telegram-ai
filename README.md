# 🚀 Sobreaviso Telegram AI

Sistema inteligente de registro de atendimentos via Telegram utilizando Inteligência Artificial com Gemini.

O projeto recebe áudios enviados pelo Telegram, realiza a transcrição automática utilizando Gemini AI, extrai informações estruturadas do atendimento e registra os dados automaticamente em uma planilha Google Sheets.

---

# 📌 Objetivo

Automatizar o processo de preenchimento de planilhas de sobreaviso e registro de atendimentos técnicos através de:

* Transcrição automática de áudio
* Extração inteligente de informações
* Cálculo automático de horários
* Registro automático em Google Sheets
* Centralização dos atendimentos
* Histórico automatizado
* Integração em tempo real via Telegram

---

# 🧠 Tecnologias Utilizadas

| Tecnologia        | Uso                                  |
| ----------------- | ------------------------------------ |
| Python 3.11       | Backend principal                    |
| FastAPI           | API/Webhook                          |
| Telegram Bot API  | Recebimento de mensagens             |
| Google Gemini AI  | Transcrição e interpretação do áudio |
| Google Sheets API | Armazenamento dos dados              |
| Docker            | Containerização                      |
| Railway           | Deploy e hospedagem                  |
| Uvicorn           | Servidor ASGI                        |
| gspread           | Integração Google Sheets             |
| OAuth2Client      | Autenticação Google                  |

---

# ⚙️ Funcionalidades

## ✅ Recebimento de Áudio

O usuário envia um áudio diretamente para o bot Telegram.

---

## ✅ Transcrição Inteligente

O Gemini realiza:

* Transcrição do áudio
* Interpretação contextual
* Extração dos campos necessários

---

## ✅ Extração Estruturada

O sistema identifica automaticamente:

| Campo            | Descrição              |
| ---------------- | ---------------------- |
| Data             | Data do atendimento    |
| Hora Início      | Horário inicial        |
| Hora Fim         | Horário final          |
| Duração          | Tempo do atendimento   |
| Descrição        | Situação relatada      |
| Ramal / Telefone | Contato do solicitante |
| Setor / Unidade  | Local do atendimento   |
| Quem Ligou       | Nome do solicitante    |

---

## ✅ Inteligência Temporal

O sistema possui validação automática de horários.

### Exemplo:

Áudio:

```text
Atendimento iniciou às 08:10 e durou 25 minutos.
```

Resultado:

```text
Hora Início: 08:10
Hora Fim: 08:35
```

---

## ✅ Google Sheets Automático

Os registros são adicionados automaticamente em uma planilha Google Sheets.

---

## ✅ Deploy em Produção

Aplicação hospedada utilizando:

* Docker
* Railway
* HTTPS
* Domínio personalizado

---

# 🏗️ Arquitetura do Projeto

```text
Telegram
   ↓
Railway (Webhook HTTPS)
   ↓
FastAPI
   ↓
Gemini AI
   ↓
Validação Python
   ↓
Google Sheets
```

---

# 📁 Estrutura do Projeto

```text
sobreaviso-telegram-ai/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   └── telegram_webhook.py
│   │
│   ├── services/
│   │   ├── audio_service.py
│   │   ├── gemini_service.py
│   │   ├── sheets_service.py
│   │   ├── telegram_service.py
│   │   └── time_service.py
│   │
│   ├── models/
│   │   └── atendimento.py
│   │
│   └── prompts/
│       └── atendimento_prompt.txt
│
├── audios/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🔐 Variáveis de Ambiente

Criar arquivo:

```text
.env
```

Conteúdo:

```env
TELEGRAM_TOKEN=
GEMINI_API_KEY=
GOOGLE_SHEETS_NAME=Sobreaviso
GOOGLE_CREDENTIALS_JSON=
```

---

# 🤖 Configuração Telegram

## 1. Criar Bot

Abrir:

[https://t.me/BotFather](https://t.me/BotFather)

Executar:

```text
/newbot
```

Salvar o token gerado.

---

# 🧠 Configuração Gemini

## 1. Criar API Key

Abrir:

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Gerar API Key.

Adicionar em:

```env
GEMINI_API_KEY=
```

---

# 📊 Configuração Google Sheets

## 1. Criar planilha

Exemplo:

```text
Sobreaviso
```

---

## 2. Criar cabeçalhos

| Data | Hora Inicio | Hora Fim | Duracao Minutos | Descricao | Ramal / Telefone | Setor / Unidade | Quem Ligou |
| ---- | ----------- | -------- | --------------- | --------- | ---------------- | --------------- | ---------- |

---

# ☁️ Configuração Google Cloud

## Ativar APIs

No Google Cloud:

* Google Sheets API
* Google Drive API

---

## Criar Service Account

1. IAM & Admin
2. Service Accounts
3. Criar conta
4. Gerar JSON

---

## Configurar Railway

Converter o JSON para uma linha única e adicionar em:

```env
GOOGLE_CREDENTIALS_JSON=
```

---

# 🐳 Docker

## Build Local

```bash
docker-compose up --build
```

---

# 🚂 Deploy Railway

## 1. Criar projeto Railway

[https://railway.app/](https://railway.app/)

---

## 2. Conectar GitHub

Selecionar repositório:

```text
sobreaviso-telegram-ai
```

---

## 3. Configurar Variáveis

Adicionar:

```env
TELEGRAM_TOKEN=
GEMINI_API_KEY=
GOOGLE_SHEETS_NAME=
GOOGLE_CREDENTIALS_JSON=
```

---

## 4. Gerar domínio público

Exemplo:

```text
https://api.ubcode.com.br
```

---

# 🌐 Configuração DNS

Exemplo de configuração:

| Tipo  | Nome                | Valor                |
| ----- | ------------------- | -------------------- |
| CNAME | api                 | xxxxx.up.railway.app |
| TXT   | _railway-verify.api | railway-verify=xxxxx |

---

# 🔗 Configuração Webhook Telegram

Executar:

```text
https://api.telegram.org/botTOKEN/setWebhook?url=https://api.ubcode.com.br/webhook
```

---

# ▶️ Executando Localmente

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Executar aplicação

```bash
uvicorn app.main:app --reload
```

---

## Testar API

Abrir:

```text
http://localhost:8000
```

Resultado esperado:

```json
{
  "status": "online"
}
```

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
python-dotenv
python-telegram-bot
google-genai
gspread
oauth2client
pydantic
python-multipart
requests
```

---

# 🧾 Exemplo de Fluxo

## Áudio enviado

```text
Maria da UTI informou lentidão no Tasy.
Atendimento iniciou às 08:10 e durou 25 minutos.
Telefone 3333-4444.
```

---

## Resultado gerado

| Campo       | Valor            |
| ----------- | ---------------- |
| Data        | 18/05/2026       |
| Hora Início | 08:10            |
| Hora Fim    | 08:35            |
| Duração     | 25               |
| Descrição   | Lentidão no Tasy |
| Telefone    | 3333-4444        |
| Setor       | UTI              |
| Quem Ligou  | Maria            |

---

# 🔒 Segurança

O projeto utiliza:

* Variáveis ambiente
* Credenciais Google protegidas
* HTTPS Railway
* GitIgnore para arquivos sensíveis

---

# 📌 Arquivos ignorados

```gitignore
.env
credentials.json
.venv/
__pycache__/
audios/
.idea/
```

---

# 🚀 Melhorias Futuras

## Planejado

* Dashboard Web
* Histórico de atendimentos
* Multiusuário
* Classificação IA
* Painel administrativo
* Logs estruturados
* Relatórios PDF

---

# 👨‍💻 Autor

Projeto desenvolvido por:

## Ueslei Bastos

Especialista em:

* Automação
* Integrações
* Oracle
* IA aplicada
* Desenvolvimento Python
* Infraestrutura

---

# 📄 Licença

Projeto para uso interno e automação operacional.

---

# ⭐ Considerações

Este projeto foi criado com foco em:

* produtividade
* automação operacional
* redução de retrabalho
* utilização prática de IA
* centralização de informações
* ganho operacional em equipes de suporte e sobreaviso
