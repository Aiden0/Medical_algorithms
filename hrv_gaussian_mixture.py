from sklearn import mixture
import numpy as np
from datetime import datetime



def day_array(data):
    times = []
    for dat in data:
        timdate = datetime.fromtimestamp(dat// 1000000000)
        ms = dat%1000000000
        ms/=1000
        timdate = timdate.replace(microsecond=int(ms))
        times.append(timdate)
        
    return times

import matplotlib.pyplot as plt


data = np.load("data/comp.npy")

idx = np.isnan(data[:,-1])==False
data2 = data[:,[0,-2,-1]]
#idx = np.isnan(data2[:,3])==False
idx = np.where(data2[:,-1] > 0)
data3 = data2[idx]

day_array = day_array(data[:,0])

tired = []
not_ti = []
for i in range(len(data)):
	if day_array[i].hour > 19 and day_array[i].hour < 23:
		tired.append(data[i])
	else:
		not_ti.append(data[i])
ti = np.array(tired)
not_ti = np.array(not_ti)


plt.plot(ti[:,-1],ti[:,-2],'*')
plt.plot(not_ti[:,-1],not_ti[:,-2],'*')
plt.show()


#data3 = data2[:,[0,3,4,5,6]]



#mixture.GaussianMixture(n_components=3, covariance_type='diag').fit()