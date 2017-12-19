import scipy
import numpy as np


def detrendyzacja_normalizacja(input):
    output = scipy.signal.detrend(input)
    output = output / max(abs(output))
    return output


def filtracja(input, a, b):
    output = scipy.signal.lfilter(b, a, input)
    output = detrendyzacja_normalizacja(output)
    return output


def funkcja_prostokatna(input, mean):
    prostokat = []
    for i in range(len(input)):
        if input[i] > input[i] * mean:
            prostokat.append(1)
        else:
            prostokat.append(0)
    return prostokat


def znajdz_zmiany_nachylenia(prostokat_diff, Delay):
    global ind_p, ind_n
    ind_p = []
    ind_n = []
    for i in range(len(prostokat_diff)):
        if prostokat_diff[i] == 1:
            ind_p.append(i - Delay + 1)
        elif prostokat_diff[i] == -1:
            ind_n.append(i - Delay + 1)
    return ind_p, ind_n


def znajdz_zalamki(ind_p, ind_n, Time, ECG):
    ilosc_prostokatow = len(ind_n)  # ilość pełnych f. prostokątnych
    # przygotowanie miejsca w pamięci
    q = np.zeros((2, ilosc_prostokatow))
    r = np.zeros((2, ilosc_prostokatow))
    s = np.zeros((2, ilosc_prostokatow))
    for n in range(ilosc_prostokatow):
        t_temp = Time[ind_p[n]:ind_n[n]]
        s_temp = ECG[ind_p[n]:ind_n[n]]

        R_temp = max(s_temp)
        R_ind = s_temp.tolist().index(R_temp)

        Q_temp = min(s_temp[1:R_ind])  # szuka w połówce QRSa
        Q_ind = s_temp[1:R_ind].tolist().index(Q_temp)

        S_temp = min(s_temp[R_ind:-1])
        S_ind = s_temp[R_ind:-1].tolist().index(S_temp)
        S_ind = S_ind + R_ind

        q[0][n] = Time[ind_p[n] + Q_ind]
        q[1][n] = ECG[ind_p[n] + Q_ind]
        r[0][n] = Time[ind_p[n] + R_ind]
        r[1][n] = ECG[ind_p[n] + R_ind]
        s[0][n] = Time[ind_p[n] + S_ind]
        s[1][n] = ECG[ind_p[n] + S_ind]
    return q, r, s
