---
name: Stonewall x2
description: Stonewall x2 tehingute mõistmine ja kasutamine
---
![kaanepilt stonewall x2](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil toimivad Stonewallx2 tehingud ainult käsitsi PSBT-de vahetamise teel asjaomaste osapoolte vahel, eeldusel, et mõlemad kasutajad on ühendatud omaenda Dojoga. Siiski on võimalik, et need tööriistad taaskäivitatakse lähinädalatel. Vahepeal võite siiski seda artiklit konsulteerida, et mõista Stonewallx2 teoreetilist toimimist ja õppida, kuidas neid käsitsi teha.*

_Kui kaalute Stonewallx2 käsitsi sooritamist, on protseduur väga sarnane selles õpetuses kirjeldatuga. Peamine erinevus seisneb Stonewallx2 tehingu tüübi valikus: `Online` asemel klõpsake `Isiklikult / Käsitsi`. Seejärel peate PSBT-d käsitsi vahetama, et konstrueerida Stonewallx2 tehing. Kui olete oma koostööpartneriga füüsiliselt lähedal, saate QR-koode järjestikku skannida. Kui olete kaugel, saab JSON-faile vahetada turvalise suhtluskanali kaudu. Ülejäänud õpetus jääb muutmata._

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui uut teavet saadaval on._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *Muuda iga kulutus coinjoiniks.*

## Mis on Stonewall x2 tehing?

Stonewall x2 on spetsiifiline Bitcoin'i tehingu vorm, mille eesmärk on suurendada kasutaja privaatsust kulutamise ajal, tehes koostööd kolmanda osapoolega, kes ei ole selles kulutuses osaline. See meetod simuleerib mini-coinjoin'i kahe osaleja vahel, samal ajal tehes makse kolmandale osapoolele. Stonewall x2 tehingud on saadaval nii Samourai Wallet rakenduses kui ka Sparrow Wallet tarkvaras. Mõlemad on omavahel ühilduvad.

Selle toimimine on suhteliselt lihtne: me kasutame oma valduses olevat UTXO-d makse tegemiseks ja otsime abi kolmandalt osapoolelt, kes samuti panustab oma UTXO-ga. Tehing toob kaasa neli väljundit: kaks neist võrdsetes summas, üks on mõeldud makse saaja aadressile, teine kuulub koostööpartnerile. Kolmas UTXO tagastatakse teisele aadressile, mis kuulub koostööpartnerile, võimaldades neil algsumma tagasi saada (neutraalne tegevus nende jaoks, miinus kaevandamistasud), ja viimane UTXO naaseb aadressile, mis kuulub meile, mis kujutab endast maksest üle jäänud raha.

Seega on Stonewall x2 tehingutes määratletud kolm erinevat rolli:
- Saatja, kes teeb tegeliku makse;
- Koostööpartner, kes annab bitcoine, et parandada tehingu üldist anonüümsust, taastades samal ajal täielikult oma vahendid lõpus (neutraalne tegevus nende jaoks, miinus kaevandamistasud);
- Saaja, kes võib olla tehingu spetsiifilisest olemusest teadmata ja lihtsalt ootab saatjalt makset.

Võtame näiteks, et paremini mõista. Alice on pagaripoes, et osta oma baguette, mis maksab `4,000 satsi`. Ta soovib maksta bitcoinides, säilitades samal ajal teatud privaatsuse taseme oma makse jaoks. Seetõttu kutsub ta appi oma sõbra Bobi, kes aitab teda selles protsessis.
![skeem stonewall x2](assets/en/1.webp)
Analüüsides seda tehingut, võime näha, et pagar sai tõepoolest `4,000 sats` makseks bageti eest. Alice kasutas sisendina `10,000 sats` ja sai väljundina `6,000 sats`, mis tulemusena andis netosaldo `-4,000 sats`, mis vastab bageti hinnale. Mis puutub Bobi, siis ta pakkus sisendina `15,000 sats` ja sai kaks väljundit: ühe `4,000 sats` ja teise `11,000 sats`, mis tulemusena andis saldo `0`. Selles näites jätsin ma tahtlikult kaevandamistasud arvestamata, et hõlbustada mõistmist. Tegelikkuses jagatakse tehingutasud võrdselt makse saatja ja kaastöötaja vahel.

## Mis vahe on Stonewall ja Stonewall x2 vahel?

StonewallX2 tehing toimib täpselt nagu Stonewall tehing, välja arvatud see, et esimene on koostööalane, samas kui viimane ei ole. Nagu me oleme näinud, hõlmab Stonewall x2 tehing kolmanda osapoole osalemist, kes ei ole maksega seotud, ja kes pakub oma bitcoine, et suurendada tehingu privaatsust. Tüüpilises Stonewall tehingus võtab saatja enda peale kaastöötaja rolli.

Vaadakem uuesti meie näidet Alice'ist pagaripoes. Kui ta ei oleks leidnud kedagi nagu Bob, kes teda tema kulutuses saadaks, oleks ta võinud teha Stonewall tehingu üksi. Seega oleksid mõlemad sisendi UTXOd olnud tema omad, ja ta oleks saanud väljundis 3.
![transaction stonewall](assets/en/2.webp)

Välisest vaatepunktist oleks tehingu muster jäänud samaks.
![Stonewall või Stonewall x2?](assets/en/5.webp)
Seega peaks loogika olema järgmine, kasutades Samourai kulutamise tööriista:
- Kui kaupmees ei toeta Payjoin Stowaway'd, saab teha koostööalase tehingu teise isikuga, kes ei ole maksega seotud, kasutades Stonewall x2.
- Kui ei leita kedagi, kes teeks Stonewall x2 tehingu, saab teha Stonewall tehingu üksi, jäljendades Stonewall x2 tehingu käitumist.
- Lõpuks oleks viimane võimalus teha tehing JoinBot'iga, serveriga, mida haldab Samourai, mis võib taotluse korral tegutseda kaastöötajana Stonewall x2 tehingus.

Kui soovite leida kaastöötajat, kes on valmis teid aitama Stonewall X2 tehingus, võite külastada ka seda Telegrami gruppi (mitteametlik), mida haldavad Samourai kasutajad saatjate ja kaastöötajate ühendamiseks: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Uuri lähemalt Stonewall tehingute kohta**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Mis on Stonewall x2 tehingu eesmärk?

Stonewall x2 struktuur lisab tehingule olulise hulga entroopiat ja segab ahela analüüsi. Väljastpoolt vaadates võib sellist tehingut tõlgendada kui väikest Coinjoin'i kahe isiku vahel. Kuid tegelikkuses on see makse. See meetod tekitab ahela analüüsis ebakindlust ja isegi viib valedeni.

Tagasi pöördudes Alice'i, Bobi ja Pagari näite juurde. Tehing plokiahelas näeks välja selline:
![stonewall x2 public](assets/en/3.webp)
Väline vaatleja, kes tugineb levinud ahela analüüsi heuristikatele, võib ekslikult järeldada, et "Alice ja Bob sooritasid väikese coinjoin'i, kus mõlemal oli sisendina üks UTXO ja väljundina kaks UTXO-d."![väär tõlgendus stonewall x2](assets/en/4.webp)See tõlgendus on vale, sest nagu te teate, saadeti UTXO Bakerile, Alicel on ainult üks vahetusväljund ja Bobil on kaks.
![tehing stonewall x2](assets/en/1.webp)
Isegi kui väline vaatleja suudab tuvastada Stonewall x2 tehingu mustrit, ei oma nad kogu informatsiooni. Nad ei suuda kindlaks teha, kumb kahest samas summas UTXO-st vastab maksele. Lisaks ei saa nad teada, kas makse tegi Alice või Bob. Lõpuks ei suuda nad kindlaks teha, kas kaks sisend-UTXO-d pärinevad kahest erinevast inimesest või kuuluvad need ühele inimesele, kes need ühendas. Viimane punkt tuleneb asjaolust, et klassikalised Stonewall tehingud, millest me eespool rääkisime, järgivad täpselt sama mustrit nagu Stonewall x2 tehingud. Väljastpoolt ja ilma konteksti lisainfota on võimatu eristada Stonewall tehingut Stonewall x2 tehingust. Siiski, esimesed ei ole koostöö tehingud, samas kui viimased on. See lisab veelgi kahtlusi selle kulu kohta.
![Stonewall või Stonewall x2 ?](assets/en/5.webp)

## Kuidas luua ühendust Paynymide vahel, et saaks koostööd teha Sorobani kaudu?

Nagu teiste koostöö tehingute puhul Samourais (*Cahoots*), hõlmab Stonewall x2 sooritamine osaliselt allkirjastatud tehingute vahetamist saatja ja kaastöötaja vahel. Vahetus võib toimuda käsitsi, juhul kui olete füüsiliselt oma kaastöötajaga koos, või automaatselt läbi Sorobani suhtlusprotokolli.

Kui valite teise võimaluse, peate enne Stonewall x2 sooritamist looma ühenduse Paynymide vahel. Selleks peab teie Paynym "järgima" teie kaastöötaja Paynymi ja vastupidi.

**Kaastöötaja Paynymi juurdepääs:**

Alustuseks on vajalik saada oma kaastöötaja Paynymi maksekood. Samourai Wallet rakenduses peab teie kaastöötaja vajutama oma Paynymi ikoonile (väike robot), mis asub ekraani ülaosas vasakul, seejärel klõpsama oma Paynymi hüüdnimele, mis algab `+...`. Näiteks minu oma on `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Kui teie kaastöötaja kasutab Sparrow Walletit, peaksid nad klõpsama vahekaardil 'Tools', seejärel 'Show PayNym'.![paynym sparrow](assets/notext/7.webp)
**Järgige oma kaastöötaja PayNymi Samourai Walletis:**

Kui kasutate Samourai Walletit, käivitage rakendus ja pääsege juurde 'PayNyms' menüüle samal viisil. Kui kasutate oma PayNymi esimest korda, peate hankima selle identifikaatori.

![taotle paynym samourai](assets/notext/8.webp)

Seejärel klõpsake ekraani paremas alanurgas sinisel '+'.
![lisa kaastöötaja paynym](assets/notext/9.webp)
Seejärel saate kleepida oma kaastöötaja maksekoodi, valides 'PASTE PAYMENT CODE', või avada kaamera nende QR-koodi skaneerimiseks, vajutades 'SCAN QR CODE'.
![paste paynym identifier](assets/notext/10.webp)
Klõpsake nupul 'JÄLGI'.
![follow paynym](assets/notext/11.webp)
Kinnitage, klõpsates 'JAH'.
![confirm follow paynym](assets/notext/12.webp)
Seejärel pakub tarkvara teile 'ÜHENDA' nuppu. Meie õpetuse jaoks ei ole vajalik seda nuppu klõpsata. See samm on vajalik ainult juhul, kui plaanite teha makseid teisele PayNym'ile osana [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)-st, mis ei ole meie õpetusega seotud.
![connect paynym](assets/notext/13.webp)
Kui teie PayNym jälgib teie koostööpartneri PayNym'i, korrake seda protsessi vastupidises suunas, et ka teie koostööpartner saaks teid jälgida. Seejärel saate teostada Stonewall x2 tehingu.

**Kuidas jälgida oma koostööpartneri PayNym'i Sparrow Wallet'is:**

Kui kasutate Sparrow Wallet'i, avage oma rahakott ja pääsete juurde menüüle 'Näita PayNym'i'. Kui kasutate oma PayNym'i esimest korda, peate identifikaatori saamiseks klõpsama 'Hangi PayNym'.
![request paynym sparrow](assets/notext/14.webp)
Seejärel sisestage oma koostööpartneri PayNym'i identifikaator (kas nende hüüdnimi '+...' või nende maksekood 'PM...') lahtrisse 'Leia Kontakt' ja klõpsake nupul 'Lisa Kontakt'.
![add contact paynym](assets/notext/15.webp)
Seejärel pakub tarkvara teile 'Link Kontakt' nuppu. Meie õpetuse jaoks ei ole vajalik seda nuppu klõpsata. See samm on vajalik ainult juhul, kui plaanite teha makseid näidatud PayNym'ile osana [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)-st, mis ei ole meie õpetusega seotud.

Kui teie PayNym jälgib teie koostööpartneri PayNym'i, korrake seda protsessi vastupidises suunas, et ka teie koostööpartner saaks teid jälgida. Seejärel saate teostada Stonewall x2 tehingu.
## Kuidas teha Stonewall x2 tehingut Samourai Wallet'is?

Kui olete eelnevad sammud Paynymide ühendamiseks lõpetanud, olete lõpuks valmis tegema Stonewall x2 tehingu! Selleks järgige meie videoõpetust Samourai Wallet'is:
![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Kuidas teha Stonewall x2 tehingut Sparrow Wallet'is?

Kui olete eelnevad sammud Paynymide ühendamiseks lõpetanud, olete lõpuks valmis tegema Stonewall x2 tehingu! Selleks järgige meie videoõpetust Sparrow Wallet'is:
![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Välised ressursid:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.