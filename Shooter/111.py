import pygame as pg
from random import randint
W = 1600
H = 900
pg.init()
win = pg.display.set_mode((W, H))
strt = [900, 300]
fin = [700, 800]


pack = [0, 0]


xway = fin[0] - strt[0]
yway = fin[1] - strt[1]


while 1:        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    key = pg.key.get_pressed()
    win.fill((255, 255, 255))
    pg.draw.circle(win, (0, 0, 0), strt, 40)
    pg.draw.circle(win, (0, 0, 0), fin, 40)

    
            
    if strt == fin:
        
        pack = [0, 0]
        
        xway = fin[0] - strt[0]
        yway = fin[1] - strt[1]

    else:
        if pack[1] == 1 and strt[1] == fin[1]:
            pack[0] = 0
            
        elif pack[1] == 1:
            if yway >0:
                strt[1]+=1
            else:
                strt[1]-=1
                
            if pack[0] >0:
                pack[0] -=1
            else:
                pack[0] +=1
        
        if pack[1] == 0 and strt[0] == fin[0]:
            pack[0] = 0
            
        elif pack[1] == 0:
            if xway>0:
                strt[0]+=1
            else:
                strt[0]-=1

            if pack[0] >0:
                pack[0] -=1
            else:
                pack[0] +=1


    memory1 = fin    
    if key[pg.K_d]:
        fin[0] +=1
        xway = fin[0] - strt[0]
        yway = fin[1] - strt[1]
        
           
        


    if key[pg.K_a]:
        fin[0] -=1
        xway = fin[0] - strt[0]
        yway = fin[1] - strt[1]
          
        

    if key[pg.K_s]:
        fin[1] +=1

        xway = fin[0] - strt[0]
        yway = fin[1] - strt[1]
           
        

    if key[pg.K_w]:
        fin[1] -=1
        xway = fin[0] - strt[0]
        yway = fin[1] - strt[1]

           
        
    
    if randint(1, 2) == 2:
        pack = [xway/100 *randint(1, 100), 0]
    else:            
        pack = [yway/100*randint(1, 100), 1]    
    
    pg.display.update() 













































































































