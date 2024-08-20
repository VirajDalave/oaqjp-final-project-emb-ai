import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)

    response_data = response.json()

    # Navigate to the emotion predictions in the response data
    if response.status_code == 200:
        emotion_data = response_data['emotionPredictions'][0]['emotion']
        # Extract the required emotions and their scores
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        # Create a dictionary to hold the emotions and their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Add the dominant emotion to the dictionary
        emotion_scores['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    return emotion_scores