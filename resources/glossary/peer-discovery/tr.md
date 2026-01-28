---
term: Eş keşfi
definition: Bir Bitcoin düğümünün ağdaki diğer düğümleri keşfetme ve onlara bağlanma süreci.
---

Bitcoin ağındaki düğümlerin bilgi edinmek için diğer düğümlere bağlanma süreci. Bir Bitcoin düğümü ilk başlatıldığında, ağdaki diğer düğümler hakkında hiçbir bilgisi yoktur. Yine de, en çok birikmiş işe sahip olan Blockchain ile senkronize olmak için bağlantı kurması gerekir. Bu eşleri keşfetmek için öncelik sırasına göre çeşitli mekanizmalar kullanılır:


- Düğüm, daha önce etkileşimde bulunduğu düğümler hakkında bilgi depolayan yerel `peers.dat` dosyasına başvurarak başlar. Eğer düğüm yeniyse, bu dosya boş olacak ve süreç bir sonraki adıma geçecektir;
- Peers.dat dosyasında bilgi olmaması durumunda (yeni başlatılan bir düğüm için bu normaldir), düğüm DNS tohumlarına DNS sorguları gerçekleştirir. Bu sunucular, bağlantı kurmak için muhtemelen aktif düğümlerin IP adreslerinin bir listesini sağlar. DNS tohumlarının adresleri Bitcoin core kodunda sabit olarak kodlanmıştır. Bu adım genellikle eşlerin keşfini tamamlamak için yeterlidir;
- DNS tohumları 60 saniye içinde yanıt vermezse, düğüm daha sonra seed düğümlerine dönebilir. Bunlar, doğrudan Bitcoin core'ün kaynak koduna entegre edilmiş yaklaşık bin girişten oluşan statik bir listede listelenen halka açık Bitcoin düğümleridir. Yeni düğüm, ağa ilk bağlantıyı kurmak ve diğer düğümlerin IP adreslerini almak için bu listeyi kullanacaktır;
- Önceki tüm yöntemlerin başarısız olması durumunda, düğüm operatörü her zaman ilk bağlantıyı kurmak için düğümlerin IP adreslerini manuel olarak ekleme seçeneğine sahiptir.