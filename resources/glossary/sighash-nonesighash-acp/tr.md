---
term: SIGHASH_NONE/SIGHASH_ACP
definition: Herhangi bir çıktı taahhüt etmeden yalnızca tek bir belirli girdiyi imzalayan SigHash kombinasyonu.
---

Bitcoin işlem imzalarında kullanılan `SIGHASH_ANYONECANPAY` değiştiricisi (`SIGHASH_ACP`) ile birleştirilmiş SigHash Bayrağı (`0x82`) türü. Bu kombinasyon, imzanın herhangi bir çıktı taahhüt etmeden yalnızca belirli bir girdi için geçerli olduğunu gösterir. Bu, diğer katılımcıların serbestçe ek girdiler eklemesine ve işlemin tüm çıktılarını değiştirmesine olanak tanır.