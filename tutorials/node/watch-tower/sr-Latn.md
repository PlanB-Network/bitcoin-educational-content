---
name: Watch Tower
description: Razumevanje i korišćenje Watch Tower
---

## Kako funkcionišu osmatračnice?


Ključni deo Lightning Network ekosistema, osmatračnice pružaju dodatni nivo zaštite korisnicima lightning kanala. Njihova glavna odgovornost je da prate stanje kanala i intervenišu ako jedna strana kanala pokuša da prevari drugu.


Dakle, kako Watchtower može utvrditi da li je kanal kompromitovan? Watchtower prima potrebne informacije od klijenta, jedne od strana u kanalu, kako bi pravilno identifikovao i odgovorio na bilo kakve povrede. Ove informacije često uključuju najnovije detalje transakcije, trenutno stanje kanala i informacije potrebne za kreiranje kaznenih transakcija. Klijent može šifrovati podatke pre nego što ih prenese na Watchtower kako bi zaštitio privatnost i tajnost. Ovo sprečava Watchtower da dešifruje šifrovane podatke osim ako zaista nije došlo do povrede, čak i ako dobije podatke. Sistem šifrovanja štiti privatnost klijenta i sprečava Watchtower da pristupi privatnim podacima bez odobrenja.


## Kako postaviti svoj Eye of Satoshi i početi doprinositi


The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)) je ne-kustodijalni Lightning Watchtower u skladu sa [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Ima dve glavne komponente:


1. teos: uključujući CLI i osnovnu funkcionalnost servera tornja. Dve binarne datoteke—teosd i teos-CLI—će biti proizvedene kada se ovaj paket izgradi.

2. teos-common: Uključuje zajedničku funkcionalnost na strani servera i klijenta (korisno za kreiranje klijenta).


Da biste uspešno pokrenuli toranj, potrebno je da bitcoind bude pokrenut pre pokretanja tornja sa teosd komandom. Pre pokretanja obe ove komande, potrebno je da podesite vaš Bitcoin.conf fajl. Evo koraka kako to da uradite:-


1. Instalirajte Bitcoin jezgro sa izvora ili ga preuzmite. Nakon preuzimanja, postavite Bitcoin.conf datoteku u korisnički direktorijum Bitcoin jezgra. Proverite ovaj link za više informacija o tome gde postaviti datoteku jer to zavisi od operativnog sistema koji koristite.

2. Nakon što identifikujete mesto gde treba kreirati datoteku, dodajte ove opcije:-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword```


Sada, ako pokrenete bitcoind, trebalo bi da pokrene čvor.


1. Za deo tornja, prvo morate instalirati teos iz izvora. Pratite uputstva data na ovom linku.

2. Nakon što ste uspešno instalirali teos na vaš sistem i pokrenuli testove, možete preći na poslednji korak, a to je podešavanje teos.toml fajla u teos korisničkom direktorijumu. Fajl treba da bude smešten u folderu nazvanom .teos (obratite pažnju na tačku) u vašem home folderu. To jest, na primer, /home/<vaše-korisničko-ime>/.teos za Linux. Kada pronađete mesto, kreirajte teos.toml fajl i postavite ove opcije koje odgovaraju stvarima koje smo promenili na bitcoind.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"```


Jednom kada to uradite, trebali biste biti spremni za pokretanje tornja. S obzirom da radimo na regtest-u, verovatno neće biti nijednog bloka iskopanog u našoj Bitcoin testnoj mreži prvi put kada se toranj poveže sa njom (ako ih ima, nešto definitivno nije u redu). Toranj gradi internu keš memoriju poslednjih 100 blokova iz bitcoind, tako da prilikom prvog pokretanja možemo dobiti sledeću grešku:


_GREŠKA [teosd] Nema dovoljno blokova za pokretanje tornja (potrebno: 100). Iskopajte još najmanje 100_


S obzirom da radimo na regtest mreži, možemo iskopati blok izdavanjem RPC komande, bez potrebe čekanja na 10-minutni medijan vremena koji obično vidimo na drugim mrežama (kao što su Mainnet ili Testnet). Proverite bitcoin-cli pomoć i potražite kako iskopati blokove. Ako vam je potrebna pomoć, možete proći kroz ovaj članak.


![image](assets/2.webp)


To je to, uspešno si pokrenuo toranj. Čestitamo. 🎉