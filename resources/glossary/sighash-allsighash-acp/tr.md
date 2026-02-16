---
term: SIGHASH_ALL/SIGHASH_ACP
definition: İlk imzadan sonra girdilerin eklenmesine izin veren SigHash kombinasyonu.
---

Bitcoin işlem imzalarında kullanılan `SIGHASH_ANYONECANPAY` değiştiricisi (`SIGHASH_ACP`) ile birleştirilmiş SigHash Bayrağı (`0x81`) türü. Bu kombinasyon, imzanın işlemin tüm çıktıları ve yalnızca belirli bir girdisi için geçerli olduğunu belirtir. sIGHASH_ALL | SIGHASH_ANYONECANPAY` diğer katılımcıların ilk imzadan sonra işleme ek girdiler eklemesine izin verir. Özellikle kitlesel fonlama işlemleri gibi, farklı katılımcıların ilk imzalayan tarafından taahhüt edilen çıktıların bütünlüğünü korurken kendi girdilerini ekleyebildiği işbirlikçi senaryolarda kullanışlıdır.