from izbiralec_letov import izbiralec_letov
import os

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

izbiralec = izbiralec_letov()



inp = "krneki"
opcije = ( #navodilo za uporavnika glede glavnih opcij programa
    "1- planiranje poti",
)
while inp != "":
    for opcija in opcije:
        print(opcija)
    inp = input("vnesite ukaz: ")
    clear()
    if inp == "1":
        inp = input("zelite nastaviti svoje preference? (y,n): ")
        if inp == "y":
            izbiralec.vpis_preference()
            izbiralec.vpis_sprejemljive_ure_cakanja()
        datum1 = vnesi_datum("vpisite datum (yyyy-mm-dd): ")
        datum2 = vnesi_datum("vpisite datum (yyyy-mm-dd), ce hocete enosmeren let pustite prazno: ")
        naj_leti = izbiralec.najbolsi_let("LJU", "SIN", datum1, datum2, 2)
        
        for x in naj_leti:
            print(x)
        
        
