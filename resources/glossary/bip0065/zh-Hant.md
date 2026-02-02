---
term: BIP0065
definition: 引入操作碼 OP_CHECKLOCKTIMEVERIFY，允許將比特幣鎖定到特定日期或區塊高度。
---

引入了一個名為 `OP_CHECKLOCKTIMEVERIFY` 的新作業碼，允許 UTXO 在指定的未來時間之前無法使用。此 BIP 的實施需要 Soft Fork，發生於 2015 年 12 月 14 日。它也引入了版本 4 的區塊。