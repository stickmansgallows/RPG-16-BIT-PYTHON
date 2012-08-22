#Input players[4], monsters(array or formation), location, battlespeed
#Return plunder class 
YMAX
XMAX
XFACTOR
FONTSIZE
flip
stancelist=['Action','Hit','Victory-Left1','Victory-Left2','Cast1','Cast2','Battle','Wounded']
frontline
top
backline
xstagger
ystagger
actionline
xmons=[]
ymons=[]
LP = len(players)
LM = len(monsters)
dancelist
hold=False

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((XMAX,YMAX))
pygame.display.set_caption('FF6')

background = pygame.transform.scale(pygame.image.load(location+'.png'), (XMAX,YMAX))

charpics={}
charatb=[]
charready=[]
for x in stancelist:
    charpics[x]=[]
    for y in range(LP):
        charpics[x].append(pygame.transform.flip(pygame.image.load(players[y].name+'-'+x+'.gif'),flip,False))
        charatb.append(0)
        charready.append(False)

monspics=[]
monsatb=[]
monsready=[]
for x in range(LM):
    monspics.append(pygame.transform.flip(pygame.image.load(monsters[y].name+'.gif'),flip,False))
    monsatb.append(0)
    monsready.append(False)


fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello world!'

soundObj = pygame.mixer.Sound('ff3_bt.mid')

i=0
counter=0
victory=False
while True:	
    #Draw
	windowSurfaceObj.blit(background, (0,0))
    for x in range(LP):
	    windowSurfaceObj.blit(charpics[stance[x]][x], (frontline+front*players[x].status['backrow']+xstagger*x+action*actionline,top+player[x].pos*ystagger))
    for x in range(LM):
	    windowSurfaceObj.blit(monspics[x], (xmons[x],ymons[y]))
        
    #Victory
    if victory:
        vitorymidi.play()
        send = Plunder(players,monsters)
        if i < 100:
            msg = 'Items'
        elif i < 200:
            msg = 'GP'
        elif i < 300:
            msg = 'Experience'
        elif i < 400:
            msg = 'AP'
        elif i < 500:
            msg = 'Levels and abilities'
        i+=1
    else:    
        #Timer
		counter+=1	#Updated once per frame	
        if not hold:
            d=0
    		for x in range(LP):
    			val = timeATB(player[x])
    			charatb[x]+=val/16*(players[x].stats['speed']+20)
                if charatb >= 65536:
                    charready[x]=True
                    if player[x].status['berserk'] or player[x].status['muddle'] or player[x].status['zombie'] or player[x].status['dance']:
                        charready[x]=False
                        charatb[x]=0
                        hold=True
                        if player[x].status['muddle']:
                            h,d=attack(player,player,x,'Attack')
                        elif player[x].status['dance']:
                            h,d=attack(player,monster,x,random.choice(dancelist))
                        elif player[x].status['zombie']:
                            t=random.choice(range(LM+LP))
                            if t>LM:
                                h,d=attack(player,player,x,'Attack')
                            else:
                                h,d=attack(player,monster,x,'Attack')
                        else: #Berserk
                            h,d=attack(player,monster,x,'Attack')
                       #Display attack 
                    
            for x in range(LM):     
                val = timeATB(monsters[x]) 
    			monsatb+=(val*(monsters[x].stats['speed']+20)+(255-((battlespeed-1)*24)))/16
                if monsatb >= 65536:
                    attackname = monsters[x].nextScript()
                    #Determine target
                    damage = attack(monsters,target,x,attackname)
                    #Display attack
                    #Display defend
            #Add status effect expiration here
    
    
            #Choice
            for x in range(LP):
                if charready[x]:
                    charready[x]=False
                    #Choose action: Attack, defend, row, item, spell, ability
                    players[x].defend=False
                    stance[x]='Action'
                    if action=='Attack':
                        #Choose target: t
                        d = pattack(player[x],monster[t])
                    elif action=='Defend':
                        stance[x]='Defend'
                        players[x].defend=True
                    elif action=='Row':
                        players[x].status['backrow']=not players[x].status['backrow']
                    elif action=='Item':
                        #Choose item
                        #Choose target
                        #Make effect
                    elif action=='Spell':
                        stance[x]='Cast0'
                        casting = Spell(spellcast)
                        #Check for status spells
                        if (casting.target=='all' and casting.side=='en') or casting.target=='allall':
                            #Show all enemy selectors 
                            d1=[]
                            for y in range(LM):
                                d1.append(mattack(players[x],casting,monsters[y],True))
                        if (casting.target=='all' and casting.side=='self') or casting.target=='allall':
                            #Show
                            d2=[]
                            for y in range(LP):
                                d2.append(mattack(players[x],casting,players[y],True))
                        
                    elif action=='
            
        else: #Hold
        
        
	#msgSurfaceObj = fontObj.render(msg, False, redColor)
	#msgRectobj = msgSurfaceObj.get_rect()
	#msgRectobj.topleft=(10,20)
	#windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
				
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
            if event.key == K_RIGHT:
            if event.key == K_UP:
            if event.key == K_DOWN:
				msg='Arrow key'
			if event.key == K_a:
				msg='A key'
			if event.key == K_ESCAPE:
                pass
				#pygame.event.post(pygame.event.Event(QUIT))
	pygame.display.update()
	fpsClock.tick(30)
