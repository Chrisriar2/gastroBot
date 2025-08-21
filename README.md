# gastroBot
=============================
CHATBOT EDUCATIVO DE SÍNTOMAS GASTROINTESTINALES
=============================

Descripción:
-------------
Este proyecto es un chatbot educativo para Telegram que ayuda a los usuarios
a identificar posibles enfermedades gastrointestinales comunes (como gastritis,
reflujo, colitis, gastroenteritis, síndrome de intestino irritable) a partir de
los síntomas que describan en lenguaje natural.

⚠️ Importante: Este bot NO da diagnósticos médicos, solo sugerencias educativas.

Tecnologías utilizadas:
----------------------
- Python 3.10+
- FastAPI (Framework web para manejar webhooks)
- spaCy (es_core_news_sm) para procesamiento de lenguaje natural en español
- Requests (para interactuar con Telegram API)
- ngrok (para exponer servidor local a Internet en desarrollo)
- Telegram Bot API

Estructura del proyecto:
-----------------------
chatbot_gastro/
│── main.py             # Servidor FastAPI y webhook
│── handlers.py         # Lógica de interacción y flujo conversacional
│── symptom_checker.py  # Módulo para detectar síntomas y enfermedades
│── requirements.txt    # Dependencias

Instalación:
------------
1. Clona el repositorio:
   git clone https://github.com/tu_usuario/chatbot_gastro.git
   cd chatbot_gastro

2. Crear y activar un entorno virtual:
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate

3. Instala las dependencias:
   pip install -r requirements.txt
   python -m spacy download es_core_news_sm

Configuración de Telegram:
--------------------------
1. Crea un bot en Telegram usando @BotFather y obtiene tu token.
2. Guarda tu token como variable de entorno (opcional):
   set TELEGRAM_TOKEN=TU_TOKEN_AQUI

Ejecución local:
----------------
1. Arranca FastAPI:
   uvicorn main:app --reload --port 8000

2. Abre ngrok para exponer tu servidor:
   ngrok http 8000

3. Copia la URL pública de ngrok (ej: https://abcd-1234.ngrok-free.app)
   y configura el webhook:
   curl "https://api.telegram.org/botTU_TOKEN/setWebhook?url=https://abcd-1234.ngrok-free.app/webhook"

4. Verifica el webhook:
   curl "https://api.telegram.org/botTU_TOKEN/getWebhookInfo"

Uso:
----
- Abre tu bot en Telegram y envía un mensaje describiendo tus síntomas.
- El bot hará preguntas adicionales si no tiene suficiente información.
- Una vez recopilados los síntomas, el bot sugerirá posibles enfermedades.

Ejemplo:
---------
Usuario: tengo dolor abdominal y náuseas
Bot: Los síntomas que describes podrían estar relacionados con: Gastritis, Colitis, Gastroenteritis.
ℹ️ Recuerda que esto es solo información educativa y no sustituye una consulta médica.

Flujo conversacional:
--------------------
1. Usuario escribe un síntoma inicial.
2. Bot analiza y detecta si hay suficientes datos para sugerir enfermedades.
3. Si no hay suficientes síntomas, hace preguntas adicionales:
   - ¿Tienes dolor abdominal?
   - ¿Tienes náuseas o vómito?
   - ¿Sientes acidez o ardor?
   - ¿Tienes diarrea o estreñimiento?
   - ¿Sientes gases o inflamación?
4. Se acumulan los síntomas en memoria.
5. Cuando hay suficientes síntomas o se acaban las preguntas, el bot da la sugerencia final.

Diagrama de flujo (texto):
--------------------------
Inicio
  |
  v
Usuario envía mensaje
  |
  v
Analizar síntomas -> Suficientes? ----No----> Pregunta adicional
  |                                   |
  Sí                                  v
  |                             Acumula síntomas
  v                                   |
Sugerir enfermedades                  |
  |                                   |
Fin <----------------------------------

Dependencias (requirements.txt):
--------------------------------
fastapi
uvicorn
requests
spacy

Nota:
-----
Este chatbot es solo educativo y NO reemplaza la consulta con un profesional médico.

Licencia:
---------
MIT License
