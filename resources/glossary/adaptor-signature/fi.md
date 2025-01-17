---
term: ADAPTERI ALLEKIRJOITUS

---
Kryptografinen menetelmä, jonka avulla voidaan yhdistää aito allekirjoitus ja ylimääräinen allekirjoitus (ns. "sovitinallekirjoitus") salaisen tiedon paljastamiseksi. Menetelmä toimii siten, että kun tiedetään kaksi elementtiä oikeasta allekirjoituksesta, mukautetusta allekirjoituksesta ja salaisesta tiedosta, voidaan päätellä puuttuva kolmas elementti. Yksi tämän menetelmän mielenkiintoisista ominaisuuksista on se, että jos tiedämme vastapuolemme mukautetun allekirjoituksen ja kyseisen mukautetun allekirjoituksen laskemiseen käytettyyn salaisuuteen liittyvän elliptisen käyrän tietyn pisteen, voimme johtaa oman mukautetun allekirjoituksen, joka vastaa samaa salaisuutta, ilman että meillä on koskaan suoraa pääsyä itse salaisuuteen. Kahden toisilleen epäluotettavan sidosryhmän välisessä vaihdossa tämä tekniikka mahdollistaa kahden arkaluonteisen tiedon samanaikaisen paljastamisen osallistujien välillä. Tämä prosessi poistaa luottamuksen tarpeen hetkellisissä transaktioissa, kuten kolikon- tai atomivaihdossa. Otetaanpa esimerkki, jotta ymmärrämme sen paremmin. Alice ja Bob haluavat lähettää toisilleen 1 BTC, mutta he eivät luota toisiinsa. Siksi he käyttävät adaptaattorisignaattoreita, jotta he eivät tarvitse tässä vaihdossa luottamusta toiseen osapuoleen (jolloin vaihdosta tulee "atominen" vaihto). Ne toimivat seuraavasti:


- Alice aloittaa tämän atomivaihdon. Hän luo transaktion $m_A$, joka lähettää 1 BTC Bobille. Hän luo allekirjoituksen $s_A$, joka vahvistaa tämän tapahtuman käyttämällä yksityistä avainta $p_A$ ($P_A = p_A \cdot G$) ja käyttämällä noncea $n_A$ ja salaisuutta $t$ ($N_A = n_A \cdot G$ ja $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \paralleli P_A \paralleli m_A) \cdot p_A$$$

&nbsp;


- Liisa laskee sovittimen allekirjoituksen $s_A'$ salaisuudesta $t$ ja todellisesta allekirjoituksestaan $s_A$:

$$s_A' = s_A - t$$$

&nbsp;


- Alice lähettää Bobille sovittimensa allekirjoituksen $s_A'$, allekirjoittamattoman tapahtuman $m_A$, salaisuutta $T$ vastaavan pisteen ja noncea $N_A$ vastaavan pisteen. Kutsumme näitä tietoja "sovittimeksi". Huomaa, että pelkästään näillä tiedoilla Bob ei pysty palauttamaan Alicen BTC:tä.
- Bob voi kuitenkin varmistaa, että Alice ei petä häntä. Tätä varten hän tarkistaa, että Alicen sovittimen allekirjoitus $s_A'$ vastaa luvattua tapahtumaa $m_A$. Jos seuraava yhtälö on oikein, hän on vakuuttunut siitä, että Alicen sovittimen allekirjoitus on pätevä:

$$s_A' \cdot G = N_A + H(N_A + T \paralleeli P_A \paralleeli m_A) \cdot P_A$$$

&nbsp;


- Tämä todentaminen antaa Bobille Alicen antamat takeet, joten hän voi jatkaa atomivaihtoprosessia rauhallisin mielin. Tämän jälkeen hän luo oman tapahtuman $m_B$, jossa hän lähettää Alicelle 1 BTC:n ja oman sovittimensa allekirjoituksen $s_B'$, johon liittyy sama salaisuus $t$, jonka vain Alice tietää toistaiseksi (Bob ei tiedä tätä arvoa $t$, vaan ainoastaan sen vastaavan pisteen $T$, jonka Alice on antanut hänelle): $$s_B' = n_B + H(N_B + T \paralleeli P_B \paralleeli m_B) \cdot p_B$$$

&nbsp;


- Bob lähettää Alicelle sovittimensa allekirjoituksen $s_B'$, allekirjoittamattoman tapahtuman $m_B$, salaisuutta $T$ vastaavan pisteen ja noncea $N_B$ vastaavan pisteen. Liisa voi nyt yhdistää Bobin sovittimen allekirjoituksen $s_B'$ ja salaisuuden $t$, jonka vain hän tietää, ja laskea pätevän allekirjoituksen $s_B$ transaktiolle $m_B$, jolla hänelle lähetetään Bobin BTC:

$$s_B = s_B' + t$$$

&nbsp;

$$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralleeli P_B \paralleeli m_B) \cdot P_B$$$

&nbsp;


- Alice lähettää tämän allekirjoitetun tapahtuman $m_B$ Bitcoin-lohkoketjussa saadakseen takaisin Bobin hänelle lupaamat BTC:t. Bob saa tietää tästä transaktiosta lohkoketjussa. Hän pystyy näin ollen poimimaan allekirjoituksen $s_B = s_B' + t$. Tästä tiedosta Bob voi eristää tarvitsemansa kuuluisan salaisuuden $t$:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$$

&nbsp;


- Tämä salaisuus $t$ oli kuitenkin ainoa puuttuva tieto, jonka avulla Bob pystyi tuottamaan Alicen sovitinallekirjoituksesta $s_A'$ kelvollisen allekirjoituksen $s_A$, jonka avulla hän voi validoida tapahtuman $m_A$, jossa Alice lähettää BTC:n Bobille. Tämän jälkeen hän laskee $s_A$ ja lähettää transaktion $m_A$ vuorollaan: $$s_A = s_A' + t$$$

&nbsp;

$$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralleeli P_A \paralleeli m_A) \cdot P_A$$