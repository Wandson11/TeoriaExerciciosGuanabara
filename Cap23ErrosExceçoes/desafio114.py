#escrever um código onde aponta que o site pudim está acessível ou não.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro')
'''except urllib.error.URLError:
        print('Deu erro')'''
else:
    print('Tudo OK.')