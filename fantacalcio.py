
def main():
    file = 'fantacalcio.txt'
    tabella_giocatori = leggi_file(file) # funzione che restituisce tabella
    ruoli = separa_dati_tabella(tabella_giocatori) # lista dei giocatori separati per ruolo

    portieri = ruoli[0]
    riordina_quotazioni(portieri)
    difensori = ruoli[1]
    riordina_quotazioni(difensori)
    centrocampisti = ruoli[2]
    riordina_quotazioni(centrocampisti)
    attaccanti = ruoli[3]
    riordina_quotazioni(attaccanti)

    forma_squadra(portieri, difensori,centrocampisti,attaccanti)




def leggi_file(file):

    infile = open(file, 'r')

    giocatori = [] # creo la tabella che raccoglie info su giocatori; ogni riga == un giocatore
    for line in infile:
        giocatore = line.rstrip() # tolgo il carattere di a capo

        info = giocatore.split(',') # 0-nome, 1-squadra, 2-ruolo, 3-quotazione(int)


        pulisci_stringhe(info) # pulisco le stringhe che contiene la lista
                                    # voglio togliere caratteri inutili (x es. ' ')
        info[3] = int(info[3]) # converto la sringa che rappresenta la quotazione in intero

        giocatori.append(info)

    return giocatori

    infile.close()

def separa_dati_tabella(tabella):
    portieri = []
    difensori = []
    centrocampisti = []
    attaccanti = []

    for calciatore in tabella:
        ruolo = calciatore[2]

        if ruolo == 'portiere':
            portieri.append(calciatore)
        elif ruolo == 'difensore':
            difensori.append(calciatore)
        elif ruolo == 'centrocampista':
            centrocampisti.append(calciatore)
        elif ruolo == 'attaccante':
            attaccanti.append(calciatore)
    ruoli = [portieri, difensori,centrocampisti,attaccanti]
    return ruoli

def pulisci_stringhe(lista): # funzione che toglie i caratteri di spazio dalle stringhe di una lista

    i = 0 # indice che mi serve per indicare la posizione della stringa nella lista
    for stringa in lista:
        stringa_pulita = ''

        for carattere in stringa:
            if carattere != ' ':
                stringa_pulita = stringa_pulita + carattere
        lista[i] = stringa_pulita
        i = i + 1
    return lista

def riordina_quotazioni(tabella):

    quotazioni = [] # creo una lista con i valori delle quotazioni messe in ordine
    for giocatore in tabella:
        quotazione = giocatore[3]
        quotazioni.append(quotazione)
    quotazioni.sort(reverse=True)

    calciatori_ordinati = []
    for numero in quotazioni:
        for  giocatore in  tabella:
            if giocatore[3] == numero:
                calciatori_ordinati.append(giocatore)
    return


def forma_squadra(portieri, difensori,centrocampisti,attaccanti):



    budget_tot = 260
    budget_portieri = 20
    budget_difensori = 40
    budget_centrocampisti = 80
    budget_attaccanti = 120

    num_portieri_da_acquistare = 3
    for portiere in portieri:
        quotazione = portiere[3]
        if quotazione<=20 and budget_portieri>=num_portieri_da_acquistare:
            pass



main()
