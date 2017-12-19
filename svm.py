import math
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from statistics import median
import pan_tompkins as pan
import sys

# k ZAMIAST ECG
k=pan.ECG
x=scipy.signal.detrend(k)
x=x/max(abs(x))
x1=x
for n in range(pan.N): #transformacje
   x[pan.ind_p[n]:pan.ind_n[n]]=0
   if n==0:
       x[0:pan.ind_p[n]]=x[0:pan.ind_p[n]]-min(x[0:pan.ind_p[n]])
       m=median(x[0:pan.ind_p[n]])
       x1[0:pan.ind_p[n]]=x[0:pan.ind_p[n]]-m
   elif n>0:
       x[pan.ind_n[n-1]:pan.ind_p[n]]=x[pan.ind_n[n-1]:pan.ind_p[n]]-min(x[pan.ind_n[n-1]:pan.ind_p[n]])
       m=median(x[pan.ind_n[n-1]:pan.ind_p[n]])
       x1[pan.ind_n[n-1]:pan.ind_p[n]]=x[pan.ind_n[n-1]:pan.ind_p[n]]-m

max=max(x1)
for i in range(len(x1)):
    if x1[i]<0.07*max:
        x1[i]=0		#zerowanie mniejszych niz 0,07 max
    else:
        continue
'''
p11=plt.plot(pan.Time, x1, '-')
plt.xlim([0,5])
plt.show()

'''
# średnia
Esi=np.mean(x1)
index_pos=[0]*len(x1)
for i in range(len(x1)):
	if x1[i]>x1[i]*Esi:
		index_pos[i]=1 #.append
	else:
		continue
#p2=plt.plot(Time, sd, Time, index_pos)
#plt.show()

Delay=16 #Empirycznie dopasowane (Nie wiem skąd brali do QRSa)
Delay2=12 #Empirycznie dopasowane (Nie wiem skąd brali do QRSa)
Delay1=10
'''p3= plt.plot(pan.Time,x1,pan.Time,index_pos ) #-pan.Time[Delay-1]
plt.xlim([0, 3])
plt.show()
'''
# DETEKCJA P i T
# pochodna index_pos-mówi kiedy rośnie (1) a kiedy maleje (-1)
d_index_pos=np.diff(index_pos)
ind_p = []
ind_n = []
for i in range(len(d_index_pos)):
	if d_index_pos[i] == 1:
		ind_p.append(i) #indeks początków załamków
		#print(i/pan.fs)
	elif d_index_pos[i] == -1:
		ind_n.append(i) # indeks końców załamków

p,t=[],[]
N=len(ind_n)
p1,p2,t1,t2=np.zeros((2,N)),np.zeros((2,N)),np.zeros((2,N)),np.zeros((2,N))

	
if ind_n[0]<ind_p[0]: #jakby się zaczynało od środka górki
	ind_n.remove(ind_n[0])
	ind_p.pop()
for i in range(len(ind_n)):
	if i>0 and ind_n[i]>ind_p[i]:
		for n in range (ind_p[i],ind_n[i]):
			if n>0:
				if x1[n]>x1[n-1]:
					m=x1[n]
			#print(m)
		for j in range (ind_p[i-1],ind_n[i-1]):
			if j>0:
				if x1[j]>x1[j-1]:
					m1=x1[j]
			#print(m1)	
		if m>m1: #spr czy pierw załamek p potem t
			t.extend([(ind_p[i]-Delay)/pan.fs,(ind_n[i]-Delay)/pan.fs])	#dopisuje początek i koniec załamka t
			p.extend([(ind_p[i-1]-Delay)/pan.fs,(ind_n[i-1]-Delay)/pan.fs]) #dopisuje początek i koniec załamka p
			p1[0][i] = pan.Time[ind_p[i-1]-Delay]
			p1[1][i] = k[ind_p[i-1]-Delay]
			t1[0][i] = pan.Time[ind_p[i]-Delay]
			t1[1][i] = k[ind_p[i]-Delay]
			p2[0][i] = pan.Time[ind_n[i-1]+Delay1]
			p2[1][i] = k[ind_n[i-1]+Delay1]
			t2[0][i] = pan.Time[ind_n[i]+Delay2]
			t2[1][i] = k[ind_n[i]+Delay2]
			
for i in range(0,len(p),2):
	print ("Początek załamka p:",p[i],"Koniec załamka p:",p[i+1])
for i in range(0,len(t),2):
	print ("Początek załamka t:",t[i],"Koniec załamka t:",t[i+1])	

p11=plt.plot(pan.Time, k, '-',p1[0],p1[1],'^g',p2[0],p2[1],'^g',t1[0],t1[1],'^r',t2[0],t2[1],'^r')
plt.xlim([0,5])
plt.show()


