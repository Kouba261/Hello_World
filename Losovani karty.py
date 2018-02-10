import random

balicek = []
znak = '♠', '♥', '♦', '♣'
hodnota = list(range(2,11)) + ['J','Q','K','A'] #list.range vytvori radu cisel od 2 do 11
karta = []
     

    
def losovani(): #FUNKCE vylosuje nahodnou kartu
    
    for Vyber_znak in znak:
        for Vyber_hodnota in hodnota:
                    karta = str(Vyber_hodnota)+Vyber_znak  # str prevede na retezec
                    balicek.append(karta)
                    

    random.shuffle(balicek) #nahodne zamicha balicek

    Vyber_kartu = random.choice(balicek)

    print("Vylosoval jsem kartu: ", Vyber_kartu)
      

def dalsi_karta(): #FUNKCE zepta se zda chces dalsi kartu
        
    Nova_karta = input("Chces losovat kartu?")

    if Nova_karta == "ano":
            losovani()
            dalsi_karta()
    elif Nova_karta == "ne":
        print ("Dobrá, nebudeme losovat")
        return
    else:
        print("Nerozumím Ti, odpovídej 'ano' nebo 'ne'")
        return
    
        
dalsi_karta()

