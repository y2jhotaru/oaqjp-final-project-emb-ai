''' This is the main file of the Emotion Detector Application 
    executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    ''' This function receives the text from the HTML interface
        and runs the emotion detector function to return the
        score of all the evaluated emotions and the dominant one
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_result

@app.route("/")
def render_index_page():
    '''
        This function renders the main page using Flask
    '''
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
