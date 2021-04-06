import re
f=open("regex_sum_642069.txt")
x=0#se uso un ciclo "esplicito" ho bisogno di salvare la somma
for line in f:#così il ciclo vedrà f come una lista di stringhe (una per riga) e su queste scorre line
    #print(line.rstrip())
    s=re.findall("[0-9]+",line)#lista di stringhe
    #print(s)
#se line contiene numeri ottengo una lista vuota, quindi escludo questo caso brutto
#con un guardiano banale. Potrei in alternativa usare un try and except ma dal
#momento che posso convertire solo le singole stringhe dentro una lista di stringhe
#quale è quella che mi restituisce re.findall() dovrei ciclare con un for sui
#suoi elementi e convertire quelli, ma evidentemente c'è più traffico così che
#sapendo già a monte se posso risparmiarmi i tentativi di conversione. Se potessi
#evitarmi di ciclare sulle stringhe sarebbe forse preferibile così; sia con if che
#con try except mi serve un for con le conversioni, ma in un caso posso occasionalmente
#saltare alcune iterazioni
    if len(s) == 0 :#Guardian line. ATTENZIONE: devo aprirmi alla possibilità di avere più numeri nella stessa riga, quindi non metto !=1 ma solo l'unico caso da evitare
        continue#così non mi serve else
    #print(s)
    for num in s :#così replico in parte il codice corto: sommo int(num) dove num è la stringa che scorre nella lista che mi ha dato findall
        #print(num.rstrip())
        x+=int(num)
print(x)
