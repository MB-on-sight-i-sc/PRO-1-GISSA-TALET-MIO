# import os

# os.system("cls")


# secret=33
# while True:
#     guess=int(input("gissa:"))
#     if guess==secret:
#         print("du gissa rätt")



import random 
import os 
os.system('cls')

spel = True

while spel == True: # Spelets loop som avgör om spelet är igång eller inte

    os.system('cls') # Clearar cmd
    
    försök = 7 # hur många försök man har

    hemligt_tal = random.randint(1,100) # generar random tal mellan 1 till 100

    print("Gissa det hemliga talet mellan 1 och 100!")
        
    print("Du har 7 försök.\n")

    while försök >0: # loop att spelet är igång när man har över 0 försök
        try:
            gissning = int(input(f"[{försök} försök kvar] Gissa: ")) 
        except ValueError:
            print("ANVÄND SIFFROR!!!")
            continue
            

        if gissning == hemligt_tal: # om gissningen är rätt får spelaren reda på det och den avslutar andra loopen
            print("Du hade rätt! ")
            break
            
        elif gissning >= hemligt_tal: # om gissningen är högre än talet får spelaren reda på det och får försöka igen
            print("för högt!!! prova ett lägre tal.")
            försök -= 1 # tar bort ett försök
        
        elif gissning <= hemligt_tal: # om gissningen är lägre än talet får spelaren reda på det och får försöka igen
            print("för lågt!! prova något högre tal. ")
            försök -= 1 # tar bort ett försök
        
        elif försök == 0: # om man har 0 försök kvar avslutas spelet och talar om vad talet var
            print(f"du har tyvär inga försök kvar!!! det hemliga talet var{hemligt_tal} =( ")
            break
        
    
        
        else: # om något annat konstigt skulle hända avslutas spelet
            print("Något gick snett, spelet avslutas")  
            break
            
  
    spela_igen = input("Vill du spela igen? (j/n): ") # frågar om man vill spela igen

    if spela_igen == "n": # om spelare svarar n avslutas spelet
        print ("Tack för att du spelade! hej då! ")
        break
    
    elif spela_igen == "j": # om spelare svarar j startas spelet om
        print("Ny omgång!!!")
        continue
    else: # om man svarar annat säger den till
        print("Svara endast med j/n")
        


print("spelet är över")
spel == False

