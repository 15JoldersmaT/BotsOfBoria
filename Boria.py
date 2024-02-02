import pygame
import sys
import random
import math

display = pygame.display.set_mode((1300,800) ,flags=pygame.SCALED, vsync=0)
pygame.display.set_caption('Bots of Boria')

clock = pygame.time.Clock()

time = 0

grav = 1

# Generate random counts for bots of each color
pinkBots = random.randint(1, 30) 
yellowBots = random.randint(1, 30) 
greenBots = random.randint(1, 30) 
blueBots = random.randint(1, 30) 


g1 = random_number = random.uniform(-1, 1)
g2 = random_number = random.uniform(-1, 1)
g3 = random_number = random.uniform(-1, 1)
g4 = random_number = random.uniform(-1, 1)
g5 = random_number = random.uniform(-1, 1)
g6 = random_number = random.uniform(-1, 1)
g7 = random_number = random.uniform(-1, 1)
g8 = random_number = random.uniform(-1, 1)
g9 = random_number = random.uniform(-1, 1)

g10 = random_number = random.uniform(-1, 1)
g11 = random_number = random.uniform(-1, 1)
g12 = random_number = random.uniform(-1, 1)
g13 = random_number = random.uniform(-1, 1)
g14 = random_number = random.uniform(-1, 1)
g15 = random_number = random.uniform(-1, 1)
g16 = random_number = random.uniform(-1, 1)

bots = []

class Bot:
    def __init__(self,x, y,color):
        self.x = x
        self.y = y
        self.color = color
        
 

            

    def move(self):
        global bots
        global g1
        global g2
        global g3
        global g4
        global g5
        global g6
        global g7
        global g8
        global g9
        global g10
        global g11
        global g12
        global g13
        global g14
        global g15
        global g16

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
                if self.color == (255,0,0):
                    g = g1
                elif self.color == (0,255,0):
                    g = g2
                elif self.color == (0,0,255):
                    g = g3
                else:
                    g = g4

            elif i.color == (0,255,0):
                if self.color ==(255,0,0):
                    g = g5
                elif self.color == (0,255,0):
                    g = g6
                elif self.color == (0,0,255):
                    g = g7
                else:
                    g = g8
            elif i.color == (0,0,255):
                if self.color ==(255,0,0):
                    g = g9
                elif self.color == (0,255,0):
                    g = g10
                elif self.color == (0,0,255):
                    g = g11
                else:
                    g = g12
            else:
                if self.color ==(255,0,0):
                    g = g13
                elif self.color == (0,255,0):
                    g = g14
                elif self.color == (0,0,255):
                    g = g15
                else:
                    g = g16
                
                
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
        if self.x < 15:
            self.x = 15

        if self.x > 1295:
            self.x = 1295

        if self.y >795:
            self.y = 795

        if self.y < 5:
            self.y = 5
            
            
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

for i in range(0,blueBots):
    bot = Bot(random.randint(1,1300), random.randint(1,800), (0,0,255)) 
    bots.append(bot)
    
while True:

        
    display.fill((24,164,86))
    pygame.draw.rect(display, (0,0,25), (0,0,1300,1200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed();

    if keys[pygame.K_r]:
        for i in bots:
            bots.remove(i)
        pinkBots = random.randint(1, 30) 
        yellowBots = random.randint(1, 30) 
        greenBots = random.randint(1, 30) 
        blueBots = random.randint(1, 30)

        g1 = random_number = random.uniform(-1, 1)
        g2 = random_number = random.uniform(-1, 1)
        g3 = random_number = random.uniform(-1, 1)
        g4 = random_number = random.uniform(-1, 1)
        g5 = random_number = random.uniform(-1, 1)
        g6 = random_number = random.uniform(-1, 1)
        g7 = random_number = random.uniform(-1, 1)
        g8 = random_number = random.uniform(-1, 1)
        g9 = random_number = random.uniform(-1, 1)
        g10= random_number = random.uniform(-1, 1)
        g11 = random_number = random.uniform(-1, 1)
        g12 = random_number = random.uniform(-1, 1)
        g13 = random_number = random.uniform(-1, 1)
        g14 = random_number = random.uniform(-1, 1)
        g15 = random_number = random.uniform(-1, 1)
        g16 = random_number = random.uniform(-1, 1)
        for i in range(0,pinkBots):
            bot = Bot(random.randint(1,1300), random.randint(1,800), (255,0,0)) 
            bots.append(bot)

        for i in range(0,yellowBots):
            bot = Bot(random.randint(1,1300), random.randint(1,800), (215, 215, 18)) 
            bots.append(bot)

        for i in range(0,greenBots):
            bot = Bot(random.randint(1,1300), random.randint(1,800), (0,255,0)) 
            bots.append(bot)

        for i in range(0,blueBots):
            bot = Bot(random.randint(1,1300), random.randint(1,800), (0,0,255)) 
            bots.append(bot)

            
        
        
    for i in bots:
        i.show(display)
        i.move()
        
    clock.tick(60)

    pygame.display.update()
   
