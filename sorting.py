import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 700

FONT_BIG = pygame.font.SysFont('comicsans',40)
FONT_MEDIUM = pygame.font.SysFont('comicsans',30)
FONT_SMALL = pygame.font.SysFont('comicsans',15)

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Sorting')

LIGHT_BLUE = (64,223,208)
BLUE = (41,41,64)
DARK_BLUE = (15,15,38)
BLACK_BLUE = (5,5,28)
RED = (255,10,10)
GREEN = (10,255,10)
WHITE = (255,255,255)
L_BLUE = (20,20,255)
ORANGE = (255,100,0)

NUM_BAR = 50
BORDER = 25

SORTED = False

SPACE = (WIDTH - 25 - BORDER) / NUM_BAR

BAR_WIDTH, BAR_HEIGHT = SPACE - 1.2, 2.87

FPS = 60

RUN = True

DOWN = 25

COUNT = 0

name = FONT_MEDIUM.render('Abhi',1,WHITE)
project = FONT_BIG.render('SORTING',1,WHITE)
sorting = [
    FONT_SMALL.render('1.Selection Sort',1,WHITE),
    FONT_SMALL.render('2.Insertion Sort',1,WHITE),
    FONT_SMALL.render('3.Bubble Sort',1,WHITE)
]
reset = FONT_SMALL.render('0.Reset',1,WHITE)
    
class Bar:
    def __init__(self,x,y,width,height,value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = LIGHT_BLUE
        self.value = value
    
    def reset(self,num):
        self.x = BORDER + num * SPACE
        return self
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    
    def check(self):
        self.color = RED
        
    def done(self):
        self.color = GREEN
    
    def match(self):
        self.color = L_BLUE
    
    def back(self):
        self.color = LIGHT_BLUE
        
sort = [x for x in range(1, NUM_BAR + 2)]
random.shuffle(sort)
bar = [Bar((BORDER + i * SPACE),(HEIGHT - DOWN - (BAR_HEIGHT * sort[i])),BAR_WIDTH, BAR_HEIGHT * sort[i],sort[i]) for i in range(NUM_BAR)]

def main(win):
    clock = pygame.time.Clock()
    
    global RUN
    global bar
    global SORTED
    
    while RUN:
        clock.tick(FPS)
        draw(win,bar)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_0]:
            random.shuffle(sort)
            bar =  [Bar((BORDER + i * SPACE),(HEIGHT - DOWN - (BAR_HEIGHT * sort[i])),BAR_WIDTH, BAR_HEIGHT * sort[i],sort[i]) for i in range(NUM_BAR)]
            SORTED = False
        
        if keys[pygame.K_1]:
            check()
            selectionSort(bar,win)
        
        if keys[pygame.K_2]:
            check()
            insertionSort(bar,win)
        
        if keys[pygame.K_3]:
            check()
            bubbleSort(bar,win)
    
    pygame.quit()

def check():
    global SORTED
    global bar
    if SORTED:
        SORTED = False
        random.shuffle(sort)
        bar =  [Bar((BORDER + i * SPACE),(HEIGHT - DOWN - (BAR_HEIGHT * sort[i])),BAR_WIDTH, BAR_HEIGHT * sort[i],sort[i]) for i in range(NUM_BAR)]
         
# Function Draw a Screen
def draw(win,bar):
    global reset
    global name
    global sorting
    global project
    
    win.fill(BLUE)
    
    pygame.draw.rect(win, DARK_BLUE, (0,0,800,180))
    
    win.blit(project, (30,20))
    
    win.blit(name, (40,90))
    
    pygame.draw.rect(win, BLUE, (250,15,15,150))
    
    for i in range(len(sorting)):
        win.blit(sorting[i],(270,13 + (25 * i)))
    win.blit(reset,(460,13))
    
    for i in bar:
        i.draw(win)
        
    pygame.display.update()

def selectionSort(bar,win):
    global SORTED
    SORTED = True
    global RUN
    
    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        
        min = i
        
        for u in range(i+1, len(bar)):
            bar[min].match()
            bar[u].check()
            draw(win, bar)
            bar[u].back()
            
            if bar[u].y > bar[min].y:
                bar[min].back()
                min = u
                
        bar[len(bar) - 1].back()
        temp = bar[min]
        bar[min] = bar[i]
        bar[i] = temp
        bar[min].reset(min)
        bar[i].reset(i).done()
        

def insertionSort(bar,win):
    global RUN
    global SORTED
    SORTED = False
    
    for i in range(1,len(bar)):
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        j = i
        
        while j > 0 and bar[j].value < bar[j-1].value:
            if not RUN:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                    break
            bar[i].check()
            draw(win, bar)
            bar[i].back()
            bar[j], bar[j-1] = bar[j-1], bar[j]
            bar[j].reset(j)
            bar[j-1].reset(j-1)
            j -= 1
            
    for i in range(len(bar)):
        bar[i].done()
        pygame.time.delay(2)
        draw(win, bar)
        
def bubbleSort(bar,win):
    global RUN
    global SORTED
    SORTED = True
    
    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
            
        for j in range(len(bar) - 1 - i):
            bar[j].check()
            draw(win, bar)
            bar[j].back()
            
            if bar[j].value > bar[j + 1].value:
                temp = bar[j]
                bar[j] = bar[j + 1]
                bar[j + 1] = temp
                bar[j].reset(j)
                bar[j + 1].reset(j + 1)
        
        bar[len(bar) - 1 - i].done()

if __name__ == "__main__":
    main(win)
