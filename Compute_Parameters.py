def compute_parameters(ECG):
    ppValue = max(ECG) - min(ECG)#amplituda
    sum = 0
    for value in ECG:
        sum += value#suma po wszystkich wartościach( sum = sum + value)
    average = sum / ECG.__len__()
    sum = 0
    for value in ECG:
        sum += value**2#kwadrat, suma kwadratów przez liczbę elementów
    power = sum / ECG.__len__()
    return ppValue, average, power