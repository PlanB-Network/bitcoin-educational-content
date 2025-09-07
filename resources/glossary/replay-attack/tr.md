---
term: SALDIRIYI TEKRARLAYIN
---

Bitcoin bağlamında, bir Blockchain'daki geçerli bir işlem, aynı işlem geçmişine sahip başka bir Blockchain'da kötü niyetli olarak yeniden üretildiğinde bir tekrarlama saldırısı meydana gelir. Başka bir deyişle, bir kanalda yayınlanan bir işlem, ilk işlemi gönderenin rızası olmadan başka bir kanalda çoğaltılabilir.


Hard Fork'ten "*BitcoinBis*" adlı varsayımsal bir Bitcoin örneğini ele alalım. Gerçek Blockchain Bitcoin'teki bir fırıncıdan baget almak için bitcoin ile bir ödeme yaparsanız, aynı fırıncı bu meşru işlemi *BitcoinBis* üzerinde tekrarlayarak aynı tutarı bu Fork'te kripto para olarak alabilir ve sizin herhangi bir işlem yapmanıza gerek kalmaz.


Bu tür bir saldırı yalnızca Blockchain'nın zaman içinde devam eden 2 bağımsız zincirle dallanması durumunda meydana gelebilir. Tipik olarak bu durum Hard Fork ile gerçekleşir. Bir tekrarlama saldırısının mümkün olabilmesi için 2 blok zincirinin ortak bir geçmişe sahip olması ve tekrarlanan işlemin iki zincir ayrılmadan önce gerçekleşen önceki işlemlerden ya da daha önceki bir tekrarlama saldırısında zaten tekrarlanmış olan önceki işlemlerden yaratılan UTXO'ları girdi olarak kullanması gerekir.


Genel olarak, bilgi işlemde bir tekrar saldırısı, orijinal iletimi tekrarlayarak bir sistemi aldatmak için geçerli verilerin ele geçirilmesi ve yeniden kullanılmasından oluşur. Bu bazen bir ağ üzerinde kimlik hırsızlığına yol açabilir.


> ► *Bir Bitcoin işlemine yönelik bir tekrarlama saldırısı durumunda, bu bazen basitçe "tekrarlama işlemi" olarak adlandırılır. "*