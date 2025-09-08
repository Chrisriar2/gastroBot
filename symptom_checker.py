import spacy

nlp = spacy.load("es_core_news_sm")

# Diccionario simple de síntomas -> enfermedades
symptom_disease_map = {
    "dolor abdominal": ["Gastritis", "Colitis", "Gastroenteritis"],
    "náuseas": ["Gastroenteritis", "Gastritis"],
    "vómito": ["Gastroenteritis", "Reflujo"],
    "acidez": ["Reflujo", "Gastritis"],
    "diarrea": ["Gastroenteritis", "Síndrome de intestino irritable"],
    "estreñimiento": ["Síndrome de intestino irritable", "Colitis"],
    "inflamación": ["Colitis", "Síndrome de intestino irritable"],
    "ardor": ["Reflujo", "Gastritis"],
    "gases": ["Colitis", "Síndrome de intestino irritable"],
}

def check_symptoms(text: str):
    doc = nlp(text.lower())
    matched_diseases = set()

    for symptom, diseases in symptom_disease_map.items():
        if symptom in text.lower():
            matched_diseases.update(diseases)

    return list(matched_diseases)
