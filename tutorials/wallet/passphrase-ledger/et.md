---
name: BIP39 Paroolilausete Ledger
description: Kuidas lisada paroolilauset oma Ledger rahakotti?
---
![kaas](assets/cover.webp)

BIP39 paroolilause on valikuline parool, mis koos sinu mnemoonilise fraasiga kasutades, pakub lisakaitsekihti deterministlikele ja hierarhilistele Bitcoin rahakottidele. Selles õpetuses vaatame koos, kuidas seadistada paroolilauset oma turvalises Bitcoin rahakotis Ledgeril (sõltumata mudelist).

Enne selle õpetuse alustamist, kui sa pole tuttav paroolilause kontseptsiooniga, kuidas see töötab ja millised on selle tagajärjed sinu Bitcoin rahakotile, soovitan tungivalt konsulteerida selle teise teoreetilise artikliga, kus ma kõike selgitan:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Kuidas paroolilause Ledgeril toimib?

Ledger seadmetega on sul kaks erinevat võimalust paroolilause seadistamiseks oma rahakotil: "*PIN-koodiga seotud*" valik ja "*ajutine*" valik.

"*PIN-koodiga seotud*" valikuga seostad paroolilause teise PIN-koodiga oma Ledgeril. See tähendab, et sul on 2 PIN-koodi: üks tavapärase rahakoti juurdepääsuks ilma paroolilausega ja teine teise rahakoti juurdepääsuks, mis on kaitstud paroolilausega.

![PASSPHRASE BIP39](assets/notext/03.webp)

Põhimõtteliselt, isegi selle paroolilause valikuga, mis on seotud teise PIN-koodiga, jääb sinu paroolilause ikkagi sinu paroolilauseks. See tähendab, et kui kaotad oma Ledgeri ja soovid oma bitcoine taastada teisel seadmel või tarkvaral, on sul absoluutselt vaja oma 24-sõnalist fraasi ja sinu **täielikku paroolilauset**. Paroolilausega seotud PIN-koodi kasutatakse ainult sellele juurdepääsuks sinu praegusel Ledgeril, kuid see ei tööta teistel Ledgeritel või muul tarkvaral. Seetõttu on oluline oma paroolilause täielikult füüsilisel kandjal varundada. **Teise PIN-koodi teadmine üksi ei ole piisav, et taastada juurdepääs sinu rahakotile**; see on lihtsalt mugavusfunktsioon sinu Ledgeril.

See teine PIN-koodi valik on eriti huvitav füüsiliste rünnakute korral. Näiteks, kui ründaja sunnib sind oma seadet avama, et varastada sinu vahendeid, saad kasutada esimest PIN-koodi, et pääseda ligi petterahakotile, mis sisaldab väikest kogust bitcoine, hoides samal ajal oma peamisi vahendeid turvaliselt teise PIN-koodi taga.

Lisaks pakub see valik kõiki BIP39 paroolilause turvaeeliseid ilma vajaduseta seda iga kord käsitsi sisestada, kui kasutad oma allkirjastamisseadet. See võimaldab kasutada pikka ja juhuslikku paroolilauset, tugevdades kaitset jõuga murdmise rünnakute vastu, samal ajal vältides raskust seda iga kord seadme väikeste nuppudega käsitsi sisestada.
"Ajutise paroolilause" valik ei salvesta paroolilauset seadmesse. Iga kord, kui soovid oma kaitstud rahakotile juurde pääseda, pead paroolilause Ledgeril käsitsi sisestama. See muudab kasutamise tülikamaks, kuid suurendab ka turvalisust, jättes seadmesse paroolilausest jälge. Niipea, kui seade välja lülitad, naaseb see oma vaikeseisundisse ja nõuab peidetud kontodele juurdepääsuks täieliku paroolilause uut sisestamist. See "ajutise paroolilause" valik on seega sarnane teiste riistvaraliste rahakottide toimimisega.
Selles õpetuses kasutan näitena Ledger Flexi. Kui kasutad aga mõnda teist Ledgeri mudelit, jääb protsess samaks. Ledger Staxi puhul on liides sama, mis Ledger Flexil. Nano S, Nano S Plus ja Nano X mudelite puhul, kuigi liides on erinev, jääb protsess ja menüüde nimed samaks.
**Tähelepanu:** Kui olete juba enne paroolilause aktiveerimist oma Ledgerisse bitcoine saanud, peate need üle kandma Bitcoin'i tehingu kaudu. Paroolilause genereerib uue võtmete komplekti, luues seeläbi rahakoti, mis on täiesti sõltumatu teie esialgsest rahakotist. Paroolilause lisamisel saate uue rahakoti, mis on tühi. See aga ei kustuta teie esimest paroolilausega rahakotti. Saate sellele endiselt juurde pääseda, kas otse oma Ledgeri kaudu ilma paroolilause sisestamata või kasutades mõnda muud tarkvara koos oma 24-sõnalise fraasiga.
Enne selle õpetuse alustamist veenduge, et olete oma Ledgeri juba seadistanud ja genereerinud oma mnemoonilise fraasi. Kui see pole nii ja teie Ledger on uus, järgige oma mudeli jaoks saadaolevat spetsiifilist õpetust PlanB võrgustikus. Kui see samm on lõpetatud, võite naasta selle õpetuse juurde.

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4
https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Kuidas seadistada ajutist paroolilause Ledgeris?

Oma Ledgeri avalehel klõpsake seadete hammasratta ikoonil.

![PASSPHRASE BIP39](assets/notext/04.webp)

Valige "Advanced" menüü, seejärel "Set passphrase".

![PASSPHRASE BIP39](assets/notext/05.webp)

See on samm, kus saate valida "linked to PIN" võimaluse või "temporary" võimaluse, millest rääkisime eelmises osas. Siin selgitan, kuidas seadistada ajutist paroolilause, nii et klõpsake "Set temporary passphrase".

![PASSPHRASE BIP39](assets/notext/06.webp)
Seejärel palutakse teil sisestada oma paroolilause. Valige tugev paroolilause ja tehke kohe füüsiline varukoopia, näiteks paberil või metallil. Selles näites valisin paroolilause: `fH3&kL@9mP#2sD5qR!82`. Pärast oma paroolilause sisestamist klõpsake nupul "*Continue*".
![PASSPHRASE BIP39](assets/notext/07.webp)

Kontrollige, et teie paroolilause vastab sellele, mida olete oma füüsilisel varukoopial märkinud, seejärel klõpsake nupul "*Yes, it's correct*", et kinnitada.

![PASSPHRASE BIP39](assets/notext/08.webp)

Oma paroolilause loomise lõpuleviimiseks sisestage oma Ledgeri PIN-kood. Edaspidi, kui soovite oma Ledgeris paroolilausega rahakotile juurde pääseda, peate järgima täpselt samu samme, nagu siin kirjeldatud.

![PASSPHRASE BIP39](assets/notext/09.webp)

Nüüd saate oma avalike võtmete komplekti importida Sparrow Wallet'isse, et hallata oma rahakotti. Sparrow'is vastab see erinevale rahakotile teie esialgsest paroolilausega rahakotist.

Avage Sparrow Wallet. Veenduge, et tarkvara on ühendatud sõlmega, seejärel klõpsake vahekaardil "*File*" ja valige "*New Wallet*".

![PASSPHRASE BIP39](assets/notext/10.webp)

Valige oma paroolilausega kaitstud rahakotile nimi. Selleks näiteks valisin nime, mis sisaldab selgelt terminit "*passphrase*". Kui eelistate aga oma arvutis selle rahakoti diskreetsust säilitada, võite valida vähem ilmeka nime.

![PASSPHRASE BIP39](assets/notext/11.webp)

Valige oma rahakoti jaoks skripti tüüp. Soovitan valida "*Taproot*" või alternatiivina "*Native SegWit*".

![PASSPHRASE BIP39](assets/notext/12.webp)
Ühendage oma Ledger arvutiga ja seejärel klõpsake nupul "*Connected Hardware Wallet*". Veenduge, et olete oma Ledgeris juba sisestanud oma paroolilause. Kui ei, siis palun minge tagasi eelmistesse sammudesse, et sisestada oma paroolilause. Enne skaneerimisele jätkamist pidage meeles ka avada oma Ledgeris "*Bitcoin*" rakendus.
![PASSPHRASE BIP39](assets/notext/13.webp)

Klõpsake nupul "*Scan...*".

![PASSPHRASE BIP39](assets/notext/14.webp)

Klõpsake oma Ledgeri kõrval nupul "*Import Keystore*".

![PASSPHRASE BIP39](assets/notext/15.webp)

Teie paroolilausega kaitstud rahakott on nüüd Sparrow's loodud. Kinnitamiseks klõpsake nupul "*Apply*".

![PASSPHRASE BIP39](assets/notext/16.webp)
Valige tugev parool, et tagada juurdepääsu turvalisus Sparrow Wallet'ile. See parool tagab teie rahakoti andmetele Sparrow's juurdepääsu turvalisuse, mis aitab kaitsta teie avalikke võtmeid, aadresse, silte ja tehingute ajalugu igasuguse volitamata juurdepääsu eest.
Soovitan teil see parool salvestada paroolihaldurisse, et te seda ei unustaks.

![PASSPHRASE BIP39](assets/notext/17.webp)

Ja ongi kõik, teie rahakott on nüüd loodud! "*Settings*" menüüs pakub Sparrow teile teie "*Master fingerprint*". See esindab teie peamise võtme sõrmejälge, mida kasutatakse teie rahakoti tuletamise alusena. Soovitan tungivalt hoida sellest sõrmejäljest koopiat. Minu näites vastab see: `281ee33a`.

![PASSPHRASE BIP39](assets/notext/18.webp)

Pidage meeles, mida mainisime eelmistes osades: viga, isegi väike, teie paroolilause sisestamisel genereerib täiesti uue rahakoti erinevate võtmetega. Iga kord, kui peate veenduma, et pääsete õige rahakoti juurde õige paroolilausega, kontrollige, et teie peamise võtme sõrmejälg vastab sellele, mille te üles märkisite. See teave iseenesest ei kujuta ohtu teie vahendite turvalisusele ega teie privaatsusele.

Enne oma paroolilausega rahakoti kasutamist soovitan tungivalt teha kuiva taastamise testi. Märkige üles viiteteave nagu teie xpub või teie peamise võtme sõrmejälg, seejärel lähtestage oma Ledger, kui rahakott on veel tühi. Seejärel proovige oma Ledgeris rahakotti taastada, kasutades oma 24-sõnalise fraasi ja paroolilause paberkoopiaid. Kontrollige, et taastamise järel genereeritud teave vastab sellele, mida algselt märkisite. Kui see nii on, võite olla kindel, et teie paberkoopiad on usaldusväärsed.

## Kuidas seadistada paroolilauset, mis on seotud PIN-koodiga Ledgeris?

Ledgeri avalehel klõpsake seadete hammasratta ikoonil.

![PASSPHRASE BIP39](assets/notext/19.webp)

Valige menüü "*Advanced*", seejärel "*Set passphrase*".

![PASSPHRASE BIP39](assets/notext/20.webp)

See on samm, kus saate valida "*linked to PIN*" või "*temporary*" valiku vahel, millest rääkisime eelmises osas. Siin selgitan, kuidas seadistada paroolilauset, mis on seotud uue PIN-koodiga, nii et klõpsake "*Set passphrase and attach it to a new PIN*".

![PASSPHRASE BIP39](assets/notext/21.webp)
Seejärel peate valima PIN-koodi, mis seostatakse teie paroolilausega. Nagu peamise PIN-koodi puhul, soovitatakse valida võimalikult juhuslik 8-kohaline PIN-kood. Samuti veenduge, et salvestate selle koodi erinevasse kohta, kus teie Ledger Flex hoitakse.
Minu puhul on peamine PIN-kood `58293647` ja valisin fraasiga seotud teisejärguliseks PIN-koodiks `71425839`.

Teilt palutakse seejärel sisestada oma fraas. Valige tugev fraas ja jätkake kohe füüsilise varukoopia tegemisega, kasutades selleks näiteks paberit või metalli. Selles näites valisin fraasi: `fH3&kL@9mP#2sD5qR!82`. Pärast fraasi sisestamist klõpsake nupul "*Jätka*".

Kontrollige, et teie fraas ühtib teie füüsilisel varukoopial märgituga, seejärel klõpsake kinnitamiseks nupul "*Jah, see on õige*".

Fraasi loomise lõpuleviimiseks sisestage oma Ledgeri peamine PIN-kood (mitte see, mis on seotud fraasiga).

Edaspidi, kui soovite oma rahakotile Ledgeris fraasiga juurde pääseda, peate sisestama mitte peamise PIN-koodi, vaid teisejärgulise PIN-koodi:
- Peamine PIN-kood (`58293647`) > rahakott ilma fraasita.
- Teisejärguline PIN-kood (`71425839`) > rahakott fraasiga.

Nüüd saate oma avalike võtmete komplekti importida Sparrow Walletisse, et hallata oma rahakotti. Sparrow's vastab see erinevale rahakotile võrreldes teie esialgse fraasita rahakotiga.

Avage Sparrow Wallet. Veenduge, et tarkvara on ühendatud sõlmega, seejärel klõpsake vahekaardil "*Fail*" ja valige "*Uus rahakott*".

Valige oma fraasiga kaitstud rahakotile nimi. Selles näites valisin nime, mis sisaldab sõnaselgelt terminit "*fraas*". Kui eelistate aga selle rahakoti diskreetsust oma arvutis säilitada, võite valida vähem ilmeka nime.

Valige oma rahakoti jaoks skripti tüüp. Soovitan valida "*Taproot*" või kui see pole võimalik, siis "*Native SegWit*".

Ühendage oma Ledger arvutiga, seejärel klõpsake nupul "*Ühendatud riistvararahakott*". Veenduge, et teie Ledgeris on juba teie fraas, avades selle teisejärgulise PIN-koodiga. Kui mitte, taaskäivitage oma Ledger ja sisestage fraasiga seotud PIN-kood. Enne skaneerimisele jätkamist pidage meeles avada ka oma Ledgeris "*Bitcoin*" rakendus.

Klõpsake nupul "*Skaneeri...*".

Klõpsake nupul "*Impordi Keystore*".

Teie fraasiga kaitstud rahakott on nüüd Sparrow's loodud. Kinnitamiseks klõpsake nupul "*Rakenda*".

Valige Sparrow Walleti juurdepääsu turvamiseks tugev parool. See parool tagab teie rahakoti andmetele Sparrow's juurdepääsu turvalisuse, aidates kaitsta teie avalikke võtmeid, aadresse, silte ja tehingute ajalugu igasuguse volitamata juurdepääsu eest.

Soovitan salvestada selle parooli paroolihaldurisse, et te seda ei unustaks.
![PASSPHRASE BIP39](assets/notext/33.webp)
Ja ongi tehtud, teie rahakott on nüüd loodud! "*Seadete*" menüüs annab Sparrow teile teie "*Master fingerprint*". See esindab teie peamise võtme sõrmejälge, mida kasutatakse teie rahakoti tuletamise alusena. Ma soovitan tungivalt sellest sõrmejäljest koopia teha. Minu näites vastab see: `281ee33a`.

![PASSPHRASE BIP39](assets/notext/34.webp)

Mäletage, mida me eelmistes osades mainisime: viga, isegi väike, teie paroolifraasi sisestamisel genereerib täiesti uue rahakoti erinevate võtmetega. Iga kord, kui on vaja tagada õige rahakoti juurdepääs õige paroolifraasiga, kontrollige, et teie peamise võtme sõrmejälg ühtib märkmetes olevaga. See teave iseenesest ei kujuta ohtu teie vahendite turvalisusele ega teie privaatsusele.
Enne oma rahakoti kasutamist paroolifraasiga, soovitan tungivalt teha kuiva proovitaastamise testi. Märkige üles viiteteave, nagu teie xpub või teie peamise võtme sõrmejälg, seejärel lähtestage oma Ledger, kui rahakott on veel tühi. Seejärel proovige oma rahakotti Ledgeris taastada, kasutades teie 24-sõnalise fraasi ja paroolifraasi paberkoopiaid. Kontrollige, et taastamise järel genereeritud teave ühtib algsega. Kui see nii on, võite olla kindel, et teie paberkoopiad on usaldusväärsed.

Palju õnne, teie Bitcoin'i rahakott on nüüd paroolifraasiga kaitstud! Kui leidsite selle õpetuse kasuliku, oleksin tänulik, kui jätaksite allpool pöidla üles. Julgelt jagage seda artiklit oma sotsiaalvõrgustikes. Suur tänu!

Soovitan teil samuti tutvuda selle teise põhjaliku õpetusega, kuidas kasutada oma Ledger Flexi:

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a