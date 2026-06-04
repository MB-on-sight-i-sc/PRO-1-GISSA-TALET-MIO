bilar = [
    {"märke": "Volvo", "modell": "V60", "år": 2022, "färg": "svart", "pris": 389000},
    {"märke": "Volvo", "modell": "945", "år": 1994, "färg": "svart", "pris": 50000},
    {"märke": "Audi", "modell": "RS-6", "år": 2015, "färg": "vit", "pris": 850000},
    {"märke": "BMW", "modell": "M5", "år": 2024, "färg": "blå", "pris": 1400000}
]

def visa_bilar(lista):
    for i, bil in enumerate(lista, 1):
        print(f"{i}. {bil['märke']} {bil['modell']} ({bil['år']}) - {bil['pris']:,} kr, Färg: {bil['färg']}")

def lagg_till_bil():4
    ny = {
        "märke": input("Märke: "),
        "modell": input("Modell: "),
        "år": int(input("År: ")),
        "färg": input("Färg: "),
        "pris": int(input("Pris (kr): "))
    }
    bilar.append(ny)
    print("Bil tillagd!")

def ta_bort_bil():
    try:
        index = int(input("Vilken bil vill du ta bort? ")) - 1
        print(f"Tog bort: {bilar.pop(index)['märke']} {bilar[index]['modell']}")
    except:
        print("Fel nummer!")

def andra_bil():
    try:
        index = int(input("Vilken bil vill du ändra? ")) - 1
        bil = bilar[index]
        for key in ["märke","modell","år","färg","pris"]:
            inp = input(f"{key.capitalize()} (enter = behåll {bil[key]}): ")
            if inp:
                bil[key] = int(inp) if key in ["år","pris"] else inp
        print("Bil uppdaterad!")
    except:
        print("Fel inmatning!")

while True:
    val = input("\n[1] Visa bilar [2] Lägg till [3] Ta bort [4] Ändra [0] Avsluta: ").strip()
    if val == "0": break
    elif val == "1": visa_bilar(bilar)
    elif val == "2": lagg_till_bil()
    elif val == "3": ta_bort_bil()
    elif val == "4": andra_bil()
    else: print("Välj 0-4 tack!")
