---
name: Zeus Embedded - Täiustatud
description: Mitme sõlmega isehallatav Lightning rahakott
---

![Zeus](assets/cover.webp)


## ZEUS Wallet tutvustus


ZEUS on mobiilne Bitcoin Wallet ja sõlmede haldamise rakendus, millel on Bitcoin välk Wallet täisfunktsionaalsus, mis muudab Bitcoin maksed lihtsaks, annab kasutajatele täieliku kontrolli oma rahaasjade üle ja võimaldab edasijõudnud kasutajatel hallata oma välgussõlmi peopesast.


### Kellele on ZEUS mõeldud?

Praegu on ZEUS mõeldud inimestele, kes käitavad omaenda kodu- või ärisõlmi [Lightning Network Daemon (LND)](https://lightning.engineering/) või [Core Lightning (CLN)](https://blockstream.com/lightning/) ning haldavad neid Zeus'i kaudu eemalt.


Kauplejad, kes kasutavad [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) või [Alby](https://getalby.com/) (või mõnda muud LNDhub kontot), saavad samuti ühendada, kasutada ja hallata oma sõlmi / kontosid ZEUSi kaudu.


[Alates v0.8 versioonist](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) hakkab ZEUS teenindama tavakasutajaid, kes soovivad lihtsalt kiireid ja odavaid bitcoini makseid teha oma mobiilseadmest, kasutades [sisse-ehitatud mobiilset Lightning sõlme](https://docs.zeusln.app/category/embedded-node) koos integreeritud [Lightning teenusepakkujaga (LSP)](https://docs.zeusln.app/lsp/intro).


### Olulised Zeuse ressursid:


- Zeus ametlik kodulehekülg - [https://zeusln.app/](https://zeusln.app/)
- Zeus dokumentatsioon - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Githubi hoidla](https://github.com/ZeusLN/zeus)
- [Zeus Telegrami tugigrupp](https://t.me/ZeusLN)
- [Zeus NOSTR-is](https://iris.to/zeus@zeusln.app)
- [Zeus blogi teadaanded](https://blog.zeusln.com)


### Zeusi omadused

#### Üldised omadused:


- Iseseisvad, ainult Bitcoin ja Lightning Wallet
- Ei töötlemistasusid, ei KYC
- Täielikult avatud lähtekoodiga (APGLv3)
- Mitme sõlme / kontode toetamine (saate hallata oma kodusõlme(d), käivitada varjatud LND sõlme, ühenduda mitme LNDhubi kontoga)
- Lihtsalt kasutatav tegevusmenüü
- PIN või passphrase krüpteerimine, privaatsusrežiim - varjata oma tundlikke andmeid
- Kontaktraamat, mitmeteemaline, mitmekeelne


#### Tehnilised omadused


- Ühendage üle Tor'i
- Täielik LNURL tugi (maksmine, tagasivõtmine, auth, kanal), saatmine Lightning aadressidele
- Detailne valgustuskanali haldamine, MPP/AMP tugi, Keysend, marsruutimistasude haldamine
- Replace-by-fee (RBF) ja "laps maksab vanema eest" (CPFP) toetus
- NFC-maksed ja -päringud, sõnumite allkirjastamine ja kinnitamine
- SegWit ja Taproot toetus
- Lihtsad Taproot kanalid
- Iseseisvad välguaadressid (@zeuspay.com)
- Müügipunkt Square'i poolt (varsti avatud PoS)


### Juhendid ja videoõpikud

Selleks, et olla võimeline kasutama Zeus ja hallata Lightning kanaleid, likviidsust, tasusid jne, on parem lugeda kõigepealt mõned olulised juhendid Lightning Network kohta.


#### Juhendid:


- [LND - Lightning Network Daemon dokumentatsioon](https://docs.lightning.engineering/)
- [CLN - Core Lightning dokumentatsioon](https://lightning.readthedocs.io/index.html)
- [Algajate Lightning juhend](https://bitcoiner.guide/lightning/) – autor: Bitcoin KKK
- [Lightning sõlme haldus](https://www.lightningnode.info/) – autor: openoms
- [Lightning Network ja lennujaama analoogia](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Lightning sõlme likviidsuse haldamine](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Lightning sõlme hooldus](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### BTC Sessionsi videoõpetus


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Juhend, kuidas alustada Zeus LN varjatud sõlme kasutamist oma mobiilseadmes


![Image](assets/en/01.webp)


Pühendan selle juhendi kõigile neile uutele Lightning Network (LN) kasutajatele, kes soovivad alustada uut suveräänset teekonda, kasutades oma mobiilseadmete Wallet isehaldussõlme.


Oletame, et te juba läbite kogu selle hulga eestkoste LN rahakotte, kuid te ei ole veel valmis alustama PUBLIC routing LN sõlme käivitamist, vaid soovite lihtsalt rohkem Sats-i üle LN-i kuhjata isemoodi ja teha oma regulaarsed maksed üle LN-i.


Siin tuleb Zeus, alates [versioonist v0.8.0, mis kuulutati välja nende blogis](https://blog.zeusln.com/new-release-zeus-v0-8-0/), ning nüüd pakub ta rakendusse sisseehitatud LND sõlme. Seni oli Zeus kaug-sõlmede haldamise rakendus + LNDhub kontod. Aga nüüd… sõlm on telefonis!


![Image](assets/en/02.webp)


### Kiire kokkuvõte Zeus Node'i peamistest funktsioonidest:



- **Privaatne LND sõlme** - See tähendab, et see sõlme EI tee teiste maksete avalikku marsruutimist teie sõlme kaudu. Sõlm ja kanalid on teatamata (privaatne, ei ole nähtav avalikus LN graafikus). Et saada ja teha makseid tehakse põhjalikult oma ühendatud LSP eakaaslased. **MÄRKUS: Zeus Embedded Node EI tee avalikku marsruutimist!**
- **Püsiv LND teenus** - kasutaja saab selle funktsiooni aktiveerida ja hoida LND teenust pidevalt aktiivsena nagu iga tavalist LN sõlme. Rakendus ei pea olema avatud, püsiv teenus hoiab kogu suhtluse võrgus.
-   **Neutrino plokifiltrid** - plokkide sünkroonimine toimub [plokifiltrite ja Neutrino protokolli](https://bitcoinops.org/en/topics/compact-block-filters/) abil (ilma meie kasutajate on-chain vahendite kohta teavet andmata). Meeldetuletus: kõrge latentsuse / aeglase internetiühenduse korral võib see Neutrino-põhine plokkide sünkroonimine mõnikord ebaõnnestuda. Katse lülituda lähimale Neutrino serverile võib aidata sünkroonimist taastada. Ilma selle sünkroonimiseta ei saa teie LND sõlm käivituda!
- **Lihtsad Taproot kanalid** - Nende kanalite sulgemisel on kasutajatel vähem tasusid ja neil on rohkem privaatsust, kuna nad näivad oma On-Chain jalajälge uurides olevat nagu kõik teised Taproot kulutused.
- **Integreeritud LSP** - Olympus on Zeuse uus LSP-sõlm. Kasutajad saavad kohe Sats üle LN uuesti vastu võtta, ilma et nad peaksid eelnevalt LN kanaleid seadistama. Lihtsalt tuleb luua LN Invoice ja maksta mõnest teisest LN Wallet, Zeus 0-conf kanaliteenusega. Lisateavet Zeus LSP kohta leiate siit. LSP pakub meie kasutajatele ka täiendavat privaatsust, pakkudes neile pakendatud arveid, mis varjavad maksjate eest nende sõlmede avalikke võtmeid.
- **Kontaktide raamat** - saate salvestada käsitsi kontakte või importida neid NOSTRist, et saate hõlpsasti saata makseid oma tavalistele sihtkohtadele.
- **Täielik toetus LNURL, LN Address saatmine ja vastuvõtmine** - nüüd saate @zeuspay.com abil luua omaenda LN Address iseteeninduse. Meeldetuletus: Võite kasutada Zeust ka LN-auth jaoks saitidel, kus saate sisse logida LN autentimisega. On väga mugav.
- **Müügipunkt** - Nüüd saavad kaupmeeste kasutajad luua oma tooteid ja müüa otse Zeusist koos integreeritud müügipunktiga. Hetkel sisaldab põhilisi vajadusi, kuid tulevikus sisaldab laiendatud funktsioone.
- **LND logid** - kasutaja saab reaalajas lugeda LND teenuse logisid ja kasutada neid võimalike probleemide kõrvaldamiseks (peamiselt halbade ühenduste puhul)
- **Automaatne varundamine** - LN sõlme kanalid varundatakse automaatselt Olympuse serveris. See automaatne varundus on krüpteeritud koos teie sõlme Wallet seed (ilma seed on täiesti kasutu). Kasutaja saab ka käsitsi eksportida SCB (staatiliste kanalite varukoopia) katastroofi taastamiseks.


### Kuidas saada pardale Zeus LN Node (LND embedded)


Selles juhendis räägin ainult sisseehitatud LND sõlmest, mitte teistest viisidest, kuidas seda suurepärast rakendust kasutada (kaug-sõlmede haldamine ja LNDhub kontod). Teiste ühenduste tüüpide jaoks vaadake palun [Zeus dokumentatsiooni lehte](https://docs.zeusln.app/category/getting-started), mis on väga hästi selgitatud ja ei vaja eraldi juhendit.


#### SAMM 1 - ESIALGNE SEADISTAMINE


Tänu sellele, et Zeus on täielik LND sõlmpunkt, on mul mõned esialgsed soovitused:



- Ärge kasutage vana seadet, see võib mõjutada selle võimsa rakenduse kasutamist. Eriti sünkroonimise ajal võib rakendus kasutada intensiivselt protsessorit ja RAM-i. Nende puudumine võib teha Zeus'i rakenduse kasutamise isegi võimatuks.
- Kasutage vähemalt Android 11 mobiilne OS ja uuendatud nii palju kui võimalik. IOS-i puhul sama, proovige kasutada palju kõrgemat OS-versiooni.
- Andmete salvestamiseks on vaja vähemalt 1 GB kettaruumi. Aja jooksul võib kasvada rohkem, kuid on olemas funktsionaalsus andmebaasi tihendamiseks MB tasemele.
- Tor või Orbot teenusega pole vaja kasutada Zeus't. Palun ärge tehke asju keerulisemaks kui vaja. Tor sel juhul ei paku teile rohkem privaatsust, vaid teeb esialgse sünkroniseerimise ainult halvemaks. Samuti olge ettevaatlik, milliseid VPN-i kasutate seda ja kontrollige ühenduse latentsust neutrino serverite suunas. Pidage meeles, Neutrino blokeerimisfilter ei leki ega jälgi teie seadme identiteeti, on lihtsalt teenindavad plokid. LN liiklus on ka LSP taga privaatseid kanaleid, nii et väga vähe teavet on välja, ei ole põhjust muretseda privaatsuse pärast.
-   Olge kannatlik algse sünkroonimise ajal, see võib võtta mitu minutit. Püüdke olla ühendatud lairiba internetiühendusega, millel on hea latentsus. Kui käitate oma Bitcoini sõlme, [saate aktiveerida neutrino teenuse](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) ja ühendada oma Zeusi oma sõlmega, isegi sisemise LAN-i kaudu, nii saavutate maksimaalse kiiruse.


Kui olete seadistanud ühenduse tüübi "Embedded node", hakkab rakendus mõnda aega sünkroonima. Oodake kannatlikult selle osa lõpetamist, seejärel sisenege peamise seadete lehele.


![Image](assets/en/03.webp)


Sukeldume lühidalt igasse seadete sektsiooni ja mõistame mõningaid põhifunktsioone, enne kui hakkate Zeust kasutama:


**A - SEADED**


See on kogu rakenduse üldisi seadeid sisaldav jaotis


**1 - Lightning Service Provider (LSP)**


Siin on esitatud kaks LSP teenust:



- _Just in time channels_ - kui teil ei ole ühtegi avatud kanalit või sissetulevat likviidsust saadaval, siis kui teenus on aktiveeritud, avab see teile kanali jooksvalt. Selle valiku saab välja lülitada, kui te ei soovi rohkem selliseid kanaleid avada.
- _Kanalite eelnev tellimine_ - saate osta sissetulevaid kanaleid Olympus LSP-st otse rakenduses, kus on mitu võimalust ja summat (sissetulevate ja väljaminevate kanalite jaoks).


LSP aitab kasutajatel ühendada Lightning-võrguga, avades maksekanaleid nende sõlmedesse. [Loe LSP kohta lähemalt siit](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS-il on uus integreeritud LSP nimega [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), mis on saadaval kõigile kasutajatele, kes kasutavad uut sisseehitatud sõlme.


Selles jaotises on vaikimisi Olympus LSP (https://0conf.lnolymp.us), kuid varsti saate määrata ka teise 0conf LSP, mis toetab seda protokolli.


pidage meeles:_

_Kui avate kanali Olympus LSP-ga, kasutades pakendatud LN arveid, saate ka 100k sissetuleva likviidsuse ! See on tõesti hea võimalus juhul, kui teil on vaja saada kohe rohkem Sats._

näide: te hoiustate 400k Sats, et avada LSP kanal, siis LSP avab 500k Sats võimsusega kanali teie Zeuse sõlme suunas ja lükkab 400k Sats, mida te hoiustate, teie poole

_"Sissetulev likviidsus" = rohkem "ruumi" teie kanalis, et saada._


Tulevikus loodame, et meil võiks olla palju teisi LSP-sid, mida saaks integreerida Zeusesse ja kasutada alternatiivselt igaüht. On vaid aja küsimus, kuni uued LSP-d võtavad vastu avatud standardi selliste 0conf-kanalite jaoks.


Kui te ei soovi uusi kanaleid "jooksvalt" avada, võite selle võimaluse keelata.


Samas jaotises on teil ka võimalus valida "taotleda lihtsaid Taproot kanaleid", kui LSP avab kanali teie Zeus-sõlme suunas. Need Simple Taproot Channels pakuvad paremat On-Chain privaatsust ja väiksemaid tasusid kanali sulgemisel. On ainult kaks põhjust, miks te ei taha neid kasutada:



- Need on uued ja nende kasutamisel võib LND-s veel vigu esineda.
- Teie vastaspool ei toeta neid. Isegi LND sõlmede puhul tuleb neid esialgu selgesõnaliselt valida.


**2 - makse seaded**


See funktsioon pakub teile võimalust määrata oma eelistatud tasud maksete tegemiseks LN või onchaini kaudu. Samuti annab võimaluse suurendada või vähendada oma arvete aegumistähtaega.


Kui mõni teie LN makse ebaõnnestub, võite suurendada tasu, et leida parem tee. Samuti, kui teete onchain txs, saate seadistada konkreetse tasu, nii et teie tx ei võiks sattuda kinni Mempool pikka aega, juhul kui kõrge tasu perioodi.


**3 - Arvete seaded**


Selles jaotises on mõned generate arvete valikud:



- Seadistage Invoice-s kuvatav standardmärkus teile generate
- Aegumistähtaeg sekundites, juhul kui soovite, et Invoice maksetähtaeg oleks pikem või lühem
- Lisage marsruudiviiteid - andke teavet reklaamimata või eraviisiliste kanalite leidmiseks. See võimaldab maksete suunamist sõlmpunktidesse, mis ei ole võrgus avalikult nähtavad. Marsruudi vihje annab osalise marsruudi vastuvõtja privaatsõlme ja avaliku sõlme vahel. See marsruutimisviide lisatakse vastuvõtja poolt genereeritud Invoicei ja edastatakse maksjale. Soovitan seda vaikimisi lubada, sest muidu võivad sissetulevad maksed ebaõnnestuda (marsruuti ei leitud).
- AMP Invoice - Atomic Multi-path Payments on uut tüüpi välkmaksed, mida rakendab LND, mis võimaldavad saada Sats ilma konkreetse Invoice-ta, kasutades [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). On praktiliselt staatiline maksekood. [Loe lähemalt siit](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Näita kohandatud eelpildi välja - kasutage seda valikut ainult väga spetsiifilistel juhtudel, kui soovite tõesti kasutada eelpildis kohandatud välju. [Loe lähemalt siit](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Teine võimalus selles jaotises on see, kuidas määrata, millist tüüpi onchain Address soovite kasutada: SegWit nested, SegWit, Taproot.


![Image](assets/en/04.webp)


Klõpsake ülemisel ratta nupul ja avaneb hüpikaken, et valida soovitud Address tüüp. Kui olete selle seadistanud, siis järgmine kord, kui vajutate onchaini vastuvõtunuppu, valib generate valitud Address tüübi. Te saate seda igal ajal muuta.


**4 - kanalite seaded**


Selles sektsioonis saate eelseadistada mõned avamiskanalite funktsioonid, nagu:



- kinnituste arv
- Announce channel (vaikimisi on välja lülitatud), see tähendab, et see on kuulutamata kanalid
- Lihtsad Taproot kanalid
- Näita kanali ostunuppu


**5 - Privaatsusseaded**


Siit leiad mõned põhilised seaded, et suurendada privaatsust Zeuse rakenduse abil:



- Block explorer avada tx üksikasjad (Mempool.space, blockstream.info või kohandatud isiklik)
- Lugeda lõikelaua - sisse/välja lülitus, kui soovite, et Zeus loeks teie seadme lõikelaua
- Lurker-režiim - sisse/välja lülitus, kui soovite varjata teatud tundlikku teavet oma Zeuse rakendusest. On hea valik, kui teete demosid või ekraanipilte.
- Mempool tasude soovitus - aktiveerige see valik, kui soovite kasutada [Mempool.space](https://Mempool.space/) soovituslikke tasumäärasid


**6 - Turvalisus**


Selles jaotises on rakenduse avamisel ainult kaks võimalust rakenduse kaitsmiseks: määrata parool või PIN-kood.


Kui olete seadnud rakenduse avamiseks PIN-koodi, saate määrata ka "sunniviisilise PIN-koodi". Seda salajast täiendavat PIN-koodi kasutatakse AINULT sundolukorras, kui teid ähvardab oht. Kui panete selle PIN-koodi, siis on kõik konfiguratsioonid WPE OUT. Nii et te parem hoida uuendatud oma varukoopiaid. Automaatsed varukoopiad on vaikimisi sisse lülitatud, kuid on hea, kui teil on ka oma varukoopiad seadmest väljas.


**7 - Valuuta**


Lülita sisse või välja võimalus näidata fiat-valuuta konverteerimist Zeuse rakenduse kasutamisel. Praegu toetab üle 30 ülemaailmse fiat-valuuta.


**8 - keel**


Saate vahetada mitme tõlkekeele vahel, mida Zeuse kogukond on läbi vaadanud koos emakeelekõnelejatega.


**9 - Kuva**


Selles jaotises saate oma Zeuse ekraani isikupärastada, valides erinevaid värvitoone, vaikimisi ekraani (klaviatuur või tasakaal), kuvada oma sõlme aliase, aktiveerida suured klahvinupud, näidata rohkem kümnendkohti.


**10 - Müügipunkt**


See on erifunktsioon, mille abil saab Zeusesse integreeritud PoS-süsteemi sisse/välja lülitada. Saate kasutada iseseisvat PoS-i või seotud Square PoS-süsteemiga. Praegu toetab põhifunktsioone kui PoS, kuid piisab heast algusest ja võiks aidata neil väikestel kaupmeestel (baarid/restoranid, toidupoed) alustada BTC vastuvõtmist emakeelena.


Selle seadistuse sees leiate mitmesuguseid võimalusi oma PoSi seadistamiseks:



- Kinnitusmakse tüüp: Ainult LN, 0-konf, 1-konf
- Nõuannete lubamine / keelamine töötajale, kes kasutab kassat
- Näidata / peita klaviatuur
- Piletile kohaldatav maksuprotsent
- Looge tooteid ja tootekategooriaid
- Lihtne loetelu kõigist müügitehingutest


Siin on live demo video, kuidas kasutada Zeus PoSi:


**B - Wallet varukoopia**


ZEUSi sisseehitatud sõlmpunkt põhineb LND-l ja kasutab [aezeed seed formaati](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). See erineb tüüpilisest [BIP39 formaadist](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki), mida näete enamikus Bitcoin rahakottides, kuigi see võib tunduda sarnane. Aezeed sisaldab mõningaid lisaandmeid, sealhulgas Wallet sünniaega, mis aitavad taastamise käigus toimuvatel kordusskaneeringutel tõhusamalt toimuda.


Aezeed võtme formaat peaks ühilduma järgmiste mobiilsete rahakottidega: Blixt, BlueWallet ja Breez. Pange tähele, et seed ainuüksi ei ole piisav, et taastada kõik teie saldod, kui teil on avatud või sulgemisjärgus kanalid !


Lisateavet varundamise ja taastamise kohta leiate [Zeus Docs page](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


VÄLJAKUTSE: Kui salvestate oma seed, salvestage ka sõlme pubkey! Mõnikord on hea, kui see on käepärast koos seed ja SCB-ga (Static Channels Backup), juhul kui teil on vaja taastada.


SCB on vajalik ainult siis, kui teil on LN kanalid avatud. Kui teil on ainult onchain vahendid, ei ole vaja.


Kui näete, et pärast pikka aega ei näita ikka veel vana ajalugu txs, mine Embedded node - Peers ja keelata võimalus kasutada nimekirja valitud eakaaslaste (vaikimisi on btcd.lnolymp.us). See käivitab taaskäivituse ja ühendab esimese kättesaadava neutrino sõlme parema ajavastusega. Või kasutage allpool mainitud teisi tuntud neutrino peereid.


Kui soovite näha rohkem taastamise võimalusi LND sõlme jaoks, [lugege minu eelmist juhendit](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), kust leiate sammud, kuidas importida aezeed seed Sparrow Wallet või muud meetodid.


**C - sisseehitatud sõlme**


Selles jaotises leiame mõned põhilised tööriistad integreeritud sõlme haldamiseks:



- _Katastroofide taastamine_ - LN kanalite automaatsed ja manuaalsed varukoopiad. Palun lugege lähemalt, kuidas seda funktsiooni kasutada Zeus Docs lehel.
- _Express Graph Sync_ - Zeuse rakendus laeb LN kuulujuttude andmegraafi alla spetsiaalsest serverist, et sünkroonimine oleks kiirem ja parem, pakkudes parimaid makseviise. Saate valida ka eelmise graafiku andmete kustutamise käivitamisel.
- _Peers_ - sektsioon neutriinode ja 0-conf peeride haldamiseks. Kui teil on probleeme esialgse sünkroniseerimisega, kanalid ei tule online, on see, et teie seadmel on suur latentsus koos konfigureeritud neutrino peeriga. Proovige vahetada eelistatud partnerite nimekirja või lisage oma konkreetne partner, mille kohta te teate, et see on sünkroonimiseks parema latentsusega. Tuntud neutrino serverid on järgmised:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - USA piirkonna jaoks
 - sg.lnolymp.us - Aasia piirkonna jaoks
 - btcd-Mainnet.lightning.computer - USA piirkonna jaoks
 - uswest.blixtwallet.com (Seattle) - USA piirkonna jaoks
 - europe.blixtwallet.com (Saksamaa) - ELi piirkonna jaoks
 - asia.blixtwallet.com - Aasia piirkonna jaoks
 - node.eldamar.icu - USA piirkonna jaoks
 - noad.sathoarder.com - USA piirkonna jaoks
 - bb1.breez.technology | bb2.breez.technology - USA piirkonna jaoks
 - neutrino.shock.network - USA piirkond



- _LND logid_ - väga kasulik vahend LN sõlme probleemide kõrvaldamiseks ja põhjalikumaks kontrollimiseks, mis toimub tehnilisel tasemel.
- _täiustatud seaded_ - rohkem vahendeid LND sõlme kasutamise kontrollimiseks:



 - _Pathfinding mode_ - bimodaalne või apriori, kuidas leida parem marsruut oma LN maksetele ja ka eelmise marsruudi teabe lähtestamine. Palun lugege neid väga häid juhendeid teeotsingu kohta: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - by Docs Lightning Engineering ja [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - by Voltage
 - _Püsiv LND_ - aktiveerige see režiim, kui soovite, et LND teenus töötaks pidevalt taustal ja hoiaks teie sõlme võrgus 24/7. See on väga kasulik, kui kasutate Zeust PoSina väikeses poes või kui saate palju LN vihjeid üle LN Address.
 - _Rescan wallet_ - see valik käivitab taaskäivitamisel teie Wallet kõigi ahelas olevate tx-de täieliku skaneerimise. Aktiveerige see ainult juhul, kui teie Wallet-st puuduvad mõned tx-d. Ülesanne rescan võtab aega, mitu minutit, nii et olge kannatlik ja vaadake alati logisid, et näha täpsemaid üksikasju edusammude kohta.
 - _Compact Database_ - see valik on väga kasulik, kui teie Zeuse rakendus võtab palju ruumi seadmes (vt rakenduse üksikasju seadme seadetes). Kui teil on Zeuse kasutamisel palju tegevust, soovitan seda tihendamist sagedamini teha. Kui näete, et teil on Zeuse rakenduse jaoks rohkem kui 1-1,5 GB andmeid, tehke tihendamine. See käivitub uuesti ja võtab aega, seega olge kannatlik.
 - _Delete Neutrino files_ - see valik neutriinofailide kustutamiseks (koos taaskäivitusega) vähendab oluliselt andmesalvestusruumi kasutamist. Andmekasutuse vähendamisel on suur mõju ka aku kasutamisele, vähendades aku kasutamist, eriti kui kasutate Zeust püsivas režiimis.


**D - sõlme info**


Selles jaotises leiate lisateavet oma Zeus-sõlme oleku kohta järgmiselt:



- Alias - lühike sõlme ID
- Avalik võti - teie sõlme täielik avalik võti, mida teised sõlmed vajavad, et leida tee teie sõlme poole. Pidage meeles, et see avalik võti EI ole nähtav tavalistel LN Exploreritel (Mempool, Amboss, 1ML jne). See avalik võti on kättesaadav AINULT teie ühendatud LN eakaaslaste ja kanalite kaudu.
- LN rakendusversioon
- Zeus rakenduse versioon
- Synced to chain ja Synced to graph status - väga olulised, mis näitavad teie sõlme õiget staatust. Kui need kaks ei näita "true", siis tähendab see, et teie sõlme sünkroonimine on veel pooleli või on probleeme sünkroonimisega. Seega on soovitatav vaadata oma LND logisid või oodata veel natuke aega.
- Ploki kõrgus ja Hash - näitab viimast plokki ja Hash, mida teie sõlm nägi ja sünkroonis.


**E - võrguteave**


Selles jaotises kuvatakse rohkem üksikasju Lightning Network üldise oleku kohta, mis on saadud teie graafi sünkroonimisandmetest: olemasolevate avalike kanalite arv, sõlmede arv, zombikanalite arv (offline või surnud), graafi läbimõõt, graafi keskmine ja maksimaalne kraad.


Need andmed võivad olla kasulikud vigade kõrvaldamiseks või lihtsalt statistika tegemiseks.


**F - välk Address**


Selles jaotises võib kasutaja luua omaenda enesehoolduse LN Address @zeuspay.com.


ZEUS PAY kasutab kasutaja loodud eelpildi hashide, HODL arveid ja Zaplocker Nostr tõendamisskeemi, et võimaldada kasutajatel, kes ei pruugi olla 24/7 võrgus, saada makseid staatilisele välk Address-le. Kasutajad peavad lihtsalt 24 tunni jooksul oma ZEUSi rahakotti sisse logima, et makseid nõuda, vastasel juhul tagastatakse need saatjale.


Kui te aktiveerite "püsiva režiimi", saavad kõik maksed LN Address koheselt kätte.


Lugege, kuidas [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) maksed toimivad ja rohkem [ZeusPay tasude kohta siit](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain aadressid**


Selles jaotises võite konsulteerida oma genereeritud onchain aadressid parema mündi kontrollimiseks


**H - Kontaktid**


Zeus v 0.8.0 tutvustas uut kontaktraamatut, mida saab kasutada maksete kiireks saatmiseks oma sõpradele ja pereliikmetele, samuti on võimalik importida oma kontakte Nostrist.


Sisestage lihtsalt oma Nostr npub või inimloetav NIP-05 Address ja ZEUS küsib Nostrilt kõiki teie kontakte. Sealt saate saata kontaktile kiire makse või importida kõik või valitud kontaktid oma kohalikku kontaktraamatusse./<<


Siin on lühike video, kuidas konfigureerida ja kasutada oma Zeuse kontakte:


**I - Tööriistad**


Siin on erinevaid alajaotusi, kus on rohkem vahendeid:



- _Accounts_ - siin saate importida väliseid kontosid / rahakotte, Cold rahakotte, Hot rahakotte, et kontrollida või kasutada oma Zeus-sõlme kanalite välise rahastamisallikana. See funktsioon on veel eksperimentaalne.
- _Tehingu kiirendamine_ - See funktsioon võib olla kasulik, kui teil on takerdunud tx Mempool-sse ja soovite tasu tõsta. Te peate esitama tx väljundi tx üksikasjadest ja valima soovitud uue tasu, mida soovite kasutada. Peab olema kõrgem kui eelmine ja nõuab, et teil oleks rohkem vahendeid saadaval teie onchain Wallet.


![Image](assets/en/05.webp)


Te peate minema oma ootava tx juurde ja kopeerima txid väljundpunkti. Siis tule siia ja kleebi see sisse, seejärel vali uus tasu, mida soovid kasutada, et seda pumbata. See avab uue ekraani soovitatud tasudega sel hetkel või saate määrata kohandatud tasud. Pea meeles, et PEAB olema kõrgem kui eelmine.


On alati parem hoida UTXO koos maksimaalselt 100k Sats oma Zeus onchain Wallet, et oleks võimalik kasutada seda bump tasud, kui on vaja.



- _Signeeri või kinnita_ - Selle funktsiooniga saate allkirjastada konkreetse sõnumi oma Wallet võtmetega. Samuti saab seda funktsiooni kasutada sõnumi kontrollimiseks, et tõestada, et see pärineb konkreetselt Wallet võtmelt.
- _Vääringu konverter_ - lihtne vahend BTC ja teiste fiat-valuutade vahelise vahetuskursi arvutamiseks.


**J - kaubad ja toetus**


Siit leiad rohkem infot ja linke Zeuse, veebipoe, sponsorite ja sotsiaalmeedia kohta.


**K - Abi**


Selles viimases jaotises leiate lingid Zeuse dokumentatsioonilehele, Githubi probleemidele (kui soovite esitada vea või taotluse otse rakenduse arendajatele), e-posti toele.



### SAMM 2 - ZEUSE SÕLME KASUTAMISE ALUSTAMINE



Pea meeles, et Zeus on peamiselt mõeldud kasutamiseks LN Wallet, lihtsate ja kiirete maksete tegemiseks üle LN. Muidugi, see sisaldab ka onchain Wallet, kuid seda tuleks kasutada ainult LN kanalite avamiseks / sulgemiseks ja mitte regulaarsete maksete kohvi.


Palun lugege minu teist juhendit [kuidas olla oma pank, kasutades Stash 3 taset](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Sel hetkel on kasutajal 2 võimalust Zeusi kasutamist alustada:



- Otse üle LN, kasutades Olympuse LSP 0-konf-kanalit
- Hoiustage esmalt onchain Wallet ja seejärel avage tavaline LN kanal koos soovitud partneriga.


#### Meetod A - Olympus LSP kasutamine


See on väga lihtne ja lihtne viis, kuidas uus LN kasutaja Zeusesse sisse viia. See võib olla täiesti uus Bitcoin kasutaja, kellel ei ole Sats üldse, keda sõber või uus kaupmees, kes alustab oma 1. LN maksega.


Vaikimisi kasutab Zeus oma LSP-d, Olympus. Kuid hiljem saate kanalite avamiseks lülituda ka teiste LSP-de peale, mis toetavad seda 0-conf protokolli.


Luues oma Zeusesse lihtsalt Invoice (sisestage summa ja vajutage nupule "taotlus"), saate need Sats kohe kätte.


Invoice teile generate on [pakitud](https://docs.zeusln.app/lsp/wrapped-invoices) ja teile esitatakse teenusega seotud tasud, kui need on makstud. See pakitud Invoice sisaldab marsruudi vihjeid teie Zeus-sõlme suunas, nii et LSP võiks leida teie uue sõlme ja avada kanali uute rahaliste vahenditega, mida te hoiustate.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Selleks, et saada LN kanali LSP-lt raha, mida soovite saada 1. korda, tuleb see Invoice maksta teisest LN Wallet ja oodata paar hetke, kuni LSP avab kanali teie Zeus-sõlme suunas, arvata maha tasu ja lükata ülejäänud summa makse teie poole kanali.


Kõik, mida peate tegema, on maksta Invoice, mis on teie jaoks ZEUSis loodud teise välk Wallet, ja teie kanal avaneb kohe. [Palun tutvuge Zeus LSP tasudega](https://docs.zeusln.app/lsp/fees).


Teine eelis, mida kanali eest tasumine annab, on null tasu marsruutimine. See tähendab, et maksete marsruutimisel ei teki esimese hüppe puhul OLYMPUS by ZEUSi kaudu marsruutimistasusid. Pange tähele, et OLYMPUS by ZEUS'ile järgnevate teekondade eest tuleb ikkagi maksta.


Kui kanal on valmis, klõpsake ekraani allosas paremal nupul, mis kuvab Zeuse kanalid.


![Image](assets/en/08.webp)


Ja te näete sellist kanalit, mis näitab teiepoolset kanali tasakaalu:


![Image](assets/en/09.webp)


Sest rohkem kulutate sellest kanalist, rohkem sissetulevat likviidsust teil on. Mida rohkem Sats te sellesse kanalisse saate, seda vähem on teil sissetuleva likviidsuse ruumi.


Siin on kena lihtne visuaalne demonstratsioon (Rene Pickhardt) LN kanalite tööpõhimõtete kohta:


Sel hetkel, arvestades kanalite demoekraani, klõpsake kanali nimele ja näete selle kohta rohkem üksikasju.


Teil on Olympusega üks kanal, mille koguvõimsus on 490 000 Sats, kusjuures teie poolel on 378 000 Sats ja Olympuse poolel 88 000 Sats. See tähendab, et te võite samasse kanalisse saada maksimaalselt 88k Sats rohkem.


Kui teil on vaja saada rohkem kui 88k Sats (olemasolev sissetulev likviidsus antud juhul), ütleme, et veel 500k Sats, siis lihtsalt uue LN Invoice loomisega selle kogusega käivitub uus kanali taotlus Olympus LSP-le. Nii et saate 2. kanali.


Seetõttu, et vältida mitme kanali avamise eest suurema tasu maksmist, on soovitatav avada kõigepealt suurem kanal, ütleme 1-2M Sats. Kui see on avatud, võite vahetada osa neist Sats kanalitest, ütleme 50%, kasutades selleks mõnda käesolevas juhendis kirjeldatud välist vahetusteenust.


Kui te vahetate sellest kanalist välja ütleme 50% ja saate Sats tagasi oma Zeus onchain Wallet, olete valmis liikuma järgmise meetodi juurde uue kanali avamiseks - onchaini tasakaalust.


#### Meetod B - oma ahelasaldo kasutamine


Selle meetodi abil saate avada kanaleid mis tahes teise LN sõlme, sealhulgas sama Olympuse LSP poole. Aga kui teil on juba kanal Olympus on soovitatav, et on ka teise sõlme, suurema usaldusväärsuse ja ka võiks kasutada MPP (multi-part makse).


![Image](assets/en/10.webp)


Ülaltoodud on näide LN Invoice maksmisest MPP abil. Nagu näete, on ekraani allosas "seaded" ja avaneb rippmenüü, kus on rohkem üksikasju makse kohta, mida te kavatsete teha. Sellel ekraanil, kui teil on vähemalt 2 kanalit avatud, on MPP-funktsioon vaikimisi sisse lülitatud. Samuti saate aktiveerida AMP (atomic multi-path) ja määrata konkreetsed osad, mida soovite. See on võimas funktsioon!


Erasõlme jaoks nagu Zeus, soovitaksin omada 2-3 head kanalit (max. 4-5), heade LSP-de ja hea likviidsusega, et katta kõik teie vajadused, et maksta või saada Sats üle LN. [Vt rohkem nõuandeid LN-sõlme likviidsuse kohta selles juhendis](/nodes/managing-lightning-node-liquidity-en.html). Samuti siin veel üks [üldine juhend LN likviidsuse kohta](https://Bitcoin.design/guide/how-it-works/liquidity/) Bitcoin disainimeeskonnalt.


Ma tean, et õigete eakaaslaste valimine ei ole lihtne ülesanne isegi kogenud kasutajatele. [Nii et ma annan teile mõned võimalused alustuseks](https://github.com/ZeusLN/zeus/discussions/2265), need on peer-sõlmed, mida ma ise katsetasin Zeuse abil (püüdsin ühendada ainult LND sõlmedega, et vältida ühilduvusprobleeme)


Siin on ka nimekiri Zeuse jaoks garanteeritud sõlmede võrdsetest partneritest. Kui te teate häid, võite neid sellesse nimekirja lisada.


Kanalit saate Zeusis avada, kui lähete kanalite vaatesse, klõpsates peavaate alumises paremas nurgas oleval kanali ikoonil ja seejärel vajutades paremas ülemises nurgas olevale + ikoonile.


![Image](assets/en/11.webp)


Kui soovite avada kanali konkreetse sõlme, klõpsake (A) ülemises nurgas, et skaneerida sõlme QR nodeID (Mempool, Amboss, 1ML puhul saate selle QR-i) ja kõik partneri andmed täidetakse.


MEELDE:


- Zeus embedded node ei kasuta Tor teenust ! Seega ärge proovige avada kanaleid Tor-i all olevate sõlmedega! Te teete endale rohkem kahju kui lisate rohkem privaatsust. Tor LN jaoks ei paku rohkem privaatsust, vaid lisab rohkem probleeme.
- valige targalt oma eakaaslasi, parem on head LSP-d, head marsruutimise sõlmed, mitte juhuslikud pleb sõlmed, mis võivad sulgeda teie kanalid ja ei suuda pakkuda head likviidsust. [Siin ma kirjutasin spetsiaalse juhendi](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) likviidsuse ja sõlmede näite kohta.


Kui klõpsate otse nupule "Open Channel to Olympus", täidetakse vajalikud väljad, et avada kanal [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Erinevalt tasulistest LSP-kanalitest nõuab teie kanal On-Chain kinnitust, kasutades oma ahelas olevaid vahendeid (saate valida oma UTXOde hulgast avatud kanali vaates); see ei avane koheselt. Palun vaadake kõigepealt tegelikke Mempool tasusid ja kohandage neid vastavalt, sõltuvalt sellest, kui kiiresti soovite selle kanali avada.


Enne kanali avamise nupu vajutamist libistage edasijõudnute valikuid:


![Image](assets/en/12.webp)


Samuti peate veenduma, et kanal on etteteatamata (privaatne). Vaikimisi on see valik väljakuulutatud kanalite puhul välja lülitatud. Seda valikut ei soovitata Zeuse varjatud sõlme puhul aktiveerida, see on kasulik ainult siis, kui kasutate Zeust koos oma kaugseade sõlme kui avaliku marsruutimise sõlme.


Erinevalt tasulistest LSP-kanalitest ei saa te selle meetodi abil kanalite avamisel kasu nulltasu marsruutimisest.


Ja valmis, klõpsake lihtsalt nupule "Open Channel", oodake, et kaevurid kinnitaksid tx. Kui kanal on avatud, saate oma kanalitest Sats-ga soovi korral tehinguid teha.


Pidage meeles, et need kanalid on kogu saldo teie poolel, nii et teil ei ole sissetulevat likviidsust. Nagu ma juba ütlesin, vahetage välja või kulutage mõned Sats ostes asju üle LN, et "teha rohkem ruumi", et saada.


Mõelge oma LN kanalitest kui klaasist veest. Te valate tühja klaasi (teie kanalisse) vett (Sats), kuni see täitub. Te ei saa valada rohkem vett, kuni te ei joo seda (kulutate/vahetate välja). Kui klaas on peaaegu tühi, valage sinna rohkem vett (Sats), kasutades sisse vahetamist. [Lisateave välise vahetuse kohta siin](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


On ka teisi LSP teenuseid, mis müüvad teile sissetulevaid kanaleid: LNBig või Bitrefill. Ma arvan, et on rohkem teenuseid nagu need, kuid ei mäleta neid praegu.


Seega, kui teil on vaja praktiliselt tühja LN kanalit (saldo on algusest peale 100% vastastikku), et saada rohkem makseid, kui te suudate oma olemasolevatel täis kanalitel vastu võtta, võib see olla väga hea valik. Te maksate nende kanalite avamise eest kindlat tasu ja saate palju sissetulevat ruumi.



## NÄPUNÄITEID JA NIPPE


### Sissetuleva reservi piirmäärad


Praegu ei ole mõne LN koodi piirangute tõttu võimalik saada täpselt, kui palju kuvatakse "Sissetuleku". Pidage alati meeles, et te peaksite oma arveid koostama veidi väiksema summaga, vastavalt "Channel Local Reserve" summale.


![Image](assets/en/13.webp)


Nagu näete ülaltoodud pildil, näitab "sissetulev", et ma võin endiselt saada 5101 Sats, kuid tegelikult on sel hetkel võimatu saada rohkem. Ja te võite täheldada, et see on sama palju kui "Kohalik reserv".


Seega pidage meeles, et kui teete arvete vastuvõtmiseks, vaadake ka oma kanalite likviidsust ja arvestage sellest summast maha kohalik reserv, kui soovite saadaoleva summa piiridesse suruda.


### Kiire nõuanne uutele kasutajatele, kes alustavad Zeus node'iga:



- Kasutage õigesti oma uusi kanaleid.


Näiteks, kui te teate, et saate nädala jooksul, ütleme, 1M Sats, avage 2M Sats kanal ja vahetage välja onchain Wallet või teise (ajutiselt) hoiustatud LN kontole 50-60% oma väljaminevast likviidsusest. Olge alati valmis suurema likviidsusega. Kui teil on vaja rohkem likviidsust tagasi oma Zeus-kanalitesse, saate selle hoiukontodelt tagasi viia.


Kui teate, et saadate näiteks 500k Sats nädalas, siis avage 1M Sats kanal. Sel viisil on teil ikka veel reservi, kuni te seda uuesti täidate.



- Kui olete kaupmees ja saate alati rohkem, kui regulaarselt kulutate, ostke spetsiaalne sissetulev kanal. On kõige odavam viis. Te maksate minimaalset tasu ja saate "tühja" kanali.



- Ärge avage väikeseid mõttetuid kanaleid 50-100-300-500k Sats. Te täidate need mõne päevaga, isegi kui kasutate neid ainult zapside jaoks. Avage suuremaid ja erinevaid, MITTE ainult ühte kanalit.


Kui avate suurema kanali, saate alati kasutada väliseid allveelaeva vahetusi, et liigutada Sats oma onchaini rahakottidesse (sealhulgas tagasi Zeus onchaini). Tasakaalu hoidmine sisse- ja väljapoole suunatud likviidsuse vahel on hea ja samuti saate neid Sats "taaskasutada", et avada rohkem kanaleid, kui soovite.


### Pakitud Invoice


Kui soovite vastuvõtmisel lisada rohkem privaatsust, võite kasutada "pakitud Invoice" meetodit. Meeldetuletus: selleks, et seda teha, on teil vaja Olympus LSP kanalit. Pakitud arved "peidavad" lõppsihtkoha (teie Zeus-sõlme) ja näitavad maksjale sihtkohana teie LSP-sõlme.


Pakendatud Invoice saamiseks minge põhiklahvistiku ekraanile, sisestage summa ja vajutage nuppu request. Kuvatakse tavaline QR-kood teie Invoice jaoks. Nüüd klõpsake üleval paremal nupul "X" ja teid suunatakse edasi Invoice lisavõimaluste juurde.


![Image](assets/en/14.webp)


Nüüd tuleb teil aktiveerida see valik üleval "Enable LSP" ja vajutada nuppu "Create Invoice". See valik loob pakitud Invoice ja mäletage, võtab väikese tasu.


### Arved koos marsruudi vihjetega


See on väga kasulik funktsioon, kui soovite hallata mitme sissetuleva kanali likviidsust. Praktiliselt saate märkida, millisele sissetulevale kanalile soovite saada Sats Invoice-st.


Seda funktsiooni saab kasutada ka ringikujulise tasakaalustamise puhul, kui soovite liigutada likviidsust ühest täidetud kanalist teise tühjenenud kanalisse.


Kuidas luua Invoice koos marsruutide vihjetega?



- Libistage põhiekraanil LN sahtlit paremale ja klõpsake nuppu "Receive"
- Invoice seadistuses mine alumisse ossa ja aktiveeri nupp "Insert route vihjeid", seejärel vali vahekaart "Custom". See avab ekraani kõigi teie olemasolevate kanalitega. Valige see, mida soovite vastu võtta.
- Täitke kõik muud Invoice andmed, summa, memo jne ja klõpsake "create Invoice".
- Selle Invoice maksmine toob Sats näidatud kanalisse.


Kui soovite maksta endale, et Invoice (ümmargune tasakaalustamine), kui te maksate seda samast Zeus-sõlmest, valige makseekraanil väljaminev kanal (see, millel on rohkem likviidsust), mida soovite kasutada makse saatmiseks.


### Maksa Keysendiga


Keysend on väga alahinnatud LN funktsioon ja kasutajad peaksid seda sagedamini kasutama.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) võimaldab Lightning Network kasutajatel saata makseid teistele , otse nende avalikule võtmele, kui nende sõlmes on avalikud kanalid ja keysend on lubatud. Keysend ei nõua, et makse saaja väljastaks Invoice.


Kuidas saab seda teha Zeusiga?


Lihtsalt skaneerige või kopeerige sihtkoha nodeID (või kasutage Zeuse kontakte, et salvestada oma tavalised sihtkoha sõlmed kontaktidena) ja seejärel klõpsake Zeuse põhiekraanil nupul "Saada". Seejärel kleepige nodeID või valige see oma kontaktidest.


Pange Sats summa, vajadusel sõnum (jah, seda saab kasutada ka salajase vestluse kaudu LN) ja vajutage nupule "Saada". Valmis!


![Image](assets/en/15.webp)


Kui teil on otsekanal sihtkoha partneriga, siis EI OLE tasusid.


Kui teil ei ole otsekanalit sihtkoha partneriga, siis maksab võtmeside makse tasud tavalise LN Invoice maksena, mis suunatakse regulaarse tee kaudu nagu iga teine makse. Ainult et, pidage meeles, et see ei jää mingit jälge kui LN Invoice.


## Conlusion


Soovitan lugeda lisajuhendit [Advanced use of Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html), kus on rohkem juhiseid ja kasutusjuhendeid.


Ja... see on kõik! Nüüdsest alates kasutate Zeus Node'i tavalise BTC/LN Wallet-ga oma mobiilis. Kasutajaliides on üsna sirgjooneline ja lihtne kasutada, intuitiivne igat tüüpi kasutajale, ma ei usu, et pean rohkem üksikasju sisestama, kuidas makseid teha ja vastu võtta.


Kokkuvõtteks on siin võrdlus privaatsustabel :


![Image](assets/en/16.webp)
