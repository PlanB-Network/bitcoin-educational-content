---
term: (HILJAISET MAKSUT)

---
Hiljaiset maksut -protokollassa tunnisteet ovat kokonaislukuja, joita käytetään alkuperäisen staattisen osoitteen muuttamiseen monien muiden staattisten osoitteiden luomiseksi. Näiden tunnisteiden käyttö mahdollistaa hiljaisten maksujen kautta lähetettyjen maksujen erottelun käyttämällä eri staattisia osoitteita kutakin käyttöä varten ilman, että maksujen havaitsemiseen (skannaukseen) liittyvä operatiivinen taakka kasvaa kohtuuttomasti. Bob käyttää staattista osoitetta $B$, joka koostuu kahdesta julkisesta avaimesta: $B_{\text{scan}}$ skannausta varten ja $B_{\text{spend}}$ kuluttamista varten. Kulutuksen julkiseen avaimeen $B_{\text{scan}}$ lisätään $b_{\text{scan}}$:n ja kokonaisluvun $m$, joka on skalaarimuunnettu generaattoripisteellä $G$, muodostama hash-arvo, jolloin syntyy eräänlainen uusi kulutuksen julkinen avain $B_m$:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $ $$

Esimerkiksi ensimmäinen avain $B_1$ saadaan tällä tavalla:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Bobin julkaisema staattinen osoite koostuu nyt seuraavista osista: $B_{\text{scan}}$ ja $B_m$. Esimerkiksi ensimmäinen staattinen osoite, jonka nimi on $1$, on seuraava:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Aloitamme vain etiketistä $1$, koska etiketti $0$ on varattu muutosta varten. Alice, joka haluaa lähettää bitcoineja Bobin antamaan staattiseen osoitteeseen, johtaa yksilöllisen maksuosoitteen $P_0$ käyttämällä uutta $B_1$:a $B_{\text{spend}}$:n sijaan:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G$ $$

Todellisuudessa Alice ei välttämättä edes tiedä, että Bobilla on merkitty osoite, sillä hän käyttää yksinkertaisesti Bobin antaman staattisen osoitteen toista osaa, joka tässä tapauksessa on arvo $B_1$ eikä $B_{\text{spend}}$. Maksujen skannaamiseen Bob käyttää aina alkuperäisen staattisen osoitteensa arvoa $B_{\text{spend}}$:lla tällä tavalla:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Sitten hän yksinkertaisesti vähentää $P_0$:lle löytämänsä arvon jokaisesta ulostulosta yksi kerrallaan. Sitten hän tarkistaa, vastaako jokin näiden vähennysten tuloksista yhden lompakossaan käyttämänsä etiketin arvoa. Jos se täsmää esimerkiksi tulosteen #4 kohdalla, jossa on merkintä $1$, tämä tarkoittaa, että tämä tuloste on hiljainen maksu, joka liittyy hänen staattiseen osoitteeseensa, jonka nimi on $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$ $$

Tämä toimii, koska:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Tämän menetelmän ansiosta Bob voi käyttää useita staattisia osoitteita ($B_1$, $B_2$, $B_3$...), jotka kaikki on johdettu hänen staattisesta perusosoitteestaan ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}}$), jotta käyttötarkoitukset voidaan erottaa toisistaan asianmukaisesti.

Tämä staattisten osoitteiden erottelu on kuitenkin voimassa vain henkilökohtaisen lompakon hallinnan näkökulmasta, mutta se ei mahdollista identiteettien erottelua. Koska kaikilla on sama $B_{\text{scan}}$, on hyvin helppoa yhdistää kaikki staattiset osoitteet toisiinsa ja päätellä, että ne kuuluvat yhdelle taholle.