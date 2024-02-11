import pygame
import sys
import random
import math


display = pygame.display.set_mode((1300,800) ,flags=pygame.SCALED, vsync=0)
pygame.display.set_caption('Bots of Boria')

clock = pygame.time.Clock()

time = 0

Grav =  random.uniform(0, 2)

downOn = False

#fewer bots
lowMode = False
emptyMode = False
# Generate random counts for bots of each color
pinkBots = random.randint(1, 25) 
yellowBots = random.randint(1, 25) 
greenBots = random.randint(1, 25) 
blueBots = random.randint(1, 25) 
orangeBots = random.randint(1, 25)  # Add orange bots
cyanBots = random.randint(1, 25)    # Add cyan bots
redBots = random.randint(1, 25)

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
g37 = random_number = random.uniform(-1, 1)
g38 = random_number = random.uniform(-1, 1)
g39 = random_number = random.uniform(-1, 1)
g40 = random_number = random.uniform(-1, 1)
g41 = random_number = random.uniform(-1, 1)
g42 = random_number = random.uniform(-1, 1)


#Contagion logic
c1 =random.randint(0,2)
c2 =random.randint(0,2)
c3 =random.randint(0,2)
c4 =random.randint(0,3)
c5 =random.randint(0,3)
c6 =random.randint(0,3)
c7 =random.randint(0,3)


d1 =random.randint(0,3)
d2 =random.randint(0,3)
d3 =random.randint(0,3)
d4 =random.randint(0,3)
d5 =random.randint(0,3)
d6 =random.randint(0,3)
d7 =random.randint(0,3)



#how contagious? 
cc1 =random.randint(0,10)
cc2 =random.randint(0,10)
cc3 =random.randint(0,10)
cc4 =random.randint(0,10)
cc5 =random.randint(0,10)
cc6 =random.randint(0,10)
cc7 =random.randint(0,10)
#Used to determine what color this one changes others to
c11 = (255,0,0)
c12 = (255,0,0)
c13 = (255,0,0)
c14 = (255,0,0)
c15 = (255,0,0)
c16 = (255,0,0)
c17 = (255,0,0)
        
bots = []
tiles = []

gDist = random.randint(100,400)
#color of particles user can place
placeColor = (255,0,0)

class Tile:
    def __init__(self, x, y, particles, g, color):
        self.x = x
        self.y = y
        self.particles = particles
        self.g = g
        self.color = color
        
    def show(self,display):
        pygame.draw.rect(display, self.color,(self.x, self.y, 100, 100))

    def calcGrav(self):
        ultG = 0
        usedBots = 0
        for i in bots:
            
            if i.x >= self.x and i.x < self.x + 100 and i.y >= self.y and i.y < self.y + 100 and self.particles != []:
                usedBots = usedBots + 1
                if i.color == (255,0,0):
                    ultG  = ultG + g1
                elif i.color == (0,255,0):
                    ultG  = ultG + g2
                elif i.color == (0,0,255):
                    ultG  = ultG + g3
                elif i.color == (255,165,0):  # Orange color
                    ultG  = ultG + g4
                elif i.color == (0,255,255):  # Cyan color
                    ultG  = ultG + g5
                elif i.color == (215, 134, 18):  # Cyan color
                    ultG  = ultG + g6
                else:
                    ultG  = ultG + g7
        if usedBots > 0:
            ultG  = ultG / (usedBots)
        self.g = ultG

             
            
        
    
class Bot:
    def __init__(self, x, y, color, contagious, conColor, conChance, conDist, tile):
        self.x = x
        self.y = y
        self.color = color
        self.contagious = contagious
        self.conColor = color
        self.conChance = 10
        self.conDist = .5
        self.tile = tile
        
 

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
        global g37
        global g38
        global g39
        global g41
        global g42
        global c1
        global c2
        global c3
        global c4
        global c5
        global c6

        global grav
        global downOn
        global gDist
        

        if self.color == (255, 0, 0) and c1 == True:
            self.contagious = True

        if self.color == (215, 215, 18) and c2 == True:
            self.contagious = True

        if self.color == (0, 255, 0) and c3 == True:
            self.contagious = True

        if self.color == (0, 0, 255) and c4 == True:
            self.contagious = True

        if self.color == (200, 55, 187) and c5 == True:
            self.contagious = True

        if self.color == (0, 255, 255) and c6 == True:
            self.contagious = True
        ##SET BOUNDS##

        #if self.x < 16:
            #self.x = self.x + 20

        #if self.x > 1294:
            #self.x = self.x - 20

        #if self.y >794:
            #self.y = self.y - 20

        #if self.y < 6:
            #self.y = self.y + 20

        #Will be used to move bot after gravity effects are calculated
        mX = 0
        mY = 0
        
        #Determine what tile the particle is in
        for i in tiles:
            if self.x >= i.x and self.x < i.x + 100 and self.y >= i.y and self.y < i.y + 100:
                self.tile = i
            oX = i.x
            oY = i.y

            dX = self.x - oX
            dY = self.y - oY

            dist = (dX*dX)+(dY*dY)
            dist = math.sqrt(dist)
            
            g = i.g
            if dist > 0 and i != self.tile  :
                F = g/(dist*Grav)
                mX += (F*dX)
                mY += (F*dY)
        
        #Need to calculate gravity
        for i in bots:
            #Get distance between this and every bot
            oX = i.x
            oY = i.y

            dX = self.x - oX
            dY = self.y - oY

            dist = (dX*dX)+(dY*dY)
            dist = math.sqrt(dist)
            
            if dist <= self.conDist  and self.contagious == True and self.color != i.color:
                sChance = random.randint(0,self.conChance)
                if sChance == 1:
                    i.color = self.conColor
                    i.contagious = False
                    i.conColor = self.conColor
                    if i.color == (255,0,0):
                        i.conColor = c11
                        i.conDist = d1
                        i.conChance = cc1
                        if c1 == True:
                            i.contagious = True
                    elif i.color == (215,215,18):
                        i.conColor = c12
                        i.conDist = d2
                        i.conChance = cc2
                        if c2 == True:
                            i.contagious = True
                    elif i.color == (0, 255, 0):
                        i.conColor = c13
                        i.conDist = d3
                        i.conChance = cc3
                        if c3 == True:
                            i.contagious = True
                    elif i.color == (0, 0, 255):
                        i.conColor = c14
                        i.conDist = d4
                        i.conChance = cc4
                        if c4 == True:
                            i.contagious = True
                    elif i.color == (200, 55, 187):
                        i.conColor = c15
                        i.conDist = d5
                        i.conChance = cc5
                        if c5 == True:
                            i.contagious = True
                    elif i.color == (0, 255, 255):
                        i.conColor = c16
                        i.conDist = d6
                        i.conChance = cc6
                        if c6 == True:
                            i.contagious = True
                    elif i.color == (200,0,0):
                        i.conColor = c17
                        i.conDist = d7
                        i.conChance = cc7
                        if c7 == True:
                            i.contagious = True
                    i.conDist = self.conDist
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
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g6
                else:
                    g = g7
            elif i.color == (0,255,0):
                if self.color ==(255,0,0):
                    g = g8
                elif self.color == (0,255,0):
                    g = g9
                elif self.color == (0,0,255):
                    g = g10
                elif self.color == (255,165,0):
                    g = g11
                elif self.color == (0,255,255):
                    g = g12
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g13
                else:
                    g = g14
            elif i.color == (0,0,255):
                if self.color ==(255,0,0):
                    g = g15
                elif self.color == (0,255,0):
                     g = g16
                elif self.color == (0,0,255):
                     g = g17
                elif self.color == (255,165,0):
                     g = g18
                elif self.color == (0,255,255):
                     g = g19
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g20
                else:
                    g = g21

            elif i.color == (255,165,0):
                if self.color ==(255,0,0):
                    g = g22
                elif self.color == (0,255,0):
                    g = g23
                elif self.color == (0,0,255):
                    g = g24
                elif self.color == (255,165,0):
                    g = g25
                elif self.color == (0,255,255):
                    g = g26
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g27
                else:
                    g = g28
            elif i.color == (0,255,255):
                if self.color ==(255,0,0):
                    g = g29
                elif self.color == (0,255,0):
                    g = g30
                elif self.color == (0,0,255):
                    g = g31
                elif self.color == (255,165,0):
                    g = g32
                elif self.color == (0,255,255):
                    g = g33
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g34
                else:
                    g=g35
            else:
                if self.color ==(255,0,0):
                    g = g36
                elif self.color == (0,255,0):
                    g = g37
                elif self.color == (0,0,255):
                    g = g38
                elif self.color == (255,165,0):
                    g = g39
                elif self.color == (0,255,255):
                    g = g40
                elif self.color == (215, 134, 18):  # Cyan color
                    g = g41
                else:
                    g = g42
                
            if dist > 0 and self.tile == i.tile or dist > 0 and dist <= gDist:
                F = g/(dist*Grav)
                mX += (F*dX)
                mY += (F*dY)

       
            


        #if self.x <= 6:
         #   mX = mX * - 1

       # if self.x >= 1294:
        #    mX = mX * - 1

        #if self.y >=794:
         #   mY = mY * -1

        #if self.y <= 6:
          #  mY = mY * -1
                    
        self.x = self.x + mX
        self.y = self.y + mY

        if downOn == True:
            self.y = self.y + 1.5

        
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


startX = 0
startY = 0
for i in range(225):
    tX = startX * 100
    tY = startY * 100
    startX = startX + 1
    if startX > 15:
        startY = startY + 1
        startX = 0
    tile = Tile(tX, tY, [], 0, (0,random.randint(1, 200),0))
    tiles.append(tile)
    

for _ in range(pinkBots + yellowBots + greenBots + blueBots + orangeBots + cyanBots + redBots):
    bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)]),False, (255,0,0),10,1,tiles[0])
    if bot.color == (255, 0, 0) and c1 == True:
        bot.contagious = True

    if bot.color == (215, 215, 18) and c2 == True:
        bot.contagious = True

    if bot.color == (0, 255, 0) and c3 == True:
        bot.contagious = True

    if bot.color == (0, 0, 255) and c4 == True:
        bot.contagious = True

    if bot.color == (200, 55, 187) and c5 == True:
        bot.contagious = True

    if bot.color == (0, 255, 255) and c6 == True:
        bot.contagious = True
    bots.append(bot)

comp = False




while True:
    mouseX, mouseY = pygame.mouse.get_pos()
        
    display.fill((24,164,86))
    pygame.draw.rect(display, (0,0,25), (0,0,1300,1200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed();

    if keys[pygame.K_1]:
        placeColor = (255,0,0)
    if keys[pygame.K_2]:
        placeColor = (0,255,0)
    if keys[pygame.K_3]:
        placeColor = (0,0,255)
    if keys[pygame.K_4]:
        placeColor = (255,165,0)
    if keys[pygame.K_5]:
        placeColor = (0,255,255)
    if keys[pygame.K_6]:
        placeColor = (215, 134, 18)
    if keys[pygame.K_7]:
        placeColor = (200, 55, 187)

    if event.type == pygame.MOUSEBUTTONDOWN:
            bot = Bot(mouseX, mouseY, placeColor,False, (255,0,0),10,1,tiles[0])
            bots.append(bot)

    if keys[pygame.K_g]:
        if downOn == False:
            downOn = True
        else:
            downOn = False
            
    if keys[pygame.K_0]:
        comp = True
    if keys[pygame.K_9]:
        comp = False

    if keys[pygame.K_l]:
        if lowMode == False:
            lowMode = True
        else:
            lowMode = False

    if keys[pygame.K_e]:
        if emptyMode == False:
            emptyMode = True
        else:
            emptyMode = False


    
        placeColor = (200, 55, 187)
        
    if keys[pygame.K_SPACE]:
        for i in tiles:
            i.particles = []
        for i in bots:
            i.x = random.randint(1, 1300)
            i.y = random.randint(1, 800)

    spawnNum = 270
  
        
    if keys[pygame.K_r]:
        bots = []
        for i in tiles:
            i.particles = []
        Grav =  random.uniform(.50, .8)

        cBots = random.randint(1, 5) 

        gDist = random.randint(50,300)
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
    

        c1 =random.randint(0,2)
        c2 =random.randint(0,2)
        c3 =random.randint(0,2)
        c4 =random.randint(0,2)
        c5 =random.randint(0,2)
        c6 =random.randint(0,2)
        c7 =random.randint(0,2)

        

        #how contagious? 
        cc1 =random.randint(0,10)
        cc2 =random.randint(0,10)
        cc3 =random.randint(0,10)
        cc4 =random.randint(0,10)
        cc5 =random.randint(0,10)
        cc6 =random.randint(0,10)
        cc7 =random.randint(0,10)


        #how far from is it contagious?
        d1 =random.uniform(0, 3)
        d2 =random.uniform(0, 3)
        d3 =random.uniform(0, 3)
        d4 =random.uniform(0, 3)
        d5 =random.uniform(0, 3)
        d6 =random.uniform(0, 3)
        d7 =random.uniform(0, 3)

        c11 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c12 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c13 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c14 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c15 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c16 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        c17 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c1 == 1:
            c11 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
            
        if c2 == 1:
            c12 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c3 == 1:
            c13 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c4 == 1:
            c14 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c5 == 1:
            c15 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c6 == 1:
            c16 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
        if c7 == 1:
            c17 = random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)])
                                 

        if lowMode == True:
            spawnNum = 150

        if emptyMode == True:
            spawnNum = 0
        for _ in range(spawnNum):
            if cBots == 1 or comp == True :
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187), (0, 255, 255)]),False,(0, 255, 255), 10,1,tiles[0])
            elif cBots == 2:
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0)]),False,(0, 255, 255), 10,1,tiles[0])
            elif cBots == 3:
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18)]),False,(0, 255, 255), 10,1,tiles[0])
            elif cBots == 4:
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0)]),False,(0, 255, 255), 10,1,tiles[0])
            elif cBots == 5:
                bot = Bot(random.randint(1, 1300), random.randint(1, 800), random.choice([(215, 134, 18),(255, 0, 0), (215, 215, 18), (0, 255, 0), (0, 0, 255), (200, 55, 187)]),False,(0, 255, 255), 10,1,tiles[0])
            
            if bot.color == (255,0,0) and c1 == 1:
                bot.conColor = c11
                bot.conChance = cc1
                bot.conDist = d1
                bot.contagious == True
            elif bot.color == (215,215,18) and c2 == 1:
                bot.conColor = c12
                bot.conChance = cc2
                bot.conDist = d2
                bot.contagious == True
            elif bot.color == (0, 255, 0) and c3 == 1:
                bot.conColor = c13
                bot.conChance = cc3
                bot.conDist = d3
                bot.contagious == True
            elif bot.color == (0, 0, 255) and c4 == 1:
                bot.conColor = c14
                bot.conChance = cc4
                bot.conDist = d4
                bot.contagious == True
            elif bot.color == (200, 55, 187) and c5 == 1:
                bot.conColor = c15
                bot.conChance = cc5
                bot.conDist = d5
                bot.contagious == True
            elif bot.color == (0, 255, 255) and c6 == 1:
                bot.conColor = c16
                bot.conChance = cc6
                bot.conDist = d6
                bot.contagious == True
            elif bot.color == (200, 0, 0) and c7 == 1:
                bot.conColor = c17
                bot.conChance = cc7
                bot.conDist = d7
                bot.contagious == True
                
            bots.append(bot)
            
            
        
    for i in tiles:
        #i.show(display)
        i.calcGrav()
    for i in bots:
        i.show(display)
        i.move()

    pygame.display.flip()
        
    clock.tick(160)

    pygame.display.update()
