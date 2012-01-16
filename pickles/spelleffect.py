#!/usr/bin/python

import pickle

fst=False
sel=True
if fst:
	if sel:
		spells = pickle.load(open('spells2.p','rb'))
		spells['select']=[]
	else:
		spells = pickle.load(open('spells.p','rb'))
		spells['effect']=[]
else:
	spells = pickle.load(open('spells2.p','rb'))

for x in range(len(spells['name'])):
#for x in range(2):
	if fst:
		if sel:
			spells['select'].append("")
		else:
			spells['effect'].append([])
	else:
		if sel:
			ts='select'
		else:
			ts='effect'
			
		print spells['name'][x]
		t=raw_input(spells[ts][x])
		if t == 'quit':
			break
		if t == 'none':
			spells[ts][x]=[]
		elif t != '':
			if sel:
				spells[ts][x]=t
			else:
				spells[ts][x]=(t.split(','))
		

pickle.dump(spells, open('spells2.p','wb'))
