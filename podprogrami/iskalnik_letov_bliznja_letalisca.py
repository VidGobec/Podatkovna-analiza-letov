import json, iata
from izbiralec_letov import IzbiralecLetov

letalisca = ["LJU,KLU,GRZ","ZAG,TRS,TSF", "VCE,TRS,VIE", "SZG,LIN,MXP", "MUC,STR,BUD"]
destinacija = input("Vpiši IATA kodo kam želiš leteti: ").upper()

if iata.iata(destinacija):
    datum = input("Vpiši termin (format: YYYY-MM-DD - YYYY-MM-DD): ")
    try:
        odhod_datum, prihod_datum = datum.split(" - ")
    except ValueError:
        print("\n⚠️ Napačni format za datum. Uporabi format YYYY-MM-DD - YYYY-MM-DD.\n")
        exit()
    izbiralec = IzbiralecLetov()
    vsi_rezultati = izbiralec.najbolsi_let(letalisca, destinacija, odhod_datum, prihod_datum, n=5)
    izbiralec.izpisi_podatke_o_letih(vsi_rezultati)
else:
    print("\n⚠️ Vpiši veljavno IATA kodo!\n")