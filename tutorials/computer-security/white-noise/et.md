---
name: White Noise
description: Nostr ja MLS protokollidel põhinev privaatne, detsentraliseeritud sõnumirakendus
---

![cover](assets/cover.webp)




## Sissejuhatus



"Raskuste keskel peitub võimalus". See Albert Einsteini tsitaat tuletab meile meelde, et probleemid ei ole lõplikud, vaid sisaldavad endas uute, innovaatiliste lahenduste seemneid.



Selles õpetuses esitletava lahenduse käivitamise motivatsioon illustreerib seda suurepäraselt. See on **White Noise**, mis on sündinud vajadusest.



Selle asutaja Max Hillebrandi sõnadega, millest on teatanud *Bitcoin Magazine*: "Me käivitasime selle projekti alternatiivide puudumise tõttu." Ta selgitab, et "olemasolevad krüpteerimisrakendused on suures mahus ebatõhusad: 100 inimese lisamine grupivestlusele aeglustab krüpteerimist märkimisväärselt. Detsentraliseeritud platvormid aga ei paku privaatset sõnumite edastamist. Lõpuks võimaldab Nostr avatud releevõrk kõigil ideid levitada, kuid otsesõnumite kaitse jääb dramaatiliselt ebapiisavaks. Me mõistsime: vabaduse kaitsmiseks pidime need süsteemid ühendama."



## Mis on White Noise?



White Noise on avatud lähtekoodiga sõnumirakendus, mille on välja töötanud mittetulundusühing. Rakendus edendab turvalisust, privaatsust ja detsentraliseerimist. Erinevalt tavapärastest rakendustest ei nõua see telefoninumbrit ega e-posti aadressi.


White Noise eristub kahe põhiprotokolli - Nostr ja MLS - integreerimise poolest, mis moodustavad selle tehnilise aluse.



Nostr (Notes and Other Stuff Transmitted by Relays) on detsentraliseeritud, avatud lähtekoodiga protokoll, mis on loodud tsensuurile vastu seisma.  Protokollis kasutatakse releesid, võtmepaare ja kliente.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Valge müra abil saate isegi valida oma relee seaded, et maksimeerida privaatsust.



MLS (Messaging Layer Security) on seevastu turvaprotokoll, mis võimaldab sõnumite läbivat krüpteerimist. Teisisõnu, sõnumid on kättesaadavad ainult lõpp-punktides, st sõnumi saatja ja vastuvõtja. See tähendab, et sõnumite marsruutimises osalevad releed ei pääse ligi nende sisule.



Siin on kiire võrdlus White Noise ja mitmete tuntuimate sõnumivahetuse rakenduste vahel.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## White Noise kasutamise alustamine



### White Noise paigaldus



Mine [White Noise veebilehele](https://www.whitenoise.chat/), seejärel klõpsa **Download**.



![screen](assets/fr/03.webp)



White Noise on praegu saadaval ainult mobiilseadmetes.


Ilmuvas uues kasutajaliideses vajutage :





- **Zapstore** või **Android APK** nuppu, kui soovite seda Androidile alla laadida;
- nuppu **iOS TestFlight**, kui kasutate iPhone'i.



![screen](assets/fr/04.webp)



Selle õpetuse jaoks teeme Androidi allalaadimise.


Kui valite allalaadimise **Zapstore** kaudu, suunatakse teid sinna. Kui olete Zapstore'is, sisestage otsinguribale **White Noise**. Seejärel jätkake allalaadimist, klõpsates **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Kui otsustate APK-faili alla laadida, suunatakse teid White Noise GitHubi repositooriumi, et valida oma nutitelefoni jaoks õige versioon.



Saadaval on järgmised APK-failid :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), sobib 64-bitise protsessoriga telefonidele;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) sobib vanematele 32-bitise protsessoriga telefonidele.



Sul on ka **.sha256** failid, mis on lihtsalt kontrollsummad, et kontrollida allalaadimise terviklikkust.



![screen](assets/fr/07.webp)



Kui allalaadimine on lõppenud, installige ja avage rakendus.



![screen](assets/fr/08.webp)



### Kasutajakonto esialgne seadistamine



Esimeseks ühendamiseks White Noise-ga vajutage nuppu **Registreeri**.



![screen](assets/fr/09.webp)



Seejärel seadistage oma profiil, valides profiilifoto, nime ja lisades enda lühikirjelduse. Te ei pea täitma oma tegelikku identiteeti (nimi ja foto).


Pange tähele, et White Noise valib teile automaatselt nime (pseudonüümi), mida saate säilitada või muuta. Lõpuks vajutage nuppu **End**.



![screen](assets/fr/10.webp)



Teid suunatakse ümber White Noise **kodukuvale**, kus teie vestlused on loetletud. Teie konto on nüüd loodud ja valmis kasutamiseks. Võite jagada oma profiili või otsida sõpru, et alustada vestlust.



![screen](assets/fr/11.webp)




### White Noise liideste avastamine



Põhiliideses, ekraani ülaosas näete :



Vasakus ülanurgas on profiili ikooniks teie profiilifoto pisipilt või teie profiili nime esimene täht. Klõpsake sellel, et pääseda oma konto seadetele.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Paremas ülanurgas on uue vestluse alustamise ikoon.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Kasutajakonto seaded



Seadete avamiseks vajutage vasakus ülanurgas olevale profiili ikoonile.



![screen](assets/fr/16.webp)



Kasutajaliidese **Settings** ülaosas leiate oma foto ja profiili nime, millele järgneb teie avalik võti, mida saate jagada, kasutades selle kõrval olevat QR-koodi.



![screen](assets/fr/17.webp)



Kohe allpool leiate nupu **Muuta kontot**, mis võimaldab teil rakenduse sees ühendada teise profiiliga.



![screen](assets/fr/18.webp)



Seejärel on teil esimene osa nelja (4) alammenüüga, näiteks :





- Profiili muutmine**



Selles alammenüüs saate muuta profiili nime, Nostr aadressi (NIP-05)... Ärge unustage muudatuste salvestamiseks klõpsata nuppu **Save**.



![screen](assets/fr/19.webp)





- Profiili võtmed**



Siin on teil juurdepääs oma avalikule ja salajasele (salajasele) võtmele. Nagu White Noise tuletab teile meelde, ei tohi teie privaatvõtit mingil juhul avaldada.



![screen](assets/fr/20.webp)





- Võrgurelee



Selles alammenüüs saate lisada või eemaldada **üldised releed** (releed, mis on määratletud kasutamiseks kõigis teie Nostr rakendustes), **inboxi releed** ja **võtmepaketi releed**.



Selleks puudutage relee kustutamiseks ikooni **prügikasti** relee ees või uue relee lisamiseks ikooni **+** (pluss).



![screen](assets/fr/21.webp)





- Ühendamise katkestamine**



Klõpsake sellel alamvalikul, et oma konto rakendusest lahti ühendada. Kuid veenduge, et olete oma privaatvõtmed salvestanud offline, sest muidu ei saa te hiljem uuesti sisse logida.



![screen](assets/fr/22.webp)




Teine osa pakub alammenüüd:





- Rakenduse seaded



Siin saate määrata rakenduse välimuse (teema ja kuvamiskeele) ning isegi kustutada andmeid, kui tunnete, et need on ohustatud või kui tunnete end ise ohus olevat.



![screen](assets/fr/23.webp)





- Annetada White Noise-le



White Noise taga olevat meeskonda (mittetulundusühing) saab toetada annetustega nende Lightning-aadressi või Bitcoin vaikiva makse aadressi kaudu.



![screen](assets/fr/24.webp)



Lõpuks, kõige allosas on **arendaja seaded**.



![screen](assets/fr/25.webp)




## Alusta vestlust



Nüüd vaatame, kuidas vestlust alustada. Kirjutamise ajal pakub White Noise kolm suhtlemisvõimalust. Uurime kordamööda **Privaatvestlusi** (**Chat 1:1**), st ainult teie ja ühe teise isiku vahel, **Rühmavestlusi** ja **Multimeediafailide saatmist**.




### Kat 1:1



Uue korrespondendi lisamiseks klõpsake põhiliideses uue vestluse alustamise ikoonil.


Seejärel skaneerige avaliku võtme QR-kood (1) või kleepige oma uue korrespondendi avalik võti (2) otsinguribale, et teda leida.



![screen](assets/fr/26.webp)



Seejärel puudutage nuppu **Käivitage vestlus**, et alustada vestlust oma korrespondendiga. Võite ka **jälgida** oma korrespondenti või kutsuda teda grupivestlusse, vajutades nuppu **Lisata gruppi**.



![screen](assets/fr/27.webp)



Teie esimene sõnum uuele korrespondendile on sarnane kutsetaotlusega. Enne kui saate temaga suhelda, peab teie korrespondent selle taotluse vastu võtma. Kui ta keeldub, noh, siis ei ole vestlus võimalik.



![screen](assets/fr/28.webp)



Veelgi enam, kui nad ei võta teie kutset vastu, ei saa nad lugeda teie esialgse sõnumi sisu.



Kui ta teie kutse vastu võtab, saab ta nüüd teile vastata ning te saate omavahel sujuvalt ja turvaliselt suhelda.



![screen](assets/fr/29.webp)



Veelgi enam, arutelus on teil lisafunktsioone.



Te saate pikalt vajutada konkreetsele sõnumile, et kuvada selliseid võimalusi nagu :




- reageerida sõnumile emotikoniga (1) ;
- vastamiseks sõnumisse **direktsitaat**, vajutades klahvi **Vastata** (2) ;
- kopeerige sõnum, vajutades **Kopeeri** (3).



![screen](assets/fr/30.webp)





- kustutage sõnum nupuga **Kustuta** ainult siis, kui see on teie poolt.



![screen](assets/fr/31.webp)



Saate otsida vestluse sees.



Klõpsake korrespondendi avataril ekraani ülaosas, et pääseda juurde "vestlusteabele", ja koputage nupule **Vestluses otsimine**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Kirjutage avanevale otsinguribale sõna, mida soovite otsida, ja käivitage otsing. Seejärel näete oma otsingusõnu esiletõstetuna **paksus kirjas**.



![screen](assets/fr/34.webp)




### Rühmavestlused



White Noise-s saab luua vestlusrühmi.



Selleks puudutage uue vestluse käivitamisliideses ikooni ja seejärel klõpsake valikut **Uus grupivestlus**. Seejärel sisestage otsinguribale selle esimese liikme avalik võti, keda soovite oma gruppi lisada.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Lõpuks, kui see valik ei toimi, sisestage otsinguribale **Uue vestluse alustamine** liidesest selle esimese liikme avalik võti, keda soovite gruppi lisada. Võite skannida ka tema avaliku võtmega seotud QR-koodi.



Seekord klõpsake nupu **Alusta vestlust** asemel nupule **Lisata gruppi**.



![screen](assets/fr/37.webp)



Ilmuvas hüpikmenüüs koputage valikut **Uus grupivestlus**.



![screen](assets/fr/38.webp)



Seejärel vajutage **Jätka** (te ei pea uuesti sisestama selle avalikku võtit).



![screen](assets/fr/39.webp)



Rühma loojana olete automaatselt selle administraator. Täitke rühma andmed, näiteks **rühma nimi ja kirjeldus**, ja vajutage seejärel nupule **Loo rühm**.



![screen](assets/fr/40.webp)



Kasutajale, kelle lisate esimeseks liikmeks, ja kõigile teistele, kelle lisate hiljem, saadetakse teade, milles kutsutakse neid grupiga liituma. Nad peavad nõustuma, klõpsates **Accept**, et rühmaga liituda.



![screen](assets/fr/41.webp)



Samuti on võimalik lisada uus liige, kellega te juba vestlete olemasolevasse gruppi. Selleks klõpsake korrespondendi avataril ekraani ülaosas, et pääseda "vestlusinfole" ja vajutage nupule **Lisata gruppi**.



![screen](assets/fr/42.webp)



Avanevas uues kasutajaliideses **märgistage** rühm, kuhu soovite teda lisada, ja koputage valikut **Lisata rühma**. Jääb vaid oodata, et ta nõustuks rühmaga liituma.



![screen](assets/fr/43.webp)



Pange tähele, et ainult grupi administraator saab muuta grupi teavet ja lisada või kustutada liikmeid. Samuti takistab võtmete rotatsioon keelustatud liikmete tulevaste sõnumite dekrüpteerimist.



Liikme eemaldamiseks puudutage rühma põhiliidesest rühma infoliidesele pääsemiseks ülevalpool asuvat rühma ikooni.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Seejärel klõpsake liikme nimele ja **Eemalda rühmast**. Sellest kasutajaliidesest saate talle ka sõnumi saata, teda jälgida või lisada teise gruppi.



![screen](assets/fr/46.webp)



### Multimeediafailide saatmine



Hetkel saab White Noise kasutajate vahel jagada ainult fotosid. Kas olete privaatvestluses või grupivestluses, selleks peate :





- vajutage tekstisõnumi sisestusvälja vasakul poolel asuvat sümbolit **pluss (+)**.



![screen](assets/fr/47.webp)





- seejärel klõpsake allosas oleval kastil **Fotod**, et pääseda oma galeriisse.



![screen](assets/fr/48.webp)





- valige foto(d), mille soovite saata.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Peamised punktid, mida meeles pidada



White Noise pakub head konfidentsiaalsuse taset ja kõrgetasemelist turvalisust. Teisest küljest on tegemist väga uue rakendusega, mis ei ole veel väga levinud ja on alles lapsekingades. Sellest tulenevalt on veel liiga vara teha aktiivseid järeldusi. Kasutamise käigus võib esineda mõningaid tõrkeid.



Praegu puuduvad sellel teatavad funktsioonid (puuduvad audio- või videokõned, audio- või videomultimeediafailide saatmine) võrreldes populaarsete sõnumirakendustega.



Sellest hoolimata on White Noise endiselt huvitav võimalus vestlusteks, kus konfidentsiaalsus on esmatähtis (nt perekonna, lähedaste sõprade või ühise eesmärgi aktivistidega), isegi kui selle paigaldamine (alternatiivsete rakenduspoodide või APK-failide kaudu) ja õppimine (võtmepaaride, klientide ja releede kontseptsiooni mõningane omandamine Nostr protokolliga) nõuab veidi vaeva.



Nüüd tead, kuidas kasutada White Noise, et suhelda turvaliselt oma sõprade ja pereliikmetega. Palun andke meile pöidlaid üles, kui see õpetus on teie arvates kasulik.



Soovitame meie õpetust Tox vestluse kohta, mis võimaldab teil ilma vahendajateta vestelda detsentraliseeritud Tox protokolli kaudu.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3