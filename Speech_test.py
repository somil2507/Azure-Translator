import speech_recognition as sr
import pyttsx3
import requests, uuid, json

key = "3a987f3811fb4699bea3ce0a406fdf1c"
endpoint = "https://api.cognitive.microsofttranslator.com"

location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    #'to': ['fr', 'zu']
    'to': ['hi']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    voice = r.listen(source)
    text = r.recognize_google(voice, language='en')
    print(text)

body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


