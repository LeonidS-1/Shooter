import pygame as pg
from random import randint
W = 1600
H = 900
pg.init()
win = pg.display.set_mode((W, H))
pg.display.update() 
bullist = []
vislist = []
# ((x, y, w, h)-кардинаты, 1 - тип, 1 - вид, 1000 - здоровье)
collist = [((0, 0, 10, 890), 1, 0, 0), ((0, 0, 1600, 10), 1, 0, 0), ((1590, 0, 10, 890), 1, 0, 0), ((0, 890, 1600, 10), 1, 0, 0), #граница
 ((390, 300, 20, 600), 1, 390, 260), ((790, 0, 20, 600), 1, 790, 620), ((1190, 300, 20, 600), 1, 1190, 260), #внутренние стены
 [(1420, 800, 20, 20), 2, 1, 1000], ] #Враги
###################
#   50 - 500
strikespeed = 50
###################

zeropoint = (100, 800)

def game():
    global zeropoint
    for i in range(len(bullist)):         
        try:       
            if -30 < bullist[i][0][0] < 1630 and -30 < bullist[i][0][1]< 930:
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
        except:
            continue

    
    mistaker1 = False
    for i in range(len(bullist)):    
        for j in range(len(collist)):
            if mistaker1 == False and collist[j][0][0] < bullist[i][0][0] < collist[j][0][0]+collist[j][0][2] and collist[j][0][1] < bullist[i][0][1] <collist[j][0][1] + collist[j][0][3]:
                
                if collist[j][1] == 1:                                     
                    bullist.pop(i)
                    mistaker1 = True
                if collist[j][1] == 2:                    
                    collist[j][3] -=250                  
                    if collist[j][3] <=0:
                        collist.pop(j)
                    bullist.pop(i)
                    mistaker1 = True

                          
        ### pg.draw.line(win, (0, 0, 0), (bullist[i][0][0] - 75, bullist[i][0][1] + 75*(bullist[i][1]*1.5)), bullist[i][0],  2)
        ### pg.draw.line(win, (0, 0, 0), (bullist[i][0][0] - 100, bullist[i][0][1] + 100*(bullist[i][1]/1.5)), bullist[i][0],  2)        
        try:
            if bullist[i][3] == 0:
                pg.draw.circle(win, ('#d77d31'), bullist[i][0], 5)
        except:
            
            continue

    pg.display.update()
def process(connect):
    while 1:        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        
        
        ####### Передвижение игрока и снарядов
        moveandpaint()
        
        ####### Выстрелы          
        shots(0)
        
        ####### Взгляд врагов  
        vision(connect)
        
        #######

def moveandpaint():
    global zeropoint
    key = pg.key.get_pressed()


    
    for j in range(strikespeed):
            
        game()
        moveallow = 0
        
        if key[pg.K_a]:
            for i in range(len(collist)):
                if collist[i][1] == 1 and 0 < zeropoint[0]-collist[i][0][0]-collist[i][0][2]<40 and not  (zeropoint[1]>collist[i][0][1]+collist[i][0][3]+40 or zeropoint[1]<collist[i][0][1]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0]-0.35, zeropoint[1])
            moveallow = 0                
        if key[pg.K_d]:
            for i in range(len(collist)):
                if collist[i][1] == 1 and 0 < collist[i][0][0]-zeropoint[0]<40 and not (zeropoint[1]>collist[i][0][1]+collist[i][0][3]+40 or zeropoint[1]<collist[i][0][1]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0]+0.35, zeropoint[1]) 
            moveallow = 0
        if key[pg.K_w]:
            for i in range(len(collist)):
                if collist[i][1] == 1 and 0 < zeropoint[1]-collist[i][0][1]-collist[i][0][3]<40 and not  (zeropoint[0]>collist[i][0][0]+collist[i][0][2]+40 or zeropoint[0]<collist[i][0][0]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0], zeropoint[1]-0.35) 
            moveallow = 0
        if key[pg.K_s]:
            for i in range(len(collist)):
                if collist[i][1] == 1 and 0 < collist[i][0][1]-zeropoint[1]<40 and not (zeropoint[0]>collist[i][0][0]+collist[i][0][2]+40 or zeropoint[0]<collist[i][0][0]-40):
                    moveallow = 1
            if moveallow == 0:
                zeropoint = (zeropoint[0], zeropoint[1]+0.35) 
            moveallow = 0
        
    



        win.fill((255, 255, 255))
        for i in range(len(collist)):
            if collist[i][1] == 1:
                pg.draw.rect(win, (0, 0, 0), collist[i][0])
            if collist[i][1] == 2:
                pg.draw.circle(win, (255, 0, 0), (collist[i][0][0]+collist[i][0][2]//2, collist[i][0][1]+collist[i][0][2]//2), collist[i][0][2])
                
        pg.draw.circle(win, (0, 0, 0), zeropoint, 40)


def shots(connect1):
    
    clicked = pg.mouse.get_pressed()  
    if connect1 == 0:
        mouse = pg.mouse.get_pos()
        
        bulletcrd = zeropoint
        movetype = 0
    else:
        mouse = connect1[0]
        zeropoint = (connect1[1], connect1[2])
        movetype = 1
    if clicked[0]==1 or connect1 != 0:
        
        if mouse[0] > zeropoint[0] and  mouse[1] < zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = zeropoint[1] - mouse[1] 
            if xchange>ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] + 40, zeropoint[1] - 40*koef)
                bullist.append((bulletcrd, koef, 1.5, movetype)) 
                # bullist.append((bulletcrd, koef+koef/10, 1.5)) 
                # bullist.append((bulletcrd, koef-koef/10, 1.5))                     
            elif  ychange>xchange :
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] + 40*koef, zeropoint[1] - 40)
                bullist.append((bulletcrd, koef, 1.0, movetype))   
        elif mouse[0] > zeropoint[0] and  mouse[1] > zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = mouse[1] - zeropoint[1]
            if xchange>ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] + 40, zeropoint[1] + 40*koef)
                bullist.append((bulletcrd, koef, 2.5, movetype)) 
            elif  ychange>xchange :
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] + 40*koef, zeropoint[1] + 40)
                bullist.append((bulletcrd, koef, 2.0, movetype))
        elif mouse[0] < zeropoint[0] and  mouse[1] > zeropoint[1]:
            xchange = mouse[0] - zeropoint[0]
            ychange = zeropoint[1] - mouse[1]
            if xchange>ychange:                    
                koef =xchange / ychange 
                bulletcrd = (zeropoint[0] - 40*koef, zeropoint[1] + 40)
                bullist.append((bulletcrd, koef, 3.5, movetype)) 
            elif  ychange>xchange :
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] - 40, zeropoint[1] + 40*koef)
                bullist.append((bulletcrd, koef, 3.0, movetype))
        elif mouse[0] < zeropoint[0] and  mouse[1] < zeropoint[1]:
            xchange = zeropoint[0] - mouse[0] 
            ychange = zeropoint[1] - mouse[1]
            if xchange>ychange:                    
                koef =ychange / xchange 
                bulletcrd = (zeropoint[0] - 40, zeropoint[1] - 40*koef)
                bullist.append((bulletcrd, koef, 4.5, movetype)) 
            elif  ychange>xchange :
                koef =xchange / ychange
                bulletcrd = (zeropoint[0] - 40*koef, zeropoint[1] - 40) 
                bullist.append((bulletcrd, koef, 4.0, movetype))


def vision(mouse1):
    
    
    global zeropoint, vislist
    for i in range(len(collist)):
        if collist[i][2] == 2:            
            for movei in range(len(bullist)):
                if bullist[movei][3] == 1:
                    collist[i][0] = [bullist[movei][0][0], bullist[movei][0][1], 20, 20]


    
    skndvislist = []
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
            if mouse[0] > zeropoint1[0] and  mouse[1] < zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = zeropoint1[1] - mouse[1] 
                if xchange>ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 10.5
                    vislist.append((bulletcrd, koef, 10.5, 0)) 
                elif  ychange>xchange :
                    koef =xchange / ychange 
                    littlehelp = 10.0
                    vislist.append((bulletcrd, koef, 10.0, 0))   
            elif mouse[0] > zeropoint1[0] and  mouse[1] > zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = mouse[1] - zeropoint1[1]
                if xchange>ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 20.5
                    vislist.append((bulletcrd, koef, 20.5, 0)) 
                elif  ychange>xchange :
                    koef =xchange / ychange 
                    littlehelp = 20.0
                    vislist.append((bulletcrd, koef, 20.0, 0))
            elif mouse[0] < zeropoint1[0] and  mouse[1] > zeropoint1[1]:
                xchange = mouse[0] - zeropoint1[0]
                ychange = zeropoint1[1] - mouse[1]
                if xchange>ychange:                    
                    koef =xchange / ychange 
                    littlehelp = 30.5
                    vislist.append((bulletcrd, koef, 30.5, 0)) 
                elif  ychange>xchange :
                    koef =ychange / xchange 
                    littlehelp = 30.0
                    vislist.append((bulletcrd, koef, 30.0, 0))
            elif mouse[0] < zeropoint1[0] and  mouse[1] < zeropoint1[1]:
                xchange = zeropoint1[0] - mouse[0] 
                ychange = zeropoint1[1] - mouse[1]
                if xchange>ychange:                    
                    koef =ychange / xchange 
                    littlehelp = 40.5
                    vislist.append((bulletcrd, koef, 40.5, 0)) 
                elif  ychange>xchange :
                    koef =xchange / ychange
                    littlehelp = 40.0
                    vislist.append((bulletcrd, koef, 40.0, 0))
    mistaker3 = 0
    while mistaker3 == 0:

        
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                exit()
        
        for i in range(len(vislist)): 
            
            
            # pg.draw.circle(win, (0, 0, 0), vislist[i][0], 10)  
            # pg.display.update()
            
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
            #pg.display.update() 
            
            for o in range(len(vislist)):   
                mistaker1 = True
                for j in range(len(collist)):
                    # if collist[j][1] == 1:
                    #     collist[enemy][0] = (collist[j][2], collist[j][3], 20, 20)
                        #pg.time.delay(50)  
                    if mistaker1 == True:
                        if collist[j][0][0] < vislist[o][0][0] < collist[j][0][0]+collist[j][0][2] and collist[j][0][1] < vislist[o][0][1] <collist[j][0][1] + collist[j][0][3]:
                            
                            mistaker1 = False
                            if collist[j][1] == 1:
                                mistaker3 = 1
                                if not j <= 3 and collist[j][1] == 1 :
                                    
                                    collist[enemy][0] = (collist[j][2], collist[j][3], 20, 20)
                                    
                                    #print((bulletcrd, koef, littlehelp))    
                                    shots((collist[enemy][0], collist[j][2], collist[j][3], zeropoint))
                                    
                                    process(0)
                                    #process((collist[j][2], collist[j][3]))
                        if zeropoint[0]-10 < vislist[o][0][0] < zeropoint[0]+10 and zeropoint[1]-10 < vislist[o][0][1] < zeropoint[1]+10:
                            mistaker3 = 1
                            #vislist = [vislist[0]]
                            
                            mistaker1 = False
                            process(0)             
                        # if zeropoint[0] < vislist[o][0][0] < zeropoint[0]+40 and zeropoint[1] < vislist[o][0][1] <zeropoint[1] + 40:
                        #     mistaker3 = 1
                        #     #vislist = [vislist[0]]
                        #     
                        #     mistaker1 = False
                        #     process(0)
                           
                    else:
                        break    
              

try:
    process(0)
except:
    #print("ERROR")
    process(0)