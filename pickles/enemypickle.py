#!/usr/bin/python

import pickle
import base64
import gzip

enemies={}
inp = open('monsters2.txt', 'r')
temp = "Go!"
i=0
#stats = ['vigor', 'speed', 'stamina', 'mpower', 'bpower', 'defense','evade','mdefense','mblock']
props = ['level', 'hp', 'mp', 'exp', 'gp']
stats = ['bpower', 'speed', 'hitrate', 'mpower', 'defense', 'evade', 'mdefense', 'mblock']
g1 = ['steal', 'itemwin', 'morph', 'morphp']
g2 = ['absorb', 'null', 'weak']
g3 = ['rage', 'sketch', 'control']
g4 = ['status', 'protected']
g5 = ['specialinfo']
g6 = ['weapongraphic', 'special']
g = g1+g2+g3+g4+g5+g6
i=0
flags={}
for t in g+props+stats:
	enemies[t]=[]
for t in g:
	flags[t]=False
enemies['name']=[]
temp = inp.readline()
while temp != "":
	while temp.split()[0] != str(i):
		temp = inp.readline()
		if temp == '':
			break
	if temp == '':
		break
	if len(temp.split()) == 1:
		enemies['name'].append('NA')
	else:
		enemies['name'].append(temp.split()[1])
	
	while temp.split()[0] != "Level:":
		temp = inp.readline()
	enemies['level'].append(int(temp.split()[1]))
	enemies['hp'].append(int(temp.split()[3]))
	enemies['mp'].append(int(temp.split()[5]))
	enemies['exp'].append(int(temp.split()[7]))
	enemies['gp'].append(int(temp.split()[9]))
	
	temp = inp.readline()
	enemies['bpower'].append(int(temp.split()[2]))
	enemies['speed'].append(int(temp.split()[5]))
	enemies['hitrate'].append(int(temp.split()[8]))
	enemies['mpower'].append(int(temp.split()[11]))
	
	temp = inp.readline()
	enemies['defense'].append(int(temp.split()[2]))
	enemies['evade'].append(int(temp.split()[5]))
	enemies['mdefense'].append(int(temp.split()[8]))
	enemies['mblock'].append(int(temp.split()[11]))
	
	
	while temp.split()[0] != 'Stats':
		temp = inp.readline()
		q=1
		if temp.split()[0]=='Steal:':
			namep='steal'
		elif temp.split()[0]=='Win:':
			namep='itemwin'
		elif temp.split()[0]=='Morph:':
			namep='morph'
		elif temp.split()[0]=='Morph':
			enemies['morphp'].append(float(temp.split()[3][0:-1]))
			continue
		elif temp.split()[0]=='Absorb:':
			namep='absorb'
		elif temp.split()[0]=='Nullify:':
			namep='null'
		elif temp.split()[0]=='Weakness:':
			namep='weak'
		elif temp.split()[0]=='Rage:':
			namep='rage'
		elif temp.split()[0]=='Sketch:':
			namep='sketch'
		elif temp.split()[0]=='Control:':
			namep='control'
		elif temp.split()[0]=='Status:':
			namep='status'
		elif temp.split()[0]=='Protected':
			namep='protected'
			q=2
		elif temp.split()[0]=='Special':
			if temp.split()[1]=='Info:':
				namep='specialinfo'
				q=2
			elif temp.split()[1]=='Attack:':
				enemies['special'].append(" ".join(temp.split()[2:]))
				continue
		elif temp.split()[0]=='Regular':
			enemies['weapongraphic'].append(" ".join(temp.split()[3:]))
			continue
		else:
			if temp.split()[0]=='Stats':
				break
			namep='protected'
			for j in range(len(temp.split())):
				if temp.split()[j][-1]==',':
					enemies[namep][i].append(temp.split()[j][0:-1])
				else:
					enemies[namep][i].append(temp.split()[j])
			continue
		
		enemies[namep].append([])
		for j in range(len(temp.split())-q):
			if temp.split()[j+q][-1]==',':
				enemies[namep][i].append(temp.split()[j+q][0:-1])
			else:
				enemies[namep][i].append(temp.split()[j+q])
		
	i+=1

for x in range(len(enemies['name'])):
    enemies['pic'].append(base64.encodestring(open(enemies['name'][x]+'.gif','rb').read())) #Test first
    
#Get scripts

pickle.dump(enemies, gzip.open("enemies.p", "wb"), -1)

