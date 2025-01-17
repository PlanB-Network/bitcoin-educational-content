---
term: DNS SEEDS

---
De første tilkoblingspunktene for nye Bitcoin-noder som blir med i nettverket. Disse seedene, som faktisk er spesifikke DNS-servere, har adressen sin permanent innebygd i Bitcoin Core-koden. Når en ny node starter, kontakter den disse serverne for å få en tilfeldig liste over IP-adresser til antatt aktive Bitcoin-noder. Den nye noden kan deretter opprette forbindelser med nodene på denne listen for å innhente informasjonen som trengs for å utføre sin Initial Block Download (IBD) og synkronisere med den kjeden som har mest akkumulert arbeid. Her er listen over Bitcoin Core DNS-frø og personene som er ansvarlige for vedlikeholdet av dem (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


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

DNS-frø er den andre metoden, i prioritert rekkefølge, for en Bitcoin-node for å etablere forbindelser. Den første metoden innebærer å bruke peers.dat-filen som noden selv har opprettet. Denne filen er naturlig nok tom når det gjelder en ny node, med mindre brukeren har endret den manuelt.

> dNS-frø må ikke forveksles med "frø-noder", som er den tredje måten å opprette forbindelser på