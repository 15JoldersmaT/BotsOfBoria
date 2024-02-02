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
pinkBots = random.randint(1, 25) 
yellowBots = random.randint(1, 25) 
greenBots = random.randint(1, 25) 
blueBots = random.randint(1, 25) 
orangeBots = random.randint(1, 25)  # Add orange bots
cyanBots = random.randint(1, 25)    # Add cyan bots

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

g10 = random_number = random.uniform(-1, 1)
g11 = random_number = random.uniform(-1, 1)
g12 = random_number = random.uniform(-1, 1)
g13 = random_number = random.uniform(-1, 1)
g14 = random_number = random.uniform(-1, 1)
g15 = random_number = random.uniform(-1, 1)
g16 = random_number = random.uniform(-1, 1)

g17 = random_number = random.uniform(-1, 1)
g18 = random_number = random.uniform(-1, 1)
g19 = random_number = random.uniform(-1, 1)
g20 = random_number = random.uniform(-1, 1)
g21 = random_number = random.uniform(-1, 1)
g22 = random_number = random.uniform(-1, 1)
g23 = random_number = random.uniform(-1, 1)
g24= random_number = random.uniform(-1, 1)
g25 = random_number = random.uniform(-1, 1)
g26 = random_number = random.uniform(-1, 1)
g27 = random_number = random.uniform(-1, 1)
g28 = random_number = random.uniform(-1, 1)
g29 = random_number = random.uniform(-1, 1)
g30 = random_number = random.uniform(-1, 1)
g31 = random_number = random.uniform(-1, 1)
g32 = random_number = random.uniform(-1, 1)
g33 = random_number = random.uniform(-1, 1)
g34 = random_number = random.uniform(-1, 1)
g35 = random_number = random.uniform(-1, 1)
g36 = random_number = random.uniform(-1, 1)


bots = []

class Bot:
    def __init__(self, x, y, color):
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
        global g17
        global g18
        global g19
        global g20
        global g21
        global g22
        global g23
        global g24
        global g25
        global g26
        global g27
        global g28
        global g29
        global g30
        global g31
        global g32
        global g33
        global g34
        global g35
        global g36
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
                elif self.color == (255,165,0):  # Orange color
                    g = g4
                elif self.color == (0,255,255):  # Cyan color
                    g = g5
                else:
                    g = g6
            elif i.color == (0,255,0):
                if self.color ==(255,0,0):
                    g = g7
                elif self.color == (0,255,0):
                    g = g8
                elif self.color == (0,0,255):
                    g = g9
                elif self.color == (255,165,0):
                    g = g10
                elif self.color == (0,255,255):
                    g = g11
                else:
                    g = g12
            elif i.color == (0,0,255):
                if self.color ==(255,0,0):
                    g = g13
                elif self.color == (0,255,0):
                     g = g14
                elif self.color == (0,0,255):
                     g = g15
                elif self.color == (255,165,0):
                     g = g16
                elif self.color == (0,255,255):
                     g = g17
                else:
                    g = g18

            elif i.color == (255,165,0):
                if self.color ==(255,0,0):
                    g = g19
                elif self.color == (0,255,0):
                    g = g20
                elif self.color == (0,0,255):
                    g = g21
                elif self.color == (255,165,0):
                    g = g22
                elif self.color == (0,255,255):
                    g = g23
                else:
                    g = g24
            elif i.color == (0,255,255):
                if self.color ==(255,0,0):
                    g = g25
                elif self.color == (0,255,0):
                    g = g26
                elif self.color == (0,0,255):
                    g = g27
                elif self.color == (255,165,0):
                    g = g28
                elif self.color == (0,255,255):
                    g = g29
                else:
                    g=30
            else:
                if self.color ==(255,0,0):
                    g = g31
                elif self.color == (0,255,0):
                    g = g32
                elif self.color == (0,0,255):
                    g = g33
                elif self.color == (255,165,0):
                    g = g34
                elif self.color == (0,255,255):
                    g = g35
                else:
                    g = g36
                
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



for _ in range(pinkBots + yellowBots + greenBots + blueBots + orangeBots + cyanBots):
    bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (255, 165, 0), (0, 255, 255)]))
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
  
        cBots = random.randint(1, 5) 

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

        g10 = random_number = random.uniform(-1, 1)
        g11 = random_number = random.uniform(-1, 1)
        g12 = random_number = random.uniform(-1, 1)
        g13 = random_number = random.uniform(-1, 1)
        g14 = random_number = random.uniform(-1, 1)
        g15 = random_number = random.uniform(-1, 1)
        g16 = random_number = random.uniform(-1, 1)

        g17 = random_number = random.uniform(-1, 1)
        g18 = random_number = random.uniform(-1, 1)
        g19 = random_number = random.uniform(-1, 1)
        g20 = random_number = random.uniform(-1, 1)
        g21 = random_number = random.uniform(-1, 1)
        g22 = random_number = random.uniform(-1, 1)
        g23 = random_number = random.uniform(-1, 1)
        g24= random_number = random.uniform(-1, 1)
        g25 = random_number = random.uniform(-1, 1)
        g26 = random_number = random.uniform(-1, 1)
        g27 = random_number = random.uniform(-1, 1)
        g28 = random_number = random.uniform(-1, 1)
        g29 = random_number = random.uniform(-1, 1)
        g30 = random_number = random.uniform(-1, 1)
        g31 = random_number = random.uniform(-1, 1)
        g32 = random_number = random.uniform(-1, 1)
        g33 = random_number = random.uniform(-1, 1)
        g34 = random_number = random.uniform(-1, 1)
        g35 = random_number = random.uniform(-1, 1)
        g36 = random_number = random.uniform(-1, 1)
        if cBots == 1:
            for _ in range(120):
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (255, 165, 0), (0, 255, 255)]))
                bots.append(bot)
        elif cBots == 2:
            for _ in range(120):
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(255, 0, 0), (0, 255, 0), (255, 165, 0), (0, 255, 255)]))
                bots.append(bot)
        elif cBots == 3:
            for _ in range(120):
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(0, 255, 0), (255, 165, 0), (0, 255, 255)]))
                bots.append(bot)
        else:
            for _ in range(120):
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(0, 255, 0), (0, 255, 255)]))
                bots.append(bot)
            
            

            
        
        
    for i in bots:
        i.show(display)
        i.move()
        
    clock.tick(60)

    pygame.display.update()
   
