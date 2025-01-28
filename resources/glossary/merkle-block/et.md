---
term: MERKLE BLOCK

---
Andmestruktuur, mida kasutatakse BIP37 kontekstis (*Transaction Bloom Filtering*), et pakkuda kompaktset tõendit konkreetsete tehingute sisalduse kohta plokis. Seda kasutatakse eelkõige SPV rahakottide puhul. Merkle Block sisaldab ploki päiseid, filtreeritud tehinguid ja osalist Merkle-puud, mis võimaldab kergklientidel kiiresti kontrollida, kas tehing kuulub plokki, ilma et nad peaksid kõiki tehinguid alla laadima.