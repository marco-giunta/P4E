name = "mbox-short.txt"
handle = open(name)
mail=dict()
for line in handle :
    if not line.startswith("From ") :
        continue
    words=line.split()
    word=words[1]
    mail[word]=mail.get(word,0)+1

bigperson = None
bigcount = None#oppure semplicemente gli dai tipo -1 e poi if count>bigcount
for adress,count in mail.items() :#anche se forse così è più generale perché magari si presta anche ad una ricerca simultanea del minimo, boh
    if bigcount is None or count>bigcount:
        bigcount=count
        bigadress=adress
print(bigadress,bigcount)
