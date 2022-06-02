import turtle
import time
import random
posponer=0.1
#-----Puntos-----
puntuación=0
record=0
#-----Configuración de la ventana-----
wn=turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)
#-----Cabeza serpiente-----
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("#0BFE18")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
#-----Comida-----
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
#-----Cuerpo-----
cuerpos=[]
#-----Texto-----
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntuación: 0     Record: 0", align="center", font=("Courier",24,"normal"))
#-----Funciones-----
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"
def mov():
    if cabeza.direction=="up":
        if cabeza.direction!="down":
            y=cabeza.ycor()
            cabeza.sety(y+20)
    if cabeza.direction=="down":
        if cabeza.direction!="up":
            y=cabeza.ycor()
            cabeza.sety(y-20)
    if cabeza.direction=="left":
        if cabeza.direction!="right":
            x=cabeza.xcor()
            cabeza.setx(x-20)
    if cabeza.direction=="right":
        if cabeza.direction!="left":
            x=cabeza.xcor()
            cabeza.setx(x+20)
#-----Teclado-----
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")
while True:
    wn.update()
    #-----Colisiones bordes-----
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        #-----Esconder cuerpo-----
        for cuerpo in cuerpos:
            cuerpo.goto(1000,1000)
        #-----Limpiar-----
        cuerpos.clear()
        #-----Limpiar puntos----
        puntuación=0
        texto.clear()
        texto.write("Puntuación: {}    Record: {}".format(puntuación,record), align="center", font=("Courier",24,"normal"))
    #-----Colisiones comida-----
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        
        cuerpo=turtle.Turtle()
        cuerpo.speed(0)
        cuerpo.shape("square")
        cuerpo.color("#0D7613")
        cuerpo.penup()
        cuerpos.append(cuerpo)
        #-----Aumentar puntos-----
        puntuación=puntuación+10
        if puntuación>record:
            record=puntuación
        texto.clear()
        texto.write("Puntuación: {}    Record: {}".format(puntuación,record), align="center", font=("Courier",24,"normal"))
    #-----Mover cuerpo----
    totalcuer=len(cuerpos)
    for index in range(totalcuer-1,0,-1):
        x=cuerpos[index-1].xcor()
        y=cuerpos[index-1].ycor()
        cuerpos[index].goto(x,y)
    if totalcuer>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        cuerpos[0].goto(x,y)
        
    mov()
    #-----Colisiones cuerpo
    for cuerpo in cuerpos:
        if cuerpo.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            #-----Esconder cuerpo-----
            for cuerpo in cuerpos:
                cuerpo.goto(1000,1000)
            #-----Limpiar-----
            cuerpos.clear()
            #-----Limpiar puntos----
            puntuación=0
            texto.clear()
            texto.write("Puntuación: {}    Record: {}".format(puntuación,record), align="center", font=("Courier",24,"normal"))
    time.sleep(posponer)
