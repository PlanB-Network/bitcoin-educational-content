---
term: Blocks/rev*.dat
definition: UTXO setinin önceki bir durumuna dönülmesine olanak tanımak için geri alma (undo) verilerini saklayan dosyalar.
---

Daha önce eklenen bloklar tarafından UTXO setinde yapılan değişiklikleri potansiyel olarak tersine çevirmek için gereken bilgileri depolayan Bitcoin core'daki dosyaların adı. Her dosya, karşılık geldiği blk*.dat dosyasıyla aynı olan benzersiz bir numarayla tanımlanır. Rev*.dat dosyaları, blk*.dat dosyalarında saklanan bloklara karşılık gelen tersine çevirme verilerini içerir. Bu veriler esasen bir blokta girdi olarak kullanılan tüm UTXO'ların bir listesidir. Bu tersine çevirme dosyaları, daha önce onaylanmış blokların atılmasına neden olan bir Blockchain yeniden düzenlemesi durumunda düğümün önceki bir duruma geri dönmesini sağlar.