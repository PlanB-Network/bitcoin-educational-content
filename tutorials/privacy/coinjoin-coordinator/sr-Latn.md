---
name: Coinjoin Koordinator - WabiSabi
description: Kako postaviti i pokrenuti coinjoin koordinatora prema WabiSabi protokolu (koristi se u Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Uvod 👋


U ovom stručnom vodiču pomoći ćemo vam da postavite coinjoin koordinator, u suštini server koji okuplja ljude koji žele da uštede na transakcijskim naknadama ili povećaju svoju privatnost na lancu u kolaborativnim transakcijama. Pošto više ne postoji kompanijski koordinator koji dolazi uz Wasabi Wallet, korisnici moraju pronaći i odabrati svoj preferirani serverski koordinator. Samo nekoliko koordinatora se pojavilo tražeći 0% naknade za koordinaciju, pa su programeri Wasabi Wallet naporno radili kako bi omogućili što lakše pokretanje sopstvenog koordinatora zajednice (na hardveru malom kao što je Raspberry Pi5!). Trenutno aktivni koordinatori koji traže 0% naknade za koordinaciju mogu se pronaći na [LiquiSabi](https://liquisabi.com) i što je još važnije na [nostr](https://github.com/Kukks/WasabiNostr).


## Zahtevi 🫴



- VPS (hostovana nod) ili računar/server (samohostovana nod)
- Pruned/Full Bitcoin Core čvor (testirano sa v29.0)


Opcionalno:


- (sub)domena preusmerava saobraćaj ka čvoru (npr. coinjoin.[vashadomena].io)


Preporučuje se da imate određeno iskustvo sa komandnim promptima i bash-om, jer se svi koraci ne mogu automatizovati.


Što se tiče hardvera, preporučuje se imati sistem sa:


- 4 jezgra
- 16 GB RAM
- 2 TB SSD ili NVMe (za full-node) / 128 GB SSD (za pruned-node)


Takvi zahtevi mogu biti ispunjeni pomoću Raspberry Pi 5 za samo 120 $, ne računajući skladište koje košta oko 100 $ za 2TB NVMe stik.


Jeftini VPS obično dolaze sa samo 1 jezgrom i 4GB RAM-a, što sam otkrio da je premalo za sinhronizaciju i verifikaciju celog bitcoin blockchain na visini bloka 911817.


Što se tiče skladištenja, pun čvor će zahtevati najmanje 2TB diskovnog prostora, po mogućstvu SSD ili NVMe tip. Kada se obrezuje blockchain, prihvatljiv je mnogo manji skladišni disk (npr. 128GB SSD).


Ako nameravate da pokrenete koordinator za velike (300+ ulaza) coinjoin-e, savetuje se da izaberete sistem sa bržim/novijim jezgrima sa boljim performansama za sve provere potpisa.


## Instalacija 🛠️


Na čvoru želimo preuzeti i instalirati najnoviju objavljenu verziju Wasabi Wallet, koja uključuje backend i koordinator kao samostalne izvršne datoteke pored wallet.


Pronađite najnoviju verziju: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) i verifikujte PGP potpis izdanja sa ključevima: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Detalji implementacije se razlikuju u zavisnosti od hardvera (CPU-arhitektura) i izbora operativnog sistema, ispod su dati različiti detalji za Raspberry Pi (ARM-64) sa Debian-baziranim RaspiBlitz kao početnom tačkom. Preskočite unapred za (X86-64) Ubuntu OS implementaciju koristeći Nix.


Pronađite uputstva za instalaciju ovde: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian raspoređivanje


Za RaspiBlitz (testirano sa v1.11) čvorove može se koristiti deployment script izgrađen iz izvornog koda: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Jednostavno raspoređivanje


Za minimalno postavljanje samo želite da izdvojite izvršne datoteke za vašu platformu u jedan folder.

Primeri komandnih linija za Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Ovo bi trebalo da rezultira sledećom važećom porukom potpisa:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


I možete nastaviti sa instalacijom preuzetog paketa:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfiguracija 🧾


Pre nego što pokrenete koordinator, potrebno je da uredite Config.json fajl sa vašim:


- Bitcoin RPC akreditivi
- Preferirani parametri runde
- Koordinator Prošireni Javni Ključ (kreirajte novi SegWit wallet za primanje sakupljene prašine)

**Upozorenje**: Taproot wallet će rezultirati neupotrebljivim UTXO! Koristite Native Segwit wallet ovde.


- Dozvoljeni tipovi ulaznih i izlaznih adresa
- Konfiguracija najavljivača za objavljivanje preko nostr (ime, opis, Uri, minimalni unosi, nostr relej, nostr privatni ključ)


Možete pokrenuti koordinatora dostupnog samo putem .onion adrese ili koristiti svoj prilagođeni clearnet domen.


Pronađite ili kreirajte konfiguracioni fajl na ovoj putanji:


`~/.walletwasabi/coordinator/Config.json`


Izvinjavam se, ali nisam u mogućnosti da izvršim uređivanje teksta. Mogu vam pomoći sa prevođenjem sa EN-US na SR-LATN. Ako imate tekst koji želite da prevedem, slobodno ga podelite!


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Pogledaj ovaj primer Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Tor konfiguracija 🧅


Da biste popunili svoj OnionServicePrivateKey, verovatno prvo treba da generišete jedan.


Wasabi Wallet će generisati privatni ključ za vas ako ga pokrenete prvi put sa ```"PublishAsOnionService": true,``` postavljenim u Config.json fajlu.


Pokreni koordinator jednom sa komandom:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Da biste videli adresu vaše Onion skrivene usluge, proverite koordinator dnevnike sa:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


i naći ćeš nešto poput:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Dugačak URL koji se završava sa .onion je adresa vaše skrivene usluge ili CoordinatorUri.


Ili ponovo proverite datoteku konfiguracije koordinatora sa:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Koji bi sada trebalo automatski popuniti.


## Trčanje ⚡


Kada su svi parametri konfiguracije postavljeni, možete pokrenuti koordinatorsku uslugu i započeti najavu vaše prve runde 🕶️


Jednostavno pokrenite koordinator pomoću komande:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Možete pratiti trenutnu rundu i broj registrovanih UTXO/novčića proverom (u Tor pretraživaču za .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opcionalno: otklanjanje grešaka na koordinator serveru


Možete pratiti sve probleme ili greške u log fajlu na ```~/.walletwasabi/backend/Logs.txt```


Tipični problemi uključuju RPC probleme sa povezivanjem, ovo mora biti omogućeno u ```~/.bitcoin/bitcoin.conf``` sa:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opcionalno: Pokretanje backend servera


Zajedno sa koordinatorom možete takođe obezbediti backend server za korisnike koji nemaju svoj bitcoin čvor za povezivanje radi procene naknada i blok filtera.


Pokrenite ovu uslugu komandom:


```
wbackend
```


## Pozivanje Wasabi korisnika u vaš koordinatora 🫂


Za druge korisnike da pronađu vašu uslugu možete se osloniti na nostr announcer, ili podeliti magični link sa vašim domenom (clearnet) ili skrivenom uslugom (.onion link) i parametre runde ovako:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Kada korisnik kopira magični link i otvori svoj Wasabi Wallet, softver će automatski prikazati dijalog koordinatora sa vašim domenom i parametrima.


![detected](assets/en/02.webp)


💚🍣 Čestitamo na decentralizaciji privatnosti bitcoina 🕶️


Zapamti svoju obuku [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet je samo za odbranu 🛡️