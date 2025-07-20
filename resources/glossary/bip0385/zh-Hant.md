---
term: BIP0385
---

引入描述符函數 `addr(ADDR)` 和 `raw(HEX)` 。`addr(ADDR)`函數允許使用接收 Address 來描述輸出腳本，而`raw(HEX)`函數則允許使用該腳本的原始十六進位表示來指定輸出腳本。BIP385 與所有其他與描述符相關的 BIP（BIP386 除外）已在 Bitcoin Core 的 0.17 版中實作。