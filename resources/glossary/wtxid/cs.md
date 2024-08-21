---
term: WTXID
---

Rozšíření tradičního TXID, které zahrnuje svědecká data zavedená s SegWit. Zatímco TXID je hash transakčních dat bez svědka, WTXID je `SHA256d` celých transakčních dat, včetně svědka. WTXID jsou uloženy v samostatném Merkle stromu, jehož kořen je umístěn v coinbase transakci. Toto oddělení umožňuje odstranění mutability transakce TXID.