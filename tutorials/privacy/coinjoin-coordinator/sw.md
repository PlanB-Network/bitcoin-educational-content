---
name: Mratibu wa Coinjoin - WabiSabi
description: Jinsi ya kuanzisha na kuendesha mratibu wa coinjoin kwa kufuata itifaki ya WabiSabi (inayotumika katika Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Utangulizi 👋


Katika mwongozo huu wa kitaalamu tutakusaidia kuanzisha mratibu wa coinjoin, kimsingi seva inayowaunganisha watu wanaotaka kuokoa ada za miamala au kuongeza faragha yao ya onchain katika miamala ya ushirikiano. Kwa kuwa hakuna tena mratibu wa uendeshaji wa kampuni aliyeunganishwa na Wasabi Wallet, watumiaji wanapaswa kutafuta na kuchagua seva yao ya mratibu wanayopendelea. Ni waratibu wachache tu wamejitokeza wakiomba ada ya uratibu ya 0%, kwa hivyo watengenezaji wa Wasabi Wallet wamekuwa wakifanya kazi kwa bidii ili kurahisisha iwezekanavyo kuanza kuendesha mratibu wako wa jumuiya (kwenye vifaa vidogo kama Raspberry Pi5!). Waratibu wanaofanya kazi kwa sasa wanaoomba ada ya uratibu ya 0% wanaweza kupatikana kwenye [LiquiSabi](https://liquisabi.com) na muhimu zaidi kwenye [nostr](https://github.com/Kukks/WasabiNostr).


## Mahitaji 🫴



- VPS (nodi iliyopangishwa) au kompyuta/seva (nodi iliyopangishwa yenyewe)
- Nodi ya Bitcoin Iliyokatwa/Kamili (iliyojaribiwa na v29.0)


Hiari:


- (ndogo) Trafiki ya usambazaji wa kikoa kwenye nodi (k.m. coinjoin.[yourdomain].io)


Inashauriwa kuwa na uzoefu fulani na vidokezo vya mstari wa amri na bash, kwani si hatua zote zinaweza kuwa otomatiki.


Kwa upande wa vifaa, inashauriwa kuwa na mfumo wenye:


- Viini 4
- RAM ya GB 16
- SSD ya TB 2 au NVMe (kwa nodi kamili) / SSD ya GB 128 (kwa nodi ya pruned)


Mahitaji kama hayo yanaweza kutolewa na Raspberry Pi 5 kwa $120 pekee, ukiondoa hifadhi ambayo inagharimu takriban $100 kwa kijiti cha NVMe cha 2TB.


VPS ya bei nafuu kwa kawaida huja na kiini 1 pekee na RAM ya 4GB, ambayo nimegundua kuwa ni kidogo sana kusawazisha na kuthibitisha bitcoin nzima ya blockchain katika urefu wa blockheight 911817.


Kwa upande wa hifadhi, nodi kamili itahitaji angalau 2TB ya hifadhi ya diski, ikiwezekana aina ya SSD au NVMe. Wakati wa kupogoa blockchain, hifadhi ndogo zaidi inakubalika (k.m. SSD ya 128GB).


Ikiwa unakusudia kuendesha mratibu wa coinjoins kubwa (zaidi ya 300), inashauriwa kuchagua mfumo wenye cores za kasi/mpya zaidi zenye utendaji wa juu kwa uthibitishaji wote wa sahihi.


## Usakinishaji 🛠️


Kwenye nodi tunataka kupakua na kusakinisha toleo jipya zaidi la Wasabi Wallet, ambalo linajumuisha sehemu ya nyuma na mratibu kama vitendaji vinavyoweza kutekelezwa kando ya wallet.


Tafuta toleo jipya zaidi: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) na uthibitishe sahihi ya PGP ya toleo kwa kutumia funguo: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Maelezo ya utekelezaji hutofautiana kulingana na vifaa (usanifu wa CPU) na chaguo la Mfumo wa Uendeshaji, chini ya maelezo tofauti yanatolewa kwa Raspberry Pi (ARM-64) yenye RaspiBlitz inayotegemea Debian kama mahali pa kuanzia. Ruka mbele kwa ajili ya utekelezaji wa Mfumo wa Uendeshaji wa Ubuntu (X86-64) kwa kutumia Nix.


Pata maagizo ya usakinishaji hapa: [Hati za Wasabi](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Utekelezaji wa RaspiBlitz/Debian


Kwa nodi za RaspiBlitz (zilizojaribiwa na v1.11), jengo la usanidi wa script kutoka kwa msimbo chanzo linaweza kutumika: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Usambazaji rahisi


Kwa usanidi mdogo zaidi, unataka tu kutoa vitendakazi vinavyoweza kutekelezwa kwa mfumo wako kwenye folda.

Mifano ya misimbo ya amri ya Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Hii inapaswa kusababisha ujumbe ufuatao sahihi halali:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Na unaweza kuendelea kusakinisha kifurushi kilichopakuliwa:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Usanidi 🧾


Kabla ya kuendesha kiratibu unahitaji kuhariri faili ya Config.json na:


- Sifa za Bitcoin RPC
- Vigezo vya mviringo vinavyopendelewa
- Mratibu Ufunguo wa Umma Uliopanuliwa (tengeneza SegWit wallet mpya kwa ajili ya kupokea vumbi lililokusanywa)

**Onyo**: Taproot wallet itasababisha UTXO zisizoweza kutumika! Tumia wallet ya Asili ya Segwit hapa.


- Aina za anwani zinazoruhusiwa za kuingiza na kutoa
- Usanidi wa mtangazaji kwa ajili ya kuchapisha juu ya nostr (jina, maelezo, Uri, ingizo la chini kabisa, nostr relay, nostr private key)


Unaweza kuendesha kiratibu kinachoweza kufikiwa kupitia anwani ya .onion pekee, au kutumia kikoa chako maalum cha clearnet.


Tafuta au unda faili ya usanidi kwenye njia hii:


`~/.walletwasabi/mratibu/Config.json`


Hariri kwa amri:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Tazama mfano huu Config.json:


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

### Usanidi wa Tor 🧅


Ili kujaza OnionServicePrivateKey yako huenda ukahitaji kutengeneza moja kwanza.


Wasabi Wallet itakutengenezea ufunguo wa faragha ikiwa utauendesha mara ya kwanza ukitumia ```"PublishAsOnionService": true,``` iliyowekwa kwenye faili ya Config.json.


Endesha mratibu mara moja kwa amri:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Ili kuona anwani yako ya huduma iliyofichwa ya Onion, angalia kumbukumbu za mratibu kwa kutumia:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


na utapata kitu kama:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


URL ndefu inayoishia na .onion ni anwani yako ya huduma iliyofichwa au MratibuUri.


Au angalia tena faili yako ya usanidi wa mratibu na:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Ambayo inapaswa kujazwa kiotomatiki sasa.


## Kukimbia ⚡


Mara vigezo vyote vya usanidi vikiwa vimewekwa unaweza kuendesha huduma ya mratibu na kuanza kutangaza raundi yako ya kwanza 🕶️


Anza tu mratibu kwa amri:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Unaweza kufuatilia raundi ya sasa na idadi ya sarafu/sarafu za UTXO zilizosajiliwa kwa kuangalia (katika kivinjari cha Tor kwa .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Hiari: seva ya mratibu wa utatuzi wa matatizo


Unaweza kufuatilia matatizo au hitilafu zozote kwenye faili ya kumbukumbu katika ```~/.walletwasabi/backend/Logs.txt```


Matatizo ya kawaida yanajumuisha matatizo ya muunganisho wa RPC, hii lazima iwezeshwe katika ```~/.bitcoin/bitcoin.conf``` na:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Hiari: Kuendesha seva ya nyuma


Pamoja na mratibu unaweza pia kutoa seva ya nyuma kwa watumiaji ambao hawana nodi yao ya bitcoin ya kuunganishwa nayo kwa makadirio ya ada na vichujio vya kuzuia.


Anza huduma hii kwa amri:


```
wbackend
```


## Kuwaalika watumiaji wa Wasabi kwa mratibu wako 🫂


Kwa watumiaji wengine kupata huduma yako unaweza kutegemea mtangazaji wa nostr, au kushiriki kiungo cha uchawi na kikoa chako (clearnet) au huduma iliyofichwa (kiungo cha .onion) na vigezo vya mviringo kama hivi:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Mtumiaji anaponakili kiungo cha uchawi na kufungua Wasabi Wallet yake, programu itaonyesha kiotomatiki kidirisha cha mratibu chenye kikoa chako na vigezo.


![detected](assets/en/02.webp)


💚🍣 Hongera kwa kugawanya faragha ya bitcoin 🕶️


Kumbuka mafunzo yako [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet ni ya ulinzi pekee 🛡️