---
term: WTXID

---
Rozšíření tradičního TXID včetně svědeckých dat zavedených s technologií SegWit. Zatímco TXID je hash dat transakce bez svědka, WTXID je `SHA256d` celých dat transakce včetně svědka. WTXID jsou uloženy v samostatném Merklově stromu, jehož kořen je umístěn v transakci coinbase. Toto oddělení umožňuje odstranit zkomolení TXID transakce.