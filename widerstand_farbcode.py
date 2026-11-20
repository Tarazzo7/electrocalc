def widerstand_farbcode():
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
    print("1 = Farben in Widerstand umrechnen")
    print("2 = Widerstand in Farben umrechnen")
    while True:
        modus = input("Modus auswählen: ")
        if modus == "1":
            while True:
                print('schreiben sie "stop" um zurückzukehren.')

                ring1 = input("1. ring farbe:").lower()
                if ring1 not in ring1farbe:
                    print("falsche eingabe in farbe 1, versuchen sie es erneut")
                    continue
                if ring1 == "stop":
                    return

                ring2 = input("2. ring farbe:").lower()
                if ring2 not in ring2farbe:
                    print("falsche eingabe in farbe 2, versuchen sie es erneut")
                    continue
                if ring2 == "stop":
                    return

                ring3 = input("3. ring farbe:").lower()
                if ring3 not in ring3farbe:
                    print("falsche eingabe in farbe 3, versuchen sie es erneut")
                    continue
                if ring3 == "stop":
                    return

                ring4 = input("4. ring farbe:").lower()
                if ring4 not in ring4farbe:
                    print("falsche eingabe in farbe 4, versuchen sie es erneut")
                    continue
                if ring4 == "stop":
                    return
                break


            vorergebnis = str(ring1farbe[ring1]) + str(ring2farbe[ring2])
            ergebnis = int(vorergebnis) * (ring3farbe[ring3])
            endergebnis = ergebnis

            if ergebnis >= 1_000_000_000:
                endergebnis = f"{ergebnis / 1_000_000_000} G"
            elif ergebnis >= 1_000_000:
                    endergebnis = f"{ergebnis / 1_000_000} M"
            elif ergebnis >= 1_000:
                endergebnis = f"{ergebnis / 1_000} K"

            print(f"der widerstand beträgt {endergebnis}Ω mit einer Toleranz von {ring4farbe[ring4]}%")
            while True:
                endfrage = input("einen weiteren widerstand berechnen oder zurück zum Ohm-Rechner? 1 oder 2?: ")
                if endfrage == "2":
                    return
                elif endfrage == "1":
                    widerstand_farbcode()
                else:
                    print ("lern tippen du idiot")
                    continue


        elif modus == "2":
            while True:
                Ohm = input("wie viele ohm hat der widerstand?: ")
                erste_ziffer = int(Ohm[0])
                zweite_ziffer = int(Ohm[1])
                multiplikator = len(Ohm) - 2

                print("1. Ring:", zahl1farbe[erste_ziffer])
                print("2. Ring:", zahl1farbe[zweite_ziffer])
                print("3. Ring:", multiplikator_farben[multiplikator])

        


        else:
            print("falsche eingabe, versuche es erneut.")
        continue