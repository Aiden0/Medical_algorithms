#from numpy import genfromtxt
#data = genfromtxt('raw.csv',delimiter
import numpy as np

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
def lengthoffile(filepath):
	num_lines = sum(1 for line in open(filepath))
	return num_lines

def getpatid(filepath):
	count = 0
	with open(filepath, "r") as filestream:
		for line in filestream:
			
			if(count>1):
				pat_id = line.split(",")[3]
				break
	return pat_id

store = []
#This is the name you change
filepath = 'raw.csv'
#lenoffil = 7302818
lenoffil = lengthoffile(filepath)
#date,
idx = [2]+list(range(11,21))
f = open(filepath, "r") 
for i,line in enumerate(f):
	currentline = line.split(",")
	store.append([float(currentline[i]) if isfloat(currentline[i]) else np.nan for i in idx])
	print("{} %".format(round((i/lenoffil)*100,2)),end="\r")
f.close()

out = np.array(store)
np.save("data", out)

