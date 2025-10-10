---
term: OP_CHECKSIG (0XAC)
---

Belirli bir açık anahtara karşı bir imzanın geçerliliğini doğrular. Yığından en üstteki iki Elements değerini alır: imza ve açık anahtar ve imzanın Hash işlemi ve belirtilen açık anahtar için doğru olup olmadığını değerlendirir. Doğrulama başarılı olursa, yığına `1` (doğru) değerini, aksi takdirde `0` (yanlış) değerini iter. Bu işlem kodu Tapscript'te Schnorr imzalarını doğrulamak için değiştirilmiştir.