namn = ["Erik", "noel", "Mohammed", "vilgot", "linus"]

print("Lista med namn:")
for person in namn:
    print(person)

namn[0] = "Anne Onym"
print("\nEfter ändring:")
for person in namn:
    print(person)


namn.append("Fatima")
print("\nEfter att ha lagt till Fatima:")
for person in namn:
    print(person)

print("\nAntal namn just nu:", len(namn))


borttaget = namn.pop()
print("\nTog bort:", borttaget)
print("Listan nu:")
for person in namn:
    print(person)


print("\n=== Namnprogram ===\n")

while True:
    print("Nuvarande namn:", namn)
    print("Antal:", len(namn))
    print("  Skriv ett namn → lägg till")
    print("  Skriv 'radera nummer' t.ex. radera 1")
    print("  Skriv 'sluta' för att avsluta")
    
    val = input("\nVad vill du göra? ").strip()
    
    if val.lower() == "sluta":
        print("\nHej då! Slutlig lista:")
        for n in namn:
            print("→", n)
        break
        
    elif val.startswith("radera "):
        try:
            index = int(val.split()[1])
            if 0 <= index < len(namn):
                bort = namn.pop(index)
                print(f"Tog bort: {bort}")
            else:
                print("Fel index!")
        except:
            print("Skriv t.ex. radera 0")
            
    elif val != "":
        namn.append(val)
        print(f"Lade till: {val}")
    else:
        print("Skriv något...")