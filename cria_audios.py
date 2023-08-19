from gtts import gTTS
from playsound import playsound


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/comando-invalido.mp3')
    playsound('audios/comando-invalido.mp3')


cria_audio('Não entendi!')
