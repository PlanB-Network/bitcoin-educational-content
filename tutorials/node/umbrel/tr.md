---
name: Şemsiye
description: Umbrel'i keşfedin ve kurun - Bitcoin düğümünüz ve ana sunucunuz
---

![cover](assets/cover.webp)


![video](https://youtu.be/qFfhr4sApso)


## Giriş



### Bitcoin düğümü nedir?



Bir Bitcoin düğümü, Bitcoin core yazılımı veya alternatif bir istemci çalıştırarak Bitcoin ağına katılan bir bilgisayardır. Rolü, ağın çalışması ve güvenliği için çok önemlidir:





- Blockchain deposu**: Blockchain Bitcoin'in eksiksiz ve güncel bir kopyasını muhafaza eder
- İşlem doğrulama**: her işlemi ve bloğu protokol kurallarına göre doğrular
- Bilgi yayma**: Yeni işlemleri ve blokları diğer düğümlerle paylaşır
- Fikir birliği oluşturma**: Ağ kurallarının uygulanmasına katkıda bulunur



Kendi Bitcoin düğümünüzü çalıştırmak, finansal egemenliğe doğru atılmış çok önemli bir adımdır ve birkaç önemli fayda sunar:





- Gizlilik**: İşlemlerinizi bilgilerinizi üçüncü şahıslara vermeden paylaşın
- Sansüre karşı direnç**: Kimse sizi Bitcoin kullanmaktan alıkoyamaz
- Bağımsız doğrulama**: İşlemlerinizi doğrulamak için başkalarının düğümlerine güvenmenize gerek yok
- Fikir birliği oluşturma**: Bitcoin ağ kurallarının uygulanmasına katkıda bulunun
- Ağ desteği**: Ağ dağıtımı ve ademi merkeziyetçiliğinde aktif bir katılımcı olun



### Umbrel: Bir Bitcoin düğümünü çalıştırmak için basit bir çözüm



Umbrel, bir Bitcoin düğümünün kurulumunu ve yönetimini basitleştiren açık kaynaklı bir işletim sistemidir. Ayrıca bilgisayarınızı kişisel ve özel bir ev sunucusuna dönüştürerek, :





- Eksiksiz bir Bitcoin düğümü
- Bitcoin temel uygulamalar (Electrs, Mempool.space)
- Diğer kişisel hizmetler (bulut depolama, akış, VPN, vb.)



Zarif ve sezgisel Interface kullanıcısı Interface ile Umbrel, verileriniz üzerinde tam kontrol sağlarken, kendi kendine barındırılan hizmetleri herkes için erişilebilir hale getirir.



## Şemsiye montaj seçenekleri



Umbrel, çözümlerini kullanmanın iki ana yolunu sunuyor: anahtar teslimi bir seçenek (Umbrel Home) ve ücretsiz bir açık kaynak sürümü (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Anahtar teslim çözüm



Umbrel Home, optimum bir deneyim için özel olarak tasarlanmış, önceden yapılandırılmış bir ev sunucusudur. Bu hepsi bir arada donanım çözümü şunları içerir:



**Donanım özellikleri**




- Kendi kendine barındırma için optimize edilmiş yüksek performanslı işlemci
- Önceden yüklenmiş yüksek hızlı SSD depolama
- Sessiz soğutma sistemi
- Kompakt, zarif tasarım
- Entegre USB ve Ethernet bağlantı noktaları



**Özel avantajlar**




- Tak ve çalıştır kurulum: tak ve çalıştır
- Özel yardım ile premium destek
- Garantili otomatik güncellemeler
- Entegre geçiş sihirbazı
- Tam donanım garantisi
- Tüm işlevler için tam destek



**Fiyat**: €399 (fiyat sezona göre değişebilir)



### UmbrelOS: Açık kaynak sürümü



UmbrelOS, Umbrel işletim sisteminin ücretsiz, açık kaynaklı sürümüdür. Bu esnek çözüm, Umbrel'in temel özelliklerinden yararlanırken kendi donanımınızı kullanmanızı sağlar.



**Faydalar**




- Tamamen ücretsiz
- Açık, doğrulanabilir kaynak kodu
- Seçim özgürlüğü
- Gelişmiş özelleştirme seçenekleri



**Desteklenen platformlar**




- Raspberry Pi 5: Popüler ve uygun fiyatlı bir çözüm
- X86 sistemleri: Standart PC'ler veya sunucular için
- Sanal makine: Test etmek veya mevcut altyapıda kullanmak için



**Sınırlamalar




- Sadece toplum desteği
- Umbrel Home için ayrılmış bazı gelişmiş özellikler
- Daha teknik ilk yapılandırma
- Performans seçilen donanıma bağlıdır



Bu sürüm aşağıdakiler için idealdir :




- Teknik kullanıcılar
- Halihazırda uyumlu ekipmana sahip olanlar
- Öğrenmek ve denemek isteyen insanlar
- Projeye katkıda bulunmak isteyen geliştiriciler



Resmi kurulum bağlantıları :




- [Raspberry Pi 5 üzerine kurulum](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [x86 sistemlerine kurulum (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Sanal makine kurulumu](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Bu eğitimde, UmbrelOS'u Raspberry Pi 5'e kurmaya odaklanacağız, ancak temel ilkeler diğer platformlar için de benzerdir.



## Umbrel OS'yi Raspberry Pi 5 üzerine yükleme



### Gerekli bileşenler



Bu kurulum için ihtiyacınız olacak :





- Raspberry Pi 5 (4 GB veya 8 GB RAM)
- Resmi bir Raspberry Pi güç Supply (kararlılık için çok önemli!)
- MicroSD kart (minimum 32 GB)
- Bir microSD kart okuyucu
- Veri depolama için harici bir SSD
- Ethernet kablosu
- SSD'yi bağlamak için bir USB kablosu



### Kurulum adımları



**UmbrelOS'u indirin**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Resmi web sitesini] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5) ziyaret edin
- Raspberry Pi 5 için UmbrelOS'un en son sürümünü indirin



**Balena Etcher** kurulumu



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Bilgisayarınıza [Balena Etcher](https://www.balena.io/etcher/) indirin ve yükleyin



**microSD** kartın hazırlanması



![Insertion carte microSD](assets/fr/03.webp)




- MicroSD kartınızı bilgisayarınızın kart okuyucusuna takın



**Görüntü yanıp sönüyor**



![Flashage UmbrelOS](assets/fr/04.webp)




- Balena Etcher'ı Başlatın
- İndirilen UmbrelOS görüntüsünü seçin
- Hedef olarak microSD kartınızı seçin
- "Flash!" üzerine tıklayın ve işlemin bitmesini bekleyin
- Kartı güvenli bir şekilde çıkarın



**microSD kart kurulumu



![Installation microSD](assets/fr/05.webp)




- MicroSD kartı Raspberry Pi 5'inize takın



**Çevresel bağlantı**



![Connexion périphériques](assets/fr/06.webp)




- Harici SSD'yi kullanılabilir bir USB bağlantı noktasına bağlayın
- Pi ile yönlendiriciniz arasında Ethernet kablosunu bağlayın



**Güç açık



![Démarrage du Pi](assets/fr/07.webp)




- Resmi Raspberry Pi güç Supply'yı bağlayın
- Sistemin başlaması için birkaç dakika bekleyin



**İlk erişim**



![Accès interface web](assets/fr/08.webp)




- Aynı ağa bağlı bir cihazda tarayıcınızı açın
- Umbrel'in Interface web sitesine şu adresten erişebilirsiniz: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Eğer `umbrel.local` çalışmazsa, yerel ağınızdaki Raspberry Pi'nizin IP Address'ini bulmanız gerekir. Yapabilirsiniz :




- Yönlendiricinizin Interface'una başvurun
- Nmap gibi bir ağ tarayıcısı kullanma
- Bilgisayarınızın terminalinde `arp -a` komutunu kullanın



## Umbrel'de ilk adım



Umbrel'iniz başlatıldıktan ve tarayıcınız üzerinden erişilebilir hale geldikten sonra, başlamak için aşağıdaki adımları izleyin:



### İlk yapılandırma



**Hesabınızı oluşturun**



![Création compte](assets/fr/10.webp)




- Bir kullanıcı adı seçin
- Güvenli bir parola belirleyin
- Umbrel'inize erişmek için bu kimlik bilgilerine ihtiyacınız olacak



**Hesap onayı



![Confirmation compte](assets/fr/11.webp)




- Kontrol panelinize erişmek için "İleri "ye tıklayın



**Interface'nin Keşfi**



![Interface Umbrel](assets/fr/12.webp)




- Umbrel App Store'a erişin
- Mevcut birçok uygulamayı keşfedin
- Bitcoin için gerekli uygulamaları yükleyerek başlayalım



### Bitcoin uygulamalarının yüklenmesi



**Bitcoin Node**



![Bitcoin Node](assets/fr/13.webp)




- Yüklenecek ilk uygulama
- Blockchain Bitcoin'in tamamını indirin ve kontrol edin



**Seçmenler**



![Installation Electrs](assets/fr/14.webp)




- Bitcoin cüzdanlarını bağlamak için Electrum sunucusu
- Bitcoin düğümünüz ile senkronize olur



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Blockchain için Interface ekranı
- İşlemleri ve blokları gerçek zamanlı olarak izler



## Mempool.space ile bir işlemin izlenmesi



Mempool.space, Blockchain ağının gerçek zamanlı görselleştirilmesini sağlayan açık kaynaklı bir Bitcoin gezginidir. İşlemlerinizi izlemenizi ve işlemlerin ağda nasıl yayıldığını anlamanızı sağlar.



### Mempool ve onayları anlama



"Mempool" (bellek havuzu), onaylanmamış tüm Bitcoin işlemlerinin bir bloğa dahil edilmeden önce saklandığı sanal bir bekleme odası gibidir. Bir işlem şu şekilde işlenir:



1. **Yayın**: Bir işlem gönderdiğinizde, ilk olarak Bitcoin ağında yayınlanır


2. **Mempool'da bekliyor**: Maliyetler temelinde bir Miner tarafından seçilmeyi bekliyor


3. **İlk onay**: Reşit olmayan bir kişi bunu bir bloğa dahil eder (1. onay)


4. **Ek onaylar**: İşleminizi içeren bloktan sonra kazılan her yeni blok bir onay ekler



Tavsiye edilen onay sayısı miktara bağlıdır:




- Küçük miktarlar için: 1-2 onay yeterli olabilir
- Büyük miktarlar için: 6 onay genellikle çok güvenli kabul edilir



### Mempool.space'den Interface'i keşfedin



1. **Ana sayfa** size Bitcoin ağına genel bir bakış sunar:




   - Yakın zamanda çıkarılan bloklar
   - Farklı öncelikler için maliyet tahminleri
   - Mempool'ün mevcut durumu



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Bir işlem arayın**: Belirli bir işlemi izlemek için, tanımlayıcısını (txid) sayfanın üst kısmındaki arama çubuğuna yapıştırın.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### İşlem ayrıntılarını analiz edin



İşleminiz bulunduğunda, Mempool.space size eksiksiz bir analiz sunar:



1. **Temel bilgiler** :




   - Durum (onaylandı veya onaylanmadı)
   - Ödenen giderler (Sats/vB cinsinden)
   - Tahmini onay süresi



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **İşlem yapısı** :




   - Girdi ve çıktıların görsel temsili
   - İlgili adreslerin ayrıntılı listesi
   - Aktarılan tutarlar



3. **Teknik veriler** :




   - İşlem ağırlığı
   - Sanal boyut
   - Kullanılan format ve sürüm
   - Diğer özel meta veriler



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Umbrel'de Mempool.space kullanmanın avantajları



1. **Gizlilik**: Talepleriniz kendi düğümünüzden geçer


2. **Bağımsızlık**: Üçüncü taraf bir hizmete güvenmeye gerek yok


3. **Güvenilirlik**: Genel tarayıcılar kapalı olduğunda bile verilere erişim



Bu uygulama ile işlemlerinizi verimli bir şekilde izleyebilir, ücretlerin onay hızını nasıl etkilediğini anlayabilir ve Bitcoin ağının nasıl çalıştığını daha iyi anlayabilirsiniz.



## Düğümünüze bir Wallet Bitcoin bağlama



### Elektrik konfigürasyonu



**Yerel bağlantı



![Connexion locale](assets/fr/18.webp)




- Yerel ağınızda kullanım için
- Daha hızlı ve kolay kurulum



**Tor** üzerinden uzaktan bağlantı



![Connexion Tor](assets/fr/19.webp)




- Düğümünüze her yerden erişmek için
- Daha güvenli ve özel



### Sparrow wallet ile bağlantı



**Parametrelere erişim



![Paramètres Sparrow](assets/fr/20.webp)




- Açık Sparrow wallet
- Tercihler > Sunucu'ya gidin
- "Mevcut bağlantıyı değiştir" üzerine tıklayın



**Bağlantı türü seçimi



Sparrow üç bağlantı modu sunar:



***Halka Açık Sunucu***




- Genel sunuculara bağlantı (örn. blockstream.info, Mempool.space)
- Basit ama daha az özel



***Bitcoin core***




- Bir Bitcoin düğümüne doğrudan bağlantı
- Özel ama daha yavaş



***Özel Elektrum***




- Electrs sunucunuza bağlanın
- Gizlilik ve performansı birleştirir



**Electrs** yapılandırması



Daha önce gördüğümüz Electrs uygulamasında görüntülenen bilgileri kullanarak bağlantı türünüzü seçin:



Her iki durumda da "SSL kullan" ve "Proxy kullan" seçeneklerinin işaretini kaldırın.



**Yerel bağlantı


Ana bilgisayar: umbrel.local


Port numarası: 50001



**Uzaktan bağlantı (Tor)**


Ev sahibi : [your-Address-onion]


Port numarası: 50001



Düğümünüze yerel ağınızın dışından erişmek istiyorsanız Tor bağlantısı gereklidir.



![Configuration connexion](assets/fr/21.webp)


Sparrow wallet yazılımı hakkında daha fazla bilgi için kapsamlı bir öğreticimiz var:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Sonuç



Umbrel'iniz artık kullanıma hazır. Verilerinizin tam kontrolünü elinizde tutarken Bitcoin ağına aktif olarak katılırsınız. Ev sunucunuzun yeteneklerini genişletmek için Umbrel App Store'da bulunan diğer birçok uygulamayı keşfetmekten çekinmeyin.



## Yararlı kaynaklar



### Resmi belgeler




- [Resmi Umbrel web sitesi](https://umbrel.com)
- [Umbrel belgeleri](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin uygulamaları




- [Bitcoin core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow wallet](https://sparrowwallet.com)



### Topluluk




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)