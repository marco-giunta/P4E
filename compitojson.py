import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_642074.json"#642074 o 42
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)#proprio come open mi restituisce un handle per il "file" che non si trova sul pc

data = uh.read()#legge il nostro url handle
print('Retrieved', len(data), 'characters')
#print(data.decode())#usa questo per esplorare la struttura del diz.
data = json.loads(data.decode())#ATTENZIONE: se non decodifico ottengo un diz binario, se decofidico un'unica stringa se non uso json loads!! Che infatti serve a caricare una stringa...
x=0#siccome comunque devo sfruttare la forma specifica dei dati decodificati tanto vale fare un hardcoding bello fiero
x=sum([int(n["count"]) for n in data["comments"]])#solo una volta usato json.loads i dati sono veramente un diz. anziché una stringa che lo imita formalmente se stampata
print(x)
#for n in data :
#    print(n,type(n))
#print(type(data))
