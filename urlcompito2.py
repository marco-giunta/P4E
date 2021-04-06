import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/known_by_Cedar.html"#Cedar (7,18) o Fikret (4,3)
count = input("Enter count:")
count = int(count)#tagliamo la testa al toro con int già qui perché non so come si comporterebbe range
position = input("Enter position:")
position = int(position)-1#così non devo rifare la differenza ogni volta nel for
print("Retrieving:",url)#stampo il primo url fuori dal ciclo alla faccia di Marco Russo
for n in range(count) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')#è una lista di stringhe, io voglio solo un elemento
    url=tags[position].get('href', None)#dovrebbe estrarre il singolo url
    print("Retrieving:",url)
