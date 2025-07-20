---
term: BIP0383
---

為描述符引入`multi(NUM, KEY, ..., KEY)`和`sortedmulti(NUM, KEY, ..., KEY)`函數。這些函式允許在描述符中描述多重簽章腳本，其中 `sortedmulti` 會以辭典順序排序公開金鑰，以確保匯入時的相容性。BIP383 與所有其他與描述符相關的 BIP（BIP386 除外）已在 Bitcoin Core 0.17 版中實作。