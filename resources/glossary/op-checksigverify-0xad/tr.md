---
term: OP_CHECKSIGVERIFY (0XAD)
---

OP_CHECKSIG` ile aynı işlemi gerçekleştirir, ancak imza doğrulaması başarısız olursa, kod hemen bir hatayla durur ve böylece işlem geçersiz olur. Doğrulama başarılı olursa, kod yığına bir `1` (true) değeri itmeden devam eder. Özetle, `OP_CHECKSIGVERIFY`, `OP_CHECKSIG` işlemini ve ardından `OP_VERIFY` işlemini gerçekleştirir. Bu işlem kodu Tapscript'te Schnorr imzalarını doğrulamak için değiştirilmiştir.