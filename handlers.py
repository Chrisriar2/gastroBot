# handlers.py

conversation_state = {}

def handle_message(chat_id: str, message: str) -> str:
    """
    Manejador conversacional para el chatbot.
    Guarda el estado del usuario y responde de manera más natural.
    """
    if chat_id not in conversation_state:
        conversation_state[chat_id] = {"step": 0, "answers": {}}

    state = conversation_state[chat_id]

    if state["step"] == 0:
        response = "¡Hola! Soy tu asistente de salud. ¿Qué síntoma principal tienes? (ej. dolor de estómago, diarrea, vómito, fiebre)"
        state["step"] = 1

    elif state["step"] == 1:
        state["answers"]["symptom"] = message
        response = f"Entendido, mencionaste **{message}**. ¿Desde cuándo lo tienes? (ej. 'hace 2 días', 'desde ayer')"
        state["step"] = 2

    elif state["step"] == 2:
        state["answers"]["duration"] = message
        response = f"Perfecto, lo tienes desde {message}. ¿El dolor o malestar es leve, moderado o fuerte?"
        state["step"] = 3

    elif state["step"] == 3:
        state["answers"]["severity"] = message
        symptom = state['answers']['symptom']

        # Aquí podrías usar symptom_checker.py para sugerencias más realistas
        if "diarrea" in symptom:
            response = "Parece un cuadro de diarrea. Esto puede deberse a una infección estomacal o intolerancia alimentaria. Mantente hidratado y visita un médico si dura más de 2 días."
        elif "dolor" in symptom or "estómago" in symptom:
            response = "El dolor de estómago puede deberse a gastritis, indigestión o incluso reflujo. Si es intenso o constante, consulta a un médico."
        elif "fiebre" in symptom:
            response = "La fiebre suele acompañar infecciones gastrointestinales. Vigila tu temperatura y consulta a un médico si pasa de 38.5°C."
        else:
            response = f"Gracias, entiendo que presentas {symptom}. Te sugiero observar tu evolución y acudir a un médico si empeora."

        # Reiniciamos la conversación
        conversation_state[chat_id] = {"step": 0, "answers": {}}

    return response
