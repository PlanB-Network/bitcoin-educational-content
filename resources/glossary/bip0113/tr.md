---
term: BIP0113
---

Tüm zaman kilidi işlemlerinin (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ve `OP_CHECKSEQUENCEVERIFY`) hesaplanmasında bir değişiklik yapıldı. Zaman kilitlerinin geçerliliğini değerlendirmek için artık son 11 bloğun zaman damgalarının ortancası olan MTP (*Median Time Past*) ile karşılaştırılmaları gerektiğini belirtir. Önceden sadece bir önceki bloğun Timestamp'i kullanılıyordu. Bu yöntem sistemi daha öngörülebilir hale getirmekte ve zaman referansının madenciler tarafından manipüle edilmesini engellemektedir. BIP113, BIP9 yöntemi kullanılarak ilk kez etkinleştirilen BIP68 ve BIP112 ile birlikte 4 Temmuz 2016 tarihinde bir Soft Fork aracılığıyla tanıtıldı.