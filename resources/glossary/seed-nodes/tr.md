---
term: seed NODES
---

Doğrudan Bitcoin core'in kaynak koduna (`Bitcoin/src/chainparamsseeds.h`) entegre edilmiş genel Bitcoin düğümlerinin statik listesi. Bu liste, ağa katılan yeni Bitcoin düğümleri için bağlantı noktaları olarak hizmet eder, ancak yalnızca DNS tohumları isteklerinden sonraki 60 saniye içinde bir yanıt vermezse kullanılır. Bu durumda, yeni Bitcoin düğümü ağa ilk bağlantıyı kurmak ve diğer düğümlerin IP adreslerini talep etmek için bu seed düğümlerine bağlanacaktır. Nihai amaç, İlk Blok İndirmeyi (IBD) gerçekleştirmek için gerekli bilgileri edinmek ve en çok iş biriktiren zincirle senkronize olmaktır. seed düğümlerinin listesi, BIP155 tarafından belirlenen standarda uygun olarak tanımlanmış yaklaşık 1000 düğüm içermektedir. Dolayısıyla, seed düğümleri, düğümün kendisi tarafından oluşturulan `peers.dat` dosyasının olası kullanımı ve DNS tohumlarının talep edilmesinden sonra, bir Bitcoin düğümü için ağa üçüncü bağlantı yöntemini temsil eder.


> ► *Not, seed düğümleri, bağlantı kurmanın ikinci yöntemi olan "DNS tohumları" ile karıştırılmamalıdır.*