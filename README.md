# Projeto Rose - Assistente Virtual em Python

O projeto Rose é uma assistente virtual desenvolvida em Python que utiliza reconhecimento de fala (Speech Recognition) e a API do Google Cloud para realizar várias tarefas úteis, como busca por playlists no Spotify, obtenção de notícias do dia e exibição da temperatura atual. A assistente Rose foi criada para interagir de maneira eficiente e amigável com o usuário, proporcionando uma experiência de assistência personalizada.

## Funcionalidades

O projeto Rose oferece as seguintes funcionalidades principais:

1. **Busca por Playlist no Spotify:** Através da integração com a API do Spotify, a assistente pode receber comandos de voz para buscar e reproduzir playlists específicas. Isso permite ao usuário ouvir sua música favorita de forma conveniente.

2. **Notícias do Dia:** A assistente é capaz de buscar e fornecer as notícias mais recentes do dia. Ela utiliza técnicas de web scraping e a biblioteca Beautiful Soup para extrair informações relevantes de fontes confiáveis de notícias.

3. **Temperatura Atual:** Utilizando a API do Google Cloud e suas funcionalidades de reconhecimento de fala, a assistente pode receber perguntas relacionadas à temperatura atual em uma determinada localização e fornecer respostas precisas.

## Requisitos do Sistema

Certifique-se de ter as seguintes bibliotecas instaladas em sua máquina antes de executar o projeto:

- Lista de bibliotecas:
- beautifulsoup4           4.12.2
bs4                      0.0.1
cachetools               5.3.1
certifi                  2023.7.22
charset-normalizer       3.2.0
click                    8.1.6
colorama                 0.4.6
gcloud                   0.18.3
google-api-core          2.11.1
google-api-python-client 2.97.0
google-auth              2.22.0
google-auth-httplib2     0.1.0
google-cloud-speech      2.21.0
googleapis-common-protos 1.60.0
grpcio                   1.57.0
grpcio-status            1.57.0
gTTS                     2.3.2
httplib2                 0.22.0
idna                     3.4
importlib-metadata       6.7.0
oauth2client             4.1.3
pip                      23.2.1
playsound                1.2.2
proto-plus               1.22.3
protobuf                 4.24.0
pyasn1                   0.5.0
pyasn1-modules           0.3.0
PyAudio                  0.2.13
pyparsing                3.1.1
requests                 2.31.0
rsa                      4.9
setuptools               65.5.1
six                      1.16.0
soupsieve                2.4.1
SpeechRecognition        3.9.0
typing_extensions        4.7.1
uritemplate              4.1.1
urllib3                  1.26.16
wheel                    0.38.4
zipp                     3.15.0


## Como Executar

1. Clone o repositório do projeto para sua máquina local.
2. Instale todas as bibliotecas listadas acima usando o gerenciador de pacotes `pip`.
3. Configure suas credenciais para a API do Google Cloud e do Spotify conforme as orientações fornecidas nas respectivas documentações.
4. Execute o arquivo principal `rose_assistant.py` para iniciar a assistente virtual.
5. Fale os comandos de voz para interagir com a assistente e desfrutar das funcionalidades oferecidas.


**Divirta-se interagindo com a assistente virtual Rose e aproveite todas as suas funcionalidades!**
