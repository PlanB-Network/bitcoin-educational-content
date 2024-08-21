---
term: MERKLE BLOKK
---

Andmestruktuur, mida kasutatakse BIP37 (*Transaction Bloom Filtering*) kontekstis, et pakkuda kompaktset tõestust kindlate tehingute kaasamisest blokis. Seda kasutatakse märkimisväärselt SPV rahakottide jaoks. Merkle blokk sisaldab bloki päiseid, filtreeritud tehinguid ja osalist Merkle puud, võimaldades kergklientidel kiiresti kontrollida, kas tehing kuulub blokki, ilma et peaksid alla laadima kõik tehingud.