#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Dec 21, 2017 12:01:46 AM
import sys
from tkinter import filedialog
from Wykrywanie_pt import znajdz_p_t
from Signal_parameters import wykresy_parametrow, mean_values, oblicz_parametry
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import GUI_Projekt_Sygnaly_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    GUI_Projekt_Sygnaly_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    GUI_Projekt_Sygnaly_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    file_name = ''

    def wczytaj_plik(self):
        self.file_name = filedialog.askopenfilename()

    def wyswietl_ECG(self):
        znajdz_p_t(self.file_name, True)

    def wyswietl_wykresy_parametrow(self):
        wykresy_parametrow(self.file_name)

    def wypisz_parametry(self):
        dict = mean_values(self.file_name)
        ppValue, meanValue, RR, PP, HR, P_len, QRS_dur, T_len = oblicz_parametry(self.file_name)
        self.PPWynik.config(text = round(dict['mean_PP_interval'], 1))
        self.RRWynik.config(text = round(dict['mean_RR_interval'], 1))
        self.AmplitudaWynik.config(text = str(round(ppValue, 1)))
        self.DlugoscPWynik.config(text = round(dict['mean_P_wave'], 1))
        self.DlugoscTWynik.config(text = round(dict['mean_T_wave'], 1))
        self.Label22.config(text = round(dict['mean_QRS_duration'], 1))
        self.TetnoWynik.config(text = round(dict['mean_heart_rate'], 1))
        self.Label8.config(text = str(round(meanValue, 1)))



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font15 = "-family Calibri -size 18 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("600x393+636+332")
        top.title("New Toplevel 1")
        top.configure(background="#c0dce9")



        self.TytulGUI = Label(top)
        self.TytulGUI.place(relx=0.15, rely=0.05, height=35, width=447)
        self.TytulGUI.configure(background="#c0dce9")
        self.TytulGUI.configure(disabledforeground="#a3a3a3")
        self.TytulGUI.configure(font=font15)
        self.TytulGUI.configure(foreground="#000000")
        self.TytulGUI.configure(text='''WYZNACZANIE PARAMETROW SYGNALU EKG''')

        self.WczytajPlikButton = Button(top, command = lambda: self.wczytaj_plik())
        self.WczytajPlikButton.place(relx=0.17, rely=0.2, height=24, width=74)
        self.WczytajPlikButton.configure(activebackground="#d9d9d9")
        self.WczytajPlikButton.configure(activeforeground="#000000")
        self.WczytajPlikButton.configure(background="#d9d9d9")
        self.WczytajPlikButton.configure(disabledforeground="#a3a3a3")
        self.WczytajPlikButton.configure(foreground="#000000")
        self.WczytajPlikButton.configure(highlightbackground="#d9d9d9")
        self.WczytajPlikButton.configure(highlightcolor="black")
        self.WczytajPlikButton.configure(pady="0")
        self.WczytajPlikButton.configure(text='''Wczytaj plik''')

        self.OknoPacjent = LabelFrame(top)
        self.OknoPacjent.place(relx=0.08, rely=0.31, relheight=0.34
                , relwidth=0.28)
        self.OknoPacjent.configure(relief=GROOVE)
        self.OknoPacjent.configure(foreground="black")
        self.OknoPacjent.configure(text='''DANE PACJENTA''')
        self.OknoPacjent.configure(background="#d9d9d9")
        self.OknoPacjent.configure(width=170)

        self.Imie = Label(self.OknoPacjent)
        self.Imie.place(relx=0.06, rely=0.22, height=21, width=29)
        self.Imie.configure(background="#d9d9d9")
        self.Imie.configure(disabledforeground="#a3a3a3")
        self.Imie.configure(foreground="#000000")
        self.Imie.configure(text='''Imie''')

        self.Nazwisko = Label(self.OknoPacjent)
        self.Nazwisko.place(relx=0.06, rely=0.44, height=21, width=56)
        self.Nazwisko.configure(background="#d9d9d9")
        self.Nazwisko.configure(disabledforeground="#a3a3a3")
        self.Nazwisko.configure(foreground="#000000")
        self.Nazwisko.configure(text='''Nazwisko''')

        self.Pesel = Label(self.OknoPacjent)
        self.Pesel.place(relx=0.06, rely=0.67, height=21, width=34)
        self.Pesel.configure(background="#d9d9d9")
        self.Pesel.configure(disabledforeground="#a3a3a3")
        self.Pesel.configure(foreground="#000000")
        self.Pesel.configure(text='''Pesel''')
        self.Pesel.configure(width=34)

        self.WpiszImie = Entry(self.OknoPacjent)
        self.WpiszImie.place(relx=0.41, rely=0.22, relheight=0.15, relwidth=0.49)

        self.WpiszImie.configure(background="white")
        self.WpiszImie.configure(disabledforeground="#a3a3a3")
        self.WpiszImie.configure(font="TkFixedFont")
        self.WpiszImie.configure(foreground="#000000")
        self.WpiszImie.configure(insertbackground="black")
        self.WpiszImie.configure(width=84)

        self.WpiszNazwisko = Entry(self.OknoPacjent)
        self.WpiszNazwisko.place(relx=0.41, rely=0.44, relheight=0.15
                , relwidth=0.49)
        self.WpiszNazwisko.configure(background="white")
        self.WpiszNazwisko.configure(disabledforeground="#a3a3a3")
        self.WpiszNazwisko.configure(font="TkFixedFont")
        self.WpiszNazwisko.configure(foreground="#000000")
        self.WpiszNazwisko.configure(insertbackground="black")
        self.WpiszNazwisko.configure(width=84)

        self.WpiszPesel = Entry(self.OknoPacjent)
        self.WpiszPesel.place(relx=0.41, rely=0.67, relheight=0.15
                , relwidth=0.49)
        self.WpiszPesel.configure(background="white")
        self.WpiszPesel.configure(disabledforeground="#a3a3a3")
        self.WpiszPesel.configure(font="TkFixedFont")
        self.WpiszPesel.configure(foreground="#000000")
        self.WpiszPesel.configure(insertbackground="black")
        self.WpiszPesel.configure(width=84)

        self.WyswietlsygnalEKG = Button(top, command = lambda: self.wyswietl_ECG())
        self.WyswietlsygnalEKG.place(relx=0.12, rely=0.71, height=24, width=119)
        self.WyswietlsygnalEKG.configure(activebackground="#d9d9d9")
        self.WyswietlsygnalEKG.configure(activeforeground="#000000")
        self.WyswietlsygnalEKG.configure(background="#d9d9d9")
        self.WyswietlsygnalEKG.configure(disabledforeground="#a3a3a3")
        self.WyswietlsygnalEKG.configure(foreground="#000000")
        self.WyswietlsygnalEKG.configure(highlightbackground="#d9d9d9")
        self.WyswietlsygnalEKG.configure(highlightcolor="black")
        self.WyswietlsygnalEKG.configure(pady="0")
        self.WyswietlsygnalEKG.configure(text='''Wyswietl sygnal EKG''')

        self.ObliczParametry = Button(top, command = lambda: self.wypisz_parametry())
        self.ObliczParametry.place(relx=0.58, rely=0.2, height=24, width=101)
        self.ObliczParametry.configure(activebackground="#d9d9d9")
        self.ObliczParametry.configure(activeforeground="#000000")
        self.ObliczParametry.configure(background="#d9d9d9")
        self.ObliczParametry.configure(disabledforeground="#a3a3a3")
        self.ObliczParametry.configure(foreground="#000000")
        self.ObliczParametry.configure(highlightbackground="#d9d9d9")
        self.ObliczParametry.configure(highlightcolor="black")
        self.ObliczParametry.configure(pady="0")
        self.ObliczParametry.configure(text='''Oblicz Parametry''')

        self.OknoParametry = LabelFrame(top)
        self.OknoParametry.place(relx=0.48, rely=0.31, relheight=0.55
                , relwidth=0.43)
        self.OknoParametry.configure(relief=GROOVE)
        self.OknoParametry.configure(foreground="black")
        self.OknoParametry.configure(text='''PARAMETRY''')
        self.OknoParametry.configure(background="#d9d9d9")
        self.OknoParametry.configure(width=260)

        self.AmplitudaTytul = Label(self.OknoParametry)
        self.AmplitudaTytul.place(relx=0.12, rely=0.09, height=21, width=65)
        self.AmplitudaTytul.configure(background="#d9d9d9")
        self.AmplitudaTytul.configure(disabledforeground="#a3a3a3")
        self.AmplitudaTytul.configure(foreground="#000000")
        self.AmplitudaTytul.configure(text='''Amplituda:''')

        self.AmplitudaWynik = Label(self.OknoParametry)
        self.AmplitudaWynik.place(relx=0.62, rely=0.09, height=21, width=86)
        self.AmplitudaWynik.configure(background="#d9d9d9")
        self.AmplitudaWynik.configure(disabledforeground="#a3a3a3")
        self.AmplitudaWynik.configure(foreground="#000000")
        self.AmplitudaWynik.configure(width=86)

        self.WartoscSredniaSygnaluTytul = Label(self.OknoParametry)
        self.WartoscSredniaSygnaluTytul.place(relx=0.04, rely=0.19, height=21
                , width=134)
        self.WartoscSredniaSygnaluTytul.configure(background="#d9d9d9")
        self.WartoscSredniaSygnaluTytul.configure(disabledforeground="#a3a3a3")
        self.WartoscSredniaSygnaluTytul.configure(foreground="#000000")
        self.WartoscSredniaSygnaluTytul.configure(text='''Wartosc srednia sygnalu:''')
        self.WartoscSredniaSygnaluTytul.configure(width=134)

        self.Label8 = Label(self.OknoParametry)
        self.Label8.place(relx=0.62, rely=0.19, height=21, width=86)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(width=86)

        self.WartosciSrednieTytul = Label(self.OknoParametry)
        self.WartosciSrednieTytul.place(relx=0.38, rely=0.28, height=21
                , width=105)
        self.WartosciSrednieTytul.configure(background="#d9d9d9")
        self.WartosciSrednieTytul.configure(disabledforeground="#a3a3a3")
        self.WartosciSrednieTytul.configure(font=font10)
        self.WartosciSrednieTytul.configure(foreground="#000000")
        self.WartosciSrednieTytul.configure(text='''Wartosci srednie :''')

        self.TetnoTytul = Label(self.OknoParametry)
        self.TetnoTytul.place(relx=0.23, rely=0.37, height=21, width=40)
        self.TetnoTytul.configure(background="#d9d9d9")
        self.TetnoTytul.configure(disabledforeground="#a3a3a3")
        self.TetnoTytul.configure(foreground="#000000")
        self.TetnoTytul.configure(text='''Tetno:''')

        self.RRTytul = Label(self.OknoParametry)
        self.RRTytul.place(relx=0.23, rely=0.47, height=21, width=28)
        self.RRTytul.configure(background="#d9d9d9")
        self.RRTytul.configure(disabledforeground="#a3a3a3")
        self.RRTytul.configure(foreground="#000000")
        self.RRTytul.configure(text='''R-R:''')

        self.PPTytul = Label(self.OknoParametry)
        self.PPTytul.place(relx=0.23, rely=0.56, height=21, width=28)
        self.PPTytul.configure(background="#d9d9d9")
        self.PPTytul.configure(disabledforeground="#a3a3a3")
        self.PPTytul.configure(foreground="#000000")
        self.PPTytul.configure(text='''P-P:''')

        self.DlugoscPTytul = Label(self.OknoParametry)
        self.DlugoscPTytul.place(relx=0.19, rely=0.65, height=21, width=62)
        self.DlugoscPTytul.configure(background="#d9d9d9")
        self.DlugoscPTytul.configure(disabledforeground="#a3a3a3")
        self.DlugoscPTytul.configure(foreground="#000000")
        self.DlugoscPTytul.configure(text='''Dlugosc P:''')

        self.DlugoscTTytul = Label(self.OknoParametry)
        self.DlugoscTTytul.place(relx=0.19, rely=0.74, height=21, width=62)
        self.DlugoscTTytul.configure(background="#d9d9d9")
        self.DlugoscTTytul.configure(disabledforeground="#a3a3a3")
        self.DlugoscTTytul.configure(foreground="#000000")
        self.DlugoscTTytul.configure(text='''Dlugosc T:''')

        self.DlugoscQRStytul = Label(self.OknoParametry)
        self.DlugoscQRStytul.place(relx=0.19, rely=0.84, height=21, width=77)
        self.DlugoscQRStytul.configure(background="#d9d9d9")
        self.DlugoscQRStytul.configure(disabledforeground="#a3a3a3")
        self.DlugoscQRStytul.configure(foreground="#000000")
        self.DlugoscQRStytul.configure(text='''Dlugosc QRS:''')

        self.TetnoWynik = Label(self.OknoParametry)
        self.TetnoWynik.place(relx=0.54, rely=0.37, height=21, width=100)
        self.TetnoWynik.configure(background="#d9d9d9")
        self.TetnoWynik.configure(disabledforeground="#a3a3a3")
        self.TetnoWynik.configure(foreground="#000000")
        self.TetnoWynik.configure(width=44)

        self.RRWynik = Label(self.OknoParametry)
        self.RRWynik.place(relx=0.54, rely=0.47, height=21, width=100)
        self.RRWynik.configure(background="#d9d9d9")
        self.RRWynik.configure(disabledforeground="#a3a3a3")
        self.RRWynik.configure(foreground="#000000")

        self.PPWynik = Label(self.OknoParametry)
        self.PPWynik.place(relx=0.54, rely=0.56, height=21, width=100)
        self.PPWynik.configure(background="#d9d9d9")
        self.PPWynik.configure(disabledforeground="#a3a3a3")
        self.PPWynik.configure(foreground="#000000")
        self.PPWynik.configure(width=86)

        self.DlugoscPWynik = Label(self.OknoParametry)
        self.DlugoscPWynik.place(relx=0.54, rely=0.65, height=21, width=110)
        self.DlugoscPWynik.configure(background="#d9d9d9")
        self.DlugoscPWynik.configure(disabledforeground="#a3a3a3")
        self.DlugoscPWynik.configure(foreground="#000000")
        self.DlugoscPWynik.configure(width=86)

        self.DlugoscTWynik = Label(self.OknoParametry)
        self.DlugoscTWynik.place(relx=0.54, rely=0.74, height=21, width=110)
        self.DlugoscTWynik.configure(background="#d9d9d9")
        self.DlugoscTWynik.configure(disabledforeground="#a3a3a3")
        self.DlugoscTWynik.configure(foreground="#000000")

        self.DlugoscQRSWynik = Label(self.OknoParametry)
        self.DlugoscQRSWynik.place(relx=86.58, rely=21.84, height=21, width=6)
        self.DlugoscQRSWynik.configure(background="#d9d9d9")
        self.DlugoscQRSWynik.configure(disabledforeground="#a3a3a3")
        self.DlugoscQRSWynik.configure(foreground="#000000")

        self.Label22 = Label(self.OknoParametry)
        self.Label22.place(relx=0.54, rely=0.84, height=21, width=110)
        self.Label22.configure(background="#d9d9d9")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(width=86)

        self.WykresyParametrowButton = Button(top, command = lambda: self.wyswietl_wykresy_parametrow())
        self.WykresyParametrowButton.place(relx=0.08, rely=0.79, height=24
                , width=170)
        self.WykresyParametrowButton.configure(activebackground="#d9d9d9")
        self.WykresyParametrowButton.configure(activeforeground="#000000")
        self.WykresyParametrowButton.configure(background="#d9d9d9")
        self.WykresyParametrowButton.configure(disabledforeground="#a3a3a3")
        self.WykresyParametrowButton.configure(foreground="#000000")
        self.WykresyParametrowButton.configure(highlightbackground="#d9d9d9")
        self.WykresyParametrowButton.configure(highlightcolor="black")
        self.WykresyParametrowButton.configure(pady="0")
        self.WykresyParametrowButton.configure(text='''Wyswietl wykresy parametrow''')

        self.GenerujRaportTytul = Button(top)
        self.GenerujRaportTytul.place(relx=0.13, rely=0.87, height=24, width=100)

        self.GenerujRaportTytul.configure(activebackground="#d9d9d9")
        self.GenerujRaportTytul.configure(activeforeground="#000000")
        self.GenerujRaportTytul.configure(background="#d9d9d9")
        self.GenerujRaportTytul.configure(disabledforeground="#a3a3a3")
        self.GenerujRaportTytul.configure(foreground="#000000")
        self.GenerujRaportTytul.configure(highlightbackground="#d9d9d9")
        self.GenerujRaportTytul.configure(highlightcolor="black")
        self.GenerujRaportTytul.configure(pady="0")
        self.GenerujRaportTytul.configure(text='''Generuj RAPORT''')






if __name__ == '__main__':
    vp_start_gui()

