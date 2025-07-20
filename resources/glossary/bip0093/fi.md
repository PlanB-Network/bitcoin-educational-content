---
term: BIP0093
---

Tiedollinen BIP, jossa ehdotetaan standardia hierarkkisen deterministisen portfolion seed:n tallentamiseen ja palauttamiseen (BIP32:n mukaisesti) Shamirin salaisen avaimen jakamisen avulla. Tämä protokolla määrittelee "codex32"-muodon, joka on saanut vaikutteita bech32-muodosta, ottamalla käyttöön strukturoidun merkkijonon, joka koostuu etuliitteestä, kynnysarvoparametrista, tunnisteesta, jakoindeksistä, hyötykuormasta ja tarkistussummasta (BCH). Menetelmän avulla seed voidaan jakaa enintään 31 jakoon, joista seed:n täydellinen palautus edellyttää määriteltyä kynnysarvoa (1-9).