erster_start = True
def widerstand_farbcode_start():
    global erster_start
    zahl1farbe = {
        0: "schwarz",
        1: "braun",
        2: "rot",
        3: "orange",
        4: "gelb",
        5: "grün",
        6: "blau",
        7: "violett",
        8: "grau",
        9: "weiß"
        }
    zahl2farbe = {
        0: "schwarz",
        1: "braun",
        2: "rot",
        3: "orange",
        4: "gelb",
        5: "grün",
        6: "blau",
        7: "violett",
        8: "grau",
        9: "weiß"
        }
    zahl3farbe = {
        1: "schwarz",
        10: "braun",
        100: "rot",
        1000: "orange",
        10000: "gelb",
        100000: "grün",
        1000000: "blau",
        10000000: "violett",
        100000000: "grau",
        1000000000: "weiß",
        0.1: "gold",
        0.01: "silber"
        }
    zahl4farbe = {  
        1: "braun",
        2: "rot",
        0.5: "grün",
        0.25: "blau",
        0.1: "violett",
        0.05: "grau",
        5: "gold",
        10: "silber"
        }
    ring1farbe = {
    "schwarz": 0,
    "braun": 1,
    "rot": 2,
    "orange": 3,
    "gelb": 4,
    "grün": 5,
    "blau": 6,
    "violett": 7,
    "grau": 8,
    "weiß": 9
}
    ring2farbe = {
    "schwarz": 0,
    "braun": 1,
    "rot": 2,
    "orange": 3,
    "gelb": 4,
    "grün": 5,
    "blau": 6,
    "violett": 7,
    "grau": 8,
    "weiß": 9
}
    ring3farbe = {
    "schwarz": 1,
    "braun": 10,
    "rot": 100,
    "orange": 1_000,
    "gelb": 10_000,
    "grün": 100_000,
    "blau": 1_000_000,
    "violett": 10_000_000,
    "grau": 100_000_000,
    "weiß": 1_000_000_000,
    "gold": 0.1,
    "silber": 0.01
}
    ring4farbe = {
    "braun": 1,
    "rot": 2,
    "grün": 0.5,
    "blau": 0.25,
    "violett": 0.1,
    "grau": 0.05,
    "gold": 5,
    "silber": 10
}
    multiplikator_farben = {
        0: "schwarz",
        1: "braun",
        2: "rot",
        3: "orange",
        4: "gelb",
        5: "grün",
        6: "blau",
        7: "violett",
        8: "grau",
        9: "weiß"
    }
    ring1 = None
    ring2 = None
    ring3 = None
    ring4 = None

    def ring1_f():
        ring1 = input("1. Ring (Ziffer 1): ").lower()

        if ring1 == "reset":
            return "reset"
        elif ring1 == "exit":
            return "exit"
        elif ring1 == "help":
            return "help"
        elif ring1 not in ring1farbe:
            print('Farbe Falsch, schreibe "help" um auswahl angezeigt zu bekommen')
            return ring1_f()
        else:
            return ring1


    def ring2_f():
        ring2 = input("2. Ring (Ziffer 2): ").lower()

        if ring2 == "reset":
            return "reset"
        elif ring2 == "exit":
            return "exit"
        elif ring2 == "help":
            return "help"
        elif ring2 not in ring2farbe:
            print('Farbe Falsch, schreibe "help" um auswahl angezeigt zu bekommen')
            return ring2_f()
        else:
            return ring2


    def ring3_f():
        ring3 = input("3. Ring (Multiplikator): ").lower()

        if ring3 == "reset":
            return "reset"
        elif ring3 == "exit":
            return "exit"
        elif ring3 == "help":
            return "help"
        elif ring3 not in ring3farbe:
            print('Farbe Falsch, schreibe "help" um auswahl angezeigt zu bekommen')
            return ring3_f()
        else:
            return ring3


    def ring4_f():
        ring4 = input("4. Ring (Toleranz): ").lower()

        if ring4 == "reset":
            return "reset"
        elif ring4 == "exit":
            return "exit"
        elif ring4 == "help":
            return "help"
        elif ring4 not in ring4farbe:
            print('Farbe Falsch, schreibe "help" um auswahl angezeigt zu bekommen')
            return ring4_f()
        else:
            return ring4

    print("1 = Farben in Widerstand umrechnen")
    print("2 = Widerstand in Farben umrechnen")
    print("3 = Zurück zum Hauptmenü")
    while True:
        modus = input("Modus auswählen: ")
        if modus == "1":
            def berechnung_farbe_zu_ohm():
                    vorergebnis = str(ring1farbe[ring1]) + str(ring2farbe[ring2])
                    ergebnis = int(vorergebnis) * ring3farbe[ring3] 

                    if ergebnis >= 1_000_000_000:
                        endergebnis = f"{ergebnis / 1_000_000_000} GΩ"  
                    elif ergebnis >= 1_000_000:
                        endergebnis = f"{ergebnis / 1_000_000} MΩ"
                    elif ergebnis >= 1_000:
                        endergebnis = f"{ergebnis / 1_000} kΩ"
                    else:
                        endergebnis = f"{ergebnis} Ω"

                    print(f"Der Widerstand beträgt {endergebnis} mit einer Toleranz von {ring4farbe[ring4]}%")
            while modus == "1":

                print('')
                print('"reset" um neu einzugeben.')
                print('"exit" um ins Hauptmenü zurückzukehren.')
                print('"help" um auswahlmöglichkeiten zu sehen')
                while True:
                    ring1 = ring1_f()
                    if ring1 == "reset":
                        print("")
                        continue
                    if ring1 == "exit":
                        return
                    if ring1 == "help":
                        print(ring1farbe)
                        ring1 = ring1_f()
                    
                    ring2 = ring2_f()
                    if ring2 == "reset":
                        print("")
                        continue
                    if ring2 == "exit":
                        return
                    if ring2 == "help":
                        print(ring2farbe)
                        ring2 = ring2_f()
                    
                    ring3 = ring3_f()
                    if ring3 == "reset":
                        print("")
                        continue
                    if ring3 == "exit":
                        return
                    if ring3 == "help":
                        print(ring3farbe)
                        ring3 = ring3_f()
                        
                    
                    ring4 = ring4_f()
                    if ring4 == "reset":
                        print("")
                        continue
                    if ring4 == "exit":
                        return
                    if ring4 == "help":
                        print(ring4farbe)
                        ring4 = ring4_f()
                
                    berechnung_farbe_zu_ohm()
                    while True:
                        endfrage = input("Weiter berechnen (1) oder zurück zum Hauptmenü (2)? ")

                        if endfrage == "1":
                            weiter = True
                            break
                        elif endfrage == "2":
                            weiter = False 
                            break   
                        else:
                            print("Falsche Eingabe. Bitte 1 oder 2 eingeben.")

                    if weiter == False:
                       return 

        elif modus == "2":
            while True:
                Ohm = input("wie viele ohm hat der widerstand?: ")
                erste_ziffer = int(Ohm[0])
                zweite_ziffer = int(Ohm[1])
                multiplikator = len(Ohm) - 2

                print("1. Ring:", zahl1farbe[erste_ziffer])
                print("2. Ring:", zahl2farbe[zweite_ziffer])
                print("3. Ring:", multiplikator_farben[multiplikator])
                if erster_start:
                    print("anmerkung (wird nur ein Mal angezeigt):")
                    print("4. Ring ist die Toleranz des Widerstands. Diese kann man über den Widerstand alleine nicht herausfinden.")
                    erster_start = False
                input("drücken sie enter um fortzufahren")
                print('')
                widerstand_farbcode_start()

        elif modus == "3":
            return
            

        else:
            print("falsche eingabe, versuche es erneut.")
            continue