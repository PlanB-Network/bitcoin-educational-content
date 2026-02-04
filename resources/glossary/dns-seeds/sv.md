---
term: Dns seeds
definition: DNS-servrar som tillhandahåller IP-adresser för aktiva noder till nya noder som ansluter till Bitcoin-nätverket.
---

Initiala anslutningspunkter för nya Bitcoin-noder som ansluter till nätverket. Dessa seed, som faktiskt är specifika DNS-servrar, har sin Address permanent inbäddad i Bitcoin-kärnkoden. När en ny nod startar kontaktar den dessa servrar för att få en slumpmässig lista med IP-adresser till förmodat aktiva Bitcoin-noder. Den nya noden kan sedan upprätta förbindelser med noderna på den här listan för att få den information som behövs för att utföra sin IBD (Initial Block Download) och synkronisera med den kedja som har mest ackumulerat arbete. Från och med 2024 finns här en lista över Bitcoin Core DNS seeds och de personer som ansvarar för underhållet av dem (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.Bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.Bitcoin.dashjr-lista-över-P2P-noder.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.Bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.Bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.Bitcoin.wiz.biz: Jason Maurice;
- seed.Mainnet.achownodes.xyz: Ava Chow.


DNS seeds är den andra metoden, i prioritetsordning, för en Bitcoin-nod att upprätta anslutningar. Den första metoden innebär att man använder filen peers.dat som noden själv har skapat. Denna fil är naturligtvis tom när det gäller en ny nod, såvida inte användaren manuellt har ändrat den.


> dNS-frön ska inte förväxlas med "seed-noder", som är det tredje sättet att upprätta anslutningar