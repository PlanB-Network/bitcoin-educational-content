---
term: Dns seeds
definition: DNS-servers die IP-adressen van actieve nodes verstrekken aan nieuwe nodes die zich aansluiten bij het Bitcoin-netwerk.
---

Initiële verbindingspunten voor nieuwe Bitcoin knooppunten die zich bij het netwerk aansluiten. Deze seeds, die eigenlijk specifieke DNS servers zijn, hebben hun Address permanent ingebed in de Bitcoin core code. Wanneer een nieuw knooppunt start, neemt het contact op met deze servers om een willekeurige lijst van IP-adressen van vermoedelijk actieve Bitcoin knooppunten te verkrijgen. Het nieuwe knooppunt kan dan verbindingen maken met de knooppunten op deze lijst om de informatie te verkrijgen die nodig is om zijn Initial Block Download (IBD) uit te voeren en te synchroniseren met de keten die het meeste werk heeft geaccumuleerd. Vanaf 2024 is dit de lijst van Bitcoin core DNS seeds en de personen die verantwoordelijk zijn voor het onderhoud ervan (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.Bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.Bitcoin.dashjr-lijst-van-P2P-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.Bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.Bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.Bitcoin.wiz.biz: Jason Maurice;
- seed.Mainnet.achownodes.xyz: Ava Chow.


DNS seeds zijn de tweede methode, in volgorde van prioriteit, voor een Bitcoin knooppunt om verbindingen tot stand te brengen. De eerste methode maakt gebruik van het bestand peers.dat dat het knooppunt zelf heeft aangemaakt. Dit bestand is natuurlijk leeg in het geval van een nieuw knooppunt, tenzij de gebruiker het handmatig heeft aangepast.


> opmerking: DNS seeds moeten niet verward worden met "seed nodes", die de derde manier zijn om verbindingen tot stand te brengen