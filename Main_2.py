from podprogrami.izbiralec_letov import IzbiralecLetov
import os

#start program za "aplikacijo"

def vnesi_datum(msg = "vpisite datum (yyyy-mm-dd): "):
    """funkcija, ki uporabnika prosi da vnese datum ter ga vrne"""
    while True:
            try:
                inp = input(msg)
                datum1 = inp.split("-")
                if len(datum1[0]) == 4 or inp=="": #recimo da je to dovolj dober test
                    break
            except:
                print("prosim vnesite primeren datum.")
    return inp

#funkcija ki izbrise tekst na terminalu
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

izbiralec = IzbiralecLetov()



inp = "krneki"
opcije = ( #navodilo za uporavnika glede glavnih opcij programa
    "1- planiranje poti",
)
while inp != "":
    for opcija in opcije:
        print(opcija)
    inp = input("vnesite ukaz: ")
    #planiranje leta
    if inp == "1":
        inp = input("zelite nastaviti svoje preference? (ja,ne): ")
        if inp == "ja":
            izbiralec.vpis_preference()
            izbiralec.vpis_sprejemljive_ure_cakanja()
        datum1 = vnesi_datum("vpisite datum (yyyy-mm-dd): ")
        datum2 = vnesi_datum("vpisite datum (yyyy-mm-dd), ce hocete enosmeren let pustite prazno: ")
        pomTab = ["LJU","ZAG","TRS"] #,"TSF", "VCE","TRS","VIE", "SZG","LIN","MXP", "MUC","STR","FCO", "BUD","PRG","ZRH"]
        naj_leti = izbiralec.najbolsi_let(pomTab, "SIN", datum1, datum2, 10)
        
        i = 0
        for x in naj_leti:
            i += 1
            print(f"LET {i}:")
            for let in x["flights"]:
                try:
                    print(let["departure_airport"]["name"], "->", let["arrival_airport"]["name"])
                except Exception as e:
                    print(e)
    #prikaz grafov
    if inp == "2":
        pass
        
        
