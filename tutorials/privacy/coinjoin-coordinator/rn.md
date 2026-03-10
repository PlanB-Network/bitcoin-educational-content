---
name: Umuhuzabikorwa wa Coinjoin - WabiSabi
description: Uko woshiraho no gukoresha umuhuzabikorwa wa coinjoin ukurikije umurongo wa WabiSabi (ukoreshwa muri Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Intangamarara 👋


Muri iyi nkuru y’abahinga tuzogufasha gushinga umuhuzabikorwa wa coinjoin, mu vy’ukuri umukozi ahuriza hamwe abantu bashaka kuzigama ku mahera y’ibikorwa canke kwongera ubuzima bwite bwabo mu bikorwa vy’ubufatanye. Kubera ko ata muhuzabikorwa w’ishirahamwe agifise afatanijwe na Wasabi Wallet, abakoresha bategerezwa kurondera no guhitamwo umuhuzabikorwa bakunda. Abahuzabikorwa bakeyi gusa ni bo bagaragaje basaba amafaranga y’uguhuza 0%, rero abateguye Wasabi Wallet bamaze igihe bakora cane kugira ngo vyorohe uko bishoboka kwose gutangura gukoresha umuhuzabikorwa wawe w’abanyagihugu (ku bikoresho bitobito nka Raspberry Pi5!). Abahuzabikorwa bariko barakora ubu basaba 0% y’amahera y’uguhuza ibikorwa bashobora kubisanga kuri [LiquiSabi](https://liquisabi.com) kandi ikiruta vyose kuri [nostr](https://github.com/Kukks/WasabiNostr).


## Ibisabwa 🫴



- VPS (uruzitiro rwakira) canke mudasobwa/serveri (uruzitiro rwikorera)
- Igipande c'ingenzi ca Bitcoin (cageragejwe na v29.0)


Ntivyemewe:


- (sub)Indangarubuga yohereza uruja n'uruza ku nzira (nk'akarorero coinjoin.[intara yawe].io)


Ni vyiza kugira ubumenyi bumwe bumwe ku bijanye n’amategeko n’ivyo gukoresha, kuko intambwe zose zidashobora gukorwa.


Mu bijanye n’ibikoresho, ni vyiza kugira ubuhinga bufise:


- 4 cores
- 16 GB RAM
- 2 TB SSD canke NVMe (ku nzira yuzuye) / 128 GB SSD (ku nzira ya pruned)


Ivyo bisabwa bishobora gutangwa na Raspberry Pi 5 ku madolari 120 gusa, hatarimwo ububiko bugura amadolari nka 100 ku nkoni ya NVMe ya 2TB.


VPS ihenda cane izana n’umutima 1 gusa na 4GB RAM, ivyo nasanze ari bike cane kugira ngo bihuze no kugenzura bitcoin yose blockchain ku burebure bwa blockheight 911817.


Mu bijanye n’ububiko, node yuzuye izosaba nibura 2TB y’ububiko bwa disiki, vyiza ni ubwoko bwa SSD canke NVMe. Igihe ukata blockchain, ushobora gukoresha ububiko buto cane (nk’akarorero SSD ya 128GB).


Niba ushaka gukoresha umuhuzabikorwa w’ama coinjoins manini (300+ input), ni vyiza guhitamwo uburyo bufise ama cores yihuta/mashasha afise ubushobozi bwinshi ku bijanye n’igenzura ryose ry’imikono.


## Gushiraho 🛠️


Ku nzira turashaka gukuraho no gushiramwo verisiyo nshasha ya Wasabi Wallet, irimwo inyuma n'umuhuzabikorwa nk'ibikorwa vyihariye iruhande ya wallet.


Rondera verisiyo nshasha: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/ibisohotse) maze usuzume umukono wa PGP w'ivyo bisohotse ukoresheje imfunguruzo: [PGP.txt] (ibirimwo


Ivyerekeye gukoresha biratandukanye bivanye n’ibikoresho (CPU-architecture) n’uguhitamwo OS, aha hepfo ivyerekeye gukoresha Raspberry Pi (ARM-64) ifise RaspiBlitz ishingiye kuri Debian nk’intango. Simbuka imbere ku (X86-64) Ubuntu OS gukoresha Nix.


Rondera amabwirizwa yo gushiramwo hano: [Inyandiko za Wasabi](https://inyandiko.wasabiwallet.io/ukoresha-wasabi/Inyandiko zo Gushiramwo.html)


### Gushirwaho kwa RaspiBlitz/Debian


Ku bihimba vya RaspiBlitz (vyageragejwe na v1.11) inyubakwa yo gukoresha script ivuye kuri kode y’inkomoko irashobora gukoreshwa: [inzu



### Gushiraho vyoroshe


Kubera gukoresha bike cane ushaka gukuraho ibikorwa vy'urubuga rwawe muri dosiye.

Akarorero k'umurongo w'itegeko rya Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Ibi bikwiye gutuma haba ubutumwa bukurikira:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Kandi ushobora gukomeza gushiramwo porogaramu yakuwe kuri interineti:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Gutunganya 🧾


Imbere yo gukoresha umuhuzabikorwa ukeneye guhindura dosiye Config.json n'iyawe:


- Bitcoin Ivyemezo vya RPC
- Ivyagezwe vy'uruziga
- Umuhuzabikorwa Urufunguzo rwa bose rwagutse (gukora SegWit wallet nshasha yo kwakira inkungugu yegeranijwe)

**Imburi**: Taproot wallet izotuma haba ama UTXO atazokoreshwa! Koresha Segwit y’Igihugu wallet hano.


- Ubwoko bw'amaderesi y'injiza n'isohoka yemerewe
- Itunganywa ry'umumenyeshamakuru ryo gutangaza kuri nostr (izina, insobanuro, Uri, ivyinjizwa bike, nostr relay, nostr urufunguzo rwihariye)


Ushobora gukoresha umuhuzabikorwa ashobora gushikirwa gusa biciye kuri aderesi .onion, canke ukoreshe urwego rwawe rwa clearnet.


Rondera canke ureme dosiye y'imiterere kuri iyi nzira:


`~/.walletwasabi/umuhuzabikorwa/imiterere.json`


Bihindure n'itegeko:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Raba aka karorero Config.json:


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

### Itunganywa rya Tor 🧅


Kugira ngo wuzuze urufunguzo rwawe rw'igitunguru, birashoboka ko ukeneye kubanza gukora rumwe.


Wasabi Wallet izoguha urufunguzo rwihariye niwarukoresha ubwa mbere na ```"GusohoraNk'Igitunguru": ukuri,``` gushizwe muri dosiye Config.json.


Gukoresha umuhuzabikorwa rimwe n'itegeko:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Kugira ngo ubone aderesi yawe y'igitunguru, ushobora gusuzuma ibitabo vy'umuhuzabikorwa na:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


kandi uzosanga ikintu nk'iki:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


URL ndende ihera muri .onion ni aderesi yawe y'ibikorwa vyihishijwe canke CoordinatorUri.


Canke usubire gusuzuma dosiye y'imiterere y'umuhuzabikorwa wawe na:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Ivyo bikwiye kwuzuzwa ubwavyo ubu.


## Kwiruka ⚡


Igihe amaparametere yose ya config amaze gushirwaho ushobora gukoresha service y'umuhuzabikorwa maze ugatangura kumenyesha urugendo rwawe rwa mbere 🕶️ 


Gusa tangura umuhuzabikorwa n'itegeko:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Ushobora gukurikirana uruziga rw'ubu n'umubare w'ibiceri vya UTXO vyanditswe mu gusuzuma (mu mucukumbuzi wa Tor ku .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Amahitamwo: gukosora umuhuzabikorwa


Ushobora gukurikirana ibibazo vyose canke amakosa ari muri dosiye y'inyandiko kuri ```~/.walletwasabi/backend/Logs.txt```


Ibibazo bisanzwe birimwo ibibazo vy'ihuriro rya RPC, ibi bitegerezwa gushobozwa muri ```~/.bitcoin/bitcoin.conf``` na:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Amahitamwo: Gukoresha umukozi w'inyuma


Hamwe n’umuhuzabikorwa urashobora kandi gutanga server y’inyuma ku bakoresha badafise node yabo bwite ya bitcoin yo kwifatanya na yo kugira ngo bamenye amafaranga y’ibiharuro n’ama blockfilters.


Tangira iyi serivisi n'itegeko:


```
wbackend
```


## Gutumira abakoresha Wasabi ku muhuzabikorwa wanyu 🫂 


Kugira ngo abandi bakoresha bashobore kuronka serivisi yawe ushobora kwizigira umumenyeshamakuru wa nostr, canke ugasangira uruja n'uruza rw'ubupfumu n'itongo ryawe (clearnet) canke serivisi yihishije (.onion link) n'ibipimo nk'ibi:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Iyo umukoresha akopiye uruja n’uruza rw’ubupfumu maze akagurura Wasabi Wallet yiwe, iyo porogarama izoca yerekana ikiganiro c’umuhuzabikorwa n’itongo ryawe n’ibipimo vyawe.


![detected](assets/en/02.webp)


💚🍣 Urakoze cane ku kwegereza ubuzima bwite bwa bitcoin 🕶️


Ibuka imyimenyerezo yawe [wasabika](https://docs.wasabiwallet.io/Inyishu-inyishu.html#ushobora-kuba-umu-wasabika), Wasabi Wallet ni iyo kwikingira gusa 🛡️