from googletrans import Translator
from textblob import TextBlob

frase = input('Digite uma frase: ')

tradutor = Translator()
fraseTraduzida = tradutor.translate(frase)
fraseTratada = TextBlob(fraseTraduzida.text)
resposta = fraseTratada.sentiment.polarity

if resposta < 0:
    print('Frase negativa')

elif resposta == 0:
    print('Frase neutra')

elif resposta > 0:
    print('Frase positiva')
