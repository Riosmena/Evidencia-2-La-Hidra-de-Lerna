import pygame
pygame.init()
#Colores-------------------
Negro=(0,0,0)
Blanco=(255,255,255)
Rojo=(255,0,0)
Naranja=(255,98,9)
Verde=(0,255,0)
#Ventana-------------------
tam=(800,500)
screen=pygame.display.set_mode(tam)
clock=pygame.time.Clock()
texto=pygame.font.SysFont("OCR A Extended",100)
texto2=pygame.font.SysFont("OCR A Extended",40)
texto3=pygame.font.SysFont("OCR A Extended",30)
texto4=pygame.font.SysFont("OCR A Extended",25)
#Juego---------------------
cx=360
cy=300
gg=False
while not gg:
    margen=texto4.render("--------------------------------------------------------",True,Naranja)
    titulo=texto.render("CAR RACING",True,Verde)
    autor=texto2.render("JR60",True,Rojo)
    jugar=texto3.render("Play",True,Blanco)
    salir=texto3.render("Quit",True,Blanco)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gg=True
        if event.type.pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                cy=360
            if event.key==pygame.K_UP:
                cy=300
    raton=pygame.mouse.get_pos()
    x=raton[0]
    y=raton[1]
    #Dibujo----------------
    screen.fill(Negro)
    screen.blit(margen,(0,10))
    screen.blit(margen,(0,465))
    screen.blit(titulo,(110,100))
    screen.blit(autor,(360,220))
    screen.blit(jugar,(380,300))
    screen.blit(salir,(380,360))
    #Actualizar------------
    pygame.display.flip()
    clock.tick(80)
pygame.quit()
