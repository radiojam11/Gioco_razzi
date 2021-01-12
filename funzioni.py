from navicelle import *
from funzioni import *

 
def crea_flotte(nav=5, codici="Y,W,Z,X,Q,Z,T,K" ):  #passare optional nav=(numero delle navicelle della flotta) codici=" lettere divise da virgola tante quante nav + 3"
      lista = codici.split(",")
      if nav < len(lista):
            x = len(lista)
            for i in range((nav - x)+3):
                  lista.append(Q)
      for i in range(nav) :
            flottaR.append(Navicella(n="Navicella"+ lista[i] + "0" + str(i+1) + "R", squadra = "Rossa"))
            flottaN.append(Navicella(n="Navicella"+ lista[i+1] + "0" + str(i+1) + "N", squadra = "Nera"))
      stazioni.append(StazioneSpaziale(n="SSB_R",squadra = "Rossa", x=0, y=100))
      stazioni.append(StazioneSpaziale(n="SSB_N",squadra="Nera", x=100, y=100))
      stazioni.append(StazioneSpaziale(n="SSR", x= randint(2,99), y=randint(2,99)))
     

def aggiorna_areaGioco():
  for navN in flottaN:
        areaGioco[navN.name] = [navN.x, navN.y]
  for navR in flottaR:
        areaGioco[navR.name] = [navR.x, navR.y]
  for staz in stazioni:
        areaGioco[staz.name] = [staz.x, staz.y]
  


def inizia_gioco():
      #funzione che inizializza il gioco crea le flotte di n navicelle, e popola l'area di gioco con  le SSB, la SSR e gli eventuali handicap
      crea_flotte()

      aggiorna_areaGioco()

       