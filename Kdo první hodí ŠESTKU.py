from random import randrange
hra = input ("Chceš si zahrát kostky? ")

if hra == "ano" :
  print ("Paráda, jdem na to!")
  hod = input ('Napiš "y" a začni házet kostkou:')
  if hod == "y":
    
    #HRAJE HRÁČ#
    pocet_hodu = 0
    while True: # hazi do nekonecna
       cislo = (randrange (1,7))
       pocet_hodu = pocet_hodu + 1
       print (cislo)
       if cislo == 6:
         print("Tvůj počet hodů byl: ", pocet_hodu , "\nTeď je na řadě počítač:")
         break
       
    #HRAJE POCITAC#   
    pocet_hoduPC = 0
    while True: #hazí do nekonecna
      pc_hod = (randrange (1,7))
      pocet_hoduPC = pocet_hoduPC + 1
      print (pc_hod)
      
      if pc_hod == 6:
        
        break
    print("Počet hodů počítače byl: ", pocet_hoduPC) 
      
         
    if pocet_hoduPC > pocet_hodu:
      print ("Vyhráváš, hodil jsi 6 na méně hodů")
    elif pocet_hoduPC < pocet_hodu:
      print ("Prohráváš, počítač hodil šestku rychleji")
    else:
      print ("Tohle je remíza, oba jste hodili šestku na stejný počet hodů")
      
elif hra == "ne":
  print ("Nevadí, třeba příště")
else:
  print ("Nerozumím Ti.")
