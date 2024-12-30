---
name: Boltzmanni Kalkulaator
description: Mõista entroopia kontseptsiooni ja kuidas Boltzmanni kasutada
---
![kaas](assets/cover.webp)

***HOIATUS:** Pärast Samourai Walleti asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil on KYCP.org veebileht praegu kättesaamatu. Gitlab, mis hostis Pythoni Boltzmanni Kalkulaatori koodi, on samuti konfiskeeritud. Praeguse seisuga ei ole võimalik seda tööriista alla laadida. Siiski on võimalik, et kood võidakse järgnevate nädalate jooksul teiste poolt uuesti avaldada. Vahepeal saate siiski sellest õpetusest kasu, et mõista Boltzmanni Kalkulaatori toimimist. Selle tööriista poolt pakutavad näitajad kehtivad igale Bitcoin tehingule ja neid saab samuti käsitsi arvutada. Ma annan selles õpetuses kõik vajalikud arvutused. Kui olete juba alla laadinud Pythoni tööriista oma masinasse või kasutate RoninDojo, võite tööriista kasutamist ja selle õpetuse järgimist jätkata nagu tavaliselt, see töötab endiselt.*

_Me jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Olge kindlad, et me uuendame seda õpetust, kui saadaval on uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

Boltzmanni Kalkulaator on tööriist Bitcoin tehingu analüüsimiseks, mõõtes selle entroopia taset koos teiste edasijõudnute näitajatega. See pakub ülevaadet tehingu sisendite ja väljundite vahelistest seostest. Need näitajad pakuvad kvantifitseeritud hinnangut tehingu privaatsusele ja aitavad tuvastada võimalikke vigu.

Selle Pythoni tööriista arendasid Samourai Walleti ja OXT meeskonnad, kuid seda saab kasutada mis tahes Bitcoin tehingul.

## Kuidas kasutada Boltzmanni Kalkulaatorit?
Boltzmanni Kalkulaatori kasutamiseks on teile kaks võimalust. Esimene on installida Pythoni tööriist otse oma masinasse. Alternatiivina võite valida KYCP.org (_Know Your Coin Privacy_) veebilehe, mis pakub lihtsustatud kasutusplatvormi. [RoninDojo](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8) kasutajatele, pange tähele, et see tööriist on juba teie sõlme integreeritud.

KYCP lehe kasutamine on üsna lihtne: sisestage lihtsalt analüüsida soovitud tehingu identifikaator (TXID) otsinguribale ja vajutage `ENTER`.
![KYCP](assets/1.webp)
Seejärel leiate erinevat teavet tehingu kohta, sealhulgas sisendite ja väljundite vahelised seosed. Klõpsake `deterministlikud seosed`.
![KYCP](assets/2.webp)
Jõuate lehele, mis on pühendatud Boltzmanni Kalkulaatori näitajatele.
![KYCP](assets/3.webp)
Neile, kes eelistavad tööriista kasutada otse oma RoninDojo sõlmest, on see kättesaadav kaudu `RoninCLI > Samourai Toolkit > Boltzmanni Kalkulaator`.

Nagu KYCP.org lehel, kui Pythoni tööriist on installitud, peate lihtsalt kleepima tehingu TXID, mida soovite analüüsida.

![KYCP](assets/7.webp)

Seejärel vajutage tulemuste saamiseks `ENTER` klahvi.

![KYCP](assets/8.webp)

## Mis on Boltzmanni Kalkulaatori näitajad?
### Kombinatsioonid / Tõlgendused:
Esimene näitaja, mida tarkvara arvutab, on võimalike kombinatsioonide koguarv, mida näidatakse tööriistas `nb combinations` või `interpretations` all.
Arvestades tehingus osalevate UTXO-de väärtusi, arvutab see indikaator sisendite ja väljundite seostamise võimalike viiside arvu. Teisisõnu, see määrab, mitu usutavat tõlgendust võib tehing välisvaatleja analüüsi perspektiivist esile kutsuda. Näiteks, coinjoin, mis on struktureeritud vastavalt Whirlpool 5x5 mudelile, esitab `1,496` võimalikku kombinatsiooni: ![KYCP](assets/4.webp)
Teisest küljest, Whirlpool Surge Cycle 8x8 coinjoin esitab `9,934,563` võimalikku tõlgendust: ![KYCP](assets/5.webp)
Vastandina, traditsioonilisem tehing 1 sisendiga ja 2 väljundiga esitab ainult ühe tõlgenduse: ![KYCP](assets/6.webp)

### Entroopia:
Teine arvutatav indikaator on tehingu entroopia, mida tähistatakse kui `Entropy`.

Üldises krüptograafia ja informatsiooni kontekstis on entroopia kvantitatiivne mõõt ebakindluse või ettearvamatuse kohta, mis on seotud andmeallika või juhusliku protsessiga. Teisisõnu, entroopia on viis mõõta, kui raske on informatsiooni ennustada või ära arvata.

Spetsiifilises ahela analüüsi kontekstis on entroopia samuti indikaatori nimi, mis on tuletatud Shannoni entroopiast ja [leiutatud LaurentMT poolt](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), mida arvutatakse Boltzmanni tööriistaga.

Kui tehing esitab suure hulga võimalikke kombinatsioone, on sageli asjakohasem viidata selle entroopiale. See indikaator võimaldab mõõta analüütikute teadmiste puudumist tehingu täpse konfiguratsiooni kohta. Teisisõnu, mida suurem on entroopia, seda raskem on analüütikutel tuvastada bitcoini liikumisi sisendite ja väljundite vahel.

Praktikas paljastab entroopia, kas tehing esitab välisvaatleja perspektiivist mitmeid võimalikke tõlgendusi, tuginedes ainult sisendite ja väljundite summadele, ilma teiste väliste või sisemiste mustrite ja heuristikate arvestamiseta. Kõrge entroopia on seega sünonüüm tehingu paremale konfidentsiaalsusele.

Entroopia on määratletud kui võimalike kombinatsioonide arvu binaarlogaritm. Siin on kasutatav valem:
```plaintext
E: tehingu entroopia
C: tehingu võimalike kombinatsioonide arv

E = log2(C)
```

Matemaatikas vastab binaarlogaritm (alus-2 logaritm) 2 eksponenteerimise pöördoperatsioonile. Teisisõnu, `x` binaarlogaritm on eksponent, millele `2` tuleb tõsta, et saada `x`. See indikaator väljendatakse seega bittides.

Võtame näiteks entroopia arvutamise coinjoin tehingu jaoks, mis on struktureeritud vastavalt Whirlpool 5x5 mudelile, mis, nagu varem mainitud, pakub `1,496` võimalikku kombinatsiooni:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bitti
```
Seega kuvab see coinjoin tehing entroopiat `10.5469 bitti`, mis on peetud väga rahuldavaks. Mida kõrgem see väärtus, seda rohkem erinevaid tõlgendusi tehing lubab, tugevdades seeläbi selle privaatsuse taset.
8x8 coinjoin tehingu puhul, mis esitab `9,934,563` tõlgendust, oleks entroopia:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bitti
```
Vaatame veel ühte näidet tavapärasema tehinguga, mis sisaldab ühte sisendit ja kahte väljundit: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Selles tehingujuhtumis on ainus võimalik tõlgendus: `(Sis.0) > (Väl.0 ; Väl.1)`. Seega on selle entroopia määratletud kui `0`:```plaintext
C = 1
E = log2(1)
E = 0 bitti
```

### Efektiivsus:
Boltzmanni kalkulaatori kolmas näitaja kannab nime `Rahakoti Efektiivsus`. See näitaja hindab tehingu efektiivsust, võrreldes seda optimaalse tehinguga identse konfiguratsiooniga.

See viib meid aruteluni maksimaalse entroopia mõiste üle, mis vastab kõrgeimale entroopiale, mida konkreetne tehingustruktuur teoreetiliselt saavutada võiks. Tehingu efektiivsus arvutatakse seejärel, võrreldes seda maksimaalset entroopiat analüüsitava tehingu tegeliku entroopiaga.

Kasutatav valem on järgmine:
```plaintext
ER: tehingu tegelik entroopia, väljendatuna bittides
EM: antud tehingustruktuuri maksimaalne võimalik entroopia, väljendatuna bittides
Ef: tehingu efektiivsus bittides

Ef = ER - EM
```

Näiteks Whirlpool 5x5 tüüpi coinjoin struktuuri puhul on maksimaalne entroopia määratud kui `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bitti
```

See näitaja väljendatakse ka protsendina, selle valem on siis:
```plaintext
CR: tegelik võimalike kombinatsioonide arv
CM: maksimaalne võimalike kombinatsioonide arv sama struktuuriga
Ef: efektiivsus väljendatuna protsendina

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Efektiivsus `100%` näitab seega, et tehing maksimeerib oma privaatsuse potentsiaali vastavalt oma struktuurile.

### Entroopia Tihedus:
Neljas näitaja on entroopia tihedus, mida tööriistas märgitakse kui `Entroopia Tihedus`. See pakub perspektiivi entroopia kohta suhteliselt iga sisendi või väljundi kohta tehingus. See näitaja osutub kasulikuks tehingute efektiivsuse hindamisel ja võrdlemisel erineva suurusega. Selle arvutamiseks jagage lihtsalt tehingu koguentroopia sisendite ja väljundite koguarvuga:
```plaintext
ED: entroopia tihedus, väljendatuna bittides
E: tehingu entroopia, väljendatuna bittides
T: tehingus osalevate sisendite ja väljundite koguarv

ED = E / T
```

Võtame näiteks Whirlpool 5x5 coinjoini:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bitti
```

Arvutame ka entroopia tiheduse Whirlpool 8x8 coinjoini jaoks:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bitti
```

### Boltzmanni Skoor:
Boltzmanni kalkulaatori poolt edastatud viies teave on sisendite ja väljundite vaheliste vastavusvõimaluste tabel. See tabel näitab Boltzmanni skoori kaudu tingimuslikku tõenäosust, et kindel sisend on seotud antud väljundiga.
Seega on see tingimusliku tõenäosuse kvantitatiivne mõõt, et sisendi ja väljundi vaheline seos tehingus esineb, põhinedes soodsate sündmuste arvu suhtele kõigi võimalike sündmuste arvuga tõlgenduste kogumis.

Võttes taas näiteks Whirlpooli coinjoin'i, toob tingimuslike tõenäosuste tabel esile iga sisendi ja väljundi vahelise seose tõenäosused, pakkudes tehingu seoste ebamäärasuse kvantitatiivset mõõtu:

| %       | Väljund 0 | Väljund 1 | Väljund 2 | Väljund 3 | Väljund 4 |
| ------- | --------- | --------- | --------- | --------- | --------- |
| Sisend 0 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 1 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 2 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 3 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Sisend 4 | 34%       | 34%       | 34%       | 34%       | 34%       |

Siin näeme selgelt, et igal sisendil on võrdne võimalus olla seotud mis tahes väljundiga, mis suurendab tehingu konfidentsiaalsust.
Boltzmanni skoori arvutamine hõlmab teatud sündmuse esinemise interpretatsioonide arvu jagamist saadaolevate interpretatsioonide koguarvuga. Seega, et määrata skoor, mis seostab sisendi nr 0 väljundiga nr 3 (`512` interpretatsiooni), kasutatakse järgmist protseduuri:
```plaintext
Interpretatsioonid (IN.0 > OUT.3) = 512
Koguinterpretatsioonid = 1496
Skoor = 512 / 1496 = 34%
```

Võttes näiteks Whirlpooli 8x8 coinjoin'i (tõusu tsükkel), näeks Boltzmanni tabel välja selline:

|       | VÄL.0 | VÄL.1 | VÄL.2 | VÄL.3 | VÄL.4 | VÄL.5 | VÄL.6 | VÄL.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| SIS.0 | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| SIS.1 | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| SIS.2 | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| SIS.3 | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Siiski, lihtsa tehingu puhul, millel on üks sisend ja kaks väljundit, on olukord erinev:

| %       | Väljund 0 | Väljund 1 |
|---------|-----------|-----------|
| Sisend 0 | 100%      | 100%      |

Siin on täheldatud, et tõenäosus iga väljundi puhul, et see pärineb sisendist nr 0, on `100%`. Madalam tõenäosus tähendab seega suuremat privaatsust, lahjendades otseseid seoseid sisendite ja väljundite vahel.

### Deterministlikud Seosed:
Kuues esitatud teave on deterministlike seoste arv, mida täiendab nende seoste suhe. See näitaja paljastab, mitu ühendust analüüsitud tehingu sisendite ja väljundite vahel on vaieldamatud, tõenäosusega `100%`. Suhe seevastu pakub perspektiivi nende deterministlike seoste kaalust kogu tehingu seoste hulgas.
Näiteks Whirlpool-tüüpi coinjoin tehingul pole deterministlikke seoseid ja seetõttu kuvatakse näitaja ja suhe `0%`. Vastupidi, meie teises uuritud lihtsas tehingus (ühe sisendi ja kahe väljundiga) on näitaja määratud väärtusele `2` ja suhe jõuab `100%`ni. Seega nullnäitaja signaliseerib suurepärast konfidentsiaalsust tänu otsese ja vaieldamatute seoste puudumisele sisendite ja väljundite vahel.

**Välised Ressursid:**

- Boltzmanni kood Samourai peal
- [Bitcoin Tehingud & Privaatsus (Osa I) autorilt Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Tehingud & Privaatsus (Osa II) autorilt Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Tehingud & Privaatsus (Osa III) autorilt Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP Veebileht
- [Mediumi Artikkel Boltzmanni Skripti Tutvustusest autorilt Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)