import json
from serpapi import GoogleSearch
import utility_funkcije as f
import math

class izbiralec_letov:
    def __init__(self) -> None:
        self._preferenca = { 
                                    "cena": 1,
                                    "celoten cas" : 0,
                                    "cas v zraku" : 0,
                                    "cas med leti" : 0,
                                    "karbonske emisije": 0
                                    }
        self._tabela_primerjanj = []
        self._zadnjaKulUra = 8
        pass

    def get_preferenca(self):
        """vrne trenutno shranjen preferencni slovar"""
        return self._preferenca
    
    def set_preferenca(self, pref):
        """nastavi preferenco na pref"""
        self._preferenca = pref

    def get_ZadnjaKulUra(self):
        return self._zadnjaKulUra

    def set_ZadnjaKulUra(self, ure):
        """funkcija za spremeniti vrednost zadnje ure, za katero je uporabniku sprejemljivo cakati za nov let"""
        try:
            self._zadnjaKulUra = float(ure)
        except:
            print("nistve vnesli pravilne ure, vrednost ostane zadnje spremenljive ure nespremenena.")

    def vpis_preference(self):
        """funkcija, ki z pomocjo uporabniskega vnosa nastavi preferenco uporabnika"""
        nova_preferenca = dict()
        while len(nova_preferenca) < len(self.get_preferenca()):
            for pref in self.get_preferenca():
                try:
                    inp = float(input(f"vpisite preferenco za {pref}: "))
                    nova_preferenca[pref] = inp
                except:
                    print("prosim vnesite stevilo.")
                    break

        self.set_preferenca(nova_preferenca)

    def vpis_sprejemljive_ure_cakanja(self):
        """funkcija, ki uporabnika vprasa koliko je zanj sprejemljivo pocakati med leti in to vrednost nastavi"""
        self.set_ZadnjaKulUra(input("Vnesite najvec koliko ur je za vas sprejemljivo cakati med leti: "))

    def _kreiranje_tabele_primerjanj(self, tabela_letov):
        """metoda prejme tabelo letov in kreaira tabelo za primerjanje
        tabela primerjan predstavlja 2d tabelo ki izgleda nekako:
               1      2      3  ... n
        cena   c1     c2..
        cas    c3     c4...
        ...
        zgrajena pa je kot slovar, kjer je kljuc npr cena vrednost pa tabela vrednost (npr c1 c2 zgoraj)
        """
        ##cena
        self._tabela_primerjanj.append([x["price"] for x in tabela_letov])
        ##cas v zraku(v minutah)
        self._tabela_primerjanj.append([sum([let["duration"] for let in x["flights"]]) for x in tabela_letov])
        ##cas med leti(tabela minut - [mina, minb])
        self._tabela_primerjanj.append([[let["duration"] for let in x["layovers"]] for x in tabela_letov])
        ##celoten cas potovanja
        pom = [sum([let["duration"] for let in x["flights"]]) for x in tabela_letov]
        zdr = [x + y for x, y in zip(self._tabela_primerjanj[1], pom)]
        self._tabela_primerjanj.insert(1, list(zdr))
        ##karbonske emisije
        self._tabela_primerjanj.append([x["carbon_emissions"]["this_flight"] for x in tabela_letov])

    @staticmethod
    def pridobi_lete(iz, kam, datum_tja, datum_nazaj = ""):
        """funkcija, ki sprejme letalisce iz katerega gremo, letalisce v katerega hocemo prispeti, cas odhoda ko gremo tja in cas odhoda
        ko gremo nazaj. iz (letalisce iz katerega gremo) je lahko tudi tabela vecih letalisc.
        """
        key = "9aa8f07a4838c4c78081cbafe35b26cd7389b628269b05fe8304a3e55f902c47"
        leti = []

        if type(iz) == str:
            iz = [iz]

        for iz_i in iz:
            params = {
                "type" : 2,
                "engine": "google_flights",
                "departure_id": iz_i,
                "arrival_id": kam,
                "outbound_date": datum_tja,
                "currency": "EUR",
                "hl": "en",
                "api_key": key
            } 
            if datum_nazaj != "":
                params["type"] = 1
                params["return_date"] = datum_nazaj
            search = GoogleSearch(params)
            results = search.get_json()
            leti = leti + results["best_flights"] + results["other_flights"]
        return leti




    def najbolsi_let(self, iz, kam, datum_tja, datum_nazaj = 0, n = 1):
        """vrne n najbolsih letov v urejenem seznamu (urejen po oceni nasih preferenc)"""
        try:
            tabela_letov = izbiralec_letov.pridobi_lete(iz, kam, datum_tja, datum_nazaj)
        except: #zalomi se ce ne najde letov zato vrnemo prazen seznam
            return []

        self._kreiranje_tabele_primerjanj(tabela_letov)
        prefs = self.get_preferenca()
        st_vseh_opcij = len(tabela_letov)
        ocene = [0]*st_vseh_opcij

        #more biti toliko kolikor je kljucev v preferencah
        if prefs["cena"] > 0:
            ocene = self._oceni_ceno(ocene, st_vseh_opcij)
        if prefs["celoten cas"] > 0:
            ocene = self._oceni_celoten_cas(ocene, st_vseh_opcij)
        if prefs["cas v zraku"] > 0:
            ocene = self._oceni_cas_v_zraku(ocene, st_vseh_opcij)
        if prefs["cas med leti"] > 0:
            ocene = self._oceni_cas_med_leti(ocene, st_vseh_opcij)
        if prefs["karbonske emisije"] > 0:
            ocene = self._oceni_karbonske_emisije(ocene, st_vseh_opcij)

        naj_leti = []
        sort_ocene = sorted(ocene, reverse=True)
        print(ocene)
        print(sort_ocene)
        #pridobimo najbolse lete
        for ocena in sort_ocene[0:n]:
            i = 0
            while i < len(ocene):
                if ocene[i] == ocena:
                    naj_leti.append(tabela_letov[i])
                    break
                i += 1

        return naj_leti
        

    def _oceni_ceno(self, ocene, st_vseh_opcij):
        """funkcija, ki prejme ocene in jih posodobi z oceno glede nasih preferenc cene"""
        tabela_primerjanj = self._tabela_primerjanj
        minv = min(tabela_primerjanj[0])
        maxv = max(tabela_primerjanj[0])
        i = 0
        while i < st_vseh_opcij:
            ocene[i] += f.linearen_utility(tabela_primerjanj[0][i], minv, maxv) * self.get_preferenca()["cena"]
            i += 1
        return ocene
    
    def _oceni_celoten_cas(self, ocene, st_vseh_opcij):
        """funkcija, ki prejme ocene in jih posodobi z oceno glede nasih preferenc celotenga casa letenja"""
        tabela_primerjanj = self._tabela_primerjanj
        minv = min(tabela_primerjanj[1])
        maxv = max(tabela_primerjanj[1])
        i = 0
        while i < st_vseh_opcij:
            ocene[i] += f.linearen_utility(tabela_primerjanj[1][i], minv, maxv) * self.get_preferenca()["celoten cas"]
            i += 1
        return ocene
    
    def _oceni_cas_v_zraku(self, ocene, st_vseh_opcij):
        """funkcija, ki prejme ocene in jih posodobi z oceno glede nasih preferenc casa letenja (ko smo v zraku)"""
        tabela_primerjanj = self._tabela_primerjanj
        minv = min(tabela_primerjanj[2])
        maxv = max(tabela_primerjanj[2])
        i = 0
        while i < st_vseh_opcij:
            ocene[i] += f.linearen_utility(tabela_primerjanj[2][i], minv, maxv) * self.get_preferenca()["cas v zraku"]
            i += 1
        return ocene
    
    def _oceni_cas_med_leti(self, ocene, st_vseh_opcij):
        """funkcija, ki prejme ocene in jih posodobi z oceno glede nasih preferenc casa med leti"""
        tabela_primerjanj = self._tabela_primerjanj
        odklon = math.sqrt(-(self.get_ZadnjaKulUra() - 3)**2 / (2 * math.log(0.01)))
        i = 0
        while i < st_vseh_opcij:
            st_prestopov = len(tabela_primerjanj[3][i])
            for cas in tabela_primerjanj[3][i]:
                ocene[i] += (f.cas_prestopanja(cas, odklon = odklon) * self.get_preferenca()["cas med leti"])/st_prestopov
            i += 1
        return ocene
        
    def _oceni_karbonske_emisije(self, ocene, st_vseh_opcij):
        """funkcija, ki prejme ocene in jih posodobi z oceno glede nasih preferenc o karbonkih emisijah letal"""
        tabela_primerjanj = self._tabela_primerjanj
        minv = min(tabela_primerjanj[4])
        maxv = max(tabela_primerjanj[4])
        i = 0
        while i < st_vseh_opcij:
            ocene[i] += f.linearen_utility(tabela_primerjanj[4][i], minv, maxv) * self.get_preferenca()["karbonske emisije"]
            i += 1
        return ocene
    