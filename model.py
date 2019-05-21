# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

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
        return len(napacne_crke(self))

    def zmaga(self):
        if self.poraz:
            return False #načeloma se to ne zgodi
        
        for crka in self.geslo:
            if crka not in pravilne_crke(self):
                return False
        return True
    
    def poraz(self):
        return len(napacne_crke(self)) > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in pravilne_crke(self):
                niz += ' ' + crka
            else:
                niz += ' _'
        return niz.strip() #počistimo presledke, če lahko
    
    def nepravilni_ugibi(self):
        return napacne_crke(self).join(', ')

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

            