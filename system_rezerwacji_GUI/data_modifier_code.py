import json

def reset_miejsca():
    
    wszystkie_miejsca = []

    # tworzy pętle na 40 miejsc i dopisuje do kazdego slownika odpowiadajacemu rzedowi, konkretne miejsca z konkretnymi wlasciwosciami
    for i in range(40):
        # tworzy rząd VIP:
        if i <= 7:
            wszystkie_miejsca.append({
                "nr_miejsca": i + 1,
                "rzad": 1,
                "czy_wolne": True,
                "cena": 300,
                "dodatkowa_oplata": 100,
                "czy_dla_niepelnosprawnych": False,
                "czy_vip": True,
                "id_klienta": 10000
            })
        if i >= 8 and i <= 16:
            wszystkie_miejsca.append({
                "nr_miejsca": i + 1,
                "rzad": 2,
                "czy_wolne": True,
                "cena": 300,
                # "dodatkowa_oplata": 0,
                "czy_dla_niepelnosprawnych": False,
                "czy_vip": False,
                "id_klienta": 10000
            })
        if i >= 17 and i <= 23:
            wszystkie_miejsca.append({
                "nr_miejsca": i + 1,
                "rzad": 3,
                "czy_wolne": True,
                "cena": 300,
                # "dodatkowa_oplata": 0,
                "czy_dla_niepelnosprawnych": False,
                "czy_vip": False,
                "id_klienta": 10000
            })
        # tworzy rząd dla miejsc z udogodnieniami dla osób niepełnosprawnych
        if i >= 24 and i <= 31:
            wszystkie_miejsca.append({
                "nr_miejsca": i + 1,
                "rzad": 4,
                "czy_wolne": True,
                "cena": 300,
                # "dodatkowa_oplata": 0,
                "czy_dla_niepelnosprawnych": True,
                "czy_vip": False,
                "id_klienta": 10000,
                "dodatkowe_udogodnienia": {'Parking': False, 'Asystent': False}
            })
        if i >= 32 and i <= 40:
            wszystkie_miejsca.append({
                "nr_miejsca": i + 1,
                "rzad": 5,
                "czy_wolne": True,
                "cena": 300,
                # "dodatkowa_oplata": 0,
                "czy_dla_niepelnosprawnych": False,
                "czy_vip": False,
                "id_klienta": 10000
            })

    with open("miejsca.json", "w") as outfile:
        json.dump(wszystkie_miejsca, outfile, indent=3)



def reset_klienci():
    default = []
    with open("klienci.json", "w") as outfile:
        json.dump(default, outfile, indent=3)



def reset_rezerwacje():
    default = []
    with open("rezerwacje.json", "w") as outfile:
        json.dump(default, outfile, indent=3)
        

reset_klienci()
reset_miejsca()
reset_rezerwacje()