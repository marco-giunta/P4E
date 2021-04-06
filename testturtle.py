import turtle #penso si possa abbreviare con as tr tipo
fin = turtle.Screen() #creo una istanza detta fin della classe Screen di turtle; non gli passo argomenti
fin.bgcolor("lightgreen")#funziona esattamente come sotto per far avanzare alex; bgcolor=backgroundcolor
alex = turtle.Turtle() #creo una tartaruga chiamata alex
alex.forward(200) #aggiorno la classe (?) forward per fare avanzare alex di 200px
alex.left(90)#gira a sx di 90 gradi
alex.forward(200)
alex.left(90)#penso che questa dot notation sia analoga a quella usata in C per
alex.forward(200)#recuperare il valore delle cose dentro le strutture dati
alex.left(90)
alex.forward(200)
alex.numeroacaso = 500 #posso anche aggiungere io nuovi dati salvati
print(alex.numeroacaso)

gina=turtle.Turtle()#NON DIMENTICARE LE PARENTESI VUOTE SE NO Dà ERRORE
gina.pensize(5)
gina.color("hotpink")
gina.forward(200)
gina.left(120)
gina.forward(200)
gina.left(120)
gina.forward(200)

fin.exitonclick()#così la finestra si chiude solo quando qualcuno ci clicca
