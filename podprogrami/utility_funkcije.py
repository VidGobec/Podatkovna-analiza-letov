import math

def linearen_utility(cena, min, max):
    """linarno padajoca funkcija"""
    return 1 - (cena - min) / (max - min)

def cas_prestopanja(prestopanje, ideal = 3, odklon = 8):
    """funkcija ki je 0 za ure < 2 povsod drugje pa je gavsovo porazdeljena z srediscem v 3 (najvecja vrednost je 1)"""
    prestopanje = prestopanje/60 #pretvorba v ure
    if prestopanje < 2:
        return 0

    return math.exp(-(pow((prestopanje - ideal),2)) / (2 * pow(odklon,2)))