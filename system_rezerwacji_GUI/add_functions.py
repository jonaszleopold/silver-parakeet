import datetime, tkinter
from tkinter import messagebox


if __name__ == '__main__':
    print('My add_functions.py script runs')

def get_date_and_time():
    data_czas = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    return data_czas

def validate(input):
    if len(input) == 0:
        # empty Entry is ok
        return True
    elif len(input) == 1 and input.isdigit() and int(input) != 0:
        # Entry with 1 digit which is not '0' is ok
        return True
    elif len(input) == 2 and input.isdigit() and int(input) <= 40:
        # Entry with 2 digit is ok
        return True
    else:
        # Anything else, reject it
        return False

def validate_name_surname(input):
    if len(input) == 0:
        # empty Entry is ok
        return True
    if len(input) <=20 and input.isalpha():
        return True
    else:
        # Anything else, reject it
        return False

def validate_username(input):
    if len(input) == 0:
        # empty Entry is ok
        return True
    if len(input) <=20:
        return True
    else:
        # Anything else, reject it
        return False

def validate_password(input):
    if len(input) == 0:
        # empty Entry is ok
        return True
    if len(input) <=20:
        return True
    else:
        # Anything else, reject it
        return False


def validate_id(input):
    if len(input) == 0:
        # empty Entry is ok
        return True
    elif len(input) == 1 and input.isdigit():
        # Entry with 1 digit which is not '0' is ok
        return True
    elif len(input) <= 7 and input.isdigit():
        # Entry with 2 digit is ok
        return True
    else:
        # Anything else, reject it
        return False



# DO FUNKCJI TWORZENIA MIEJSC W TEATRZE:
def stworz_slownik_VIP():
    miejsca_vip = {}
    czy_kontynuowac = 'Y'
    rekord = len(miejsca_vip)

    while czy_kontynuowac == 'Y' or czy_kontynuowac == 'y':
        miejsce_vip_input = input('Proszę, podaj numer miejsca VIP:\n')
        miejsca_vip[f'miejsce_vip_{rekord}'] = miejsce_vip_input
        rekord += 1
        czy_kontynuowac = input('Wiecej miejsc? Y/N\n')
    else:
        print(f'Dziękujemy, oto twoje miejsca VIP:\n{miejsca_vip}')

# def stworz_slownik_zwykle():
#     miejsca_zwykle = {}
#     czy_kontynuowac = 'Y'
#     rekord = len(miejsca_zwykle)
#
#     while czy_kontynuowac == 'Y' or czy_kontynuowac == 'y':
#         miejsce_zwykle_input = input('Proszę, podaj numer miejsca standardowego:\n')
#         miejsca_zwykle[f'miejsce_standard_{rekord}'] = miejsce_zwykle_input
#         rekord += 1
#         czy_kontynuowac = input('Wiecej miejsc? Y/N\n')
#     else:
#         print(f'Dziękujemy, oto twoje miejsca standard:\n{miejsca_zwykle}')
#
# def stworz_slownik_miejsca_dla_niepelnosprawnych():
#     miejsca_dla_niepelnosprawnych = {}
#     czy_kontynuowac = True
#     rekord = len(miejsca_dla_niepelnosprawnych)
#
#     while czy_kontynuowac:
#         miejsce_dla_niepelnosprawnych_input = input('Proszę, podaj numer miejsca dla_niepelnosprawnych:\n')
#         miejsca_dla_niepelnosprawnych[f'miejsce_dla_niepelnosprawnych_{rekord}'] = miejsce_dla_niepelnosprawnych_input
#         rekord += 1
#         # if jakiś_przycisk_kliknięty:
#         #     czy_kontynuowac = False
#     else:
#         print(f'Dziękujemy, oto twoje miejsca dla_niepelnosprawnych:\n{miejsca_dla_niepelnosprawnych}')
