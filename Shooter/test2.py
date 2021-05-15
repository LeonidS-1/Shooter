import pygame as pg
from random import randint
W = 1600
H = 900
pg.init()
win = pg.display.set_mode((W, H))
pg.display.update() 
bullist = []
vislist = []
enemylist = []
mistaker5 = 0
moveprocess = False
shotguncount = 0
shotgun = True
# ((x, y, w, h)-кардинаты, 1 - тип, 1 - вид, 1000 - здоровье)
collist = [((0, 0, 10, 890), 1, 0, 0), ((0, 0, 1600, 10), 1, 0, 0), ((1590, 0, 10, 890), 1, 0, 0), ((0, 890, 1600, 10), 1, 0, 0), #граница
 ((390, 300, 20, 600), 1, 390, 260), ((790, 0, 20, 600), 1, 780, 600), ((1190, 300, 20, 600), 1, 1190, 240),#((650, 200, 20, 700), 1, 650, 160), #внутренние стены
 [(1420, 800, 20, 20), 2, 1, 1000], ]#[(1420, 800, 20, 20), 2, 1, 1000]] #Враги
###################
#   50 - 500
strikespeed = 50
###################
myhp = 1000
zeropoint = (100, 800)
for i in range(len(collist)):
    if collist[i][2] == 2:
        enemylist.append(Enemy(collist[i]))
# pic1 =  pg.image.load(r'pic333.jpg')
# pg.mouse.set_cursor(pic1)

# #print(pg.transform.laplacian(pic1))
# pg.draw.polygon(win, [(0, 0), (10, 0), (10, 10), (0, 10)], pic1, 0)

def game():
    global zeropoint, myhp
    
    for i in range(len(bullist)):         
        
                  
        if -30 <= bullist[i][0][0] <= 1630 and -30 <= bullist[i][0][1]<= 930:
            movetype = bullist[i][3]
            koef = bullist[i][1] 
            
                
            if bullist[i][2] == 1.5:                
                bulletcrd = (bullist[i][0][0] + 1, bullist[i][0][1] - 1*bullist[i][1])  
                                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 1.5, movetype)) 
            elif bullist[i][2] == 1.0:
                bulletcrd = (bullist[i][0][0] + 1*bullist[i][1], bullist[i][0][1] - 1)
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 1.0, movetype)) 
            elif bullist[i][2] == 2.5:                
                bulletcrd = (bullist[i][0][0] + 1, bullist[i][0][1] + 1*bullist[i][1])  
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 2.5, movetype)) 
            elif bullist[i][2] == 2.0:
                bulletcrd = (bullist[i][0][0] + 1*bullist[i][1], bullist[i][0][1] + 1)
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 2.0, movetype)) 
            elif bullist[i][2] == 3.5:                
                bulletcrd = (bullist[i][0][0] - 1*bullist[i][1], bullist[i][0][1] + 1)  
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 3.5, movetype)) 
            elif bullist[i][2] == 3.0:
                bulletcrd = (bullist[i][0][0] - 1, bullist[i][0][1] + 1*bullist[i][1])
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 3.0, movetype))  
            elif bullist[i][2] == 4.5:                
                bulletcrd = (bullist[i][0][0] - 1, bullist[i][0][1] - 1*bullist[i][1])  
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 4.5, movetype)) 
            elif bullist[i][2] == 4.0:
                bulletcrd = (bullist[i][0][0] - 1*bullist[i][1], bullist[i][0][1] - 1)
                
                bullist.pop(i)
                bullist.insert(i, (bulletcrd, koef, 4.0, movetype))  
            
        else:
            bullist.pop(i)                
        


    mistaker1 = False

    for i in range(len(bullist)):    
        for j in range(len(collist)):
            if mistaker1 == False and bullist[i][3] == 3:
                if zeropoint[0]-40 <= bullist[i][0][0] <= zeropoint[0]+40 and zeropoint[1]-40 <= bullist[i][0][1] <=zeropoint[1]+40:
                    myhp-=100
                    if myhp<=0:
                        zeropoint = (100, 800)
                        myhp = 1000
                    bullist.pop(i)
                    mistaker1 = True
                    

            if mistaker1 == False and collist[j][0][0] <= bullist[i][0][0] <= collist[j][0][0]+collist[j][0][2] and collist[j][0][1] <= bullist[i][0][1] <=collist[j][0][1] + collist[j][0][3]:
                
                if collist[j][1] == 1:                                     
                    bullist.pop(i)
                    mistaker1 = True
                if collist[j][1] == 2:                    
                    collist[j][3] -=250                  
                    if collist[j][3] <=0:
                        collist.pop(j)
                    bullist.pop(i)
                    mistaker1 = True

    
        try:
            if bullist[i][3] == 0:
                pg.draw.circle(win, ('#d77d31'), bullist[i][0], 5)
            elif bullist[i][3] == 3:
                pg.draw.circle(win, (255, 0, 0), bullist[i][0], 5)
        except:

            pass

    pg.display.flip()
    
def process(connect):
    global moveprocess
    while 1:        
        for event in pg.event.get():
            if event.type == pg.QUIT:                
                pg.quit()
                exit()
        
        
        ####### Передвижение игрока и снарядов
        moveandpaint()
        
        ####### Выстрелы          
        shots(0)
        
        ####### Взгляд врагов  
        vision(connect)
        
        #######
        
        #on_my_way()

def paint():
    win.fill((255, 255, 255))
    for x1 in range(len(collist)):
        if collist[x1][1] == 1:
            pg.draw.rect(win, (0, 0, 0), collist[x1][0])
        if collist[x1][1] == 2:
            pg.draw.circle(win, (255, 0, 0), (collist[x1][0][0]+collist[x1][0][2]//2, collist[x1][0][1]+collist[x1][0][2]//2), collist[x1][0][2])
    for x2 in range(len(bullist)):
        if bullist[x2][3] == 0:
            pg.draw.circle(win, ('#d77d31'), bullist[x2][0], 5)
        elif bullist[x2][3] == 3:
            pg.draw.circle(win, (255, 0, 0), bullist[x2][0], 5)        
    pg.draw.circle(win, (0, 0, 0), zeropoint, 40)


def moveandpaint():
    global zeropoint
    key = pg.key.get_pressed()


    moveallow = 0
        
    
    for j in range(strikespeed):
            
        game()
        if key[pg.K_a]:
            for i in range(len(collist)):
                if (collist[i][1] == 1 or collist[i][1] == 2) and 0 <= zeropoint[0]-collist[i][0][0]-collist[i][0][2]<=40 and not  (zeropoint[1]>=collist[i][0][1]+collist[i][0][3]+40 or zeropoint[1]<=collist[i][0][1]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0]-0.35, zeropoint[1])
            moveallow = 0                
        if key[pg.K_d]:
            for i in range(len(collist)):
                if (collist[i][1] == 1 or collist[i][1] == 2) and 0 <= collist[i][0][0]-zeropoint[0]<=40 and not (zeropoint[1]>=collist[i][0][1]+collist[i][0][3]+40 or zeropoint[1]<=collist[i][0][1]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0]+0.35, zeropoint[1]) 
            moveallow = 0
        if key[pg.K_w]:
            for i in range(len(collist)):
                if (collist[i][1] == 1 or collist[i][1] == 2) and 0 <= zeropoint[1]-collist[i][0][1]-collist[i][0][3]<=40 and not  (zeropoint[0]>=collist[i][0][0]+collist[i][0][2]+40 or zeropoint[0]<=collist[i][0][0]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0], zeropoint[1]-0.35) 
            moveallow = 0
        if key[pg.K_s]:
            for i in range(len(collist)):
                if (collist[i][1] == 1 or collist[i][1] == 2) and 0 <= collist[i][0][1]-zeropoint[1]<=40 and not (zeropoint[0]>=collist[i][0][0]+collist[i][0][2]+40 or zeropoint[0]<=collist[i][0][0]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0], zeropoint[1]+0.35) 
            moveallow = 0
        #vision(0)
        paint()
        
        # win.fill((255, 255, 255))
        # for i in range(len(collist)):
        #     if collist[i][1] == 1:
        #         pg.draw.rect(win, (0, 0, 0), collist[i][0])
        #     if collist[i][1] == 2:
        #         pg.draw.circle(win, (255, 0, 0), (collist[i][0][0]+collist[i][0][2]//2, collist[i][0][1]+collist[i][0][2]//2), collist[i][0][2])
                
        # pg.draw.circle(win, (0, 0, 0), zeropoint, 40)
    
def shots(connect1):
         
    global zeropoint, shotguncount
    zeropoint1 = zeropoint 
    clicked = pg.mouse.get_pressed()  
    if connect1 == 0.0:
        mouse = pg.mouse.get_pos()
        
        bulletcrd = zeropoint
        movetype = 0 
        
   
    elif len(connect1) == 5: 
        mouse =  zeropoint
        
        zeropoint = connect1[0]
        movetype = 3
    
    else:
        
        mouse = (connect1[1], connect1[2])
        zeropoint = connect1[0]
        movetype = 1
    if movetype == 0:
        space = 40
    if movetype == 3:
        
        space = 20
        shotguncount+=1
        if shotguncount ==4:
            shotguncount=0
    if movetype == 1:
        space = 20
    if (clicked[0]==1 or connect1 != 0) and (shotguncount == 3 or movetype !=3):
        # for xxx in range(3):
        if mouse[0] >= zeropoint[0] and  mouse[1] <= zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = zeropoint[1] - mouse[1] 
            if xchange>=ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] + space, zeropoint[1] - space*koef)
                bullist.append((bulletcrd, koef, 1.5, movetype)) 
                # bullist.append((bulletcrd, koef+koef/10, 1.5)) 
                # bullist.append((bulletcrd, koef-koef/10, 1.5))                     
            elif  ychange>=xchange :
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] + space*koef, zeropoint[1] - space)
                bullist.append((bulletcrd, koef, 1.0, movetype))  
        elif mouse[0] >= zeropoint[0] and  mouse[1] >= zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = mouse[1] - zeropoint[1]
            if xchange>=ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] + space, zeropoint[1] + space*koef)
                bullist.append((bulletcrd, koef, 2.5, movetype)) 
            elif  ychange>=xchange :
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] + space*koef, zeropoint[1] + space)
                bullist.append((bulletcrd, koef, 2.0, movetype))
        elif mouse[0] <= zeropoint[0] and  mouse[1] >= zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = zeropoint[1] - mouse[1]
            if xchange>=ychange:                    
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] - space*koef, zeropoint[1] + space)
                bullist.append((bulletcrd, koef, 3.5, movetype)) 
            elif  ychange>=xchange :
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] - space, zeropoint[1] + space*koef)
                bullist.append((bulletcrd, koef, 3.0, movetype))
        elif mouse[0] <= zeropoint[0] and  mouse[1] <= zeropoint[1]:
            xchange = zeropoint[0] - mouse[0] 
            ychange = zeropoint[1] - mouse[1]
            if xchange>=ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] - space, zeropoint[1] - space*koef)
                bullist.append((bulletcrd, koef, 4.5, movetype)) 
            elif  ychange>=xchange :
                koef =xchange / ychange
                bulletcrd = (zeropoint[0] - space*koef, zeropoint[1] - space) 
                bullist.append((bulletcrd, koef, 4.0, movetype))
            # if movetype!=1:
            #     break
    zeropoint = zeropoint1
        
def vision(mouse1):
    
    
    global vislist, moveprocess, mistaker5, bullist
    for i in range(len(collist)):
        if collist[i][2] == 2:            
            for movei in range(len(bullist)):
                if bullist[movei][3] == 1:
                    collist[i][0] = [bullist[movei][0][0], bullist[movei][0][1], 20, 20]


    
    
    mistaker4 = 0
    for ox in collist:
        if ox[1] == 2:
            mistaker4 = 1
    if mistaker4 == 0:
        
        collist.append([(1420, 800, 20, 20), 2, 1, 1000])
    for enemy in range(len(collist)):

        if collist[enemy][1] == 2:
            if mouse1 ==0:                
                vislist = []
                mouse = zeropoint
            else:
                mouse = mouse1
        
            zeropoint1 = (collist[enemy][0][0]+collist[enemy][0][2]//2, collist[enemy][0][1]+collist[enemy][0][2]//2)
            bulletcrd = zeropoint1
            #print(bulletcrd, mouse)
            if mouse[0] >= zeropoint1[0] and  mouse[1] <= zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = zeropoint1[1] - mouse[1] 
                if xchange>=ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 10.5
                    vislist.append((bulletcrd, koef, 10.5, 0)) 
                elif  ychange>=xchange :
                    koef =xchange / ychange 
                    littlehelp = 10.0
                    vislist.append((bulletcrd, koef, 10.0, 0))   
            elif mouse[0] >= zeropoint1[0] and  mouse[1] >= zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = mouse[1] - zeropoint1[1]
                if xchange>=ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 20.5
                    vislist.append((bulletcrd, koef, 20.5, 0)) 
                elif  ychange>=xchange :
                    koef =xchange / ychange 
                    littlehelp = 20.0
                    vislist.append((bulletcrd, koef, 20.0, 0))
            elif mouse[0] <= zeropoint1[0] and  mouse[1] >= zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = zeropoint1[1] - mouse[1]
                if xchange>=ychange:                    
                    koef =xchange / ychange 
                    littlehelp = 30.5
                    vislist.append((bulletcrd, koef, 30.5, 0)) 
                elif  ychange>=xchange :
                    koef =ychange / xchange 
                    littlehelp = 30.0
                    vislist.append((bulletcrd, koef, 30.0, 0))
            elif mouse[0] <= zeropoint1[0] and  mouse[1] <= zeropoint1[1]:
                xchange = zeropoint1[0] - mouse[0] 
                ychange = zeropoint1[1] - mouse[1]
                if xchange>=ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 40.5
                    vislist.append((bulletcrd, koef, 40.5, 0)) 
                elif  ychange>=xchange :
                    koef =xchange / ychange
                    littlehelp = 40.0
                    vislist.append((bulletcrd, koef, 40.0, 0))
    
    mistaker3 = 0
    while mistaker3 == 0 :
        for event in pg.event.get():
            if event.type ==pg.QUIT:                
                pg.quit()
                exit()
        if len(vislist)==0:
            mistaker3 = 1
        for i in range(len(vislist)): 
            
            if vislist[i][2] == 10.5:                
                bulletcrd = (vislist[i][0][0] + 1, vislist[i][0][1] - 1*vislist[i][1])  
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 10.5, 0)) 
                
            elif vislist[i][2] == 10.0:
                bulletcrd = (vislist[i][0][0] + 1*vislist[i][1], vislist[i][0][1] - 1)
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 10.0, 0)) 
            elif vislist[i][2] == 20.5:                
                bulletcrd = (vislist[i][0][0] + 1, vislist[i][0][1] + 1*vislist[i][1])  
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 20.5, 0)) 
            elif vislist[i][2] == 20.0:
                bulletcrd = (vislist[i][0][0] + 1*vislist[i][1], vislist[i][0][1] + 1)
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 20.0, 0)) 
            elif vislist[i][2] == 30.5:                
                bulletcrd = (vislist[i][0][0] - 1*vislist[i][1], vislist[i][0][1] + 1)  
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 30.5, 0)) 
            elif vislist[i][2] == 30.0:
                bulletcrd = (vislist[i][0][0] - 1, vislist[i][0][1] + 1*vislist[i][1])
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 30.0, 0))  
            elif vislist[i][2] == 40.5:                
                bulletcrd = (vislist[i][0][0] - 1, vislist[i][0][1] - 1*vislist[i][1])  
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 40.5, 0)) 
            elif vislist[i][2] == 40.0:
                bulletcrd = (vislist[i][0][0] - 1*vislist[i][1], vislist[i][0][1] - 1)
                koef = vislist[i][1]
                vislist.pop(i)
                vislist.insert(i, (bulletcrd, koef, 40.0, 0)) 
            



            #pg.draw.circle(win, (0, 0, 0), bulletcrd, 40) 
            #pg.draw.line(win, (255, 0, 0), zeropoint1, bulletcrd, 2)

            for enemy in range(len(collist)):
                if collist[enemy][1] == 2:
                    for o in range(len(vislist)):   
                        mistaker1 = True
                        for j in range(len(collist)):
                            # if collist[j][1] == 1:
                            #     collist[enemy][0] = (collist[j][2], collist[j][3], 20, 20)
                                #pg.time.delay(50)  
                            if mistaker1 == True:
                                if collist[j][0][0] <= vislist[o][0][0] <= collist[j][0][0]+collist[j][0][2] and collist[j][0][1] <= vislist[o][0][1] <=collist[j][0][1] + collist[j][0][3]:
                                    
                                    mistaker1 = False
                                    if collist[j][1] == 1 :
                                        mistaker3 = 1
                                        if not j <= 3 and collist[j][1] == 1 :

                                                    
                                                #print(pack)
                                                #collist[enemy][0] = (strt[0], strt[1], 20, 20)
                                            #if mistaker5 == 0:
                                            #mistaker5 = (collist[enemy][0], collist[j][2], collist[j][3], zeropoint)

                                            # 
                                            #       bullist.insert(i, (bulletcrd, koef, 2.0, movetype)) 
                                            
                                            #collist[enemy][0] = (collist[j][2], collist[j][3], 20, 20)
                                            #
                                            
                                                    
                                            shots((collist[enemy][0], collist[j][2], collist[j][3], zeropoint))
                                            
                                            #for xxx in range(30):    
                                            for moving in range(len(bullist)):

                                                if bullist[moving][3] == 1:                                               
                                                                            
                                                    collist[enemy][0] = (bullist[moving][0][0], bullist[moving][0][1], 20, 20)
                                                    bullist.pop(moving)
                                                paint()
                                            #vision(1)    
                                                    
                                            
                                            ##################collist[enemy][0] = (collist[j][2], collist[j][3], 20, 20)
                                            


                                            #print((bulletcrd, koef, littlehelp))    
                                            #shots(mistaker5)
                                                
                                            
                                            #process(0)

                                if zeropoint[0]-10 <= vislist[o][0][0] <= zeropoint[0]+10 and zeropoint[1]-10 <= vislist[o][0][1] <= zeropoint[1]+10:
                                    shots(((collist[enemy][0][0]+collist[enemy][0][2]//2, collist[enemy][0][1]+collist[enemy][0][2]//2), collist[j][2], collist[j][3], zeropoint, 'shoot'))
                                    mistaker3 = 1
                                    moveprocess = False
                                    mistaker1 = False
                                    #mistaker5 = 0           
                                    #vislist = [vislist[0]]           
                                    #process(0)
                                    #vision(1)
                                    
                                    
                            
                            else:
                                
                                continue
            #vision(1)  

def start():

    try:
        process(0)
    except:
        start()

start()