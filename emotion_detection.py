import requests

def emotion_detector(text_to_analyse):
    URL ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = Input, Headers = Header)
    return response.text
