---
term: HASH FUNCTION

---
Matemaattinen funktio, joka ottaa vaihtelevan kokoisen syötteen (jota kutsutaan viestiksi) ja tuottaa kiinteän kokoisen tulosteen (jota kutsutaan hashiksi, hashingiksi, digestiksi tai sormenjäljeksi). Hash-funktiot ovat laajalti käytettyjä salausmenetelmiä. Niillä on erityisiä ominaisuuksia, jotka tekevät niistä sopivia käytettäväksi turvallisissa yhteyksissä:


- Esikuvakestävyys: on oltava hyvin vaikeaa löytää viesti, joka tuottaa tietyn hash-tunnisteen, eli löytää hash-tunnisteelle $h$ sellainen esikuva $m$, että $h = H(m)$, missä $H$ on hash-funktio;
- Toisen esikuvan resistenssi: kun on annettu viesti $m_1$, on oltava hyvin vaikeaa löytää toinen viesti $m_2$ (joka on erilainen kuin $m_1$) siten, että $H(m_1) = H(m_2)$;
- Törmäyskestävyys: on oltava hyvin vaikeaa löytää kaksi erillistä viestiä $m_1$ ja $m_2$ siten, että $H(m_1) = H(m_2)$;
- Tamper resistance: pienten muutosten syötteessä on aiheuttava merkittäviä ja ennalta arvaamattomia muutoksia ulostulossa.

Bitcoinin yhteydessä hash-funktioita käytetään useisiin tarkoituksiin, muun muassa todistusmekanismiin (*Proof-of-Work*), transaktioiden tunnisteisiin, osoitteiden luomiseen, tarkistussumman laskemiseen ja tietorakenteiden, kuten Merkle-puiden, luomiseen. Bitcoin käyttää protokollan puolella yksinomaan `SHA256d`-funktiota, joka on myös nimeltään `HASH256` ja joka koostuu kaksinkertaisesta `SHA256`-hashista. `HASH256`-funktiota käytetään myös tiettyjen tarkistussummien laskennassa, erityisesti laajennetuille avaimille (`xpub`, `xprv`...). Lompakon puolella käytetään myös seuraavia:


- Yksinkertainen `SHA256` muistilauseiden tarkistussummia varten;
- "SHA512" "HMAC"- ja "PBKDF2"-algoritmeissa, joita käytetään determinististen ja hierarkkisten lompakoiden muodostamisessa;
- `HASH160`, joka kuvaa `SHA256`:n ja `RIPEMD160`:n peräkkäistä käyttöä. `HASH160`:tä käytetään vastaanotto-osoitteiden luomisessa (lukuun ottamatta P2PK:ta ja P2TR:ää) ja laajennettujen avainten vanhempien avainten sormenjälkien laskennassa.

> ► *Englanniksi sitä kutsutaan "hash-funktioksi".*