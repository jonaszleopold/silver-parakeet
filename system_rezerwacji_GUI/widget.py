from tkinter import *
from PIL import ImageTk, Image # install pillow
import class_t, add_functions, data_modifier_code

if __name__ == '__main__':
    print('My main_widget.py script runs')

# functions for use in button creation
def podwozka():
    window_podwozka = Toplevel()
    window_podwozka.title('Zarejestruj')
    window_podwozka.geometry('900x500')
    window_podwozka.resizable(width=False, height=False)
    window_podwozka.config(bg=kolor_frame)
    Label(window_podwozka, bg=kolor_frame, font='Consolas', pady=150, text=r'''
                                      _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [///] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
        
        ''').pack()

def show_password(entry_name):
    if entry_name.cget('show') == '*':
        entry_name.config(show='')
    else:
        entry_name.config(show='*')
# wykorzystywany do komunikatów jako alternatywa dla messagebox
def komunikat(info):
    window_komunikat = Toplevel()
    window_komunikat.title('INFO')
    window_komunikat.geometry('600x300')
    window_komunikat.resizable(width=False, height=False)
    window_komunikat.config(bg=kolor_frame)
    Label(window_komunikat, bg=kolor_frame, font=('Small Fonts', 15), text=f'{info}').pack(fill='both', expand=True)
    Button(window_komunikat,
           command=lambda: window_komunikat.destroy(),
           background=kolor2,
           foreground=kolor4,
           activebackground=kolor5,
           activeforeground=kolor4,
           highlightthickness=2,
           highlightbackground=kolor2,
           highlightcolor='WHITE',
           width=20,
           height=2,
           relief='groove',
           cursor='hand2',
           text='OK',
           font=(font1, size_font1, 'bold')
           ).pack(fill='both')

# zarejestruj klienta (sprawdza czy pola entry są wypelnione)
def zarejestruj_klienta(window, nazwa_uzytkownika, haslo, imie, nazwisko):
    if imie == '':
        lbl_imie = Label(window, text='Wpisz imię', font=(font1, size_font1), bg=kolor_frame)
        lbl_imie.pack()
        lbl_imie.after(2000, lbl_imie.destroy)
    elif nazwisko == '':
        lbl_nazwisko = Label(window, text='Wpisz nazwisko', font=(font1, size_font1), bg=kolor_frame)
        lbl_nazwisko.pack()
        lbl_nazwisko.after(2000, lbl_nazwisko.destroy)
    elif nazwa_uzytkownika == '':
        lbl_nazwa_uzytkownika = Label(window, text='Stwórz nazwę użytkownika', font=(font1, size_font1), bg=kolor_frame)
        lbl_nazwa_uzytkownika.pack()
        lbl_nazwa_uzytkownika.after(2000, lbl_nazwa_uzytkownika.destroy)
    elif haslo == '':
        lbl_haslo = Label(window, text='Stwórz hasło', font=(font1, size_font1), bg=kolor_frame)
        lbl_haslo.pack()
        lbl_haslo.after(2000, lbl_haslo.destroy)
    else:
        teatr.rejestruj(nazwa_uzytkownika, haslo, imie, nazwisko)
        komunikat(f'Zarejestrowano nowego użytkownika.\n Witaj {nazwa_uzytkownika}!')
        window.destroy()

def zaloguj_klienta(window, nazwa_uzytkownika, haslo):
    if nazwa_uzytkownika == '':
        lbl_nazwa_uzytkownika = Label(window, text='Wpisz nazwę użytkownika', font=(font1, size_font1), bg=kolor_frame)
        lbl_nazwa_uzytkownika.pack()
        lbl_nazwa_uzytkownika.after(2000, lbl_nazwa_uzytkownika.destroy)
    elif haslo == '':
        lbl_haslo = Label(window, text='Wpisz hasło', font=(font1, size_font1), bg=kolor_frame)
        lbl_haslo.pack()
        lbl_haslo.after(2000, lbl_haslo.destroy)
    else:
        if teatr.zaloguj(nazwa_uzytkownika, haslo) == 0:
            komunikat(f'Zalogowano!.\n Witaj ponownie {nazwa_uzytkownika}!')
            window.destroy()
        else:
            komunikat(f'Błędna nazwa użytkownika lub hasło')


# window zarejestruj - tworzy okno rejestracji klienta
def okno_zarejestruj():
    if teatr.czy_klient_zalogowany:
        komunikat_juz_zalogowany = f'Jesteś zalogowany jako {teatr.zalogowany_klient.nazwa_uzytkownika}!'
        komunikat(komunikat_juz_zalogowany)
    else:
        window_zarejestruj = Toplevel()
        window_zarejestruj.title('Zarejestruj')
        window_zarejestruj.geometry('300x320')
        window_zarejestruj.resizable(width=False, height=False)
        window_zarejestruj.config(bg=kolor_frame)

        # name input
        Label(window_zarejestruj, text='Imię:', font=(font1, size_font1), bg=kolor_frame).pack()
        imie = StringVar()
        ent_imie = Entry(window_zarejestruj, textvariable=imie)
        ent_imie.config(border=2, font=(font1, size_font1), justify='center', width=20)
        ent_imie.pack()

        # validating the input
        reg_imie = window_zarejestruj.register(add_functions.validate_name_surname)
        ent_imie.config(validate="key", validatecommand=(reg_imie, '%P'))

        # surname input
        Label(window_zarejestruj, text='Nazwisko:', font=(font1, size_font1), bg=kolor_frame).pack()
        nazwisko = StringVar()
        ent_nazwisko = Entry(window_zarejestruj, textvariable=nazwisko)
        ent_nazwisko.config(border=2, font=(font1, size_font1), justify='center', width=20)
        ent_nazwisko.pack()

        # validating the input
        reg_nazwisko = window_zarejestruj.register(add_functions.validate_name_surname)
        ent_nazwisko.config(validate="key", validatecommand=(reg_nazwisko, '%P'))

        # username input:
        Label(window_zarejestruj, text='Nazwa użytkownika:', font=(font1, size_font1), bg=kolor_frame).pack()
        nazwa_uzytkownika = StringVar()
        ent_nazwa_uzytkownika = Entry(window_zarejestruj, textvariable=nazwa_uzytkownika)
        ent_nazwa_uzytkownika.config(border=2, font=(font1, size_font1), justify='center', width=20)
        ent_nazwa_uzytkownika.pack()

        # validating the input
        reg_nazwa_uzytkownika = window_zarejestruj.register(add_functions.validate_username)
        ent_nazwa_uzytkownika.config(validate="key", validatecommand=(reg_nazwa_uzytkownika, '%P'))

        # password input:
        Label(window_zarejestruj, text='Hasło:', font=(font1, size_font1), bg=kolor_frame).pack()
        haslo = StringVar()
        ent_haslo = Entry(window_zarejestruj,show='*', textvariable=haslo)
        ent_haslo.config(border=2, font=(font1, size_font1), justify='center', width=20)
        ent_haslo.pack()

        # validating the input
        reg_haslo = window_zarejestruj.register(add_functions.validate_password)
        ent_haslo.config(validate="key", validatecommand=(reg_haslo, '%P'))

        # checkbutton for showpassword
        check_button = Checkbutton(window_zarejestruj, command=lambda: show_password(ent_haslo), text='show password', font=(font1, 10), bg=kolor_frame, activebackground=kolor_frame)
        check_button.pack()

        # button REJESTRUJ
        Button(window_zarejestruj,
               command=lambda: zarejestruj_klienta(window_zarejestruj, ent_nazwa_uzytkownika.get(), ent_haslo.get(), ent_imie.get(), ent_nazwisko.get()),
                 background=kolor2,
                 foreground=kolor4,
                 activebackground=kolor5,
                 activeforeground=kolor4,
                 highlightthickness=2,
                 highlightbackground=kolor2,
                 highlightcolor='WHITE',
                 width=20,
                 height=2,
                 relief='groove',
                 cursor='hand2',
                 text='REJESTRUJ',
                 font=(font1, size_font1, 'bold')
                 ).pack()

# window zaloguj - tworzy okno logowania klienta
def okno_zaloguj():
    if teatr.czy_klient_zalogowany:
        komunikat_juz_zalogowany = f'Jesteś zalogowany jako {teatr.zalogowany_klient.nazwa_uzytkownika}!'
        komunikat(komunikat_juz_zalogowany)
    else:
        window_zaloguj = Toplevel()
        window_zaloguj.title('Zaloguj')
        window_zaloguj.geometry('300x200')
        window_zaloguj.resizable(width=False, height=False)
        window_zaloguj.config(bg=kolor_frame)

        # username input:
        Label(window_zaloguj, text='Nazwa użytkownika:', font=(font1, size_font1), bg=kolor_frame).pack()
        nazwa_uzytkownika = StringVar()
        ent_nazwa_uzytkownika = Entry(window_zaloguj, textvariable=nazwa_uzytkownika)
        ent_nazwa_uzytkownika.config(border=2, font=(font1, size_font1), justify='center', width=15)
        ent_nazwa_uzytkownika.pack()

        # validating the input
        reg_nazwa_uzytkownika = root.register(add_functions.validate_username)
        ent_nazwa_uzytkownika.config(validate="key", validatecommand=(reg_nazwa_uzytkownika, '%P'))

        # password input:
        Label(window_zaloguj, text='Hasło:', font=(font1, size_font1), bg=kolor_frame).pack()
        haslo = StringVar()
        ent_haslo = Entry(window_zaloguj, textvariable=haslo)
        ent_haslo.config(show='*', border=2, font=(font1, size_font1), justify='center', width=15)
        ent_haslo.pack()

        # validating the input
        reg_haslo = root.register(add_functions.validate_password)
        ent_haslo.config(validate="key", validatecommand=(reg_haslo, '%P'))

        # checkbutton for showpassword
        check_button = Checkbutton(window_zaloguj, command=lambda: show_password(ent_haslo), text='show password', font=(font1, 10), bg=kolor_frame, activebackground=kolor_frame)
        check_button.pack()

        # button ZALOGUJ
        Button(window_zaloguj,
               command=lambda: zaloguj_klienta(window_zaloguj, ent_nazwa_uzytkownika.get(), ent_haslo.get()),
               background=kolor2,
               foreground=kolor4,
               activebackground=kolor5,
               activeforeground=kolor4,
               highlightthickness=2,
               highlightbackground=kolor2,
               highlightcolor='WHITE',
               width=20,
               height=2,
               relief='groove',
               cursor='hand2',
               text='ZALOGUJ',
               font=(font1, size_font1, 'bold')
               ).pack(pady=5)

def okno_info(nr_miejsca_wybrany):
    window_info = Toplevel()
    window_info.title('INFO')
    window_info.geometry('600x440')
    window_info.resizable(width=False, height=True)
    window_info.config(bg=kolor_frame)
    for i in range(teatr.liczba_miejsc_w_pliku + 1):
        if nr_miejsca_wybrany != '':
            if i == int(nr_miejsca_wybrany):
                miejsce = teatr.miejsca_w_teatrze[i]
                if miejsce.czy_wolne:
                    dostepnosc = "Wolne"
                else:
                    dostepnosc = "Zajete"
                if miejsce.czy_vip:
                    add_msg = f"Ekskluzywne miejsce VIP w pierwszym rzędzie!\n  Za to miejsce doliczana jest dodatkowa opłata w wysokości {miejsce.dodatkowa_oplata}PLN.\n  Opłata wliczona w cenę wyświetloną poniżej!"
                elif miejsce.czy_dla_niepelnosprawnych:
                    add_msg = "Miejsce z udogodnieniami dla niepełnosprawnych."
                else:
                    add_msg = "Miejsce standard."
                Label(window_info, font=(font1, size_font1), bg=kolor_frame, text=f'Numer miejsca:\n {miejsce.nr_miejsca}').pack(pady=10)
                Label(window_info, font=(font1, size_font1), bg=kolor_frame, text=f'Rząd:\n {miejsce.rzad}').pack(pady=10)
                Label(window_info, font=(font1, size_font1), bg=kolor_frame, text=f'Dostępność:\n {dostepnosc}').pack(pady=10)
                Label(window_info, font=(font1, size_font1), bg=kolor_frame, text=f'Rodzaj:\n {add_msg}').pack(pady=10)
                Label(window_info, font=(font1, size_font1), bg=kolor_frame, text=f'Cena:\n {miejsce.cena}PLN').pack(pady=10)

def okno_historia_rezerwacje():
    if teatr.czy_klient_zalogowany:
        window_historia_rezerwacji = Toplevel()
        window_historia_rezerwacji.title('Historia rezerwacji')
        window_historia_rezerwacji.geometry('300x500')
        window_historia_rezerwacji.resizable(width=False, height=True)
        window_historia_rezerwacji.config(bg=kolor_frame)

        # username input:
        Label(window_historia_rezerwacji, text='Moje rezerwacje:', font=(font1, size_font1), bg=kolor_frame).pack()
        info = teatr.pokaz_rezerwacje()
        for i in range(len(info)):
            if info[i]['czy_anulowana']:
                aktywna = 'Niektywna'
            else:
                aktywna = 'Aktywna'
            Label(window_historia_rezerwacji, text=f'Numer rezerwacji: {info[i]['nr_rezerwacji']}\nNumer miejsca: {info[i]['nr_miejsca']}\nData rezerwacji: {info[i]['data_rezerwacji']}\n{aktywna}',
                  font=(font1, size_font1), bg=kolor_frame).pack()
    else:
        komunikat_nie_zalogowany = 'Zaloguj się, aby zobaczyć historię rezerwacji.'
        komunikat(komunikat_nie_zalogowany)

def anuluj_rezerwacje(window, numer_rezerwacji):
    if teatr.czy_klient_zalogowany:
        if numer_rezerwacji == '':
            lbl_nr = Label(window, text='Wpisz numer rezerwacji', font=(font1, size_font1), bg=kolor_frame)
            lbl_nr.pack()
            lbl_nr.after(2000, lbl_nr.destroy)
        else:
            teatr.anuluj_rezerwacje(int(numer_rezerwacji))
            if teatr.anuluj_rezerwacje(int(numer_rezerwacji)) == 0:
                komunikat_rezerwacja_anulowana = 'Rezerwacja anulowana.'
                komunikat(komunikat_rezerwacja_anulowana)
            else:
                komunikat_błedny_numer = 'Błędny numer rezerwacji lub rezerwacja anulowana wcześniej.\n Sprawdź numer rezerwacji i spróbuj ponownie.'
                komunikat(komunikat_błedny_numer)

    else:
        komunikat_nie_zalogowany = 'Zaloguj się, aby anulować rezerwację.'
        komunikat(komunikat_nie_zalogowany)

def okno_rezerwacja_dla_niepelnosprawnych(numer_miejsca):
    window_miejsce_dla = Toplevel()
    window_miejsce_dla.title('Zaloguj')
    window_miejsce_dla.geometry('300x200')
    window_miejsce_dla.resizable(width=False, height=False)
    window_miejsce_dla.config(bg=kolor_frame)

    # username input:
    Label(window_miejsce_dla, text=f'Zarezerwowano miejsce {numer_miejsca}.', font=(font1, size_font1),bg=kolor_frame).pack(pady=20)
    Label(window_miejsce_dla, text='Czy potrzebne dodatkowe udogonienia?', font=(font1, size_font1), bg=kolor_frame).pack()

    # button ZALOGUJ
    Button(window_miejsce_dla,
           # command=lambda:,
           background=kolor2,
           foreground=kolor4,
           activebackground=kolor5,
           activeforeground=kolor4,
           highlightthickness=2,
           highlightbackground=kolor2,
           highlightcolor='WHITE',
           width=20,
           height=2,
           relief='groove',
           cursor='hand2',
           text='Tak',
           font=(font1, size_font1, 'bold')
           ).pack(pady=5)
    Button(window_miejsce_dla,
           # command=lambda:,
           background=kolor2,
           foreground=kolor4,
           activebackground=kolor5,
           activeforeground=kolor4,
           highlightthickness=2,
           highlightbackground=kolor2,
           highlightcolor='WHITE',
           width=20,
           height=2,
           relief='groove',
           cursor='hand2',
           text='Nie',
           font=(font1, size_font1, 'bold')
           ).pack(pady=5)

def rezerwuj(numer_miejsca):
    if teatr.czy_klient_zalogowany:
        wynik = teatr.rezerwacja(numer_miejsca)
        if wynik == 20:
            komunikat_miejsce_zajęte = f'Rezerwacja już zrobiona!'
            komunikat(komunikat_miejsce_zajęte)
        elif wynik == 0:
            if teatr.miejsca_w_teatrze[numer_miejsca].czy_dla_niepelnosprawnych:
                okno_rezerwacja_dla_niepelnosprawnych(numer_miejsca)
            else:
                komunikat_rezerwacja_zrobiona = f'Zarezerwowano miejsce {numer_miejsca}.'
                komunikat(komunikat_rezerwacja_zrobiona)
        else:
            print('Something went wrong')
    else:
        komunikat_nie_zalogowany = 'Zaloguj się, aby zrobić rezerwację.'
        komunikat(komunikat_nie_zalogowany)

# tworzy przyciski siedzeń
def tworzenie_przyciskow(liczba_miejsc, name_frame):
    column_start = 0
    column_end = column_start + 8
    row = 0
    lbl_width = 12
    lbl_height = 6
    relief_btns = RIDGE
    # info button:
    info_icon = '\u24D8'
    info_width = 2
    info_height = 1
    # rezerwuj button:
    rez_width = 8
    rez_height = 1
    rez_font_size = 8
    #other buttons
    font_size_btns = 10
    for i in range(liczba_miejsc):
        if teatr.miejsca_w_teatrze[i].czy_wolne:
            if teatr.miejsca_w_teatrze[i].czy_vip:
                Label(
                    name_frame,
                    background='#D4AF37',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=lbl_width,
                    height=lbl_height,
                    relief=relief_btns,
                    text=f'VIP {i + 1}',
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=(0, 30))
                Button(
                    name_frame,
                    command=lambda element=i: okno_info(element),
                    background='#D4AF37',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=info_width,
                    height=info_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=info_icon,
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='sw')
                Button(
                    name_frame,
                    command=lambda element=i: rezerwuj(element+1),
                    background='#D4AF37',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=rez_width,
                    height=rez_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=f'rezerwuj',
                    font=(font1, rez_font_size, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='se')
            elif teatr.miejsca_w_teatrze[i].czy_dla_niepelnosprawnych:
                Label(
                    name_frame,
                    background='#b6c8ff',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=lbl_width,
                    height=lbl_height,
                    relief=relief_btns,
                    text=f'\u267F {i + 1}',
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=(0, 30))
                Button(
                    name_frame,
                    command=lambda element=i: okno_info(element),
                    background='#b6c8ff',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=info_width,
                    height=info_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=info_icon,
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='sw')
                Button(
                    name_frame,
                    command=lambda element=i: rezerwuj(element+1),
                    background='#b6c8ff',
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=rez_width,
                    height=rez_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=f'rezerwuj',
                    font=(font1, rez_font_size, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='se')
            else:
                Label(
                    name_frame,
                    background=kolor2,
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=lbl_width,
                    height=lbl_height,
                    relief=relief_btns,
                    text=f'{i + 1}',
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=(0, 30))
                Button(
                    name_frame,
                    command=lambda element=i: okno_info(element),
                    background=kolor2,
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=info_width,
                    height=info_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=info_icon,
                    font=(font1, font_size_btns, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='sw')
                Button(
                    name_frame,
                    command=lambda element=i: rezerwuj(element+1),
                    background=kolor2,
                    foreground=kolor4,
                    activebackground=kolor5,
                    activeforeground=kolor4,
                    highlightthickness=2,
                    highlightbackground=kolor2,
                    highlightcolor='WHITE',
                    width=rez_width,
                    height=rez_height,
                    relief=relief_btns,
                    cursor='hand2',
                    text=f'rezerwuj',
                    font=(font1, rez_font_size, 'bold')
                ).grid(column=column_start, row=row, pady=3, sticky='se')
        else:
            Label(
                name_frame,
                background=kolor3,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=10,
                height=5,
                relief=relief_btns,
                text=f'Zajęte',
                font=(font1, 12)
            ).grid(column=column_start, row=row, pady=3)

        column_start += 1
        if column_start == column_end:
            column_start = 0
            row += 1

# font settings
font1 = 'Small Fonts'
font2 = 'Arial'
size_font1 = 15
size_font_seats = 15

# # colors type 1 - Sunrise
kolor1 = '#ffa3ac'
kolor2 = '#ffae97'
kolor3 = '#ffba81'
kolor4 = 'BLACK'
kolor5 = '#ffc56c'
kolor6 = 'WHITE'
kolor_frame = '#ffd156'

# colors type 2 - Pink
# kolor1 = '#f09dda'
# kolor2 = '#f09dda'
# kolor3 = '#f09dda'
# kolor4 = 'BLACK'
# kolor5 = '#f09dda'
# kolor6 = 'WHITE'
# kolor_frame = '#f09dda'

# # colors type 3 - Tsunami
# kolor1 = '#d8d9ff'
# kolor2 = '#4766ff'
# kolor3 = '#539bff'
# kolor4 = 'BLACK'
# kolor5 = '#73bcff'
# kolor6 = 'WHITE'
# kolor_frame = '#531eff'

# # colors type 4 - Whirpool
# kolor1 = '#4766ff'
# kolor2 = '#d8d9ff'
# kolor3 = '#539bff'
# kolor4 = 'BLACK'
# kolor5 = '#73bcff'
# kolor6 = 'WHITE'
# kolor_frame = '#531eff'

# instance of teatr
teatr = class_t.Teatr()

# main widget is defined:
root = Tk()
root.title('Witaj w systemie rezerwacji - Kino Life')
root.geometry('1300x910')
root.resizable(width=False, height=False)
root.config(bg=kolor_frame)

# loading images
life_ph = Image.open('../system_rezerwacji_GUI/images/life.jpg').resize((250,180)) # 1.25
life_ph = ImageTk.PhotoImage(life_ph)
welcome_ph = Image.open('../system_rezerwacji_GUI/images/welcome.jpg').resize((354,200))
welcome_ph = ImageTk.PhotoImage(welcome_ph)
cinema_ph = Image.open('../system_rezerwacji_GUI/images/cinema.jpg').resize((354,200))
cinema_ph = ImageTk.PhotoImage(cinema_ph)
grid_ph = Image.open('../system_rezerwacji_GUI/images/grid.jpg').resize((354,200))
grid_ph = ImageTk.PhotoImage(grid_ph)


# baner frame
baner_frame = Frame(root, borderwidth=5, relief=RIDGE)
baner_frame.config(bg=kolor_frame)
label1 = Label(baner_frame, text='Witaj w systemie rezerwacji\nKino Life', bg=kolor1, font=(font1, 20), justify='center')

# menu frame
menu_frame = Frame(root, width=300, height=580, bg=kolor_frame)
# menu frame - labels
lbl_lub = Label(menu_frame, text='lub', bg=kolor_frame, font=(font1, size_font1))
lbl_nr_rezerwacji = Label(menu_frame, text='Wpisz numer rezerwacji do anulowania:', bg=kolor_frame, font=(font1, 12))
# menu frame - creating input box for reservation number to delete
numer_rezerwacji_do_usuniecia = StringVar()
ent_numer_rezerwacji_do_usuniecia = Entry(menu_frame, textvariable=numer_rezerwacji_do_usuniecia)
ent_numer_rezerwacji_do_usuniecia.config(border=2, font=(font1, 30), justify='center', width=8)
# menu frame - validating the input for reservation box
reg_anuluj = menu_frame.register(add_functions.validate_id)
ent_numer_rezerwacji_do_usuniecia.config(validate="key", validatecommand=(reg_anuluj, '%P'))
# menu frame - buttons
btn_zarejestruj = Button(menu_frame,
                command=lambda: okno_zarejestruj(),
                background=kolor2,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=20,
                height=2,
                cursor='hand2',
                text='Zarejestruj się',
                font=(font1, size_font1, 'bold')
                )
btn_zaloguj = Button(menu_frame,
                command=lambda: okno_zaloguj(),
                background=kolor2,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=20,
                height=2,
                cursor='hand2',
                text='Zaloguj',
                font=(font1, size_font1, 'bold')
                )
btn_pokaz_rezerwacje = Button(menu_frame,
                command=lambda: okno_historia_rezerwacje(),
                background=kolor2,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=20,
                height=2,
                cursor='hand2',
                text='Pokaż moje rezerwacje',
                font=(font1, size_font1, 'bold')
                )
btn_anuluj_rezerwacje = Button(menu_frame,
                command=lambda: anuluj_rezerwacje(menu_frame, numer_rezerwacji_do_usuniecia.get()),
                background=kolor2,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=20,
                height=2,
                cursor='hand2',
                text='Anuluj rezerwacje',
                font=(font1, size_font1, 'bold')
                )
btn_resetuj = Button(menu_frame,
                command=lambda: [data_modifier_code.reset_rezerwacje(), data_modifier_code.reset_miejsca(), data_modifier_code.reset_klienci()],
                background=kolor2,
                foreground=kolor4,
                activebackground=kolor5,
                activeforeground=kolor4,
                highlightthickness=2,
                highlightbackground=kolor2,
                highlightcolor='WHITE',
                width=20,
                height=2,
                cursor='hand2',
                text='RESETUJ TEATR',
                font=(font1, size_font1, 'bold')
                )

# ekran frame
ekran_frame = Frame(root, height=48, bg=kolor_frame)
lbl_ekran = Label(ekran_frame, text='EKRAN', font=(font1, 20), bg=kolor4, foreground='WHITE')

# seats frame
seats_frame = Frame(root, height=700, bg=kolor_frame)

# down right frame
down_right_frame = Frame(root)
down_right_frame.config(bg=kolor_frame, borderwidth=4, relief=RIDGE)
btn_podwozka = Button(menu_frame, text='PODWÓZKA', command=lambda: podwozka(), bg=kolor1, font=(font1, size_font1))

# baner layout
lbl_life_ph = Label(baner_frame, image=life_ph)
lbl_life_ph.pack(side='left')
label1.pack(side='left', fill='both', expand=True, pady=(35,0))
lbl_life_ph2 = Label(baner_frame, image=life_ph)
lbl_life_ph2.pack(side='left')
lbl_life_ph3 = Label(baner_frame, image=life_ph)
lbl_life_ph3.pack(side='left')
lbl_life_ph4 = Label(baner_frame, image=life_ph)
lbl_life_ph4.pack(side='left')
lbl_life_ph5 = Label(baner_frame, image=life_ph)
lbl_life_ph5.pack(side='left')
lbl_life_ph7 = Label(baner_frame, image=life_ph)
lbl_life_ph7.pack(side='left')
lbl_life_ph8 = Label(baner_frame, image=life_ph)
lbl_life_ph8.pack(side='left')
lbl_life_ph9 = Label(baner_frame, image=life_ph)
lbl_life_ph9.pack(side='left')
baner_frame.pack()

# menu layout
btn_zarejestruj.pack(fill='both', expand=True)
lbl_lub.pack(fill='x', ipady=20)
btn_zaloguj.pack(fill='both', expand=True, pady=10)
btn_pokaz_rezerwacje.pack(fill='both', expand=True, pady=10)
lbl_nr_rezerwacji.pack(fill='both', expand=True, pady=10)
ent_numer_rezerwacji_do_usuniecia.pack(fill='y', expand=True, pady=10)
btn_anuluj_rezerwacje.pack(fill='both', expand=True, pady=10)
btn_podwozka.pack(fill='both', expand=True, pady=10)
btn_resetuj.pack(fill='both', expand=True, pady=10)
menu_frame.pack_propagate(False)
menu_frame.pack(side='left', padx=50, pady=85)

# ekran layout
lbl_ekran.grid(ipadx=380)
ekran_frame.pack_propagate(False)
ekran_frame.pack(pady=20, ipadx=100)

# places layout
tworzenie_przyciskow(40, seats_frame)
seats_frame.pack(ipadx=70)

# down right layout
down_right_frame.pack(fill='both')


root.mainloop()