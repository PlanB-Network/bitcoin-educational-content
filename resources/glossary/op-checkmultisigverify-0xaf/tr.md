---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Bir `OP_CHECKMULTISIG` ve bir `OP_VERIFY` birleştirir. Tıpkı `OP_CHECKMULTISIG` gibi `N` imzadan `M` tanesinin geçerli olduğunu doğrulamak için birden fazla imza ve açık anahtar alır. Ardından, `OP_VERIFY` gibi, doğrulama başarısız olursa, kod hemen bir hatayla durur. Doğrulama başarılı olursa, kod yığına herhangi bir değer itmeden devam eder. Bu işlem kodu Tapscript'te kaldırılmıştır.