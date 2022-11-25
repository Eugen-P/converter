
def ausgabeMenue():
    print("\n - - - \nBitte wählen Sie ...\n")
    print("(1) Hexadezimalzahl umwandeln.")
    print("(2) Dezimalzahl umwandeln.")
    print("(3) Oktalzahl umwandeln.")
    print("(4) Dualzahl umwandeln.")
    print("(q) Beenden\n")

def hexadezimal():
    zahl = input("\n - - - \nBitte Zahl fur Umrechnung eingeben: ")
    # hexa in dezimal
    rest = str()
    base = 16
    power = 1
    antwort = 0
    for i in zahl[:: -1]:
        antwort += int(i) * power
        power *= base
        
    print("\nEingegebene Zahl umrechnen in...\n")
    print("(d) Dezimalzahl")
    print("(o) Oktalzahl")
    print("(b) Dualzahl \n")
    eingabe = input("Ihre Auswahl: ")

    if eingabe == 'd':
        print(f"Ergebniss: {antwort}")
    elif eingabe == 'o':
        base = 8
        while antwort > 0:
            rest = str(antwort % base) + rest
            antwort //= base
        print(f"Ergebniss: {rest}")     
    elif eingabe == 'b':
        while antwort > 0:
            base = 2
            rest = str(antwort % base) + rest
            antwort //= base
        print(f"Ergebniss: {rest}") 
    else:
        print("Falsche Eingabe\n")
        quit()
    input('\nWeiter mit der Eingebe-Taste')
def dezimal():
    rest = str()
    zahl = int(input("\n - - - \nBitte Zahl fur Umrechnung eingeben: "))
    print("\nEingegebene Zahl umrechnen in...\n")
    print("(h) Hexadezimalzahl")
    print("(o) Oktalzahl")
    print("(b) Dualzahl \n")
    eingabe = input("Ihre Auswahl: ")

    if eingabe == 'h':
        base = 16
        al = 'ABCDEF'
        c = int()
        while zahl > 0:
            c =  zahl % base
            if c < 10:
                rest = str(c) + rest
            else:
                rest = al[c-10] + rest
            zahl //= base
        print(f"Ergebniss: {rest}") 
    elif eingabe == 'o':
        base = 8      
        while zahl > 0:
            rest = str(zahl % base) + rest
            zahl //= base
        print(f"Ergebniss: {rest}") 
    elif eingabe == 'b':
        base = 2
        while zahl > 0:
            rest = str(zahl % base) + rest
            zahl //= base
        print(f"Ergebniss: {rest}") 
    else:
        print("Falsche Eingabe\n")
        quit()
    input('\nWeiter mit der Eingebe-Taste')   
def oktal():
    zahl = input("\n - - - \nBitte Zahl fur Umrechnung eingeben: ")
    #oktal in dezimal
    rest = str()
    base = 8
    power = 1
    antwort = 0
    for i in zahl[:: -1]:
        antwort += int(i) * power
        power *= base
    print("\nEingegebene Zahl umrechnen in...\n")
    print("(d) Dezimalzahl")
    print("(h) Hexadezimalzahl")
    print("(b) Dualzahl \n")
    eingabe = input("Ihre Auswahl: ")

    if eingabe == 'd':
        print(f"Ergebniss: {antwort}")
    elif eingabe == 'h':
        base = 16
        al = 'ABCDEF'
        c = int()
        while antwort > 0:
            c =  antwort % base
            if c < 10:
                rest = str(c) + rest
            else:
                rest = al[c-10] + rest
            antwort //= base
        print(f"Ergebniss: {rest}")        
    elif eingabe == 'b':
        while antwort > 0:
            base = 2
            rest = str(antwort % base) + rest
            antwort //= base
        print(f"Ergebniss: {rest}")    
    else:
        print("Falsche Eingabe\n")
        quit()
    input('\nWeiter mit der Eingebe-Taste')
        
def dual():
    zahl = input("\n - - - \nBitte Zahl fur Umrechnung eingeben: ")
    # dual in dezimal
    rest = str()
    base = 2
    power = 1
    antwort = 0
    for i in zahl[:: -1]:
        antwort += int(i) * power
        power *= base
    print("\nEingegebene Zahl umrechnen in...\n")
    print("(d) Dezimalzahl")
    print("(o) Oktalzahl")
    print("(h) Hexadezimalzahl\n")
    eingabe = input("Ihre Auswahl: ")
    if eingabe == 'd':
        print(f"Ergebniss: {antwort}")
    elif eingabe == 'o':
        base = 8
        while antwort > 0:
            rest = str(antwort % base) + rest
            antwort //= base
        print(f"Ergebniss: {rest}")     
    elif eingabe == 'h':
        base = 16
        al = 'ABCDEF'
        c = int()
        while antwort > 0:
            c =  antwort % base
            if c < 10:
                rest = str(c) + rest
            else:
                rest = al[c-10] + rest
            antwort //= base
        print(f"Ergebniss: {rest}")       
    else:
        print("Falsche Eingabe\n")
        quit()
    input('\nWeiter mit der Eingebe-Taste')
   
