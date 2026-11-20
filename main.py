#Spannung =U (V)
#Strom = I (A)
#Widerstand = R (Ohm)
from widerstand_farbcode import widerstand_farbcode

input("Willkommen zum Ohm'schen Gesetz Rechner! drücken sie Enter um Fortzufahren")
#abfrage
while True:
    ergebnisFrage = input("was möchten sie berechnen? U, R, I, P oder Farbe?: ").lower()
    erlaubteAntworten = ["r", "i", "u", "ohm", "a", "v", "p", "w", "farbe"]
    if ergebnisFrage in ["farbe"]:
        widerstand_farbcode()

    if ergebnisFrage in ["u", "v"]:
        StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
        WiderstandFrage = float(input("Geben sie bitte den widerstand ein: "))
        #U = I * R

    elif ergebnisFrage in ["i", "a"]:
        SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
        WiderstandFrage = float(input("Geben sie bitte den widerstand ein: "))
        #I = U / R

    elif ergebnisFrage in ["r", "ohm"]:
        SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
        StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
        #R = U / A

    elif ergebnisFrage in ["p", "w"]:
            SpannungFrage = float(input("Geben sie bitte die stromspannung ein: "))
            StromFrage = float(input("Geben sie bitte die stromstärke ein: "))
            #P = u * I

    elif ergebnisFrage not in erlaubteAntworten:
            print("einagbe falsch, probiere es erneut")
            input()
            continue

#berechnung
    if ergebnisFrage != "farbe":
        input("um " + ergebnisFrage + " zu berechnen, bitte enter drücken.")

    if ergebnisFrage in ["u", "v"]:
        ergebnis = StromFrage * WiderstandFrage
        print(ergebnis)

    elif ergebnisFrage in ["i", "a"]:
        ergebnis = SpannungFrage / WiderstandFrage
        print(ergebnis)

    elif ergebnisFrage in ["r", "ohm"]:
        ergebnis = SpannungFrage / StromFrage
        print(ergebnis)

    elif ergebnisFrage in ["p", "w"]:
        ergebnis = SpannungFrage * StromFrage
        print(ergebnis)

    endfrage = 1
    if ergebnisFrage != "farbe":
        endfrage = input("wollen sie noch eine berechnung durchführen oder einen widerstand durch den farbcode berechnen? 1 oder 2?: ")
    if endfrage == "1":
        continue
    elif endfrage == "2":
        widerstand_farbcode()

