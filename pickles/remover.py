#!/usr/bin/python


inp = open('spells.txt', 'r')
outp = open('spells.tmp', 'w')

temp = inp.readline()
while temp != "":
	if len(temp.split()) != 0:
		outp.write(temp)
		
	temp=inp.readline()


