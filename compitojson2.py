import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ho capito a cosa serva tutta questa storia... lui si è salvato dei dati sul suo sito, quindi se non hai una tua chiave anziché maps usi il suo sito
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "The University of Latvia"#"South Federal University" o "The University of Latvia"
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)#questo encode non funziona senza dizionario; in più il sito vuole una chiave - te lo dice pure nel terminale
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
data=json.loads(data)
print(data["results"][0]["place_id"])#così data è un diz che alla key results come value
#corrispondente ha una lista di un unico dict (con altri sotto diz) di cui mi interessa
#solo la coppia relativa al place_id
