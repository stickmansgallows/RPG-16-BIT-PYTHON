#!/usr/bin/python
import pickle
level={}
inp = open('levels.txt', 'r')
level['hp']=[]
level['mp']=[]
level['exp']=[]
level['exp'].append(0)
level['hp'].append(0)
level['mp'].append(0)
temp = inp.readline()
while temp != "":
	temp = inp.readline()
	if temp == "":
		break
	#print len(temp.split())
	level['exp'].append(int(temp.split()[1]))
	level['hp'].append(int(temp.split()[2]))
	level['mp'].append(int(temp.split()[4]))
	
print level['hp']
pickle.dump(level, open("levels.p", "wb"))
