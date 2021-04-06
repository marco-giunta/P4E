testo="Apelle figlio di Apollo fece una palla di pelle di pollo e tutti i pesci vennero a galla per ammirare la palla di pelle di pollo fatta da Apelle figlio di Apollo"
parole=testo.split()
conteggio=dict()

for parola in parole :
    conteggio[parola]=conteggio.get(parola,0)+1

s=sorted([(v,k) for k,v in conteggio.items()],reverse=True)
s=[(k,v) for v,k in s]
print(s)
