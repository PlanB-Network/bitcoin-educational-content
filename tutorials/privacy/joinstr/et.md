---
name: Joinstr
description: Detsentraliseeritud CoinJoins Nostr-võrgu kaudu suveräänse Bitcoin konfidentsiaalsuse tagamiseks
---

![cover](assets/cover.webp)



Bitcoin plokiahela läbipaistvus võimaldab jälgida tehingute ajalugu. CoinJoins katkestab need seosed, segades mitu samaaegset tehingut, taastades sularahaga võrreldava konfidentsiaalsuse taseme.



Traditsioonilised lahendused tuginevad aga kesksele koordinaatorile kui ühele tõrkepunktile. Wasabi ja Samourai lõpetasid tegevuse 2024. aastal regulatiivse surve all.



**Joinstr** kõrvaldab selle nõrkuse, kasutades koordineerimiseks detsentraliseeritud Nostr-võrku. See avatud lähtekoodiga rakendus võimaldab tõeliselt suveräänseid CoinJoins, kus ükski keskasutus ei saa tsenseerida, jälgida või katkestada teenust.



## Mis on Joinstr?



Joinstr on avatud lähtekoodiga tööriist, mis muudab CoinJoins'i lähenemisviisi revolutsiooniliselt, kasutades Nostr-protokolli koordineerimisinfrastruktuurina. Erinevalt tsentraliseeritud lahendustest, mis nõuavad spetsiaalset serverit, tugineb Joinstr Nostr-i releede hajutatud võrgule, mis võimaldab osalejatel koordineerida otse eakaaslaste vahel.



**Detsentraliseeritud arhitektuur** : Nostr-võrk asendab keskse koordinaatori. Osalejad loovad või liituvad "basseinidega", postitades krüpteeritud teateid Nostri releede kaudu. See teave (summad, osalejad, aadressid) jääb releedele arusaamatuks, mis tagab, et ükski keskne üksus ei saa jälgida, tsenseerida või filtreerida CoinJoins'i.



**SIGHASH_ALL|ANYONECANPAY mehhanism**: Joinstr kasutab seda Bitcoin allkirjastamise märki, võimaldades igal osalejal allkirjastada ainult oma sisendit, valideerides samal ajal kõik väljundid. Iga kasutaja genereerib oma PSBT lokaalselt, seejärel levitab seda Nostr kaudu. Iga kasutaja genereerib oma PSBT lokaalselt, allkirjastab selle, seejärel levitab seda Nostr kaudu. Teie bitcoinid jäävad kuni lõpliku allkirjastamiseni teie ainukontrolli alla.



**Filosoofia**: Joinstr järgib Bitcoin cypherpunk eetost, mille eesmärk on kolm: **Tsensuurivastasus** (ükski asutus ei saa teenust peatada), **täielik mittesaladus** (te säilitate oma isiklikud võtmed) ja **võrdne kohtlemine** (ühtegi UTXO ei saa diskrimineerida).



### Peamised omadused



**Flexible basseinid**: Erinevalt fikseeritud nimiväärtustest saab iga kasutaja luua täpselt soovitud summa ja osalejate arvu, optimeerides UTXO kasutamist ilma kunstliku jagamiseta.



** Läbipaistvad tasud**: Kooskõlastustasud puuduvad. Ainult Bitcoin tehingutasud jagatakse võrdselt osalejate vahel (paar tuhat satošit inimese kohta).



**Efemenaliteet**: Kasutajate andmeid ei säilitata. Teave edastatakse krüpteeritud efemeersete Nostr-sõnumite kaudu, mis unustatakse kohe pärast tehingu sooritamist.



### Kättesaadavad platvormid



See õpetus keskendub **Android-rakendusele**, mis on hetkel ainus stabiilne ja soovitatav lahendus. Electrum plugin on olemas, kuid sellel on ühilduvusprobleeme, mis muudavad selle ebastabiilseks. Veebiliides on väljatöötamisel.



## Bitcoin tuumkonfiguratsioon



Joinstr Android nõuab ühendust Bitcoin sõlme RPC kaudu. Kõigepealt peate seadistama Bitcoin Core arvutis nii, et see võtaks vastu ühendusi telefonist.



**Märkus**: Täpsemat teavet Bitcoin Core'i täieliku konfigureerimise kohta leiate meie spetsiaalsetest juhendmaterjalidest :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Võrgunõuded



#### Kohaliku IP-aadressi leidmine



Teie Android-telefon peab olema võimeline jõudma teie Bitcoin sõlmpunktini kohalikus võrgus. Leidke oma arvuti IP-aadress:



**On macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Lihtne alternatiiv:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Linuxis** :



```bash
hostname -I | awk '{print $1}'
```



**Windowsi puhul** :



```cmd
ipconfig
```



Leia IPv4-aadress (formaat `192.168.x.x.x` või `10.0.x.x.x`)



### RPC konfiguratsioon



#### bitcoin.conf redigeerimine



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Leidke oma "bitcoin.conf" fail:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Avage fail oma lemmiktekstiredaktoriga ja lisage see konfiguratsioon RPC serveri aktiveerimiseks.



**Soovitatav konfiguratsioon alustamiseks (järjehoidja)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** konfiguratsioon (tootmiskasutuseks) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Tähtis** :




- Signet on väga soovitatav** esimesteks testideks: rakendus on veel arenduses (beeta) ja vigu võib veel esineda. Signet võimaldab teil tasuta testida, ilma et riskiksite reaalsete rahaliste vahenditega
- Asendage `192.168.1.0/24` oma võrgu alamvõrguga (nt kui teie IP on `192.168.68.57`, kasutage `192.168.68.0/24`)



**Turvalisus**: Loo tugev parool :



```bash
openssl rand -base64 32
```



### Initsialiseerimine



#### Taaskäivitage ja kontrollige



1. Lülita Bitcoin Core täielikult välja


2. Käivitage see uuesti, et rakendada konfiguratsiooni




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Kui Bitcoin Core esimest korda käivitub, laeb ta alla ja sünkroonib järjehoidja plokiahelat. See toiming on palju kiirem kui mainnet puhul (ainult mõni minut). Enne jätkamist oodake, kuni sünkroniseerimine on lõpetatud.



![CRÉATION DE WALLET](assets/fr/04.webp)



Kui olete sünkrooninud, looge uus portfell, klõpsates nupule "Create a new wallet". Andke sellele selgesõnaline nimi, näiteks `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Teie wallet on nüüd loodud ja valmis vastu võtma testimiseks järjehoidja bitcoin'e.



#### Saada järjehoidja bitcoinid (test)



Et testida Joinstr-i järjehoidjat, vajate tasuta test bitcoins :



![SIGNET FAUCET](assets/fr/06.webp)



Kasutage avalikku järjehoidjat nagu :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Bitcoin Core, generate uus vastuvõtu aadress ("Receive" vahekaart), kopeeri see ja kleebi see kraanivormi. Lahendage vajaduse korral captcha. Saate tasuta järjehoidja bitcoinid mõne sekundi jooksul.



## Androidi rakendus



### Paigaldamine



![APPLICATION ANDROID](assets/fr/07.webp)



Mine [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases), et laadida alla uusim APK versioon. Laadige fail alla oma Androidi brauseris, seejärel avage see, et käivitada paigaldus. Vajaduse korral peate oma telefoni turvasätetes lubama installimist tundmatutest allikatest.



### Rakenduse konfiguratsioon



![PERMISSIONS VPN](assets/fr/08.webp)



Esimesel käivitamisel küsib Joinstr rakendus sisseehitatud VPN-i kontrollimiseks õigusi. Võtke mõlemad õiguste taotlused vastu: OpenVPN-i juhtimine ja VPN-ühendus. Need õigused on vajalikud VPN-i integreerimiseks, mis kaitseb teie võrgu privaatsust.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr rakendus on jaotatud kolmeks peamiseks vahekaardiks:




- Kodu**: Avakuva
- Basseinid**: CoinJoin basseinide loomine ja haldamine
- Seaded**: Rakenduse konfiguratsioon



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigureerige seaded vahekaardil "Seaded":



**1. Nostr relee**: Nostr relee aadress basseinide koordineerimiseks




- Näide: `wss://relay.damus.io`
- Muud soovitatavad releed: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Tähtis**: Kõik osalejad peavad kasutama **sama Nostr relee**, et näha ja liituda samade basseinidega. Kui kasutate teistsugust releed, ei näe te teistes releedes loodud basseinid



**2. Sõlme URL**: Teie Bitcoin sõlme IP-aadress (ilma portita)




- Formaat: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC kasutajanimi** : Kasutajanimi, mis on konfigureeritud teie bitcoin.conf-s `rpcuser=`




- Näide: `satoshi



**4. RPC Parool** : Parool, mis on määratud bitcoin.conf-s `rpcpassword=`



**5. RPC port** : RPC port sõltuvalt võrgust




- Mainnet** : `8332`
- Järjehoidja**: `38332`



**6. Wallet**: Valige Bitcoin Core portfell, mis sisaldab segatavaid UTXOsid




- Näide: `tuto_joinstr_signet`



**7. VPN Gateway**: Valige Riseup VPN server




- Näide: `(Paris) vpn07-par.riseup.net`
- Teised saadaval: Amsterdam, Seattle jne.
- ⚠️ **Tähtis**: CoinJoin-s osalemiseks peavad kõik samas koondis osalejad kasutama **sama VPN-ühendust**. Segamisvooru ajal peavad kõik osalejad ilmuma sama väljumis-IP-aadressiga, et võrguanalüüs ei saaks osalejaid omavahel seostada



Rakendus Joinstr **integreerib algselt** Riseup VPN-i, lihtsustades osalejate vahelist koordineerimist.



**Tähtis** :




- Veenduge, et teie telefon ja arvuti on samas kohalikus WiFi-võrgus
- VPN-ühendus aktiveeritakse automaatselt, kui osalete koondamises
- Kui olete kõik parameetrid seadistanud, klõpsake **"Salvesta "**



## Praktiline kasutamine



### Luua bassein või liituda sellega



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Teil on kaks võimalust CoinJoin-s osalemiseks:



**Võimalus 1: uue basseini loomine**



Klõpsake vahekaardil "Poolid" nuppu "Create New Pool". Määrake nimiväärtus BTC-des (nt 0,002 BTC) ja soovitud osalejate arv (minimaalselt 2, suurema anonüümsuse tagamiseks soovitatakse 3-5). Seejärel ootab rakendus teisi kasutajaid, kes teie basseiniga liituksid. Kui nõutav arv on saavutatud, algab automaatselt väljundregistreerimine ja te peate valima oma UTXO segamiseks ja klõpsama nupule "Registreeri".



**⏱️ Oluline**: Basseinid aeguvad pärast **10-minutilist** tegevusetust. Kui nõutavat osalejate arvu ei saavutata, suletakse bassein automaatselt.



**Võimalus 2: liituda olemasoleva basseiniga**



Vaatelehel "Muude basseinide vaatamine" saate sirvida teiste kasutajate loodud basseinid. Valige oma summale vastav bassein ja liituge sellega. Veenduge, et olete konfigureerinud sama Nostr relee ja VPN Gateway kui teised osalejad (vt jaotist Configuration).



**UTXO valikureegel**: Teie UTXO peab olema veidi suurem kui koondnimetus (vahemikus +500 kuni +5000 sats ülejääk).



**näide**: Kasutage 0,002 BTC (200 000 sats) suuruse reservi puhul UTXO vahemikus 200 500 ja 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Seejärel on protsess **täiesti automaatne**: kui teie sisend on registreeritud, ootab rakendus, et kõik osalejad registreeriksid oma sisendi. Kui kõik sisendid on registreeritud, luuakse PSBT, mis allkirjastatakse automaatselt teie võtmetega ja ühendatakse seejärel teiste osalejate allkirjadega. Lõpuks edastatakse kogu tehing Bitcoin võrgus. Kui ülekanne on lõpetatud, saate TXID (tehingu identifikaator). Androidi puhul ei ole vaja PSBT käsitsi manipuleerida.



### on-chain kontroll



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Kui tehing on edastatud, saate TXID (tehingu identifikaator). Vaadake seda [mempool.space](https://mempool.space) või oma lemmik brauseris. Proovimiseks järjehoidjas kasutage [mempool.space/signet](https://mempool.space/signet).



Saate jälgida :





- N sissekannet**: Üks iga osaleja kohta (meie näites 2 sissekannet)
- N identset väljundit**: täpne nimiväärtus (siin 2 väljundit, igaüks 0,00199800 BTC)
- Voolukaart**: mempool.space näitab visuaalselt sisendite ja väljundite kombinatsiooni
- Omadused** : Tehingut saab identifitseerida kui SegWit, Taproot, RBF jne.



Kuna kõigil põhiväljunditel on sama summa, siis on **mõeldamatu kindlaks teha, milline neist kuulub kellele**. See on CoinJoin põhiprintsiip: väljundite eristamatus.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Pöörake tähelepanu**: Kui teie UTXOd olid suuremad kui koondnomenklatuur, siis on teil valuutaväljaminekud (ülejäägid). Need vahetuskursi UTXOd jäävad jälgitavaks ja neid tuleb hallata eraldi teie anonüümsetest väljunditest. Ärge kunagi ühendage neid oma segaväljunditega.



## CoinJoin kvaliteedi ja anonüümsuse paketid



CoinJoin tõhusust mõõdetakse selle **anonseti** järgi: tehingu käigus toodetud identse väärtusega väljundite arv. Mida suurem on see arv, seda raskem on kindlaks teha, milline sisend vastab millisele väljundile.



Joinstr genereerib praegu keskmiselt **2 kuni 5 osalejat**. Need arvud on väiksemad kui traditsioonilistel tsentraliseeritud koordinaatoritel nagu Wasabi (50-100 osalejat) või Whirlpool (5-10 osalejat), kuid see on detsentraliseerimise hind.



💡 **Anonüümsuskomplektide ja nende arvutamise üksikasjalikuks mõistmiseks** vt meie täielikku kursust: [Anonüümsuskomplektid](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. teised CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Muud aktiivsed CoinJoin lahendused** :




- Ashigaru**: Whirlpool protokolli avatud lähtekoodiga rakendamine tsentraliseeritud koordinaatoriga, kuid detsentraliseeritult rakendatav. Jätkab tegevust pärast Samourai Wallet hõivamist 2024. aastal.
- JoinMarket**: Detsentraliseeritud P2P lahendus ilma keskse koordinaatorita, mis põhineb tegija/võtja ärimudelil, kus "tegijad" pakuvad likviidsust ja "võtjad" maksavad neile tasu.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Põhimõtteline kompromiss**: Joinstr ja JoinMarket on ainsad kaks lahendust ilma keskse koordinaatorita. JoinMarket kasutab P2P ärimudelit koos rahaliste stiimulitega, samas kui Joinstr kasutab Nostr'i tasuta koordineerimiseks. Joinstr ohverdab kohese suuremahulise anonüümsuse lihtsuse (tegija/võtja haldamise puudumine) ja koordineerimistasude täieliku puudumise kasuks.



**Praktiline soovitus**: Kompenseerimaks väiksemaid võistluskogumeid, korraldage mitu järjestikust CoinJoin vooru erinevate osalejatega. Jagage oma voorud ja vahetage iga vooru vahel Nostr-releed, et maksimeerida oma konfidentsiaalsust.



Lisateavet selle teema kohta leiate meie täielikust kursusest Bitcoini privaatsuse kohta:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Eelised ja piirangud



### Tähtsündmused



**Tihedam privaatsus**: Nostr-side krüpteerimise, osalejate vahelise jagatud VPN-i ja Tori soovitatud kasutamise kombinatsioon loob mitmekihilise kaitse, millest on raske mööda minna.



** Läbipaistev, minimaalsed kulud**: Koordineerimiskulud puuduvad, ainult mining kulud jagatakse osalejate vahel võrdselt. Ükski operaator ei võta protsente.



### Piirangud, millega tuleb arvestada





- Muutuv likviidsus**: Väiksemad basseinid, võivad oodata osalejate kokkutulekut
- Käimasolev projekt**: Rakendus on beetaversioonis, vead võimalikud. Testi kõigepealt väikeste summade kohta järjehoidja
- Sybil ründab**: Võimalus, et üks vastane kontrollib mitut basseinis osalejat



## Parimad tavad



**UTXO isolatsioon**: Ärge kunagi ühendage segatud UTXO segamata UTXO-ga. Kasutage anonüümsete väljundite jaoks eraldi portfelli.



**Monitoorne mängimine on oluline**: Teha vähemalt 3 järjestikust vooru erinevate osalejatega. Varieerige koguseid ja ajastust, et vältida mustreid. Vahetage voorude vahel mitu tundi.



**Võrgu kaitse**: Kasutage lisaks sisseehitatud VPN-le süstemaatiliselt Tor'i. Looge efemeriaalseid Nostr-võtmeid iga olulise seansi jaoks.



**Vaiksed edusammud**: Alustage järjehoidjate lisamist väikeste kogustega.



## Kokkuvõte



Joinstr kujutab endast tõeliselt detsentraliseeritud Bitcoin privaatsuslahendust. Kasutades koordineerimiseks Nostr-i, kaotab see sõltuvuse kesksetest koordinaatoritest, säilitades samal ajal kasutajate suveräänsuse.



**Kasutajatele, kes hindavad tsensuurivastasust ja on valmis teostama mitu CoinJoin ringi, et kompenseerida väiksemaid pooli.



Kasvava finantskontrolli taustal on detsentraliseeritud vahendid eraelu puutumatuse kaitsmiseks muutumas hädavajalikuks.



## Ressursid



### Ametlikud dokumendid




- [Joinstr ametlikul kodulehel](https://joinstr.xyz)
- [Kasutaja dokumentatsioon](https://docs.joinstr.xyz/users/using-joinstr)
- [Tehniline dokumentatsioon](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLabi lähtekood](https://gitlab.com/invincible-privacy/joinstr)
- [Androidi rakendus](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutorials




- [Electrum plugin õpetus](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Uncensored Techi täielik juhend



### Ühendus ja toetus




- [Telegram Joinstr Group](https://t.me/joinstr) - Ühenduse toetus ja järjehoidja nurgad
- [Tehniline arutelu DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Lisavahendid




- [järjehoidja Faucet](https://signetfaucet.com) - Tasuta test Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternatiivne versioon
- [Mempool.space](https://mempool.space) - Block explorer koos eraelu puutumatuse analüüsiga