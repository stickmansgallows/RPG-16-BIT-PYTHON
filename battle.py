from characters import *
import random
import time

def animateAttack(playerpic,attacktype,targetpic,damage):
def animateDefend(playerpic,defendtype):

def fullRandAttack(player, target, actor, actionName):
    #For randomly assigning targets for spells and abilities. Also handles undirected attacks (status effects)
    LT = len(target)
    LP = len(player)
    #Numbers < LT refer to side of target
    #Numbers >= LT refer to side of actor
    damage=[]
    hit=[]
    if atname = 'Attack':
        hit.append(random.choice(range(LT)))
        damage.append(pattack(player,target[hit[0]]))
    else:
        atspell = Spell(atname)
        if atspell.power==0: #Special attacks
            #Do special stuff...so much...
        if atspell.target='one' or (atspell.target='any' and random.random()<.5):
            damage.append(mattack(player,atspell,target[random.choice(range(LT))],False))
        else:
            for x in range(LT):
               damage.append(mattack(player,atspell,target[x],True))

            
    return hit, damage
                
def timeATB(thing):
    if thing.status['haste']:
        val=126
    elif thing.status['slow']:
    	val=48
    elif thing.status['stop'] or thing.status['petrify'] or thing.status['freeze'] or thing.status['sleep']:
        val=0
	else:
		val=96
    return val    
    
def pattack(player, target):
    if player.type == 'player':
		vigor2 = player.stats['vigor']*2
		if vigor2 > 255:
			vigor2 = 255
		attack = player.stats['bpower'] + vigor2
		if player.relic[0] == 'gauntlet' or player.relic[1] == 'gauntlet':
			attack += player.stats['bpower']*.75
		damage = player.stats['bpower'] + player.level*player.level*attack/256*3/2
		if player.relic[0] == 'offering' or player.relic[1] == 'offering':
			damage /= 2
		#If genji glove is equipped but only one weapon, damage*=.75
		#If atlas armlet or hero ring, damage*=1.25 no stack
		if player.status.backrow:
			damage /= 2
		dmult = player.status.morph*2+player.status.berserk
		if random.random() < .03:
			dmult += 2
		damage += damage/2*dmult
	elif player.kind == 'monster':
		damage = (player.level * player.level * (player.stats['bpower'] * 4 + player.stats['vigor']) / 256)

	
	if hitcalc(player.stats['hitrate'], player, target, 'p'):
		return damagecalc(player, target, damage, 'p')
	else:
		return 0

def mattack(player, spell, target, mult):
	if target.null=spell.element:
		return 0
		
	if spell.phys:
		player.stats['bpower']=spell.power
		return  pattack(player,target)
	if player.kind == 'player':
		damage = (spell.power*4 + (player.level * player.stats['mpower'] * 1.5 * spell.power / 32.0))
		if relic[0] == 'earring' or relic[0] == 'hero ring':
			damage *= 1.25
		if relic[1] == 'earring' or relic[1] == 'hero ring':
			damage *= 1.25
		if mult:
			damage /= 2
		if player.morph:
			damage *= 2
	elif player.kind == 'monster':
		damage = (spell.power*4 + player.level * player.stats['mpower']*1.5*spell.power/32)
		
	if target.absorb=spell.element:
		t=-1
	else:
		t=1
		
	if target.weak=spell.element:
		t=2
	
	if spell.igdef:
		r='mig'
	else:
		r='m'
			
	if hitcalc(spell.hitrate, player, target, r):
		return t*damagecalc(player, target, damage, r)
	else:
		return 0
	

	
def damagecalc(player, target, damage, attacktype):
	damage = damage * int(random.uniform(224,255))/256 + 1
	if attacktype == 'p':
		damage = (damage * (255 - target.stats['defense']) / 256) + 1
		if target.status.safe:
			damage = (damage * 170 / 256) + 1
		if target.defend:
			damage /= 2
		if target.status.backrow:
			damage /= 2
		if player.faceleft == target.faceleft:
			damage *= 1.5
		if target.status.petrify:
			damage = 0
	elif attacktype == 'm':
		damage = (damage * (255 - target.stats['mdefense']) / 256) + 1
		if target.status.morph:
			damage /= 2
		if target.status.shell:
			damage = (damage * 170 / 256) + 1
	elif attacktype == 'pu':
		damage = (damage * (255 - target.stats['defense']) / 256) + 1
					
	if target.kind == player.kind and damage > 0:
		damage /= 2
	return damage
		
		
def hitcalc(hit, player, target, attacktype):
	if target.status.clear:
		if attacktype[0] == 'm' :
			return True
		else:
			return False
	#Death protection
	#Unblockable
	if target.status.sleep or target.status.petrify or target.status.freeze or target.status.stop:
		return True
	if player.faceleft == target.faceleft:
		return True
	if hit == 255:
		return True
	if attacktype == 'p' and target.status.image:
		return False
	
	if attacktype == 'p':
		blockvalue = (255 - target.stats['evade'] * 2) + 1
	else:
		blockvalue = (255 - target.stats['mblock'] * 2) + 1
	if blockvalue > 255:
		blockvalue = 255
	if blockvalue < 1:
		blockvalue = 1
	if (hit * blockvalue / 256) > random.uniform(0,99):
		return True
	else:
		return False
		
		

if __name__ == '__main__':
	thing=[]
	thing.append(Player('Sabin', 500000))
	print thing[0].name, thing[0].level, thing[0].maxhp, thing[0].maxmp
	thing.append(Monster('steroidite'))
	print thing[1].name, thing[1].level, thing[1].maxhp, thing[1].maxmp
	thing[0].atb=0
	battlespeed=1
	thing[1].atb=0
	counter=0
	while 1:
		time.sleep(1/30)	
		counter+=1
		if thing[0].hp <= 0:
				print thing[0].name+' has fallen'
				break
		if thing[1].hp <= 0:
				print thing[1].name+' has fallen'
				break
				
		for i in range(len(thing)):
			#print i, thing[i].atb
			if thing[i].status.haste:
				val=126
			elif thing[i].status.slow:
				val=48
			else:
				val=96
			if thing[i].type == 'player':
				d=val/16*(thing[i].stats['speed']+20)
				thing[i].atb+=d				
			else:
				d=(val*(thing[i].stats['speed']+20)+(255-((battlespeed-1)*24)))/16
				thing[i].atb+=d

			if thing[i].atb >= 65536:
				thing[i].atb=0
				if i==0:
					t=1
				else:
					t=0
				d=pattack(thing[i],thing[t])
				if d > 0:
					print thing[i].name+' hits '+thing[t].name+' for '+str(d)+' damage'
				else:
					print thing[i].name+' missed'
	if (hit * blockvalue / 256) > random.uniform(0,99):
		return True
	else:
		return False
		
			
	
#Blind reduces hitrate by 50%, increases hitter rate by 25%
#Beads half hitter rate
#zombie, auto-life and confustion get hit 25% more
#poison, critical, seizure, and haste decrease hit rate by 25%
