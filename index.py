import pygame
import random
import math
from pygame import mixer

pygame.init()
#title-bar
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("AMARJEET`S FIRST GAME CODE")
icon=pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

#inside game
playeri=pygame.image.load("player.png")
playerx=370
playery=730

#score
score=0

#background
background=pygame.image.load("background.png")

#mixer.music.load("background_music.wav") #we used music for big file and sound for small file
#mixer.music.play(-1)



# variable to change the value
playerx_change=0
playery_change=0

def player(x,y):
    screen.blit(playeri,(x,y))

#intruder
alien=[]
alienx=[]
alieny=[]
alienx_change=[]
alieny_change=[]

number=5
for a in range(number):
    alien.append(pygame.image.load("alien.png"))
    alienx.append(random.randint(0,750))
    alieny.append(random.randint(0,400))
    alienx_change.append(3)
    alieny_change.append(70)

def aliens(j,k,b):
    screen.blit(alien[b],(j,k))

#bullet
bullet_img=pygame.image.load("bullet.png")
bulletx=0
bullety=730
bulletx_change=0
bullety_change=10
bullet_state="ready"

def fire(x,y):
    global bullet_state
    bullet_state="fire"
    
    screen.blit(bullet_img,(x+18,y-33))

#collision
def collision(alienx,alieny,bulletx,bullety):
    #distance=((alienx-bulletx)**2+(alieny-bullety)**2)**(1/2)
    distance=math.sqrt((math.pow(alienx-bulletx,2))+(math.pow(alieny-bullety,2)))
    if distance<30:
        return True
    else:
        return False
    
#score
f=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
def show_score(x,y):
    s=f.render("SCORE:"+str(score),True,(16,89,100))
    screen.blit(s,(x,y))

#game over function
over_font=pygame.font.Font("freesansbold.ttf",60)
def over():
    text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(text,(250,350))
         
    
r=True
while r:
    screen.fill((41, 63, 92))
    screen.blit(background,(0,0))
    
    
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            r=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_LEFT:
                playerx_change=-3
                print("left")
                
            if e.key==pygame.K_RIGHT:
                playerx_change=3
                print("right")
                
            if e.key==pygame.K_UP:
                playery_change=-3
                print("up")
                
            if e.key==pygame.K_DOWN:
                playery_change=3
                print("down")
                
            if e.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    F=mixer.Sound("laser - Copy.wav")
                    mixer.Sound.play(F)
                    bulletx=playerx  #cuurent cordinate of x, spacship
                    bullety=playery
                    fire(bulletx,bullety)
                
        if e.type==pygame.KEYUP:
            if e.key==pygame.K_LEFT:
                #playerx_change=0
                print("left")
                
            if e.key==pygame.K_RIGHT:
                #  playerx_change=0
                print("right")
                
            if e.key==pygame.K_UP:
                # playery_change=0
                print("up")
                
            if e.key==pygame.K_DOWN:
                #  playery_change=0
                print("down")
        
                
                
    # limiting spaceship to boundary             
    playerx+=playerx_change
    
    if playerx<=0:
        playerx=0
    if playerx>=730:
        playerx=730
    
    playery+=playery_change
    
    if playery>=700:
        playery=700
    if playery<=0:
        playery=0

    #movement of alien
    for b in range(number):
        if alieny[b]>700:
            for c in range(number):
                alieny[c]=1000
            over()
            break
        
        



        
        alienx[b]+=alienx_change[b]
        if alienx[b]>=750:
            alienx_change[b]=-3
            alieny[b]+=alieny_change[b]
        if alienx[b]<=0:
            alienx_change[b]=3
            alieny[b]+=alieny_change[b]
        #collision
        coll=collision(alienx[b],alieny[b],bulletx,bullety)
        if coll:
            E=mixer.Sound("explosion.wav")
            mixer.Sound.play(E)
            bullety=730
            bullet_state= "ready"
            score+=1
            print(score)
            alienx[b]=random.randint(0,750)
            alieny[b]=random.randint(0,400)

        aliens(alienx[b],alieny[b],b)

    #movement of fired bullet
    if bullet_state=="fire":
        fire(bulletx,bullety)
        bullety-=bullety_change
    if bullety<=0:
        bullety=730
        bullet_state="ready"

    
        
        
    player(playerx,playery)
    show_score(textx,texty)
    
    pygame.display.update()

 
