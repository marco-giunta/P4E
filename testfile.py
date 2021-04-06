fn="scarlett1000.txt"
fh=open(fn)
for line in fh:
    print(line.rstrip())
    #print(type(line))#con questo scopro che line è una stringa che corrisponde
    #ad una riga; in effetti dunque for line in fh mi dà una lista di stringhe
    #ciascuna delle quali corrisponde a una delle righe!
