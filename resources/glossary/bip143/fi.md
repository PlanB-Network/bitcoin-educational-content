---
term: BIP143

---
Otetaan käyttöön uusi tapa hassata transaktio allekirjoituksen todentamista varten SegWitin jälkeisissä skripteissä. Tavoitteena on minimoida turhat operaatiot tarkistuksen aikana ja sisällyttää UTXO:n arvo syötteessä allekirjoitukseen. Tämä ratkaisee kaksi suurta ongelmaa, jotka liittyivät alkuperäiseen transaktioiden hashausalgoritmiin:


- Tiedon hajauttamisen neliöllinen kasvu allekirjoitusten määrän myötä;
- Syöttöarvoa ei sisällytetty allekirjoitukseen, mikä aiheutti riskin laitteistolompakoille, erityisesti tietoisuuden osalta aiheutuneista transaktiomaksuista.

Koska BIP141:ssä selitetty SegWit-päivitys tuo mukanaan uudenlaiset transaktiot, joiden käsikirjoitusta vanhat solmut eivät varmenna, BIP143 käyttää tilaisuutta hyväkseen ja puuttuu tähän ongelmaan ilman, että se vaatii hard forkia. Siksi BIP143 on osa SegWit-pehmeää haarautumista.