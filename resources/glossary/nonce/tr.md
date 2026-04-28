---
term: Nonce
definition: Madenciler tarafından geçerli bir blok karması (hash) bulmak için değiştirilen, yalnızca bir kez kullanılan sayı.
---

Hesaplama bağlamında, "Nonce" terimi yalnızca bir kez kullanılan ve daha sonra değiştirilen bir sayı anlamına gelir. Genellikle rastgele veya sözde rastgeledir. Nonces, işlemin güvenliğini sağlamak için çeşitli kriptografik protokollerde kullanılır. Örneğin, Bitcoin protokolünde kullanılan ECDSA imzaları bir Nonce kullanımını içerir. Bu, bu sayının her imza için yeni olması gerektiği anlamına gelir. Böyle bir durum söz konusu değilse, aynı Nonce'yi kullanan iki imzayı karşılaştırarak kullanılan özel anahtarı hesaplamak mümkündür.


Nonce'lar Bitcoin Mining sürecinde de kullanılır. Madenciler bu değiştirilebilir değerleri kendi aday blokları içinde artırırlar. Zorluk hedefine eşit veya daha düşük bir kriptografik Hash bulmak için Nonce değerini değiştirirler. Bu süreç, çok sayıda olası nonce arasında kapsamlı bir arama içerdiğinden önemli bir hesaplama gücü gerektirir. Bir Miner, bloğuna dahil edildiğinde zorluk kriterini karşılayan bir özet üreten bir Nonce bulduğunda, blok ağa yayınlanır ve Miner ödülü kazanır.


> 2010 yılında araştırmacılar Sony PlayStation 3'ün farklı kod paketlerini imzalarken aynı Nonce'i kullandığını keşfetti. Nonce'in bu şekilde yeniden kullanılması, saldırganların yazılımı imzalamak için kullanılan özel anahtarı hesaplamasına olanak sağladı. Ellerindeki özel anahtarla saldırganlar herhangi bir kod için geçerli imzalar oluşturarak korsan oyunlar ya da özel işletim sistemleri de dahil olmak üzere yetkisiz yazılımları doğrudan PS3 üzerinde çalıştırabiliyorlardı.

> ► *"Nonce" teriminin kökeni hakkında yaygın bir yanlış anlama vardır. Bazıları bunun "sadece bir kez kullanılan sayı" ifadesinin kısaltması olduğunu iddia etmektedir. Gerçekte, kelimenin kökeni 18. yüzyıla kadar uzanmaktadır ve "fırsat için" anlamına gelen Eski İngilizce "then anes" ifadesinin anlamsal evriminden gelmektedir.*