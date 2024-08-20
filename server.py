'''
Importing required modules
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyzes the emotion of the provided text using the emotion_detector function.

    Retrieves the text to analyze from the request, processes it using the
    emotion_detector function, and returns a formatted string with the emotion scores
    and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Format the result into the required string format
    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    if response['anger'] is None:
        return "Invalid text! Please try again!"

    return formatted_result


@app.route("/")
def render_index_page():
    """
    Renders the index page.
    
    This function serves the index.html file when the root URL is accessed.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
