---
term: Ham işlem
definition: Ağda yayınlanmaya hazır, tam ikili (binary) formdaki Bitcoin işlemi.
---

Oluşturulmuş ve imzalanmış, ikili formunda mevcut olan bir Bitcoin işlemi. Ham bir işlem (*raw TX*), bir işlemin ağda yayınlanmadan hemen önceki son temsilidir. Bu işlem, bir bloğa dahil edilmesi için gerekli tüm bilgileri içerir:


- Versiyonu;
- Bayrak;
- Girdiler;
- Çıktılar;
- Kilitlenme zamanı;
- Tanık.


"*Ham işlem*" olarak adlandırılan şey, işlemin generate'ünü txid'e dönüştürmek için SHA256 Hash işlevinden iki kez geçirilen ham verileri temsil eder. Bu veriler daha sonra işlemi Blockchain'ye entegre etmek için bloğun Merkle Tree'inde kullanılır.


