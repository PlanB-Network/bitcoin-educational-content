---
name: Payjoin - Sparrow Wallet
description: Kuidas teha Payjoin tehingut Sparrow Wallet'is?
---
![õpetuse kaanepilt sparrow payjoin](assets/cover.webp)

_**HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil töötavad Payjoins Stowaway'd Samourai Wallet'is nüüd ainult käsitsi PSBT vahetades osapoolte vahel, eeldusel, et mõlemad kasutajad on ühendatud omaenda Dojoga. Sparrow' puhul töötavad Payjoinsid BIP78 kaudu endiselt. Siiski võidakse need tööriistad järgnevatel nädalatel taaskäivitada. Vahepeal võite alati seda artiklit lugeda, et mõista payjoinide teoreetilist toimimist._

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *"Sunnib plokiahela nuhke kõike, mida nad arvavad teadvat, ümber mõtlema."*

Payjoin on konkreetne Bitcoin'i tehingu struktuur, mis parandab kasutaja privaatsust kulutamisel, tehes koostööd makse saajaga. On mitmeid rakendusi, mis hõlbustavad PayJoin'i seadistamist ja automatiseerimist. Nende rakenduste hulgas on kõige tuntum Stowaway, mille on välja töötanud Samourai Wallet'i meeskond. See õpetus on mõeldud juhendama teid läbi Stowaway Payjoin tehingu tegemise protsessi, kasutades Sparrow Wallet tarkvara.

## Kuidas Stowaway töötab?

Nagu varem mainitud, pakub Samourai Wallet PayJoin tööriista nimega "Stowaway". See on kättesaadav Sparrow Wallet tarkvara kaudu arvutis või Samourai Wallet rakenduses Androidis. Payjoin'i tegemiseks peab saaja, kes samuti toimib koostööpartnerina, kasutama Stowaway'ga ühilduvat tarkvara, nimelt Sparrow'd või Samourai Wallet'i. Need kaks tarkvara on omavahel ühilduvad, võimaldades Stowaway tehinguid Sparrow rahakoti ja Samourai rahakoti vahel ning vastupidi.

Stowaway tugineb tehingute kategooriale, mida Samourai nimetab "Cahoots'iks". Cahoot on sisuliselt mitme kasutaja vaheline koostöötehing, mis nõuab väljaspool ahelat toimuvat infovahetust. Praegu pakub Samourai kahte Cahoots tööriista: Stowaway (Payjoins) ja StonewallX2 (mida uurime tulevases artiklis).

Cahoots tehingud hõlmavad osaliselt allkirjastatud tehingute vahetamist kasutajate vahel. See protsess võib olla pikk ja tülikas, eriti kui see toimub kaugelt. Siiski saab seda siiski teha käsitsi teise kasutajaga, mis võib olla mugav, kui koostööpartnerid on füüsiliselt lähedal. Praktikas hõlmab see viie QR-koodi käsitsi vahetamist, mida tuleb järjestikku skannida.

Kaugelt tehes muutub see protsess liiga keerukaks. Selle probleemi lahendamiseks on Samourai välja töötanud Toril põhineva krüpteeritud suhtlusprotokolli nimega "Soroban". Sorobaniga automatiseeritakse Payjoin'i jaoks vajalikud vahetused kasutajasõbraliku liidese taga. See on teine meetod, mida me selles artiklis uurime.

Need krüpteeritud vahetused nõuavad Cahoots osalejate vahelise ühenduse ja autentimise loomist. Soroban suhtlused tuginevad kasutajate Paynymidele. Kui te ei ole Paynymidega tuttav, siis soovitan teil tutvuda selle artikliga lisateabe saamiseks: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Lihtsalt öeldes on Paynym unikaalne identifikaator, mis on seotud teie rahakotiga ja võimaldab erinevaid funktsioone, sealhulgas krüpteeritud sõnumite saatmist. Paynym esitatakse identifikaatori ja illustratsioonina, mis kujutab robotit. Siin on näide minu omast Testnetis: ![Paynym Sparrow](assets/en/1.webp)
**Kokkuvõttes:**
- *Payjoin* = Koostööl põhineva tehingu spetsiifiline struktuur;
- *Stowaway* = Payjoini rakendus, mis on saadaval Samourai ja Sparrow Walletis;
- *Cahoots* = Nimetus, mille Samourai on andnud kõigile oma koostööl põhinevatele tehingutele, sealhulgas Payjoin Stowaway;
- *Soroban* = Krüpteeritud suhtlusprotokoll, mis on loodud Tori peal, võimaldades koostööd teiste kasutajatega Cahoots tehingu kontekstis.
- *Paynym* = Rahakoti unikaalne identifikaator, mis võimaldab suhelda teise kasutajaga Sorobanis, et teostada Cahoots tehing.

[**-> Uuri lähemalt Payjoin tehingute ja nende kasulikkuse kohta**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Kuidas luua ühendust Paynymide vahel?

Kaug-Cahoots tehingu, eriti PayJoin (Stowaway) teostamiseks Samourai või Sparrow kaudu, on vajalik "Jälgida" kasutajat, kellega soovite koostööd teha, kasutades nende Paynymi. Stowaway puhul tähendab see isiku jälgimist, kellele soovite bitcoine saata.

**Siin on protseduur selle ühenduse loomiseks:**

Esmalt peate saama saaja Paynymi identifikaatori. Seda saab teha kasutades nende hüüdnime või maksekoodi. Selleks valige saaja Sparrow rahakotist `Tools` vaheleht, seejärel klõpsake `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
Teie poolel avage oma Sparrow Wallet ja pääsege samale `Show PayNym` menüüle. Kui kasutate oma Paynymi esimest korda, peate identifikaatori saamiseks klõpsama `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Järgmisena sisestage oma koostööpartneri Paynymi identifikaator (kas nende hüüdnimi `+...` või nende maksekood `PM...`) `Find Contact` kasti, seejärel klõpsake `Add Contact` nupule.
![add contact](assets/notext/4.webp)
Tarkvara pakub seejärel `Link Contact` nuppu. Meie õpetuse kontekstis ei ole selle nupu vajutamine vajalik. See samm on vajalik ainult juhul, kui plaanite teha makseid näidatud Paynymile [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093) kontekstis, mis ei ole seotud meie õpetusega.

Kui saaja Paynymi jälgib teie Paynym, korrake seda toimingut vastupidises suunas, nii et teie saaja jälgib ka teid. Seejärel saate teostada Payjoini.

## Kuidas teostada Payjoini Sparrow Walletis?
Kui olete need mõned esialgsed sammud lõpetanud, olete lõpuks valmis teostama Payjoin tehingu! Selleks järgige meie videoõpetust:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Välised ressursid:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.