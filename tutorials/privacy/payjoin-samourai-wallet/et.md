---
name: Payjoin - Samourai Wallet
description: Kuidas teostada Payjoin tehingut Samourai Wallet'is?
---
![samourai payjoin kaas](assets/cover.webp)

***TÄHELEPANU:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil toimivad Payjoins Stowaway tehingud Samourai Wallet'is ainult käsitsi PSBT vahetades huvitatud osapoolte vahel, eeldusel, et mõlemad kasutajad on ühendatud omaenda Dojoga. Sparrow puhul töötavad Payjoins BIP78 kaudu endiselt. Siiski on võimalik, et need tööriistad taaskäivitatakse järgnevate nädalate jooksul. Vahepeal võite siiski seda artiklit lugeda, et mõista Stowaway teoreetilist toimimist.*

_Kui plaanite teostada Stowaway tehingut käsitsi, on protseduur väga sarnane selles õpetuses kirjeldatuga. Peamine erinevus seisneb Stowaway tehingu tüübi valikus: `Online` asemel klõpsake `In Person / Manual`. Seejärel peate käsitsi vahetama PSBTsid, et konstrueerida Stowaway tehing. Kui olete oma koostööpartneriga füüsiliselt lähedal, saate QR-koode järjest skannida. Kui olete kaugel, saab JSON-faile vahetada turvalise suhtluskanali kaudu. Ülejäänud õpetus jääb muutmata._

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Olge kindlad, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *"Sunnib plokiahela spioone ümber mõtlema kõike, mida nad arvavad teadvat."*

Payjoin on konkreetne Bitcoin'i tehingu struktuur, mis suurendab kasutaja privaatsust kulutamise ajal, tehes koostööd makse saajaga. On mitmeid rakendusi, mis hõlbustavad PayJoin'i seadistamist ja automatiseerimist. Nende rakenduste hulgas on kõige tuntum Stowaway, mille on välja töötanud Samourai Wallet'i meeskonnad. See õpetus selgitab, kuidas teostada Stowaway Payjoin tehingut kasutades Samourai Wallet rakendust.

## Kuidas Stowaway töötab?

Nagu varem mainitud, pakub Samourai Wallet PayJoin tööriista nimega "Stowaway." See on kättesaadav läbi Sparrow Wallet tarkvara PC-l või Samourai Wallet rakenduse Androidis. Payjoin'i teostamiseks peab saaja, kes samuti toimib koostööpartnerina, kasutama Stowaway'ga ühilduvat tarkvara, nimelt Sparrow'd või Samourai'd. Need kaks tarkvara on omavahel ühilduvad, võimaldades Stowaway tehingut Sparrow rahakoti ja Samourai rahakoti vahel, ja vastupidi.

Stowaway tugineb tehingute kategooriale, mida Samourai nimetab "Cahoots'iks." Cahoot on sisuliselt koostöö tehing mitme kasutaja vahel, mis nõuab väljaspool ahelat toimuvat infovahetust. Praeguse seisuga pakub Samourai kahte Cahoots tööriista: Stowaway (Payjoins) ja StonewallX2 (mida uurime tulevases artiklis).

Cahoots tehingud hõlmavad osaliselt allkirjastatud tehingute vahetusi kasutajate vahel. See protsess võib olla pikk ja tülikas, eriti kui see toimub kaugelt. Siiski on see siiski võimalik käsitsi teostada teise kasutajaga, mis võib olla mugav, kui koostööpartnerid on füüsiliselt lähedal. Praktikas hõlmab see viie QR-koodi käsitsi vahetamist, mida tuleb järjest skannida.
Kui seda protsessi tehakse kaugjuhtimisega, muutub see liiga keerukaks. Selle probleemi lahendamiseks on Samourai välja töötanud krüpteeritud suhtlusprotokolli, mis põhineb Toril, nimetusega "Soroban". Sorobani abil automatiseeritakse Payjoini jaoks vajalikud vahetused kasutajasõbraliku liidese taga. See on teine meetod, mida me selles artiklis uurime.

Need krüpteeritud vahetused nõuavad ühenduse loomist ja autentimist Cahootsi osalejate vahel. Seega põhinevad Sorobani suhtlused kasutajate Paynymidel. Kui te ei ole Paynymidega tuttav, siis kutsun teid üles lugema selle kohta rohkem siit: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Lihtsalt öeldes on Paynym unikaalne identifikaator, mis on seotud teie rahakotiga ja võimaldab erinevaid funktsioone, sealhulgas krüpteeritud sõnumite saatmist. Paynym esitatakse identifikaatori ja illustratsioonina, mis kujutab robotit. Siin on minu näide Testnetis: ![paynym samourai wallet](assets/en/1.webp)

**Kokkuvõttes:**
- _Payjoin_ = Koostööl põhinevate tehingute spetsiifiline struktuur;
- _Stowaway_ = Payjoini rakendus, mis on saadaval Samourai ja Sparrow Walletis;
- _Cahoots_ = Nimi, mille Samourai on andnud kõigile oma koostööl põhinevatele tehingutele, sealhulgas Payjoin Stowaway;
- _Soroban_ = Krüpteeritud suhtlusprotokoll, mis on loodud Tori peal, võimaldades koostööd teiste kasutajatega Cahootsi tehingu kontekstis;
- _Paynym_ = Rahakoti unikaalne identifikaator, mis võimaldab suhelda teise kasutajaga Sorobanis, et teostada Cahootsi tehing.

[**-> Uuri lähemalt Payjoin tehingute ja nende kasulikkuse kohta**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Kuidas luua ühendus Paynymide vahel?

Kaugjuhtimisega Cahootsi tehingu, eriti PayJoini (Stowaway) teostamiseks Samourai kaudu, on vajalik "Jälgida" kasutajat, kellega soovite koostööd teha, kasutades nende Paynymi. Stowaway puhul tähendab see isiku jälgimist, kellele soovite bitcoine saata.

**Siin on protseduur selle ühenduse loomiseks:**

Alustuseks peate saama saaja Paynymi maksekoodi Payjoini jaoks. Samourai Wallet rakenduses peab saaja koputama oma Paynymi ikoonile (väike robot), mis asub ekraani ülaosas vasakul, ja seejärel klõpsama oma Paynymi hüüdnimele, mis algab `+...`. Näiteks minu oma on `+namelessmode0aF`. Kui teie kaastöötaja kasutab Sparrow Walletit, siis kutsun teid üles tutvuma meie pühendatud õpetusega, klõpsates siin.

![connexion paynym samourai](assets/notext/2.webp)

Teie kaastöötaja suunatakse seejärel oma Paynymi lehele. Sealt saavad nad kas jagada oma Paynymi andmeid teiega või jagada oma QR-koodi, mida saate skannida. Selleks peavad nad klõpsama väikesel "jaga" ikoonil, mis asub nende ekraani ülaosas paremal.
![partager paynym samourai](assets/en/1.webp)

Teie poolel käivitage oma Samourai Wallet rakendus ja pääsete samamoodi juurde "PayNyms" menüüle. Kui kasutate oma Paynymi esimest korda, peate hankima identifikaatori.

![demander un paynym](assets/notext/3.webp)

Seejärel klõpsake ekraani paremas alanurgas sinisel "+".
![ajouter paynym collaborateur](assets/notext/4.webp)
Seejärel saate oma koostööpartneri maksekoodi kleepida, valides `COLLER LE CODE PAIEMENT`, või avada kaamera nende QR-koodi skaneerimiseks, vajutades `SCANNEZ LE CODE QR`. ![paste paynym identifier](assets/notext/5.webp)
Klõpsake nupul `SUIVRE`.
![follow paynym](assets/notext/6.webp)
Kinnitage, klõpsates `YES`.
![confirm follow paynym](assets/notext/7.webp)
Seejärel pakub tarkvara teile nuppu `SE CONNECTER`. Meie õpetuse jaoks ei ole selle nupu vajutamine vajalik. See samm on vajalik ainult juhul, kui plaanite teha makseid teisele Paynym'ile osana [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)-st, mis ei ole meie õpetusega seotud.
![connect paynym](assets/notext/8.webp)
Kui saaja Paynym on teie Paynym'i poolt jälgitud, korrake seda toimingut vastupidises suunas, nii et saaja jälgiks ka teid. Seejärel saate teostada Payjoini.

## Kuidas teha Payjoini Samourai Wallet'is?

Kui olete need esialgsed sammud lõpetanud, olete lõpuks valmis sooritama Payjoin tehingu! Selleks järgige meie videoõpetust:

![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Välised ressursid:**
- https://docs.samourai.io/en/spend-tools#stowaway.