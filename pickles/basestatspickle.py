#!/usr/bin/python
import pickle
players={}
inp = open('basestats.txt', 'r')
temp = "Go!"
i=0
stats = ['vigor', 'speed', 'stamina', 'mpower', 'bpower', 'defense','evade','mdefense','mblock']


i=0
flags={}
for t in stats:
	players[t]=[]
players['name']=[]
temp = inp.readline()
while temp != "":
	temp = inp.readline()
	players['name'].append(temp.rstrip())
	temp = inp.readline()
	for t in stats:
		temp = inp.readline()
		if t == 'evade' or t == 'mblock':
			temp = temp.split()[-1][0:-1]
		players[t].append(int(temp.split()[-1]))
		
	temp=inp.readline()
	temp=inp.readline()
	
inp.close()
inp = open('hpstart.txt','r')
l = len(players['name'])
players['hp']=[]
players['mp']=[]
for x in range(l):
	players['hp'].append(0)
	players['mp'].append(0)
while True:
	temp=inp.readline()
	if temp == "":
		break
	for x in range(len(temp.split())/3):
		for y in range(l):
			if temp.split()[x*3].capitalize() == players['name'][y]:
				players['hp'][y]=int(temp.split()[x*3+1])
				players['mp'][y]=int(temp.split()[x*3+2])
				break
		
				

temp = ['name','hp','mp']
for x in temp+stats:
	print players[x][l-1]
pickle.dump(players, open("basestats.p", "wb"))
