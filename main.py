from analise_sentimentos import AnaliseSentimentos
from googletrans import Translator
from textblob import TextBlob

analise = AnaliseSentimentos()
frase = input('Digite uma frase: ')

tradutor = Translator()
fraseTraduzida = tradutor.translate(frase, src='auto', dest='pt')
fraseTratada = TextBlob(fraseTraduzida.text)

print(f'Tradução: {fraseTratada}')
resultado = analise.avalia(str(fraseTratada))
print(resultado)

if resultado['score'] < 0:
    print('Frase negativa')

elif resultado['score'] == 0:
    print('Frase neutra')

elif resultado['score'] > 0:
    print('Frase positiva')
