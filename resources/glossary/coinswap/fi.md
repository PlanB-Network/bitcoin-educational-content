---
term: COINSWAP
---

Ownership:n salaisen siirron protokolla käyttäjien välillä. Tämän menetelmän tarkoituksena on siirtää bitcoinit henkilöltä toiselle ja päinvastoin ilman, että Exchange näkyy selvästi Blockchain:ssa. Coinwap käyttää älykkäitä sopimuksia siirron tekemiseen ilman, että osapuolten välillä tarvitaan luottamusta.


Kuvitellaanpa naiivi esimerkki (joka ei toimi), jossa on Alice ja Bob. Alicella on 1 BTC, joka on suojattu yksityisellä avaimella $A$, ja Bobilla on myös 1 BTC, joka on suojattu yksityisellä avaimella $B$. Teoriassa he voisivat Exchange:n avulla siirtää salaiset avaimensa ulkoisen viestintäkanavan kautta salaisen siirron. Tämä naiivi menetelmä aiheuttaa kuitenkin suuren riskin luottamuksen kannalta. Mikään ei estä Alicea pitämästä kopiota yksityisestä avaimesta $A$ Exchange:n jälkeen ja käyttämästä sitä myöhemmin bitcoinien varastamiseen, kun avain on Bobin hallussa. Lisäksi ei ole mitään takeita siitä, että Alice ei saa Bobin yksityistä avainta $B$ eikä koskaan välitä yksityistä avainta $A$ Exchange:ssä. Tämä Exchange perustuu siis liialliseen luottamukseen osapuolten välillä, eikä se pysty varmistamaan Ownership:n turvallista ja salaista siirtoa.


Ratkaistaksemme nämä ongelmat ja mahdollistaaksemme kolikonvaihdon sellaisten osapuolten välillä, jotka eivät luota toisiinsa, käytämme Smart contract-järjestelmiä, jotka tekevät Exchange:sta "atomisen". Nämä voivat olla HTLC (*Hash Time-Locked Contracts*) tai PTLC (*Point Time-Locked Contracts*). Nämä kaksi protokollaa toimivat samalla tavalla käyttäen aikalukitusjärjestelmää, joka varmistaa, että Exchange on joko onnistuneesti suoritettu tai kokonaan peruutettu, mikä suojaa molempien osapuolten varojen eheyttä. Tärkein ero HTLC:n ja PTLC:n välillä on se, että HTLC käyttää hasheja ja esikuvia tapahtuman suojaamiseen, kun taas PTLC käyttää Adaptor Signatures -sovellusta.


HTLC:n tai PTLC:n avulla tapahtuvassa kolikonvaihtoskenaariossa Alicen ja Bobin välillä Exchange tapahtuu turvallisella tavalla: joko se onnistuu ja kumpikin saa toisen BTC:n, tai se epäonnistuu ja kumpikin pitää oman BTC:nsä. Näin kumpikaan osapuoli ei voi huijata tai varastaa toisen BTC:tä.


Adaptor-allekirjoitusten käyttö on erityisen mielenkiintoista tässä yhteydessä, koska sen avulla voidaan luopua perinteisistä skripteistä (mekanismia kutsutaan joskus "_skriptittömiksi skripteiksi_"). Tämä vähentää Exchange:een liittyviä kustannuksia. Toinen suuri etu Adaptor Signatures -aloituksissa on se, että ne eivät edellytä yhteisen Hash:n käyttöä molemmille transaktion osapuolille, jolloin niiden välistä suoraa yhteyttä ei tarvitse paljastaa tietyntyyppisissä Exchange:ssä.