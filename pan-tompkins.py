import math
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

import sys

# ---------------------- WCZYTYWANIE DANYCH - FUNKCJA------------------------------------
time = []
resp = []
bp = []
ecg = []
def get_values_from_file(file_name):
	file_to_open = open(file_name)
	while(True):#iteracja po całym pliku
		line = file_to_open.readline()
		if line.__len__() == 0:
		#plik się skończył
			break
		if line[0].isdigit(): #bierzemy pod uwagę tylko linie zaczynające się cyfrą (pierwszy el.)
			line = line.replace('\n', '', 1) #usunięcie przejścia do nowej linii
			values = line.split('\t') #utweórz listę, separatorem jest tabulator
			time.append(float(values.__getitem__(0)))#zbieram wartości czysu (pierwsza kolumna linii
			resp.append(float(values.__getitem__(1)))
			bp.append(float(values.__getitem__(2)))
			ecg.append(float(values.__getitem__(3)))
		else:
			continue
	return time, resp, bp, ecg
# ---------------------------------------------------------------------------------------------------------------
plt.close('all')

# wczytanie danych
[Time, Resp, BPL, ECG]=get_values_from_file('sygnal.txt')

fs=200
t_temp=np.linspace(Time[0], Time[-1], fs*Time[-1])

ECG=np.interp(t_temp, Time, ECG)
Time=t_temp

p1=plt.plot(t_temp, ECG, '-')
#plt.xlim([0,2])
plt.show()

'''p2= plt.plot(Time, ECG)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude {\mu}V')
plt.xlim([0,2])
plt.title('Electrocardiogram')
plt.show()'''

fs=1/(Time[2]-Time[1])

# KROK 1 - detrendyzacja i normalizacja
x=scipy.signal.detrend(ECG)
x=x/max(abs(x))

# KROK 2 - filtr dolnoprzepustowy
b=[1, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 1]
a=[1, -2, 1]
x_lp_filter = scipy.signal.lfilter(b,a,x)
y=scipy.signal.detrend(x_lp_filter)
y=y/max(abs(y))

# KROK 3 - filtr górnoprzepustowy
b=[-1/32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/32]
a=[1, -1]
x_hp_filter = scipy.signal.lfilter(b,a,y)
z=scipy.signal.detrend(x_hp_filter)
z=z/max(abs(z))

# KROK 4 - filtr różniczkujący
b=[2/8, 1/8, 0, -1/8, -2/8]
a=[1]
x_dfilter = scipy.signal.lfilter(b,a,z)
sd=scipy.signal.detrend(x_dfilter)
sd=sd/max(abs(sd))

# Podniesienie do kwadratu
sd2=sd**2

# całkowanie
b=[1/31]*31
a=[1]
si=scipy.signal.lfilter(b,a,sd2)
si=scipy.signal.detrend(si)
si=si/max(abs(si))

# średnia
Esi=np.mean(si)
index_pos=[]
for i in range(len(si)):
	if si[i]>si[i]*Esi:
		index_pos.append(1)
	else:
		index_pos.append(0)
p2=plt.plot(Time, si, Time, index_pos)
plt.show()

Delay=35 #5+15+1+14
p3= plt.plot(Time,x,Time-Time[Delay-1],index_pos )
plt.xlim([0, 3])
plt.show()

# DETEKCJA QRS
# pochodna index_pos
d_index_pos=np.diff(index_pos)
ind_p = []
ind_n = []
for i in range(len(d_index_pos)):
	if d_index_pos[i] == 1:
		ind_p.append(i - Delay + 1)
	elif d_index_pos[i] == -1:
		ind_n.append(i - Delay + 1)

N=len(ind_n) #ilość pełnych f. prostokątnych

# przygotowanie miejsca w pamięci
Q=np.zeros((2,N))
R=np.zeros((2,N))
S=np.zeros((2,N))

for n in range(N):
    t_temp=Time[ind_p[n]:ind_n[n]]
    s_temp=ECG[ind_p[n]:ind_n[n]]

    R_temp = max(s_temp)
    R_ind = s_temp.tolist().index(R_temp)

    Q_temp = min(s_temp[1:R_ind]) #szuka w połówce QRSa
    Q_ind = s_temp[1:R_ind].tolist().index(Q_temp)

    S_temp = min(s_temp[R_ind:-1])
    S_ind = s_temp[R_ind:-1].tolist().index(S_temp)
    S_ind=S_ind+R_ind

    Q[0][n] = Time[ind_p[n]+Q_ind]
    Q[1][n] = ECG[ind_p[n]+Q_ind]
    R[0][n] = Time[ind_p[n]+R_ind]
    R[1][n] = ECG[ind_p[n]+R_ind]
    S[0][n] = Time[ind_p[n]+S_ind]
    S[1][n] = ECG[ind_p[n]+S_ind]



pp=plt.plot(Time, ECG,'-', R[0],R[1],'ro', Q[0],Q[1],'^g', S[0], S[1],'ks')
plt. xlim([10,13])
plt.show()



