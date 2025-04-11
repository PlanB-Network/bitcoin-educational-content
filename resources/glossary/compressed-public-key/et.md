---
term: KOKKUSURUTUD AVALIK VÕTI

---
Avalikku võtit kasutatakse skriptides (kas otse avaliku võtme või aadressi kujul) bitcoinide vastuvõtmiseks ja kaitsmiseks. Toores avalik võti on kujutatud punktina elliptilisel kõveral, mis koosneb kahest koordinaadist (`x, y`), millest igaühe pikkus on 256 bitti. Toorformaadis on avaliku võtme pikkus seega 512 bitti, arvestamata täiendavat baiti formaadi identifitseerimiseks. Pakitud avalik võti on seevastu avaliku võtme kompaktsem esitusviis. See kasutab ainult koordinaati "x" ja eesliidet ("02" või "03"), mis näitab "y" koordinaadi pariteeti (paariline või paaritu).

Kui me lihtsustame seda reaalarvude väljale, siis arvestades, et elliptiline kõver on sümmeetriline x-telje suhtes, siis iga punkti $P$ (`x, y`) kohta kõveral on olemas punkt $P'$ (`x, -y`), mis asub samuti sellel samal kõveral. See tähendab, et iga `x` jaoks on ainult kaks võimalikku `y` väärtust, positiivne ja negatiivne. Näiteks on antud absissil `x` elliptilisel kõveral kaks punkti $P1$ ja $P2$, millel on sama absiss, kuid mille ordinaadid on vastupidised:

![](../../dictionnaire/assets/29.webp)

Selleks, et valida kahe võimaliku punkti vahel kõveral, lisatakse `x`-le eesliide, mis määrab, milline `y` valida. See meetod võimaldab vähendada avaliku võtme suurust 520 bitilt ainult 264 bitini (8 bitti eesliidet + 256 bitti `x` jaoks). Sellist esitusviisi nimetatakse avaliku võtme tihendatud vormiks.

Elliptiliste kõverate krüptograafia kontekstis ei kasuta me siiski reaalarvu, vaid lõplikku välja järjekorranumbriga "p" (algarv). Selles kontekstis määratakse `y` märk kindlaks selle pariteediga, st kas `y` on paariline või paaritu. Eesliide `0x02` tähistab siis paarilist `y`, samas kui `0x03` tähistab paaritu `y`.

Vaadake järgmist näidet toorest avalikust võtmest (punkt elliptilisel kõveral) heksakomaalses kirjas:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Me võime eraldada eesliite `x` ja `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Baas 16 (heksadekaal): f

Alus 10 (kümnendmõõdustik): 15

y on paaritu

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```