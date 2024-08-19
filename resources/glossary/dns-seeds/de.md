---
term: DNS SEEDS
---

Initiale Verbindungspunkte für neue Bitcoin-Knoten, die dem Netzwerk beitreten. Diese Seeds, die tatsächlich spezifische DNS-Server sind, haben ihre Adresse dauerhaft im Bitcoin Core-Code eingebettet. Wenn ein neuer Knoten startet, kontaktiert er diese Server, um eine zufällige Liste von IP-Adressen vermutlich aktiver Bitcoin-Knoten zu erhalten. Der neue Knoten kann dann Verbindungen mit den Knoten auf dieser Liste herstellen, um die Informationen zu erhalten, die benötigt werden, um seinen Initial Block Download (IBD) durchzuführen und mit der Kette zu synchronisieren, die die meiste akkumulierte Arbeit hat. Stand 2024, hier ist die Liste der Bitcoin Core DNS-Seeds und die Personen, die für ihre Wartung verantwortlich sind (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS-Seeds sind die zweite Methode, in der Reihenfolge der Priorität, für einen Bitcoin-Knoten, um Verbindungen herzustellen. Die erste Methode beinhaltet die Verwendung der Datei peers.dat, die der Knoten selbst erstellt hat. Diese Datei ist natürlich leer im Fall eines neuen Knotens, es sei denn, der Benutzer hat sie manuell modifiziert.

> ► *Hinweis, DNS-Seeds sollten nicht mit "Seed-Knoten" verwechselt werden, die die dritte Art sind, Verbindungen herzustellen.*