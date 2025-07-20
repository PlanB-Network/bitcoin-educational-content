---
term: ECDSA
---

Akronim za "Elliptic Curve Digital Signature Algorithm." To je algoritam za digitalni potpis zasnovan na kriptografiji eliptičkih krivih (ECC). To je varijanta DSA (Digital Signature Algorithm). ECDSA koristi svojstva eliptičkih krivih kako bi obezbedio nivoe sigurnosti uporedive sa tradicionalnim algoritmima javnog ključa, kao što je RSA, dok koristi značajno manje veličine ključeva. ECDSA omogućava generisanje parova ključeva (javni i privatni ključevi) kao i kreiranje i verifikaciju digitalnih potpisa.


U kontekstu Bitcoin, ECDSA se koristi za izvođenje javnih ključeva iz privatnih ključeva. Takođe se koristi za potpisivanje transakcija, kako bi se zadovoljio skript za otključavanje bitkoina i njihovo trošenje. Eliptična kriva korišćena u Bitcoin-ovom ECDSA je `secp256k1`, definisana jednačinom $y^2 = x^3 + 7$. Ovaj algoritam se koristi od početka Bitcoin 2009. godine. Danas deli svoje mesto sa Schnorr protokolom, još jednim algoritmom digitalnog potpisa uvedenim sa Taproot 2021. godine.