"""
Le Navicelle hanno di base queste caratteristiche:
Posizione x e y (def 0, 0)
Un nome n (default NavicellaTipo)
Velocita' speed (def 5)
Potenza in combattimento power (def 5) da implementare 
Radar per conoscere in anticipo la posizione (relativa ed assoluta?) del nemico e degli ostacoli radar (def False)
Spionaggio consente di conoscere con approssimazione le mosse del nemico - ma attenti alle spie doppiogiochiste spy (def False) #da sviluppare
Carburante che si consuma ogni azione e si rifornisce in casa o su Stazione Spaziale Rifornimento SSR propeller (def 10)
Capacita' di comunicazione trx(def False)
Esperienza - si acquisisce esperienza durante le missioni, l'esperienza favorisce in alcune fasi del gioco (in battaglia, in viaggio, in spionaggio)

Funzioni di base:
move() sposta la Navicella di una posizione casuale in un raggio massimo  di 4 caselle ma consuma solo 2 di Carburante 
muovi_dove() sposta la Navicella di alcune posizioni passate come parametro - la funzione consuma Carburante pari a (x*y)
crea_flotte() crea due flotte di 5 Navicelle - si puo aumentare la quantita' di Navicelle passando un numero intero come parametro alla funzione
creo_ostacoli()
controllo_carb() controlla lo stato del carburante e stampa allert se  < 3 cioe' riserva.

Obiettivi:
Arrivare a conquistare la Home dell'altra flotta, e proteggere la propria dal nemico

"""

from math import sqrt
from random import randint
areaGioco={} #dizionario che registra tutte le posizioni degli elementi in gioco in questo formato{nomeElemento:[x,y]}
flottaR=[]
flottaN=[]
stazioni=[]
class SpaceElement():
  def __init__(self, x=0, y=0, n="NavicellaTipo", speed=5, power=0, radar=False, spy=False, propeller=10, trx=False, exp=0):
    self.x = x
    self.y = y
    self.name = n
    self.speed= speed
    self.power = power
    self.radar=radar
    self.spy=spy
    self.propeller=propeller
    self.trx=trx
    self.esperienza=exp


  def move(self):
    self.y += randint(1,5) #si puo' anche pensare ad uno spostamento negativo !
    self.x += randint(1,5)
    self.consumo(2)

  def move_rocket(self, x_increment=0,y_increment=0):
    self.x += x_increment
    self.y += y_increment
    self.consumo( 1*(self.x * self.y) )
  
  def consumo(self,p):
    self.propeller -= p

  def controllo_carb(self):
    if self.propeller < 3:
      print(f"ALLERT! Hai solo {self.propeller} di propellente, considera di tornare alla Base per i rifornimenti")
    elif self.propeller == 1:
       print("puoi solamente tornare alla Base o aspettare rifornimenti")
    else:
      print(f"Carburante ancora disponibile: {self.propeller}")


  def get_distance(self, pos):
    a = abs(self.x - pos[0])                      #controllare se funziona riceve per es. [4:6]
    b = abs(self.y - pos[1])
    distance = sqrt(a**2+b**2)
    return distance

  def lunch(self):
    print( f"La Navicella {self.name} e' partita.....! \n\t Buon Volo")

  def safety_check(self, areaGioco):
    for el in areaGioco:
      distance = self.get_distance(areaGioco(el))
      if distance == 0:
        print("Danger!! CRASH")
      elif distance<2:
        print("Attenzione sei Troppo vicino a ", el)
      elif 3 < distance < 5:
        print("Puoi ancora navigare o ingaggiare battaglia con ",el, " che si trova a ", distance, "di distanza") 
      else:
        print("Tutto bene volo sereno!")

  def land_nav(self):
    self.y = 0
    self.consumo(1)
    #self.x = 0
  
class StazioneSpaziale(SpaceElement):
      def __init__(self, x=0, y=0, n="Stazione Spaziale Neutra", speed=0, power=1000, radar=True, spy=False, propeller=1000, trx=True, exp=10, missioni=0, squadra="Neutra", pattracco=4):
            super().__init__(x, y, n, speed, power, radar, spy, propeller, trx, exp)
            self.missioni = missioni
            self.squadra = squadra
            self.posti_attracco = pattracco


class Navicella(SpaceElement):
  def __init__(self, x=0, y=0, n="NavicellaTipo", speed=5, power=0, radar=False, spy=False, propeller=10, trx=False, exp=0, missioni=0, squadra="Neutra"):
    super().__init__(x, y, n, speed, power, radar, spy, propeller, trx, exp)
    self.missioni = missioni
    self.squadra = squadra
  def atterra(self):
    #qui riscrivo lo stesso metodo della classe super (overriding) con calcoli modificati come
    self.y = 0
    self.x = 0
    self.missioni += 1
    print(f"{self.name} e' atterrato, ha completato {self.missioni} missioni")

     
  