def U_berechnung():
    while True:
         
        try:
            StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        try:
            WiderstandFrage = float(input("Geben sie bitte den widerstand ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        return StromFrage * WiderstandFrage
        #U = I * R

def I_berechnung():
    while True:
        try:
            SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        try:
            WiderstandFrage = float(input("Geben sie bitte den widerstand ein: "))
        except ValueError:
                    print("Falsche eingabe. Bitte eine Zahl eingeben.")
                    print("")
                    continue
        return SpannungFrage / WiderstandFrage
        #I = U / R

def R_berechnung():
    while True:
        try:
            SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        try:
            StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        return SpannungFrage / StromFrage
        #R = U / A

def P_berechnung():
    while True:
        try:
            SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
        except ValueError:
            print("Falsche eingabe. Bitte eine Zahl eingeben.")
            print("")
            continue
        try:
            StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
        except ValueError:
                    print("Falsche eingabe. Bitte eine Zahl eingeben.")
                    print("")
                    continue
        return SpannungFrage * StromFrage
        #P = u * I