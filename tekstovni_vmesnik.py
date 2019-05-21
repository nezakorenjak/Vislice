import model

# Generiramo izpise za igralca

def izpis_igre(igra):
    tekst = (
        '=====================================\n\n'
        '    {trenutno_stanje}\n\n'
        'Neuspešni poskusi: {poskusi}\n\n'
        '====================================='
    ).format(trenutno_stanje=igra.pravilni_del_gesla(), \
    poskusi=igra.nepravilni_ugibi())

def izpis_zmage(igra):
    return 'Pravilno ste uganili geslo {}!'.format(igra.geslo)

def izpis_poraza(igra):
    return 'Žal ste izgubili.'


# Izvajanje vmesnika

def zahtevaj_vnos():
    x = input('Ugibaj: ')
    return x

def preveri_vnos():
    if len(vnos) != 1:
        print('Neveljaven vnos: vnesi samo 1 črko.')
        return False
    else:
        return True

        # Če boš preveril ali je to sploh črka, potem vnesi 
        # abecedo kar v model kot konstanto.

def pozeni_vmesnik():
    
    igra = model.nova_igra()

    while True:
        # izpišemo stanje:
        print(izpis_igre(igra))
        # igralec ugiba
        poskus = zahtevaj_vnos()
        if not preveri_vnos(poskus):
            continue #preskoči preostanek zanke

        rezultat = ugibaj(igra, poskus)
        #preverimo, če je konec
        if igra.poraz(): 
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return

#Zares poženi igro:
pozeni_vmesnik()