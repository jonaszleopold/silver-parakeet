import json
import add_functions

if __name__ == '__main__':
    print('My class_t.py script runs')


class MiejsceTeatralne:
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta):
        self.nr_miejsca = nr_miejsca
        self.rzad = rzad
        self.czy_wolne = czy_wolne
        self.cena = cena
        self.czy_dla_niepelnosprawnych = czy_dla_niepelnosprawnych
        self.czy_vip = czy_vip
        self.id_klienta = id_klienta

    def informacje(self):
        print(f'''
            {self.nr_miejsca}
            {self.rzad}
            {self.czy_wolne}
            {self.cena}
            {self.czy_dla_niepelnosprawnych}
            {self.czy_vip}
            {self.id_klienta}
        ''')


class MiejsceZwykle(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta)

class MiejsceVip(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, dodatkowa_oplata, czy_dla_niepelnosprawnych, czy_vip, id_klienta):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta)
        self.dodatkowa_oplata = 80
        self.cena = cena + self.dodatkowa_oplata

    def zamow_podwozke(self):
        podjazd = r'''
                                      _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [///] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
        
        '''
        print(podjazd)

class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta, dodatkowe_udogodnienia):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena,  czy_dla_niepelnosprawnych, czy_vip, id_klienta)
        self.dodatkowe_udogodnienia = dodatkowe_udogodnienia

    def sprawdz_udogodnienia(self):
        print(f'{self.dodatkowe_udogodnienia}')


class Klient():
    def __init__(self, id_klienta, nazwa_uzytkownika, _haslo, imie, nazwisko):
        self.id_klienta = id_klienta
        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.haslo = _haslo
        self.imie = imie
        self.nazwisko = nazwisko


class Teatr:

    #ładowanie danych:
    # ładuje pliki do zmiennych
    dane_z_pliku_klienci = open('klienci.json', 'r')
    dane_z_pliku_miejsca = open('miejsca.json', 'r')
    dane_z_pliku_rezerwacje = open('rezerwacje.json', 'r')

    # ładuje dane z plików do list
    wszyscy_klienci_z_pliku = json.load(dane_z_pliku_klienci)
    wszystkie_miejsca_z_pliku = json.load(dane_z_pliku_miejsca)
    wszystkie_rezerwacje_z_pliku = json.load(dane_z_pliku_rezerwacje)

    # tworzy zmienna ktora mówi ile jest zapisów w danym pliku - nie zamieniać na range bo jest używane do nadawania id
    liczba_klientow_w_pliku = len(wszyscy_klienci_z_pliku)
    liczba_miejsc_w_pliku = len(wszystkie_miejsca_z_pliku)
    liczba_rezerwacji_w_pliku = len(wszystkie_rezerwacje_z_pliku)

    #miejsca:
    # tworząc obiekt teatr tworze liste z obiektami klasy 'MiejsceTeatralne' i dziedziczących klas
    miejsca_w_teatrze = []
    for i in range(liczba_miejsc_w_pliku):
        if wszystkie_miejsca_z_pliku[i]['czy_vip']:
            miejsca_w_teatrze.append(MiejsceVip(**wszystkie_miejsca_z_pliku[i]))
        elif wszystkie_miejsca_z_pliku[i]['czy_dla_niepelnosprawnych']:
            miejsca_w_teatrze.append(MiejsceDlaNiepelnosprawnych(**wszystkie_miejsca_z_pliku[i]))
        elif wszystkie_miejsca_z_pliku[i]['czy_dla_niepelnosprawnych'] == False and wszystkie_miejsca_z_pliku[i]['czy_vip'] == False:
            miejsca_w_teatrze.append(MiejsceZwykle(**wszystkie_miejsca_z_pliku[i]))

    #klient:
    # tworząc obiekt teatr tworze liste z obiektami klasy 'Klient' na podstawie danych z listy stworzonej z pliku klienci
    klienci = []
    for i in range(liczba_klientow_w_pliku):
        klienci.append(Klient(**wszyscy_klienci_z_pliku[i]))
    # ustawiamy klienta jako nie zalogowanego
    czy_klient_zalogowany = False
    # id dla nowych klientow to dlugosc listy klienci.json + 1
    id_nowy_klient = liczba_klientow_w_pliku
    # id dla nowych rezerwacji podobnie jak wyżej
    id_nowa_rezerwacja = liczba_rezerwacji_w_pliku

    #metody:

    def __init__(self):
        self.zalogowany_klient = None

    def pokaz_wolne(self):
        for i in range(self.liczba_miejsc_w_pliku):
            if self.miejsca_w_teatrze[i].czy_wolne:
                self.miejsca_w_teatrze[i].informacje()


    def zaloguj(self, nazwa_uzytkownika, _haslo):
        # sprawdzam czy klient jest zalogowany:
        if self.czy_klient_zalogowany:
            komunikat_juz_zalogowany = 'Już zalogowany!'
            print(komunikat_juz_zalogowany)
            return komunikat_juz_zalogowany
        # jesli nie jest to odpalam loopa zeby znalezc klienta w liscie obiektow (klientow)
        else:
            for i in range(self.liczba_klientow_w_pliku):
                print(nazwa_uzytkownika, self.klienci[i].nazwa_uzytkownika, _haslo, self.klienci[i].haslo)
                if nazwa_uzytkownika == self.klienci[i].nazwa_uzytkownika and _haslo == self.klienci[i].haslo:
                    # updejtuje obiekt zalogowanego klienta
                    self.zalogowany_klient = Klient(self.klienci[i].id_klienta, self.klienci[i].nazwa_uzytkownika, self.klienci[i].haslo, self.klienci[i].imie, self.klienci[i].nazwisko)
                    self.czy_klient_zalogowany = True
                    komunikat_zalogowany = f'Klient zalogowany:\nImię: {self.zalogowany_klient.imie}\nNazwa użytkownika: {self.zalogowany_klient.nazwa_uzytkownika}\n'
                    print(komunikat_zalogowany)
                    return 0

    def rejestruj(self, stworz_nazwa_uzytkownika, stworz_haslo, imie, nazwisko):
        if self.czy_klient_zalogowany:
            komunikat_juz_zalogowany = 'Już zalogowany (REJESTRACJA!'
            print(komunikat_juz_zalogowany)
            return komunikat_juz_zalogowany
        else:
            for i in range(self.liczba_klientow_w_pliku):
                if stworz_nazwa_uzytkownika == self.klienci[i].nazwa_uzytkownika:
                    komunikat_nazwa_uzytkownika_zajeta = 'Nazwa uzytkownika zajeta (REJESTRACJA!'
                    print(komunikat_nazwa_uzytkownika_zajeta)
                    return komunikat_nazwa_uzytkownika_zajeta
            if not self.czy_klient_zalogowany:
                # tworzy zalogowanego klienta i dodaje go do listy obiektów klienci. Zmienia też status logowania na True
                self.zalogowany_klient = Klient(self.id_nowy_klient, stworz_nazwa_uzytkownika, stworz_haslo, imie, nazwisko)
                self.czy_klient_zalogowany = True
                self.klienci.append(self.zalogowany_klient)
                # tworzy dict object klienta
                dict_nowy_klient = {
                    "id_klienta": self.id_nowy_klient,
                    "nazwa_uzytkownika": stworz_nazwa_uzytkownika,
                    "_haslo": stworz_haslo,
                    "imie": imie,
                    "nazwisko": nazwisko
                }

                # dodaje dict klienta do listy wszystkich klientów i zapisuje klientów wraz z nowym klientem:
                with open('klienci.json', 'w', encoding='UTF8') as outfile_klienci:
                    self.wszyscy_klienci_z_pliku.append(dict_nowy_klient)
                    outfile_klienci.write(json.dumps(self.wszyscy_klienci_z_pliku, indent=3))

                komunikat_klient_zarejestrowany = 'Klient zarejestrowany!'
                print(komunikat_klient_zarejestrowany)
                return komunikat_klient_zarejestrowany
            else:
                komunikat_blad_rejestracja = 'Coś poszło nie tak (REJESTRACJA)'
                print(komunikat_blad_rejestracja)
                return komunikat_blad_rejestracja

    def rezerwacja(self, nr_wpisany_miejsca):
        czas_rejestracji = add_functions.get_date_and_time()
        if self.czy_klient_zalogowany:
            # sprawdza czy nr miejsce jest wolny
            if self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_wolne: # trzeba odjąć ze względu na elementy zaczynajace się od indeksu 0 do 39
                # tworzy dict object rezerwacji
                dict_nowa_rezerwacja = {
                        "nr_rezerwacji": self.id_nowa_rezerwacja,
                        "nr_miejsca": nr_wpisany_miejsca,
                        "id_klienta": self.zalogowany_klient.id_klienta,
                        "data_rezerwacji": czas_rejestracji,
                        "czy_anulowana": False,
                        "data_anulacji": ""
                }

                # dodaje dict rezerwacji do listy listy wszystkich_rezerwacji i zapisuje go do pliku:
                with open('rezerwacje.json', 'w', encoding='UTF8') as outfile_rezerwacje:
                    self.wszystkie_rezerwacje_z_pliku.append(dict_nowa_rezerwacja)
                    outfile_rezerwacje.write(json.dumps(self.wszystkie_rezerwacje_z_pliku, indent=3, default=str))

                # zaznacza, że miejsce nie jest wolne w pliku miejsca.json - teatr musi być reloadowany ponieważ zaciąga pliki w momencie tworzenia???
                with open('miejsca.json', 'w', encoding='UTF8') as outfile_miejsca:
                    self.wszystkie_miejsca_z_pliku[nr_wpisany_miejsca - 1]['czy_wolne'] = False
                    self.wszystkie_miejsca_z_pliku[nr_wpisany_miejsca - 1]['id_klienta'] = self.zalogowany_klient.id_klienta
                    outfile_miejsca.write(json.dumps(self.wszystkie_miejsca_z_pliku, indent=3, default=str))

                self.id_nowa_rezerwacja += 1 # zeby tworzyc wiele rezerwacji na raz i nadawać im odpowiednie id
                self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_wolne = False
                komunikat_miejsce_zarezerwowane = 'Miejsce zarezerwowane!'
                print(komunikat_miejsce_zarezerwowane)
                return 0
            else:
                komunikat_miejsce_zajete = 'Miejsce zajete!'
                print(komunikat_miejsce_zajete)
                return 20
        else:
            komunikat_nie_zalogowany = 'Użytkownik nie zalogowany z ID (REZERWACJA)'
            print(komunikat_nie_zalogowany)
            return komunikat_nie_zalogowany

    def pokaz_rezerwacje(self):
        if self.czy_klient_zalogowany:
            rezerwacje = []
            for i in range(self.liczba_rezerwacji_w_pliku):
                try:
                    if self.wszystkie_rezerwacje_z_pliku[i]['id_klienta'] == self.zalogowany_klient.id_klienta:
                        rezerwacja = {
                            "nr_rezerwacji": self.wszystkie_rezerwacje_z_pliku[i]["nr_rezerwacji"],
                            "nr_miejsca": self.wszystkie_rezerwacje_z_pliku[i]["nr_miejsca"],
                            "id_klienta": self.wszystkie_rezerwacje_z_pliku[i]["id_klienta"],
                            "data_rezerwacji": self.wszystkie_rezerwacje_z_pliku[i]["data_rezerwacji"],
                            "czy_anulowana": self.wszystkie_rezerwacje_z_pliku[i]["czy_anulowana"],
                            "data_anulacji": self.wszystkie_rezerwacje_z_pliku[i]["data_anulacji"]
                                      }
                        rezerwacje.append(rezerwacja)
                except:
                    print('Brak Rezerwacji!')
            print(rezerwacje)
            return rezerwacje
        else:
            komunikat_nie_zalogowany = 'Użytkownik nie zalogowany z ID (POKAZ REZERWACJE)'
            print(komunikat_nie_zalogowany)
            return komunikat_nie_zalogowany


    def anuluj_rezerwacje(self, numer_rezerwacji_do_anulowania):
        czas_anulacji = add_functions.get_date_and_time()
        if self.czy_klient_zalogowany:
            # porównuje id obiektu klienta z id klienta w liscie z numerami rezerwacji, jesli sie zgadza to nadpisuje element 'czy_anulowane'
            try:
                for i in range(self.liczba_rezerwacji_w_pliku):
                    wskazana_rezerwacja_klienta = self.wszystkie_rezerwacje_z_pliku[i]
                    print(wskazana_rezerwacja_klienta)
                    if self.zalogowany_klient.id_klienta == wskazana_rezerwacja_klienta['id_klienta'] and numer_rezerwacji_do_anulowania == wskazana_rezerwacja_klienta['nr_rezerwacji']:
                        wskazana_rezerwacja_klienta['czy_anulowana'] = True
                        wskazana_rezerwacja_klienta['data_anulacji'] = czas_anulacji

                        with open('rezerwacje.json', 'w', encoding='UTF8') as outfile_rezerwacje:
                            outfile_rezerwacje.write(json.dumps(self.wszystkie_rezerwacje_z_pliku, indent=3, default=str))

                        with open('miejsca.json', 'w', encoding='UTF8') as outfile_miejsca:

                            miejsce_do_zmiany = self.wszystkie_miejsca_z_pliku[wskazana_rezerwacja_klienta['nr_miejsca'] - 1]
                            miejsce_do_zmiany['czy_wolne'] = True
                            miejsce_do_zmiany['id_klienta'] = 0
                            outfile_miejsca.write(json.dumps(self.wszystkie_miejsca_z_pliku, indent=3, default=str))

                        komunikat_anulowano_rezerwacje = 'Rezerwacja anulowana!'
                        print(komunikat_anulowano_rezerwacje)
                        return 0
            except:
                komunikat_bledny_nr_rezerwacji = 'Bledny numer rezerwacji!'
                print(komunikat_bledny_nr_rezerwacji)
                return 31
        else:
            komunikat_nie_zalogowany = 'Użytkownik nie zalogowany z ID (ANULACJA)'
            print(komunikat_nie_zalogowany)
            return komunikat_nie_zalogowany