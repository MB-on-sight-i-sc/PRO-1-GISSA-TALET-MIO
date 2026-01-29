import random  

print("Välkommen till mitt lilla program!")
print("Här kommer alla utmaningar i ett enda program.\n")


print("--- Uppgift 1: Skriv bara siffror ---")
while True:
    siffror = input("Skriv bara siffror: ")
    if siffror.isdigit():               
        print("Bra jobbat! Du skrev:", siffror)
        break
    else:
        print("Fel! Bara siffror tack. Försök igen.\n")


print("\n--- Uppgift 2: Första 10 bokstäverna ---")
ord = input("Skriv ett ord eller en mening: ")
print("Första 10 tecknen är:", ord[:10])

print("\n--- Uppgift 3: Kapa för långt ord ---")
längd_gräns = 15
text = input("Skriv något (vi kapar vid 15 tecken): ")
if len(text) > längd_gräns:
    kort_text = text[:längd_gräns] + "..."
    print("Kapad version:", kort_text)
else:
    print("Du skrev:", text)


print("\n--- Uppgift 4: Namn med fina bokstäver ---")
while True:
    namn = input("Skriv ditt namn (bara bokstäver): ")
    if namn.isalpha():                  
        fint_namn = namn[0].upper() + namn[1:].lower()  
        print("Hej", fint_namn + "!")
        print("Ditt namn har", len(namn), "bokstäver.")
        break
    else:
        print("Oj! Bara bokstäver i namnet tack.\n")


print("\n--- Uppgift 5: Gissa talet (1-10) ---")
print("Jag tänker på ett tal mellan 1 och 10.")
print("Skriv 'q' när du vill sluta spela.")

hemligt_tal = random.randint(1, 10)

while True:
    gissning = input("Din gissning: ")
    
    if gissning == "q":
        print("Du slutade. Det hemliga talet var", hemligt_tal)
        break
    
    if gissning.isdigit():              
        tal = int(gissning)
        if tal < hemligt_tal:
            print("För lågt! Gissa högre.")
        elif tal > hemligt_tal:
            print("För högt! Gissa lägre.")
        else:
            print("Grattis! Du gissade rätt:", hemligt_tal)
            break
    else:
        print("Skriv en siffra eller 'q' för att sluta.")

print("\nTack för att du kört programet=)")