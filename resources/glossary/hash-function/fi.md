---
termi: HASH-FUNKTIO
---

Matemaattinen funktio, joka ottaa muuttuvan kokoisen syötteen (kutsutaan viestiksi) ja tuottaa kiinteän kokoisen tulosteen (kutsutaan hashiksi, hashaukseksi, tiivisteeksi tai sormenjäljeksi). Hash-funktiot ovat laajalti käytettyjä perusosia kryptografiassa. Ne osoittavat erityisiä ominaisuuksia, jotka tekevät niistä sopivia käytettäväksi turvallisissa yhteyksissä:
* Preimage-resistanssi: viestin löytäminen, joka tuottaa tietyn hashin, tulee olla erittäin vaikeaa, eli löytää preimage $m$ hashille $h$ siten, että $h = H(m)$, missä $H$ on hash-funktio;
* Toisen preimage-resistanssi: annetun viestin $m_1$ kohdalla, toisen viestin $m_2$ (joka on eri kuin $m_1$) löytäminen siten, että $H(m_1) = H(m_2)$, tulee olla erittäin vaikeaa;
* Kolarinkestävyys: kahden erillisen viestin $m_1$ ja $m_2$ löytäminen siten, että $H(m_1) = H(m_2)$, tulee olla erittäin vaikeaa;
* Manipuloinnin kestävyys: pienien muutosten syötteessä tulee aiheuttaa merkittäviä ja arvaamattomia muutoksia tulosteessa.

Bitcoinin kontekstissa hash-funktioita käytetään useisiin tarkoituksiin, mukaan lukien proof-of-work-mekanismi (*Proof-of-Work*), transaktioidentifikaattorit, osoitteiden generointi, tarkistussummien laskenta ja tietorakenteiden, kuten Merkle-puiden, luominen. Protokollan puolella Bitcoin käyttää yksinomaan `SHA256d`-funktiota, joka tunnetaan myös nimellä `HASH256`, ja joka koostuu kaksinkertaisesta `SHA256`-hashista. `HASH256`-funktiota käytetään myös tiettyjen tarkistussummien laskennassa, erityisesti laajennettujen avainten (`xpub`, `xprv`...) kohdalla. Lompakon puolella käytetään myös seuraavia:
* Yksinkertainen `SHA256` mnemonisten fraasien tarkistussummien laskemiseen;
* `SHA512` `HMAC`- ja `PBKDF2`-algoritmeissa, joita käytetään determinististen ja hierarkkisten lompakoiden johdannaisprosessissa;
* `HASH160`, joka kuvaa peräkkäistä käyttöä `SHA256` ja `RIPEMD160`-funktioille. `HASH160`-funktiota käytetään vastaanotto-osoitteiden generoinnissa (poikkeuksena P2PK ja P2TR) ja laajennettujen avainten vanhempien avainten sormenjälkien laskennassa.

> ► *Englanniksi sitä kutsutaan "hash function" -nimellä.*