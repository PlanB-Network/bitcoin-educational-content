---
name: Bitcoin Keeper
description: Bitcoin mobiilne wallet turvalisuse tagamiseks ja multi-sig
---

![cover](assets/cover.webp)



Bitcoinide turvaline haldamine kujutab endast suurt väljakutset igale omanikule, kes on teadlik finantssuveräänsuse panustest. Mobiilse wallet lihtsuse ja multi-sig lahenduse töökindluse vahel võib paljude kasutajate jaoks tunduda hirmutav tehniline lõhe. Bitcoin Keeper on paigutatud just sellele ristumiskohale, pakkudes progressiivset lähenemist turvalisusele, mis kaasab kasutajaid nende arengus.



Bitcoin Keeper on avatud lähtekoodiga mobiilirakendus, mis on pühendatud ainult Bitcoin-le ja mille on välja töötanud BitHyve meeskond. Selle eesmärk on muuta edasijõudnud portfellihaldus kättesaadavaks, eriti mitme allkirjaga konfiguratsioonid, säilitades samas intuitiivse kasutajaliidese algajatele. Rakendus võtab kasutusele loosungi "Secure today, Plan for tomorrow", mis peegeldab selle pikaajalise toetuse filosoofiat.



Erinevalt üldistest rahakottidest, mis haldavad mitmeid krüptovaluutasid, keskendub Bitcoin Keeper rangelt Bitcoin-le. Selline ainult bitcoinidele keskenduv lähenemisviis vähendab võimalikku ründepinda ja lihtsustab oluliselt kasutajakogemust. Rakendus paistab silma ka kõige levinumate riistvaraliste rahakottide emakeelse integreerimise ja UTXO täiustatud haldusfunktsioonide poolest.



## Mis on Bitcoin Keeper?



### Filosoofia ja eesmärgid



Bitcoin Keeper on loodud nende bitcoin'i kasutajate erivajaduste rahuldamiseks, kes soovivad säilitada täieliku kontrolli oma privaatvõtmete üle. Projekt hõlmab täielikult Bitcoin aluspõhimõtteid: avatud ja kontrollitav lähtekood, eraelu puutumatuse austamine ja kasutaja suveräänsus. Rakenduse kasutamiseks ei ole vaja registreerimist ega isiklikke andmeid ning see võib allkirjastamistoimingute tegemiseks töötada isegi võrguühenduseta.



Keskne eesmärk on pakkuda paindlikku ja tulevikukindlat vahendit BTC säilitamiseks mitme aasta ja isegi mitme põlvkonna jooksul tänu pärimisfunktsioonidele. Rakendus võimaldab kasutajatel alustada lihtsalt mobiilse wallet-ga ja seejärel järk-järgult areneda turvalisemate mitme allkirjaga lahenduste suunas.



### Rakenduse arhitektuur



Bitcoin Keeper korraldab fondide haldamist kahe erineva kontseptsiooni alusel. **Hot Wallet** on lihtne ühe klahviga wallet, mida hoitakse telefonis ja mis on mõeldud igapäevaste kulutuste ja tagasihoidlike summade jaoks. Vaults** on mitme allkirjaga (Multi-Key) seifid, mis nõuavad kulutuste autoriseerimiseks mitut võtit ja on mõeldud pikaajaliseks turvaliseks säilitamiseks.



### Peamised omadused



Bitcoin Keeper toetab peaaegu kõiki turul olevaid riistvaralisi rahakotte: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport ja Coinkite'i Tapsigner. Integreerimine toimub sõltuvalt seadmest erinevate meetodite kaudu: QR-koodi skaneerimine, NFC-ühendus või faili import.



Rakendus pakub ka täiustatud UTXO juhtimist koos tehingu märgistamisega, mündi kontrollimist, et saata sisendid käsitsi ja PSBT formaadi toetust osaliselt allkirjastatud tehingute jaoks.



## Paigaldamine ja esialgne seadistamine



Bitcoin Keeper on tasuta saadaval Androidis Google Play Store'i kaudu ja iOS-is App Store'i kaudu. Väljaandja on BitHyve. Enne installimist veenduge, et teie seade on pahavara vaba, ajakohane ja mitte juurdunud või jailbreakitud.



Esimesel käivitamisel palub rakendus teil luua turva-PIN-kood. See kood kaitseb juurdepääsu teie wallet-le ja krüpteerib tundlikud andmed lokaalselt. Valige tugev kood ja jätke see meelde. Seejärel saate kiiremaks avamiseks aktiveerida biomeetrilise autentimise (sõrmejälg või Face ID).



![Installation et configuration du PIN](assets/fr/01.webp)



Seejärel esitab rakendus mitu sissejuhatavat ekraani, kus selgitatakse selle kolme sammast: wallet loomine bitcoinide saatmiseks ja vastuvõtmiseks, võtmehaldus koos riistvara wallet ühilduvusega ning pärandite planeerimine bitcoinide edasiandmiseks. Vajutage "Get Started", seejärel valige "Start New", et luua uus konfiguratsioon.



![Écrans d'introduction](assets/fr/02.webp)



## Liidese avastamine



Bitcoin Keeper kasutajaliides on korraldatud nelja peamise vahekaardi ümber, mis on kättesaadavad alumisest navigatsiooniribast:



![Les quatre onglets de l'application](assets/fr/03.webp)



Vahekaardil **Pangakotid** kuvatakse teie rahakotid ja nende saldod. Siin saate juurdepääsu oma rahakottidele, et saata ja vastu võtta bitcoine. Sildid "Hot Wallet" ja "Single-Key" või "Multi-Key" võimaldavad teil kiiresti tuvastada iga wallet tüüpi.



Vahekaart **Keys** koondab allkirja võtmete haldamise. Siit leiate rakenduse poolt genereeritud mobiilivõtme, samuti kõik riistvaralistest rahakottidest imporditud võtmed. Siin saate lisada ka uusi allkirjastamisvahendeid.



Vahekaart **Concierge** pakub tugiteenuseid: esitage küsimusi tugimeeskonnale ja võtke ühendust Bitcoin nõustajatega, et saada personaalset abi.



Vahekaart **More** (Rohkem valikuid) annab juurdepääsu sellistele seadetele nagu isiklik serveriühendus, võtmete varundamine, päranddokumendid, kuvamise eelistused ja wallet haldamine.



## Ühendus oma serveriga



Konfidentsiaalsuse tugevdamiseks võimaldab Bitcoin Keeper teil ühendada rakenduse oma Electrum serveriga, mitte kasutada vaikimisi avalikke servereid.



![Configuration du serveur Electrum](assets/fr/04.webp)



Leidke vahekaardilt More (Rohkem) serveri seaded. Uue ühenduse seadistamiseks vajutage nuppu "Lisa server". Saate valida "Public Server" (eelkonfigureeritud avalikud serverid) ja "Private Electrum" (teie enda server) vahel.



Eraserveri puhul sisestage URL (nt umbrel.local Umbrel sõlme puhul) ja portnumber (tavaliselt 50001). Aktiveerige SSL, kui teie server seda toetab. Võite skannida ka konfiguratsiooni QR-koodi. Kui olete parameetrid sisestanud, vajutage "Connect to Server".



Kui teil ei ole veel oma Bitcoin sõlme, vaadake meie õpetust Umbrel kohta, mis on lihtne ja taskukohane viis oma sõlme keeramiseks:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Bitcoinide vastuvõtmine



Vahelehel Rahakotid valige wallet, kust soovite raha saada, vajutades seda. wallet ekraanil kuvatakse saldo ja kolm tegevusnuppu: Send Bitcoin, Receive Bitcoin ja View All Coins (Vaata kõiki münte).



![Réception de bitcoins](assets/fr/05.webp)



Vajutage nuppu "Receive Bitcoin". Bitcoin Keeper genereerib uue vastuvõtu aadressi Bech32 formaadis (alustades bc1...) koos selle QR-koodiga. Sellele aadressile saab lisada sildi, et identifitseerida vahendite allikas. Jagage aadressi saatjaga, kuvades QR-koodi või kopeerides tekstiaadressi.



Rakendus genereerib automaatselt uue aadressi iga vastuvõtu puhul, säilitades teie privaatsust. Vajaduse korral kasutage "Get New Address", et saada tühi aadress.



## UTXO juhtimine



Bitcoin Keeper pakub täielikku ülevaadet UTXO (kulutamata tehingu väljundid), mis moodustavad teie saldo. wallet ekraanil vajutage "View All Coins" (Vaata kõiki münte), et pääseda nurgahaldurisse.



![Gestion des UTXO](assets/fr/06.webp)



Ekraanil "Müntide haldamine" on iga UTXO eraldi loetletud koos selle summa ja sildiga. See vaade võimaldab teil jälgida oma müntide päritolu ja neid korrastada. Saate valida konkreetsed UTXOd "Select to Send" kaudu, et saata koos mündikontrolliga, vältides seega eri päritoluga müntide segunemist.



## Bitcoinide saatmine



Saatmiseks valige allikaportfell ja vajutage "Send Bitcoin". Sisestage sihtkoha aadress (kleebitud või skaneeritud QR-koodi abil) ja lisage soovi korral silt saaja identifitseerimiseks.



![Envoi de bitcoins](assets/fr/07.webp)



Järgmisel ekraanil saate sisestada saadetava summa. Kasutajaliides näitab teie olemasolevat saldot ja fiat-valuuta ümberarvestust. Valige tasustamise prioriteet: Madal (ökonoomne, ~60 minutit), Keskmine või Kõrge (prioriteet). Eeldatavad tasud sats/vabaidina kuvatakse reaalajas. Jätkamiseks vajutage nuppu "Saada".



![Confirmation et envoi](assets/fr/08.webp)



Kokkuvõtlik ekraan kuvab kõik üksikasjad: wallet allikas, sihtkoha aadress, tehingu prioriteet, võrgutasud, saadetud summa ja kogusumma. Palun kontrollige seda teavet hoolikalt, sest Bitcoin tehingud on pöördumatud. Tehingu saatmiseks vajutage "Confirm & Send".



Ilmub kinnitus "Saatmine õnnestus" koos täieliku kokkuvõttega. Tehing on nähtav ajaloost "Viimased tehingud" koos selle sildiga.



## Salvesta oma võtmed



Taastamisvõtme varundamine on kriitiline samm. Minge vahekaardil "More" jaotisse "Backup and Recovery" ja klõpsake "Recovery Key" (taastamisvõti).



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Ekraanil kuvatakse teie varukoopiate olek. Varukoopia kinnitamiseks palub rakendus teil kinnitada kindlat sõna teie fraasis (nt 7. sõna). See kinnitus tagab, et olete oma taastamisfraasi õigesti kirja pannud.



"Recovery Key Settings" (Taastamisvõtme seaded) kaudu saate vaadata oma täielikku fraasi "View Recovery Key" (Taastamisvõtme vaatamine) ja näha oma võtme allkirjastaja sõrmejälge. Hoidke oma 12-sõnalist fraasi paberil, turvalises kohas, niiskuse ja tule eest kaitstult. Ärge hoidke seda kunagi ühendatud seadmes.



## Välise võtme lisamine (wallet riistvara)



Üks Bitcoin Keeper peamisi eeliseid on riistvara rahakottide integreerimine. Vajutage vahekaardil Võtmed uue allkirjastamise seadme lisamiseks "Lisa võti".



![Ajout d'une clé hardware](assets/fr/10.webp)



Riistvara wallet ühendamiseks valige "Add key from a hardware". Rakendus toetab paljusid seadmeid: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ja Specter Solutions.



### Tapsigner konfiguratsioon



Tapsigner on Coinkite'i NFC-kaart, mis sobib eriti hästi mobiilseks kasutamiseks. Kui soovite rohkem teada saada, on meil spetsiaalne õpetus :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Tapsigner lisamiseks valige see riistvara rahakottide nimekirjast.



![Configuration du Tapsigner](assets/fr/11.webp)



Esmalt sisestage kaardi tagaküljele trükitud 6-32-kohaline PIN-kood (uute kaartide puhul vaikimisi) või oma PIN-kood, kui see on juba konfigureeritud. Vajutage "Proceed", seejärel viige oma Tapsigner telefoni tagaküljele, kui kuvatakse "Ready to scan". NFC-side impordib automaatselt avaliku võtme. Seejärel saate selle võtme identifitseerimiseks lisada kirjelduse (nt "Métro Card").



## Loo multisig portfell



Kui olete oma võtmed seadistanud, saate luua mitut seadet ühendava wallet mitme allkirjaga. Klõpsake vahekaardil "Rahakotid" nupule "Lisa Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Teil on kolm võimalust: "Loo Wallet" uue portfelli jaoks, "Impordi Wallet" olemasoleva wallet taastamiseks või "Koostöö Wallet" jagatud võlvkambrite jaoks. Valige "Create Wallet" ja seejärel "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Järgmine ekraan pakub erinevaid konfiguratsioone: "Ühe klahviga", "2 3-st mitme klahviga" või "3 5-st mitme klahviga". Kohandatud multi-sig jaoks vajutage "Select custom setup" (valige kohandatud seadistus). Valige näiteks "1 of 2": kahest võimalikust võtmest on nõutav üks allkiri.



Seejärel valige võtmed, mis moodustavad teie Vault'i. Meie näites kombineerime "Mobile Key" (telefoni tarkvaravõti) ja "TAPSIGNER" (Metro Card). Selline konfiguratsioon pakub redundantsust: kui üks võtmetest muutub kättesaamatuks, saate alati oma raha kulutada teise võtmega.



![Finalisation du wallet multisig](assets/fr/14.webp)



Nimetage oma wallet (nt "Test PlanB"), lisage valikuline kirjeldus ja kontrollige valitud võtmed. Vajutage nuppu "Create Your Wallet". Ilmub kinnitusteade "Wallet Created Successfully" (Wallet edukalt loodud), mis tuletab teile meelde, et salvestate wallet taastamisfaili.



Teie uus multisig wallet ilmub nüüd rahakoti vahekaardil sildiga "Multi-key" ja märkega "1 of 2".



### Konfigureerimisfaili salvestamine



** Erinevalt lihtsast wallet-st, kus taastamisfraasist piisab juurdepääsu taastamiseks, vajab wallet multisig, mis kirjeldab seifi struktuuri (millised võtmed osalevad, kui palju allkirju on vaja), ka konfiguratsioonifaili. Ilma selle failita ei saa te isegi kõigi taastamislausetega oma wallet uuesti üles ehitada.



![Export du fichier de configuration](assets/fr/15.webp)



Selle faili eksportimiseks valige oma wallet multisig rahakoti vahekaardil, seejärel vajutage üleval paremas nurgas olevale seadete ikoonile (hammasratas). Klõpsake jaotises "Wallet Settings" (Wallet seaded) nupule "Wallet configuration file" (Wallet konfiguratsioonifail). Saadaval on mitu ekspordivõimalust:





- Ekspordi PDF**: genereerib PDF-dokumendi, mis sisaldab kogu wallet teavet
- Näita QR**: kuvab skaneeritava QR-koodi konfiguratsiooni importimiseks teise seadmesse
- Airdrop / File Export**: ekspordib faili telefoni jagamisvõimaluste kaudu
- NFC**: jagamine NFC kaudu ühilduva seadmega



Hoidke seda konfiguratsioonifaili taastamislausetest eraldi, ideaaljuhul krüpteeritud või trükitud andmekandjal. Kui te kaotate oma telefoni, võimaldab see fail koos iga osaleva võtme taastamislausetega taastada wallet multisignaali Bitcoin Keeper või mõne muu ühilduva tarkvara abil.



## Parimad tavad



### Fondi korraldus



Struktureerige oma bitcoinid vastavalt nende kasutamisele: kuum wallet Single-Key jooksvate kulutuste jaoks piiratud summadega ja üks või mitu Vaults Multi-Key pikaajaliste säästude jaoks. Süstemaatiline UTXO märgistamine aitab teil jälgida, kust teie vahendid pärinevad, mis on eriti kasulik konfidentsiaalsuse haldamiseks ja eri päritolu müntide segamise vältimiseks.



Hoidke oma telefoni turvaliselt: aktiveerige biomeetriline lukk, tehke regulaarselt süsteemivärskendusi ja olge valvsad paigaldatud rakenduste suhtes. Ja hoidke Bitcoin Keeper turvaparandustega kursis.



### Varukoopia turvalisus



Hoidke vähemalt kaks koopiat igast taastamislausest paberil, mida hoitakse geograafiliselt eraldi paikades. Suurte summade puhul kaaluge graveeritud, katastroofikindlat metalli. Ärge säilitage neid fraase kunagi internetiga ühendatud seadmes ega pildistage neid kunagi.



multi-sig Vaultsi puhul salvestage ka konfiguratsioonifail (Wallet Recovery File), mis sisaldab osalevaid avalikke võtmeid ja võlvkambri struktuuri. See fail koos võtmete taastamise lausetega võimaldab wallet uuesti üles ehitada mis tahes ühilduvas tarkvaras, näiteks Sparrow või Specter.



## Eelised ja piirangud



### Tähtsündmused





- Ainult Bitcoin rakendus vähendab keerukust ja riski
- Multisig Vaults'i loomulik integratsioon koos samm-sammult juhiste andmisega
- Laiendatud riistvara wallet tugi (Tapsigner, Coldcard, Ledger, Jade jne)
- UTXO ja mündikontrolli täiustatud juhtimine
- Saab ühendada isikliku Electrum serveriga
- Avatud, auditeeritav lähtekood



### Piirangud, millega tuleb arvestada





- Interface peamiselt inglise keeles
- Mõned lisafunktsioonid (Cloud Backup, Assisted Server) nõuavad uuendamist
- Multisig konfiguratsioon nõuab algkoolitust



## Kokkuvõte



Bitcoin Keeper paistab skaleeritava lahendusena teie bitcoinide haldamiseks silma. Selle progressiivne lähenemine, alates lihtsast kuumast wallet-st kuni mitme allkirjaga võlvikuteni, tähendab, et turvalisust saab vastavalt vajaduste muutumisele täiustada. Võimalus hõlpsasti integreerida riistvara rahakotte, nagu Tapsigner, sillutab teed töökindlatele konfiguratsioonidele ilma liigse keerukuseta.



Ainult bitcoinidele keskendumine, avatud lähtekood ja eraelu puutumatuse austamine teevad sellest valiku, mis on kooskõlas Bitcoin ökosüsteemi põhiväärtustega.



See õpetus hõlmab Bitcoin Keeper põhifunktsioone selle tasuta versioonis. Rakendus pakub ka lisafunktsioone (Cloud Backup, Assisted Server Backup, Canary Wallets), mida käsitletakse eraldi õpetuses. Järgmises juhendis uurime ka pärimise planeerimise funktsiooni, mis võimaldab teil tänu rakendusse integreeritud täiustatud võlvidele ja kaasnevatele dokumentidele valmistada ette oma bitcoinide edastamist oma lähedastele.



## Ressursid





- Ametlik veebileht: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Abikeskus: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Allikakood: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)