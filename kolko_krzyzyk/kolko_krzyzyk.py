import random


def narysuj_plansze(plansza):
    # plansza to lista zawierająca 10 łańcuchów, które reprezentują planszę.

    print(plansza[7] + '|' + plansza[8] + '|' + plansza[9])
    print('-+-+-')
    print(plansza[4] + '|' + plansza[5] + '|' + plansza[6])
    print('-+-+-')
    print(plansza[1] + '|' + plansza[2] + '|' + plansza[3])


def wczytaj_litere_gracza():
    # Gracz wybiera swoją literę. Funkcja zwraca listę na której pierwsza jest litera gracza a druga litera komputera.
    litera = ''
    while not (litera == 'X' or litera == 'O'):
        print('Chcesz używać zmaku X czy O?')
        litera = input().upper()

    if litera == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def kto_zaczyna():
    # Funkcja losowo wybiera gracza, który zaczyna grę.
    if random.randint(0, 1) == 0:
        return 'komputer'
    else:
        return 'gracz'


def wykonaj_ruch(plansza, litera, ruch):
    plansza[ruch] = litera


def wygrana(pl, li):
    # Funkcja znając stan planszy i literę gracza zwreaca True jeśli gracz wygrał.
    return ((pl[7] == li and pl[8] == li and pl[9] == li) or # górny wiersz
            (pl[4] == li and pl[5] == li and pl[6] == li) or # środkowy wiersz
            (pl[1] == li and pl[2] == li and pl[3] == li) or # dolny wiersz
            )