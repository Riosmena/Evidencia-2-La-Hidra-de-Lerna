import pygame
import time
pygame.init()
#Colores-------
Negro=(0,0,0)
Blanco=(255,255,255)
Gris=(220,220,220) 
#Configuración de la ventana---------
tam=(800,600)
ventana=pygame.display.set_mode(tam)
pygame.display.set_caption("Pong")
fuente1=pygame.font.SysFont("Kristen ITC",80)
fuente2=pygame.font.SysFont("Showcard Gothic",80)
puntos1=0
puntos2=0
#Control de frames--------
tiempo=pygame.time.Clock()
#Configuración del juego---------
gg=False
#Configuracion del jugador-------
largo=100
ancho=15
p1x=50
p1y=300
p1v=0
p2x=720
p2y=300
p2v=0
#Configuracion de la pelota------
px=400
py=300
pvx=4
pvy=4.5

while not gg:
    puntuacion1=fuente1.render(str(puntos1),True,Blanco)
    puntuacion2=fuente1.render(str(puntos2),True,Blanco)
    gameover=fuente2.render("¡Fin del juego!",True,Gris)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gg=True
            pygame.quit()
        #Teclado------
        if event.type==pygame.KEYDOWN:
            #Jugador 1-------
            if event.key==pygame.K_w:
                p1v=-3
            if event.key==pygame.K_s:
                p1v=3
            #Jugador 2-------
            if event.key==pygame.K_UP:
                p2v=-3
            if event.key==pygame.K_DOWN:
                p2v=3
        if event.type==pygame.KEYUP:
            #Jugador 1-------
            if event.key==pygame.K_w:
                p1v=0
            if event.key==pygame.K_s:
                p1v=0
            #Jugador 2-------
            if event.key==pygame.K_UP:
                p2v=0
            if event.key==pygame.K_DOWN:
                p2v=0
    if p1y<0:
        p1y=1
    if p1y>510:
        p1y=509
    if p2y<0:
        p2y=1
    if p2y>510:
        p2y=509
    if py>590 or py<10:
        pvy*=-1
    #Anotacion---------
    if px>810:
        puntos1=puntos1+1
        px=400
        py=300
        pvx*=-1
        pvy*=-1
    if px<-10:
        puntos2=puntos2+1
        px=400
        py=300
        pvx*=-1
        pvy*=-1
    #Movimiento--------
    p1y+=p1v
    p2y+=p2v
    px+=pvx
    py+=pvy
    #Color de la ventana---------
    ventana.fill(Negro)
    #Zona de trabajo-------------
    jugador1=pygame.draw.rect(ventana,Blanco,(p1x,p1y,ancho,largo))
    jugador2=pygame.draw.rect(ventana,Blanco,(p2x,p2y,ancho,largo))
    pelota=pygame.draw.circle(ventana,Blanco,(px,py),10)
    pygame.draw.rect(ventana,Blanco,(400-10,0,10,600))
    pygame.draw.rect(ventana,Blanco,(400+10,0,10,600))
    ventana.blit(puntuacion1,(200,20))
    ventana.blit(puntuacion2,(600,20))
    #Game over---------
    if puntos1>10 or puntos2>10:
        ventana.blit(gameover,(90,300))
        gg=True
    #Colisiones-------
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pvx*=-1
    #Actualizar pantalla---------
    pygame.display.flip()
    tiempo.tick(80)
time.sleep(3)
pygame.quit()
