---
term: ECDSA
---

Akronüüm fraasile "Elliptic Curve Digital Signature Algorithm" (Elliptilise Kõvera Digitaalallkirja Algoritm). See on digitaalallkirja algoritm, mis põhineb elliptilise kõvera krüptograafial (ECC). See on DSA (Digital Signature Algorithm ehk Digitaalallkirja Algoritm) variatsioon. ECDSA kasutab elliptiliste kõverate omadusi, et pakkuda turvalisuse taset, mis on võrreldav traditsiooniliste avaliku võtme algoritmidega, nagu RSA, kasutades samal ajal märkimisväärselt väiksemaid võtmesuurusi. ECDSA võimaldab võtmepaaride (avalikud ja privaatsed võtmed) genereerimist ning digitaalallkirjade loomist ja kontrollimist.

Bitcoin'i kontekstis kasutatakse ECDSA-d avalike võtmete tuletamiseks privaatvõtmetest. Samuti kasutatakse seda tehingute allkirjastamiseks, et rahuldada skripti bitcoinide avamiseks ja kulutamiseks. Bitcoin'i ECDSA-s kasutatav elliptiline kõver on `secp256k1`, mida defineerib võrrand $y^2 = x^3 + 7$. Seda algoritmi on kasutatud alates Bitcoin'i loomisest 2009. aastal. Täna jagab see kohta Schnorri protokolliga, teise digitaalallkirja algoritmiga, mis tutvustati Taproot'iga 2021. aastal.