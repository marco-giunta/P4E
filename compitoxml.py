import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_642073.xml"#642073 o 42
print('Retrieving', url)
xml = urllib.request.urlopen(url, context=ctx)
data = xml.read()#apre il file e mi dà un'unica stringa in UTF-8
#print('Retrieved', len(data), 'characters')
#print(data.decode())#non ho bs4 che decodifichi per me (non sto nemmeno lavorando con html)
tree = ET.fromstring(data)#restituisce un oggetto tree, non è una classe nativa diciamo
counts = tree.findall('.//count')#sto usando XPath; .//count significa trova tutti i count nel current tree (che in questo caso è solo uno e si chiama proprio tree)
#print(type(counts[0]))#counts è una lista di trees; mi serve .text per estrarre il numero
#print(counts)
#for count in counts :
#    print(count.text)#così ci siamo! ma provo con una list comprehension
print("Count:",len(counts))
x=sum([int(num.text) for num in counts])
print("Sum:",x)
