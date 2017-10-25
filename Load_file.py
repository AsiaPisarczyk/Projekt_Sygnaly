#####file_name podany jako parametr
def get_values_from_file(file_name):
    file_to_open = open(file_name)
    time = []
    resp = []
    bp = []
    ecg = []
    while(True):#iteracja po całym pliku
        line = file_to_open.readline()
        if line.__len__() == 0:#plik się skończył
            break
        if line[0].isdigit():#bierzemy pod uwagę tylko linie zaczynające się cyfrą (pierwszy el.)
            line = line.replace('\n', '', 1)#usunięcie przejścia do nowej linii
            values = line.split('\t')#utweórz listę, separatorem jest tabulator
            time.append(float(values.__getitem__(0)))#zbieram wartości czysu (pierwsza kolumna linii
            resp.append(float(values.__getitem__(1)))
            bp.append(float(values.__getitem__(2)))
            ecg.append(float(values.__getitem__(3)))
        else:
            continue
    return time, resp, bp, ecg