import os
import time
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')


def visa_nuvarande_tid():
    nu = datetime.now()
    print("Nu:", nu.strftime("%Y-%m-%d %H:%M:%S"))


def visa_format():
    nu = datetime.now()
    print("Datum:", nu.strftime("%Y-%m-%d"))
    print("Tid:", nu.strftime("%H:%M:%S"))
    print("Svenskt:", nu.strftime("%d/%m/%Y"))


def klocka_live():
    print("Tryck Ctrl+C för att stoppa")
    try:
        while True:
            nu = datetime.now()
            print(nu.strftime("%H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStoppad")


def stoppur():
    input("Tryck Enter för att starta...")
    start = time.time()

    input("Tryck Enter för att stoppa...")
    slut = time.time()

    print("Tid:", round(slut - start, 2), "sekunder")


def datum_text():
    månader = [
        "Januari","Februari","Mars","April","Maj","Juni",
        "Juli","Augusti","September","Oktober","November","December"
    ]

    nu = datetime.now()
    print(f"{nu.day} {månader[nu.month - 1]} {nu.year}")


def dagar_mellan():
    år = int(input("År: "))
    månad = int(input("Månad: "))
    dag = int(input("Dag: "))

    valdatum = datetime(år, månad, dag)
    idag = datetime.now()

    skillnad = idag - valdatum
    print("Antal dagar:", abs(skillnad.days))


def nedrakning():
    sek = int(input("Hur många sekunder? "))

    for i in range(sek, 0, -1):
        print(i, end="\r")
        time.sleep(1)

    print("KLART!")


def meny():
    while True:
        print("\n--- MENY ---")
        print("1. Visa nuvarande tid")
        print("2. Visa olika format")
        print("3. Live-klocka")
        print("4. Stoppur")
        print("5. Datum med text")
        print("6. Räkna dagar mellan datum")
        print("7. Nedräkning")
        print("0. Avsluta")

        val = input("Välj: ")

        if val == "1":
            visa_nuvarande_tid()
        elif val == "2":
            visa_format()
        elif val == "3":
            klocka_live()
        elif val == "4":
            stoppur()
        elif val == "5":
            datum_text()
        elif val == "6":
            dagar_mellan()
        elif val == "7":
            nedrakning()
        elif val == "0":
            break
        else:
            print("Fel val!")


meny()