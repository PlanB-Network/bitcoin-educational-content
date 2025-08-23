---
term: IŞLEM TANIĞI
---

Bitcoin işlemlerinin SegWit ile birlikte Soft Fork'den Address'ye taşınan bir bileşenini ifade eder. Tanık, bir işlemde harcanan bitcoinlerin kilidini açmak için gerekli imzaları ve açık anahtarları içerir. Eski işlemlerde tanık, tüm girdilerden `scriptSig` toplamını temsil ediyordu. SegWit işlemlerinde, tanık her bir girdi için `scriptWitness` toplamını temsil eder ve işlemin bu kısmı artık blok içinde ayrı bir Merkle Tree'a taşınmıştır.


SegWit'ten önce, bir işlem onaylanmadan önce imzalar geçersiz kılınmadan biraz değiştirilebiliyordu ve bu da işlem tanımlayıcısını değiştiriyordu. Bu, onaylanmamış bir işlemin tanımlayıcısının değiştiğini görebileceği için çeşitli protokoller oluşturmayı zorlaştırıyordu. Tanıkları ayıran SegWit, imzalardaki herhangi bir değişiklik artık işlem tanımlayıcısını (txid) değil, yalnızca tanık tanımlayıcısını (WTXID) etkilediğinden işlemleri değiştirilemez hale getirir. Değiştirilebilirlik sorununu çözmenin yanı sıra, bu ayrım her bir bloğun kapasitesinin artmasını sağlar.


> ► *İngilizcede "témoin" sözcüğü "tanık" olarak çevrilmektedir