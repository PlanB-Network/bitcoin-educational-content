---
term: XOR

---
Toiminnon "Exclusive or" lyhenne, ranskaksi "Ou exclusif" Se on Boolen logiikan perustoiminto. Tämä operaatio ottaa kaksi Boolen operandia, joista kumpikin on $true$ tai $false$, ja tuottaa tuloksen $true$ vain silloin, kun nämä kaksi operandia eroavat toisistaan. Toisin sanoen XOR-operaation tulos on $true$, jos täsmälleen toinen (mutta eivät molemmat) operandeista on $true$. Esimerkiksi $1$:n ja $0$:n välinen XOR-operaatio antaa tulokseksi $1$. Huom:

$$
1 \oplus 0 = 1
$$

Vastaavasti XOR-operaatio voidaan suorittaa pidemmille bittisarjoille. Esimerkiksi:

$$
10110 \oplus 01110 = 11000
$$

Sarjan jokaista bittiä verrataan sen vastakappaleeseen ja suoritetaan XOR-operaatio. Tässä on XOR-operaation totuustaulukko:

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
- Sillä on neutraali elementti $0$: operandi, joka on xored $0$:lla, on aina yhtä suuri kuin operandi. Tietylle muuttujalle $A$: $A \oplus 0 = A$;
- Jokainen elementti on oma käänteislukunsa. Tietylle muuttujalle $A$: $A \oplus A = 0$.

Bitcoinin yhteydessä XOR-operaatiota käytetään ilmeisesti monissa paikoissa. XOR-operaatiota käytetään esimerkiksi laajasti SHA256-funktiossa, jota käytetään laajasti Bitcoin-protokollassa. Jotkin protokollat, kuten Coldcardin *SeedXOR*, käyttävät tätä primitiiviä myös muissa sovelluksissa. Se esiintyy myös BIP47:ssä uudelleenkäytettävän maksukoodin salaamiseen sen siirron aikana.

Laajemmalla kryptografian alalla XOR:ia voidaan käyttää sellaisenaan symmetrisenä salausalgoritmina. Tätä algoritmia kutsutaan nimellä "One-Time Pad" tai "Vernam Cipher", joka on nimetty sen keksijän mukaan. Vaikka tämä algoritmi on epäkäytännöllinen avaimen pituuden vuoksi, se on yksi ainoista ehdoitta turvalliseksi tunnustetuista salausalgoritmeista.