import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
from Load_file import get_values_from_file
from Signal_processing import detrendyzacja_normalizacja, filtracja, funkcja_prostokatna, znajdz_zmiany_nachylenia, znajdz_zalamki

def stworz_wykres(nazwa_pliku):

    # wczytanie danych
    [Time, Resp, BPL, ECG] = get_values_from_file(nazwa_pliku)

    fs = 200
    t_temp = np.linspace(Time[0], Time[-1], fs * Time[-1])

    ECG = np.interp(t_temp, Time, ECG)
    Time = t_temp

    p1 = plt.plot(t_temp, ECG, '-')
    # plt.xlim([0,2])
    #plt.show()

    # KROK 1 - detrendyzacja i normalizacja
    ECG_norm = detrendyzacja_normalizacja(ECG)

    # KROK 2 - filtr dolnoprzepustowy
    b = [1, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 1]
    a = [1, -2, 1]
    ECG_lp_filter = filtracja(ECG_norm, a, b)

    # KROK 3 - filtr górnoprzepustowy
    b = [-1 / 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 / 32]
    a = [1, -1]
    ECG_hp_filter = filtracja(ECG_lp_filter, a, b)

    # KROK 4 - filtr różniczkujący
    b = [2 / 8, 1 / 8, 0, -1 / 8, -2 / 8]
    a = [1]
    ECG_diff_filter = filtracja(ECG_hp_filter, a, b)

    # Podniesienie do kwadratu
    ECG_diff_filter_squared = ECG_diff_filter ** 2

    # całkowanie
    b = [1 / 31] * 31
    a = [1]
    ECG_integral_filter = filtracja(ECG_diff_filter_squared, a, b)

    # średnia
    ECG_mean = np.mean(ECG_integral_filter)

    prostokat = funkcja_prostokatna(ECG_integral_filter, ECG_mean)

    delay = 35  # 5+15+1+14

    # DETEKCJA QRS
    # pochodna prostokata
    prostokat_diff = np.diff(prostokat)

    ind_p, ind_n = znajdz_zmiany_nachylenia(prostokat_diff, delay)

    q, r, s, ind_q, ind_r, ind_s = znajdz_zalamki(ind_p, ind_n, Time, ECG)
    ind_r = r[0]

    return ind_p, ind_n, Time, ECG, q, r, s, ind_q, ind_r, ind_s