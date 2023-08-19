import speech_recognition as sr
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS
import webbrowser as browser

hotword = 'rose'

def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save('audios/mensagem.mp3')
    print('ROSIE: ', mensagem)
    playsound('audios/mensagem.mp3')


def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:2]:
        mensagem = item.title.text
        cria_audio(mensagem)

def play_list(album):
    if album == 'jonga':
        browser.open('https://open.spotify.com/intl-pt/track/1crJyVBXmm9w8ljO6PylZ6?si=f3b4d3079e7a4fe2')
    elif album == 'sertanejo':
        browser.open('https://open.spotify.com/intl-pt/track/1mimc5QiUuwmVYdXkWvgOQ?si=033a8c312fa64dcc')

def executa_comandos(trigger):
    if 'noticias' in trigger:
        ultimas_noticias()
    elif 'toca' in trigger and 'jonga' in trigger:
        play_list('jonga')
    elif 'toca' in trigger and 'sertanejo ' in trigger:
        play_list('sertanejo')
    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('COMANDO INVALIDO: ', mensagem)
        responde('comando-invalido')

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("->Aguardando o Comando: ")
            audio = microfone.listen(source)
            try:
                trigger = microfone.recognize_google_cloud(audio, credentials_json='credenciais/rose-python-assitente-1221a3067ae7.json', language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('COMANDO: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

             except sr.UnknownValueError:
                print("Google not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
    return trigger



def main():
    while True:
        monitora_audio()


main()
ultimas_noticias()
