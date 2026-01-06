---
name: Bitchat
description: Ücretsiz iletişim için merkezi olmayan, internetsiz mesajlaşma
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*BTC Sessions'ın bu eğitim videosu, Bitchat'i kurma ve kullanma sürecinde size yol gösteriyor!


Bitchat, [@jack](https://primal.net/jack)'in bir hafta sonu kodlama oturumu sırasında ilk konsepti geliştirdiği hızlı bir prototipleme çabasından ortaya çıktı. kısa bir süre sonra [@calle](https://primal.net/calle) Android uygulamasını birlikte geliştirmek üzere projeye katıldı. Jack şu anda iOS sürümünün geliştirilmesine liderlik ederken, calle diğer birçok katılımcının desteğiyle Android sürümünü denetliyor.


## Giriş: Şebeke Olmadan Özgürce Sohbet Edin


İnternet kesildiğinde, doğal afet sırasında veya iletişimin kısıtlı olduğu yerlerde mesaj gönderdiğinizi hayal edin. Bitchat bunu mümkün kılıyor. Merkezi sunucuları atlayan, cihazların Bluetooth ve örgü ağ kullanarak tamamen çevrimdışı olarak doğrudan birbirleriyle konuşmasına izin veren merkezi olmayan, eşler arası bir mesajlaşma uygulamasıdır. Gizlilik ve esneklik göz önünde bulundurularak tasarlanan Bitchat, felaket senaryoları, uzak yerler veya gözetimden kaçınmak isteyenler gibi geleneksel bağlantının güvenilmez veya kullanılamaz olduğu alanlarda kullanım için idealdir. Bitchat özünde, her mesajın uçtan uca şifrelenmesini, doğrulanmasını ve kurcalamaya karşı korumalı olmasını sağlamak için kriptografi kullanır.


Bu eğitimde, Bitchat'ün nasıl çalıştığını ve gerçekten özel, çevrimdışı iletişim için nasıl kullanabileceğinizi göstereceğiz.


## 🚀 Temel Özellikler


Bitchat bu [özellikler](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features) aracılığıyla çevrimdışı mesajlaşmayı mümkün kılar:



- Çapraz Platform Uyumlu**: IOS ve Android arasında tam protokol uyumluluğu.
- Merkezi Olmayan Mesh Ağı**: Bluetooth Düşük Enerji (BLE) üzerinden otomatik eş keşfi ve çok atlamalı mesaj aktarımı
- Uçtan Uca Şifreleme**: X25519 anahtar değişimi + özel mesajlar için AES-256-GCM
- Kanal Tabanlı Sohbetler**: İsteğe bağlı parola koruması ile konu tabanlı grup mesajlaşması
- Sakla ve İlet**: Çevrimdışı eşler için önbelleğe alınan ve yeniden bağlandıklarında teslim edilen mesajlar
- Önce Gizlilik**: Hesap yok, telefon numarası yok, kalıcı tanımlayıcı yok
- IRC Tarzı Komutlar: Tanıdık `/join, /msg, /who` tarzı arayüz.
- Mesaj Saklama**: Kanal sahipleri tarafından kontrol edilen isteğe bağlı kanal çapında mesaj kaydetme
- Acil Durum Silme**: Tüm verileri anında temizlemek için logoya üç kez dokunun
- Modern Android Kullanıcı Arayüzü**: Material Design 3 ile Jetpack Compose
- Koyu/Açık Temalar**: IOS sürümüyle eşleşen Terminal'den ilham alan estetik
- Pil Optimizasyonu**: Uyarlanabilir tarama ve güç yönetimi


## 1️⃣ Bitchat Nasıl Çalışır - basitçe


Bitchat, internet veya hücre sinyali gerekmeden doğrudan Bluetooth (aşağıdaki gibi `BLE`) aracılığıyla yakındaki telefonlara mesaj göndermenizi sağlar. Bir sohbet başlattığınızda, telefonlar görüşmeniz için benzersiz, geçici bir şifreleme anahtarı oluşturmak üzere güvenli bir el sıkışma gerçekleştirir. Her mesaj uçtan uca şifreleme ile korunur ve telefonunuz daha sonra tehlikeye girse bile geçmiş mesajların güvende kalmasını sağlamak için her biri için yeni bir anahtar kullanılır. Son olarak, uygulama mesajları küçük parçalara böler ve mesajlaşma etkinliğinizi gizlemek için bunları rastgele sahte verilerle karıştırır. Doğrudan cihazdan cihaza sohbetler için, yalnızca ~100 metreye kadar bir menzil içinde çalışır. Bu, kalabalık bir odada şifreli notlar iletmek gibidir; cihazlar doğrudan birbirlerine fısıldar ve her mesajdan sonra anahtarları parçalar.


Bitchat ayrıca Nostr protokolü ve `#geohash` kullanarak konum tabanlı sohbet odalarına katılmanızı sağlar. Bir geohash, `#u33d` gibi, tek bir mahalleden tüm bir şehre veya bölgeye kadar belirli bir coğrafi alanı temsil eden kısa bir koddur. Sadece etiketini girerek dünyadaki herhangi bir geohash sohbet odasına `teleport` yapabilirsiniz. Mesajlarınız, tam konumunuzu koruyan merkezi olmayan bir röle ağı aracılığıyla gönderilir. Ayrıca, bir geohash odasına her katıldığınızda, size yeni, geçici bir kimlik verilir ve konum tabanlı konuşmalarınıza ekstra bir gizlilik katmanı eklenir.


Daha doğru teknik ayrıntılar için lütfen [resmi Beyaz Bülten]'e (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md) bakın.


## 2️⃣ Kurulum ve Ayarlama


### Bitchat Nereden Alınır


Bitchat'i şu yolla yükleyebilirsiniz:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (iOS cihazları için)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (Android cihazlar için)


Android kullanıcılarının da alternatif seçenekleri var:



- APK'yı doğrudan [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) sayfasından indirin veya
- Nostr uyumlu [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr) aracılığıyla yükleyin


![image](assets/en/01.webp)


**Not**: _Bu eğitim öncelikle Android uygulamasına odaklanmaktadır. IOS sürümü farklı olabilir._


### Kurulum Süreci


Kurulumdan sonra, bu ilk izinler ekranını görmek için Bitchat'ü açın. İşte yapmanız gerekenler:


1. **Bu gerekli izinleri verin:**


   - Bluetooth erişimi** (yakındaki Bitchat kullanıcılarını keşfetmek için)
   - Kesin konum** (Android, Bluetooth işlevselliği için bunu gerektirir)
   - Bildirimler** (özel mesaj uyarıları almak için)

2. **Pil optimizasyonunu devre dışı bırakın**:


   - Bu, Bitchat'in arka planda çalışmasını sağlar
   - Örgü ağ bağlantılarını sürekli olarak korur


Bir sonraki ekrana geçmek için `Grant Permissions` (İzin Ver) üzerine dokunun, `prompts` (öneriler) ve `Disable Battery Optimization` (Pil Optimizasyonunu Devre Dışı Bırak) seçeneklerini izleyin.


![image](assets/en/02.webp)


Bitchat'nın ana ekranına hoş geldiniz. Hadi yönümüzü bulalım:


### Ayarlar


Her şey sırayla. Ayarlar menüsü `Bitchat logosuna` dokunarak açılabilir.  Aşağıdaki seçenekler mevcuttur:



- Görünümü ayarlayın (sistem/açık/koyu).
- spam caydırıcılığı için geohash'e `İş kanıtı` özelliğini etkinleştirin (isteğe bağlı)
- Gizliliği artırmak için `Tor` özelliğini açın.


![image](assets/en/16.webp)


### Kimliğinizi Belirleyin


Kullanıcı adınızı seçmek için üstteki `bitchat/anonXXXX` alanına dokunun. Bu, başkalarının sizi hem Bluetooth hem de internet modlarında nasıl göreceğidir. Örneğin, "anon2022 "yi istediğiniz bir kullanıcı adıyla değiştirebilirsiniz.


![image](assets/en/03.webp)


### Ağ Kanallarını Seçin


Bağlantı türleri arasında geçiş yapmak için `#location channels` menüsünü (kullanıcı adının sağında) kullanın:



- BLE Mesh***: Varsayılan Bluetooth modu (internet yok, 10 ila 50 metre menzil)
- #geohashes**: Nostr protokolü] kullanan internet destekli coğrafi topluluklar (https://nostr.com/)


Coğrafi toplulukları etkinleştirmek için `#geohashes` modunu seçtiğinizde, Bitchat Nostr protokolü ile entegre olur. Mesajlarınız Bitchat'un eşler arası ağı yerine `merkezi olmayan Nostr rölelerine' yayınlanır ve daha geniş ancak konum filtreli konuşmalara olanak tanır. En önemlisi, Bitchat kimlik anahtarlarınız kimlik doğrulamayı sürdürmek için tüm Nostr olaylarını kriptografik olarak imzalarken, geohash etiketleri (bir mahalle için `#u4pruyd` gibi) mesajları seçtiğiniz hassasiyet seviyesine göre filtreler. Bu, internet erişimi gerekli olsa da, tam koordinatları açıklamadan yerel tartışmalara katılabileceğiniz anlamına gelir.


![image](assets/en/04.webp)


### Akranları İzleme

lisans: CC-BY-SA-V4

Eş sayaç kullanıcıları gösterir:



- Yakındaki (BLE Mesh) veya
- Geohash bölgenizde (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Global Sohbet & Özel Mesajlar


Bitchat, farklı ihtiyaçlara uygun iki farklı iletişim modu sağlar:



- Genel Kanallar:** Başkalarıyla açık sohbetler için. Yakındaki kullanıcılar için yerel BLE örgü ağı aracılığıyla veya internet özellikli, konum tabanlı topluluklar için küresel bir #geohash aracılığıyla bağlanabilirsiniz.
- Özel Mesajlar:** Güvenli, bire bir görüşmeler için. Bunlar, alışverişlerinizi gizli tutmak için doğrudan, şifreli bir bağlantı kurar.


Her iki modu da anlamak, konuşmalarınızda yolunuzu bulmanıza yardımcı olacaktır.


### Kamu Kanalları: Topluluk Merkezi


Konum kanalları menüsü (sağ üst) genel görünürlüğünüzü kontrol eder. Mesh` seçeneğinin seçilmesi sizi BLE mesh aracılığıyla yakındaki tüm kullanıcılara, genellikle 10-50 metre arasındaki cihazlara bağlar. Bu, mesajların menzil içindeki herkese yayınlandığı, etkinlik duyuruları veya yerel uyarılar için ideal olan açık bir forum oluşturur.


Daha geniş coğrafi erişim için, konuma göre filtrelenmiş internet destekli topluluklara katılmak üzere herhangi bir `#geohash` etiketini seçin. Bu kanallar Nostr protokol rölelerini kullanarak şehirler veya bölgeler arasında iletişime izin verirken konuma dayalı alaka düzeyini korur. Mesajlarınız aynı kanaldaki diğer kişilere canlı olarak görünür ve yeni katılımcılar katıldıklarında otomatik olarak son mesaj geçmişini görürler.


![image](assets/en/06.webp)


### Özel konuşmalar: Güvenli ve Şifreli


Özel bir görüşme başlatmak için, `Kişilere Genel Bakış` bölümünde görüntülenen herhangi bir `kullanıcı adı` üzerine doğrudan tek dokunuşla dokunun. Ayrıca, bu kullanıcıyı favori olarak işaretlemek için `yıldız simgesi` üzerine dokunabilirsiniz; bu, çevrimdışı olsalar bile kişi listenizde görünür kalmalarını sağlar.


![image](assets/en/07.webp)


Bitchat, özel bir sohbet başlattığınızda otomatik olarak `güvenlik el sıkışmasını` başlatır. Cihazlar, konuşmanız için özel olarak şifrelenmiş bir tünel oluşturmak üzere geçici anahtarları değiş tokuş eder. Bu işlem, sürekli uçtan uca şifreleme sayesinde tüm mesajlarınızın ve paylaşılan dosyalarınızın gizli kalmasını sağlar. Özel mesajlar metin ve dosya paylaşımını destekler.


![image](assets/en/08.webp)


## 4️⃣ Ek özellikler


Bitchat'te herhangi bir yere `/` yazarak eylemler paneline anında erişebilirsiniz. Bu, hızlı eylemler için bir komut menüsü ortaya çıkarır.



- Bağlantıları yönet**: `Kullanıcıları engelle` veya `Eşlerin engelini kaldır`
- Kanal kontrolleri**: `Kanalları göster` veya `Kanala katıl/kanal oluştur`
- Sosyal etkileşimler**: `Sıcak bir kucaklama gönder` veya `alabalıkla tokatla` 🎣
- Sohbet bakımı**: `Sohbet mesajlarını temizle`
- Gizlilik araçları**: "Kimin çevrimiçi olduğunu gör" veya "Özel mesaj gönder


Eleştirileri susturmak için `/block Satoshi` veya pozitifliği yaymak için `/hug Hal` gibi komutlar anında yürütülür 🫂.


![image](assets/en/09.webp)


## 5️⃣ Kanal oluşturma


Bitchat'daki kanallar konular, konumlar veya topluluklar etrafında organize iletişim sağlar. Kendi kanalınızı oluşturmak için bu iş akışını izleyin:


### Adım 1: Bir kanal oluşturun


Bir kanal oluşturmak için, herhangi bir sohbette `/j` veya `/join` ve ardından `kanal adı` yazın (örn. `/j <kanal adı>`). Oluşturulduktan sonra yeni kanalı gösteren yeni bir `ikon ⧉` belirir. Diğer kullanıcılar aynı komutu yazarak katılabilirler (örn. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Adım 2: Ayarları yapılandırın


Varsayılan komutlara ek olarak, bir kanal içinde aşağıdaki ayarlar kullanılabilir:



- mesajları yerel olarak kaydetmek için `/save`
- kanal sahipliğini aktarmak için `/transfer` ve
- kanal şifresini değiştirmek için `/pass`.


Özel topluluklar için bu komut parola korumasını etkinleştirerek onaylı üyelerin katılmadan önce özel bir parola girmesini gerektirir.


## 6️⃣ Panik Modu


Şimdi şu "panik modundan" bahsedelim: "Bitchat logosuna" üç kez dokunmak, uygulama içindeki tüm yerel mesajların ve verilerin tamamen silinmesini başlatır. Bu, nihai gizlilik korumanızdır ve acil gizlilik gerektiren durumlar için mükemmeldir.


**Önemli hatırlatma:** _Panik modu kalıcıdır. Etkinleştirildikten sonra veriler kurtarılamaz. Dikkatli kullanın.**


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash kanalları, geleneksel ağ bağlantıları yerine `coğrafi konumlara` dayalı hedeflenmiş konuşmaları mümkün kılar. Bu özellik, bitchat'ı yerel koordinasyon, topluluk oluşturma ve konuma özel tartışmalar için ideal, konuma duyarlı bir iletişim aracına dönüştürür.


### #geohashes` nasıl çalışır?


Sistem, [Geohash sistemi](https://en.wikipedia.org/wiki/Geohash) kullanarak dünyayı ızgara karelere böler; burada hashteki her karakter daha fazla hassasiyeti temsil eder:



- Seviye 4** (örneğin, `u33d`): Yaklaşık 25km × 25km'lik bir alanı kapsar - şehir çapında tartışmalar için idealdir
- Seviye 6** (örneğin, `u33d8z`): Yaklaşık 1,2 km × 1,2 km'yi kapsar - mahalle hassasiyeti
- Seviye 8** (örneğin, `u33d8z1k`): Kabaca 150 m × 150 m'yi kapsar - sokak segmenti doğruluğu


Hassas seçim, gizlilik ile faydayı dengeler: daha yüksek seviyeler daha özel bölgeler yaratır, ancak konumunuzu daha kesin bir şekilde gösterir.


### #geohash` kanallarına katılma


1. #location channels` menüsüne erişin.

2. İstediğiniz hassasiyet seviyesini seçin ve `#geohash` girin (örn. #u33d)

3. Konum kanalına katılmak için `Teleport` düğmesine dokunun.


![image](assets/en/12.webp)


Alternatif olarak, hassasiyet seviyesini belirlemek üzere harita görünümünü kullanmak için `harita simgesine` dokunabilir ve `#location channel`a katılmak için `seç` seçeneğine dokunabilirsiniz.


![image](assets/en/13.webp)


**Önemli hatırlatma**: _#geohash işlevi aktif bir internet bağlantısı gerektirir - Bluetooth aracılığıyla çevrimdışı çalışan BLE mesh'in aksine._


## 8️⃣ Isı Haritaları


Isı haritaları, dünyanın dört bir yanındaki Bitchat etkinliklerini ve kanallarını keşfetmenin harika bir yoludur. [Bitmap](https://bitmap.lat/), Nostr ağındaki anonim, konuma dayalı mesajları görselleştirir ve izler, geçici Nostr etkinliklerini görüntüler. Bir göz atın ve konuma özel kanallara ve sohbetlere katılın.


![image](assets/en/15.webp)


## 🎯 Sonuç


Bitchat, geleneksel mesajlaşmanın başarısız olduğu senaryolar için güvenli, merkezi olmayan iletişim sağlar. BLE örgü ağını kullanarak internet altyapısı olmadan çalışabilir, bu da onu protestolar, afet bölgeleri ve bağlantının sınırlı olduğu veya sansürlendiği uzak alanlar için uygun hale getirir. Uygulama, geçici anahtar şifreleme, geohash tabanlı konum kanalları ve panik modu veri silme yoluyla gizlilik sağlar.


Uygulama henüz geliştirmenin ilk aşamalarında, ancak şimdiden umut vaat ediyor. Kullanıcılar ara sıra hata beklemeli ve sorunları [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) üzerinden bildirmelidir. Cashu protokolünü kullanan özel uygulama içi işlemler için `ecash` entegrasyonu da dahil olmak üzere iyileştirmeler planlanmaktadır.


![image](assets/en/14.webp)


## 📚 Bitchat Kaynakları


[Github](https://github.com/permissionlesstech) | [Web Sitesi ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)