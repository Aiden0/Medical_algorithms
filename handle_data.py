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
	count = 0
	with open(filepath, "r") as filestream:
		for line in filestream:
			count += 1
	return count

def getpatid(filepath):
	count = 0
	with open(filepath, "r") as filestream:
		for line in filestream:
			
			if(count>1):
				pat_id = line.split(",")[3]
				break
	return pat_id

store = []
filepath = 'raw.csv'
#lenoffil = 7302818
lenoffil = lengthoffile(filepath)
#date,
idx = [2]+list(range(11,21))
f = open(filepath, "r") 
for i,line in enumerate(f):
	currentline = line.split(",")
	store.append([float(currentline[i]) if isfloat(currentline[i]) else np.nan for i in idx])
	print("{} %".format(round((i/7302818)*100,2)),end="\r")
f.close()

out = np.array(store)
data = np.sort(out[1:])




#_data = data[:,[2]+list(range(11,21))]
