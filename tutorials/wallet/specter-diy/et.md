---
name: Specter DIY
description: Specter DIY seadistusjuhend
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks kirjutavad koodi. Me teame, et keegi peab kirjutama tarkvara, et kaitsta eraelu puutumatust, ja kuna me ei saa eraelu puutumatust, kui me kõik seda ei tee, siis me kirjutame seda.

*Cypherpunk manifest - Eric Hughes - 9. märts 1993*


Projekti idee on ehitada riistvara wallet valmiskomponentidest.

Kuigi meil on olemas laiendusplaat, mis paneb kõik kenasse vormi ja aitab teil vältida jootmist, jätkame standardkomponentide toetamist ja ühilduvuse säilitamist.


![image](assets/fr/01.webp)


Samuti soovime hoida projekti paindlikuna, et see saaks töötada mis tahes muu komponentide komplektiga minimaalsete muudatustega. Võib-olla soovite teha riistvaralise wallet teistsugusel arhitektuuril (RISC-V?), millel on kommunikatsioonikanaliks audiomodem - see peaks olema võimalik. Specteri funktsionaalsust peaks olema lihtne lisada või muuta ja me püüame abstraheerida loogilisi mooduleid nii palju kui võimalik.


QR-koodid on Specteri vaikimisi viis suhelda vastuvõtjaga. QR-koodid on üsna mugavad ja võimaldavad kasutajal kontrollida andmeedastust - iga QR-kood on väga piiratud võimsusega ja side toimub ühesuunaliselt. Ja see on airgapped - te ei pea wallet igal ajal arvutiga ühendama.


Saladuste salvestamiseks toetame agnostilist režiimi (wallet unustab kõik saladused, kui see on välja lülitatud), hoolimatut režiimi (salvestab saladused rakenduse mikrokontrolleri flashis) ja peagi on tulemas secure element integratsioon.


Meie põhirõhk on mitme allkirja seadistamisel koos teiste riistvaraliste rahakottidega, kuid wallet võib töötada ka üksikallkirjastajana. Me püüame teha seda Bitcoin Core'iga ühilduvaks, kus saame - PSBT allkirjastamata tehingute jaoks, wallet kirjeldused mitme allkirjaga rahakottide importimiseks/eksportimiseks. Bitcoin Core'iga lihtsamalt suhtlemiseks töötame ka [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - väike python flask server, mis räägib teie Bitcoin Core'i sõlmega.


Enamik püsivara on kirjutatud MicroPythonis, mis muudab koodi hõlpsasti auditeeritavaks ja muudetavaks. Elliptiliste kõverate arvutamiseks kasutame Bitcoin Core'i raamatukogu [secp256k1](https://github.com/bitcoin-core/secp256k1) ja graafilise kasutajaliidese jaoks [LittlevGL](https://lvgl.io/).


## Vastutusnõue


Projekt on oluliselt laienenud, nii et Specter-DIY turvalisuse tase on nüüd võrreldav turul olevate kommertslike riistvaraliste rahakottidega. Rakendasime turvalise alglaaduri, mis kontrollib püsivara uuendusi, nii et võite olla kindel, et seadmesse saab pärast esmast seadistamist laadida ainult allkirjastatud püsivara. Erinevalt kommertslike allkirjastatud seadmete puhul peab kasutaja siiski bootloaderi käsitsi paigaldama ja seda ei ole seadme müüja tehases seadistatud. Seega pöörake esialgse püsivara paigaldamise ajal erilist tähelepanu ja veenduge, et olete kontrollinud PGP-allkirju ja flashinud püsivara turvalisest arvutist.


Kui midagi ei tööta, ava probleem siin või küsi küsimus meie [Telegram grupis](https://t.me/+VEinVSYkW5TUl5Ai).


## Specter-DIY ostunimekiri


Siin kirjeldame, mida osta, ja kokkupaneku järgmises osas selgitame, kuidas seda kokku panna, ning mõned märkused plaadi kohta - toitejumperid, USB-pordid jne.


### Avastuslaud


Seadme peamine osa on arendusplaat:



- STM32F469I-DISCO arendusplaat (nt [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) või [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB kaabel
- Standardne MicroUSB-kaabel USB-kaabli kaudu suhtlemiseks


Vabatahtlik, kuid soovitatav:


- [Waveshare QR-koodi skanner](https://www.waveshare.com/barcode-scanner-module.htm) koos pikkade viiguotsikutega nagu [need](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) või [need](https://www.amazon.com/gp/product/B015KA0RRU/), et ühendada skanner tahvliga (vaja on 4 viiguotsikut).


Praegu töötame laiendusplaadi kallal, mis sisaldab kiipkaardipesa, QR-koodi skannerit, akut ja 3d-prinditud korpust, kuid see ei sisalda peamist osa - avastamisplaati, mille peate eraldi tellima. Nii ei ole tarneahela rünnak endiselt probleemiks, sest turvalisuskriitilised komponendid ostetakse juhuslikust elektroonikapoest.


Specterit saab hakata kasutama ka ilma lisakomponentideta, kuid sa saad sellega suhelda USB või sisseehitatud SD-kaardipesa kaudu. Specteri kasutamine üle USB tähendab, et see ei ole õhu kaudu ühendatud, seega kaotate olulise turvaomaduse.


### QR-skanner


QR-koodi skanneri jaoks on teil mitu võimalust.


**Võimalus 1. Soovitatav.** Vastupidi hea skanner Waveshare'ilt (40$)


[Waveshare skanner](https://www.waveshare.com/barcode-scanner-module.htm) - peate leidma viisi, kuidas seda kenasti paigaldada, võib-olla kasutate mingit Arduino prototüübi kilpi ja veidi teipi.


Jootmist ei ole vaja, aga kui sul on jootmisoskused, saad wallet palju ilusamaks teha ;)


**Võimalus 2.** Mikroe väga kena skanner, kuid üsna kallis (150$):


[Barcode Click](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Võimalus 3.** Mis tahes muu QR-skanner


Hiinas on võimalik leida odavaid skannereid. Nende kvaliteet ei ole sageli nii hea, kuid võite proovida. Võib-olla isegi ESPcamera teeb seda tööd. Teil on vaja ühendada ainult toide, UART (viigud D0 ja D1) ja päästik D5.


**Võimalus 4.** Skanner puudub.


Siis saate Specterit kasutada ainult USB / SD-kaardiga.


Kui te ei ehita omaenda kommunikatsioonimoodulit, mis kasutab QR-koodide asemel midagi muud - audiomodem, bluetooth või midagi muud. Niipea, kui seda saab käivitada ja saata andmeid üle jadaühenduse, saate teha, mida iganes soovite.


### Valikulised komponendid


Kui lisate pisikese energiapanga või aku ja akulaadija/võimendi, muutub teie wallet täiesti iseseisvaks ;)



## Specter-DIY kokkupanek



![video](https://youtu.be/1H7FqG_FmCw)


### Waveshare vöötkoodiskänneri ühendamine


wallet püsivara konfigureerib skanneri teie eest esimesel käivitamisel, seega ei ole käsitsi eelkonfigureerimine vajalik.


Järgnevalt on kirjeldatud, kuidas ühendada skanner tahvliga:


![image](assets/fr/02.webp)


Mugavuse huvides võite osta Arduino Protype kilbi ja joota ja paigaldada kõik selle peale (nt [see](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Energiamajandus


Plaadi ülemisel küljel on hüppaja, mis määrab, kust see toite võtab. Saate muuta hüppaja asendit ja valida toiteallikaks ühe USB-portidest või VIN-pini ja ühendada sinna välise aku (peaks olema 5V).


### Karbid DIY jaoks


Vaadake kausta [lisad](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Ole loominguline!


Koosta oma Specter-DIY ja saada meile pildid (tee pull request või võta meiega ühendust).


Vaata [Galerii](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) koos kogukonna poolt kokku pandud Spectersidega!




## Kompileeritud koodi paigaldamine


Turvalise alglaadijaga on püsivara esialgne paigaldamine veidi erinev. Uuendamine on lihtsam ja ei nõua riistvara wallet ühendamist arvutiga.


![video](https://youtu.be/eF4cgK_L6T4)


### Esialgse püsivara väljalülitamine


**Märkus** Kui te ei soovi kasutada binaarsüsteeme väljaannetest, vaadake [bootloader documentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md), mis selgitab, kuidas seda kompileerida ja konfigureerida, et kasutada oma avalikke võtmeid meie võtmete asemel.



- Kui te uuendate versiooni alla `1.4.0` või laadite püsivara esimest korda üles, kasutage `initial_firmware_<version>.bin` leheküljelt [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Kontrollida faili `sha256.signed.txt` allkirja [Stepan's PGP key](https://stepansnigirev.com/ss-specter-release.asc) suhtes
 - Kontrollida faili `initial_firmware_<version>.bin` hash'i võrreldes failis `sha256.signed.txt` salvestatud hash'iga
- Kui te uuendate tühjast alglaadijast või näete alglaadija veateadet, et püsivara ei ole kehtiv, vaadake järgmist jaotist - allkirjastatud Specteri püsivara väljalülitamine.
- Veenduge, et teie avastamisplaadi toitejumper on asendis STLK
- Ühendage avastamisplaat arvutiga plaadi peal oleva **miniUSB** kaabli kaudu.
    - Plaat peaks ilmuma eemaldatava kettana nimega `DIS_F469NI`.
- Kopeerige fail `initial_firmware_<version>.bin` failisüsteemi `DIS_F469NI` juurtesse.
- Kui tahvel on püsivara väljalülitamise lõpetanud, lähtestab tahvel end ise ja taaskäivitub alglaadijale. Bootloader kontrollib püsivara ja käivitub põhifirmavara. Kui näete veateadet, et püsivara ei ole leitud - järgige uuendamisjuhiseid ja laadige püsivara SD-kaardi kaudu üles.
- Nüüd saate lülitada toitejumpi sinna, kuhu soovite, ja toitepangast või akust toidab tahvlit.


Esialgse püsivara väljalülitamine faili `.bin` copy-paste abil ei õnnestu mõnikord - sageli kaabli tõttu või kui ühendate seadme USB-keskuse kaudu. Sellisel juhul võite proovida veel paar korda (tavaliselt töötab 2-3 katsega).


Kui see ei õnnestu kogu aeg, võite kasutada [stlink](https://github.com/stlink-org/stlink/releases/latest) avatud lähtekoodiga tööriista. Installige see ja sisestage see oma terminali: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. See töötab tavaliselt palju usaldusväärsemalt.


### Firmware uuendamine



- Lae alla `specter_upgrade_<versioon>.bin` [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Kopeerige see binaarskeem SD-kaardi (FAT-vorminguga, maksimaalselt 32 GB) juurtele
 - Veenduge, et juurkataloogis on ainult üks fail `specter_upgrade***.bin`
- Sisestage SD-kaart avastamisplaadi SD-pessa ja lülitage plaat sisse
- Bootloader flashib püsivara ja teatab teile, kui see on tehtud.
- Käivitage tahvel uuesti - nüüd näete Specter-DIY kasutajaliidest, mis soovitab teil valida oma PIN-koodi


Iga kord, kui uus versioon ilmub, laadige lihtsalt alla `specter_upgrade_<version>.bin` versioonidest, visake see SD-kaardile ja uuendage seadet nagu eelmises sammus. Bootloader veendub, et pardale saab laadida ainult allkirjastatud firmware'i.


### Kuidas leida püsivara versiooni


Minge menüüsse "Seadme seaded" - seal kuvatakse ekraani pealkirja all versiooni number.


## Kasutage Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Specter-DIY turvalisus


### Riistvara


Näidikut kontrollib rakenduse MCU.


Turvaliste elementide integreerimine ei ole veel olemas - praegu salvestatakse saladusi ka peamise MCU-s. Kuid wallet saab kasutada ilma saladust salvestamata - peate iga kord sisestama oma taastamisfraasi. Milleks mäletada pikka passphrase, kui saab mäletada kogu mnemoonikat?


Seade kasutab mõnede failide salvestamiseks välist välismälu (QSPI), kuid kõik kasutajafailid on allkirjastatud wallet poolt ja kontrollitud laadimisel.


QR-skaneerimisfunktsioon on eraldi mikrokontrolleril, nii et kogu pilditöötlus toimub väljaspool turvakriitilist MCU-d. Praegu haldab USB ja SD-kaarti endiselt peamine MCU, seega ärge kasutage SD-kaarti ja USB-d, kui soovite vähendada rünnakupinda.


### PIN-kaitse (kasutaja autentimine)


Esimese käivitamise ajal luuakse peamise MCU-s unikaalne saladus. See saladus võimaldab kontrollida, et seade ei ole asendatud pahatahtliku seadmega - PIN-koodi sisestamisel kuvatakse nimekiri sõnadest, mis jäävad saladuse olemasolu ajal samaks.


Teie PIN-koodi koos selle unikaalse saladusega kasutatakse generate dekrüpteerimisvõtme jaoks teie Bitcoin võtmete jaoks (kui te neid salvestate). Seega, kui ründaja suudaks PIN-koodi ekraanist mööda minna, siis dekrüpteerimine ikkagi ebaõnnestub.


Kui olete lukustanud püsivara (TODO: lisage siia juhiste link), lukustab see tõhusalt ka saladuse, nii et kui ründaja flashib pardale teistsuguse püsivara, kustutatakse saladus ja te saate selle ära tunda, kui hakkate PIN-koodi sisestama - sõnade järjestus on erinev.


### Taastamislause genereerimine


See on üks wallet kõige olulisemaid osi - generate võtme turvaliselt. Selleks, et seda hästi teha, kasutame mitut entroopia allikat:



- Mikrokontrolleri TRNG. Omane, sertifitseeritud ja tõenäoliselt hea, kuid me ei usalda seda
- Puuteekraan. Iga kord, kui ekraani puudutate, mõõdame asukohta ja hetke, mil see puudutus toimus (mikrokontrolleri tiksudes 180MHz juures).
- Sisseehitatud mikrofonid - veel mitte. Tahvlil on kaks mikrofoni, nii et riistvara wallet saab teid kuulata ja segada need andmed entroopiakogumisse.


Kogu see entroopia on kokku räsitud ja teisendatud teie taastumisfraasiks. Saadud entroopia on alati parem kui üksikud allikad.


### Kõrgetasemeline loogika - rahakotid


Specter tegutseb võtmesalvestusena. See hoiab HD privaatvõtmeid, mida saab kaasata rahakottidesse. Rahakotid on määratletud nende kirjelduste abil. Me toetame ka miniskripti.


Iga wallet kuulub konkreetsesse võrku. See tähendab, et kui te impordite wallet võrku `testnet`, siis ei ole see saadaval `mainnet` või `regtest` - te peate lülituma sellesse võrku ja importima wallet eraldi.


### Tehingute kontrollimine


Järgmised eeskirjad kehtivad tehingute suhtes, mida wallet allkirjastab:



- kui leitakse segatud sisendid erinevatest rahakottidest, hoiatatakse kasutajat ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- muuta väljundid näitavad wallet nime, millele need saadetakse
- multisig või miniskripti kasutamiseks tuleb kõigepealt importida wallet, lisades wallet kirjelduse (QR, USB või SD-kaardi kaudu)


## Deskriptorite toetus


Kõik tavalised Bitcoin kirjeldajad töötavad. Peale selle on meil mõned laiendused:


### Mitu haru kirjeldustes


Et QR-koodides ruumi kokku hoida, lubame korraga lisada mitme haruga kirjeldusi. Kui soovite kasutada `wpkh(xpub/0/*)` vastuvõtuaadresside jaoks ja `wpkh(xpub/1/*)` muutmisaadresside jaoks, saate neid kombineerida ühte kirjeldajasse: `wpkh(xpub/{0,1}/*)` - wallet käsitleb `{}` kogumiosa esimest indeksit kui vastuvõtuaadresside haru ja teist kui muutmisaadresside haru.


Samuti saab määrata rohkem kui kaks haru ja haruindeksid võivad olla erinevate kaasallkirjutajate puhul erinevad, seega on see kirjeldus väga veider, kuid täiesti kehtiv:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Siin kasutab wallet aadressi number 17 vastuvõtmiseks skripti `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Ainus nõue on, et indeksite arv kõigis komplektides on sama (ülaltoodud juhul 3).


### Vaikimisi tuletised


Kui kirjeldus sisaldab avalikke põhivõtmeid, kuid ei sisalda metsikuid tuletisi, lisatakse kõikidele laiendatud võtmetele kirjelduses vaikimisi tuletis `/{0,1}/*`. Kui vähemalt üks xpubidest sisaldab metsikut tuletist, siis kirjeldajat ei muudeta.


Deskriptor `wpkh(xpub)` teisendatakse `wpkh(xpub/{0,1}/*)`.


### Miniskript


Specter toetab miniscripti, kuid ei toeta poliitikast miniscripti koostamist (sest see on liiga kallis). Me teeme miniskriptis mõningaid kontrolle, nii et ainult `B` skriptid on lubatud ülemisel tasemel ja kõik argumendid alam-miniskriptides peavad omama [spec](http://bitcoin.sipa.be/miniscript/) kohaseid omadusi.


Saate kasutada [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/), et generate kirjeldada poliitikast ja seejärel importida see wallet-sse.


Näiteks poliitika "ma võin kulutada praegu või 100 päeva pärast minu naine võib kulutada" saab wallet-ks ümber kujundada nii:


Poliitika: (minu võti on 9 korda tõenäolisem)


Miniskript: `või_d(pk(xpubA),ja_v(v:pkh(xpubB),vanemad(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Kuna meil ei ole siin mingeid metsikuid tuletisi, siis lisatakse xpubs'ile vaikimisi tuletised `/{0,1}/*`.



---

MIT litsents


Autoriõigus (c) 2019 cryptoadvance


---