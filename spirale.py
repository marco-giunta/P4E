import turtle
fin=turtle.Screen()
fin.bgcolor("lightgreen")
turi=turtle.Turtle()
turi.color("blue")
turi.shape("turtle")
dist=5
turi.up()#nuovo metodo: così la penna viene sollevata, non lascia la scia, per lasciare una stampa bisogna usare turi.stamp()
n_iterazioni=60
for _ in range(n_iterazioni):
    turi.stamp()
    turi.forward(dist)
    turi.left(24)
    dist=dist+2
fin.exitonclick()
