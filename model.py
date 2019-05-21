# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

# Definiramo logični model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() # string
        self.crke = crke # list
        return
    
    def napacne_crke(self):
        sez = []
        for crka in self.crke:
            if crka not in self.geslo:
                sez.append(crka)
        return sez

    def pravilne_crke(self):
        sez = []
        for crka in self.crke:
            if crka in self.geslo:
                sez.append(crka)
        return sez

    def stevilo_napak(self):
        return len(self.napacne_crke()) 

    def zmaga(self):
        if self.poraz():
            return False #načeloma se to ne zgodi
        
        for crka in self.geslo:
            if crka not in self.pravilne_crke():
                return False
        return True
    
    def poraz(self):
        return len(self.napacne_crke()) > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                niz += ' ' + crka
            else:
                niz += ' _'
        return niz.strip() #počistimo presledke, če lahko
    
    def nepravilni_ugibi(self):
        return self.napacne_crke().join(', ')

    # ne briši presledkov z niz[:-1], raje s strip(), da ne
    # nastane prazen niz in morda sesuje serverja
    
    def ugibaj(self, crka):
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

    # izluščimo slovenske besede

bazen_besed = []

with open('besede.txt', 'r', encoding='utf-8') as besede:
    for beseda in besede.readlines():
        bazen_besed.append(beseda.upper().strip())

    # Funkcije za generiranje iger

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

            

class Vislice:

    def __init__(self):
        self.igre = {} 
        
        # V slovarju igre ima vsaka igra svoj ID
        # ID je celo število
        return

    def prost_id_igre(self):
        if not self.igre:     # torej če je prazen
            return 0
        else:
            # Preverimo, katero od prvih n+1 števil še ni
            # uporabljeno za id n iger
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i 

    def nova_igra(self):
        
        igra = nova_igra()
        id = self.prost_id_igre()
        self.igre[id] = (igra, ZACETEK)
        return id

    def ugibaj(self, id_igre, crka):
        
        # Pridobi igro
        (igra, _) = self.igre[id_igre]  # _ tisto stran vrže, ne
                                        # moreš po nesreči spet uporabit
        #Ugibaj
        nov_poskus = igra.ugibaj(crka)
        
        self.igre[id_igre] = (igra, nov_poskus)



        
        # naredi novo igro z naključnim geslom
    