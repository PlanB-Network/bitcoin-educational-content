---
term: DNS SEEDS
---

Početne tačke povezivanja za nove Bitcoin čvorove koji se pridružuju mreži. Ovi seed-ovi, koji su zapravo specifični DNS serveri, imaju svoj Address trajno ugrađen u Bitcoin Core kod. Kada novi čvor započne, kontaktira ove servere kako bi dobio nasumičnu listu IP adresa verovatno aktivnih Bitcoin čvorova. Novi čvor tada može uspostaviti veze sa čvorovima na ovoj listi kako bi dobio informacije potrebne za izvršavanje početnog preuzimanja blokova (IBD) i sinhronizaciju sa lancem koji ima najviše akumuliranog rada. Od 2024. godine, ovde je lista Bitcoin Core DNS seed-ova i pojedinaca odgovornih za njihovo održavanje (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.Bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.Bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.Bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.Bitcoin.wiz.biz: Džejson Moris;
- seed.Mainnet.achownodes.xyz: Ava Chow.


DNS seeds su drugi metod, po prioritetu, za Bitcoin čvor da uspostavi konekcije. Prvi metod uključuje korišćenje peers.dat fajla koji je čvor sam kreirao. Ovaj fajl je prirodno prazan u slučaju novog čvora, osim ako ga korisnik nije ručno izmenio.


> ► *Napomena, DNS semena ne treba mešati sa "seed čvorovima," koji su treći način uspostavljanja konekcija.*