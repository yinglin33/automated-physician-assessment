# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "../assets/audio.mp3"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

word_list = []

for result in response.results:
    word_list.append(result.alternatives[0].transcript)
    print(word_list)
