'''
vanner_lista.py: Program för att hantera en lista med vänner

__author__  = "Anne Onym"
__version__ = "1.0.0"
__email__   = "namn.efternamn@elev.ga.ntig.se"
'''

import os

def rensa_skarm():
    os.system("cls" if os.name == "nt" else "clear")

def visa_vanner(lista):
    print("\033[96m")
    print("===== MINA VÄNNER =====")

    if len(lista) == 0:
        print("Listan är tom.")
    else:
        for index, namn in enumerate(lista, start=1):
            print(f"{index}. {namn}")

    print(f"\nAntal vänner: {len(lista)}")
    print("\033[0m")

def lagg_till_van(lista):
    namn = input("Skriv namn att lägga till: ")

    if namn == "" or namn == "/q":
        return

    if namn in lista:
        print("Namnet finns redan.")
    else:
        lista.append(namn)
        print(f"{namn} har lagts till.")

def andra_van(lista):
    visa_vanner(lista)

    if len(lista) == 0:
        return

    try:
        nummer = int(input("Vilket nummer vill du ändra? "))

        if nummer < 1 or nummer > len(lista):
            print("Ogiltigt nummer.")
            return

        nytt_namn = input("Skriv nytt namn: ")

        if nytt_namn == "" or nytt_namn == "/q":
            return

        lista[nummer - 1] = nytt_namn
        print("Namnet har ändrats.")

    except ValueError:
        print("Du måste skriva ett nummer.")

def ta_bort_van(lista):
    visa_vanner(lista)

    if len(lista) == 0:
        return

    try:
        nummer = int(input("Vilket nummer vill du ta bort? "))

        if nummer < 1 or nummer > len(lista):
            print("Ogiltigt nummer.")
            return

        borttagen = lista.pop(nummer - 1)
        print(f"{borttagen} har tagits bort.")

    except ValueError:
        print("Du måste skriva ett nummer.")

vanner = ["Anna", "Erik", "Sara", "Mohammed"]

kor_program = True

while kor_program:

    rensa_skarm()

    print("\033[95m")
    print("===================================")
    print("        MINA FAVVOVÄNNER")
    print("===================================")
    print("\033[0m")

    visa_vanner(vanner)

    print("\n1. Lägg till vän")
    print("2. Ändra vän")
    print("3. Ta bort vän")
    print("4. Visa lista")
    print("5. Avsluta")

    val = input("\nVälj 1-5: ")

    if val == "1":
        lagg_till_van(vanner)

    elif val == "2":
        andra_van(vanner)

    elif val == "3":
        ta_bort_van(vanner)

    elif val == "4":
        visa_vanner(vanner)

    elif val == "5" or val == "/q":
        kor_program = False
        print("Programmet avslutas...")

    else:
        print("Ogiltigt val.")

    input("\nTryck ENTER för att fortsätta...")