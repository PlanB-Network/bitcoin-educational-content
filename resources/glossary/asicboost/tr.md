---
term: Asicboost
definition: Birden fazla deneme arasında hesh hesaplamalarının bir kısmını yeniden kullanarak madencilik verimliliğini yaklaşık %20 artırmaya olanak tanıyan algoritmik optimizasyon.
---

ASICBOOST, 2016 yılında icat edilen ve başlığın her bir Hash denemesi için gereken hesaplama miktarını azaltarak Bitcoin Mining'in verimliliğini yaklaşık %20 oranında artırmak için tasarlanmış algoritmik bir optimizasyon yöntemidir. Bu teknik, Mining için kullanılan SHA256 Hash işlevinin, verileri işlemeden önce bloklara bölen bir özelliğinden faydalanır. ASICBOOST, bu bloklardan birini birden fazla hashing denemesi boyunca değiştirmeden tutarak Miner'nin birkaç denemede bu blok için işin yalnızca bir kısmını yapmasına olanak tanır. Bu veri paylaşımı, önceki hesaplamalardan elde edilen sonuçların yeniden kullanılmasını sağlar ve böylece geçerli bir Hash bulmak için gereken toplam hesaplama sayısını azaltır.


ASICBOOST iki şekilde kullanılabilir: Overt ASICBOOST ve Covert ASICBOOST. Overt ASICBOOST formu, bloğun `nVersion` alanını bir Nonce olarak kullanmayı ve gerçek `Nonce`yı değiştirmemeyi içerdiğinden herkes tarafından görülebilir. Covert formu, Merkle ağaçlarını kullanarak bu değişiklikleri gizlemeye çalışır. Bununla birlikte, bu ikinci yöntem, ikinci Merkle Tree nedeniyle SegWit'in piyasaya sürülmesinden bu yana daha az etkili hale gelmiştir ve bu da onu kullanmak için gereken hesaplama sayısını artırmaktadır.


Özetle, ASICBOOST madencilerin tüm hash denemeleri için gerçek bir tam SHA256 gerçekleştirmek zorunda kalmamalarını sağlar, çünkü sonucun bir kısmı değişmeden kalır ve bu da madencilerin çalışmalarını hızlandırır.