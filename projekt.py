import random

#-------------------------
kolor = ["żółty","pomarańczowy","Niebieski","Czerwony","Biały","Szary"]
# ------------------------
print("1 IMPOSTOR AMONG US!")

print("-" * 50)

mój_kolor = random.randint(1, 6)
kolor = ["żółty","pomarańczowy","Niebieski","Czerwony","Biały","Szary"]
if mój_kolor == 1:
    print("Twój kolor to żółty")
elif mój_kolor == 2:
    print("Twój kolor to niebieski")
elif mój_kolor == 3:
    print("Twój kolor to czerwony")
elif mój_kolor == 4:
    print("Twój kolor to biały")
elif mój_kolor == 5:
    print("Twój kolor to pomarańczowy")
elif mój_kolor == 6:
    print("Twój kolor to szary")

# ------------------------

impostor = random.randint(1, 6)
if impostor == mój_kolor:
    print("Jesteś impostorem (SUS)")
else:
    print("Jesteś crewmatem (not SUS)")

print("-" * 50)

# ------------------------------

if mój_kolor == impostor:
    task_faked = input("Wpisz tf: ").lower()
    print("Gratulacje nic nie zrobiłeś :)")

# ------------------------------

def task_1():    
    if mój_kolor == impostor:
        print("Jesteś impostorem, nie możesz wykonać tego zadania.")
    else:
        task_1_losowanie = random.randint(1, 3)
        print("TASK")

        while True:
            wybierz_liczbe = int(input("Wybierz liczbę od 1-3: "))

            if task_1_losowanie == wybierz_liczbe:
                print("TASK COMPLETED!!")
                break
            else:
                print("TASK FAILED :(")


# -----------------------------

def voting():
    global kolor
    print("VOTING TIME")

    suma_zulty = 0
    suma_niebieski = 0
    suma_czerwony = 0
    suma_bialy = 0
    suma_pomaranczowy = 0
    suma_szary = 0
    skip = 0

    print(f'Dostępne kolory graczy: {kolor}')
    Muj_glos = int(input("Na kogo głosujesz? (1 - żółty, 2 - niebieski, 3 - czerwony, 4 - biały, 5 - pomarańczowy, 6 - szary, 7 - skip): "))

    print("-" * 50)

    for i in range(5): 
        liczba_vote = random.randint(1, 7)

        if liczba_vote == 1:
            suma_zulty += 1
        elif liczba_vote == 2:
            suma_niebieski += 1
        elif liczba_vote == 3:
            suma_czerwony += 1
        elif liczba_vote == 4:
            suma_bialy += 1
        elif liczba_vote == 5:
            suma_pomaranczowy += 1
        elif liczba_vote == 6:
            suma_szary += 1
        elif liczba_vote == 7:
            skip += 1

    # --------------------------- 
    if Muj_glos == 1:
        suma_zulty += 1
    elif Muj_glos == 2:
        suma_niebieski += 1
    elif Muj_glos == 3:
        suma_czerwony += 1
    elif Muj_glos == 4:
        suma_bialy += 1
    elif Muj_glos == 5:
        suma_pomaranczowy += 1
    elif Muj_glos == 6:
        suma_szary += 1
    elif Muj_glos == 7:
        skip += 1

    print(f'Żółty otrzymał {suma_zulty} głosów(ów)')
    print(f'Niebieski otrzymał {suma_niebieski} głosów(ów)')
    print(f'Czerwony otrzymał {suma_czerwony} głosów(ów)')
    print(f'Biały otrzymał {suma_bialy} głosów(ów)')
    print(f'Pomarańczowy otrzymał {suma_pomaranczowy} głos(ów)')
    print(f'Szary otrzymał {suma_szary} głosy(ów)')
    print(f'Osoby które wstrzymały się od głosowania (skip): {skip}')

    max_glosow = max(suma_zulty, suma_niebieski, suma_czerwony, suma_bialy, suma_pomaranczowy, suma_szary, skip)

    print("-" * 50)

    sprawdzienie_glosow = []

    if max_glosow == suma_zulty:
        sprawdzienie_glosow.append("Żółty")
    
    elif max_glosow == suma_niebieski:
        sprawdzienie_glosow.append("Niebieski")
    
    elif max_glosow == suma_czerwony:
        sprawdzienie_glosow.append("Czerwony")
    
    elif max_glosow == suma_bialy:
        sprawdzienie_glosow.append("Biały")
    
    elif max_glosow == suma_pomaranczowy:
        sprawdzienie_glosow.append("Pomarańczowy")
    
    elif max_glosow == suma_szary:
        sprawdzienie_glosow.append("Szary")
    
    elif max_glosow == skip:
        print("No one was ejected (skipped)")
    
    elif len(sprawdzienie_glosow) == 1:
        print(f'{sprawdzienie_glosow[0]} was ejected.')
        kolor.remove(sprawdzienie_glosow[0])
    
    elif len(sprawdzienie_glosow) > 1:
        print("No one was ejected (Tie).")

    # ------------------------

    if max_glosow == skip:
        print(f'Pozostali {kolor}')
    else:
        ejected_color = max(
            {'żółty': suma_zulty, 'niebieski': suma_niebieski, 'czerwony': suma_czerwony, 'bialy': suma_bialy, 'pomarańczowy': suma_pomaranczowy, 'szary': suma_szary},
            key=lambda k: {'żółty': suma_zulty, 'niebieski': suma_niebieski, 'czerwony': suma_czerwony, 'bialy': suma_bialy, 'pomarańczowy': suma_pomaranczowy, 'szary': suma_szary}[k]
        )
        kolor.remove(ejected_color)
        print(f'Pozostało {kolor} graczy!!')

def task_2():
    print("TASK")
    if mój_kolor == impostor:
        print("Jestes impostorem nie mozesz przeciez wykonywac zadan")
    else:
        losowanie_zad = random.randint(1, 3)

        while True:
            if losowanie_zad == 1:
                print("Brawo, wylosowałeś zadanie proste: ile to 2 + 2 * 2 = ...")
                odp = int(input("Odpowiedz: ..."))
                if odp == 6:
                    print('Brawo, zadanie rozwiązane!! (TASK COMPLETED)')
                    break
                else:
                    print("Zle naprawdę?? Spróbuj jeszcze raz (TASK FAILED)")

            elif losowanie_zad == 2:
                print("Brawo, wylosowałeś zadanie średnie: ile to 10 * 10 - 23 + 12 - 1 = ...")
                odp = int(input("Odpowiedz: ..."))
                if odp == 88:
                    print('Brawo, zadanie rozwiązane!! (TASK COMPLETED)')
                    break
                else:
                    print("Zle ?? Spróbuj jeszcze raz (TASK FAILED)")

            elif losowanie_zad == 3:
                print("Brawo, wylosowałeś zadanie trudne: (podaj zaokrąglenie liczby pi do 5 miejsc po przecinku) = ...")
                odp = float(input("Odpowiedz: 3, ..."))
                if odp == 14159:
                    print('Brawo, zadanie rozwiązane!! (TASK COMPLETED)')
                    break
                else:
                    print("Zle ale było dobrze :) Spróbuj jeszcze raz (TASK FAILED)")

def task_3():
    if mój_kolor == impostor:
        print("Nie robisz zadania po raz kolejny :)")
    else:
        print('TASK')
        print("ZAGADKI :)")
        
        losowanie_zagadki = random.randint(1, 2)

        while True:
            if losowanie_zagadki == 1:
                print("Zadanie proste:")
                print('CO NIE JE NIE PIJE ALE CHODZI I ŻYJE? ...')
                odpowiedz = input("Odpowiedz: ").lower()
                if odpowiedz == "zegar":
                    print("Brawo, myślenie kreatywne (TASK COMPLETED)")
                    break
                else:
                    print("Nie tym razem, dawaj jeszcze raz.")

            elif losowanie_zagadki == 2:
                print("Zadanie średnie:")
                print("Co to jest, ma klucze, ale nie otwiera żadnych drzwi?")
                odpowiedz_2 = input("Odpowiedz: ").lower()
                if odpowiedz_2 == "klawiatura":
                    print("Brawo, myślenie kreatywne (TASK COMPLETED)")
                    break
                else:
                    print("Nie tym razem, dawaj jeszcze raz.")