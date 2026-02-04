---
term: İşlem (tx)
definition: Bir veya daha fazla girişten bir veya daha fazla çıkışa bitcoin sahipliğini devreden, blok zincirine kaydedilen işlem.
---

Bitcoin bağlamında, bir işlem ("TX" olarak kısaltılır) Blockchain üzerinde kaydedilen ve Ownership bitcoinlerini bir veya daha fazla girdiden bir veya daha fazla çıktıya aktaran bir işlemdir. Her işlem, önceki işlemlerden elde edilen çıktılar olan Harcanmamış İşlem Çıktılarını (UTXO'lar) girdi olarak tüketir ve gelecekteki işlemlerde girdi olarak kullanılabilecek yeni UTXO'ları çıktı olarak oluşturur.


Her girdi, referans aldığı çıktı tarafından belirlenen harcama koşullarını (`scriptPubKey`) yerine getiren bir imza betiği (`scriptSig`) ile birlikte mevcut bir çıktıya referans içerir. Bu, bitcoinlerin kilidinin açılmasını sağlayan şeydir. Çıktılar, aktarılan bitcoinler için yeni harcama koşullarını (`scriptPubKey`), genellikle bitcoinlerin artık ilişkilendirildiği bir açık anahtar veya bir Address şeklinde tanımlar.