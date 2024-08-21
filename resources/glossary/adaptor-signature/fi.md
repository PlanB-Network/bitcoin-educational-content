---
termi: ADAPTOR SIGNATURE
---

Kryptografinen menetelmä, joka mahdollistaa aitojen allekirjoitusten yhdistämisen lisäallekirjoituksen (kutsutaan "adaptor signature") kanssa paljastaakseen salaisen tiedon. Tämä menetelmä toimii siten, että tietäessä kaksi elementtiä kolmesta – voimassa olevan allekirjoituksen, adaptor-allekirjoituksen ja salaisuuden – voidaan päätellä puuttuva kolmas elementti. Yksi tämän menetelmän mielenkiintoisista ominaisuuksista on, että jos tiedämme vastapuolemme adaptor-allekirjoituksen ja tietyn pisteen elliptisellä käyrällä, joka liittyy salaisuuteen, jota käytettiin tämän adaptor-allekirjoituksen laskemiseen, voimme johtaa oman adaptor-allekirjoituksemme, joka vastaa samaa salaisuutta, koskaan suoraan pääsemättä käsiksi itse salaisuuteen. Kahden toisiaan luottamattoman osapuolen välisessä vaihdossa tämä tekniikka mahdollistaa kahden arkaluonteisen tiedon samanaikaisen paljastamisen osallistujien välillä. Tämä prosessi poistaa luottamuksen tarpeen välittömissä transaktioissa, kuten Coin Swap tai Atomic Swap. Otetaan esimerkki ymmärtääksemme paremmin. Alice ja Bob haluavat lähettää toisilleen 1 BTC, mutta he eivät luota toisiinsa. He käyttävät siis adaptor-allekirjoituksia poistaakseen luottamuksen tarpeen toiseen osapuoleen tässä vaihdossa (tehden siitä "atomisen" vaihdon). He toimivat seuraavasti:
* Alice aloittaa tämän atomisen vaihdon. Hän luo transaktion $m_A$, joka lähettää 1 BTC:n Bobille. Hän luo allekirjoituksen $s_A$, joka vahvistaa tämän transaktion käyttäen hänen yksityistä avaintaan $p_A$ ($P_A = p_A \cdot G$), ja käyttäen noncea $n_A$ ja salaisuutta $t$ ($N_A = n_A \cdot G$ ja $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice laskee adaptor-allekirjoituksen $s_A'$ salaisuudesta $t$ ja hänen todellisesta allekirjoituksestaan $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice lähettää Bobille adaptor-allekirjoituksensa $s_A'$, allekirjoittamattoman transaktionsa $m_A$, pisteen, joka vastaa salaisuutta $T$, ja pisteen, joka vastaa noncea $N_A$. Kutsutaan näitä tietoja "adaptoriksi". Huomaa, että pelkällä tämän tiedon avulla Bob ei pysty palauttamaan Alicen BTC:tä.
* Bob voi kuitenkin varmistaa, ettei Alice petä häntä. Tehdäkseen tämän, hän tarkistaa, että Alicen adaptor-allekirjoitus $s_A'$ vastaa luvattua transaktiota $m_A$. Jos seuraava yhtälö on oikein, hän on vakuuttunut, että Alicen adaptor-allekirjoitus on pätevä: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Tämä varmistus antaa Bobille vakuutuksia Alicelta, jotta hän voi jatkaa atomisen vaihdon prosessia mielenrauhassa. Hän luo sitten oman transaktionsa $m_B$ lähettäen 1 BTC:n Alicelle ja hänen oman adaptor-allekirjoituksensa $s_B'$, joka linkittyy samaan salaisuuteen $t$, jonka vain Alice toistaiseksi tietää (Bob ei tiedä tätä arvoa $t$, mutta vain sen vastaavan pisteen $T$, jonka Alice on hänelle antanut): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob lähettää Alicelle sovittimen allekirjoituksensa $s_B'$, allekirjoittamattoman tapahtumansa $m_B$, pisteen, joka vastaa salaisuutta $T$, ja pisteen, joka vastaa noncea $N_B$. Alice voi nyt yhdistää Bobin sovittimen allekirjoituksen $s_B'$ salaisuuden $t$ kanssa, jonka vain hän tietää, laskeakseen voimassa olevan allekirjoituksen $s_B$ tapahtumalle $m_B$, joka lähettää hänelle Bobin BTC:t: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice lähettää tämän allekirjoitetun tapahtuman $m_B$ Bitcoin-lohkoketjuun palauttaakseen BTC:t, jotka Bob lupasi hänelle. Bob saa tiedon tästä tapahtumasta lohkoketjussa. Hän pystyy näin ollen eristämään allekirjoituksen $s_B = s_B' + t$ perusteella kuuluisan salaisuuden $t$, jota hän tarvitsi:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Kuitenkin tämä salaisuus $t$ oli ainoa puuttuva tieto Bobille tuottaa voimassa oleva allekirjoitus $s_A$, Alicen sovittimen allekirjoituksesta $s_A'$, joka sallii hänen vahvistaa tapahtuman $m_A$ lähettäen BTC:n Alicelta Bobille. Hän laskee sitten $s_A$:n ja lähettää tapahtuman $m_A$ vuorostaan: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$