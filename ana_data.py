import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time


def convert_date(unixtime):
    ms = unixtime%1000000000
    dt = datetime.fromtimestamp(unixtime // 1000000000)
    return dt,ms

def day_array(data):
    times = []
    for dat in data:
        timdate = datetime.fromtimestamp(dat// 1000000000)
        ms = dat%1000000000
        ms/=1000
        timdate = timdate.replace(microsecond=int(ms))
        times.append(timdate)
        
    return times

def make_date(d,m,y):
    s="{:02d}/{:02d}/{:04d}".format(d,m,y)
    return time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())*1000000000

def chop_data(data):
    idx = []
    flag = 1
    for i,dat in enumerate(data):
        tmp = datetime.fromtimestamp(dat // 1000000000)
        if tmp.hour >= 8  and flag == 1:
            #print(i,end="\r")
            idx.append(i)
            flag = 0
        elif tmp.hour < 8:
            flag = 1
    return idx


#HRV data
data = np.load("stat_data.npy")
#RAW PPG date
raw = np.load("data.npy")


#remove nan data from HRV
idx = np.isnan(data[:,-1])==False
hrv = data[idx][:,[0,-1]]
idx = np.where(hrv[:,1] > 0)
hrv = hrv[idx]

#remove Nan date from raw
idx = np.isnan(raw[:,-2])==False
ppg = raw[idx][:,[0,-2]]


#get day times for hrv dat
hrv_days = day_array(hrv[:,0])
hrv_dat = hrv[:,1]
idx = chop_data(hrv[:,0])


#get day times
ppg_days = day_array(ppg[:,0])
ppg_dat = ppg[:,1]
idx2 = chop_data(ppg[:,0])


#cut date into day chunks###
cut_ppg_times = []
cut_ppg_dat = []
for i in range(len(idx2)-1):
    cut_ppg_times.append(ppg_days[idx2[i]:idx2[i+1]])
    cut_ppg_dat.append(ppg_dat[idx2[i]:idx2[i+1]])
cut_ppg_times.append(ppg_days[idx2[-1]:])
cut_ppg_dat.append(ppg_dat[idx2[-1]:])


cut_hrv_times = []
cut_hrv_dat = []
for i in range(len(idx)-1):
    cut_hrv_times.append(hrv_days[idx[i]:idx[i+1]])
    cut_hrv_dat.append(hrv_dat[idx[i]:idx[i+1]])
    
cut_hrv_times.append(hrv_days[idx[-1]:])
cut_hrv_dat.append(hrv_dat[idx[-1]:])


np.save("hrv_times",cut_hrv_times)
np.save("hrv_dat",cut_hrv_dat)
np.save("ppg_times",cut_ppg_times)
np.save("ppg_dat",cut_ppg_dat)

# #Plot 
# ax = plt.subplot(2,1,1)
# for i in range(len(cut_ppg_times)):
#     plt.plot(cut_ppg_times[i],cut_ppg_dat[i])
# plt.gcf().autofmt_xdate()
# plt.setp(ax.get_xticklabels(), fontsize=6)

# plt.subplot(2,1,2, sharex = ax)
# for i in range(len(cut_hrv_times)):
#     plt.plot(cut_hrv_times[i],cut_hrv_dat[i])
# plt.gcf().autofmt_xdate()