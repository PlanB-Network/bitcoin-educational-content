---
name: YubiKey 2FA
description: Kuidas kasutada füüsilist turvavõtit?
---
![kaas](assets/cover.webp)

Tänapäeval on kahefaktoriline autentimine (2FA) muutunud hädavajalikuks online-kontode turvalisuse tõstmiseks volitamata juurdepääsu eest. Küberrünnakute sagenemisega on mõnikord ainult paroolist kontode kaitsmiseks ebapiisav.

2FA tutvustab lisaturvalisuse kihti, nõudes traditsioonilisele paroolile lisaks teist autentimise vormi. See kinnitamine võib võtta erinevaid vorme, nagu kood, mis saadetakse SMS-i teel, dünaamiline kood, mille genereerib spetsiaalne rakendus, või füüsilise turvavõtme kasutamine. 2FA kasutamine vähendab oluliselt teie kontode kompromiteerimise riske, isegi kui teie parool varastatakse.

Teises õpetuses selgitasin, kuidas seadistada ja kasutada TOTP 2FA rakendust:

https://planb.network/tutorials/others/authy

Siin vaatame, kuidas kasutada füüsilist turvavõtit kõigi teie kontode teise autentimisfaktorina.

## Mis on füüsiline turvavõti?

Füüsiline turvavõti on seade, mida kasutatakse teie online-kontode turvalisuse tõstmiseks kahefaktorilise autentimise (2FA) kaudu. Need seadmed meenutavad sageli väikeseid USB-võtmeid, mis tuleb sisestada arvuti porti, et kinnitada, et ühendust üritav isik on tõepoolest õigustatud kasutaja.
![TURVAVÕTI 2FA](assets/notext/01.webp)
Kui logite sisse 2FA-ga kaitstud kontole ja kasutate füüsilist turvavõtit, peate sisestama mitte ainult oma tavalise parooli, vaid ka sisestama füüsilise turvavõtme oma arvutisse ja vajutama nuppu autentimise kinnitamiseks. See meetod lisab lisaturvalisuse kihi, sest isegi kui keegi suudab teie parooli hankida, ei saa nad ilma füüsilist võtit omamata teie kontole juurde pääseda.

Füüsiline turvavõti on eriti tõhus, kuna see ühendab kahte erinevat autentimisfaktorit: teadmiste tõend (parool) ja valdamise tõend (füüsiline võti).

Siiski on sellel 2FA meetodil ka puudusi. Esiteks peate alati omama turvavõtit, kui soovite oma kontodele juurde pääseda. Võite vajada selle lisamist oma võtmehoidjale. Teiseks, erinevalt teistest 2FA meetoditest, kaasneb füüsilise turvavõtme kasutamisega esialgne kulu, kuna peate väikese seadme ostma. Turvavõtmete hinnad varieeruvad üldiselt vahemikus 30 kuni 100 eurot, sõltuvalt valitud omadustest.

## Millist füüsilist turvavõtit valida?

Turvavõtme valimisel tuleb arvesse võtta mitmeid kriteeriume.
Eelkõige peate kontrollima seadme poolt toetatud protokolle. Minimaalselt soovitan valida võtme, mis toetab OTP, FIDO2 ja U2F protokolle. Need üksikasjad on tavaliselt tootjate poolt tootekirjeldustes esile tõstetud. Iga võtme ühilduvuse kontrollimiseks võite külastada ka [dongleauth.com](https://www.dongleauth.com/dongles/).
Veenduge ka, et võti ühildub teie operatsioonisüsteemiga, kuigi tuntud brändid nagu Yubikey toetavad üldiselt kõiki laialdaselt kasutatavaid süsteeme.

Peaksite valima võtme ka sõltuvalt teie arvuti või nutitelefoni saadaolevatest portidest. Näiteks, kui teie arvutil on ainult USB-C pordid, valige võti USB-C ühendusega. Mõned võtmed pakuvad ka ühendusvõimalusi Bluetoothi või NFC kaudu.
![TURVAVÕTI 2FA](assets/notext/02.webp)
Võite võrrelda seadmeid ka nende lisafunktsioonide põhjal, nagu vee- ja tolmukindlus, samuti võtme kuju ja suurus.
Turvalisuse võtmemarkide osas on Yubico kõige tuntum oma [YubiKey seadmetega](https://www.yubico.com/), mida ma isiklikult kasutan ja soovitan. Google pakub samuti seadet nimega [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Avatud lähtekoodiga alternatiividest on huvitavad valikud [SoloKeys](https://solokeys.com/) (mitte OTP) ja [NitroKey](https://www.nitrokey.com/products/nitrokeys), kuid mul pole kunagi olnud võimalust neid testida.
## Kuidas kasutada füüsilist turvavõtit?

Kui olete oma turvavõtme kätte saanud, ei ole vaja teha mingit spetsiifilist seadistust. Võti on tavaliselt kasutusvalmis kohe peale kättesaamist. Saate seda kohe kasutada oma veebikontode turvamiseks, mis toetavad seda tüüpi autentimist. Näiteks näitan teile, kuidas turvata oma Protoni meilikontot selle füüsilise turvavõtmega.
![TURVAVÕTI 2FA](assets/notext/03.webp)
Leiate võimaluse aktiveerida 2FA oma konto seadetes, tihti "*Parooli*" või "*Turvalisuse*" jaotise all. Klõpsake märkeruudul või nupul, mis võimaldab teil aktiveerida 2FA füüsilise võtmega.
![TURVAVÕTI 2FA](assets/notext/04.webp)
Ühendage oma võti arvutiga.
![TURVAVÕTI 2FA](assets/notext/05.webp)
Puudutage oma turvavõtme nuppu, et kinnitada.
![TURVAVÕTI 2FA](assets/notext/06.webp)
Sisestage nimi, et mäletada, millist võtit kasutasite.
![TURVAVÕTI 2FA](assets/notext/07.webp)
Ja ongi kõik, teie turvavõti on edukalt lisatud teie konto 2FA autentimiseks.
![TURVAVÕTI 2FA](assets/notext/08.webp)
Minu näites, kui proovin uuesti ühenduda oma Protoni meilikontoga, palutakse mul esmalt sisestada oma parool koos kasutajanimega. See on esimene autentimise faktor.
![TURVAVÕTI 2FA](assets/notext/09.webp)
Seejärel palutakse mul ühendada oma turvavõti teise autentimise faktori jaoks.
![TURVAVÕTI 2FA](assets/notext/10.webp)
Järgmisena pean puudutama füüsilise võtme nuppu, et kinnitada autentimist, ja olen taasühendatud oma Protoni meilikontoga.
![TURVAVÕTI 2FA](assets/notext/11.webp)
Korrake seda toimingut kõigi veebikontode jaoks, mida soovite sel viisil turvata, eriti kriitiliste kontode puhul nagu teie meilikontod, paroolihaldurid, pilve- ja veebisalvestusteenused või teie finantskontod.