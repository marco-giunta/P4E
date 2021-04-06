fh=open("romeo.txt")
count=dict()
for line in fh :
    words=line.split()
    for word in words :
        count[word]=count.get(word,0)+1
ris=sorted([(v,k) for k,v in count.items()],reverse=True)
ris=[(k,v) for v,k in ris]
print(ris)
