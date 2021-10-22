#Alex Ladin
#10/15/21
#Learning diplay,
#opening windows,
#changing size window,
#basic game loop

import pygame, random

from pygame.draw import circle
#first thing to do is to intialize pygame
pygame.init()
check= True 
height=600
width=700
colors= {'black':(0,0,0), 'red':(225,0,0), 'green':(0,225,0), 'blue':(0,0,225), 'white':(225,225,225), 'purple':(150,0,150), 'pink':(400,225,225), 'light blue':(225,225,400), 'light green':(225,0,225)}
ColorList= ['black', 'red', 'green', 'blue', 'white','purple', 'pink', 'light blue', 'light green']
randColor=random.choice(ColorList)
while check:
    #height=input("height of the window: (100-1000)")
    #width=input("Width of your window: (100-1000)")
   
    try:
        height=int(height)
        width=int(width)
        check= False
    except ValueError:
        check= False
color= randColor
window=pygame.display.set_mode((width,height)) #set up color 
# window.fill(color)
pygame.display.flip() #refresh window with new color 
#change title of your window 
pygame.display.set_caption("Alex's Window")
pygame.display.flip()
hbox=50
wbox=50
speed=5
xc=random.randint(25,500)
yc=random.randint(25,400)
radius=hbox/2
#ball=pygame.circle(x=width/2, y=width/2)
rect=pygame.Rect(width/2, height/2, wbox, hbox )
pygame.draw.rect(window, color, rect)
#pygame.draw.circle(window ,color.get('green'),rect)
pygame.draw.circle(window, colors.get('green'), (xc,yc), radius)


pygame.display.flip()
run=True

#main loop for the game:
while run:
    pygame.time.delay(100)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #how to get the position of the mouse
   # x,y=pygame.mouse.get_pos()
    #print("("+str(x)+","+str(y)+")")
    keyPressed= pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        rect.y -= speed
        if rect.y<0:
            rect.y=height
    if keyPressed[pygame.K_DOWN]:
        rect.y += speed
        if rect.y>height:
            rect.y=0
    if keyPressed[pygame.K_LEFT]:
        rect.x -= speed
        if rect.x<1:
            rect.x=width-wbox/2
    if keyPressed[pygame.K_RIGHT]:
        rect.x += speed
        if rect.x>width:
            rect.x=width-wbox/2
    if keyPressed[pygame.K_w]:
        yc -= speed
        if yc<0:
            yc=wbox
    if keyPressed[pygame.K_s]:
        yc += speed
        if yc> height:
            yc=height-wbox
    if keyPressed[pygame.K_a]:
        xc -= speed
        if xc<1:
            xc=wbox/2
    if keyPressed[pygame.K_d]:
        xc += speed
        print("xc= ", xc)
        if xc>(width-wbox):
            xc=width



    window.fill(color)
    pygame.display.flip()
    pygame.draw.rect(window, 'green', rect)
    pygame.draw.circle(window, colors.get('green'), (xc,yc), radius)
    pygame.display.flip()

#trying to make it collide 
#if pygame.Rect.collidepoint(startRoundBtn, mousePos):
            #start_round()
        #if pygame.Rect.collidepoint(increaseSpeedBtn, mousePos):

pygame.quit()
