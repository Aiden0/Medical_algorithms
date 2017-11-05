import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

def make_date(mins,h,d,m,y):
	s= datetime.datetime.utcfromtimestamp(0)
	return s.replace(year=y, month= m, day=d, hour=h, minute = mins)



store = []
#This is the name you change
filepath = 'anotes.csv'
#length of file
idx = [2,3,4]
f = open(filepath, "r") 
for i,line in enumerate(f):
	currentline = line[:-1].split(",")
	if currentline[4] == "Fatigued":
		dt = datetime.datetime.strptime(currentline[2], "%a %d %b %Y")
		tmp = datetime.datetime.strptime(currentline[3], "%H:%M")
		dt = dt.replace(hour = tmp.hour, minute = tmp.minute)
		store.append(dt)

f.close()

np.save("data/fatig", store)





idx = []
idx.append(make_date(0,00,18,10,2017))
np.save("fatig", idx)