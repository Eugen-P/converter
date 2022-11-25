from Funktionen import *

print("- - - Zahlenumrechner - - - ")
eingabe = ""

while eingabe != "q":
    ausgabeMenue()
    eingabe = input("Ihre Auswahl: ")
    if eingabe == "1":
        print(f"Hexadezimalzahl umwandeln. ")
        hexadezimal()
    elif eingabe == "2":
        print(f"Dezimalzahl umwandeln.")
        dezimal()
    elif eingabe == "3":
        print(f"Oktazahl umwandeln.")
        oktal()
    elif eingabe == "4":
        print(f"Dualzahl umwandeln. ")
        dual()
    elif eingabe == "q":
        print("Ende")
    else:
        print("Falsche Eingabe")
        print()
