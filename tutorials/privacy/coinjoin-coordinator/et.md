---
name: Coinjoin koordinaator - WabiSabi
description: Kuidas seadistada ja käivitada WabiSabi protokolli (kasutatakse Wasabi Wallet 2.0-s) järgivat coinjoin koordinaatorit
---

![cover](assets/cover.webp)


---

## Sissejuhatus 👋


Selles ekspertide juhendis aitame teil luua coinjoin koordinaatori, mis on sisuliselt server, mis toob kokku inimesed, kes soovivad tehingutasusid säästa või suurendada oma privaatsust koostööl põhinevates tehingutes. Kuna Wasabi Walletga ei ole enam komplekteeritud ettevõtte poolt juhitavat koordinaatorit, peavad kasutajad ise leidma ja valima oma eelistatud koordinaatoriserveri. Vaid mõned koordinaatorid on ilmunud, kes küsivad 0% koordineerimistasu, seega on Wasabi Wallet arendajad teinud kõvasti tööd, et muuta oma kogukonna koordinaatori käivitamine võimalikult lihtsaks (nii väikesel riistvaral kui Raspberry Pi5!). Praegu aktiivsed koordinaatorid, kes küsivad 0% koordineerimistasu, on leitavad [LiquiSabi](https://liquisabi.com) ja mis veelgi olulisem, [nostr](https://github.com/Kukks/WasabiNostr).


## Nõuded 🫴



- VPS (hostitud sõlme) või arvuti/server (ise hostitud sõlme)
- Kärbitud/täielik Bitcoin tuumasõlm (testitud versiooniga v29.0)


Vabatahtlik:


- (alam)domeen, mis edastab liiklust sõlme (nt coinjoin.[sinudomeen].io)


Soovitatav on omada mõningaid kogemusi käsurea käskluste ja bashiga, kuna kõiki samme ei saa automatiseerida.


Riistvaraliselt on soovitatav, et süsteemil oleks:


- 4 südamikku
- 16 GB RAM
- 2 TB SSD või NVMe (täieliku sõlme puhul) / 128 GB SSD (pruned-sõlme puhul)


Selliseid nõudeid saab Raspberry Pi 5 pakkuda vaid 120 $ eest, välja arvatud salvestusruumi, mis maksab umbes 100 $ 2TB NVMe mälupulga eest.


Odav VPS on tavaliselt ainult 1 tuum ja 4GB RAM, mis on minu arvates liiga vähe, et sünkroonida ja kontrollida kogu bitcoin blockchain blokikõrgusel 911817.


Salvestusruumi mõttes vajab täisnoode vähemalt 2 TB kettamälu, eelistatavalt SSD või NVMe tüüpi. blockchain kärpimisel on vastuvõetav ka palju väiksem salvestusketas (nt 128 GB SSD).


Kui te kavatsete kasutada koordinaatorit suurte (300+ sisend) mündiliidete jaoks, on soovitatav valida kiiremate/uuemate tuumadega süsteem, millel on suurem jõudlus kõigi allkirjade kontrollimiseks.


## Paigaldamine 🛠️


Sõlme tahame alla laadida ja paigaldada Wasabi Wallet uusima avaldatud versiooni, mis sisaldab backend'i ja koordinaatorit iseseisvate käivitatavate failidena wallet kõrval.


Leia uusim versioon: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) ja kontrollige väljaande PGP-allkirja võtmetega: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Kasutuselevõtu üksikasjad erinevad sõltuvalt riistvarast (protsessor-arhitektuurist) ja operatsioonisüsteemi valikust, allpool on esitatud erinevad üksikasjad Raspberry Pi (ARM-64) ja Debian-põhise RaspiBlitz jaoks, mis on lähtepunktiks. Jätke edasi (X86-64) Ubuntu operatsioonisüsteemi kasutuselevõtu puhul, kasutades Nixi.


Paigaldusjuhised leiate siit: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian kasutuselevõtt


RaspiBlitz (testitud v1.11) sõlmede puhul saab kasutada script juurutamist lähtekoodist: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Lihtne kasutuselevõtt


Minimaalse kasutuselevõtu puhul soovite lihtsalt oma platvormi jaoks vajalikud käivitatavad failid ühte kausta ekstraheerida.

Debian/Ubuntu käsurea näidiskoodid:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Selle tulemuseks peaks olema järgmine kehtiv allkirja sõnum:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Ja te võite jätkata allalaaditud paketi installimist:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfiguratsioon 🧾


Enne koordinaatori käivitamist peate muutma Config.json faili oma:


- Bitcoin RPC volitused
- Eelistatud ümmargused parameetrid
- Koordinaatori laiendatud avalik võti (luua uus SegWit wallet kogutud tolmu vastuvõtmiseks)

**Hoiatus**: Taproot wallet toob kaasa kulutamatud UTXO'd! Kasutage siin Native Segwit wallet.


- Lubatud sisend- ja väljundaadressi tüübid
- Teataja konfiguratsioon nostr-i kaudu avaldamiseks (nimi, kirjeldus, Uri, minimaalsed sisendid, nostr-i relee, nostr-i privaatne võti)


Võite käivitada koordinaatori, mis on kättesaadav ainult .onion-aadressi kaudu, või kasutada oma kohandatud clearnet-domeeni.


Leidke või looge konfiguratsioonifail sellel teekonnal:


`~/.walletwasabi/coordinator/Config.json`


Redigeeri seda käsuga:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Vaata seda näide Config.json:


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

### Tori konfiguratsioon 🧅


OnionServicePrivateKey täitmiseks peate tõenäoliselt esmalt looma oma OnionServicePrivateKey.


Wasabi Wallet genereerib teie jaoks privaatse võtme, kui te käivitate selle esimest korda, kui Config.json failis on määratud ```"PublishAsOnionService": true,```.


Käivitage koordinaator üks kord käsuga:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Et näha oma Onioni varjatud teenuse aadressi, kontrollige kas koordinaatori logisid:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


ja leiad midagi sellist:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Pikk URL, mis lõpeb .onioniga, on teie varjatud teenuse aadress ehk CoordinatorUri.


Või kontrollige uuesti oma koordinaatori konfiguratsioonifaili:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Mis peaks nüüd automaatselt täidetud olema.


## Jooksev ⚡


Kui kõik konfiguratsiooniparameetrid on määratud, võite käivitada koordinaatoriteenuse ja alustada esimese ringi väljakuulutamist 🕶️


Lihtsalt käivitage koordinaator käsuga:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Saate jälgida praegust vooru ja registreeritud UTXO-i/müntide arvu, kontrollides (Tori brauseris .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Valikuline: koordinaatori serveri silumine


Probleeme ja vigu saab jälgida logifailis aadressil ```~/.walletwasabi/backend/Logs.txt```


Tüüpiliste probleemide hulka kuuluvad RPC ühendusprobleemid, see tuleb lubada ```~/.bitcoin/bitcoin.conf``` koos:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Vabatahtlik: Backend-serveri käivitamine


Koos koordinaatoriga saate pakkuda ka backend-serverit kasutajatele, kellel ei ole oma bitcoin-sõlme, millega ühendust võtta, et saada tasu hinnanguid ja blokifiltreid.


Käivitage see teenus käsuga:


```
wbackend
```


## Wasabi kasutajate kutsumine oma koordinaatorile 🫂


Teiste kasutajate jaoks, et leida teie teenus, võite tugineda nostr kuulutaja, või jagada magic link oma domeeni (clearnet) või varjatud teenuse (.onion link) ja ümmargused parameetrid nagu see:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Kui kasutaja kopeerib maagilise lingi ja avab oma Wasabi Wallet, näitab tarkvara automaatselt koordinaatori dialoogi teie domeeni ja parameetritega.


![detected](assets/en/02.webp)


💚🍣 Palju õnne Bitcoini privaatsuse detsentraliseerimise puhul 🕶️


Pea meeles oma koolitust [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet on ainult kaitseks 🛡️