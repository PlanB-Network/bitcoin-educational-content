---
name: Sentinel Watch-Only
description: Mis on Watch-Only rahakott ja kuidas seda kasutada?
---
![kaas](assets/cover.webp)

---

***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil jätkab Sentinel rakendus töötamist, kuid **on kohustuslik kasutada oma Dojo't**, et pääseda ligi plokiahela informatsioonile ja teostada tehinguid.*

_Jälgime selle juhtumi arenguid ning sellega seotud tööriistade arenguid tähelepanelikult. Võite kindlad olla, et uuendame seda õpetust, kui saabub uut informatsiooni._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest_

---

*"Hoia oma privaatvõtmed privaatsena."*

Selles artiklis uurime kõike, mida on vaja teada Watch-Only rahakottide kohta. Arutleme, kuidas need töötavad ja vaatame üle turul saadaolevad erinevad rakendused. Lõpuks pakume detailset õpetust ühe populaarseima Watch-Only rahakoti rakenduse kohta: Sentinel.

## Mis on Watch-Only Rahakott?
Watch-Only rahakott ehk ainult-vaatamise rahakott on tarkvara tüüp, mis võimaldab kasutajal jälgida tehinguid, mis on seotud ühe või mitme konkreetse Bitcoin'i avaliku võtmega, ilma et tal oleks juurdepääsu vastavatele privaatvõtmetele.

See tüüpi rakendus säilitab ainult andmed, mis on vajalikud Bitcoin'i rahakoti jälgimiseks, sealhulgas selle saldo ja tehingute ajaloo vaatamiseks, kuid tal puudub juurdepääs privaatvõtmetele. Seetõttu on võimatu kulutada rahakotis olevaid bitcoine Watch-Only rakenduse kaudu.
![watch-only](assets/en/1.webp)
Watch-Only't kasutatakse üldiselt koos riistvara rahakotiga. See võimaldab rahakoti privaatvõtmete "külma" hoiustamist seadmel, mis ei ole ühendatud internetiga, mis omab minimaalset rünnaku pinda, isoleerides privaatvõtmed potentsiaalselt haavatavatest keskkondadest. Watch-Only rakendus seevastu säilitab ainult Bitcoin'i rahakoti laiendatud avaliku võtme (`xpub`, `zpub` jne). See vanemvõti ei võimalda seotud privaatvõtmete avastamist ja seega ei luba bitcoine kulutada. Siiski võimaldab see tuletada alamavalikke võtmeid ja vastuvõtu aadresse. Tundes riistvara rahakoti poolt kaitstud rahakoti aadresse, saab Watch-Only rakendus jälgida neid tehinguid Bitcoin'i võrgus, pakkudes kasutajale võimalust jälgida oma saldot ja genereerida uusi vastuvõtu aadresse, ilma et peaks iga kord oma riistvara rahakotti ühendama.

## Millist Watch-Only Rahakotti kasutada?
Praegu on kõige terviklikum Watch-Only rakendus [Sentinel](https://sentinel.watch/), mille on välja töötanud Samourai Wallet'i meeskonnad. See hõlmab kõiki olulisi omadusi hea Watch-Only rahakoti jaoks:
- Tugi laiendatud võtmetele, avalikele võtmetele ja aadressidele;
- Võimalus korraldada mitu kontot või rahakotti kogumitesse;
- Aadresside genereerimine bitcoinide vastuvõtmiseks oma riistvara rahakotis ilma selle otsese kasutamiseta;
- Tehingute koostamine ja edastamine võrguühenduseta;
- Võimalus ühenduda omaenda Bitcoin'i noodiga;
- Tori integratsioon privaatsuse suurendamiseks.
Sentineli ainulaadsed puudused seisnevad selles, et rakendus on saadaval ainult Androidile ja see ei toeta mitme allkirjaga rahakotte. Seega, kui omate Androidi seadet ja teie rahakott on klassikaline ühe allkirjaga, soovitan Sentineli.
Neile, kes soovivad jälgida mitme allkirjaga rahakotti, on Blue Wallet ainus rakendus, mida tean, mis pakub Watch-Only režiimi nende tüüpi rahakottide jaoks, ja see on kättesaadav nii Androidis kui ka iOS-is.
iOS-i kasutajatele, kes otsivad alternatiivi Sentinelile, võivad olla võimalused [Green Wallet](https://blockstream.com/green/) või [Blue Wallet](https://bluewallet.io/watch-only/), kuigi nende ainult-vaatamise funktsionaalsus ei ole nii kõikehõlmav kui Sentinelil. ![watch-only](assets/notext/2.webp)
## Kuidas kasutada Sentinel ainult-vaatamise rahakotti?
### Paigaldamine ja seadistamine
Alustage Sentinel rakenduse paigaldamisega. Saate seda teha kas Google Play poest või kasutades [APK-d, mis on allalaadimiseks saadaval ametlikul veebilehel](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Rakenduse esmakordsel avamisel antakse teile valik:
- `Ühenda Dojoga`;
- `Ühenda Samourai serveriga`.

Dojo, mille on välja töötanud Samourai meeskond, on täielik Bitcoin node versioon, mida saab paigaldada iseseisvalt või lisada ühe klikiga node-in-box lahendustele nagu [Umbrel](https://umbrel.com/) ja [RoninDojo](https://ronindojo.io/).

[**-> Avasta, kuidas paigaldada RoninDojo v2 Raspberry Pi-le.**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

Kui teil on oma Dojo, saate selles etapis sellega ühenduda. Tehes seda, saate kasu kõrgeimast privaatsuse tasemest, kontrollides oma Bitcoin võrgu tehinguteabeid.

![watch-only](assets/notext/4.webp)

Vastasel juhul on võimalik valida Samourai vaikeserver. Samuti saate valida, kas ühenduda Tori kaudu või mitte.

![watch-only](assets/notext/5.webp)

Seejärel jõuate Sentinel pealehele.

![watch-only](assets/notext/6.webp)

Alustamiseks saate rakenduse seadistada. Klõpsake paremas ülanurgas kolmel väikesel punktil, seejärel `Settings`.

![watch-only](assets/notext/7.webp)
Valides `User PIN code`, on teil võimalus seada parool, et kaitsta juurdepääsu oma ainult-vaatamise rahakotile. Teil on ka võimalus muuta viitevaluutat, et konverteerida oma saldosid fiat-valuutasse, või isegi peita fiat-väärtused, aktiveerides `Hide fiat values` valiku. Suurema turvalisuse tagamiseks saate aktiveerida `Disable Screenshots`, mis takistab teie Sentinel rakenduse ekraanipiltide tegemist ja seeläbi väldib teabe avalikustamist välisel ekraanil.
![watch-only](assets/notext/8.webp)

Selles seadete menüüs on teil võimalus ka oma Sentinel varundada.

### Ainult-vaatamise rahakoti kasutamine
Avalehelt vajutage sinist `NEW` nuppu, et lisada uus laiendatud avalik võti jälgimiseks. Seejärel on teil võimalus skannida oma võtme QR-koodi või otse kleepida võti (`xpub`, `zpub`...) valides `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Üldiselt on teie rahakoti `xpub` otseselt kättesaadav rahakoti haldustarkvara kaudu, mida kasutate. Näiteks, kui haldate oma riistvara rahakotti Sparrow'ga, leitakse see teave `Settings` vahelehelt, `Keystore` sektsiooni alt.

![watch-only](assets/notext/10.webp)
Pärast laiendatud avaliku võtme sisestamist Sentinelis, pakub rakendus teile uue kollektsiooni loomist. Kollektsioon esindab koos organiseeritud laiendatud avalike võtmete kogumit. See võimalus annab teile võimaluse mitte ainult kõiki oma `xpubs` loetleda, vaid ka neid korrapäraselt klassifitseerida. Näiteks, kui teil on mitme kontoga Samourai rahakott (deposiit, premix, postmix...), saate kõik need kontod koondada `Samourai` kollektsiooni alla. Rahakottide haldamisel oma pere jaoks võite luua kollektsiooni nimega `Pere`.
Valige `Loo uus kollektsioon`. Seejärel sisestage äsja integreeritud laiendatud võtme jaoks nimi. Näiteks, kui skaneerin oma Samourai rahakoti deposiidikontot, nimetaksin seda võtit `Deposiit`. Klõpsake `SALVESTA`, et lõpetada.

![watch-only](assets/notext/11.webp)

Järgmisena määrake sellele kollektsioonile nimi ja vajutage ekraani paremas ülanurgas asuvale kinnitamise ikoonile, et kollektsioon salvestada. Teie kollektsioon on nüüd Sentinel avalehel nähtav.

![watch-only](assets/notext/12.webp)

Kui soovite lisada veel ühe laiendatud avaliku võtme, klõpsake uuesti `UUS` ja sisestage oma võti.

![watch-only](assets/notext/13.webp)
Seejärel palutakse teil valida kollektsioon, millesse soovite selle võtme integreerida, või luua uus. Näiteks minu puhul olen seadistanud spetsiaalse kollektsiooni oma Ledger rahakotile.
![watch-only](assets/notext/14.webp)

Kollektsiooni laiendatud võtmete üksikasjalikuks vaatamiseks klõpsake lihtsalt sellel. Seejärel saate erinevate vahelehtede kaudu navigeerida, et vaadata tehingute ajalugu.

![watch-only](assets/notext/15.webp)

Kollektsioonist, koputades ekraani paremas ülanurgas asuvatele kolmele väikesele punktile, seejärel `Vaata kulutamata väljundeid`, pääsete juurde jälgitava rahakoti poolt hoitavate UTXO-de loendile.

![watch-only](assets/notext/16.webp)

### Bitcoinide saatmine ja vastuvõtmine Sentinelist
Nagu iga hea ainult-vaatamise rahakott, võimaldab Sentinel genereerida vastuvõtu aadresse, et vastu võtta bitcoine jälgitavas rahakotis. Kuid Sentinel pakub ka teist arenenud funktsiooni: osaliselt allkirjastatud Bitcoin tehingu (PSBT) loomine ja edastamine. Seega saab rahakott, mis hoiab privaatvõtmeid, selle tehingu allkirjastada, mis, kui see on allkirjastatud, saab edastada Bitcoin võrgus Sentinel'i poolt. Vaatame, kuidas seda kõike teha.

**Ettevaatust, ei ole soovitatav vastu võtta bitcoine vastuvõtu aadressil, mida rahakott ise ei ole kinnitanud.** Kui rahakott, mis hoiab privaatvõtmeid, näiteks riistvara rahakott, ei ole selgesõnaliselt kinnitanud, et teatud aadress on sellega seotud, on bitcoinide saatmine sellele aadressile riskantne praktika. Tõepoolest, ilma selle kinnitamiseta pole mingit garantiid, et aadress tõepoolest kuulub teie rahakotile. Seetõttu tuleks ainult-vaatamise rahakoti vastuvõtu funktsiooni kasutada ettevaatlikult, arvestades, et saadetud vahendid võivad potentsiaalselt kaduma minna.

Bitcoinide vastuvõtmiseks Sentinel'i kaudu valige huvipakkuv kollektsioon, seejärel klõpsake vahelehel, mis vastab laiendatud avalikule võtmele, mille poole soovite vahendeid üle kanda.

![watch-only](assets/notext/17.webp)

Lõpuks klõpsake ekraani allosas vasakul asuval nooleikoonil. Sentinel genereerib teile tühja vastuvõtu aadressi. Saate selle kopeerida või skaneerida QR-koodi kasutades.

![watch-only](assets/notext/18.webp)
PSBT genereerimiseks Sentinel'ist ja seeläbi maksetehingu alustamiseks, minge rahakoti laiendatud võtmele, millest soovite makse teha. Võtame näiteks minu deposiidikonto minu Samourai rahakotis. Seejärel klõpsake ekraani paremas alanurgas asuval nooleikoonil.
![watch-only](assets/notext/19.webp)

Sisestage kõik teie tehinguga seotud parameetrid:
- Sisestage saaja aadress (QR-koodi ikoonil klõpsates on teil võimalus see aadress skannida);
- Määrake sellele aadressile saatmise summa;
- Määrake tehingutasud.

Kui olete kõik tehinguks vajalikud väljad täitnud, vajutage nuppu `COMPOSE UNSIGNED TRANSACTION`.

![watch-only](assets/notext/20.webp)

Seejärel pääsete juurde PSBT-le, mis esindab koostatud, kuid allkirjastamata Bitcoin tehingut, kuna Sentinel'il puudub juurdepääs teie privaatvõtmetele. Teil on võimalus see tehing kopeerida, eksportida `.psbt` failina või skannida seda animeeritud QR-koodi kaudu.

![watch-only](assets/notext/21.webp)

Seejärel minge oma rahakotti, mis omab tehingu allkirjastamiseks privaatvõtmeid (Samourai, riistvara rahakott...).

![watch-only](assets/notext/22.webp)

Kui tehing on allkirjastatud, võite naasta Sentinel'i, et seda edastada. Selleks klõpsake avalehe menüüst paremal üleval asuvatel kolmel väikesel punktil, seejärel `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Teil on võimalus sisestada oma allkirjastatud PSBT kolmel erineval viisil:
- Kleepides selle otse lõikelauale;
- Importides selle `.psbt` failist;
- Skannides selle QR-koodi kaudu.

![watch-only](assets/notext/24.webp)

Kui allkirjastatud tehing on halli raami sisestatud, võite vajutada rohelisele nupule `BROADCAST TRANSACTION`, et edastada see Bitcoin võrgus. Sentinel annab teile selle TXID.

![watch-only](assets/notext/25.webp)

