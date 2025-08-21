---
name: Umbrel LND
description: Umbrel'de Lightning Network Daemon (LND) kurulumu ve yapılandırılması hakkında ileri düzey eğitim
---
![cover](assets/cover.webp)




## Giriş



Bu ileri düzey eğitim, Umbrel node'unuzda Lightning Node (LND) uygulamasının kurulumu, yapılandırılması ve kullanımı konusunda sizi adım adım yönlendirir. Kanalları nasıl açacağınızı, likiditenizi nasıl yöneteceğinizi ve düğümünüzü bir mobil uygulama ile nasıl senkronize edeceğinizi öğreneceksiniz.



## 1. Ön koşul: işlevsel Bitcoin Umbrel düğümü



Lightning'i dağıtmadan önce, Umbrel üzerinde tamamen çalışır durumda bir Bitcoin düğümüne sahip olmanız gerekir. Bu, Umbrel'i (Raspberry Pi, NAS veya başka bir makineye) kurmayı ve Blockchain Bitcoin'yı tamamen senkronize etmeyi içerir.



Umbrel'i kurmak ve Bitcoin düğümünüzü yapılandırmak için özel eğitimimizi izlemenizi öneririz:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin düğümünüzün güncel olduğundan ve düzgün çalıştığından emin olun, çünkü Lightning Network tüm off-chain işlemleri için buna güvenir.



## 2. Lightning Network'e Giriş



Lightning Network, Bitcoin işlemlerini ana Blockchain'ün dışında gerçekleştirerek hızlandırmak ve maliyetini azaltmak için tasarlanmış ikinci bir Layer protokolüdür.



Somut olarak, Lightning düğümler arasında bir ödeme kanalları ağı kullanır: iki kullanıcı On-Chain BTC'yi (ilk işlem) bloke ederek bir kanal açar, ardından bu kanal içinde anında Exchange ödemeleri yapabilir. Bu off-chain işlemleri Blockchain'ya kaydedilmez, dolayısıyla hızları ve neredeyse sıfır maliyetleri vardır.



Ödemeler, ağdaki herhangi bir alıcıya ulaşmak için birden fazla kanaldan (aracı düğümler sayesinde) yönlendirilebilir ve neredeyse sınırsız ölçekte anlık işlemlere olanak tanır. Böylece Lightning, Blockchain Bitcoin üzerindeki yükü hafifletirken, günlük ödemeler veya mikro işlemler için ideal olan çok hızlı, düşük maliyetli işlemler sunar.



Bir Lightning düğümünün çalışması için ağa kalıcı olarak bağlı olması ve diğer Lightning düğümleriyle etkileşime girmesi gerekir. Hepsi birbiriyle uyumlu olan çeşitli yazılım uygulamaları (LND, Core Lightning, Eclair, vb.) mevcuttur. Umbrel, resmi Lightning Node uygulamasının bir parçası olarak LND'ü (Lightning Network Daemon) kullanır. Bu eğitim LND'e odaklanmaktadır.



Lightning Network'e tam bir teorik giriş için özel kursumuzu almanızı öneririz:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bu eğitim, LND düğümünüzle pratik yapmaya geçmeden önce size Lightning Network'in temel kavramları hakkında kapsamlı bir temel sağlayacaktır.



## 3. Neden LND'yi kendiniz barındırmalısınız?



Umbrel'de kendi Lightning düğümünüzü (LND) işletmek, saklama veya yarı saklama çözümlerine kıyasla fonlarınız ve kanallarınız üzerinde tam egemenlik sağlar.



### Yıldırım çözümlerinin karşılaştırılması :



**Solutions custodiales (örn: Satoshi'un Wallet'u)** :




- Lightning bitcoinleriniz güvenilir bir üçüncü tarafça yönetilir
- Kullanımı kolay, teknik karmaşıklık yok
- Operatör fonlarınızı tutar ve işlemlerinizi izleyebilir
- Kontrolü ve gizliliği feda edersiniz



**Emtia dışı tüketici cüzdanları (örn. Phoenix, Breez)** :




- Kullanıcılar özel anahtarlarını ve dolayısıyla BTC'lerinin Ownership'ini ellerinde tutarlar
- Tam düğüm yönetimi yok - uygulama kanalları arka planda yönetir
- Sadelik ve egemenlik arasında uzlaşma
- Likidite için tedarikçi altyapısına bağımlılık
- Teknik sınırlamalar (bir akıllı telefon diğerleri için ödeme yönlendiremez)



**Kendi kendine barındırılan LND düğümü (Umbrel)** :




- Maksimum egemenlik: On-Chain ve off-chain BTC'leriniz tamamen sizin kontrolünüz altında
- Kanalların açılması veya ödemelerinizin yönetilmesinde hiçbir üçüncü taraf yer almaz
- Daha fazla gizlilik (kanallarınız ve işlemleriniz yalnızca siz ve doğrudan eşleriniz tarafından bilinir)
- Kullanım özgürlüğü: kendi hizmetlerinize ve cüzdanlarınıza bağlanın
- Başkaları için işlem yönlendirme imkanı (mikro ücretlendirme)
- Artan teknik sorumluluklar (bakım, likidite yönetimi, yedeklemeler)



Kısacası, kendi kendini barındıran LND size maksimum kontrol sağlar, ancak daha fazla teknik beceri gerektirir. Bu, kolaylık ve egemenlik arasında bir değiş tokuştur.



## 4. Adım adım öğretici



### 4.1 Lightning Node uygulamasının Umbrel'e yüklenmesi ve yapılandırılması



Umbrel düğümünüz (Bitcoin) senkronize edildikten sonra aşağıdaki adımları izleyin :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Lightning Node uygulamasını Interface Umbrel'in "App Store" bölümünden yükleyin.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) Umbrel'inizde bir uygulama olarak konuşlandırılacaktır. İlk açtığınızda, Lightning'in deneysel bir teknoloji olduğunu bildiren bir uyarı mesajı göreceksiniz.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Yeni bir düğüm oluşturmak veya bir yedekten/seed'den bir düğümü geri yüklemek arasında seçim yapabilirsiniz. İlk kez kurulum için yeni bir düğüm oluşturmayı seçin. Lightning Node uygulaması generate 24 kelimelik bir Mnemonic ifadesi (seed Lightning'iniz) verecektir: gerekirse Lightning fonlarınızı geri yüklemek için kullanılacağından bu ifadeyi çok dikkatli bir şekilde (ideal olarak çevrimdışı, kağıt üzerine) yazın.



**Not: Umbrel'in son sürümlerinde, Lightning uygulamasının yüklenmesi bu 24 kelimelik seed'ü sağlar (Bitcoin Umbrel düğümünün kendisi sağlamaz).



![Interface principale de Lightning Node](assets/fr/04.webp)



Başlatma işleminden sonra Lightning Node'un ana Interface'ine erişeceksiniz.



![Paramètres de l'application](assets/fr/05.webp)



Uygulama ayarlarında bir dizi önemli seçenek bulacaksınız:




   - Düğüm Kimliğinize (düğümünüzün benzersiz tanımlayıcısı) başvurun
   - Harici bir Wallet bağlama (Wallet Bağlama)
   - Gizli kelimeleri görüntüle
   - Gelişmiş Ayarlara Erişim
   - Kanalları kurtarın
   - Kanal yedekleme dosyasını indirin
   - Otomatik yedeklemeleri etkinleştirin
   - Tor üzerinden yedeklemeyi yapılandırma (Tor üzerinden yedekleme)



Bu seçenekler Lightning düğümünüzün güvenliği ve yönetimi için çok önemlidir. Otomatik yedeklemeleri etkinleştirdiğinizden ve gizli kelimelerinizi güvende tuttuğunuzdan emin olun.



**Yararlı kaynaklar:**




- [Umbrel Topluluğu](https://community.umbrel.com) - Kullanıcıların Umbrel ve ekosistemi ile ilgili sorunlarını ve çözümlerini paylaşabilecekleri tartışma forumu


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Umbrel'deki Lightning Node uygulama özelliklerinin açıklaması
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Resmi LND belgeleri

### 4.2 Bir Lightning kanalı açma



LND kurulup çalışmaya başladıktan sonra ilk Lightning kanalınızı açabilirsiniz. Bağlanacak kaliteli düğümler bulmak için:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) kanal açmak için güvenilir düğümler bulmak için bir kaşiftir.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Örneğin, [ACINQ node](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) mükemmel kullanılabilirlik ve likidite istatistiklerine sahip tanınmış bir node'dur.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Bu ders için [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca) ile bir kanal açacağız. Bağlantı için gerekli bilgiler (pubkey@ip:port) Amboss sayfalarında verilmiştir.



Kanalı açmak için :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Lightning Node ana sayfasında, "+ KANAL AÇ" düğmesine tıklayın



![Configuration du canal](assets/fr/10.webp)



Kanal yapılandırma sayfasında :




   - Amboss'tan kopyalanan düğüm kimliğini yapıştırın (format: pubkey@ip:port)
   - Kanal kapasitesi miktarını tanımlayın (ACINQ gibi bazı düğümlerin minimumları vardır, örneğin 400k Sats)
   - Gerekirse açılış işlem ücretlerini ayarlayın



![Canal en cours d'ouverture](assets/fr/11.webp)



İşlem gönderildikten sonra, kanal ana sayfada "açılıyor" olarak görünecektir. On-Chain işleminin onaylanmasını bekleyin.



![Détails du canal](assets/fr/12.webp)



Ayrıntılarını görüntülemek için kanala tıklayın:




   - Mevcut durum
   - Toplam kapasite
   - Likidite dağılımı (gelen/giden)
   - Uzak düğümün açık anahtarı
   - Ve diğer teknik bilgiler



### Gelen likiditeyi elde etmek için Lightning Network+ kullanımı



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+, gelen nakit parayı elde etmeyi kolaylaştırmak için Umbrel App Store'da mevcuttur.



![Interface principale de LN+](assets/fr/14.webp)



Ana Interface üç önemli seçenek sunar:




- "Likidite swapları: mevcut swap tekliflerini keşfedin
- "Benim İçin Aç": uygun olduğunuz takasları filtreleyin
- "To Docs": belgelere erişim



![Message d'erreur LN+](assets/fr/15.webp)



Not: Henüz açık bir kanalınız yoksa, "Benim İçin Aç" seçeneğine tıkladığınızda bu hata mesajını görürsünüz.



![Liste des swaps disponibles](assets/fr/16.webp)



"Likidite Takasları" sayfası ağda mevcut olan tüm takas tekliflerini gösterir.



![Swaps éligibles](assets/fr/17.webp)



"Benim İçin Aç" yalnızca düğümünüzün gerekli koşulları karşıladığı takasları filtreler.



![Détails d'un swap](assets/fr/18.webp)



Takas detayları örneği :




- Pentagon yapılandırması (5 katılımcı)
- Kanal başına 300k Sats kapasite
- Ön koşul: 1M Sats toplam kapasiteye sahip en az 10 açık kanal
- Mevcut yerler: 4/5



### 4.3 Bir mobil uygulama ile senkronizasyon (Zeus)



Lightning düğümünüzü uzaktan (akıllı telefon) kontrol etmek için Zeus'u (iOS/Android'de bulunan açık kaynaklı uygulama) kullanabilirsiniz.



*umbrel ile *Zeus yapılandırması :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Umbrel düğümünüzün erişilebilir olduğundan emin olun (varsayılan olarak Tor üzerinden).


Interface Umbrel'de Lightning Node uygulamasını açın, ardından okla gösterildiği gibi "Wallet'u Bağla" düğmesine tıklayın.



![Page de connexion avec QR code](assets/fr/20.webp)



LND erişim verilerinizi lndconnect formatında içeren bir QR kodu görünür. Bu QR kodu özellikle yoğun bilgi içerir, bu nedenle daha kolay okumak için büyütmekten çekinmeyin.



![Configuration initiale de Zeus](assets/fr/21.webp)



Telefonunuzda :




   - Zeus'u Açın
   - Ana sayfada, kendi Lightning düğümünüzü bağlamak için "Gelişmiş kurulum "a tıklayın
   - Parametrelerde "Bir Wallet oluşturun veya bağlayın" seçeneğini seçin



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Zeus'ta:




   - Bağlantı türü olarak "LND (REST)" seçin
   - QR kodunu tarayabilir (önerilen yöntem) veya bilgileri manuel olarak girebilirsiniz. (Çok yoğun olduğu için Umbrel QR kodunu yakınlaştırmaktan çekinmeyin)
   - Önemli: Umbrel'inize yalnızca Tor üzerinden erişilebiliyorsa (varsayılan) "Tor Kullan" seçeneğini etkinleştirin
   - Yapılandırmayı kaydet



Zeus'unuz artık Umbrel düğümünüze bağlı ve tamamen kendi kendini yönetmeye devam ederken Lightning ödemeleri yapmanıza, kanallarınızı, bakiyelerinizi vb. görüntülemenize olanak tanıyor.



**Gelişmiş bağlantı seçenekleri:**



Varsayılan olarak, Zeus ↔ Umbrel bağlantısı Tor üzerinden yapılır. Daha hızlı bir bağlantı için iki alternatif vardır:



**Lightning Node Connect (LNC)** :




   - Lightning Labs'ın şifreli bağlantı mekanizması
   - Lightning Terminal uygulamasını Umbrel'e yükleyin (LNC erişimi içerir)
   - generate Lightning Terminal'de bir bağlantı QR kodu (Bağlan → Zeus'u LNC ile Bağla)
   - Zeus'a tarayın (bağlantı türü olarak "LNC" seçin)



**VPN Tailscale**:




   - Yapılandırması kolay mesh VPN
   - Tailscale'i Umbrel'e (App Store) ve cep telefonunuza yükleyin
   - Zeus'a Tor Address yerine Tailscale özel IP üzerinden bağlanın



Bu seçenekler zorunlu değildir ve Tor + Zeus çözümü çoğu durumda iyi çalışır.



> **Yararlı kaynaklar:**
> - [Zeus Dokümantasyonu - Umbrel Bağlantısı](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Zeus'u Umbrel'e bağlamak için resmi kılavuz
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus açık kaynak projesi
> - [Umbrel Topluluğu - Zeus'u Tailscale ile Bağlama](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Tailscale kullanarak Zeus'u Umbrel'e bağlama kılavuzu

## 5. Güvenlik ve en iyi uygulamalar



Kendi kendine barındırılan bir Lightning düğümünü yönetmek, güvenliğe özellikle dikkat edilmesini gerektirir.



### Düğümünüz için yedekleme ve güvenlik



**Temel yedekleme türleri**



Lightning Umbrel düğümünüz iki tür yedekleme gerektirir:



**seed cümlesi (24 kelime)**




- On-Chain fonlarını kurtarır
- Wallet Lightning'inizi yeniden oluşturmak için gerekli
- Ultra güvenli depolama için (çevrimdışı, kağıt üzerinde)



**Statik Kanal Yedekleme (SCB)** dosyası




- Yıldırım kanalı bilgilerini içerir
- Bir çarpışma durumunda kanalın zorla kapatılmasını sağlar
- Önemli:** `channel.db` dosyasını asla manuel olarak kaydetmeyin (ceza riski)



**Manuel yedekleme prosedürü



Kanallarınızı manuel olarak kaydetmek için :


1. Lightning Node menüsüne erişin ("+ Kanal Aç "ın yanındaki üç nokta "⋮")


2. Kanal yedekleme dosyasını indirin


3. Her kanal değişikliğinden sonra yeni bir SCB dışa aktarın


4. SCB'yi güvenli bir şekilde saklayın (şifrelenmiş medya, tesis dışı kopya)



**Umbrel** otomatik yedekleme sistemi



Umbrel, gelişmiş bir otomatik yedekleme sistemine sahiptir:



*Veri koruma:*




- İletimden önce istemci tarafı şifreleme
- Tor ağı üzerinden gönderme
- Rastgele doldurma ile desteklenen veriler
- Cihazınıza özgü şifreleme anahtarı



*Geliştirilmiş güvenlik:*




- Durum değişikliklerinde anında yedekleme
- Rastgele aralıklarla "tuzak" yedeklemeler
- Yedekleme boyutu değişikliklerini gizleme
- Zaman analizine karşı koruma



*Restorasyon süreci:*




- seed Şemsiyenizden türetilen tanımlayıcı ve anahtar
- Sadece Mnemonic ibaresi ile komple restorasyon mümkündür
- En son yedeklerin otomatik kurtarılması
- Kanal ayarlarını ve verileri geri yükleme



### Çarpışma restorasyonu



Düğümünüz kaybolursa (donanım arızası, bozuk SD kart) :




- Şemsiyeyi Yeniden Takın
- Lightning uygulamasına 24 kelimelik seed'inizi girin
- Geri yükleme sırasında SCB dosyasını içe aktarın



LND, eski kanallarınızı kapatmak ve On-Chain fonlarındaki payınızı geri almak için her bir ortağınızla iletişime geçecektir. Kanallar kalıcı olarak kapatılacaktır (gerekirse yeniden açılacaktır).



### Kullanılabilirlik ve dolandırıcılık koruması



İdeal olarak, düğümünüzü mümkün olduğunca sık çevrimiçi bırakın. Uzun süreli yokluk durumunda:




- Kötü niyetli bir eş, eski bir kanal durumunu yayınlamaya çalışabilir
- Yıldırım bir "protesto süresi" öngörmektedir (LND'te yaklaşık 2 hafta)
- Uzun süre uzakta olacaksanız, bir Watchtower kurun



**Watchtower yapılandırması:**




- LND gelişmiş ayarlarında, güvenilir bir Watchtower sunucusunun URL'sini ekleyin
- Bir kamu hizmetini kullanabilir veya kendi Watchtower'unuzu kurabilirsiniz




Gözetleme kulelerinin yapılandırılması ve kullanımı hakkında daha fazla bilgi edinmek için özel eğitimimize göz atmanızı öneririz:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Diğer en iyi uygulamalar





- Yazılım güncellemeleri:** Umbrel ve LND'i güncel tutun (güvenlik düzeltmeleri)
- Donanım koruması:** Sabit bir sistem (SSD'li Raspberry Pi, mini-PC) ve bir UPS kullanın
- Ağ güvenliği:** Varsayılan Tor yapılandırmasını koruyun, Umbrel yönetici parolasını değiştirin (varsayılan: "moneyprintergobrrr")
- Şifreleme:** Mümkünse disk şifrelemeyi etkinleştirin



## 6. Ek araçlar



Umbrel'in Lightning Node uygulaması kanallarınızı yönetmek için gerekli temel bilgileri sağlar, ancak üçüncü taraf araçlar gelişmiş işlevsellik sunar.



### ThunderHub



Umbrel App Store üzerinden kurulabilen Interface modern web tabanlı Lightning düğüm yönetim sistemi.



**Özellikler:**




- Kanalların gerçek zamanlı görselleştirilmesi (kapasiteler, dengeler)
- Entegre yeniden dengeleme araçları
- Çok yollu faturalandırma (MPP) desteği
- QR kod oluşturma LNURL
- İşlem yönetimi On-Chain



ThunderHub, aktif bir yönlendirme düğümünü izlemek ve basit yeniden dengeleme yapmak için idealdir.



### Ride The Lightning (RTL)



Interface web çeşitli Lightning uygulamaları ile uyumludur (LND, Core Lightning, Eclair).



**Öne Çıkanlar:**




- Çoklu düğüm yönetimi
- Bağlama duyarlı gösterge tabloları
- Denizaltı değişimleri için destek (Lightning Loop)
- 2 faktörlü kimlik doğrulama
- Kanal yedeklerini dışa/içe aktarma



RTL, bir Lightning düğümünü daha uzman odaklı bir yaklaşımla yönetmek için eksiksiz bir "İsviçre çakısı "dır.



### Diğer faydalı araçlar





- Lightning Shell** : Tarayıcı üzerinden komut satırı (lncli)
- BTC RPC Explorer & Mempool** : Blockchain'in İzlenmesi
- LNmetrics & Torq**: Yönlendirme performans analizi
- Amboss & 1ML**: düğümünüzün "sosyal" yönetimi (takma adlar, kişiler, ağ analizi)



Bu araçlar, herhangi bir karmaşık yapılandırma olmadan Umbrel App Store üzerinden sadece birkaç tıklamayla kurulabilir.



**Ek araç kaynakları:**




- [ThunderHub.io - Özellikler](https://thunderhub.io) - ThunderHub özelliklerine genel bakış
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL belgeleri
- [David Kaspar - ThunderHub aracılığıyla yeniden dengeleme](https://blog.davidkaspar.com) - Yeniden dengeleme için pratik bir kılavuz
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Güç kullanıcıları için gelişmiş belgeler



## Sonuç



Umbrel üzerinde kendi LND düğümünüzü çalıştırmak, finansal egemenliğe doğru atılmış önemli bir adımdır. Bir saklama çözümünden daha fazla teknik katılım gerektirmesine rağmen, kontrol, gizlilik ve Lightning Network'e aktif katılım açısından faydaları oldukça fazladır.



Bu kılavuzu takip ederek artık LND'ı kurabilmeli, kanalları açabilmeli, likiditenizi yönetebilmeli ve düğümünüze uzaktan erişebilmelisiniz. Ekosistemi daha yakından tanıdıkça gelişmiş özellikleri ve ek araçları kademeli olarak keşfetmekten çekinmeyin.



Fonlarınızın güvenliğinin sizin güvenlik önlemlerinize ve uygulamalarınıza bağlı olduğunu unutmayın. Büyük meblağlar taahhüt etmeden önce her yönü anlamak için zaman ayırın.