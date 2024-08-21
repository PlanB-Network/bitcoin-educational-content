---
termi: BIP145
---

Päivittää JSON-RPC-kutsun `getblocktemplate` sisältämään tuen SegWitille, BIP141:n mukaisesti. Tämä päivitys mahdollistaa louhijoiden rakentaa lohkoja ottaen huomioon uuden "paino" mittauksen transaktioille ja lohkoille, jotka SegWit toi mukanaan, sekä muita parametreja kuten sigops-rajan laskennan.