---
name: NOSTR

description: Avasta ja hakka kasutama NOSTRit
---


![Uus väljakutsuja on saabunud](assets/1.webp)

*Selle juhendi lõpuks mõistate, mis on Nostr, olete loonud konto ja saate seda kasutada.*

## Mis on Nostr?

Nostr on protokoll, millel on jõud asendada Twitter, Telegram ja teised sotsiaalmeedia platvormid. See on lihtne avatud protokoll, mis on võimeline looma ülemaailmselt vastupidava sotsiaalvõrgustiku kord ja lõplikult.

## Kuidas see töötab?

Nostr põhineb kolmel komponendil: võtmepaaridel, klientidel ja releejaamadel.

Igal kasutajal on üks või mitu identiteeti ja iga identiteet määratakse krüptograafilise võtmepaari abil.

Võrgule juurdepääsuks peate kasutama klienditarkvara ja ühenduma releejaamadega sisu vastuvõtmiseks ja edastamiseks.

![Võtmesüsteem](assets/2.webp)

## 1. Krüptograafilised võtmed

Erinevalt Facebookist või Twitterist, kus kasutajad peavad andma oma e-posti aadressi ja hulgaliselt teavet eraettevõttele, toimib Nostr ilma keskse autoriteedita. Kasutajad genereerivad krüptograafilise võtmepaari, salajase võtme (tuntud ka kui privaatvõti) ja avaliku võtme.

Salajast võtit, nsec, teab ainult kasutaja ja seda kasutatakse autentimiseks ja sisu avaldamiseks.

Avalik võti, npub, on unikaalne identifikaator, millele kõik kasutaja poolt avaldatud sisu on kinnitatud. Teie avalik võti on nagu kasutajanimi, mis võimaldab teistel kasutajatel teid leida ja tellida teie Nostr'i voogu.

## 2. Kliendid

Kliendid on tarkvara, mis võimaldab suhelda Nostr'iga. Peamised kliendid on:

- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja

Kliendid võimaldavad kasutajatel genereerida uue võtmepaari (võrdväärne konto loomisega) või autentida olemasoleva võtmepaariga.

## 3. Releejaamad

Releejaamad on lihtsad serverid, millest võite igal ajal loobuda, kui teile nende edastatav sisu ei meeldi. Samuti võite soovi korral käitada oma releejaama.

> 💡 Pro näpunäide: Tasulised releejaamad on tavaliselt tõhusamad rämpsposti ja soovimatu sisu filtreerimisel.

## Juhend

Nüüd teate piisavalt Nostr'ist, et alustada ja luua oma esimene identiteet sellel protokollil.

Selle juhendi eesmärgil kasutame iris.to-d (https://iris.to/), kuna see veebiklient töötab igal platvormil.

## 1. samm: Võtmete genereerimine

Iris loob teie jaoks võtmepaari, ilma et peaksite tegema muud, kui sisestama oma profiili jaoks nime (päris või väljamõeldud). Seejärel klõpsake nupul GO ja ongi valmis!

![Peamenüü](assets/3.webp)

> ⚠️ Tähelepanu! Peate jälgima oma võtmeid, kui soovite oma profiilile uuesti juurde pääseda, kui teie seanss on suletud. Ma näitan teile, kuidas seda juhendi lõpus teha.

## 2. samm: Sisu avaldamine

Sisu avaldamine on sama lihtne ja intuitiivne kui mõne sõna kirjutamine avaldamisväljale.

![Avaldamine](assets/4.webp)

Nii see on! Olete avaldanud oma esimese märkuse Nostr'is.

![Postitus](assets/5.webp)

## 3. samm: Leia sõber

Leia mind Nostr'is ja sa ei ole enam kunagi üksi. Ma tellin tagasi kõigile, kes tellivad minu voogu. Selleks sisestage lihtsalt minu avalik võti

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 otsinguribale.
![Minu profiil](assets/6.webp)
Klõpsa "jälgi" ja mõne päeva jooksul maksimaalselt tellin ka mina sinu voogu. Meist saavad sõbrad. Olen samuti rõõmus, kui soovid mulle sõnumi kirjutada.

Lõpuks veendu, et tellid ka Agora256 voogu, et saada märge iga kord, kui me midagi uut avaldame: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## 4. samm: Kohanda oma profiili

Sul on veel natuke tööd teha, et oma profiili kohandada. Selleks klõpsa avatari peal, mille iris automaatselt sulle ekraani paremas ülanurgas genereeris, ja seejärel klõpsa "muuda profiili".

![Profiil](assets/7.webp)

Nüüd pead lihtsalt ütlema irisele, kust leida sinu pilti ja profiilibännerit internetis. Soovitan oma sisu ise majutada: kaitse seda, mis on sinu oma.

![Teine võimalus](assets/8.webp)

Kui eelistad, võid ka pilte üles laadida, iris hoiustab neid sinu eest nostr.build lehel, mis on tasuta visuaalse sisu majutusteenus Nostrile.

Nagu näed, saad sa ka seadistada oma klienti, et oleks võimalik saata ja vastu võtta satse. Nii saad premeerida sisu autoreid, mis sulle meeldis või veel parem, koguda satse suurepärase sisu eest, mida avaldad.

## 5. samm: Varunda võtmepaar

See samm on kriitilise tähtsusega, kui soovid säilitada juurdepääsu oma profiilile pärast kliendist väljalogimist või sessiooni aegumist.
Esmalt klõpsa "seaded" ikoonil, mida esindab hammasratas
![Seaded](assets/9.webp)

Seejärel kopeeri ja kleebi ükshaaval oma npub, npub hex, nsec ja nsec hex tekstifaili, mida hoiad turvaliselt. Soovitan selle faili krüpteerida, kui tead, kuidas seda teha.

![Võti](assets/10.webp)

> ⚠️ Pane tähele hoiatust, mida iris sulle annab. Kuigi oma avalikku võtit võid jagada kartmatult, on privaatvõtmega lugu teine. Igaüks, kellel see on, saab juurdepääsu sinu kontole.

## Järeldus

Näe, väike jaanalind, oled astunud oma esimesed sammud Nostril. Nüüd pead õppima jooksma välkkiirusel. Varsti avaldame juhendid, mis näitavad, kuidas hallata oma võtmeid ja kuidas integreerida välk Nostr kogemusse kasutades getalby.