---
name: RoninDojo

description: Oma RoninDojo Bitcoin sõlme paigaldamine ja kasutamine.
---
***HOIATUS:** Pärast Samourai Walleti asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil ei ole RoninDojo teatud funktsioonid, nagu Whirlpool, enam töökorras. Siiski on võimalik, et neid tööriistu võidakse järgnevate nädalate jooksul taastada või uuesti käivitada erineval kujul. Kuna RoninDojo kood oli majutatud Samourai GitLabis, mis samuti konfiskeeriti, ei ole hetkel võimalik koodi kaugelt alla laadida. RoninDojo meeskonnad töötavad tõenäoliselt koodi uuesti avaldamise kallal.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite olla kindlad, et uuendame seda õpetust, kui uut teavet saadakse._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

_See õpetus on pühendatud RoninDojo v1 paigaldamisele. Viimaste täiustuste ja funktsioonide kasutamiseks soovitan tungivalt tutvuda meie õpetusega, mis on pühendatud RoninDojo v2 otsepaigaldusele teie Raspberry Pi-s:_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Omaenda sõlme käitamine ja kasutamine on hädavajalik, et tõeliselt osaleda Bitcoin võrgustikus. Kuigi Bitcoin sõlme käitamine ei too kasutajale rahalist kasu, võimaldab see neil säilitada oma privaatsust, tegutseda sõltumatult ja kontrollida oma usaldust võrgustiku vastu.

Sel artiklis vaatame üksikasjalikult RoninDojo't, suurepärast lahendust oma Bitcoin sõlme käitamiseks.

### Sisukord:

- Mis on RoninDojo?
- Millist riistvara valida?
- Kuidas paigaldada RoninDojo?
- Kuidas kasutada RoninDojo?
- Järeldus

Kui te ei ole tuttav sellega, kuidas Bitcoin sõlm töötab ja mis on selle roll, soovitan alustada selle artikli lugemisest: Bitcoin Sõlm - Osa 1/2: Tehnilised Kontseptsioonid.

![Samourai](assets/1.webp)

## Mis on RoninDojo?

Dojo on täielik Bitcoin sõlme server, mille on välja töötanud Samourai Walleti meeskond. Seda saab vabalt paigaldada igale masinale.

RoninDojo on paigaldusabi ja haldusvahend Dojo jaoks ning mitmete teiste tööriistade jaoks. RoninDojo võtab Dojo algse rakenduse ja lisab sellele palju muid tööriistu, muutes samal ajal paigaldamise ja haldamise lihtsamaks.

Nad pakuvad ka "plug-and-play" riistvara, RoninDojo Tanto, millele on RoninDojo eelinstalleeritud ja mille on kokku pannud nende meeskond. Tanto on tasuline lahendus, sobilik neile, kes ei soovi ise seadistamisega tegeleda.

RoninDojo kood on avatud lähtekoodiga, seega on võimalik see lahendus paigaldada ka oma riistvarale. See variant on kulutõhus, kuid nõuab veidi rohkem manipuleerimist, mida me selles artiklis teemegi.

RoninDojo on Dojo, seega võimaldab see hõlpsasti integreerida Whirlpool CLI oma Bitcoin sõlme, et saada parim võimalik CoinJoin kogemus. Whirlpool CLI abil saate mitte ainult lasta oma bitcoinidel 24/7 remixida ilma, et peaksite oma isiklikku arvutit sisselülitatuna hoidma, vaid saate ka oluliselt parandada oma privaatsust.
RoninDojo integreerib palju muid tööriistu, mis sõltuvad teie Dojost, nagu Boltzmanni kalkulaator, mis määrab tehingu privaatsuse taseme, Electrumi server, et ühendada teie erinevad Bitcoin'i rahakotid oma noodiga, või Mempooli server, et privaatselt jälgida oma tehinguid. Võrreldes teise noodilahendusega nagu Umbrel, mille teile selles artiklis tutvustasin, on RoninDojo sügavalt keskendunud "On Chain" lahendustele ja tööriistadele, mis optimeerivad kasutaja privaatsust. Seetõttu ei luba RoninDojo interaktsiooni Lightning Network'iga.

RoninDojo pakub vähem tööriistu võrreldes Umbreliga, kuid Roninis olevad mõned olulised funktsioonid Bitcoin'i kasutajale on uskumatult stabiilsed.

Niisiis, kui te ei vaja kõiki Umbreli serveri funktsioone ja soovite lihtsalt lihtsat ja stabiilset noodit mõne olulise tööriistaga nagu Whirlpool või Mempool, siis RoninDojo on tõenäoliselt hea lahendus teile.

Minu arvates on Umbreli arenduse fookus tugevalt Lightning Network'il ja mitmekülgsetel tööriistadel. See on endiselt Bitcoin'i nood, kuid eesmärk on muuta see mitmeülesandega mini-serveriks. Seevastu RoninDojo arenduse fookus on rohkem kooskõlas Samourai Wallet'i meeskondadega ja keskendub olulistele tööriistadele Bitcoin'i kasutajale, võimaldades täielikku sõltumatust ja privaatsuse optimeeritud haldamist Bitcoin'is.

Palun pange tähele, et RoninDojo nood'i seadistamine on veidi keerulisem kui Umbreli nood'i puhul.

Nüüd, kui oleme suutnud maalida pildi RoninDojost, vaatame, kuidas seda noodit koos seadistada.

## Millist riistvara valida?

RoninDojo majutamiseks ja käitamiseks masina valimiseks on teil mitu võimalust.

Nagu varem selgitatud, on lihtsaim valik tellida Tanto, spetsiaalselt selleks otstarbeks kavandatud plug-and-play masin. Oma tellimiseks minge siia: [link](https://shop.ronindojo.io/product-category/nodes/).

Kuna RoninDojo meeskonnad toodavad avatud lähtekoodiga koodi, on võimalik RoninDojo implementeerida ka teistele masinatele. Viimaste installatsiooniviisardi versioonide leiate sellelt lehelt: [link](https://ronindojo.io/en/downloads.html) ja koodi viimased versioonid sellelt lehelt: [link](https://code.samourai.io/ronindojo/RoninDojo).

Isiklikult paigaldasin selle Raspberry Pi 4 8GB peale ja kõik töötab suurepäraselt.

Siiski pange tähele, et RoninDojo meeskonnad näitavad, et korpuse ja SSD adapteriga on sageli probleeme. Seetõttu ei soovitata kasutada oma masina SSD jaoks kaabliga korpust. Selle asemel on eelistatav kasutada teie emaplaadile spetsiaalselt kavandatud mälulaienduskaarti, nagu see: Raspberry Pi 4 mälulaienduskaart.

Siin on näide, kuidas seadistada oma RoninDojo nood:

- Raspberry Pi 4.
- Korpus ventilaatoriga.
- Ühilduv mälulaienduskaart.
- Toitekaabel.
- Tööstuslik mikro SD kaart 16GB või rohkem.
- 1TB või suurem SSD.
- RJ45 Ethernet kaabel, soovitatav kategooria 8.

## Kuidas paigaldada RoninDojo?

### 1. samm: Valmistage ette käivitatav mikro SD kaart.

Kui olete oma masina kokku pannud, võite alustada RoninDojo paigaldamist. Selleks alustage sobiva kettapildi põletamist mikro SD kaardile.

Sisestage oma mikro SD kaart isiklikku arvutisse, seejärel minge ametlikule RoninDojo veebisaidile, et alla laadida RoninOS kettapilt: https://ronindojo.io/en/downloads.html.
Laadige alla kettapilt, mis vastab teie riistvarale. Minu puhul laadisin alla "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" pildi:
![Laadige alla RoninOS kettapilt](assets/2.webp)

Kui pilt on alla laaditud, kontrollige selle terviklikkust vastava .SHA256 faili abil. Kirjeldan üksikasjalikult, kuidas seda teha selles artiklis: Kuidas kontrollida Bitcoin tarkvara terviklikkust Windowsis?

Spetsiifilised juhised RoninOS-i terviklikkuse kontrollimiseks on samuti saadaval sellel lehel: https://wiki.ronindojo.io/en/extras/verify.

Selle pildi põletamiseks oma mikro SD kaardile võite kasutada tarkvara nagu Balena Etcher, mida saate alla laadida siit: https://www.balena.io/etcher/.

Selleks valige Etcheris pilt ja põletage see mikro SD kaardile:

![Põletage kettapilt Etcheriga](assets/3.webp)

Kui operatsioon on lõpetatud, saate sisestada käivitatava mikro SD kaardi Raspberry Pi-sse ja lülitada masina sisse.

### 2. samm: Seadistage RoninOS.

RoninOS on teie RoninDojo sõlme operatsioonisüsteem. See on modifitseeritud versioon Manjarost, mis on Linuxi distributsioon. Pärast masina käivitamist ja mõne minuti ootamist saate alustada selle seadistamist.

Selleks, et ühenduda sellega kaugelt, peate leidma oma RoninDojo masina IP-aadressi. Selleks võite näiteks ühenduda oma internetiboksi halduspaneeliga või alla laadida tarkvara nagu https://angryip.org/, et skannida oma kohalikku võrku ja leida masina IP.

Kui olete IP leidnud, saate võtta oma masina üle kontrolli teisest arvutist, mis on ühendatud samasse kohalikku võrku, kasutades SSH-d.

macOS-i või Linuxi jooksutavast arvutist avage lihtsalt terminal. Windowsi jooksutavast arvutist võite kasutada spetsialiseeritud tööriista nagu Putty või otse kasutada Windows PowerShell-i.

Kui terminal on avatud, tippige järgmine käsk:

> ssh root@192.168.?.?

Lihtsalt asendage kaks küsimärki eelnevalt leitud RoninDojo IP-ga.
Nipp: Shellis paremklõpsates saate elemendi kleepida.

Seejärel jõuate Manjaro juhtpaneelile. Valige õige klaviatuuri paigutus, kasutades nooli sihtmärgi muutmiseks rippmenüüs.

![Manjaro klaviatuuri seadistamine](assets/4.webp)

Valige kasutajanimi ja parool oma seansiks. Kasutage tugevat parooli ja tehke sellest turvaline varukoopia. Võite valikuliselt kasutada nõrka parooli installimise ajal ja hiljem seda hõlpsalt muuta, "kopeerides-kleepides" selle RoninUI-sse. See võimaldab teil kasutada väga tugevat parooli, ilma et peaksite selle Manjaro seadistamise ajal käsitsi tippima kulutama palju aega.

![Manjaro kasutajanime seadistamine](assets/5.webp)

Seejärel palutakse teil valida ka root parool. Root parooli jaoks sisestage otse tugev parool. Te ei saa seda muuta RoninUI-st. Samuti pidage meeles, et teete sellest root paroolist turvalise varukoopia.

Seejärel sisestage oma asukoht ja ajavöönd.

![Manjaro ajavööndi seadistamine](assets/6.webp)

![Manjaro asukoha seadistamine](assets/7.webp)

Seejärel valige hostinimi.

![Manjaro hostinime seadistamine](assets/8.webp)

Lõpuks kontrollige Manjaro konfiguratsiooni infot ja kinnitage.

![ManjaroOS konfiguratsiooni info kontrollimine](assets/9.webp)

### 3. samm: Laadige alla RoninDojo.
RoninOS-i esialgne seadistamine viiakse läbi. Kui see on lõpetatud, nagu ülaltoodud ekraanipildil näha, taaskäivitub masin. Oodake mõni hetk, seejärel sisestage järgmine käsk, et ühenduda uuesti oma RoninDojo masinaga:
> ssh kasutajanimi@192.168.?.?

Lihtsalt asendage "kasutajanimi" eelnevalt valitud kasutajanimega ja küsimärgid RoninDojo IP-aadressiga.

Seejärel sisestage oma kasutaja parool.

Terminalis näeb see välja selline:

![SSH ühendus RoninOS-iga](assets/10.webp)

Nüüd olete ühendatud oma masinaga, millel on praegu ainult RoninOS. Nüüd peate sellele installima RoninDojo.

Laadige alla RoninDojo uusim versioon, sisestades järgmise käsu:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Allalaadimine on kiire. Terminalis näete seda:

![RoninDojo kloonimine](assets/11.webp)

Oodake, kuni allalaadimine lõpeb, seejärel installige ja pääsege juurde RoninDojo kasutajaliidesele, kasutades järgmist käsku:

> ~/RoninDojo/ronin

Teilt palutakse sisestada oma kasutaja parool:

![Bitcoin Node parooli kinnitamine](assets/12.webp)

See käsk on vajalik ainult esimesel korral, kui pääsete oma RoninDojo juurde. Hiljem, et pääseda SSH kaudu RoninCLI-le, peate lihtsalt sisestama käsu [SSH kasutajanimi@192.168.?.?] asendades "kasutajanimi" oma kasutajanimega ja sisestades oma sõlme IP-aadressi. Teilt küsitakse teie kasutaja parooli.

Järgmisena näete seda suurepärast animatsiooni:

![RoninCLI käivitusanimatsioon](assets/13.webp)

Seejärel jõuate lõpuks RoninDojo CLI kasutajaliidesesse.

### 4. samm: Installige RoninDojo.

Peamenüüst liikuge nooleklahvide abil "System" menüüsse. Vajutage enter-klahvi, et oma valikut kinnitada.

![RoninCLI navigeerimismenüü süsteemi](assets/14.webp)

Seejärel minge "System Setup & Install" menüüsse.

![RoninCLI navigeerimismenüü RoninDojo süsteemi installimiseks](assets/15.webp)

Lõpuks märkige "System Setup" ja "Install RoninDojo" tühikuklahviga, seejärel valige "Accept", et alustada installimist.

![RoninDojo installimise kinnitus](assets/16.webp)

Laske installimisel rahulikult toimuda. Minu puhul võttis see umbes 2 tundi. Hoidke protsessi ajal oma terminal avatud.

Kontrollige aeg-ajalt oma terminali, kuna teilt palutakse teatud installietappidel vajutada klahvi, näiteks siin:

![RoninDojo installimine käib](assets/17.webp)

Installimise lõppedes näete erinevate konteinerite käivitumist:

![Sõlme konteineri käivitamine](assets/18.webp)

Seejärel taaskäivitub teie sõlm. Ühenduge uuesti RoninCLI-ga järgmise sammu jaoks.

![Bitcoin sõlme taaskäivitamine](assets/19.webp)

### 5. samm: Laadige alla proof-of-work ahel ja pääsege juurde RoninUI-le.

Kui installimine on lõpetatud, hakkab teie sõlm alla laadima Bitcoin proof-of-work ahelat. Seda nimetatakse algseks plokkide allalaadimiseks (IBD). Sõltuvalt teie internetiühendusest ja seadmest võib see tavaliselt võtta 2 kuni 14 päeva.

Ahela allalaadimise edenemist saate jälgida, pääsedes juurde RoninUI veebiliidesele.

Sellele juurdepääsemiseks kohalikust võrgust tippige oma brauseri aadressiribale:

- Kas sisestage otse oma masina IP-aadress (192.168.?.?)

- Või sisestage: ronindojo.local
Pea meeles, et kui kasutad VPN-i, tuleks see välja lülitada.
### Võimalik keerdkäik

Kui sa ei saa RoninUI-le oma brauserist ühenduda, kontrolli rakenduse nõuetekohast toimimist oma terminalist, mis on ühendatud sinu sõlmega SSH kaudu. Ühendu peamenüüga, järgides eelnevaid samme:

- Sisesta: SSH kasutajanimi@192.168.?.?, asendades selle oma andmetega.

- Sisesta oma kasutaja parool.

Põhimenüüs olles mine:

> RoninUI > Taaskäivita

Kui rakendus taaskäivitub korrektselt, on probleem sinu brauseri ühenduses. Kontrolli, et sa ei kasutaks VPN-i ja veendu, et oled ühendatud samasse võrku kui sinu sõlm.

Kui taaskäivitamine toob kaasa vea, proovi operatsioonisüsteemi uuendada ja seejärel RoninUI uuesti installida. Operatsioonisüsteemi uuendamiseks:

> Süsteem > Tarkvarauuendused > Uuenda operatsioonisüsteemi

Pärast uuendamist ja taaskäivitamist ühendu oma sõlmega uuesti SSH kaudu ja installi RoninUI uuesti:

> RoninUI > Paigalda uuesti

Pärast RoninUI uuesti allalaadimist proovi ühenduda RoninUI-ga läbi oma brauseri.

> Nipp: Kui sa kogemata väljud RoninCLI-st ja satud Manjaro terminali, sisesta lihtsalt käsk "ronin", et naasta otse RoninCLI peamenüüsse.

### Veebis sisselogimine

Samuti saad sisse logida RoninUI veebiliidesesse mis tahes võrgust kasutades Tor-i. Selleks taasta oma RoninUI Tor aadress RoninCLI-st:

> Volitused > Ronin UI

Taasta Tor aadress, mis lõpeb .onion'iga, ja seejärel logi sisse Ronin UI-sse, sisestades selle aadressi oma Tor brauserisse. Ole ettevaatlik, et mitte lekitada oma erinevaid volitusi, kuna need on tundlik teave.

![RoninUI veebisisselogimise liides](assets/20.webp)

Sisselogimisel palutakse sul sisestada oma kasutaja parool. See on sama parool, mida kasutad sisselogimiseks SSH kaudu.

![RoninUI veebiliidese halduspaneel](assets/21.webp)

Siin näeme IBD (Initial Block Download) edenemist. Ole kannatlik, sa taastad kõik Bitcoinis alates 3. jaanuarist 2009 tehtud tehingud.

Pärast kogu plokiahela allalaadimist tihendab indekseerija andmebaasi. See toiming võtab umbes 12 tundi. Saad jälgida selle edenemist ka "Indekseerija" all RoninUI-s.

Sinu RoninDojo sõlm on pärast seda täielikult funktsionaalne:

![Indekseerija sünkroniseeritud 100% funktsionaalse sõlmega](assets/22.webp)

Kui soovid kasutaja parooli tugevamaks muuta, saad seda nüüd teha "Seaded" vahekaardilt. RoninDojol ei ole lisaturvakihti, seega soovitan valida tõeliselt tugeva parooli ja hoolitseda selle varundamise eest.

## Kuidas kasutada RoninDojo?

Kui ahel on allalaaditud ja tihendatud, saad hakata nautima oma uue RoninDojo sõlme pakutavaid teenuseid. Vaatame, kuidas neid kasutada.

### Ühendades rahakott tarkvara electrs-iga.

Sinu uue paigaldatud ja sünkroniseeritud sõlme esimene kasutusvõimalus on edastada sinu tehingud Bitcoin võrku. Seetõttu soovid tõenäoliselt ühendada oma erineva rahakottide haldustarkvara sellega.

Seda saab teha kasutades Electrum Rust Serverit (electrs). Rakendus on tavaliselt sinu RoninDojo sõlmele eelinstalleeritud. Kui mitte, saad selle käsitsi paigaldada RoninCLI liidesest.

Lihtsalt mine:

> Rakendused > Halda Rakendusi > Paigalda Electrum Server

Electrum Serveri Tor aadressi saamiseks, RoninCLI menüüst mine:

> Volitused > Electrs
Te peate lihtsalt sisestama .onion lingi oma rahakvara tarkvarasse. Näiteks Sparrow Wallet'is minge vahekaardile:
> File > Preferences > Server

Serveri tüübis valige "Private Electrum", seejärel sisestage oma Electrum Serveri Tor aadress vastavasse välja. Lõpuks klõpsake nupul "Test Connection", et testida ja salvestada oma ühendus.

![Sparrow Walleti ühendusliides electrs'iga](assets/23.webp)

### Rahakvara ühendamine Samourai Dojoga.

Electrs'i asemel võite kasutada ka Samourai Dojot, et ühendada oma ühilduv tarkvararahakott RoninDojo sõlmega. Näiteks Samourai Wallet pakub seda võimalust.

Selleks skannige lihtsalt oma Dojo ühenduse QR-koodi. Sellele juurdepääsemiseks RoninUI-st klõpsake vahekaardil "Dashboard" ja seejärel oma Dojo kastis nupul "Manage". Seejärel näete oma Dojo ja BTC-RPC Exploreri ühenduse QR-koode. Nende kuvamiseks klõpsake nupul "Display values".

![Dojoga ühenduse QR-koodi hankimine](assets/24.webp)

Oma Samourai Walleti ühendamiseks Dojoga peate selle QR-koodi skannima rakenduse installimise ajal:

![Ühendamine Dojoga Samourai Walleti rakendusest](assets/25.webp)

### Oma Mempool Exploreri kasutamine.

Oluline tööriist Bitcoin'i kasutajatele, explorer võimaldab kontrollida erinevat teavet Bitcoin'i ahela kohta. Mempooli abil saate näiteks reaalajas kontrollida teiste kasutajate rakendatud tasusid, et vastavalt oma tasusid kohandada. Samuti saate kontrollida oma tehingu kinnitamise olekut või vaadata aadressi jääki.

Need exploreri tööriistad võivad teid privaatsusriskidele avada ja nõuavad, et usaldate kolmanda osapoole andmebaasi. Kui kasutate seda veebitööriista ilma oma sõlme kaudu minemata:

- Te riskite oma rahakoti teabe lekkimisega.

- Te usaldate veebisaidi haldajat nende hostitud proof-of-work ahela eest.

Nende riskide vältimiseks võite kasutada oma Mempooli instantsi oma sõlmes Tor võrgu kaudu. Selle lahendusega mitte ainult ei säilita te oma privaatsust teenuse kasutamisel, vaid te ei pea ka enam teenusepakkujat usaldama, kuna päringute tegemisel kasutate oma andmebaasi.

Selleks alustage Mempool Space Visualizeri installimisega RoninCLI kaudu:

> Applications > Manage Applications > Install Mempool Space Visualizer

Pärast installimist hankige oma Mempooli link. Tor aadress võimaldab teil sellele juurde pääseda mis tahes võrgust. Samamoodi saame selle lingi RoninCLI kaudu:

> Credentials > Mempool

![Hankige Tor Mempooli aadress](assets/26.webp)

Lihtsalt sisestage oma Mempooli Tor aadress Tor brauserisse, et nautida oma Mempooli instantsi, mis põhineb teie enda andmetel. Soovitan lisada selle Tor aadressi oma lemmikutesse kiiremaks juurdepääsuks. Samuti võite luua otsetee oma töölaual.

![Mempool Space'i liides](assets/27.webp)

Kui teil ei ole veel Tor brauserit, saate selle alla laadida siit: https://www.torproject.org/download/

Samuti võite sellele juurde pääseda oma nutitelefonist, installides Tor Browseri ja sisestades sama aadressi. Kõikjalt saate oma sõlme kasutades vaadata Bitcoin'i ahela olekut.

### Whirlpool CLI kasutamine.

Teie RoninDojo sõlm sisaldab ka WhirlpoolCLI-d, kaugkäsurea liidest Whirlpooli segude automatiseerimiseks.
Kui teostate CoinJoini Whirlpooli rakendusega, peab teie kasutatav rakendus jääma avatuks, et teostada segamisi ja uuesti segamisi. See protsess võib olla tüütu kasutajatele, kes soovivad saavutada kõrget anonüümsuse taset, kuna seade, millel Whirlpooli rakendus töötab, peab pidevalt sisse lülitatud olema. Praktiliselt tähendab see, et kui soovite oma UTXOsid kaasata ööpäevaringsetesse uuesti segamistesse, peate hoidma oma isiklikku arvutit või telefoni pidevalt sisse lülitatuna koos avatud rakendusega.
Üks lahendus sellele piirangule on kasutada WhirlpoolCLI-d masinal, mis on mõeldud pidevalt töötama, nagu näiteks Bitcoin'i sõlm. Sellega saavad meie UTXOsid segada 24/7 ilma, et peaksime hoidma teist masinat peale meie Bitcoin'i sõlme töös.
WhirlpoolCLI-d kasutatakse koos WhirlpoolGUI-ga, graafilise liidesega, mis on mõeldud paigaldamiseks isiklikule arvutile Coinjoinide lihtsaks haldamiseks. Selles artiklis selgitan üksikasjalikult, kuidas seadistada Whirlpool CLI oma dojo'ga: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

Coinjoin'i kohta üldiselt rohkem teada saamiseks selgitan kõike selles artiklis: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Whirlpool Stat Tooli kasutamine.

Pärast CoinJoinide teostamist Whirlpooliga võite soovida teada oma segatud UTXOde tegelikku privaatsuse taset. Whirlpool Stat Tool võimaldab seda hõlpsalt teha. Selle tööriistaga saate arvutada oma segatud UTXOde potentsiaalse ja tagasiulatuva skoori. Anon Sets'i arvutamise ja nende toimimise kohta rohkem teada saamiseks soovitan lugeda seda jaotist: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Tööriist on eelinstalleeritud teie RoninDojo's. Praegu on see saadaval ainult RoninCLI kaudu. Selle käivitamiseks põhimenüüst minge:

> Samourai Toolkit > Whirlpool Stat Tool

Ilmuvad kasutusjuhised. Lõpetamisel vajutage mis tahes klahvi, et pääseda käsuridadele:

![Whirlpool Stats Tool tarkvara avaleht](assets/28.webp)

Terminal kuvatakse:

> wst#/tmp>

Sellest liidesest väljumiseks ja RoninCLI menüüsse naasmiseks sisestage lihtsalt käsk:

> quit

Alustuseks seadistame proxy Tor'is, et ekstraheerida OXT andmeid täieliku privaatsusega. Sisestage käsk:

> socks5 127.0.0.1:9050

Seejärel laadige alla andmed basseinist, mis sisaldab teie tehingut:

> download 0001
>
> Asendage 0001 basseini denominatsioonikoodiga, mis teid huvitab.

Denominatsioonikoodid on WST-s järgmised:

- Bassein 0.5 bitcoini: 05

- Bassein 0.05 bitcoini: 005

- Bassein 0.01 bitcoini: 001

- Bassein 0.001 bitcoini: 0001
![Andmete allalaadimine basseinist 0001 OXT-st](assets/29.webp)
Kui andmed on allalaaditud, laadige need käsu abil:

> load 0001
>
> Asendage 0001 teid huvitava basseini denominatsiooni koodiga.

![Andmete laadimine basseinist 0001](assets/30.webp)
Laske laadimisprotsessil toimuda, see võib võtta mõned minutid. Pärast andmete laadimist tippige skoori käsk koos oma TXID-ga (tehingu identifikaator), et saada selle Anon Sets:

> score TXID
>
> Asendage TXID oma tehingu identifikaatoriga.

![Antud TXID-i potentsiaalsete ja tagasivaatavate skooride printimine](assets/31.webp)

WST kuvab seejärel tagasivaatava skoori (tagasivaatavad meetrikad) järgnevalt potentsiaalse skoori (edasivaatavad meetrikad). Lisaks Anon Sets'i skooridele annab WST teile ka teie väljundi difusioonimäära basseinis, lähtudes anon setist.

Palun pange tähele, et teie UTXO potentsiaalne skoor arvutatakse lähtudes teie esialgse segamise TXID-st, mitte teie viimasest segamisest. Vastupidi, UTXO tagasivaatav skoor arvutatakse lähtudes viimase tsükli TXID-st.

Kui te ei mõista neid Anon Sets'i kontseptsioone, soovitan lugeda seda osa minu artiklist Coinjoin'i kohta, kus ma selgitan kõike üksikasjalikult diagrammidega: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Boltzmanni kalkulaatori kasutamine.

Boltzmanni kalkulaator on tööriist, mis võimaldab teil hõlpsalt arvutada erinevaid edasijõudnud meetrikaid Bitcoin'i tehingu kohta, sealhulgas selle entroopia taset. Kõik need andmed võimaldavad teil kvantifitseerida tehingu privaatsuse taset ja tuvastada võimalikke vigu. See tööriist on eelinstallitud teie RoninDojo sõlmele.

Sellele juurdepääsemiseks RoninCLI kaudu, ühenduge SSH kaudu, seejärel minge menüüsse:

> Samourai Toolkit > Boltzmanni kalkulaator

Enne selle kasutamise selgitamist RoninDojo's, selgitan, mida need meetrikad esindavad, kuidas neid arvutatakse ja milleks neid kasutatakse.

Neid näitajaid saab kasutada mis tahes Bitcoin'i tehingu jaoks, kuid need on eriti huvitavad Coinjoin tehingu kvaliteedi uurimiseks.

1. Esimene näitaja, mille see tarkvara arvutab, on võimalike kombinatsioonide arv. Kalkulaatoris on see märgitud kui "nb combinations". Arvestades UTXO-de väärtusi, esindab see näitaja võimalike kaardistuste arvu sisenditest väljunditesse.

> Kui te pole terminiga "UTXO" tuttav, soovitan lugeda seda lühikest artiklit: Bitcoin'i tehingu mehhanism: UTXO, sisendid ja väljundid.

Teisisõnu, see näitaja esindab võimalike tõlgenduste arvu antud tehingu jaoks. Näiteks Whirlpool 5x5 Coinjoin struktuuril on võimalike kombinatsioonide arv võrdne 1496:

![Coinjoin tehingu skeem kycp.org-is](assets/32.webp)

Krediit: KYCP
2. Teine arvutatav näitaja on tehingu entroopia. Kuna tehingu võimalike kombinatsioonide arv võib olla väga suur, võib selle asemel kasutada entroopiat. Entroopia esindab võimalike kombinatsioonide arvu binaarlogaritmi. Selle valem on järgmine:
- E: tehingu entroopia.
- C: tehingu võimalike kombinatsioonide arv.

> E = log2(C)

Matemaatikas on binaarlogaritm (alus 2) 2. astme funktsiooni pöördtehe. Teisisõnu, x binaarlogaritm on astendaja, millega arvu 2 tuleb astendada, et saada väärtus x.

Seega:

> E = log2(C)
> C = 2^E

See näitaja väljendatakse bittides. Näiteks siin on Whirlpool 5x5 Coinjoin tehingu entroopia arvutus, eelnevalt mainitud võimalike kombinatsioonide arvuga võrdne 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bitti

Seega on sellel Coinjoin tehingul entroopia 10.5469 bitti, mis on väga hea.

Mida kõrgem see näitaja on, seda rohkem erinevaid tõlgendusi tehingust on ja seega on tehing konfidentsiaalsem.

Võtame veel ühe näite. Siin on "klassikaline" tehing, millel on üks sisend ja kaks väljundit:

![Bitcoin tehingu skeem oxt.me peal](assets/34.webp)

Autor: OXT

Sellel tehingul on ainult üks võimalik tõlgendus:

> [(inp 0) > (Outp 0 ; Outp 1)]

Seega on selle entroopia võrdne 0-ga:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Kolmas näitaja, mille Boltzmanni kalkulaator tagastab, on Tx-i nimetatud "Rahakoti Efektiivsus". See näitaja lihtsalt võimaldab võrrelda sisendtehingut parima võimaliku tehinguga samas konfiguratsioonis.

Tutvustame nüüd maksimaalse entroopia mõistet, mis esindab antud tehingustruktuuri saavutatavat kõrgeimat entroopiat. Näiteks Whirlpool 5x5 Coinjoin struktuuril oleks maksimaalne entroopia 10.5469. Efektiivsuse näitaja võrdleb seda maksimaalset entroopiat sisendtehingu tegeliku entroopiaga. Selle valem on järgmine:

- ER: Tegelik entroopia väljendatuna bittides.
- EM: Maksimaalne entroopia sama struktuuriga väljendatuna bittides.
- Ef: Efektiivsus väljendatuna bittides.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bitti

See näitaja väljendatakse ka protsendina, nii et valem muutub:

- CR: Tegelik võimalike kombinatsioonide arv.
- CM: Maksimaalne võimalike kombinatsioonide arv sama struktuuriga.
- Ef: Efektiivsus väljendatuna protsendina.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

Efektiivsus 100% tähendab, et sellel tehingul on oma struktuuri suhtes kõrgeim võimalik privaatsus.

4. Neljas arvutatav näitaja on entroopia tihedus. See võimaldab meil seostada entroopiat iga sisendi või väljundi kohta. Seda näitajat saab kasutada erineva suurusega tehingute efektiivsuse võrdlemiseks.

Selle arvutamine on väga lihtne: jagame tehingu entroopia sisendite ja väljundite koguarvuga. Näiteks Whirlpool 5x5 Coinjoin puhul oleks meil:

    ED: Entroopia tihedus väljendatuna bittides.
    E: Tehingu entroopia väljendatuna bittides.
    T: Tehingu sisendite ja väljundite koguarv.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 biti

Boltzmanni kalkulaatori poolt antud viies teave on sisendite ja väljundite vaheliste linkide tõenäosustabel. See tabel annab lihtsalt tõenäosuse (Boltzmanni skoori), et antud sisend vastab kindlale väljundile.

Kui võtame meie näite Whirlpool Coinjoin'iga, näeks tõenäosustabel välja selline:

| %       | Väljund 0 | Väljund 1 | Väljund 2 | Väljund 3 | Väljund 4 |
|---------|-----------|-----------|-----------|-----------|-----------|
| Sisend 0| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 1| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 2| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 3| 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 4| 34%       | 34%       | 34%       | 34%       | 34%       |

Siit näeme, et igal sisendil on võrdne tõenäosus olla seotud iga väljundiga.

Kuid, kui võtame näiteks tehingu, millel on üks sisend ja kaks väljundit, näeks see välja selline:

| Sisend | Väljund 0 | Väljund 1 |
| ------ | --------- | --------- |
| 0      | 100%      | 100%      |

Selles näites näeme, et tõenäosus, et iga väljund pärineb sisendist 0, on 100%.

Mida madalam see tõenäosus, seda kõrgem on konfidentsiaalsuse tase.

6. Arvutatav kuues teave on deterministlike linkide arv. Samuti antakse deterministlike linkide suhe. See näitaja toob esile antud tehingu sisendite ja väljundite vaheliste linkide arvu, mille tõenäosus on 100%, mis tähendab, et need on vaieldamatud.

Suhe näitab deterministlike linkide arvu tehingus võrreldes linkide koguarvuga.

Näiteks Coinjoin Whirlpool tehingul ei ole sisendite ja väljundite vahel deterministlikke linke. Näitaja on null ja suhe samuti 0%.

Kuid teise uuritud tehingu puhul (1 sisend ja 2 väljundit) on näitaja 2 ja suhe 100%.

Seega, kui see näitaja on null, näitab see head konfidentsiaalsust.

Nüüd, kui oleme näitajad läbi vaadanud, vaatame, kuidas neid selle tarkvara abil arvutada. RoninCLI's, mine menüüsse:

> Samourai Toolkit > Boltzmanni Kalkulaator

![Boltzmanni Kalkulaatori tarkvara avaleht](assets/35.webp)

Kui tarkvara on käivitatud, sisesta uuritava tehingu ID. Sa võid sisestada korraga mitu tehingut, eraldades need komaga, seejärel vajuta sisestusklahvi:

![Sisesta TXID uurimiseks Boltzmanni Kalkulaatorisse](assets/36.webp)

Kalkulaator seejärel tagastab kõik eelnevalt nähtud näitajad:

![Boltzmanni Kalkulaatori andmete printimine selle TXID jaoks](assets/37.webp)

Tarkvarast väljumiseks ja RoninCLI menüüsse naasmiseks tippige käsk "Quit".

Boltzmanni kalkulaatori kohta lisateabe saamiseks soovitan lugeda neid artikleid:

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Bisqi ühendamine.
Bisq on peer-to-peer vahetusplatvorm, mis võimaldab teil osta ja müüa bitcoine. Seda kasutatakse koos lauaarvutitarkvaraga, mis töötab Toril ja võimaldab teil vahetada bitcoine ilma, et peaksite oma isikut tuvastama.
Bisq tagab peer-to-peer vahetused läbi 2/2 mitme allkirja süsteemi. Saate seda tarkvara kasutada koos omaenda RoninDojo noodiga, et optimeerida oma vahetuste privaatsust ja usaldada oma noodist pärinevat blockchaini andmeid.

Bisqi tarkvara allalaadimiseks minge nende ametlikule veebilehele: https://bisq.network/

Tarkvaraga alustamiseks soovitan lugeda seda lehte: https://bisq.network/getting-started/

RoninDojo ühenduslingi saamiseks peate ühenduma RoninCLI-ga SSH kaudu. Seejärel minge menüüsse:

> Rakendused > Halda Rakendusi

Sisestage oma parool, seejärel märkige ruut tühikuklahviga:

> [ ] Luba Bisqi Ühendus

Kinnitage oma valik. Laske oma noodil installida, seejärel hankige Tor V3 aadress järgmiselt:

> Tunnistused > Bitcoind

Kopeerige aadress alajaotusest "Bitcoin Daemon".

Samuti saate oma Bitcoind Tor V3 aadressi hankida RoninUI liidesest, lihtsalt klõpsates "Halda" "Bitcoin Core" kastis "Töölaual":

![Hankige TorV3 Bitcoin Daemon aadress RoninUI-st](assets/38.webp)

Noodiga Bisqist ühenduse loomiseks minge menüüsse:

> Seaded > Võrgu Info

![Juurdepääs noodiga ühenduse liidesele Bisqi tarkvaras](assets/39.webp)

Klõpsake mullil "Kasuta kohandatud Bitcoin Core noode". Seejärel sisestage oma Bitcoin TorV3 aadress ettenähtud kasti, koos ".onion" lõpuga, kuid ilma "http://".

![Kast, kuhu sisestada oma noodiga TorV3 aadress Bisqi tarkvaras](assets/40.webp)

Taaskäivitage Bisqi tarkvara. Teie nood on nüüd ühendatud teie Bisqiga.

### Muud funktsioonid.

Teie RoninDojo nood sisaldab ka muid põhifunktsioone. Teil on võimalus skannida teatud teavet, et tagada selle arvessevõtmine.

Näiteks on mõnikord võimalik, et teie RoninDojo-ga ühendatud rahakott ei leia teile kuuluvaid bitcoine. Saldo on 0, kuigi olete kindel, et selles rahakotis on teil bitcoine. Kaaluda tuleb paljusid võimalikke põhjuseid, sealhulgas tuletusteede viga, ja nende seas on võimalik, et teie nood ei jälgi teie aadresse.

Selle parandamiseks saate kontrollida, kas teie nood jälgib teie xpubi "xpub tööriista" abil. Sellele juurdepääsemiseks RoninUI-s minge menüüsse:

> Hooldus > XPUB Tööriist

Sisestage probleemne xpub ja klõpsake "Kontrolli", et seda teavet kontrollida.

![XPUB Tööriist RoninUI-st](assets/41.webp)

Kui teie xpubi jälgib nood, näete seda ilmumas:

![XPUB Tööriista tulemus, mis näitab edukat analüüsi](assets/42.webp)

Kontrollige, et kõik tehingud kuvataks korrektselt. Samuti kontrollige, kas tuletustüüp vastab teie rahakoti omale. Siin näeme, et nood tõlgendab seda xpubi kui BIP44 tuletust. Kui see tuletustüüp ei vasta teie rahakoti omale, klõpsake nupul "Sisesta uuesti", seejärel valige BIP44/BIP49/BIP84 vastavalt teie valikule:

![Muuda uuritud xpubi tuletustüüpi RoninUI-st](assets/43.webp)

Kui teie xpubi ei jälgita teie noodis, näete seda ekraani, mis kutsub teid seda importima:
![Importige xpub XPUB tööriistaga RoninUI-s](assets/44.webp)
Samuti võite kasutada muid hooldustööriistu:

- Tehingu Tööriist: Võimaldab vaadelda konkreetse tehingu detaile.
- Aadressi Tööriist: Võimaldab kontrollida, kas konkreetne aadress on teie Dojo poolt jälgitud.
- Plokkide Uuesti Skaneerimine: Sunnib teie sõlme valitud vahemikus plokke uuesti skaneerima.

Samuti leiate RoninUI-st "Push Tx" tööriista. See võimaldab teil edastada allkirjastatud tehingu Bitcoin võrku. See tuleb sisestada heksadetsimaalformaadis:

![Tööriist allkirjastatud tehingu edastamiseks RoninUI-st](assets/45.webp)

## Järeldus.

Oleme näinud, kuidas paigaldada ja alustada tööd selle suurepärase tööriistaga, mis on RoninDojo. See on suurepärane valik oma Bitcoin sõlme käitamiseks. See on stabiilne lahendus, mis integreerib ja hoiab ajakohasena kõik olulised tööriistad Bitcoin kasutajale.

Kui terminali kasutamine ei hirmuta teid ja kui te ei vaja Lightning Network'iga seotud tööriistu, siis võib RoninDojo teile meeldida.

Kui võimalik, kaaluge arendajatele annetamist, kes vabavarana neid tarkvarasid teile toodavad: https://donate.ronindojo.io/

RoninDojo kohta lisateabe saamiseks soovitan tutvuda allpool toodud väliste ressurssidega.

### Edasine lugemine:

- CoinJoin'i mõistmine ja kasutamine Bitcoinis.
- Hash funktsioonid - katkend e-raamatust Bitcoin Démocratisé 1.
- Kõik, mida peate teadma Bitcoin Passphrase'ist.

### Välised ressursid:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/boltzmanni-tutvustus-85930984a159
- https://en.wikipedia.org/wiki/Boltzmanni_valem
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
