---
term: DIFFIE-HELLMAN
---

Kryptografinen menetelmä, joka mahdollistaa kahden osapuolen luoda jaetun salaisuuden suojaamattoman viestintäkanavan yli. Tätä salaisuutta voidaan sitten käyttää osapuolten välisen viestinnän salaamiseen. Diffie-Hellman käyttää modulaariaritmetiikkaa siten, että vaikka hyökkääjä pystyisi tarkkailemaan vaihtoja, he eivät voi päätellä jaettua salaisuutta ratkaisematta vaikeaa matemaattista ongelmaa: diskreettiä logaritmia. Bitcoinissa käytetään joskus DH:n varianttia, ECDH:tä, joka hyödyntää elliptistä käyrää, erityisesti staattisia osoiteprotokollia kuten Silent Payments tai BIP47 varten.