---
termi: EXCLUSIVE OR
---

Perustava toiminto Boolen logiikassa. "Yksinomainen tai" eli XOR ("*Exclusive or*") ottaa kaksi Boolen operandia, jotka kumpikin ovat tosi tai epätosi, ja tuottaa todenmukaisen tuloksen vain, kun kaksi operandia eroavat toisistaan. Toisin sanoen, `XOR`-operaation tulos on tosi, jos tarkalleen yksi (mutta ei molemmat) operandeista on tosi. Esimerkiksi `XOR`-operaatio `1` ja `0` välillä tuottaa tuloksen `1`. Huomataan: $1 \oplus 0 = 1$. Samoin `XOR`-operaatiota voidaan suorittaa pidemmillä bittijonoilla. Esimerkiksi, $10110 \oplus 01110 = 11000$. Jokainen bittijonon bitti verrataan vastaavaansa, ja `XOR`-operaatio sovelletaan. Tässä on totuustaulukko `XOR`-operaatiolle:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

`XOR`-operaatiota käytetään monilla tietojenkäsittelytieteen alueilla, erityisesti kryptografiassa, sen mielenkiintoisten ominaisuuksien vuoksi, kuten:
* Sen kommutatiivisuus: operandien järjestys ei vaikuta tulokseen. Kahdelle annetulle muuttujalle $D$ ja $E$: $D \oplus E = E \oplus D$;
* Sen assosiatiivisuus: operandien ryhmittely ei vaikuta tulokseen. Kolmelle annetulle muuttujalle $A$, $B$ ja $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Sillä on neutraali elementti `0`: operandi xorattuna 0:n kanssa on aina yhtä suuri kuin operandi. Annetulle muuttujalle $A$: $A \oplus 0 = A$;
* Jokainen elementti on oma inversionsa. Annetulle muuttujalle $A$: $A \oplus A = 0$.

Bitcoinin kontekstissa `XOR`-operaatiota käytetään ilmeisesti monissa paikoissa. Esimerkiksi `XOR` on massiivisesti käytössä `SHA256`-funktiossa, jota käytetään laajalti Bitcoin-protokollassa. Jotkin protokollat, kuten Coldcardin *SeedXOR*, käyttävät tätä primitiiviä myös muihin sovelluksiin. Sitä löytyy myös BIP47:ssä salatessa uudelleenkäytettävää maksukoodia sen siirron aikana.
Laajemmassa kryptografian kentässä `XOR` voidaan käyttää sellaisenaan symmetrisenä salausalgoritmina. Tätä algoritmia kutsutaan "Kertakäyttöavaimen" tai "Vernamin salakirjoitukseksi", nimetty keksijänsä mukaan. Vaikka käytännössä epäkäytännöllinen avaimen pituuden vuoksi, tämä algoritmi on yksi harvoista salausalgoritmeista, jotka tunnustetaan ehdottomasti turvallisiksi.