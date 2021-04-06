#fname = input("Enter file name: ")
fname="romeo.txt"
fh = open(fname)
lst = list()
for line in fh:#line è str, può essere splittata in una lista
    #print("line=",line)
    for word in line.split():
        #print("word=",word)
        if word not in lst:
            lst.append(word)
            #print("lst=",lst)
lst.sort()
print(lst)
