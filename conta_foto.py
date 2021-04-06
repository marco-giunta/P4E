d = dict()
while(True) :
    i = input("nome persona\n")
    if i == "stop" :
        break
    d[i] = d.get(i,0)+1
    print(d[i])
print("persone e conteggi:")
print(d)
