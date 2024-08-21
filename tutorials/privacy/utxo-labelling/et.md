---
name: UTXO märgistamine
description: Kuidas korrektselt märgistada oma UTXOsid?
---
![cover](assets/cover.webp)

Selles õpetuses avastate kõik, mida peate teadma UTXOde märgistamise kohta oma Bitcoin rahakotis ja mündikontrolli kohta. Alustame teoreetilisest osast, et täielikult mõista neid kontseptsioone, enne kui liigume edasi praktilise osa juurde, kus uurime, kuidas konkreetsemalt kasutada silte peamises Bitcoin rahakotitarkvaras.

## Mis on UTXO märgistamine?
"Märgistamine" on tehnika, mis hõlmab konkreetse UTXOga Bitcoin rahakotis annotatsiooni või sildi seostamist. Need annotatsioonid salvestatakse kohalikult rahakotitarkvara poolt ja neid ei edastata kunagi Bitcoin võrgu kaudu. Märgistamine on seega isikliku halduse vahend.

Näiteks, kui ma saan UTXO P2P tehingu kaudu Bisqist Charlesilt, võiksin sellele määrata sildi `Bisq P2P ost Charles`.

Märgistamine võimaldab meenutada UTXO päritolu või kavandatud sihtkohta, mis lihtsustab fondide haldamist ja optimeerib kasutaja privaatsust. Märgistamine muutub veelgi olulisemaks, kui seda kombineerida "mündikontrolli" funktsionaalsusega. Mündikontroll on võimalus, mis on saadaval heades Bitcoin rahakottides, mis annab kasutajale võimaluse käsitsi valida, milliseid konkreetseid UTXOsid kasutatakse sisenditena tehingu loomisel.

Rahakoti kasutamine mündikontrolliga, koos UTXO märgistamisega, võimaldab kasutajatel täpselt eristada ja valida UTXOsid oma tehingute jaoks, vältides seeläbi UTXOde ühendamist erinevatest allikatest. See praktika vähendab riske, mis on seotud Common Input Ownership Heuristic (CIOH) ehk ühise sisendi omandi heuristikaga, mis viitab tehingu sisendite ühisele omandile, mis võib ohustada kasutaja privaatsust.

Tagasi minu KYC-vaba UTXO näite juurde Bisqist; ma tahan vältida selle ühendamist UTXOga, mis on pärit näiteks reguleeritud vahetusplatvormilt, mis teab minu identiteeti. Erinevate siltide paigutamisega minu KYC-vaba UTXOle ja minu KYC UTXOle, suudan ma kergesti tuvastada, millist UTXOt kasutada sisendina kulutuse rahuldamiseks, kasutades mündikontrolli funktsionaalsust.

## Kuidas korrektselt märgistada oma UTXO?
Universaalset UTXOde märgistamise meetodit, mis sobiks kõigile, ei ole olemas. Teie ülesanne on määratleda märgistamissüsteem, et saaksite oma rahakotis kergesti orienteeruda.
Üks oluline kriteerium märgistamisel on UTXO allikas. Peaksite lihtsalt näitama, kuidas see münt teie rahakotti jõudis. Kas see on vahetusplatvormilt? Kliendi poolt tasutud arve? Peer-to-peer vahetus? Või kas see esindab ostust üle jäänud vahetusraha? Seega, võiksite täpsustada:
- `Väljavõte Exchange.com`;
- `Makse Klient David`;
- `P2P Ost Charles`;
- `Vahetusraha diivani ostust`.
![labelling](assets/en/1.webp)
Oma UTXOde halduse täpsustamiseks ja oma rahakotis fondide eraldamise strateegiate järgimiseks, võiksite oma siltidele lisada täiendava indikaatori, mis peegeldab neid eraldusi. Kui teie rahakott sisaldab kahte UTXOde kategooriat, mida te ei soovi segada, võiksite oma siltidesse integreerida markeri, et need grupid selgelt eristada.

Need eraldusmarkerid sõltuvad teie enda kriteeriumidest, nagu eristamine KYC UTXO (teades teie identiteeti) ja KYC-vaba (anonüümne) vahel, või eristamine professionaalsete ja isiklike vahendite vahel. Võttes eespool mainitud sildi näiteid, võiks see tõlkida kui:
- `KYC - Väljavõte Exchange.com`;
- `KYC - Makse Klient David`;
- `KYC-VABA - P2P Ost Charles`;
- `KYC-VABA - Vahetusraha diivani ostust`.
![märgistamine](assets/en/2.webp)Igal juhul pidage meeles, et hea märgistamine on selline, mida saate mõista siis, kui seda vajate. Kui teie Bitcoin'i rahakott on peamiselt mõeldud säästudeks, võib juhtuda, et märgised on teile kasulikud alles mitme aastakümne pärast. Seetõttu veenduge, et need oleksid selged, täpsed ja kõikehõlmavad.

Samuti on soovitatav jätkata mündi märgistamist läbi tehingute. Näiteks tehes KYC-vaba UTXO konsolideerimist, veenduge, et märgistate tulemuseks oleva UTXO mitte ainult kui `konsolideerimine`, vaid spetsiifiliselt kui `KYC-vaba konsolideerimine`, et säilitada selge jälje mündi päritolust.

Lõpuks ei ole märgisele kuupäeva panemine kohustuslik. Enamik rahakottide tarkvara kuvab juba tehingu kuupäeva ja selle teabe on alati võimalik leida blokiahela uurijast, kasutades selle TXID-d.

## Õpetus: Märgistamine Specter Desktop'is

Ühendage ja avage oma rahakott Specter Desktop'is, seejärel valige `Addresses` vaheleht.

![märgistamine](assets/notext/3.webp)
Siin näete kõigi oma aadresside loendit, samuti kõiki neil lukustatud bitcoine. Vaikimisi on aadressid identifitseeritud nende indeksi järgi `Label` veerus. Märgise muutmiseks klõpsake lihtsalt sellel, sisestage soovitud märgis ja kinnitage seejärel klõpsates sinisel ikoonil.
![märgistamine](assets/notext/4.webp)

Teie märgis ilmub seejärel teie aadresside loendis.

![märgistamine](assets/notext/5.webp)

Samuti võite märgise määrata ette, kui jagate oma vastuvõtva aadressi saatjaga. Seda tehes, pääsedes ligi `Receive` vahelehele, märkige oma märgis pühendatud väljale.

![märgistamine](assets/notext/6.webp)

## Õpetus: Märgistamine Electrum'is

Electrum Wallet'is, pärast oma rahakotti sisselogimist, klõpsake tehingul, millele soovite märgise määrata, `History` vahelehelt.

![märgistamine](assets/notext/7.webp)

Avaneb uus aken. Klõpsake `Description` kastil ja tippige oma märgis.

![märgistamine](assets/notext/8.webp)

Kui märgis on sisestatud, võite selle akna sulgeda.

![märgistamine](assets/notext/9.webp)

Teie märgis on edukalt salvestatud. Leiate selle `Description` vahelehelt.

![märgistamine](assets/notext/10.webp)

`Coins` vahelehel, kust saate teostada mündikontrolli, leiate oma märgise `Label` veerust.

![märgistamine](assets/notext/11.webp)

## Õpetus: Märgistamine Green Wallet'is

Green Wallet rakenduses pääsete oma rahakotile ligi ja valige tehing, millele soovite märgise lisada. Seejärel klõpsake väikesel pliiatsi ikoonil, et märkida oma märgis.

![märgistamine](assets/notext/12.webp)

Tippige oma märgis, seejärel klõpsake rohelisel `Save` nupul.

![märgistamine](assets/notext/13.webp)

Leiate oma märgise nii oma tehingu üksikasjadest kui ka oma rahakoti armatuurlauast.

![märgistamine](assets/notext/14.webp)

## Õpetus: Märgistamine Samourai Wallet'is

Samourai Wallet'is on erinevaid meetodeid, mis võimaldavad teil tehingule märgise määrata. Esimese meetodi jaoks, avage oma rahakott ja valige tehing, millele soovite märgise lisada. Seejärel vajutage `Add` nupule, mis asub `Notes` kasti kõrval.

![märgistamine](assets/notext/15.webp)
Sisestage oma silt ja kinnitage, klõpsates sinisel `Add` nupul.
![märgistamine](assets/notext/16.webp)

Leiate oma sildi tehingu üksikasjadest, aga ka oma rahakoti armatuurlauast.

![märgistamine](assets/notext/17.webp)
Teise meetodi jaoks klõpsake ekraani paremas ülanurgas asuvatel kolmel väikesel punktil, seejärel menüül `Show Unspent Transaction Outputs`.
![märgistamine](assets/notext/18.webp)

Siin leiate oma rahakotis olevate kõikide UTXO-de põhjaliku loetelu. Kuvatud nimekiri puudutab minu deposiidikontot, kuid seda toimingut saab korrata Whirlpooli kontode jaoks, navigeerides pühendatud menüüst.

Seejärel klõpsake UTXO-l, mida soovite märgistada, järgnevalt `Add` nupul.

![märgistamine](assets/notext/19.webp)

Sisestage oma silt ja kinnitage, klõpsates sinisel `Add` nupul. Seejärel leiate oma sildi nii tehingu üksikasjadest kui ka oma rahakoti armatuurlauast.

![märgistamine](assets/notext/20.webp)

## Õpetus: Märgistamine Sparrow Wallet'is

Sparrow Wallet tarkvaraga on võimalik märgistada mitmel viisil. Lihtsaim meetod on lisada silt ette, kui edastate saatjale vastuvõtu aadressi. Selleks klõpsake menüüs `Receive` väljal `Label` ja sisestage soovitud silt. See säilitatakse ja on tarkvaras kättesaadav kohe, kui aadressile on bitcoine vastu võetud.

![märgistamine](assets/notext/21.webp)

Kui unustasite oma aadressi vastuvõtmisel märgistada, on siiski võimalik lisada silt hiljem menüü `Transactions` kaudu. Lihtsalt klõpsake oma tehingul veerus `Label`, seejärel sisestage soovitud silt.

![märgistamine](assets/notext/22.webp)

Samuti on teil võimalus lisada või muuta oma silte menüüst `Addresses`.

![märgistamine](assets/notext/23.webp)

Lõpuks saate oma silte vaadata menüüst `UTXOs`. Sparrow Wallet lisab automaatselt teie sildi taha sulgudes väljundi olemuse, mis aitab eristada vahetusest saadud UTXO-sid otse saadud UTXO-dest.

![märgistamine](assets/notext/24.webp)