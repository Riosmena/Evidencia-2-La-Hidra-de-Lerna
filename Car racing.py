from pygame import mixer
import pygame
import time
import random
fin=3
#Colores----------------
Blanco=(255,255,255)
Negro=(0,0,0)
Verde=(8,167,11)
Gris=(150,150,150)
Amarillo=(255,231,28)
#Clases-----------------
class Lineas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("lineas.png").convert()
        self.rect=self.image.get_rect()
        self.sep=100
    def update(self):
        self.rect.y+=2
        if self.rect.y>600:
            self.rect.y=-20
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Carro verde.png").convert()
        self.image.set_colorkey(Blanco)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x=480
        self.rect.y=500
        self.vel=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                self.vel+=-220
            if event.key==pygame.K_RIGHT:
                self.vel+=220
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                self.vel=0
            if event.key==pygame.K_RIGHT:
                self.vel=0
        player.rect.x+=self.vel
class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Carro naranja.png").convert()
        self.image.set_colorkey(Blanco)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y+=random.randrange(3)
        if self.rect.y>600:
            self.rect.y=-700
            self.rect.y+=random.randrange(3,5)
            self.rect.x=random.randrange(260,800,220)
#Configuracion----------
pygame.init()
screen=pygame.display.set_mode([1000,600])
pygame.display.set_caption("Car Racing")
fuente=pygame.font.SysFont("Showcard Gothic",80)
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)
fondo=pygame.image.load("Fondo.png").convert()
linea=pygame.sprite.Group()
autos=pygame.sprite.Group()
todo=pygame.sprite.Group()
for i in range(20):
    calle1=Lineas()
    calle2=Lineas()
    calle1.rect.x = 380
    calle2.rect.x = 620
    calle1.rect.y = random.randrange(600)
    calle1.rect.y += calle1.sep
    linea.add(calle1)
    todo.add(calle1)
    calle2.rect.y = random.randrange(600)
    calle2.rect.y += calle2.sep
    linea.add(calle2)
    todo.add(calle2)
for i in range(5):
    auto=Enemigos()
    auto.rect.x=random.randrange(260,800,220)
    auto.rect.y=random.randrange(-2000,0,300)
    
    autos.add(auto)
    todo.add(auto)
mixer.init()
mixer.music.load("NRX.mp3")
mixer.music.play(-1)
player=Jugador()
todo.add(player)
vel=0
#Bprincipal-------------
gg=False
while not gg:
    gameover=fuente.render("¡Fin del juego!",True,Negro)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gg=True
    todo.update()
    #Dibujo--------------------
    screen.blit(fondo,[0,0])
    bardal=pygame.draw.rect(screen,Amarillo,[180,0,20,600])
    bardad=pygame.draw.rect(screen,Amarillo,[800,0,30,600])
    pygame.draw.rect(screen,Gris,[200,0,610,600])
    todo.draw(screen)
    #Colisiones----------------
    choque=pygame.sprite.spritecollide(player,autos,True)
    if choque:
        screen.blit(gameover,(200,300))
        pygame.display.flip()
        mixer.music.stop()
        time.sleep(fin)
        gg=True
    #Actualizar----------------
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
