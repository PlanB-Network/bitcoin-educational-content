---
term: ECDSA

---
Lühend "Elliptic Curve Digital Signature Algorithm" See on digitaalallkirja algoritm, mis põhineb elliptilise kõveraga krüptograafial (ECC). See on DSA (digitaalallkirja algoritm) variant. ECDSA kasutab elliptiliste kõverate omadusi, et tagada traditsiooniliste avalike võtmealgoritmidega (nt RSA) võrreldav turvalisuse tase, kasutades samas oluliselt väiksemaid võtmesuurusi. ECDSA võimaldab luua võtmepaare (avalikud ja privaatsed võtmed) ning luua ja kontrollida digitaalallkirju.

Bitcoini kontekstis kasutatakse ECDSA-d avalike võtmete tuletamiseks privaatvõtmetest. Seda kasutatakse ka tehingute allkirjastamiseks, et rahuldada skripti bitcoinide avamiseks ja kulutamiseks. Bitcoini ECDSA-s kasutatav elliptiline kõver on `secp256k1`, mis on defineeritud võrrandiga $y^2 = x^3 + 7$. Seda algoritmi on kasutatud alates Bitcoini loomisest 2009. aastal. Tänapäeval jagab see oma kohta Schnorr'i protokolliga, mis on teine 2021. aastal Taproot'iga kasutusele võetud digitaalallkirja algoritm.