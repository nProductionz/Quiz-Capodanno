import random, time

def main():
    # Inizializzo i tipi delle domande
    type = ['generale','pop','gruppo','sfide']
    
    # Apro i file con le domande
    generaleF = open('domandeGenerale.txt')
    popF = open('domandePop.txt')
    gruppoF = open('domandeGruppo.txt')
    sfideF = open('domandeSfide.txt')

    # Carico le sfide negli array

    ### GENERALE ###
    genRead = generaleF.read()
    generaleTemp = genRead.split(';')
    generale = []
    for r in generaleTemp:
        generale.append(r.strip())
    generaleUscite = []

    ### POP ###
    popRead = popF.read()
    popTemp = popRead.split(';')
    pop = []
    for s in popTemp:
        pop.append(s.strip())
    popUscite = []

    ### GRUPPO ###
    gruppoRead = gruppoF.read()
    gruppoTemp = gruppoRead.split(';')
    gruppo = []
    for w in gruppoTemp:
        gruppo.append(w.strip())
    gruppoUscite = []

    ### SFIDE ###
    sfideRead = sfideF.read()
    sfideTemp = sfideRead.split(';')
    sfide = []
    for t in sfideTemp:
        sfide.append(t.strip())
    sfideUscite = []

    print("\n\n################\n\nLe sfide sono state caricate\n\n################\n\n")

    while(1):
        print("Carico la prossima sfida...\n\n")
        time.sleep(60)
        tipo = random.choice(type)

        if(tipo == 'generale'):
            domanda = random.choice(generale)
            
            # Controlla se la domanda è uscita
            while(domanda not in generaleUscite):
                domanda = random.choiche(generale)
            
            domandaSol = []
            domandaSol = domanda.split('|').strip()

            input("Domanda Selezionata - Categoria: Generale.\n\n")

            input(str(domandaSol[0]) + "\nSelezionare lo sfidante.\n\n")

            input("La soluzione è: " + str(domandaSol[1]+"\n\n"))
    
        if(tipo == 'pop'):
            domanda = random.choice(pop)
            
            # Controlla se la domanda è uscita
            while(domanda not in popUscite):
                domanda = random.choiche(pop)
            
            domandaSol = []
            domandaSol = domanda.split('|').strip()

            input("Domanda Selezionata - Categoria: Pop.\n\n")

            input(str(domandaSol[0]) + "\nSelezionare lo sfidante.\n\n")

            input("La soluzione è: " + str(domandaSol[1]+"\n\n"))

        if(tipo == 'gruppo'):
            domanda = random.choice(gruppo)
            
            # Controlla se la domanda è uscita
            while(domanda not in gruppoUscite):
                domanda = random.choiche(gruppo)
            
            domandaSol = []
            domandaSol = domanda.split('|').strip()

            input("Domanda Selezionata - Categoria: Gruppo.\n\n")

            input(str(domandaSol[0]) + "\nSelezionare lo sfidante.\n\n")

            input("La soluzione è: " + str(domandaSol[1]+"\n\n"))


        if(tipo == 'sfide'):
            domanda = random.choice(sfide)
            
            # Controlla se la domanda è uscita
            while(domanda not in sfideUscite):
                domanda = random.choiche(sfide)
            
            domandaSol = []
            domandaSol = domanda.split('|').strip()

            input("Domanda Selezionata - Categoria: Sfide.\n\n")

            input(str(domandaSol[0]) + "\nSelezionare lo sfidante.\n\n")

            input("La soluzione è: " + str(domandaSol[1]+"\n\n"))


        



main()