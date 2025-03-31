---
name: Nakamochi
description: Node Running Made Easy - Kuidas luua ja kasutada Nakamochi Bitcoini ja Lightning sõlme.
---
Oma Bitcoini ja Lightning'i täisnoodide käivitamine ei pea enam olema keeruline ülesanne, mis piirdub vaid tehniliste ekspertidega. Traditsiooniliselt on sõlmede loomine ja haldamine nõudnud põhjalikke teadmisi krüptograafiast, võrgutamisest ja tarkvaraarendusest. Nakamochi muudab seda, tehes sõlmed kättesaadavaks kõigile, sõltumata tehnilisest taustast.

Nakamochi abil saab igaüks luua ja hallata sõlme kodust, võimaldades täielikku privaatsust ja rahalist sõltumatust. Täieliku sõlme käitamine ei taga mitte ainult teie enda tehingute turvalisust, vaid aitab ka kaasa Bitcoini võrgu tugevusele. Detsentraliseeritud ja paindlik Bitcoini võrk tugineb oma turvalisuse ja sõltumatuse tagamiseks sõlmede laiale jaotusele.

### Sisukord


- Mis on Nakamochi ja kuidas see toimib?
- Nakamochi seadistamine
- Lightning Networki kohta
- Kanalite avamine ja tehingute tegemine Lightning-võrgus

## Mis on Nakamochi ja kuidas see toimib?

Nakamochi on ainult Bitcoini täisnood, mis toetab nii Bitcoini kui ka Lightningi võrke. See sisaldab integreeritud Bitcoini ja Lightningi rahakotti, mis võimaldab kasutajatel kasutada turvalist, isesuveräänset Bitcoini sõlme, kasutades samal ajal Lightning-võrgu kiirust ja madalaid tehingukulusid.

Teie Nakamochi-sõlme hallatakse mobiilirakenduse [BitBanana (Android)](https://bitbanana.app) ja [Zeus (iOS)](https://bitbanana.app) kaudu, mis võimaldab teil seda mugavalt juhtida kõikjalt. Need rakendused toimivad teie sõlme kaugjuhtimispunktina, võimaldades teil hõlpsasti maksta otse Bitcoini või Lightningiga, hallata tehinguid, avada või sulgeda kanaleid, kontrollida saldosid ja jälgida oma sõlme jõudlust.

## Nakamochi seadistamine võtab vaid 5 minutit

### 1. samm: ühendage ja alustage

1. Ühendage Nakamochi voolu ja Wi-Fi-ühendusega.

2. Klõpsake **"Uue rahakoti loomine "** ja salvestage turvaliselt oma 24-sõnaline taastamislause.

3. Kasutage oma Nakamochiga ühendamiseks sõlme haldamise rakendust (Zeus või BitBanana):

4. Avage rakendus ja skaneerige Nakamochi ekraanil kuvatavat QR-koodi.

5. Lisaturvalisuse tagamiseks määrake oma seadmesse PIN-kood.

![image](assets/en/01.webp)

_Connect to power and write down your 24-word seed phrase_

![image](assets/en/02.webp)

_Oota, kuni Blockchain on järele jõudnud_

![image](assets/en/03.webp)

_Uue rahakoti loomine välklambilehel_

![image](assets/en/04.webp)

_Skaneeri QR-kood koos Node Management Appiga_

![image](asset/en/05.webp)

_Seadke lisaturvalisuse tagamiseks PIN-kood_

**Märkus:** _Luba oma Nakamochi sõlme sünkroniseerida plokiahelaga. See protsess võib võtta aega, sõltuvalt teie internetiühendusest._

## Lightning Networki kohta

Bitcoini välkuvõrk muudab Bitcoini tehingud revolutsiooniliselt kiiremaks, odavamaks ja tõhusamaks. See sobib ideaalselt igapäevaseks kasutamiseks, võimaldades peaaegu koheseid makseid minimaalsete tasudega, mis on ideaalne mikrotehingute jaoks, näiteks kohvi ostmiseks või sagedaste väikeostude tegemiseks.

Kuna Lightning töötab väljaspool ahelat, on see loodud nii, et see toetab tuhandeid tehinguid sekundis, ilma et see koormaks Bitcoini peamist plokiahelat üle. See teeb sellest võtmetähtsusega mängija Bitcoini arengus praktiliseks, ülemaailmseks maksesüsteemiks.

Veel üks eelis on privaatsus, kuna Lightningi tehingud suunatakse läbi privaatsete maksekanalite, mitte ei salvestata otse plokiahelasse. See tagab diskreetsema viisi tehingute tegemiseks, säilitades samal ajal Bitcoini tugeva turvalisuse.

#### Maksekanalite selgitused

Lightning Network toimib maksekanalite kaudu, mis on kahe osapoole vahelised ühendused, mis võimaldavad mitut tehingut ilma otse plokiahelaga suhtlemata. Kui kanal on avatud, uuendatakse kahe osapoole vahelist saldot selles teise tasandi Lightning-lahenduses iga tehingu puhul, tagades kiire ja odava makse. Ainult kanali avamine ja sulgemine registreeritakse ahelas, vähendades Bitcoini plokiahelas tekkivaid ummikuid. selline disain tagab skaleeritavuse ja privaatsuse, kuna üksikud tehingud jäävad avalikus pearaamatus registreerimata.

**Näide:** Alice ja Bob avavad kanali, pannes sellele Bitcoini. Alice saadab Bitcoine Bobile ja nende ahelavälised saldod ajakohastuvad koheselt ilma ahelasiseselt registreerimata. Kui Alice maksab seejärel Charlie'le ja Alice'il ei ole otsekanalit Charlie'le, saab makse suunata läbi Bobi kanali Charlie'le. Vahendussõlmede kaudu suunamine tagab maksed ka ilma otsese ühenduseta, mis muudab võrgu väga tõhusaks.

## Kanalite avamine ja tehingute tegemine Lightning-võrgus

Kui teie Nakamochi on seadistatud ja ühendatud sõlme haldamise rakendusega, saate alustada Lightning Networki kasutamist, avades kanaleid ja tehes tehinguid.

### Kanalite avamine Zeuses (iOS):

1. Mine vahekaardile **"Kanalid "** (alumine menüü).

2. Uue kanali avamiseks klõpsake **"+"**.

3. Skaneerige või sisestage selle sõlme pubkey, millega soovite ühendust luua.

4. Sisestage lukustatud summa (valige koos oma kolleegiga või kasutage minimaalset fikseeritud summat tuntud sõlmede puhul).

5. Klõpsake **"Ava kanal "**.

![image](asset/en/06.webp)

_ZEUS Screenshot_

Lisateave: [Channels | Zeus Documentation](https://docs.zeusln.app/)

### Kanalite avamine BitBanana (Android):

1. Avage hamburgerimenüü (vasakul).

2. Mine **"Kanalid "**.

3. Uue kanali lisamiseks/avamiseks klõpsake **"+"**.

4. Skaneeri või kleebi pubkey sisse.

5. Sisestage lukustatud summa (valige koos oma kolleegiga või kasutage minimaalset fikseeritud summat tuntud sõlmede puhul).

![image](asset/en/07.webp)

_Bitbanana Screenshot_

Lisateave: [BitBanana](https://bitbanana.com)

Kui teie kanal on avatud, saab selle kaudu suunata makseid teistele võrgus osalejatele. Saldod kohanduvad väljaspool ahelat, mis tagab, et tehingud on peaaegu kohesed ja nende eest tuleb maksta minimaalselt.

Kui te ei vaja kanalit enam, võite selle sulgeda. See toiming arveldab teie ja teie partneri vahelise lõppsaldo ja registreerib selle ahelas. Ideaaljuhul on mõlemad pooled nõus ja on võrgus, et sulgeda kanal koostöös (kiiremini ja vähem tasusid kui sunniviisiline sulgemine vastamata/väljasoleva partneri puhul).

Üldiselt soovitame jätta kanalid avatuks, et vähendada kulusid ning suurendada võrgu töökindlust ja tõhusust. Kanalite avatuna hoidmisega vähendate miinimumini tehingutasusid, väldite kanalite taasühendamiseks vajalikke seisakuid ja säilitate stabiilse marsruutimisvõimsuse sujuvaks maksetöötluseks. Selline lähenemisviis soodustab töökindlat ja vastupidavat võrku, parandades samal ajal üldist kasutajakogemust ja vähendades tegevuskulusid.

### Kasulikud lingid


- [Nakamochist](https://nakamochi.io/)
- [Tellige Nakamochi uudiskiri](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)