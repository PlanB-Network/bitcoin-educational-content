---
name: Saadik
description: Passi seadistamine ja kasutamine koos Envoy rakendusega
---
![cover](assets/cover.webp)

Envoy on Bitcoini rahakoti haldamise rakendus, mille on välja töötanud Foundation. See on spetsiaalselt mõeldud kasutamiseks koos Passport riistvaralise rahakotiga.

Passport "*Batch 2*", mida esitleme selles juhendis koos Envoy rakendusega, on "*Founder's Edition*" järglane. See eristub oma kvaliteetse disaini, kõrglahutusega värviekraani ja ergonoomilise füüsilise klaviatuuriga. See töötab "*Air-Gap*" režiimis, tagades, et teie rahakoti privaatvõtmed jäävad täielikult isoleerituks, kus andmevahetus toimub MicroSD-kaardi või QR-koodide kaudu. Seade on varustatud eemaldatava ja laetava Nokia BL-5C akuga mahutavusega 1200 mAh. See mitteomandiline aku on kergesti asendatav, kuna BL-5C mudelit on lihtne leida kaubanduses.

Mis puutub ühenduvusse, siis on Passport varustatud MicroSD-pordi, USB-C-pordi laadimiseks ja tagakaameraga QR-koodide skaneerimiseks.

Turvalisuse osas sisaldab Passport turvalist elementi ja seadme lähtekood on täielikult avatud lähtekoodiga. See pakub kõiki funktsioone, mida ühelt healt Bitcoini riistvaraliselt rahakotilt oodatakse. Pange tähele, et Passport ei toeta veel miniscripti, kuid see funktsioon on kavas 2025. aasta teises kvartalis.

Hinnaga $199 on Passport positsioneeritud kui kõrgekvaliteediline riistvaraline rahakott, mis konkureerib Coldcard Q, Jade Plus, Tezor Safe 5 ja Ledgeri tippmudelitega.

![Image](assets/fr/01.webp)

Oma turvalise rahakoti haldamiseks Passportiga on teil mitu võimalust. See riistvaraline rahakott ühildub enamiku turul olevate rahakoti haldamise tarkvaradega, sealhulgas Sparrow Wallet, Specter Desktop, Nunchuk, Keeper jt.

Selles õpetuses, mis on mõeldud algajatele ja edasijõudnutele, tutvustame, kuidas kasutada Envoy rakendust koos Passportiga. See on lihtsaim viis, kuidas oma riistvara rahakotist kõige rohkem kasu saada.

Kui olete edasijõudnud kasutaja ja soovite uurida keerulisemaid funktsioone, siis soovitan vaadata seda teist õpetust, kus me konfigureerime Passport'i koos Sparrow Wallet'iga :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Passi lahtipakkimine

Kui saate oma passi kätte, veenduge, et pakendi kast ja pitser on terved, et kinnitada, et pakki ei ole avatud. Seadme seadistamisel toimub ka seadme autentsuse ja terviklikkuse tarkvaraline kontroll.

![Image](assets/fr/02.webp)

Karbi sisu sisaldab:


- Pass;
- Tükk pappi, kuhu kirjutada oma mälulause;
- USB-C-kaabel laadimiseks ;
- MicroSD-kaart ;
- Kaks MicroSD- ja Lightning- või USB-C-adapterit ;
- Kleebised.

Seadmest leiate :


- Klaviatuur (1) ;
- USB-C port (2);
- Kustutamise nupp (3);
- Tagasi pöördumise nupp (4) ;
- Kinnitusnupp (5);
- Suunaplaat (6);
- Sisse/välja nupp (7);
- Olekuindikaator (8);
- MicroSD-port (9) ;
- Nupp režiimi muutmiseks aA1 (10) ;
- Tagumine kaamera.

![Image](assets/fr/03.webp)

## Envoy taotluse allalaadimine

Minge oma rakenduste poest, et laadida alla Envoy :


- [Google Play poes](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- On [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

APK-faili saab alla laadida ka otse [sihtasutuse GitHubi repositooriumist](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Kui rakendus on avatud, valige "*Passi haldamine*".

![Image](assets/fr/52.webp)

Valige, kas soovite aktiveerida Tor-ühenduse konfidentsiaalsuse tugevdamiseks, seejärel vajutage "*Jätka*".

![Image](assets/fr/53.webp)

Valige "*Liigita olemasolev Passport*", kui teie Passport on juba konfigureeritud, või "*Uue Passport'i seadistamine*", kui seadistate oma riistvaralise rahakoti esimest korda.

![Image](assets/fr/54.webp)

Nõustuge kasutustingimustega.

![Image](assets/fr/55.webp)

Seejärel palutakse teil kontrollida passi ehtsust. Klõpsake nuppu "*Järgmine*".

![Image](assets/fr/56.webp)

## Alustades passi

Seadme käivitamiseks vajutage seadme küljel olevat sisse-/väljalülitusnuppu.

![Image](assets/fr/04.webp)

Vajutage kinnitamisnuppu, et pääseda järgmisesse menüüsse.

![Image](assets/fr/05.webp)

Selles õpetuses kasutame Envoy't, et hallata Passportiga kaitstud rahakotti. Valige "*Envoy App*".

![Image](assets/fr/57.webp)

Klõpsake nuppu "*Jätka saadetisena*".

![Image](assets/fr/58.webp)

Järgmine samm on seadme kontrollimine. Sellega kinnitatakse teie passi ehtsust ja tagatakse, et seda ei ole transiidi ajal võltsitud. Teil palutakse skaneerida QR-kood.

![Image](assets/fr/08.webp)

Skaneerige oma passiga rakenduses kuvatavaid dünaamilisi QR-koode. Kui skannimine on lõpetatud, klõpsake nuppu "*Järgmine*".

![Image](assets/fr/59.webp)

Seejärel skannige oma telefoniga passil kuvatavat QR-koodi.

![Image](assets/fr/60.webp)

Kui ilmub teade "* Teie pass on turvaline*", kinnitab see, et teie riistvaraline rahakott on ehtne. Nüüd saate seda kasutada Bitcoini rahakoti kindlustamiseks.

![Image](assets/fr/61.webp)

Kinnitage testitulemus oma passis.

![Image](assets/fr/14.webp)

## PIN-koodi seadistamine

Järgneb PIN-koodi samm. PIN-kood avab teie passi lukustuse. Seega pakub see kaitset volitamata füüsilise juurdepääsu eest. PIN-kood ei ole seotud teie rahakoti krüptograafiliste võtmete tuletamisega. Seega isegi ilma PIN-koodile juurdepääsuta võimaldab teie 12- või 24-sõnalise mnemoonilise fraasi omamine taastada juurdepääsu oma bitcoinidele.

![Image](assets/fr/15.webp)

Soovitame valida võimalikult juhusliku PIN-koodi. Samuti salvestage see kood kindlasti eraldi kohta, kus teie passi hoitakse (nt paroolihaldurisse).

PIN-koodi saab valida 6 kuni 12-kohalise koodi. Soovitan teha see võimalikult pikaks.

Kasutage PIN-koodide sisestamiseks klahvistikku. Kui olete lõpetanud, klõpsake kinnituse nupule.

![Image](assets/fr/16.webp)

Kinnitage oma PIN-kood teist korda.

![Image](assets/fr/17.webp)

Teie PIN-kood on registreeritud.

![Image](assets/fr/18.webp)

## Passi püsivara uuendamine

Teie riistvara rahakott soovitab teil oma püsivara uuendada. Soovitan teil kohe uuendada, et saada kasu viimaste versioonidega kaasnevatest parandustest ja parandustest. Jätkamiseks klõpsake paremal asuval kinnituse nupul.

![Image](assets/fr/19.webp)

Teie Passport on valmis uue püsivara vastuvõtmiseks MicroSD-kaardi kaudu.

![Image](assets/fr/20.webp)

### Ilma Envoy taotluseta

Selleks kasutage oma Passport'i karbis sisalduvat MicroSD-kaarti (või mõnda muud) ja sisestage see arvutisse. Laadige uusim püsivara versioon alla [Sihtasutuse dokumentatsiooni veebisaidilt](https://docs.foundation.xyz/firmware-updates/passport/) või [nende GitHubi repositooriumist](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Enne seadmesse paigaldamist soovitame tungivalt kontrollida allalaetud püsivara autentsust ja terviklikkust. Kui vajate selleks abi, vaadake seda õpetust :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Rakendusega Envoy

Teine, lihtsam võimalus on kasutada otse Envoy rakendust. Klõpsake nupule "*Download Firmware*".

![Image](assets/fr/62.webp)

MicroSD-kaardi ühendamiseks telefoniga kasutage Passportiga kaasas olevat adapterit.

![Image](assets/fr/63.webp)

Valige püsivara salvestamiseks MicroSD-kaart oma failiotsingusüsteemis.

![Image](assets/fr/64.webp)

Firmware on nüüd salvestatud. Eemaldage MicroSD-mäluseade nutitelefonist ja sisestage see Passporti.

![Image](assets/fr/65.webp)

Avaneb Passport failiotsinguprogramm. Valige fail `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Klõpsake nuppu "*Vali*".

![Image](assets/fr/23.webp)

Seejärel kinnitage püsivara paigaldamine.

![Image](assets/fr/24.webp)

Palun oodake, kuni uuendus on lõpule viidud.

![Image](assets/fr/25.webp)

Kui värskendus on lõpule viidud, sisestage PIN-kood, et avada seade ja jätkata seadistamist.

![Image](assets/fr/26.webp)

## Uue Bitcoini rahakoti loomine

Nüüd on aeg luua uus Bitcoini rahakott. Klõpsake kinnituse nupule.

![Image](assets/fr/27.webp)

Uue portfelli loomiseks klõpsake "*Loo uus seemne*".

![Image](assets/fr/28.webp)

Saate valida 12- või 24-sõnalise mälulause vahel. Mõlema valiku pakutav turvalisus on sarnane, seega võite valida selle, mida on kõige lihtsam salvestada, st 12 sõna.

![Image](assets/fr/29.webp)

Klõpsake nuppu "*Jätka*".

![Image](assets/fr/30.webp)

Teie pass genereerib nüüd teie "*Backup Code*". See on numbrite seeria, mida saab kasutada oma rahakoti varukoopia dekrüpteerimiseks, mis on salvestatud MicroSD-lehele. See Foundationi seadmetele omane varundussüsteem kujutab endast täiendavat varundust teie mnemofraasile, kuid ei ühildu muu Bitcoini tarkvaraga.

Kui otsustate kasutada seda "*Backup-koodi*", siis hoidke seda kindlasti teises kohas kui oma MicroSD-kood, mis sisaldab teie rahakoti krüpteeritud varukoopiat. Te võite siiski otsustada seda süsteemi mitte kasutada, kui tunnete, et teie müntide hea varukoopia on piisav.

![Image](assets/fr/31.webp)

Sisestage oma "*Backup Code*", et kinnitada, et olete selle õigesti salvestanud.

![Image](assets/fr/32.webp)

Kui sisestatud on MicroSD-mälukaart, on teie portfelli krüpteeritud varukoopia salvestatud sinna.

![Image](assets/fr/33.webp)

Teie passis kuvatakse teie 12-sõnaline mälulause. See mnemoonik annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele. Igaüks, kes seda fraasi teab, võib teie raha varastada, isegi kui tal puudub füüsiline juurdepääs teie passile.

12-sõnaline fraas taastab juurdepääsu teie bitcoinidele, kui teie pass läheb kaduma, varastatakse või puruneb. Seetõttu on väga oluline seda hoolikalt salvestada ja turvalises kohas hoida.

Võite kirjutada selle karbis olevale papile või täiendava turvalisuse tagamiseks soovitan graveerida selle roostevabast terasest alusele, et kaitsta seda tulekahju, üleujutuse või kokkuvarisemise eest.

Klõpsake kinnituse nupule, et näha oma mälulause.

![Image](assets/fr/34.webp)

Lisateavet selle kohta, kuidas oma mnemofraasi õigesti salvestada ja hallata, soovitan kindlasti jälgida seda teist õpetust, eriti kui olete algaja:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

loomulikult ei tohi te neid sõnu kunagi internetis jagada, nagu ma seda käesolevas õpetuses teen. Seda näidisportfelli kasutatakse ainult Testnetis ja see kustutatakse õpetuse lõpus.**_

Tehke sellest lausest füüsiline varukoopia.

![Image](assets/fr/35.webp)

Teie pass on edukalt konfigureeritud. Jätkamiseks klõpsake kinnituse nupule.

![Image](assets/fr/36.webp)

## Portfelli seadistamine Envoy's

Selles õpetuses näitan teile, kuidas kasutada passi koos rakendusega Envoy. Kuid see riistvaraline rahakott ühildub ka Sparrow Walleti, Keeperi, BlueWalleti, Nunchuki, Specteri ja paljude teistega...

![Image](assets/fr/66.webp)

Kasutage Envoy rakendust, et skaneerida oma passil kuvatavat QR-koodi.

![Image](assets/fr/67.webp)

Teie avalikud võtmed on nüüd rakendusse imporditud. Vajutage nupule "*Valideeri vastuvõtuaadress*".

![Image](assets/fr/68.webp)

Kasutage oma passi, et skaneerida Envoy's kuvatavat aadressi.

![Image](assets/fr/69.webp)

Teie pass kinnitab, kas Envoy kaudu imporditud rahakott on kehtiv. Kinnitage see taotluses.

![Image](assets/fr/70.webp)

Nüüd saate juurdepääsu oma rahakoti avalikele andmetele Envoy's, kuid bitcoinide kulutamiseks peate kasutama oma passi.

![Image](assets/fr/71.webp)

## Avasta passi menüüd

Teie passi kasutajaliidesel on kolm peamist menüüd:


- "*Konto*";
- "*Mitte*";
- "*Settings*".

Nende menüüde vahel navigeerimiseks kasutage suunaja noolt vasakule ja paremale.

### *Konto*" menüü

Menüüst "*Konto*" leiate oma Bitcoini rahakoti põhifunktsioonid. Tehingu saate allkirjastada kas kaamera või MicroSD-pordi kaudu.

![Image](assets/fr/37.webp)

Allmenüü "*Konto tööriistad*" pakub selliseid võimalusi nagu aadressi kontrollimine, sõnumi allkirjastamine või portfellis olevate aadresside vaatamine.

![Image](assets/fr/38.webp)

Allmenüüst "*Konto haldamine*" saate ühendada oma Bitcoini rahakoti rahakoti haldamise tarkvaraga (mida käsitleme selle õpetuse järgmistes sammudes) või vaadata ja ümber nimetada oma konto.

![Image](assets/fr/39.webp)

### Menüü "Rohkem

Menüüs "*More*" saate luua oma portfellis uue konto, mis on seotud sama mnemofraasiga.

![Image](assets/fr/40.webp)

Võite sisestada ka BIP39 paroolfraasi või kasutada ajutist seemet.

![Image](assets/fr/41.webp)

### Menüü "Seaded

Menüüst "*Settings*" leiate kõik oma rahakoti ja seadme seaded.

![Image](assets/fr/42.webp)

Alammenüü "*Seade*" annab teile võimalusi ekraani heleduse kohandamiseks, automaatse lukustuse eelse viivituse määramiseks, PIN-koodi muutmiseks või seadme ümbernimetamiseks.

![Image](assets/fr/43.webp)

"*Backup*" alammenüü võimaldab teil eksportida oma krüpteeritud portfelli varukoopia, kontrollida olemasoleva varukoopia kehtivust või otsida uuesti oma "*Backup Code*".

![Image](assets/fr/44.webp)

Alammenüü "*Firmware*" on mõeldud Passport'i püsivara uuendamiseks. Soovitame neid uuendusi regulaarselt teha, et saada kasu uusimatest parandustest ja funktsioonidest.

![Image](assets/fr/45.webp)

"*Bitcoin*" alammenüü võimaldab teil muuta kuvatavat ühikut (BTC või satoshis), hallata võimalikku Multisig rahakotti või lülitada režiimi "*Testnet*".

![Image](assets/fr/46.webp)

Valikus "*Advanced*" saate vaadata oma mnemofraasi sõnu, teha sisestatud MicroSD-kaardiga toiminguid, lähtestada passi tehaseseadetele või teostada autentsuskontrolli, nagu eelnevalt tehtud.

![Image](assets/fr/47.webp)

Saate aktiveerida funktsiooni "*Turvasõnad*", mis lisab turvakihi, kuvades pärast PIN-koodi esimese nelja numbri sisestamist seadme avamisel kaks konkreetset sõna. Need sõnad, mis salvestatakse seadistamise ajal, tagavad, et Passport ei ole välja vahetatud ega võltsitud. Hilisemate lahknevuste korral soovitame seadet mitte kasutada. Soovitan teil aktiveerida see valik, et vältida enamikku seadme füüsilise rikkumise riske.

![Image](assets/fr/48.webp)

Lõpuks võimaldab alammenüü "*Laiendused*" aktiveerida seadme teatud kasutusviisidele omaseid funktsioone, näiteks Whirlpooli coinjoin-protokolli.

![Image](assets/fr/49.webp)

## Bitcoinide vastuvõtmine

Nüüd, kui teie pass on loodud, olete valmis saama oma esimesed satsid oma uude Bitcoini rahakotti. Selleks klõpsake Envoy's oma "*Primary 0*" kontol.

![Image](assets/fr/72.webp)

Vajutage nupule "*Vastuvõtmine*".

![Image](assets/fr/73.webp)

Teie Envoy rakendus kuvab teie rahakoti esimese vaba tühja aadressi. Enne selle kasutamist kontrollime aadressi Passport ekraanil, et veenduda, et see tõesti kuulub meie Bitcoini rahakotile. Valige oma Passport'i menüüst "*Account*", valige "*Account Tools*".

![Image](assets/fr/74.webp)

Klõpsake nupule "*Verify Address*", seejärel skaneerige Envoy's kuvatavat QR-koodi.

![Image](assets/fr/75.webp)

Veenduge, et passis näidatud aadress vastab täpselt Sparrow's näidatud aadressile ja et kuvatakse "*Kontrollitud*".

![Image](assets/fr/76.webp)

Nüüd saate seda kasutada bitcoinide vastuvõtmiseks. Kui tehing edastatakse võrgus, ilmub see ka Envoy's. Oodake, kuni olete saanud piisavalt kinnitusi, et pidada tehingut lõplikuks.

![Image](assets/fr/77.webp)

## Bitcoinide saatmine

Nüüd, kui teil on mõned satsid rahakotis, võite ka mõned saata. Selleks klõpsa nupule "*Saatmine*".

![Image](assets/fr/78.webp)

Sisestage saaja aadress kas otse või skannides QR-koodi oma nutitelefoni kaameraga.

![Image](assets/fr/79.webp)

Määrake summa, mida soovite saata, ja seejärel klõpsake "*Kinnitage*".

![Image](assets/fr/80.webp)

Valige tehingutasu vastavalt praegusele turuolukorrale, seejärel kontrollige tehinguandmeid. Kui kõik on õige, klõpsake nuppu "*Sign with Passport*".

![Image](assets/fr/81.webp)

Lisage oma tehingule silt, et selle eesmärk oleks selgelt kirjas.

![Image](assets/fr/82.webp)

Seejärel kuvab Envoy PSBT (*Partially Signed Bitcoin Transaction*). Rakendus on tehingu koostanud, kuid tal puuduvad veel allkiri(d), et avada sisendiks kasutatud bitcoinid. Neid allkirju saab teha ainult Passport, mis võõrustab teie seemne, andes juurdepääsu tehingu allkirjastamiseks vajalikele privaatvõtmetele.

![Image](assets/fr/83.webp)

Mine oma passis menüüsse "*Konto*" ja klõpsa "*allkirjastamine QR-koodiga*".

![Image](assets/fr/84.webp)

Skaneerige Envoy's kuvatavat PSBT (*Partially Signed Bitcoin Transaction*).

![Image](assets/fr/85.webp)

Kinnitage, et vastuvõtja aadress ja saadetud summa on õiged, seejärel vajutage kinnitamisnuppu.

![Image](assets/fr/86.webp)

Kontrollige vahetusaadressi. Minu näites ei ole ühtegi, sest tehing sisaldab ühte väljundit.

![Image](assets/fr/87.webp)

Veenduge, et tasu on teie valitud.

![Image](assets/fr/88.webp)

Kui kõik andmed on õiged, klõpsake tehingu allkirjastamiseks kinnituse nupule.

![Image](assets/fr/89.webp)

Teie pass näitab teie allkirjastatud tehingut QR-koodi kujul.

![Image](assets/fr/90.webp)

Klõpsake Envoy rakenduses QR-koodi ikoonil, seejärel skannige passi ekraanil kuvatavat PSBT-d.

![Image](assets/fr/91.webp)

Kontrollige veelkord oma tehingu üksikasju. Kui kõik on õige, vajutage "*Sendage tehing*", et edastada see Bitcoini võrgus.

![Image](assets/fr/92.webp)

Teie tehing ootab nüüd kinnitust. Saate jälgida selle staatust otse oma kontolt.

![Image](assets/fr/93.webp)

Palju õnne, te teate nüüd, kuidas seadistada ja kasutada passi koos Envoy rakendusega. Kui leidsite selle õpetuse kasulikuks, oleksin tänulik, kui jätaksite alla rohelise pöidla. Jagage seda artiklit julgelt oma suhtlusvõrgustikes. Täname jagamise eest!

Lisateavet leiate meie Liana tarkvara juhendmaterjalist:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
