from Signal_parameters import oblicz_parametry, mean_values

def zapisz_do_pliku(imie, nazwisko, pesel, nazwa_pliku):
    ppValue, meanValue, RR, PP, HR, P_len, QRS_dur, T_len = oblicz_parametry(nazwa_pliku)
    mean_val = mean_values(nazwa_pliku)
    tytul = nazwisko + '_' + imie + '_' + 'raport_EKG' + '.txt'
    plik = open(tytul, 'w+')
    plik.writelines(['RAPORT z badania EKG \n \n', nazwisko, ' ', imie, '\n', 'Numer PESEL: ', pesel, '\n \n'])
    plik.writelines(['Wartości średnie parametrów: \n'])

    nazwy_parametrow = ['odcinek R-R', 'odcinek P-P', 'tętno (HR)', 'szerokość P', 'szerokość QRS', 'szerokość T']
    j = 0
    for klucz in mean_val:
        if klucz == 'mean_heart_rate':
            plik.writelines([nazwy_parametrow[j], '\t'])
            plik.writelines(['%.1f' % (mean_val[klucz]),'\t',  'bmp', '\n'])
        else:
            plik.writelines([nazwy_parametrow[j], '\t'])
            plik.writelines(['%.1f' % (mean_val[klucz]), '\t', ' ms', '\n'])
        j = j + 1

    plik.writelines(['\n \n', 'Wartości parametrów w czasie: \n'])
    plik.writelines(['czas[s]', '\t', 'R-R [ms]', '\t','czas[s]', '\t',  'P-P [ms]', '\t','czas[s]', '\t',
                     'tętno [bmp]', '\t''czas[s]', '\t',
                     'szer. P [ms]', '\t','czas[s]', '\t',  'szer. QRS [ms]', '\t','czas[s]', '\t',  'szer. T [ms] \n'])

    for i in range(len(P_len[0])-1):
        plik.writelines(['%.1f' % (RR[0][i]), '\t', '%.1f' % (RR[1][i]), '\t \t',
                         '%.1f' % (PP[0][i]), '\t', '%.1f' % (PP[1][i]), '\t \t',
                         '%.1f' % (HR[0][i]), '\t', '%.1f' % (HR[1][i]), '\t \t',
                         '%.1f' % (P_len[0][i]), '\t', '%.1f' % (P_len[1][i]), '\t \t',
                         '%.1f' % (QRS_dur[0][i]), '\t', '%.1f' % (QRS_dur[1][i]), '\t \t',
                         '%.1f' % (T_len[0][i]), '\t', '%.1f' % (T_len[1][i]), '\n'])


zapisz_do_pliku('Jan', 'Kowalski', '9555555', 'RI_F_03_02.txt')
