---
term: SegWit
---

"Segregated Witness "ın kısaltması olan SegWit, Ağustos 2017'de tanıtılan Bitcoin protokolünün bir güncellemesidir. Ağın işlem kapasitesi sorunu, işlemin değiştirilebilirliği sorunu ve gelecekteki protokol değişikliklerinin kolaylaştırılması dahil olmak üzere çeşitli teknik sorunları çözmeyi amaçlamaktadır.


Bu Soft Fork, imza verilerini ayrı bir dizine taşıyarak işlem yapısını değiştirir. Özellikle, SegWit ile imzalar ana bloktan çıkarılır ve bloğun sonunda tanıklar olarak bilinen ayrı bir veri yapısına eklenir. Bu ayrım, Bitcoin'te 1 MB olan maksimum blok boyutunu değiştirmeden her bloğun kapasitesinde bir artışa izin verir. Bu değişiklik aynı zamanda işlemin değiştirilebilirliği sorununu da çözmektedir. SegWit'dan önce, bir işlem onaylanmadan önce imzalar değiştirilebiliyor ve bu da işlem tanımlayıcısını değiştiriyordu. Bu durum, onaylanmamış bir işlemin tanımlayıcısının değiştirilebilmesi nedeniyle karmaşık işlemlerin oluşturulmasını zorlaştırıyordu. İmzaları ayıran SegWit, imzalardaki herhangi bir değişiklik artık işlem tanımlayıcısını (txid) değil, yalnızca tanık tanımlayıcısını (WTXID) etkilediğinden işlemleri değiştirilemez hale getirir. Değiştirilebilirlik sorununu çözen SegWit, Bitcoin sistemi üzerinde, özellikle de hızlı ve düşük maliyetli işlemlere olanak tanıyan Lightning Network üzerinde daha fazla geliştirme yapılmasının önünü açmıştır.