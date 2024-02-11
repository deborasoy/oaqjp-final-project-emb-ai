"""
Utiliza un detector de emociones externo para analizar el texto proporcionado por el usuario
"""
import requests
import json 
#función para detectar emociones en el texto
def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    # Si la solicitud es exitosa (código de estado 200), extrae las emociones y la emoción dominante
    if response.status_code == 200:
         emotions = formatted_response['emotionPredictions'][0]['emotion']
         anger_score = emotions['anger']
         disgust_score = emotions['disgust']
         fear_score = emotions['fear']
         joy_score = emotions['joy']
         sadness_score = emotions['sadness']
         dominant_emotion = max(emotions, key=emotions.get) #el argumento key=emotions.get, indica a max() que compare los valores del diccionario en lugar de las claves
    # Si hay un error en la solicitud (código de estado 400), asigna valores None a las puntuaciones de emociones y emoción dominante
    elif response.status_code == 400:
         anger_score = None
         disgust_score = None
         fear_score = None
         joy_score = None
         sadness_score = None
         dominant_emotion = None
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion }
