import matplotlib.pyplot as plt
from poizvedbe import poizvedbe
import json
import os
import geopandas
import geodatasets

def graf_povpzamuda_na_letalisce():
    ##graf letalisc in povprecnih zamud na letalisce
    pot = os.path.join('Podatki', 'podatki_svet.json')
    with open(pot, 'r') as file:
        data = poizvedbe(json.load(file))
    pot = os.path.join('Podatki', 'vsa_letalisca.json')
    with open(pot, 'r') as file:
        data_letalisa = json.load(file)

    data_po_letaliscih = data.get_grouped_data(["departure","airport"])
    tabela_zamud_po_letaliscih = []
    for letalisce, leti in data_po_letaliscih.items():
        zamudniki = poizvedbe.get_zamudniki_ob_odhodu(leti)
        vsota_zamud = sum([x["departure"]["delay"] for x in zamudniki])
        povp_zamuda = vsota_zamud/len(leti)

        try:
            tabela_zamud_po_letaliscih.append([[float(x["longitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                        [float(x["latitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                        povp_zamuda])
        except:
            pass

    #print(tabela_zamud_po_letaliscih) 
    #graf gostote zamujanja po letaliscih

    fig, ax = plt.subplots()
    plt.close('all') #cudn popravek da zapre ekstra okenjce ki ga subplots odpre avtomatsko

    #background
    path = geodatasets.get_path("naturalearth.land")
    df = geopandas.read_file(path)
    ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")

    #foregtound
    tab_x = [x[0] for x in tabela_zamud_po_letaliscih]
    tab_y = [x[1] for x in tabela_zamud_po_letaliscih]
    skalar = 30 #za povecavo poprecja zamud na grafu
    tab_povpzamuda = [x[2]*skalar for x in tabela_zamud_po_letaliscih]

    ax.scatter(tab_x, tab_y, s=tab_povpzamuda, c="red", alpha = 0.3,edgecolors=None)
    ax.scatter(tab_x, tab_y, s=15, c="blue")


    plt.show()

