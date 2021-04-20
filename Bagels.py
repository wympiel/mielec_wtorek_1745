import random

ILE_CYFR = 3
ILE_PROB = 10

def uzyskaj_tajna_liczbe():
    # Funkcja zwraca łańcóch niepowtarzajacych sie losowych cyfr
    # o długosci stalej ILE_CYFR
    liczby = list(range(10))
    random.shuffle(liczby)
    tajna_liczba = ''
    for i in range(ILE_CYFR):
        tajna_liczba += str(liczby[i])
    return tajna_liczba

def uzyskaj_podpowiedzi(strzał, tajna_liczba):
    # Funkcja zwraca lancuch z wyswietlanymi uzytkownikami podpowiedziami
    #Fermi, Pico i Bagls.
    if strzał == tajna_liczba:
        return 'Zgadza sie'
    podpowiedzi = []
    for i in range(len(strzał)):
        if strzał [i] == tajna_liczba[i]:
            podpowiedzi.append('Fermi')
        elif strzał[i] in tajna_liczba:
            podpowiedzi.append('Pico')
    if len(podpowiedzi) == 0:
        return 'Bagles'
    podpowiedzi.sort()
    return ''.join(podpowiedzi)

def zawiera_tylko_cyfry(licz):
    #Funkcja zwraca True, jesli wartosc miennej licz jest łańcóch
    #składajacy sietylko z cyfr. W przeciwnym razie zawraca False.
    if licz == '' :
        return False
    for i in licz:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('Myślę o %s-cyfrowej liczbie. Spróbuj ją odgadnąć.' % (ILE_CYFR))
print('Moje podpowiedzi to...')
print('Gdy mówię:     To oznacza:')
print('Bagels         Żadna z cyfr nie jest prawidłowa.')
print('Pico           Jedna z cyfr jest prawidłowa ale nie jest na swoim miejscu.')
print('Fermi          Jedna z cyfr jest prawidłowa i jest na swoim miejscu.')

while True:
    tajna_liczba = uzyskaj_tajna_liczbe()
    print('Wybrałem liczbę. Masz %s prób, aby ją odgadnąć.' % (ILE_PROB))

    wykonane_proby = 1
    while wykonane_proby <= ILE_PROB:
        strzał = ''
        while len(strzał) != ILE_CYFR or not zawiera_tylko_cyfry(strzał):
            print('Próba #%s: ' % (wykonane_proby))
            strzał = input()

        print(uzyskaj_podpowiedzi(strzał, tajna_liczba))
        wykonane_proby += 1

        if strzał == tajna_liczba:
            break
        if wykonane_proby > ILE_PROB:
            print('Nie masz już więcej prób. Odpowiedź prawidłowa to %s' % (tajna_liczba))

    print('Chcesz zagrać ponownie? (tak lub nie)')
    if not input().lower().startswith('t'):
        break
