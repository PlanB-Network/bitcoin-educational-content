---
term: DIFFIE-HELLMAN

---
Kryptografinen menetelmä, jonka avulla kaksi osapuolta voi luoda jaetun salaisuuden suojaamattoman viestintäkanavan kautta. Tätä salaisuutta voidaan sitten käyttää osapuolten välisen viestinnän salaamiseen. Diffie-Hellman käyttää modulaarista aritmetiikkaa, joten vaikka hyökkääjä pystyisi seuraamaan tiedonvaihtoa, hän ei voi päätellä jaettua salaisuutta ratkaisematta vaikeaa matemaattista ongelmaa: diskreettiä logaritmia. Bitcoinissa käytetään toisinaan DH:n ECDH-muunnosta, jossa käytetään elliptistä käyrää, erityisesti staattisissa osoiteprotokollissa, kuten Silent Payments tai BIP47.