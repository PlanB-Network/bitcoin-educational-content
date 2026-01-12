---
name: LNP2PBot
description: Täielik juhend LNP2PBot ja P2P bitcoin kauplemine
---
![cover](assets/cover.webp)

## Sissejuhatus

KYC-vabad peer-to-peer (P2P) börsid on kasutajate konfidentsiaalsuse ja finantsautonoomia säilitamiseks hädavajalikud. Need võimaldavad otsetehinguid üksikisikute vahel ilma isikusamasuse kontrollimiseta, mis on oluline nende jaoks, kes hindavad privaatsust. Teoreetiliste mõistete põhjalikumaks mõistmiseks vaadake kursust BTC204:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoini ostmine ja müümine peer-to-peer (P2P) on üks kõige privaatsemaid meetodeid bitcoinide omandamiseks või võõrandamiseks. LNP2PBot on avatud lähtekoodiga Telegrami bot, mis hõlbustab P2P-vahetust Lightning-võrgus, võimaldades kiireid, odavaid ja KYC-vabasid tehinguid.

### Miks kasutada Lnp2pbot'i?


- KYC ei ole nõutav
- Kiired tehingud Lightning-võrgus
- Madalad kulud
- Lihtne kasutajaliides Telegrami kaudu, mis on populaarne sõnumirakendus, mis on kättesaadav kõikjal maailmas
- Integreeritud mainesüsteem
- Automaatne eskroov turvaliseks kauplemiseks
- Mitme valuuta tugi
- Aktiivne ja kasvav kogukond

### Eeltingimused

Lnp2pbot'i kasutamiseks on vaja :

1. Lightning Network rahakott (soovitatav on Breez, Phoenix või Blixt)

2. Telegram rakendus paigaldatud (https://telegram.org/)

3. Telegrami konto, millel on määratud kasutajanimi

## Paigaldamine ja konfigureerimine

### 1. Lightning rahakoti konfigureerimine

Alusta ühilduva Lightning rahakoti paigaldamisega. Siin on meie üksikasjalikud soovitused:

**Soovitatav portfell**


- [Breez](https://breez.technology):
  - Suurepärane algajatele
  - Intuitiivne, kaasaegne kasutajaliides
  - Mittehooldusõiguslik (teil säilib kontroll oma rahaliste vahendite üle)
  - Täiesti ühildub Lnp2pbotiga
  - Saadaval iOS ja Android

Allpool on link selle rahakoti õpetuse juurde:

https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co) :
  - Lihtne ja usaldusväärne
  - Automaatne kanalite konfigureerimine
  - BOLT11 arvete loomulik tugi
  - Suurepärane igapäevasteks tehinguteks
  - Saadaval iOS ja Android

Allpool on link selle rahakoti õpetuse juurde:

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io) :
  - Tehnilisem, kuid väga täielik
  - Täiustatud seadistamisvõimalused
  - Ideaalne kogenud kasutajatele
  - Avatud lähtekood
  - Saadaval Androidis

Allpool on link selle rahakoti õpetuse juurde:

https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Tähtsaid märkusi teiste portfellide kohta**

⚠️ **Tähtis**: Enne satside müüki veenduge, et teie portfell toetab "ootearveid", mida bott kasutab eskrovisüsteemina.


- **Satoshi rahakott**: Töötab hästi sati vastuvõtmiseks, kuid võib esineda viivitusi saldo uuendamisel, kui müük tühistatakse.
- **Muun**: Ei soovitata, kuna maksed võivad ebaõnnestuda boti marsruutimistasu piirangute tõttu (maksimaalselt 0,2%).
- **Aqua**: Töötab sati vastuvõtmiseks, kuid müügi tühistamise korral võib saldo uuendamine viibida pikalt (kuni 48 tundi).

💡 **Tipp**: Optimaalse kogemuse saamiseks valige soovitatud portfellid (Breez, Phoenix või Blixt).

⚠️ **Tähtis**: Ärge unustage salvestada oma taastumisfraasid turvalisse kohta.

### 2. Lnp2pbotiga alustamine

1. Klõpsake sellel lingil, et pääseda botile juurde: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram avaneb automaatselt

3. Klõpsake "Start" või saatke käsk "/start"

4. Bot palub teil luua kasutajanimi, kui teil veel ei ole seda

5. Robot juhendab teid esialgse konfiguratsiooni kaudu

### 3. Liitu kogukonnaga


- Liituge põhikanaliga: [@p2plightning](https://t.me/p2plightning)
- Toetus: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Bitcoinide ostmine ja müümine

Lnp2pbotil on kaks peamist viisi bitcoinide vahetamiseks:

1. Turul olevate pakkumiste sirvimine ja neile reageerimine

2. Loo oma ostu- või müügipakkumine

Selles juhendis vaatame üksikasjalikult, kuidas :


- Osta bitcoine olemasolevast pakkumisest
- Müüge bitcoine, luues oma pakkumise

### Kuidas osta Bitcoine

**1. Leia ja vali pakkumine**

![Sélection d'une offre de vente](assets/fr/01.webp)

Sirvige pakkumisi [@p2plightning](https://t.me/p2plightning) ja klõpsake huvipakkuva kuulutuse all nupul "Osta satoshis".

**2. Kinnitage pakkumine ja summa**

![Validation de l'offre](assets/fr/02.webp)

1. Tagasi boti vestluse juurde

2. Kinnitage oma pakkumise valik

3. Sisestage summa fiat-valuutas, mida soovite osta

4. Bott palub teil esitada Lightning arve summa eest satoshis

**3. Võtke ühendust müüjaga**

![Mise en relation](assets/fr/03.webp)

Kui arve on saadetud, paneb robot teid müüjaga ühendust võtma.

**4. Suhtlemine müüjaga**

![Chat privé](assets/fr/04.webp)

Klõpsake müüja hüüdnimele, et avada privaatne vestluskanal, kus saate vahetada fiat-makse üksikasju.

**5. Makse kinnitamine**

![Confirmation du paiement](assets/fr/05.webp)

Pärast fiat-makse sooritamist kasuta bot'i vestluses käsku `/fiatsent`. Kui tehing on lõpule viidud, saate müüjat hinnata ja tehing suletakse.

### Kuidas müüa Bitcoine

**1. Loo müügipakkumine**

![Création d'une offre de vente](assets/fr/06.webp)

Müügipakkumise loomiseks kasutage lihtsalt käsku :

`/müüa`

Seejärel juhendab robot teid samm-sammult:

1. Valige oma valuuta

2. Märkige müüdavate satoshide kogus

3. Hinna osas on teil kaks võimalust:


   - Määrata kindlaksmääratud hind satoshi kogusele
   - Kasutage turuhinda koos võimalusega kohaldada preemiat (positiivset või negatiivset)

💡 **Tipp**: Lisatasu võimaldab teil kohandada oma hinda turuhinna suhtes. Näiteks lisatasu -1% tähendab, et müüte 1% vähem kui turuhind.

**2. Tellimuse loomise kinnitus**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Kui tellimus on loodud, näete kinnitust, kus on võimalus tellimus tühistada, kasutades käsku `/cancel`.

**3. Müügi juhtimine**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Kui ostja vastab teie pakkumisele, saate teate koos QR-koodiga ja arve tasumiseks.
- Kontrollige ostja profiili ja mainet.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Klõpsake ostja hüüdnimele, et avada privaatne arutelukanal.
- Teatage ostjale fiat-makse üksikasjad.
- Oodake ostjalt kinnitust fiat-makse kohta.
- Kontrollige, et makse on teie kontole laekunud.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Kinnitage tehing käsuga `/release` ja lõpetage tellimus. Teil on võimalus ostjat hinnata.

## Head tavad ja ohutus

### Ohutusnõuanded


- Alustage väikeste kogustega
- Kontrollige alati kasutajate mainet
- Kasutage ainult soovitatud makseviise
- Hoidke kogu suhtlus bot'i vestluses
- Ärge kunagi jagage tundlikku teavet

### Maine süsteem


- Igal kasutajal on maine skoor
- Edukad tehingud suurendavad teie skoori
- Valige hea mainega kasutajad
- Teatage moderaatoritele igast kahtlasest käitumisest

### Vaidluste lahendamine

1. Probleemide tekkimisel jääge rahulikuks ja professionaalseks

2. Kasutage pileti avamiseks käsku `/dispute`

3. Esitage kõik vajalikud tõendid

4. Oodake moderaatorit

## Võrdlus teiste lahendustega

Lnp2pbotil on mitmeid eeliseid ja puudusi võrreldes teiste P2P-vahetuslahendustega, nagu Peach, Bisq, HodlHodl ja Robosat:

### Lnp2pbot'i eelised


- **KYC ei ole nõutav**: Erinevalt mõnest platvormist ei nõua Lnp2pbot isikusamasuse kontrollimist, säilitades seega kasutaja konfidentsialususe.
- **Kiired tehingud**: Tänu Lightning-võrgule on tehingud peaaegu kohesed.
- **Madalad tasud**: Tehingukulud on madalamad kui traditsioonilistel börsidel.
- **Mobiilne kättesaadavus**: LNP2PBot on kättesaadav Telegrami kaudu, mistõttu on seda lihtne kasutada mobiilseadmetes.
- **Lihtne kasutada**: Lnp2pbot'i intuitiivne kasutajaliides teeb selle kasutamise lihtsaks ka vähem kogenud kasutajatele.

### Lnp2pbot'i puudused


- **Telegrammi sõltuvus**: Lnp2pbot'i kasutamine nõuab Telegram-kontot, mis ei pruugi kõigile kasutajatele sobida.
- **Vähem likviidsust**: Võrreldes rohkem väljakujunenud platvormidega, nagu Bisq, võib likviidsus olla piiratum.

Võrdluseks pakuvad sellised lahendused nagu Bisq suuremat likviidsust ja töölaua kasutajaliidest, kuid võivad olla seotud kõrgema tasu ja pikema tehinguajaga. HodlHodl ja Robosat pakuvad samuti KYC-vaba kauplemist, kuid erineva tasustruktuuri ja liidestega.

## Kasulikud ressursid


- Ametlik veebileht: https://lnp2pbot.com/
- Dokumentatsioon: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Toetus: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)