import turtle
fin=turtle.Screen()
gina=turtle.Turtle()
a=170#deve quasi tornare indietro ma non proprio
x=200
N=20
#gina.right(90)
for i in range(N):
    gina.forward(x)#dall'origine al primo vertice ci sono solo 200px, ma gli altri lati sono lunghi 400 perché hanno un forward dopo aver svoltato più un altro proveniente dall'iterazione seguente del ciclo
    gina.right(a)
    gina.forward(x)
fin.exitonclick()
