---
term: op_checksig (0xac)
---

針對指定的公開金鑰驗證簽章的有效性。它從堆疊中取得最上面的兩個 Elements：簽署和公開金鑰，並評估簽署對於交易 Hash 和指定的公開金鑰是否正確。如果驗證成功，則將值 `1` (true) 推入堆疊，否則為 `0` (false)。這個 opcode 在 Tapscript 中被修改以驗證 Schnorr 簽名。