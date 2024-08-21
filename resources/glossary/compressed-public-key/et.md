---
term: KOMPRESSITUD AVALIK VÕTI
---

Avalikku võtit kasutatakse skriptides (kas otseselt avaliku võtme kujul või aadressina), et vastu võtta ja turvata bitcoine. Toores avalik võti esindab punkti elliptilisel kõveral, koosnedes kahest koordinaadist (`x, y`), millest igaüks on 256 bitti. Toores formaadis on avaliku võtme suurus seega 512 bitti, lisaks veel üks bait formaadi tuvastamiseks. Kompressitud avalik võti seevastu on avaliku võtme esituse kompaktsem vorm. See kasutab ainult `x` koordinaati ja prefiksit (`02` või `03`), mis näitab `y` koordinaadi paarsust (paaritu või paaritu).

Kui lihtsustada seda reaalarvude valdkonda, arvestades, et elliptiline kõver on sümmeetriline x-telje suhtes, siis iga punkti $P$ (`x, y`) korral kõveral, eksisteerib punkt $P'$ (`x, -y`), mis samuti asub sellel samal kõveral. See tähendab, et iga `x` korral on ainult kaks võimalikku `y` väärtust, positiivne ja negatiivne. Näiteks, antud abskissa `x` korral, oleks elliptilisel kõveral kaks punkti $P1$ ja $P2$, jagades sama abskissat, kuid vastandlike ordinaatidega:

![](../../dictionnaire/assets/29.png)
Kahe potentsiaalse punkti vahel kõveral valimiseks lisatakse `x`-le prefiks, mis täpsustab, millist `y` valida. See meetod võimaldab vähendada avaliku võtme suurust 520 bitilt ainult 264 bitile (8 biti prefiks + 256 biti `x` jaoks). Seda esitust tuntakse avaliku võtme kompressitud vormina.

Siiski, elliptilise kõvera krüptograafia kontekstis, ei kasutata reaalarve, vaid lõplikku välja järjekorraga `p` (algarv). Selles kontekstis määratakse `y` "märk" selle paarsuse järgi, st kas `y` on paaris või paaritu. Prefiks `0x02` näitab siis paaris `y`, samal ajal kui `0x03` näitab paaritut `y`.

Vaatle järgmist näidet toorest avalikust võtmest (punkt elliptilisel kõveral) heksadesimaalselt:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Me saame eraldada prefiksi, `x` ja `y`:
```plaintext
Prefiks = 04
`y` paarsuse määramiseks uurime `y` viimast heksadesimaalset tähemärki:
```plaintext
Baas 16 (heksadesimaalne): f
Baas 10 (kümnendsüsteem): 15
y on paaritu
```

Kompressitud avaliku võtme prefiksiks saab `03`. Kompressitud avalik võti heksadesimaalselt muutub:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```