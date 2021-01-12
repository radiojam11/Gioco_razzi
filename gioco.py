# i moduli sono i file che contengono le classi o anche le funzioni (vedi multiplying)
from navicelle import *
from funzioni import *

 

#flottaR=[NavRossa(n="NavicellaX01R")]
#flottaN=[NavNera(n="NavicellaX01N")]

#crea_flotte()
"""
for el in flottaR:
      print("Navicella ",el.name,"Posizione X ",el.x,"Posizione Y ",el.y,"Livello Propellente ", el.propeller, "Velocita ",el.speed, "Power", el.power, "radar", el.radar, "Spy ", el.spy,"\nTrasmissioni ", el.trx, "esperienza ", el.esperienza, "Missioni ", el.missioni, "Squadra ", el.squadra )
for el in flottaN:
      print(el.name, el.propeller)

flottaR[0].move()
flottaN[0].move_rocket(2,3)

print("Navicella ",flottaR[0].name,"Posizione X ",flottaR[0].x,"Posizione Y ",flottaR[0].y,"Livello Propellente ", flottaR[0].propeller)
print(flottaR[0].name,flottaN[0].x, flottaN[0].y, flottaN[0].propeller)
for el in flottaN:
    el.move()
    print("Nav ", el.name)
    el.controllo_carb()

"""
#SSB_R = (StazioneSpaziale(n="SSB_R",squadra = "Rossa", x=0, y=100))
#SSB_N = (StazioneSpaziale(n="SSB_N",squadra="Nera", x=100, y=100))
inizia_gioco()
for el in flottaN:
    el.move()
    print(el.name, el.x, el.y)

aggiorna_areaGioco()
for el in flottaN:
    el.safety_check(areaGioco)
print(areaGioco)
