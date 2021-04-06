def my_function(a,b=2):
    result = a+2*b
    return result

my_function(3)

#interessante questo modo di assegnare dei valori di default in caso non venga
#specificato il secondo argomento... Scavalca tutto il problema dell'input
#parsing!!
