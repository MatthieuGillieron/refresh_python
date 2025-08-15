
# "calculer" une moyenne version facile
def result():
    note_1 = int(input("Valeur de la premiere note: "))
    note_2 = int(input("Valeur de la seconde note: "))
    note_3 = int(input("Valeur de la derniere note: "))
    moyenne = int((note_1 + note_2 + note_3) / 3)
    print(moyenne)
    
#recolter des values
def how_much():
    wallet = int(input("Quelle est ton solde: "))
    iphone = 50
    print("le prix de l 'iphone est de ", iphone , "$")
    print("veux tu l'acheter ?")
    answer = input("oui ou non ? ")
    if answer == "oui":
        if wallet >= iphone:
            print("Achat realiser, votres solde actuelle est de : ",  wallet - iphone)
        else:
            print("T'es brokeeeee l'iphone vaut :", iphone, "et tu as : ", wallet)
    else:
        print("bonne journee")
  
    
if __name__ == '__main__':
    result()
    how_much()
    
    