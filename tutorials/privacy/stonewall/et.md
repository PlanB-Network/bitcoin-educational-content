---
name: Stonewall
description: Stonewall tehingute mõistmine ja kasutamine
---
![kaanepilt stonewall](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil nõuab Samourai Wallet'i rakenduse kasutamine nüüd oma Dojo'ga ühenduse loomist, et see korralikult toimiks. Sellest hoolimata ei mõjuta Stonewall tehinguid üldse ja neid saab endiselt probleemideta sooritada. Tegelikult viiakse sellised tehingud läbi autonoomselt, ilma vajaduseta väliste koostööde või Soroban kaudu ühenduse loomiseks.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Võite kindlad olla, et uuendame seda õpetust, kui uut teavet saadaval on._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *"Murra blockchaini analüüsi eeldused matemaatiliselt tõestatava kahtlusega saatja ja saaja vahel oma tehingutes."*

## Mis on Stonewall tehing?
Stonewall on spetsiifiline Bitcoin'i tehingu vorm, mille eesmärk on suurendada kasutaja privaatsust tehingu ajal, jäljendades kahe osapoole vahelist coinjoin'i, ilma et see tegelikult oleks. Tegelikult ei ole see tehing koostööaldis. Kasutaja saab selle ise koostada, kasutades sisenditena ainult oma UTXO-sid. Seega saate luua Stonewall tehingu igaks juhuks, ilma et peaksite koordineerima teise kasutajaga.

Stonewall tehingu toimimine on järgmine: sisendina kasutab saatja 2 UTXO-d, mis kuuluvad neile. Väljundina toodab tehing 4 väljundit, sealhulgas 2, mis on täpselt sama summa. Ülejäänud 2 on vahetusraha. Kahest samas summas väljundist läheb tegelikult maksesaajale ainult üks.

Stonewall tehingus on ainult 2 rolli:
- Saatja, kes teeb tegeliku makse;
- Saaja, kes võib olla tehingu spetsiifilisest olemusest teadmata ja lihtsalt ootab saatjalt makset.

Võtame näite, et mõista seda tehingu struktuuri. Alice on pagaripoes, et osta oma baguette, mis maksab `4,000 satsi`. Ta soovib maksta bitcoinides, säilitades teatud privaatsuse taseme oma makses. Seetõttu otsustab ta luua makse jaoks Stonewall tehingu.
![stonewall tehing pagaripoes](assets/en/1.webp)
Seda tehingut analüüsides näeme, et pagar sai tõepoolest `4,000 satsi` makse baguette eest. Alice kasutas sisenditena 2 UTXO-d: ühte `10,000 satsi` ja teist `15,000 satsi`. Väljundina sai ta 3 UTXO-d: ühe `4,000 satsi`, ühe `6,000 satsi` ja ühe `11,000 satsi`. Alice'i netosaldo selles tehingus on `-4,000 satsi`, mis vastab baguette hinnale.

Selles näites jätsin tahtlikult kaevandamistasud välja, et mõistmine oleks lihtsam. Tegelikkuses katab saatja kõik tehingutasud.

## Mis vahe on Stonewall ja Stonewall x2-l?
Stonewall tehing toimib samamoodi nagu StonewallX2 tehing, ainus erinevus seisneb selles, et viimane nõuab koostööd, erinevalt klassikalisest Stonewall tehingust, seega ka "x2" tähistus. Tõepoolest, Stonewall tehingu saab sooritada ilma välise koostööta: saatja saab selle läbi viia ilma teise isiku abita. Siiski, Stonewall x2 tehingu puhul, liitub protsessiga täiendav osaleja, keda nimetatakse "kaastöötajaks". Kaastöötaja lisab oma bitcoine sisendina saatja omade kõrvale ja saab väljundina kogu summa (miinus kaevandamistasud).

Vaadelgem uuesti meie näidet Alice'iga pagaripoes. Kui ta oleks tahtnud teha Stonewall x2 tehingu, oleks Alice pidanud looma tehingu koostöös Bobiga (kolmas osapool). Nad oleksid mõlemad andnud sisendi UTXO. Seejärel oleks Bob saanud oma sisendi täies ulatuses väljundina. Pagar oleks saanud oma bageti eest tasutud samamoodi nagu Stonewall tehingu puhul, samal ajal kui Alice oleks saanud oma algse saldo tagasi, miinus bageti maksumus.
![transaction stonewall x2](assets/en/2.webp)

Välisest vaatepunktist oleks tehingu muster jäänud täpselt samaks.
![Stonewall või Stonewall x2 ?](assets/en/3.webp)

Kokkuvõttes jagavad Stonewall ja Stonewall x2 tehingud identset struktuuri. Erinevus kahe vahel seisneb nende koostöölises olemuses. Stonewall tehing on välja töötatud individuaalselt, ilma koostöö vajaduseta. Seevastu Stonewall x2 tehing tugineb kahe isiku koostööle selle rakendamiseks.

[**-> Uuri lähemalt Stonewall x2 tehingute kohta**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Mis on Stonewall tehingu eesmärk?
Stonewall struktuur lisab tehingule olulise hulga entroopiat ja varjab ahela analüüsi. Välisest vaatepunktist võib sellist tehingut tõlgendada kui väikest coinjoin'i kahe inimese vahel. Kuid tegelikkuses, nagu ka Stonewall x2 tehingu puhul, on see makse. See meetod loob seega ahela analüüsis ebakindlusi ja võib isegi viia valede jälgedeni.

Vaadelgem uuesti Alice'i näidet pagaripoes. Blockchainis näeks tehing välja järgmiselt:
![Stonewall või Stonewall x2 ?](assets/en/4.webp)
Väline vaatleja, kes tugineb tavalistele ahela analüüsi heuristilistele meetoditele, võiks ekslikult järeldada, et "*kaks inimest on sooritanud väikese coinjoin'i, igaüks ühe UTXO sisendiga ja kaks UTXO-d väljundina*".
![Stonewall või Stonewall x2 ?](assets/en/5.webp)
See tõlgendus on vale, sest nagu te teate, saadeti UTXO pagarile, 2 UTXO-d sisendis tulid Alice'ilt ja ta sai 3 vahetusväljundit.

![transaction stonewall baker](assets/en/1.webp)
Isegi kui välisvaatleja suudab tuvastada Stonewall tehingu mustrit, ei oma nad kogu informatsiooni. Nad ei suuda kindlaks teha, kumb kahest sama summa UTXO-st vastab maksele. Lisaks ei suuda nad kindlaks teha, kas kaks sisendis olevat UTXO-d pärinevad kahest erinevast isikust või kuuluvad need ühele isikule, kes need ühendas. Viimane punkt tuleneb asjaolust, et Stonewall x2 tehingud, millest me eespool rääkisime, järgivad täpselt sama mustrit kui Stonewall tehingud. Väljastpoolt ja ilma lisainformatsioonita konteksti kohta on võimatu eristada Stonewall tehingut Stonewall x2 tehingust. Siiski, esimesed ei ole koostöö tehingud, samas kui viimased on. See lisab veelgi kahtlusi selle kulutuse üle.
![Stonewall või Stonewall x2?](assets/en/3.webp)
## Kuidas teha Stonewall tehingut Samourai Wallet'is?
Erinevalt Stowaway'st või Stonewall x2 (kaaslased) tehingutest, ei nõua Stonewall tehing Paynymide kasutamist. Seda saab teha otse, ilma ettevalmistusetappideta. Selleks järgige meie videoõpetust Samourai Wallet'is:
![Stonewall Õpetus - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Kuidas teha Stonewall tehingut Sparrow Wallet'is?
Erinevalt Stowaway'st või Stonewall x2 (kaaslased) tehingutest, ei nõua Stonewall tehing Paynymide kasutamist. Seda saab teha otse, ilma ettevalmistusetappideta. Selleks järgige meie videoõpetust Sparrow Wallet'is:
![Stonewall Õpetus - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)


**Välised Ressursid:**
- https://docs.samourai.io/en/spend-tools#stonewall.