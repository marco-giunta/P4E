from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_642071.html"#642071 o 42
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

x=0
tags = soup('span')#dovrebbe essere così che si specifica quale tag voglia
for tag in tags:
    #print(tag)#è una classe strana, non una stringa
    #s=str(tag)
    #print(s)
    #print(re.findall("[0-9]+",s))
    #print(str(tag))
    #x+=int(re.findall("[0-9]+",str(tag)))
    x+=sum([int(n) for n in re.findall("[0-9]+",str(tag))])#quantomeno così funziona anche se ci sono più numeri nella singola stringa
print(x)#è una soluzione un po' del cavolo quella precedente, sarebbe meglio
#trovare un modo per evitare il ciclo for e usare direttamente la list Comprehension.
#Il problema è che anche se str(una lista) funziona (vettorizzazione alla matlab)
#la re.findall() va usata su una stringa sola, non su una lista di stringhe...
#posso provare a fare una list Comprehension doppia?
#y=sum([int(n) for n in re.findall("[0-9]+",str(tag)) for tag in tags])
#print("somma col nuovo metodo:",y)#così non funziona per qualche motivo
