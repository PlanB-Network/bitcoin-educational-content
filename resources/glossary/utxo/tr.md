---
term: UTXO
definition: Girdi olarak kullanılmaya hazır olan bir miktar bitcoini temsil eden harcanmamış işlem çıktısı.
---

Harcanmamış İşlem Çıktısı için kısaltma. Bir UTXO, henüz harcanmamış, yani yeni bir işlem için girdi olarak kullanılmamış bir işlem çıktısıdır. UTXO'lar, bir kullanıcının sahip olduğu ve şu anda harcanabilecek bitcoinlerin bir kısmını temsil eder. Her UTXO, bitcoinleri harcamak için gerekli koşulları tanımlayan belirli bir çıktı komut dosyası (`scriptPubKey`) ile ilişkilidir. Bitcoin'deki işlemler bu UTXO'ları girdi olarak tüketir ve çıktı olarak yeni UTXO'lar oluşturur. UTXO modeli, işlemlerin var olmayan veya daha önce harcanmış bitcoinleri harcamaya çalışmadığının kolayca doğrulanmasını sağladığından Bitcoin için temeldir.