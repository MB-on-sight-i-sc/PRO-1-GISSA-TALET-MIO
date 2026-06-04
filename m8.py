import os

os.system("cls" if os.name == "nt" else "clear")


GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


friends_list = ["Noel", "Erik", "Linus"]

def show_friends():
    if not friends_list:
        print(f"{RED}Listan är helt tom.{RESET}")
    else:
        print(f"{BLUE}Här är personerna i listan:{RESET}")
        for i, friend in enumerate(friends_list, 1):
            print(f"{i}. {friend}")

def add_friend():
   
    name = input(f"{YELLOW}Vem vill du lägga till? {RESET}").strip().title()
    if name == "" or name == "/q":
        return False
       
    if name in friends_list:
        print(f"{RED}Den personen är redan inlagd.{RESET}")
    else:
        friends_list.append(name)
        print(f"{GREEN}{name} är nu tillagd!{RESET}")
    return True

def remove_friend():
    
    show_friends()
    name = input(f"{YELLOW}Vem ska tas bort? (Skriv /q för att avbryta): {RESET}").strip().title()
    if name == "" or name == "/q":
        return False
       
    try:
        friends_list.remove(name)
        print(f"{GREEN}{name} är raderad från listan.{RESET}")
    except ValueError:
        print(f"{RED}Hittade inte det namnet.{RESET}")
       
    return True

def edit_friend():
    
    show_friends()
    old_name = input(f"{YELLOW}Vem vill du döpa om? (Skriv /q för att avbryta): {RESET}").strip().title()
    if old_name == "" or old_name == "/q":
        return False
       
    try:
        idx = friends_list.index(old_name)
       
        new_name = input(f"{YELLOW}Vad ska personen heta istället? {RESET}").strip().title()
        if new_name == "" or new_name == "/q":
            return False
           
        if new_name in friends_list:
            print(f"{RED}Det nya namnet är redan upptaget.{RESET}")
        else:
            friends_list[idx] = new_name
            print(f"{GREEN}{old_name} heter nu {new_name}.{RESET}")
           
    except ValueError:
        print(f"{RED}Hittade inte det namnet.{RESET}")
       
    return True

def main():
    """Huvudfunktion som kör programmet."""
    print(f"{YELLOW}--- Personregistret startat! ---{RESET}")
    show_friends()
   
    print("\nVälj: visa (v), lägg till (l), radera (r), döp om (ä), stäng (/q)")
   
    while True:
        try:
            command = input(f"{YELLOW}\nDitt val: {RESET}").strip().lower()
            if command in ["/q", "avsluta", "stäng"]:
                print(f"{BLUE}Programmet stängs. Antal personer sparade: {len(friends_list)}. Vi ses!{RESET}")
                break
            elif command == "v":
                show_friends()
            elif command == "l":
                add_friend()
            elif command == "r":
                remove_friend()
            elif command == "ä":
                edit_friend()
            else:
                print(f"{RED}Ogiltigt val. Försök med v, l, r, ä eller /q.{RESET}")
               
        except KeyboardInterrupt:
            print(f"\n{BLUE}Tvingat avslut. Totalt sparade: {len(friends_list)}.{RESET}")
            break
        except Exception as e:
            print(f"{RED}Något gick snett: {e}{RESET}")

if __name__ == "__main__":
    main()