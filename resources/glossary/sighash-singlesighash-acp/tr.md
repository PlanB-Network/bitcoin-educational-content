---
term: SIGHASH_SINGLE/SIGHASH_ACP
definition: Yalnızca tek bir girdiyi ve yalnızca aynı dizine sahip çıktıyı imzalayan kombinasyon.
---

Bitcoin işlem imzalarında kullanılan `SIGHASH_ANYONECANPAY` değiştiricisi (`SIGHASH_ACP`) ile birleştirilmiş SigHash Bayrağı (`0x83`) türü. Bu kombinasyon, imzanın yalnızca belirli tek bir girdi ve yalnızca bu girdiyle aynı indekse sahip çıktı için geçerli olduğunu belirtir. Diğer girdiler ve çıktılar diğer taraflarca eklenebilir veya değiştirilebilir. Bu yapılandırma, katılımcıların belirli bir çıktıyı finanse etmek için kendi girdilerini ekleyebildiği işbirliğine dayalı işlemler için kullanışlıdır.