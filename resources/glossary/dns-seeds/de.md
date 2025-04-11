---
term: DNS-SEEDS

---
Erste Verbindungspunkte für neue Bitcoin-Knoten, die dem Netzwerk beitreten. Diese Seeds, die eigentlich spezielle DNS-Server sind, haben ihre Adresse dauerhaft in den Bitcoin Core Code eingebettet. Wenn ein neuer Knoten startet, kontaktiert er diese Server, um eine zufällige Liste von IP-Adressen von vermutlich aktiven Bitcoin-Knoten zu erhalten. Der neue Knoten kann dann Verbindungen mit den Knoten auf dieser Liste herstellen, um die Informationen zu erhalten, die er benötigt, um seinen Initial Block Download (IBD) durchzuführen und sich mit der Kette zu synchronisieren, die die meiste Arbeit angesammelt hat. Ab 2024 ist hier die Liste der Bitcoin Core DNS Seeds und der Personen, die für ihre Wartung verantwortlich sind (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

DNS-Seeds sind die zweite Methode, in der Reihenfolge der Priorität, für einen Bitcoin-Knoten, um Verbindungen herzustellen. Bei der ersten Methode wird die Datei peers.dat verwendet, die der Knoten selbst erstellt hat. Diese Datei ist im Falle eines neuen Knotens natürlich leer, es sei denn, der Benutzer hat sie manuell geändert.

> dNS-Seeds sind nicht zu verwechseln mit "Seed Nodes", die die dritte Möglichkeit zum Verbindungsaufbau darstellen