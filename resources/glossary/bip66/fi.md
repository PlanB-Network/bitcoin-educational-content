---
term: BIP66

---
Otettiin käyttöön tapahtumien allekirjoitusmuodon standardointi. Tätä rajapintastandardia ehdotettiin vastauksena OpenSSL:n tavassa käsitellä allekirjoitusten koodausta eri järjestelmissä ilmenneisiin eroihin. Tämä epäyhtenäisyys aiheutti riskin lohkoketjun jakautumisesta. BIP66 standardoi allekirjoitusmuodon kaikissa transaktioissa käyttäen tiukkaa DER-koodausta (*Distinguished Encoding Rules*). Tämä muutos edellytti pehmeää haarautumista. Aktivointiinsa BIP66 käytti sitten samaa mekanismia kuin BIP34, jossa vaadittiin `nVersion`-kentän nostamista versioon 3 ja kaikkien version 2 tai sitä alempien lohkojen hylkäämistä, kun 95 prosentin louhintakynnys oli saavutettu. Tämä kynnys ylittyi lohkolla numero 363,725 4. heinäkuuta 2015.