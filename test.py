svet_iata = ["JFK", "DXB", "HND", "LHR", "IST", "DEL", "PVG", "LAX", "ICN", "CDG", "SIN", "PEK", "MAD", "AMS", "FRA", "BKK", "KUL", "DOH", "FCO", "YYZ", "GRU", "SGN", "MNL", "MEX", "SYD", "ATL", "BOM", "BOG", "CGK", "JED", "GRU", "DFW", "CAI", "ORD", "SCL", "JNB", "TPE", "AKL"]

niz = ""

for letalisce in svet_iata:
    niz += letalisce + ","

print(niz[:-1])
"JFK,DXB,HND,LHR,IST,DEL,PVG,LAX,ICN,CDG,SIN,PEK,MAD,AMS,FRA,BKK,KUL,DOH,FCO,YYZ,GRU,SGN,MNL,MEX,SYD,ATL,BOM,BOG,CGK,JED,GRU,DFW,CAI,ORD,SCL,JNB,TPE,AKL"