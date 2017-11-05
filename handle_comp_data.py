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
filepath = 'stat_data.csv'
outputpath = "comp"
#length of file
lenoffil = lengthoffile(filepath)
#tsUnixNano, accel_x,accel_y,accel_z,gyro_x,gyro_y,gyro_z,ir,red,ir_filt,red_filt
#idx = [2]+list(range(11,21))
#tsUnixNano, accel_x,accel_y,accel_z,gyro_x,gyro_y,gyro_z,ir,red,ir_filt,red_filt
idx = [2]+list(range(12,18))
f = open(filepath, "r") 
for i,line in enumerate(f):
	currentline = line[:-1].split(",")
	if(i == 0):
		names = [currentline[i] for i in idx]
	else:
		store.append([float(currentline[i]) if isfloat(currentline[i]) else np.nan for i in idx])
	print("{} %\r".format(round((i/lenoffil)*100,2)), end = '')
f.close()

out = np.array(store)
np.save(outputpath, out)
np.save("data/comp_name", names)

