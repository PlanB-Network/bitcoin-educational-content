---
term: AKÜ
---

Bitcoin UTXO'lara harcama koşulları eklemek için kullanılan komut dosyası dili bağlamında, yığın, komut dosyası yürütme sırasında geçici Elements depolamak için kullanılan bir LIFO (*Son Giren İlk Çıkar*) veri yapısıdır. Koddaki her işlem, Elements'ın eklenebildiği (*push*) veya kaldırılabildiği (*pop*) bu yığınları manipüle eder. Kodlar ifadeleri değerlendirmek, geçici değişkenleri saklamak ve koşulları yönetmek için yığınları kullanır.


Bir Bitcoin betiği yürütülürken 2 yığın kullanılabilir: ana yığın ve alt (alternatif) yığın. Ana yığın, komut dosyası işlemlerinin çoğu için kullanılır. Kod işlemleri bu yığın üzerinde veri ekler, kaldırır veya değiştirir. Diğer yandan alternatif yığın, kod yürütme sırasında verileri geçici olarak depolamak için kullanılır. OP_TOALTSTACK` ve `OP_FROMALTSTACK` gibi belirli işlem kodları, Elements'yi ana yığından alternatif yığına veya tam tersine aktarmanıza olanak tanır.


Örneğin, bir işlem doğrulandığında, imzalar ve açık anahtarlar ana yığına itilir ve imzaların işlem anahtarları ve verileriyle eşleştiğini doğrulamak için birbirini izleyen işlem kodları tarafından işlenir.