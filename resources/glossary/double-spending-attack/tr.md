---
term: Çifte harclama
definition: Karşı tarafları dolandırmak için aynı bitcoinleri birden fazla kez kullanmaya çalışan saldırı.
---

Kötü niyetli bir kullanıcının aynı UTXO'i (*Harcama Yapılmamış İşlem Çıktısı*) birden fazla kez kullanarak işlemlere dahil olan tarafların zararına kendilerini zenginleştirmeye çalıştığı bir saldırı. Prensip olarak, bir işlem bir blokta onaylandıktan ve Blockchain'a eklendikten sonra, bu bitcoinlerin kullanımı kalıcı olarak kaydedilir ve aynı bitcoinlerin daha fazla harcanması önlenir. Çifte harcamayı önlemek bile Blockchain'ın birincil faydasıdır.


Çifte harcama saldırısı bağlamında, saldırgan önce bir tüccarla meşru bir işlem yapar, ardından aynı jetonları harcayarak ikinci bir rakip işlem yaratır, ya tutarı geri almak için kendilerine geri gönderir ya da farklı bir tüccardan başka bir mal veya hizmet satın almak için kullanır.


Bu saldırıyı mümkün kılabilecek iki ana senaryo vardır. Birincisi ve saldırgan için en basit olanı, meşru işlem bir bloğa dahil edilmeden önce hileli işlemin gerçekleştirilmesini içerir. Hileli işlemlerinin önce onaylanmasını sağlamak için saldırgan, meşru işlemden çok daha yüksek işlem ücretlerini bu işlemle ilişkilendirir. Bu bir tür hileli RBF'dir. Bu senaryo yalnızca satıcı satışı "zeroconf" yani ödeme işlemi için herhangi bir onay olmadan sonuçlandırmayı kabul ederse mümkündür. Bu nedenle, bir işlemi değişmez olarak değerlendirmeden önce birkaç onay beklemeniz şiddetle tavsiye edilir. Çok daha karmaşık olan ikinci senaryo ise %51 saldırısıdır. Saldırgan ağın bilgi işlem gücünün önemli bir kısmını kontrol ediyorsa, meşru işlemi içeren ancak kendi sahte işlemini de içeren rakip bir zincir oluşturabilir. Satıcı satışı kabul ettiğinde ve saldırgan meşru zincirden daha uzun bir zincir (daha fazla birikmiş işle) oluşturmayı başardığında, ağ düğümleri tarafından geçerli zincir olarak tanınacak olan hileli zincirini yayınlayabilir.