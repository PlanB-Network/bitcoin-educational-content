---
term: BLOK
---

Bitcoin sistemindeki veri yapısı. Bir blok, başlığında yer alan bir dizi geçerli işlem ve meta veri içerir. Her blok, başlığının Hash'i ile bir sonrakine bağlanır ve böylece Blockchain'yi oluşturur. Blockchain, bir işlemin var olmadığını doğrulamak ve çifte harcamayı önlemek için her kullanıcının tüm geçmiş işlemleri bilmesini sağlayan bir zaman damgası sunucusu görevi görür. İşlemler bir Merkle Tree içinde organize edilir. Bu kriptografik akümülatör, bir bloktaki tüm işlemlerin "Merkle Root" adı verilen bir özetinin üretilmesini sağlar Bir bloğun başlığı 6 Elements içerir:


- Bloğun sürümü;
- Önceki bloğun damgası;
- İşlemlerin Merkle Tree'sının kökü;
- Bloğun Timestamp'si;
- Zorluk hedefi;
- Nonce.


Bir bloğun geçerli olabilmesi için, `SHA256d` ile özetlendiğinde zorluk hedefine eşit veya daha az bir özet üreten bir başlığa sahip olması gerekir.