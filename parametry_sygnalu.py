# WYZNACZANIE PARAMETRÓW SYGNAŁU EKG

import matplotlib.pyplot as plt
import numpy as np

from wczytaj import ECG
from pan_tompkins import Q, R, S
from svm import P, T

def basic_parameters(ECG):
    ppValue = max(ECG) - min(ECG)   # amplituda sygnału
    meanValue = np.mean(ECG)    # wartość średnia sygnału
    return ppValue, meanValue

# odległość pomiędzy załamkami R (odległość R-R)
def RR_interval(R):
    N = len(R[0])
    # utworzenie tablicy dwuwymiarowej:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych odległości R-R
    # drugi wymiar - wektor wartości odległości pomiędzy każdymi kolejnymi dwoma załamkami R
    RR = np.zeros((2, N - 1))
    for i in range(N - 1):
        RR[0][i] = R[0][i]  # wartości w [s]
        RR[1][i] = (R[0][i + 1] - R[0][i]) * 1000  # wartości w [ms]
    return RR


# odległości pomiędzy początkami załamków P (odległości P-P)
def PP_interval(P):
    N = len(P[0])
    # tablica dwuwymiarowa:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych odległości P-P
    # drugi wymiar - wektor wartości odległości pomiędzy każdymi kolejnymi dwoma początkami załamków P
    PP = np.zeros((2, N - 1))
    for i in range(N - 1):
        PP[0][i] = P[0][i]  # wartości w [s]
        PP[1][i] = (P[0][i + 1] - P[0][i]) * 1000  # wartości w [ms]
    return PP

# tętno (HR - heart rate)
def heart_rate(R):
    N = len(R[0])
    RR = RR_interval(R)  # wygenerowanie wektora odległości R-R
    # utworzenie tablicy dwuwymiarowej:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych odległości R-R
    # drugi wymiar - wektor wartości tętna
    HR = np.zeros((2, N - 1))  # wektor tętna mierzonego jako odwrotność odległości R-R
    for i in range(N-1):
        HR[0][i] = R[0][i]  # wartości w [s]
        HR[1][i] = (1 / RR[1][i]) * 60 * 1000  # wartości w [bpm] (beats per minute)
    return HR

# czas trwania załamka P
def P_wave(P):
    N = len(P[0])
    # tablica dwuwymiarowa:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych załamków P
    # drugi wymiar - wektor wartości długości kolejnych załaów P
    P_len = np.zeros((2, N ))
    for i in range(N):
        P_len[0][i] = P[0][i]  # wartości w [s]
        P_len[1][i] = (P[1][i] - P[0][i]) * 1000  # wartości w [ms]
    return P_len

# czas trwania zespołu QRS
def QRS_duration(Q, S):
    N = len(Q[0])
    # tablica dwuwymiarowa:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych zespołów QRS
    # drugi wymiar - wektor wartości długości kolejnych zespołów QRS
    QRS_dur = np.zeros((2, N ))
    for i in range(N):
        QRS_dur[0][i] = Q[0][i]  # wartości w [s]
        QRS_dur[1][i] = (S[0][i] - Q[0][i]) * 1000  # wartości w [ms]
    return QRS_dur

# czas trwania załamka T
def T_wave(T):
    N = len(T[0])
    # tablica dwuwymiarowa:
    # pierwszy wymiar - wektor położenia na osi czasu punktów początków kolejnych załamków T
    # drugi wymiar - wektor wartości długości kolejnych załaów T
    T_len = np.zeros((2, N ))
    for i in range(N):
        T_len[0][i] = T[0][i]  # wartości w [s]
        T_len[1][i] = (T[1][i] - T[0][i]) * 1000  # wartości w [ms]
    return T_len


# wartości średnie
mean_RR_interval = np.mean(RR_interval(R)[1])
mean_PP_interval = np.mean(PP_interval(P)[1])
mean_heart_rate = np.mean(heart_rate(R)[1])
mean_P_wave = np.mean(P_wave(P)[1])
mean_QRS_duration = np.mean(QRS_duration(Q, S)[1])
mean_T_wave = np.mean(T_wave(T)[1])

# wykresy: tętno, R-R, P-P
fig1, (ax1, ax2, ax3) = plt.subplots(3,1)
fig1.subplots_adjust(hspace=0.5)
ax1.scatter(heart_rate(R)[0], heart_rate(R)[1])
ax1.set_xlabel('czas [s]')
ax1.set_ylabel('Tętno [bpm]')
ax1.set_xlim([0, heart_rate(R)[0][-1]+0.5])
ax1.set_ylim([50, 100])
ax1.plot(heart_rate(R)[0], [60]*len(heart_rate(R)[0]), '-r')
ax1.plot(heart_rate(R)[0], [80]*len(heart_rate(R)[0]), '-r')

ax2.scatter(RR_interval(R)[0], RR_interval(R)[1])
ax2.set_xlabel('czas [s]')
ax2.set_ylabel('Odległość R-R [ms]')
ax2.set_xlim([0, RR_interval(R)[0][-1]+0.5])
ax2.set_ylim([400, 1600])
ax2.plot(RR_interval(R)[0], [600]*len(RR_interval(R)[0]), '-r')
ax2.plot(RR_interval(R)[0], [1200]*len(RR_interval(R)[0]), '-r')

ax3.scatter(PP_interval(P)[0], PP_interval(P)[1])
ax3.set_xlabel('czas [s]')
ax3.set_ylabel('Odległość P-P [ms]')
ax3.set_xlim([0, PP_interval(P)[0][-1]+0.5])
ax3.set_ylim([400, 1600])
ax3.plot(PP_interval(R)[0], [600]*len(PP_interval(R)[0]), '-r')
ax3.plot(PP_interval(R)[0], [1200]*len(RR_interval(R)[0]), '-r')
plt.show()


# wykresy: P, QRS, T
fig2, (ax1, ax2, ax3) = plt.subplots(3,1)
fig2.subplots_adjust(hspace=0.5)
ax1.scatter(P_wave(P)[0], P_wave(P)[1])
ax1.set_xlabel('czas [s]')
ax1.set_ylabel('długość P [ms]')
ax1.set_xlim([0, P_wave(P)[0][-1]+0.5])
ax1.set_ylim([0, 140])
ax1.plot(P_wave(P)[0], [80]*len(P_wave(P)[0]), '-r')

ax2.scatter(QRS_duration(Q, S)[0], QRS_duration(Q, S)[1])
ax2.set_xlabel('czas [s]')
ax2.set_ylabel('długość QRS [ms]')
ax2.set_xlim([0, QRS_duration(Q, S)[0][-1]+0.5])
ax2.set_ylim([0, 200])
ax2.plot(QRS_duration(Q, S)[0], [80]*len(QRS_duration(Q, S)[0]), '-r')
ax2.plot(QRS_duration(Q, S)[0], [100]*len(QRS_duration(Q, S)[0]), '-r')

ax3.scatter(T_wave(T)[0], T_wave(T)[1])
ax3.set_xlabel('czas [s]')
ax3.set_ylabel('dlugość T [ms]')
ax3.set_xlim([0, T_wave(T)[0][-1]+0.5])
ax3.set_ylim([60, 300])
ax3.plot(T_wave(T)[0], [160]*len(T_wave(T)[0]), '-r')
plt.show()
