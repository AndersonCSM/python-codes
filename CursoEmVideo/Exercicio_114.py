# Exercicio_114
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO!')
else:
    print('Deu tudo certo')
