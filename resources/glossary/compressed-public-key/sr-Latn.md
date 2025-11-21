---
term: KOMPRESOVANI JAVNI KLJUČ
---

Javni ključ se koristi u skriptama (bilo direktno u obliku javnog ključa ili kao Address) za primanje i osiguranje bitkoina. Sirovi javni ključ je predstavljen tačkom na eliptičnoj krivi, koja se sastoji od dve koordinate (`x, y`), svaka od 256 bita. U sirovom formatu, javni ključ stoga meri 512 bita, ne računajući dodatni bajt za identifikaciju formata. Kompresovani javni ključ, s druge strane, je kompaktniji oblik predstavljanja javnog ključa. Koristi samo `x` koordinatu i prefiks (`02` ili `03`) koji označava paritet `y` koordinate (paran ili neparan).


Ako ovo pojednostavimo na polje realnih brojeva, s obzirom da je eliptična kriva simetrična u odnosu na x-osu, za bilo koju tačku $P$ (`x, y`) na krivi, postoji tačka $P'$ (`x, -y`) koja će takođe biti na istoj krivi. To znači da za svaku `x` postoje samo dve moguće vrednosti `y`, pozitivna i negativna. Na primer, za datu apscisu `x`, postojale bi dve tačke $P1$ i $P2$ na eliptičnoj krivi, koje dele istu apscisu, ali sa suprotnim ordinatama:


![](../../dictionnaire/assets/29.webp)

Da bi se izabrala između dve potencijalne tačke na krivi, prefiks koji specificira koji `y` da se izabere dodaje se `x`. Ova metoda omogućava smanjenje veličine javnog ključa sa 520 bita na samo 264 bita (8 bita prefiksa + 256 bita za `x`). Ova reprezentacija je poznata kao kompresovani oblik javnog ključa.


Međutim, u kontekstu kriptografije eliptičnih krivih, ne koristimo realne brojeve, već konačno polje reda `p` (prosti broj). U ovom kontekstu, "znak" `y` određuje se njegovom parnošću, tj. da li je `y` paran ili neparan. Prefiks `0x02` tada označava paran `y`, dok `0x03` označava neparan `y`.


Razmotrite sledeći primer sirovog javnog ključa (tačka na eliptičnoj krivi) u heksadecimalnom formatu:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Možemo izolovati prefiks, `x`, i `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Baza 16 (heksadecimalno): f

Baza 10 (decimalni): 15

y je neparan

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```