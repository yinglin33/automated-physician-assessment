from google.cloud import speech
import sys

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    return_string = ""

    for result in response.results:
        return_string += result.alternatives[0].transcript

    print(return_string)



if __name__ == '__main__':
    transcribe_file(sys.argv[1])  # takes in file path for argument
