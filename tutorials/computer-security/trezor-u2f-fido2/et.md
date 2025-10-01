---
name: "Trezor U2F & FIDO2"
description: Tugevdage oma veebiturvalisust Trezoriga
---
![cover](assets/cover.webp)



Trezori seadmed on riistvaralised rahakotid, mis on algselt mõeldud Bitcoin Wallet turvamiseks, kuid neil on ka täiustatud võimalused tugevaks autentimiseks veebis. Tänu nende ühilduvusele **U2F** ja **FIDO2** protokollidega võimaldavad nad teil tagada juurdepääsu oma veebikontodele, ilma et peaksite tuginema ainult paroolidele.



U2F (*Universal 2nd Factor*) protokolli tutvustasid Google ja Yubico 2014. aastal, seejärel standardiseeris FIDO Alliance. See võimaldab sisselogimisel lisada teise füüsilise autentimisteguri (2FA). Kui see on aktiveeritud, peavad kasutajad lisaks klassikalisele paroolile kinnitama iga kontoga ühendamise katse, vajutades oma Trezoril nuppu. Selles kontekstis töötab Trezor sarnaselt Yubikey'ga.



See meetod põhineb asümmeetrilisel krüptograafial: salajasi andmeid ei edastata, mis muudab andmepüügi- või pealtkuulamisrünnakud ebatõhusaks. U2F-i toetavad nüüd paljud veebiteenused.



Lisaks U2F-le, mis võimaldab kahefaktorilist autentimist, toetavad Trezorid ka FIDO2 (*Fast IDentity Online 2.0*), mis on U2F-i edasiarendus. See on 2018. aastast standardiseeritud autentimisprotokoll, mis laiendab U2F-i loogikat ja mille eesmärk on täielikult asendada paroolid. See põhineb kahel komponendil: *WebAuthn* (brauseri pool) ja *CTAP2* (füüsilise võtme pool). FIDO2 võimaldab "paroolita" autentimist: kasutajad tuvastavad end üksnes oma Trezor-seadme kaudu, mis toimib unikaalse krüptograafilise märgisena, ilma täiendava paroolita. See protokoll ühildub nüüd mitmete veebiteenustega, eelkõige ettevõtjatele suunatud teenustega.



Lisaks **paroolita** funktsioonile võimaldab FIDO2 ka kahefaktorilist autentimist sarnaselt U2F-iga.



FIDO2 võtab kasutusele ka residentide volituste mõiste, st otse Trezorisse salvestatud identifikaatorid, mis sisaldavad nii ühendust võimaldavat privaatvõtit kui ka kasutaja identifitseerimisandmeid. See mehhanism võimaldab tõeliselt paroolivaba autentimist: lihtsalt ühendage Trezor ja kinnitage juurdepääs, sisestamata ID-d või parooli. Seevastu tavalisemad mitteresidentaalsed volitused salvestavad seadmesse ainult isikliku võtme; kasutaja ID jääb serveri poolele ja tuleb seega iga ühenduse puhul sisestada. Vaatame hiljem, kuidas neid Trezoriga salvestada.



Selles õpetuses avastame, kuidas aktiveerida U2F või FIDO2 kahefaktorilise autentimise jaoks ning seejärel, kuidas FIDO2 seadistada, et pääseda oma kontodele ligi ilma paroolita otse Trezori abil.



**Märkus:** U2F ühildub kõigi Trezori mudelitega, kuid FIDO2 on toetatud ainult mudelitel Safe 3, Safe 5 ja Model T, mitte Model One.



## U2F/FIDO2 kasutamine 2FA jaoks Trezoril



Enne alustamist veenduge, et olete oma Bitcoin Wallet seadistanud oma Trezoril. Oluline on salvestada oma Mnemonic õigesti, sest U2F ja FIDO2 võtmed, mida kasutatakse kahefaktorilise autentimise puhul, on tuletatud sellest Mnemonic-st. Kui teie Trezor on kadunud või kahjustatud, saate taastada juurdepääsu oma võtmetele, sisestades oma Mnemonic fraasi mõnes teises Trezori seadmes (pange tähele, et FIDO2-volituste jaoks režiimis "*sõnavaba*" ei piisa ainult seed-st, nagu me näeme järgmistes punktides).



Ühendage oma Trezor arvutiga ja avage see.



![Image](assets/fr/01.webp)



Juurdepääs kontole, mida soovite kaitsta kahefaktorilise autentimisega. Näiteks kasutan Bitwardeni kontot. Tavaliselt leiate 2FA valiku teenuse seadetest, vahekaartide "*autentimine*", "*turvalisus*", "*login*" või "*salasõna*" alt.



![Image](assets/fr/02.webp)



Valige kahefaktorilise autentimise sektsioonis valik "*Passkey*" (mõiste võib sõltuvalt kasutatavast saidist erineda).



![Image](assets/fr/03.webp)



Sageli palutakse teil oma praegust parooli kinnitada.



![Image](assets/fr/04.webp)



Andke oma turvavõtmele nimi, et see oleks hõlpsasti äratuntav, ja klõpsake seejärel nupule "*Luge võtit*".



![Image](assets/fr/05.webp)



Trezori ekraanile ilmuvad teie konto andmed. Kinnitamiseks puudutage ekraani või vajutage nuppu. Samuti palutakse teil kinnitada oma PIN-kood.



![Image](assets/fr/06.webp)



Registreerige see turvavõti.



![Image](assets/fr/07.webp)



Nüüdsest alates, kui soovite oma kontoga ühendust luua, palutakse teil lisaks tavapärasele paroolile ühendada ka teie Trezor.



![Image](assets/fr/08.webp)



Seejärel saate autentimise kinnitamiseks vajutada Trezori ekraanile.



![Image](assets/fr/09.webp)



Hardware Wallet Trezori kasutamise eelis kahefaktorilise autentimise puhul on see, et tänu Mnemonic fraasile saate oma võtmed hõlpsasti taastada. Lisaks sellele põhilisele varundusele saate kasutada ka iga teenuse, kus olete 2FA aktiveerinud, pakutavat hädaolukoodi. See hädaolukorra kood võimaldab teil oma kontoga ühendust võtta, kui kaotate oma turvavõti. Seega asendab see vajaduse korral 2FA ühenduse loomiseks.



Näiteks Bitwardenis saate sellele koodile ligi, kui klõpsate nupule "*View recovery code*".



![Image](assets/fr/10.webp)



Soovitan seda koodi hoida erinevas kohas, kus te säilitate oma põhiparooli, et vältida nende koos varastamist. Näiteks kui teie parool on salvestatud paroolihaldurisse, siis hoidke 2FA hädaolukorra koodi eraldi paberil.



See lähenemisviis pakub teile 2FA-autentimise Trezori kadumise korral kahetasandilist varukoopiat: esimene varukoopia, milles kasutatakse Mnemonic fraasi kõigi teie kontode jaoks, ja teine varukoopia, mis on mõeldud iga konto jaoks eraldi hädaolukorra koodidega. Siiski on oluline **ei segi ajada Mnemonic rolli hädaabikoodiga**:




- 12- või 24-sõnaline Mnemonic fraas annab teile juurdepääsu mitte ainult kõigi teie kontode 2FA jaoks kasutatavatele võtmetele, vaid ka teie Trezoriga kaitstud bitcoinidele;
- Hädaolukorra kood võimaldab teil ajutiselt 2FA taotlusest mööda minna ainult asjaomasel kontol (antud näites ainult Bitwardenis).



## FIDO2 kasutamine Trezoril



Lisaks kahefaktorilisele autentimisele võimaldab FIDO2 ka "paroolita" autentimist, st ilma salasõna sisestamiseta veebilehele sisselogimisel. Lihtsalt ühendage oma Trezor oma arvutiga, et sel viisil oma turvalisele kontole ligi pääseda. Selle funktsiooni seadistamine toimub järgmiselt.



Enne alustamist veenduge, et olete oma Bitcoin Wallet seadistanud oma Trezoril. Oluline on salvestada Mnemonic, sest FIDO2 "*sõnavabad*" identifikaatorid on teie seed-ga krüpteeritud (kuidas neid identifikaatoreid õigesti salvestada, selgub järgmises jaotises).



Ühendage Trezor arvutiga ja avage see.



![Image](assets/fr/01.webp)



Juurdepääs kontole, mida soovite turvata, on režiimis "*sõnavaba*". Kasutan näitena Bitwardeni kontot. Selle valiku leiab tavaliselt teenuse seadetest, sageli vahekaardilt "*autentimine*", "*turvalisus*" või "*salasõna*".



Näiteks Bitwardenis on see võimalus leitav vahekaardilt "*Master password*". FIDO2 kaudu autentimise aktiveerimiseks klõpsake nupule "*Turn on*".



![Image](assets/fr/11.webp)



Sageli palutakse teil oma salasõna kinnitada.



![Image](assets/fr/12.webp)



Trezori ekraanile ilmuvad teie konto andmed. Kinnitamiseks puudutage ekraani või vajutage nuppu. Samuti peate kinnitama oma PIN-koodi.



![Image](assets/fr/13.webp)



Saidil lisage nimi, et mäletada oma turvavõti, seejärel klõpsake "*Välja lülitada*".



![Image](assets/fr/14.webp)



Seejärel palutakse teil end identifitseerida, et kontrollida, kas võti töötab korralikult.



![Image](assets/fr/15.webp)



Nüüdsest alates ei ole teie kontole sisselogimisel enam vaja sisestada oma e-posti Address või sisselogimist. Vajutage lihtsalt nupule, et autentida end füüsilise võtmega sisselogimisvormil.



![Image](assets/fr/16.webp)



Kinnitage ühendus Trezoriga, sisestades Hardware Wallet PIN-koodi.



![Image](assets/fr/17.webp)



Teid ühendatakse teie kontoga ilma parooli sisestamata.



![Image](assets/fr/18.webp)



**Pöörake tähelepanu sellele, et isegi kui te aktiveerite FIDO2 kaudu oma Trezoril "*sõnavaba*" autentimise, kehtib sisselogimiseks ikkagi teie veebikonto põhiparool**



## Salvestage oma FIDO2-volitused (volituste elanikud)



Kui kasutate FIDO2 või U2F kahefaktorilise autentimise jaoks, st et logida sisse kontodele, mis nõuavad lisaks 2FA valideerimisele Trezori kaudu ka parooli, siis ainult Mnemonic fraasiga saate juurdepääsu oma võtmetele. Kui aga kasutate FIDO2-d "*sõnavaba*" režiimis, nagu on kirjeldatud eelmises jaotises, on vaja lisaks Mnemonic fraasi varundamisele, mis krüpteerib need volitused, teha koopia oma FIDO-volitustest.



Selleks on vaja arvutit, millele on paigaldatud Python. Avage terminal ja käivitage järgmine käsk, et paigaldada vajalik Trezori tarkvara:



```shell
pip3 install --upgrade trezor
```



Ühendage oma Trezor USB kaudu arvutiga ja avage see PIN-koodi abil.



![Image](assets/fr/01.webp)



Trezorisse salvestatud FIDO2-tunnuste loendi saamiseks käivitage järgmine käsk:



```shell
trezorctl fido credentials list
```



Kinnitage eksport oma Trezoril.



![Image](assets/fr/19.webp)



Teie FIDO2 sisselogimise andmed kuvatakse teie terminalis. Näiteks minu Bitwardeni konto puhul sain järgmised andmed:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopeeri ja salvesta kogu see teave tekstifaili. Selle varundamisega ei kaasne mingeid olulisi riske, välja arvatud see, et te kasutate neid teenuseid koos FIDO2-ga. "*Credential ID*" on krüpteeritud teie Wallet seed abil, mis tähendab, et ründaja, kes saab selle varukoopia, ei saaks teie kontodega ühendust, vaid märkaks ainult, et te kasutate neid kontosid. Nende ID-de dekrüpteerimiseks on vaja seed teie Wallet-s.



Seetõttu võite luua sellest tekstifailist mitu koopiat ja salvestada need eri kohtadesse, näiteks lokaalselt arvutisse, failihostingteenusesse ja välisele andmekandjale, näiteks USB-mälupulgale. Pidage aga meeles, et see varukoopia ei uuene automaatselt, seega peate seda uuendama iga kord, kui te oma Trezoriga uue "*sõnavaba*" ühenduse sisse seate.



Kujutame nüüd ette, et olete oma Trezori ära rikkunud. FIDO2-volituste taastamiseks peate kõigepealt taastama oma Wallet, kasutades oma Mnemonic fraasi uues FIDO2-ühilduvas Trezori seadmes.



Kui taastamine on lõpule viidud, käivitage oma FIDO2-tunnuste importimiseks uude seadmesse järgmine käsk terminalis:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Lihtsalt asendage `<CREDENTIAL_ID>` ühe oma identifikaatoriga. Näiteks minu puhul annaks see:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor palub teil importida oma FIDO2-tunnus. Kinnitage, vajutades ekraanil.



![Image](assets/fr/20.webp)



Teie FIDO2-sisselogimine on nüüd Trezoril töökorras. Korrake seda protseduuri kõigi oma identifikaatorite puhul.



Palju õnne, nüüd oled oma Trezori U2F ja FIDO2 kasutamisega kursis! Kui see õpetus oli teile kasulik, oleksin väga tänulik, kui jätaksite allpool Green pöidla. Palun jagage seda õpetust julgelt oma suhtlusvõrgustikes. Tänan teid väga!



Soovitan ka seda teist õpetust, kus me vaatame teist lahendust U2F ja FIDO2 autentimiseks:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e