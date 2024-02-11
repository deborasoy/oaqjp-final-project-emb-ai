"""
Implementa un servicio web utilizando Flask para analizar emociones en texto.
"""
from flask import Flask, request, render_template
#importo la funcion de package.archivo
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
#aliza el análisis de emociones en el texto proporcionado por el usuario
@app.route("/emotionDetector")
#Analiza el texto que se obtiene mediante la solicitd http, obtiene la respuesta
#evalua que el contenido sea el deseado
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': "
        f"{sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
#Renderiza: genera y envia al cliente respuesta HTML
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) #0.0.0.0 == localhost