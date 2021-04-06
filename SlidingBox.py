# SlidingBox.py : 3−D animation of forces on a beam as box slides
from vpython import *
Hsupport , d =30, 100 # height , distance supports
Lbeam=500; Wbeam=80; thickness=10 # beam dimensions
W=200; WeightBox=400 # weight of tab l e , box
Lbox=60; Wbox=60; Hbox=60 # Box Dimensions
# Graphics
scene=canvas( width=750 , height=500 , range=300)
scene.forward=vector(0.5, −0.2 , −1) # to change point of view
support1=cone(pos=vector(−d , 0 , 0 ), axis=vector(0 , Hsupport , 0 ) ,
color=color.yellow , radius=20)
support2=cone(pos=vector(d , 0 , 0 ), axis=vector(0 , Hsupport , 0 ) ,
color=color.yellow , radius=20)
beam=box (pos=vector( 0 , Hsupport+thickness /2 ,0), color=color.orange , \
length=Lbeam, width=Wbeam, height=thickness)
cube=box(pos=vector(−d , Hsupport+Hbox/2+thickness , 0 ) , length=Lbox ,
width=Wbox, height=Hbox)
piso=curv( pos=[(−300 ,0 ,0) , (300 , 0 , 0 ) ] , color=color.green , radius=1)
arrowcube=arrow(color=color.orange, axi s=vector(0 ,−0.15*Wbox, 0 ) )
arrowbeam=arrow(color=color.orange, axi s=vector(0 ,−0.15*W, 0 ) )
arrowbeam.pos=vector(0 , Hsupport+thickness/2 ,0)
v=4.0 # box speed
x=−d # box i n i t i a l p o s i t i on
Mg=WeightBox+W # weight box+beam
Fl=(2Wbox+W) /2.0
arrowFl = arrow (color=color.red ,
pos=vector(−d , Hsupport+thickness/2 ,0) , axis=vector ( 0 , 0 . 1 5  Fl , 0 ) )
Fr = Mg−Fl # r i g h t for c e
arrowFr=arrow(color=color.red, pos=vector(d , Hsupport+thickness /2 ,0) ,
axis=vector(0 , 0.15 * Fr , 0 ) )
anglabel=label(pos=vector (−100 ,150 ,0) , text=’ Fl = ’ , box=0)
Ftext1=label(pos=vector (−50 ,153 ,0) , box=0)
ang l abe l 2=label(pos=vector (100 ,150 ,0) , text=’ Fr = ’ , box=0)
Ftext2=label(pos=vector(15 0 ,1 53 ,0 ) , box=0)
rate ( 4 ) # to slow motion
for t in arange(0.0,65.0,0.5 ) :
rate(10)
x = −d+v*t
cube.pos=vector(x , Hsupport+Hbox/2+10 ,0) # p o s i t i on cube
arrowcube.pos=vector(x , Hsupport+5 ,0)
if Fl>0:
Fl=(d*Mg−x*WeightBox )/(2.0 * d)
Fr=Mg−Fl
cube.pos=vector(x, Hsupport+Hbox/2+10 ,0)
arrowcube.pos=vector(x , Hsupport+thickness /2 ,0)
arrowFl.axis=vector(0,0.15*Fl,0)
arrowFr.axis=vector(0,0.15*Fr,0)
Ftext1.text=’ %8.2 f ’%Fl # Left force
Ftext2.text=’ %8.2 f ’%Fr # Right force
elif Fl==0:
x=300
beam.rotate(angle=−0.2, axis=vector(0,0,1) ,\
origin=vector(d , Hsupport+thickness /2 ,0) )
cube.pos=vector(300 , Hsupport , 0 )
arrowcube.pos=vector(300,0,0)
break
rate( 5 )
arrowFl.axis=vector(0,0.15*0.5*W,0) # return beam
arrowFr.axis=arrowFl.axis
beam.rotate(angle=0.2, axis=vector(0,0,1),  -
origin=vector(d , Hsupport+thickness /2 ,0) )
Fl=100.0
Ftext1.text=’ %8.2 f ’%Fl
Ftext2.text=’ %8.2 f ’%Fl
