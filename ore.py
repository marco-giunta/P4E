name = "mbox-short.txt"
handle = open(name)
diz=dict()
for line in handle :
    if not line.startswith("From ") :
        continue
    words=line.split()#se no cerco il primo : e prendo i due numeri davanti
    h=words[len(words)-2]#h=hour
    h=h.split(":")
    h=h[0]
    diz[h]=diz.get(h,0)+1
#print(sorted([(k,v) for k,v in diz.items()]))#così fa tutto insieme
ore=sorted([(k,v) for k,v in diz.items()])
#print((k,v) for k,v in ore) una cosa così non funziona né va bene!
for k,v in ore :
    print(k,v)
