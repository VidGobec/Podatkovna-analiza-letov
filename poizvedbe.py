


class poizvedbe():
    def __init__(self, json):
          self._data = json
          pass
     
    def get_data(self):
         return self._data

    @staticmethod
    def _get_element(iskan, slovar):
        """prejme tabelo nizov iskan in slovar in vrne vrednost vrednosti shranjeno pod kljucem iskan.
        tabela kljucov je sestavljena iz kljucev gnezdenih slovarjev, kjer je prvi element tabele najbolj zunanji kljuc slovarja
        """
        if len(iskan)>1:
             return poizvedbe._get_element(iskan[1:], slovar[iskan[0]])
        return slovar[iskan[0]]
            
              

    def get_grouped_data(self, sortiran_po):
        """
        prejme tabelo nizov kljucev in vrne slovar kjer so kljuc grupirani po zadnjem elementu v prijeti tabeli vrednosti pa so podatki, ki imajo isto vrednost, po katerem grupiramo
        primer get_grouped_data(["flight_status"]) vrne slovar kjer so kljuci vrednosti data["flight_status"] vrednosti je tabela slovarjev, ki imajo enak flight status
        """
        slovar = dict()
        for element in self.get_data():
            kljuc = poizvedbe._get_element(sortiran_po, element)
            if kljuc == None:
                Kljuc = "None"
            if kljuc in slovar:
                slovar[kljuc].append(element)
            else:
                slovar[kljuc] = [element]

        return slovar
                                
    @staticmethod
    def get_pristali(json):
        """prejme json z podatki letov, in vrne vse lete, ki so že pristali"""
        return [x for x in json if x["flight_status"]=="landed" ]
    @staticmethod
    def get_zamudniki(json):
        """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob pristanku in odhodu"""
        return [x for x in json if x["arrival"]["delay"] is not None and x["arrival"]["delay"]>0 and x["departure"]["delay"] is not None and x["departure"]["delay"]>0]
    @staticmethod
    def get_zamudniki_ob_pristaneku(json):
            """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob pristanku"""
            return [x for x in json if x["arrival"]["delay"] is not None and x["arrival"]["delay"]>0]
    @staticmethod
    def get_zamudniki_ob_odhodu(json):
            """prejme json z podatki letov, in vrne vse lete, ki so imeli zamudo ob odhodu"""
            return [x for x in json if x["departure"]["delay"] is not None and x["departure"]["delay"]>0]
    

         

    @staticmethod
    def get_vrednosti(json, tab_kljucev):
        """prejme json z podatki letov in tabela kljucev gnezdenega slovarja, kjer je prvi element najbolj zunanji kljuc.
        Vrne tabelo elementov, kamor kazejo vneseni kljuci
        """
        #try:
        return [poizvedbe._get_element(tab_kljucev, x) for x in json]
        #except:
            #return None





