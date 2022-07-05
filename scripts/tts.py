#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""


from google.cloud import texttospeech
import sys


textfile = sys.argv[1]

# Selección de voz
voice_array = ['es-US-Wavenet-A','es-US-Wavenet-B']

# Instancia el cliente
client = texttospeech.TextToSpeechClient()

with open(textfile, 'r') as file:
    str = file.read().rstrip()

for voice_name in voice_array:
    print(textfile)
    print(voice_name)
    filename = "%s-%s.mp3" % (textfile, voice_name)
    synthesis_input = texttospeech.SynthesisInput(text=str)
    voice = texttospeech.VoiceSelectionParams(language_code="es-US", name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    with open(filename,"wb") as out:
        out.write(response.audio_content)