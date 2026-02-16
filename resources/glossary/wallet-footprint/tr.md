---
term: Cüzdan izi
definition: Bir cüzdanın işlemlerinde gözlemlenebilen ve faaliyetlerinin izlenmesine olanak tanıyan ayırt edici özellikler.
---

Aynı Bitcoin Wallet tarafından yapılan işlemlerde gözlemlenebilen bir dizi ayırt edici özellik. Bu özellikler, kod türlerinin kullanımındaki benzerlikleri, adreslerin yeniden kullanımını, UTXO'ların sırasını, değişiklik çıktılarının yerleşimini, RBF'ün (*Replace-by-fee*) sinyalizasyonunu, sürüm numarasını, `nSequence` alanını ve `nLockTime` alanını içerebilir.


Wallet ayak izleri analistler tarafından belirli bir tüzel kişinin Blockchain üzerindeki faaliyetlerini, işlemlerinde tekrar eden kalıpları tanımlayarak izlemek için kullanılır. Örneğin, değişikliklerini sistematik olarak P2TR adreslerine (`bc1p...`) gönderen bir kullanıcı, gelecekteki işlemlerini izlemek için kullanılabilecek ayırt edici bir ayak izi oluşturur.


LaurentMT'nin Space Kek #19'da (Fransızca konuşulan bir podcast) açıkladığı gibi, Wallet ayak izlerinin zincir analizindeki kullanışlılığı zaman içinde önemli ölçüde artmaktadır. Gerçekten de, artan sayıda komut dosyası türü ve bu yeni özelliklerin Wallet yazılımı tarafından giderek daha kademeli olarak kullanılması farklılıkları vurgulamaktadır. İzlenen varlık tarafından kullanılan yazılımı doğru bir şekilde tespit etmek bile mümkündür. Bu nedenle, bir Wallet'in ayak izini incelemenin, 2010'ların başında başlatılanlardan ziyade, özellikle yakın tarihli işlemlerle ilgili olduğunu anlamak önemlidir.