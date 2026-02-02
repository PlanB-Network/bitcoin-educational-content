---
term: VIN
definition: Önceki bir UTXO'ya referans vererek fonların kaynağını belirten bir Bitcoin işlemi öğesi.
---

Çıktıları karşılamak için kullanılan fonların kaynağını belirten bir Bitcoin işleminin belirli bir unsuru. Her `vin` bir önceki işlemden harcanmamış bir çıktıyı (UTXO) ifade eder. Bir işlem, her biri `txid` (orijinal işlemin tanımlayıcısı) ve `vout` (o işlemdeki çıktının indeksi) kombinasyonuyla tanımlanan birden fazla girdi içerebilir.


Her `vin` aşağıdaki bilgileri içerir:


- `txid`: burada girdi olarak kullanılan çıktıyı içeren önceki işlemin tanımlayıcısı;
- `vout`: önceki işlemdeki çıktının indeksi;
- `scriptSig` veya `scriptWitness`: genellikle kriptografik bir imza sağlayarak, fonları harcanmakta olan önceki işlemin `scriptPubKey` tarafından ortaya konan koşulları karşılamak için gerekli verileri sağlayan bir kilit açma komut dosyası;
- `nSequence`: bu girişin zamana nasıl kilitlendiğini ve RBF gibi diğer seçenekleri belirtmek için kullanılan özel bir alan.