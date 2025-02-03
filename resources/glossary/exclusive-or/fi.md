---
term: EXCLUSIVE OR

---
Boolen logiikan perustehtävä. Eksklusiivinen tai XOR ("*Exclusive or*") ottaa kaksi Boolen operandia, joista kumpikin on tosi tai epätosi, ja tuottaa tosi tuloksen vain silloin, kun nämä kaksi operandia eroavat toisistaan. Toisin sanoen `XOR`-operaation tulos on tosi, jos täsmälleen toinen (mutta eivät molemmat) operandeista on tosi. Esimerkiksi `XOR`-operaation tuloksena on `1` ja `0` välillä `1`. Huomaa: $1 \oplus 0 = 1$. Vastaavasti `XOR`-operaatio voidaan suorittaa pidemmille bittisarjoille. Esimerkiksi: $10110 \oplus 01110 = 11000$. Sarjan jokaista bittiä verrataan sen vastaavaan ja suoritetaan `XOR`-operaatio. Tässä on `XOR`-operaation totuustaulukko:

<div align="center">

| $A$ | $B$ | $A \oplus B$ | $A \plus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

XOR-operaatiota käytetään monilla tietojenkäsittelytieteen aloilla, erityisesti kryptografiassa, sen mielenkiintoisten ominaisuuksien vuoksi, kuten:


- Sen kommutatiivisuus: operandien järjestys ei vaikuta tulokseen. Kahden muuttujan $D$ ja $E$ tapauksessa: $D \oplus E = E \oplus D$;
- Sen assosiatiivisuus: operandien ryhmittely ei vaikuta tulokseen. Kolmelle muuttujalle $A$, $B$ ja $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Sillä on neutraali elementti `0`: operandi, joka on xored 0:lla, on aina yhtä suuri kuin operandi. Tietylle muuttujalle $A$: $A \oplus 0 = A$;
- Jokainen elementti on oma käänteislukunsa. Tietylle muuttujalle $A$: $A \oplus A = 0$.

Bitcoinin yhteydessä `XOR`-operaatiota käytetään ilmeisesti monissa paikoissa. Esimerkiksi `XOR`-operaatiota käytetään massiivisesti `SHA256`-funktiossa, jota käytetään laajasti Bitcoin-protokollassa. Jotkin protokollat, kuten Coldcardin *SeedXOR*, käyttävät tätä primitiiviä myös muissa sovelluksissa. Se esiintyy myös BIP47:ssä uudelleenkäytettävän maksukoodin salaamiseen sen siirron aikana.

Laajemmalla kryptografian alalla `XOR` voidaan käyttää sellaisenaan symmetrisenä salausalgoritmina. Tätä algoritmia kutsutaan nimellä "One-Time Pad" tai "Vernam Cipher", joka on nimetty sen keksijän mukaan. Vaikka tämä algoritmi on epäkäytännöllinen avaimen pituuden vuoksi, se on yksi ainoista ehdoitta turvalliseksi tunnustetuista salausalgoritmeista.