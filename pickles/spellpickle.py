#!/usr/bin/python

import pickle
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def yesno(s):
	if s.capitalize() == 'Yes':
		return True
	elif s.capitalize() == 'No':
		return False
	else:
		print s
		print "ERROR!!!"
		return False

spell={}
inp = open('spells.tmp', 'r')

cols = ['name','power','physical','igndef','unblock','hitrate','type']

for x in cols:
	spell[x]=[]
temp=inp.readline()
while temp != "":
	kind=temp[0:-2]
	temp=inp.readline()
	temp=inp.readline()
	while temp[-2] != ':':
		i=0
		#print temp
		if isInt(temp.split()[1]):
			spell['name'].append(temp.split()[i])
			i+=1
		else:
			spell['name'].append(" ".join(temp.split()[i:i+2]))
			i+=2
	
		spell['power'].append(int(temp.split()[i]))
		spell['igndef'].append(yesno(temp.split()[i+2]))
		spell['unblock'].append(yesno(temp.split()[i+3]))
		spell['physical'].append(yesno(temp.split()[i+1]))
		t = temp.split()[i+4]
		if t == "n/a":
			t = 255
		spell['hitrate'].append(int(t))
		spell['type'].append(kind)
		temp=inp.readline()
		if temp=="":
			break
	


i=40
for x in cols:
	print len(spell[x])
pickle.dump(spell, open("spells.p", "wb"))
