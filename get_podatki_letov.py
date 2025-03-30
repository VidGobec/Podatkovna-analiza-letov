import json

with open('podatki_svet.json', 'r') as file:
    data = json.load(file)



def get_pristali(json):
    """prejme json z podatki letov, in vrne vse lete, ki so že pristali"""
    return [x for x in json if x["flight_status"]=="landed" ]

def get_zamudniki(json):
    """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob pristanku in odhodu"""
    return [x for x in json if x["arrival"]["delay"] is not None and x["arrival"]["delay"]>0 and x["departure"]["delay"] is not None and x["departure"]["delay"]>0]

def get_zamudniki_ob_pristaneku(json):
        """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob pristanku"""
        return [x for x in json if x["arrival"]["delay"] is not None and x["arrival"]["delay"]>0]

def get_zamudniki_ob_odhodu(json):
        """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob odhodu"""
        return [x for x in json if x["departure"]["delay"] is not None and x["departure"]["delay"]>0]


#mogoce premakni v drug file
def povp_vrednost(tabela):
    """vrne povprecno vrednost stevil v tabeli"""
    return sum(tabela)/len(tabela)

##tests
pristali = get_pristali(data)
#print(pristali[0],"\n", pristali[1])
zamudniki = get_zamudniki(pristali)
#print(zamudniki[0])
print("ce gledamo vse lete v podatki_svet")
zamudniki_ob_pristanku = get_zamudniki_ob_pristaneku(data)
povp = povp_vrednost([x["arrival"]["delay"] for x in zamudniki_ob_pristanku])
print(f"povp vrednost zamude letal v odhodu je {povp}")

zamudniki_ob_odhodu = get_zamudniki_ob_odhodu(data)
povp = povp_vrednost([x["departure"]["delay"] for x in zamudniki_ob_odhodu])
print(f"povp vrednost zamude letal v prihodu je {povp}")

##
print("\nce gledamo le pristale lete v podatki_svet\n")
print("ce gledamo vse lete v podatki_svet")
zamudniki_ob_pristanku = get_zamudniki_ob_pristaneku(pristali)
povp = povp_vrednost([x["arrival"]["delay"] for x in zamudniki_ob_pristanku])
print(f"povp vrednost zamude letal v odhodu je {povp}")

zamudniki_ob_odhodu = get_zamudniki_ob_odhodu(pristali)
povp = povp_vrednost([x["departure"]["delay"] for x in zamudniki_ob_odhodu])
print(f"povp vrednost zamude letal v prihodu je {povp}")