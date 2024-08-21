---
termi: LABEL (HILJAISET MAKSUT)
---

Hiljaisten Maksujen protokollassa tunnisteet ovat kokonaislukuja, joita käytetään alkuperäisen staattisen osoitteen muokkaamiseen luomaan muita staattisia osoitteita. Näiden tunnisteiden käyttö mahdollistaa maksujen erottelun Hiljaisten Maksujen kautta lähettäessä, käyttämällä eri staattisia osoitteita kullekin käyttötarkoitukselle, ilman että operatiivinen taakka näiden maksujen havaitsemiseksi (skannaus) kasvaa liikaa. Bob käyttää staattista osoitetta $B$, joka koostuu kahdesta julkisesta avaimesta: $B_{\text{scan}}$ skannausta varten ja $B_{\text{spend}}$ kuluttamista varten. $b_{\text{scan}}$:n hasha ja kokonaisluku $m$, skalaarikertolaskettuna generaattoripisteellä $G$, lisätään kulutusjulkiseen avaimen $B_{\text{spend}}$ luomaan eräänlainen uusi kulutusjulkinen avain $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Esimerkiksi ensimmäinen avain $B_1$ saadaan tällä tavalla:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Bobin julkaisema staattinen osoite koostuu nyt $B_{\text{scan}}$:sta ja $B_m$:stä. Esimerkiksi ensimmäinen staattinen osoite tunnisteella $1$ on:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Aloitamme vain tunnisteesta $1$, koska tunniste $0$ on varattu vaihtorahalle. Alice, joka haluaa lähettää bitcoineja Bobin tarjoamaan tunnistettuun staattiseen osoitteeseen, johdattaa uniikin maksuosoitteen $P_0$ käyttäen uutta $B_1$:ä $B_{\text{spend}}$:n sijaan:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Todellisuudessa Alice ei ehkä edes tiedä, että Bobilla on tunnistettu osoite, sillä hän yksinkertaisesti käyttää staattisen osoitteen toista osaa, joka tässä tapauksessa on arvo $B_1$ eikä $B_{\text{spend}}$. Maksujen skannaukseen Bob käyttää aina alkuperäisen staattisen osoitteensa arvoa $B_{\text{spend}}$ tällä tavalla:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Sitten hän yksinkertaisesti vähentää löytämänsä arvon $P_0$ jokaisesta lähdöstä yksi kerrallaan. Sen jälkeen hän tarkistaa, vastaako yhden näistä vähennyksistä tulos yhtä hänen lompakossaan käyttämistä tunnisteista. Jos se vastaa, esimerkiksi lähtö #4 tunnisteella $1$, tämä tarkoittaa, että tämä lähtö on Hiljainen Maksu, joka on yhdistetty hänen tunnistettuun staattiseen osoitteeseensa $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Tämä toimii, koska:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Tämän menetelmän ansiosta Bob voi käyttää useita staattisia osoitteita ($B_1$, $B_2$, $B_3$...), jotka kaikki on johdettu hänen perusstaattisesta osoitteestaan ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), jotta hän voi erottaa käyttötarkoitukset asianmukaisesti.

Kuitenkin tämä staattisten osoitteiden erottelu on pätevää vain henkilökohtaisesta lompakonhallinnan näkökulmasta, mutta se ei mahdollista identiteettien erottelua. Koska kaikilla on sama $B_{\text{scan}}$, on erittäin helppoa yhdistää kaikki staattiset osoitteet yhteen ja päätellä, että ne kuuluvat yhdelle entiteetille.