import numpy as np


soluzioni = list()
with open("soluzioni.txt","r") as fh :
    for s in fh :
        soluzioni.append(s.strip())
    #print(soluzioni)
    n_indovinelli = len(soluzioni)
    n_ind_rimasti = n_indovinelli
    array_ind_rimasti = np.ones(n_indovinelli,dtype="bool")
    numeri_indovinelli = np.arange(n_indovinelli)

print("Benvenuto alla caccia al tesoro del compleanno di Matteo!")
print(' - Digita "status" per controllare a che punto sei.')
print(' - Digita un numero fra 1 e %d per accedere a quella prova.'%n_indovinelli)
print(' - Digita "exit" per uscire.')

while(True) :
    n_ind_rimasti = np.count_nonzero(array_ind_rimasti)
    print("\n"+"Prove rimaste: %d"%n_ind_rimasti)
    ipt = input("> ")
    try :
        idx = int(ipt)
    except :
        idx = None

    if ipt == "status" :
        for i in numeri_indovinelli :
            if array_ind_rimasti[i] :
                print('Prova n.%d: NON RISOLTA'%(i+1))
            else :
                print('Prova n.%d: RISOLTA'%(i+1))
    if idx is not None and idx in numeri_indovinelli :
        if array_ind_rimasti[idx-1] :
            tentativo = input("Digita la soluzione della prova n.%d "%idx)
            if tentativo == soluzioni[idx-1] :
                print("Risposta ESATTA!")
                array_ind_rimasti[idx-1] = False
            else :
                print("Risposta ERRATA, ritenta!")
        else :
            print("Hai già dato la risposta corretta per la prova n.%d!"%idx)
    if ipt == "exit" :
        print("Grazie per aver giocato!")
        break
    if idx is None and ipt != "status" and ipt != "exit" :
        print("Non ho capito, per favore riprova!")
