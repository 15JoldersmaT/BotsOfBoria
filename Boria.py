import pygame
import sys
import random
import math

display = pygame.display.set_mode((1300,800) ,flags=pygame.SCALED, vsync=0)
pygame.display.set_caption('Bots of Boria')

clock = pygame.time.Clock()

time = 0

grav = 1

pinkBots = 4 * 6
yellowBots = 5 * 20
greenBots = 15 * 7


bots = []

class Bot:
    def __init__(self,x, y,color):
        self.x = x
        self.y = y
        self.color = color
        
 

            

    def move(self):
        global bots



        ##SET BOUNDS##

        if self.x < 15:
            self.x = self.x + 20

        if self.x > 1295:
            self.x = self.x - 20

        if self.y >795:
            self.y = self.y - 20

        if self.y < 5:
            self.y = self.y + 20

        
        #Will be used to move bot after gravity effects are calculated
        mX = 0
        mY = 0
        #Need to calculate gravity
        for i in bots:
            #Get distance between this and every bot
            oX = i.x
            oY = i.y

            dX = self.x - oX
            dY = self.y - oY

            dist = (dX*dX)+(dY*dY)
            dist = math.sqrt(dist)
            g = .3

            if i.color == (255,0,0):
                g = .1
                if self.color == (255,0,0):
                    g = .3

            if i.color == (0,255,0):
                if self.color ==(255,0,0):
                    g = .2
                else:
                    g = -.4
                
            if dist > 0:
                F = g*.3/dist
                mX += (F*dX)
                mY += (F*dY)


        if self.x < 5:
            mX = mX * - 1

        if self.x > 1295:
            mX = mX * - 1

        if self.y >795:
            mY = mY * -1

        if self.y < 5:
            mY = mY * -1
                    
            #if i.color == (255,0,0):
             #   if self.x < i.x:
             #       mX = mX + (dist/1000)

             #   else:
            #        mX = mX - (dist/1000)

              #  if self.y < i.y:
              #      mY = mY + (dist/1000)
             #   else:
             #       mY = mY - (dist/1000)
           # else:
            #    if self.x > i.x:
             #       mX = mX + (dist/10000)
            #    else:
            #        mX = mX - (dist/10000)

             #   if self.y > i.y:
             #       mY = mY + (dist/10000)
             #   else:
              #      mY = mY - (dist/10000)
        self.x = self.x + mX
        self.y = self.y + mY
            
            
    def show(self,display):
        pygame.draw.circle(display, self.color,(self.x, self.y), 10)



for i in range(0,pinkBots):
    bot = Bot(random.randint(1,1300), random.randint(1,800), (255,0,0)) 
    bots.append(bot)

for i in range(0,yellowBots):
    bot = Bot(random.randint(1,1300), random.randint(1,800), (215, 215, 18)) 
    bots.append(bot)

for i in range(0,greenBots):
    bot = Bot(random.randint(1,1300), random.randint(1,800), (0,255,0)) 
    bots.append(bot)


    
while True:

        
    display.fill((24,164,86))
    pygame.draw.rect(display, (0,0,25), (0,0,1300,1200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed();

    for i in bots:
        i.show(display)
        i.move()
        
    clock.tick(60)

    pygame.display.update()
   
