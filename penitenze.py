import random
from termcolor import colored, cprint

def main():
    
    # Apro i file e carico le penitenze

    penitenze1F = open('penitenze1.txt')
    penitenze1Read = penitenze1F.read()
    penitenze1Temp = penitenze1Read.split(';')
    penitenze1 = []
    for t in penitenze1Temp:
        penitenze1.append(t.strip())

    penitenze2F = open('penitenze2.txt')
    penitenze2Read = penitenze2F.read()
    penitenze2Temp = penitenze2Read.split(';')
    penitenze2 = []
    for t in penitenze2Temp:
        penitenze2.append(t.strip())

    penitenze3F = open('penitenze3.txt')
    penitenze3Read = penitenze3F.read()
    penitenze3Temp = penitenze3Read.split(';')
    penitenze3 = []
    for t in penitenze3Temp:
        penitenze3.append(t.strip())

    # Carico i giocatori nelle relative squadre

    sqAndrewTate = []
    andrewTateCounter = 0
    sqKanyeWest = []
    kanyeWestCounter = 0

    listaPartecipanti = ['mario','sara','sara2','alessia','sofia','stefano','samuel','valerio','veronica','farina','alice']

    # Creazione dizionari giocatori

    mario = dict(
        cont = 0,
        lista = []
    )

    alessia = dict(
        cont = 0,
        lista = []
    )

    sofia = dict(
        cont = 0,
        lista = []
    )

    stefano = dict(
        cont = 0,
        lista = []
    )

    samuel = dict(
        cont = 0,
        lista = []
    )

    valerio = dict(
        cont = 0,
        lista = []
    )

    sara = dict(
        cont = 0,
        lista = []
    )

    veronica = dict(
        cont = 0,
        lista = []
    )

    farina = dict(
        cont = 0,
        lista = []
    )

    sara2 = dict(
        cont = 0,
        lista = []
    )

    alice = dict(
        cont = 0,
        lista = []
    )


    # Carico Kanye West

    print(colored("\n# Caricamento della squadra Kanye West...\n",'red'))
    for i in range(5):
        nome  = input("\nInserire il nome del giocatore: ")
        sqKanyeWest.append(str(nome).strip())


    # Carico Andrew Tate

    print(colored("\n\n# Caricamento della squadra Andrew Tate...\n","red"))
    for i in range(6):
        nome  = input("\nInserire il nome del giocatore: ")
        sqAndrewTate.append(str(nome).strip().lower())

    finish=False
    while(finish!=True):
        print(colored("\nRound in corso...\n",'green'))
        input(colored("Attendere la fine del round\n\n",'green'))
        check = 0
        while(check == 0):

            checkDict = False
            checkCount = False

            name = input(colored("Indicare a quale giocatore della squadra assegnare il malus: ",'red'))
            n = str(name).lower()

            # Controlli sul nome del giocatore

            # Aumento contatore squadra

            if(n in sqKanyeWest):
                kanyeWestCounter+=1
                checkCount = True

            elif(n in sqAndrewTate):
                andrewTateCounter+=1
                checkCount = True

            else:
                print("### Unknown Error - Coumt ###\n") 

            # Mario

            if(n == "mario"):
                temp = mario["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in mario["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in mario["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in mario["lista"]):
                        malus = random.choice(penitenze3)
                mario["cont"] = temp
                mario["lista"].append(malus)

                checkDict = True


            # Alessia

            elif(n == "alessia"):
                temp = alessia["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in alessia["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in alessia["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in mario["lista"]):
                        malus = random.choice(penitenze3)
                alessia["cont"] = temp
                alessia["lista"].append(malus)

                checkDict = True


            # Sofia 

            elif(n == "sofia"):
                temp = sofia["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in sofia["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in sofia["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in sofia["lista"]):
                        malus = random.choice(penitenze3)
                sofia["cont"] = temp
                sofia["lista"].append(malus)

                checkDict = True


            # Stefano 
            
            elif(n == "stefano"):
                temp = stefano["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in stefano["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in stefano["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in stefano["lista"]):
                        malus = random.choice(penitenze3)
                stefano["cont"] = temp
                stefano["lista"].append(malus)

                checkDict = True


            # Samuel

            elif(n == "samuel"):
                temp = samuel["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in samuel["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in samuel["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in samuel["lista"]):
                        malus = random.choice(penitenze3)
                samuel["cont"] = temp
                samuel["lista"].append(malus)

                checkDict = True


            # Valerio

            elif(n == "valerio"):
                temp = valerio["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in valerio["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in valerio["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in valerio["lista"]):
                        malus = random.choice(penitenze3)
                valerio["cont"] = temp
                valerio["lista"].append(malus)

                checkDict = True


            # Sara

            elif(n == "sara"):
                temp = sara["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in sara["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in sara["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in sara["lista"]):
                        malus = random.choice(penitenze3)
                sara["cont"] = temp
                sara["lista"].append(malus)

                checkDict = True

            
            # Veronica 

            elif(n == "veronica"):
                temp = veronica["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in veronica["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in veronica["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in veronica["lista"]):
                        malus = random.choice(penitenze3)
                veronica["cont"] = temp
                veronica["lista"].append(malus)

                checkDict = True

    
            # Farina

            elif(n == "farina"):
                temp = farina["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in farina["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in farina["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in farina["lista"]):
                        malus = random.choice(penitenze3)
                farina["cont"] = temp
                farina["lista"].append(malus)

                checkDict = True


            # Sara2

            elif(n == "sara2"):
                temp = sara2["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in sara2["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in sara2["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in sara2["lista"]):
                        malus = random.choice(penitenze3)
                sara2["cont"] = temp
                sara2["lista"].append(malus)

                checkDict = True


            # Alice

            elif(n == "alice"):
                temp = alice["cont"]
                temp+=1
                malus = ""
                if(temp == 1):
                    malus = random.choice(penitenze1)
                    while(malus in alice["lista"]):
                        malus = random.choice(penitenze1)
                elif(temp == 2):
                    malus = random.choice(penitenze2)
                    while(malus in alice["lista"]):
                        malus = random.choice(penitenze2)
                elif(temp>2):
                    malus = random.choice(penitenze3)
                    while(malus in alice["lista"]):
                        malus = random.choice(penitenze3)
                alice["cont"] = temp
                alice["lista"].append(malus)

                checkDict = True

            else:
                print("### Unknown Error - Dict ###\n")

            
            if(checkDict==True and checkCount==True):
                rp = str("\n#########################\n\n"+str(malus)+"\n\n#########################")
                cprint(rp,"white","on_magenta")
                if(kanyeWestCounter>=10):
                    finish=True
                elif(andrewTateCounter>=10):
                    finish=True
                check += 1
                print(colored("\nPUNTEGGIO   "+str(andrewTateCounter)+" : "+str(kanyeWestCounter)+"\n",'yellow'))
            else:
                print("\n ### Unknown Error... ###\n")

    
    if(kanyeWestCounter >= 10):
        input("Vince la squadra di Andrew Tate: auguri e figli pelati (ma soprattutto alpha).\n")

    elif(andrewTateCounter >= 10):
        input("Vince la squadra di Kanye West: ricordate chi era una brava persona dopotutto...\n")

    else:
        input("Shit happened")
    
main()