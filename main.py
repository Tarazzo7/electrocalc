#Spannung =U (V)
#Strom = I (A)
#Widerstand = R (Ohm)
from URI_rechner import *
from widerstand import widerstand_farbcode_start
def main():
    while True:
        print("")
        ergebnisFrage = input("was möchten sie berechnen? U, R, I, P oder Farbe?: ").lower()
        erlaubteAntworten = ["r", "i", "u", "ohm", "a", "v", "p", "w", "farbe"]
        if ergebnisFrage in ["farbe"]:
            widerstand_farbcode_start()

        if ergebnisFrage in ["u", "v"]:
            ergebnis = U_berechnung()
            print(f"U = {ergebnis}V")
        
        elif ergebnisFrage in ["i", "a"]:
            ergebnis = I_berechnung()
            print(f"I = {ergebnis}A")

        elif ergebnisFrage in ["r", "ohm"]:
            ergebnis = R_berechnung()
            print(f"R = {ergebnis}Ω")

        elif ergebnisFrage in ["p", "w"]:
            ergebnis = P_berechnung()
            print(f"P = {ergebnis}W")
main()
