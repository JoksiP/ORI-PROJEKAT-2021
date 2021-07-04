# ORI-PROJEKAT-2021

Članovi tima:
* Petljanski Jovan SW-31/2018, grupa 2

Asistenti:
* Aleksandar Lukić

## Opis projekta

Problem koji se rešava:<br/>
Treniranje agenta da preskače prepreke na putu

Algoritam:<br/>
NEAT - Neuroevolution of augmenting topologies

Dataset:<br/>
Agent u PyGame okruženju koji se pomera na desno i može u svakom trenutku da skoči. Potrebno ga je istrenirati NEAT algoritmom da preskoči nasumične prepreke na koje naiđe na putu.

Metrika za merenje performansi:<br/>
Fitness funkcija za evaluaciju najboljeg gena svake generacije. Metrika je totalni score dobijen, koji je ekvivalentan totalnoj distanci koju agent pređe od početka igre. Svaka kolizija sa preprekom se vodi kao negativna vrednost u fitness funkciji.

Validacija rešenja:<br/>
Validnost rešenja je merena fintess funkcijom. Rešenje je dobro, odnosno agent se dobro ponašao ako je vrednost funkcije velika.

## Pokretanje projekta

Pre nego što se pokrene projekat potrebno je instalirati Python 3.8 i izvršiti sledeće komande:<br/>
```
  pip install setuptools
  pip install pygame
  pip install neat-python
```
Nakon uspešne instalacije i pokretanja komandi projekat možete pokrenuti preko main.py fajla.<br/>
<br/>
Na prozoru možete videti agenta sa leve strane (mačka), i prepreke koje nailaze sa desne strane.<br/>
U donjem delu prozora nalaze se totalni rezultat (Score), generacija (Generation), preostala populacija (Population) i vreme koje je prošlo od početka simulacije (Elapsed).<br/>
<br/>
Takođe simulaciju je moguće privremeno zaustaviti pritiskom tastera *Esc* i istim je nastaviti.<br/>
<br/>
Nakon izvršavanja simulacija ili zatvaranjem prozora na dugme *X* rezultate simulacija možete videti na putanji **output->logs.txt**, gde je za svaku pojedinacnu<br/>
generaciju naveden rezultat (Score) najboljeg gena.
