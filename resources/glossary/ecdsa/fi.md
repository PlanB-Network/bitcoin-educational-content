---
term: ECDSA

---
Lyhenne sanoista "Elliptic Curve Digital Signature Algorithm" Se on digitaalinen allekirjoitusalgoritmi, joka perustuu elliptisen käyrän salakirjoitukseen (ECC). Se on muunnelma DSA:sta (Digital Signature Algorithm). ECDSA hyödyntää elliptisten käyrien ominaisuuksia tarjotakseen perinteisten julkisten avainten algoritmien, kuten RSA:n, turvallisuustasoja vastaavan tason, mutta käyttäen huomattavasti pienempiä avainkokoja. ECDSA mahdollistaa avainparien (julkisten ja yksityisten avainten) luomisen sekä digitaalisten allekirjoitusten luomisen ja tarkistamisen.

Bitcoinin yhteydessä ECDSA:ta käytetään julkisten avainten johtamiseen yksityisistä avaimista. Sitä käytetään myös transaktioiden allekirjoittamiseen, jotta bitcoinien avaamiseen ja käyttämiseen tarvittava käsikirjoitus täyttyy. Bitcoinin ECDSA:ssa käytetty elliptinen käyrä on `secp256k1`, joka määritellään yhtälöllä $y^2 = x^3 + 7$. Tätä algoritmia on käytetty siitä lähtien, kun Bitcoin perustettiin vuonna 2009. Nykyään se jakaa paikkansa Schnorr-protokollan kanssa, joka on toinen digitaalisen allekirjoituksen algoritmi, joka otettiin käyttöön Taprootin kanssa vuonna 2021.