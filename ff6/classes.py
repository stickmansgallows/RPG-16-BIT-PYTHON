 = basestats['hp'][x]
		self.maxmp = basestats['mp'][x]
		self.hp=self.maxhp
		self.mp=self.maxmp
		self.nextlevel = 32
		
		self.levelcheck()
		
		self.statlist = ['vigor', 'speed', 'stamina', 'mpower', 'bpower', 'defense','evade','mdefense','hitrate','mblock','element','absorb','null','weak','resist']
		
		self.esper = 'none'
		self.esperbonus = []
		self.esperspell = []
		self.spellist = {}
		
		self.stats={}
		self.equipmentlist=['rhand', 'lhand', 'helmet', 'armor', 'base','relic1','relic2']
		self.equipment = {}
		
		for t in self.statlist[0:-5]:
			self.equipment['base'][t]=basestats[t][x]
		for t in self.statlist[-5:]:
			self.equipment['base'][t]=[]
			
		for t in self.equipmentlist:
			self.equipitem('empty'+t)
		self.totalstats()
		
	def levelcheck(self):   #Checks experience for level gain
		send=0
		if self.experience >= self.nextlevel and self.level < 99:
			levels=pickle.load(open("levels.p","rb"))
		while self.experience >= self.nextlevel and self.level < 99:
			self.level += 1
			self.maxhp += levels['hp'][self.level]
			self.maxmp += levels['mp'][self.level]
			self.hp = self.maxhp
			self.mp = self.maxmp
			if self.level >= 99:
				self.nextlevel=0
			else:
				self.nextlevel = levels['exp'][self.level+1]
			send+=1
		return send	#How many levels gained
		
	def totalstats(self):   #Adds all item and base stats together. Bonus stats?
		for i in self.statlist:
			self.stats[i]=0
			for j in self.equipmentlist:
				self.stats[i]+=self.equipment[j].stats[i]
				
	def equipitem(self,this):   #To add item name to equipment slot and set stats
		itemlist = pickle.load(open("items.p","rb"))
		x = findnum(itemlist['name'],this)
		for t in self.statlist:
			self.equipment[itemlist['place'][x]][t]=itemlist[t][x]

	def equipesper(self,this):  #To add name to equipped esper, set level-up bonus, and spell learning
		esperlist = pickle.load(open('espers.p','rb'))
		x = findnum(esperlist['name'],this)
		self.esper=esperlist['name'][x]
		self.esperbonus = esperlist['bonus'][x]
		self.esperspell = esperlist['spells'][x]
			
class Monster:
	def __init__(self,this):
		monsterlist = pickle.load(open("enemies.p","rb"))
		x = findnum(monsterlist['name'],this)
		
		self.name = monsterlist['name'][x]
		self.status = Status()
        self.protected = Status()
		self.faceleft = False
		self.defend = False
		self.level = monsterlist['level'][x]
		self.experience = monsterlist['exp'][x]
		self.gp = monsterlist['gp'][x]
		self.maxhp = monsterlist['hp'][x]
		self.hp = monsterlist['hp'][x]
		self.maxmp = monsterlist['mp'][x]
		self.mp = monsterlist['mp'][x]
		self.kind = 'monster'
        self.boss = False
		self.stats={}
		self.stats['vigor']=int(random.uniform(56,63))
		temp = (self.hp/512)+16
		if temp > 40:
			temp = 40
		self.stats['stamina']=temp
		for t in ['speed', 'mpower', 'bpower', 'defense','evade','mdefense','hitrate','mblock']:
			self.stats[t]=monsterlist[t][x]
			
		self.absorb=monsterlist['absorb'][x]
		self.null=monsterlist['null'][x]
		self.weak=monsterlist['weak'][x]
		self.info=monsterlist['specialinfo'][x]
		self.special=monsterlist['special'][x]
		self.weapon=monsterlist['weaponsgraphic'][x]
        self.item=monsterlist['item'][x]
        self.steal=monsterlist['steal'][x]
        self.morph=monsterlist['morph'][x]
        self.morphp=monsterlist['morphp'][x]
        
        for t in self.status.afterbattlelist+self.status.inbattlelist:
            if t == monsterlist['status']:
                self.status.statuslist[t]=True
            if t == monsterlist['protected']:
                self.protected.statuslist[t]=True
        #Add script
        self.script=[]
        self.scriptp=0
        
        def nextScript(self):
            send = self.script[self.scriptp]
            self.scriptp+=1
            if self.scriptp >= len(self.script):
                self.script=0
            return send
                
class Plunder:
    def __init__(self,players,monster):
        self.exp=0
        self.gp=0
        self.hp=[0,0,0,0]
        self.mp=[0,0,0,0]
        self.ap=0
        self.status = [Status(),Status(),Status(),Status()]
        self.item=[]
        passStats(players)
        passBooty(monster)
        
    def passStats(self, players):
        for t in range(len(players)):
            self.hp[t]=players[t].hp
            self.mp[t]=players[t].mp
            for x in self.status.afterbattlelist:
                self.status[t].statuslist[x]=player[t].status.statuslist[x]
            
    def passBooty(self, monster):
        for x in range(len(monster)):
            self.exp+=monster.exp
            self.gp+=monster.gp
            if len(monster.item) > 0:
                self.item.append(monster.item)
            self.ap = self.exp/1000
            if self.ap < len(monster):
                self.ap=len(monster)
        