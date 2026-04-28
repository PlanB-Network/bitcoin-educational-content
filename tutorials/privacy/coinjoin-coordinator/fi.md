---
name: Coinjoin-koordinaattori - WabiSabi
description: Miten asetetaan ja ajetaan kolikkoliitoskoordinaattori WabiSabi-protokollan mukaisesti (käytetään Wasabi Wallet 2.0:ssa)?
---

![cover](assets/cover.webp)


---

## Johdanto 👋


Tässä asiantuntijaoppaassa autamme sinua perustamaan coinjoin-koordinaattorin, joka on lähinnä palvelin, joka kokoaa yhteen ihmiset, jotka haluavat säästää transaktiomaksuissa tai lisätä yksityisyyttään ketjussa yhteisissä transaktioissa. Koska Wasabi Wallet:n mukana ei enää ole yrityksen ylläpitämää koordinaattoria, käyttäjien on löydettävä ja valittava oma haluamansa koordinaattoripalvelin. Vain muutama koordinaattori on ilmaantunut pyytämään 0 prosentin koordinaatiomaksua, joten Wasabi Wallet:n kehittäjät ovat tehneet kovasti töitä sen eteen, että oman yhteisökoordinaattorin pyörittäminen olisi mahdollisimman helppoa (niinkin pienellä laitteistolla kuin Raspberry Pi5!). Tällä hetkellä aktiiviset koordinaattorit, jotka pyytävät 0 % koordinointimaksua, löytyvät [LiquiSabi](https://liquisabi.com) ja ennen kaikkea [nostr](https://github.com/Kukks/WasabiNostr).


## Vaatimukset 🫴



- VPS (isännöity solmu) tai tietokone/palvelin (itse isännöity solmu)
- Karsittu/täydellinen Bitcoin Core-solmu (testattu v29.0:lla)


Valinnainen:


- (ali)verkkotunnus, joka välittää liikennettä solmuun (esim. coinjoin.[yourdomain].io)


On suositeltavaa, että sinulla on jonkin verran kokemusta komentorivikehotteista ja bashista, sillä kaikkia vaiheita ei voi automatisoida.


Laitteistollisesti suositellaan järjestelmää, jossa on:


- 4 ydintä
- 16 GB RAM-MUISTIA
- 2 TB SSD- tai NVMe-levy (koko solmulle) / 128 GB SSD-levy (pruned-solmulle)


Tällaiset vaatimukset voidaan täyttää Raspberry Pi 5:llä vain 120 dollarilla, lukuun ottamatta tallennustilaa, joka maksaa noin 100 dollaria 2TB:n NVMe-muistitikusta.


Halvoissa VPS-palvelimissa on yleensä vain yksi ydin ja 4 Gt RAM-muistia, mikä on mielestäni liian vähän koko Bitcoin blockchain:n synkronointiin ja tarkistamiseen lohkokorkeudella 911817.


Tallennusmuistiin nähden täysi solmu vaatii vähintään 2 Tt levytallennustilaa, mieluiten SSD- tai NVMe-tyyppistä. Kun blockchain:ta karsitaan, paljon pienempi tallennusasema on hyväksyttävä (esim. 128 Gt:n SSD-levy).


Jos aiot käyttää koordinaattoria suurten (yli 300 syötettä) kolikofunktioiden yhdistämiseen, on suositeltavaa valita järjestelmä, jossa on nopeampia tai uudempia ytimiä, joiden suorituskyky on suurempi kaikkien allekirjoitusten tarkistusten osalta.


## Asennus 🛠️


Solmuun haluamme ladata ja asentaa Wasabi Wallet:n viimeisimmän julkaistun version, joka sisältää backendin ja koordinaattorin itsenäisinä suoritettavina tiedostoina wallet:n ohella.


Etsi uusin versio: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) ja tarkista julkaisun PGP-allekirjoitus avaimilla: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Käyttöönoton yksityiskohdat vaihtelevat laitteiston (CPU-arkkitehtuurin) ja käyttöjärjestelmän valinnan mukaan. Alla on esitetty eri yksityiskohdat Raspberry Pi -tietokoneelle (ARM-64), jonka lähtökohtana on Debian-pohjainen RaspiBlitz. Siirry eteenpäin (X86-64) Ubuntu-käyttöjärjestelmän käyttöönottoa varten Nixin avulla.


Löydät asennusohjeet täältä: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian käyttöönotto


RaspiBlitz:n (testattu v1.11:llä) solmuja varten voidaan käyttää lähdekoodista rakennettua script:n käyttöönottoa: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Helppo käyttöönotto


Minimaalista käyttöönottoa varten haluat vain purkaa alustan suoritettavat tiedostot kansioon.

Esimerkki komentorivikoodeista Debian/Ubuntu:lle:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Tämän pitäisi johtaa seuraavaan kelvolliseen allekirjoitusviestiin:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Sitten voit asentaa ladatun paketin:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfigurointi 🧾


Ennen koordinaattorin suorittamista sinun on muokattava Config.json-tiedostoa:


- Bitcoin RPC valtakirjat
- Suositeltavat kierroksen parametrit
- Koordinaattorin laajennettu julkinen avain (luodaan uusi SegWit wallet kerätyn pölyn vastaanottamista varten)

**Varoitus**: Taproot wallet johtaa käyttämättömiin UTXO:iin! Käytä tässä Native Segwit wallet:tä.


- Sallitut tulo- ja lähtöosoitetyypit
- Ilmoittajan konfigurointi nostr:n kautta julkaisemista varten (nimi, kuvaus, Uri, vähimmäissyötteet, nostr-rele, nostr-avain)


Voit käyttää koordinaattoria, joka on käytettävissä vain .onion-osoitteen kautta, tai käyttää omaa clearnet-verkkotunnustasi.


Etsi tai luo konfigurointitiedosto tästä polusta:


`~/.walletwasabi/coordinator/Config.json`


Muokkaa sitä komennolla:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Katso tämä esimerkki Config.json:


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

### Tor-konfiguraatio 🧅


Täyttääksesi OnionServicePrivateKey-avaimesi sinun on todennäköisesti luotava sellainen ensin.


Wasabi Wallet luo yksityisen avaimen puolestasi, jos suoritat sen ensimmäisen kerran siten, että Config.json-tiedostossa on asetettu ```"PublishAsOnionService": true,```.


Suorita koordinaattori kerran komennolla:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Jos haluat nähdä Onionin piilotetun palvelun osoitteen, tarkista koordinaattorin lokit joko seuraavalla tavalla:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


ja löydät jotain sellaista kuin:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Pitkä URL-osoite, jonka pääte on .onion, on piilotettu palveluosoitteesi eli CoordinatorUri.


Tai tarkista uudelleen koordinaattorin asetustiedosto:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Sen pitäisi nyt täyttyä automaattisesti.


## Käynnissä ⚡


Kun kaikki konfiguraatioparametrit on asetettu, voit käynnistää koordinaattoripalvelun ja aloittaa ensimmäisen kierroksen ilmoittamisen 🕶️


Käynnistä koordinaattori komennolla:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Voit seurata nykyistä kierrosta ja rekisteröityjen UTXO:ien/kolikoiden määrää tarkistamalla (Tor-selaimessa .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Valinnainen: koordinaattoripalvelimen virheenkorjaus


Voit seurata mahdollisia ongelmia tai virheitä lokitiedostosta osoitteessa ```~/.walletwasabi/backend/Logs.txt```


Tyypillisiä ongelmia ovat RPC-yhteysongelmat, tämä on otettava käyttöön ```~/.bitcoin/bitcoin.conf```` kanssa:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Valinnainen: Backend-palvelimen suorittaminen


Yhdessä koordinaattorin kanssa voit myös tarjota backend-palvelimen käyttäjille, joilla ei ole omaa bitcoin-solmua, johon he voivat muodostaa yhteyden maksuarvioita ja estosuodattimia varten.


Käynnistä tämä palvelu komennolla:


```
wbackend
```


## Wasabi-käyttäjien kutsuminen koordinaattoriin 🫂


Jotta muut käyttäjät löytäisivät palvelusi, voit luottaa nostr-ilmoittajaan tai jakaa maagisen linkin, jossa on verkkotunnuksesi (clearnet) tai piilotettu palvelusi (.onion-linkki) ja pyöreitä parametrejä, kuten tämä:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Kun käyttäjä kopioi maagisen linkin ja avaa Wasabi Wallet:nsa, ohjelmisto näyttää automaattisesti koordinaattorin valintaikkunan, jossa on verkkotunnuksesi ja parametrit.


![detected](assets/en/02.webp)


💚🍣 Onnittelut bitcoinin yksityisyyden hajauttamisesta 🕶️


Muista harjoituksesi [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet on vain puolustusta varten 🛡️