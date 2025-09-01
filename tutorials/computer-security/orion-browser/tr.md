---
name: Orion Tarayıcı
description: Mac ve iPhone'da gizliliğinizi korumak için Orion Browser nasıl kullanılır?
---

![cover](assets/cover.webp)



## Giriş



Tarayıcıların çoğunun kişisel verilerimizi büyük ölçüde topladığı bir ortamda, gizlilik dostu bir tarayıcı seçimi çok önemli hale geliyor. Chrome küresel pazarın %65'ine hakimdir, ancak iş modeli tarama verilerinizin sömürülmesine dayanmaktadır. Safari, Apple ekosistemine entegre olmasına rağmen, gelişmiş koruma özelliklerinden yoksundur ve üçüncü taraf uzantılarını esnek bir şekilde desteklemez.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Web tarayıcısı pazar dağılımı: Chrome %65'in üzerinde pazar payı ile lider konumdayken onu Safari, Edge ve Firefox takip ediyor*



**Orion Browser** kendisini Apple kullanıcıları için yenilikçi bir alternatif olarak sunuyor. Kagi tarafından geliştirilen bu tarayıcı, WebKit motorunun hızını sıfır telemetri felsefesiyle birleştiriyor. Rakiplerinin aksine, Orion uzak sunuculara hiçbir veri göndermez ve YouTube dahil olmak üzere reklamların ve izleyicilerin %99,9'unu yerel olarak engeller.



Eşsiz özelliği mi? Orion, Chrome **ve** Firefox uzantılarını yerel olarak yükleyebilen **tek WebKit** tarayıcısıdır ve her iki dünyanın da en iyisini sunar. Bu uyumluluk, diğer tarayıcılardan 2 ila 3 kat daha düşük bellek tüketimi ve Apple ekosistemiyle (iCloud, Keychain) sorunsuz entegrasyon ile birleştiğinde, gizlilik bilincine sahip Mac ve iPhone kullanıcıları için ideal bir seçim haline geliyor.



## Neden Orion Browser'ı seçmelisiniz?



### Temel faydalar



**Kutudan çıkar çıkmaz maksimum koruma**: Orion reklamların %99,9'unu (YouTube dahil) ve tüm birinci taraf ve üçüncü taraf izleyicileri varsayılan olarak engeller. Teknolojisi, maksimum verimlilik için WebKit'in Akıllı İzleme Önleme özelliğini EasyPrivacy listeleriyle birleştirir. Benzersiz özellik: Orion, parmak izi komut dosyalarını **çalıştırılmadan önce** engelleyerek izlemeyi tam anlamıyla imkansız hale getirir - yalnızca verileri "maskelemeye" çalışan diğer tarayıcılardan daha radikal bir yaklaşım.



**Sıfır doğrulanabilir telemetri**: Orion, tasarım gereği sıfır telemetri ile gizlilik konusunda radikal bir yaklaşım benimser. Başlangıçta yüzlerce ağ isteği yapan diğer tarayıcıların aksine (IP üssü, tarayıcı parmak izi, kişisel bilgiler), Orion asla "evi aramaz". Bu temel fark, kasıtsız veri sızıntısı riskini tamamen ortadan kaldırır.



**Olağanüstü performans**: WebKit'in optimize edilmiş bir sürümünü temel alan Orion, Mac'te hız açısından Safari'ye eşit, hatta daha üstün. Speedometer 2.0/2.1 testlerinde Apple Silicon işlemcilerde sürekli olarak birinci sırada yer alıyor. Yerel reklam engelleme özelliği sayfa yüklemesini %20 ila %40 oranında hızlandırır.



**Evrensel uzantı desteği**: Büyük bir yenilik olan Orion, Chrome Web Mağazası **ve** Mozilla Eklentileri'nden uzantılar yüklemenize olanak tanır. WebExtensions desteği şu anda deneyseldir ve beta sürümünde %100 uyumluluk hedeflenmektedir. Bazıları mükemmel çalışmasa da, uBlock Origin, Bitwarden gibi birçok popüler uzantıyı iPhone'da bile kullanabilirsiniz - iOS'ta dünyada bir ilk.



### Farkında olunması gereken sınırlamalar





- Sınırlı kullanılabilirlik**: Şu anda macOS ve iOS/iPadOS için ayrılmıştır. Bir Linux sürümü geliştirme kilometre taşlarına ulaşıyor (Milestone 2 2025'te), ancak herkese açık bir yapı mevcut değil. Windows ve Android kaynak yetersizliği nedeniyle geliştirme aşamasında değildir.
- Kapalı kaynak kodu**: Bazı bileşenler açık kaynaklı olsa da, Orion ağırlıklı olarak tescilli olmaya devam ediyor ve bu da gizlilik topluluğunda bir tartışma konusu.
- Deneysel uzantılar**: Uzantı desteği beta aşamasındadır ve sık sık uyumsuzluklar yaşanmaktadır. Uzantılar performansı etkileyebilir ve bazıları hiç çalışmaz.
- WebKit güvenliği**: Chromium'un aksine WebKit, belirli senaryolarda güvenlik riskleri oluşturabilecek kadar sağlam site başına işlem yalıtımı sunmaz.
- Engelleme testleri**: Kagi bu testlerin "temelde kusurlu" olduğunu düşündüğünden, Orion çevrimiçi reklam testlerinde kasıtlı olarak düşük performans göstermektedir (%26-35). Günlük kullanımdaki gerçek etkinlik çok daha üstündür.



## Orion Browser kurulumu



### MacOS üzerinde



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Kagi ana sayfası Orion Browser'ı "tam gizlilik koruması ve evrensel uzantı desteğine sahip reklamsız bir tarayıcı "* olarak tanıtıyor





- Kagi.com/orion](https://kagi.com/orion/) adresine gidin
- "** macOS için Orion'u indirin**" üzerine tıklayın



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*MacOS ve iOS için kullanılabilirliği gösteren Orion Browser indirme sayfası ve App Store bağlantıları*





- İndirilen `.dmg` dosyasını açın
- Orion uygulamasını Uygulamalar klasörüne sürükleyin
- İlk açılışta macOS sizden açılışı onaylamanızı isteyecektir



**Alternatif Homebrew**:


```bash
brew install --cask orion
```



### IPhone/iPad'de





- Uygulama Mağazasını** açın
- "**Orion Browser by Kagi**" için arama yapın
- Ücretsiz uygulamayı yükleyin (iOS 15+ uyumlu)



### İlk yapılandırma



İlk çalıştırmada Orion sizi birkaç adımda yönlendirir:



**1. Karşılama ekranı


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion Browser karşılama ekranı temel özellikleri vurgular: daha hızlı tarama, sıfır telemetri, reklam engelleme ve uzantı desteği*



**2. Interface** özelleştirme


![Options de personnalisation](assets/fr/05.webp)


*Özelleştirme ekranı, sekmelerin ve Interface'in görünümünü tercihlerinize uyacak şekilde yapılandırmanızı sağlar*





- Veri içe aktarma**: Safari, Chrome veya Firefox'tan sık kullanılanları ve parolaları kolayca aktarın
- ICloud senkronizasyonu**: Sık kullanılanlarınızı ve sekmelerinizi tüm Apple aygıtlarınızda bulmak için etkinleştirin



**3. Mobil cihazlara kurulum**


![Installation sur iOS](assets/fr/06.webp)


*Orion Browser'ı App Store'dan hızlı bir şekilde indirmek için QR kodunu gösteren iOS kurulum ekranı*



**4. Interface karşılama ve gerekli araçlar



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface ana sayfası: ok, doğrudan Address çubuğundan erişilebilen üç temel aracı gösterir*



Yapılandırma tamamlandığında, Orion'un aerodinamik Interface'ini **üç temel aracıyla** (okla gösterilmiştir) keşfedeceksiniz:





- Shield 🛡️**: Geçerli sayfada engellenen öğelerin sayısını içeren Gizlilik Raporunu görüntüler
- Fırça 🖌️**: Sayfa görüntüsünü özelleştirin (tema, yazı tipi, dikkat dağıtıcı Elements'yı kaldırın)
- Gear ⚙️**: Web sitesine özgü parametreleri yapılandırın (izinler, engelleme, vb.)



Bu araçlar her zaman kullanılabilir ve tarama deneyiminizi site bazında kontrol etmenize olanak tanır.



**Önemli**: Orion ücretsizdir ve çalıştırmak için kayıt veya hesap oluşturma gerektirmez.



![Orion+ dans les préférences](assets/fr/08.webp)


*Tercihlerdeki Orion+ abonelik ekranı, geliştirmeyi desteklemek için isteğe bağlı bir abonelik sunuyor*



**Orion+ (isteğe bağlı)**: Proje geliştirmeyi desteklemek için Kagi, Orion+ (ayda 5 dolar, yılda 50 dolar veya ömür boyu 150 dolar) sunmaktadır. Bu gönüllü abonelik,:




- Geliştirme ekibiyle doğrudan iletişim kurun
- Tarayıcının gelişimini ihtiyaçlarınıza göre etkileyin
- En son deneysel özellikleri içeren Nightly sürümlerine erişin
- En yeni WebKit motorundan yararlanın
- Geri bildirim forumunda ayırt edici bir rozet edinin



Orion+ projenin bağımsızlığını garanti ediyor: "Finansal katkınız bağımsız kalmamıza ve kullanıcılarımız için en iyi tarayıcı olma sözümüzü tutmamıza yardımcı oluyor". Orion'un reklamsız ve telemetri içermemesini sağlayan da bu kullanıcı-fonlama modelidir.



## Maksimum gizlilik için yapılandırma



### Temel parametreler



Tercihlere **Orion → Tercihler** (veya ⌘,) aracılığıyla erişin:



**1. Arama - Özel arama motoru**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Varsayılan arama motoru yapılandırması: Maksimum gizlilik için DuckDuckGo seçilmiştir*





- Varsayılan motor**: Optimum gizlilik için **DuckDuckGo**, **Startpage** veya **Kagi** seçin (Google/Bing'den kaçının)
- Arama önerileri**: Tuş vuruşlarının arama motoru sunucularına sızmasını önlemek için bunları devre dışı bırakın



**2. Gizlilik - Genel** koruma



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orion gizlilik ayarları 119.156 aktif kurallı İçerik Engelleyiciyi, izleyici kaldırma seçeneklerini ve özel kullanıcı aracısını gösterir*



**İçerik Engelleyici varsayılan olarak etkin**:




- EasyList**: 119 binden fazla reklam engelleme kuralı
- EasyPrivacy**: İzlemeye karşı koruma
- Filtre Listelerini Yönet**: Ek listeler ekleyin (Hagezi önerilir)



**Gizlilik seçenekleri**:




- URL'lerden izleyicileri kaldırın**: "Yalnızca Özel Tarama İçin" kopyalanan bağlantıları temizler
- Kaza raporlarını paylaşın**: "Onay istedikten sonra" onayınıza saygı duyar
- Özel kullanıcı aracısı**: Belirli engellemeleri aşmak için değiştirilebilir



![YouTube avec Privacy Report](assets/fr/10.webp)


*Orion ile görüntülenen YouTube örneği: reklam görünmüyor ve birçok Elements'nin engellendiğini gösteren Gizlilik Raporu*



**3. Web Sitesi Ayarları - Siteye göre kontrol**



![Website Settings pour YouTube](assets/fr/11.webp)


*YouTube için uyumluluk seçeneklerini, içerik engellemeyi ve siteye özel izinleri gösteren Web Sitesi Ayarları*



**Hızlı erişim**: Ayarlamak için Address çubuğundaki dişli ⚙️ üzerine tıklayın:




- Uyumluluk Modu**: Uzantıları askıya alarak görüntü sorunlarını çözer
- İçerik Engelleyiciler**: Gerekirse belirli bir site için engellemeyi devre dışı bırakın
- JavaScript/Çerezler**: Siteye göre granüler kontrol
- İzinler**: Kamera, mikrofon, konum ayrı ayrı yapılandırıldı



**4. Gelişmiş Özel Filtreler** (aşağıya bakın)



**Özel filtreler oluşturun** (Gizlilik → Filtre Listelerini Yönet → Özel Filtreler):



**Basitleştirilmiş sözdizimi** (Adblock Plus uyumlu):




- `reddit.com##.promotedlink`: Sponsorlu Reddit gönderilerini gizler
- `|ads.example.com^`: Bir reklam alanını tamamen engeller
- `@||site-utile.com^`: Bir site için istisna oluşturur



**İpucu: Kullanıma hazır binlerce özel liste için [FilterLists.com](https://filterlists.com) adresini ziyaret edin.



### Önerilen uzatmalar



Orion, Chrome ve Firefox uzantılarını yerel olarak destekler. Bunları doğrudan resmi mağazalardan yükleyin:



**Essentials**:




- uBlock Origin**: Yerel engelleyiciye granüler kontrol ekler
- Bitwarden**: Açık kaynaklı parola yöneticisi
- ClearURLs**: URL izleme parametrelerini siler



**Opsiyonel**:




- LocalCDN**: Paylaşılan kütüphaneleri yerel olarak sunar
- Cookie AutoDelete**: Sekmeleri kapattıktan sonra çerezleri otomatik olarak siler
- NoScript**: JavaScript yürütme üzerinde tam kontrol (ileri düzey kullanıcılar)



Yüklemek için:




- Chrome.google.com/webstore](https://chrome.google.com/webstore) veya [addons.mozilla.org](https://addons.mozilla.org) adreslerini ziyaret edin
- "Chrome/Firefox'a Ekle" üzerine tıklayın
- Orion uzantıyı otomatik olarak yakalayacak ve yükleyecektir



**Dikkat**: Uzantı desteği deneysel olduğundan, birçok uzantı düzgün çalışmayabilir veya performansı etkileyebilir. Bir sorun olması durumunda (site artık çalışmıyor, yavaşlık), kaynağı belirlemek için uzantıları tek tek devre dışı bırakın.



## Günlük kullanım



### Interface ve benzersiz özellikler




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Ekranı özelleştirmek için Orion fırça menüsü: yazı tipi boyutu, tema (açık/koyu), yapışkan başlıkların devre dışı bırakılması ve dikkat dağıtıcı Elements'un kaldırılması*



**Fırça aracı: gelişmiş özelleştirme**



Orion'un **fırça** aracı, her web sitesinin görüntüsünü özelleştirmenizi sağlayan benzersiz bir özelliktir:



**Tema seçenekleri**:




- Her site için açık ve koyu temalar arasında geçiş yapın
- Sistem tercihlerinize otomatik adaptasyon



**Tipografik kontrol**:




- Yazı tipi boyutu**: A- ve A+ düğmeleri ile okunabilirliği ayarlayın
- Yazı tipi stili**: Yazı tipi ailesini değiştirin (varsayılan veya özel)



**Interface temizliği**:




- Yapışkan başlıkları devre dışı bırak**: Kaydırma sırasında üstte takılı kalan başlıkları kaldırır
- Elements'yi sil**: Rahatsız edici Elements'yi (reklamlar, pop-up'lar, çerez banner'ları) kalıcı olarak kaldırın
  - "+ Sil" üzerine tıklayın ve ardından gizlenecek öğeyi seçin
  - Kalıcı reklamlar veya görsel izleme içeren siteler için çok kullanışlıdır Elements



**Kalıcılık**: Tüm bu ayarlar alan adı başına kaydedilir ve bir sonraki ziyaretinizde otomatik olarak yeniden uygulanır.



**Gelişmiş sekme yönetimi**:




- Dikey sekmeler**: Menü çubuğu üzerinden etkinleştirin (Yandaki Sekmeler işlevi)
- Sıkıştırılmış sekmeler**: Yer kazanmak için Tercihler → Sekmeler → Düzen "Sıkıştır"
- Sekme grupları**: Oturumlarınızı temaya göre düzenleyin
- Çoklu profiller**: Tamamen izole edilmiş verilerle menü çubuğu (Profiller işlevi) aracılığıyla ayrı kimlikler oluşturun



**Düşük Güç Modu**: IPhone'dan esinlenen bu mod, etkin olmayan sekmeleri 5 dakika sonra otomatik olarak askıya alır ve enerji tüketimini %90'a kadar azaltabilir. Mac'te Orion'un menü çubuğundan veya iOS'ta ayarlardan etkinleştirin.



**Yerleşik araçlar** (Düzen menüsü ve diğerleri):




- Sayfadaki Metni Düzenle**: herhangi bir metni geçici olarak değiştirin (Düzenle menüsü)
- Kopyala ve Yapıştır'a İzin Ver**: Kopyalama kısıtlamalarını atlar (Düzen menüsü)
- Temiz Bağlantıyı Kopyala**: İzleme parametrelerini kaldırmak için bir bağlantıya sağ tıklayın
- Odak Modu**: dikkat dağıtmayan, tam ekran navigasyon
- Resim İçinde Resim**: Videoları kayan bir pencerede izleyin
- İnternet Arşivinde Aç**: Arşivlenmiş sürümlere doğrudan erişim
- Gizlilik Raporu**: Sayfaya göre engellenen öğeleri görmek için 🛡️ kalkanına tıklayın



### Özel tarama yönetimi



Orion'un özel navigasyonu (⌘⇧N) sunar:




- Çerezlerin ve oturumların tamamen yalıtılması
- Kapanışta otomatik silme
- Geçmiş ve önbellek devre dışı bırakma
- Parmak izine karşı geliştirilmiş koruma



**İpucu**: Gelişmiş bölümlendirme için, menü çubuğu (Profiller işlevi) aracılığıyla **ayrı profiller** oluşturun. Her profil Dock'ta ayrı bir uygulama olarak görünür ve kendi ayarları, uzantıları ve verileri tamamen izole edilmiştir.



### Performans optimizasyonu ve gizlilik



Orion'u hızlı ve gizli tutmak için:




- Uzantılar**: Katı minimum ile sınırlayın (performansı düşürebilir)
- Düşük Güç Modu**: Uzun oturumlar için etkinleştirin (%90 tasarruf mümkündür)
- Gizlilik Raporu**: Engellemeleri gerçek zamanlı olarak görmek için 🛡️ kalkanına tıklayın
- Görsel özelleştirme**: Görüntüyü uyarlamak ve dikkat dağıtan Elements'ü kaldırmak için 🖌️ fırçasını kullanın
- Temiz Bağlantıyı Kopyala**: İzleyiciler olmadan bağlantıları kopyalamak için sağ tıklayın
- Ayrı profiller**: Faaliyetlerinizi bölümlere ayırmak için özel profiller kullanın
- Web Sitesi Ayarları**: İzinleri siteye göre uyarlamak için ⚙️ dişli çarkına tıklayın
- Düzenli temizlik**: Orion aracılığıyla önbelleği temizleyin → Tarama Verilerini Temizle



## Alternatiflerle karşılaştırma



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Safari'ye karşı**: Orion, WebKit performansını korurken gelişmiş engelleyici ve uzantı desteği ile üstün koruma sunar.



**Versus Chrome**: Chrome uzantıları desteği sayesinde uyumluluktan ödün vermeden rakipsiz gizlilik.



**Firefox'a karşı**: Mac'te daha hızlı, Interface daha sezgisel, ancak daha az ayrıntılı kontrol ve açık kaynak değil.



**Brave'e karşı**: Benzer felsefe, ancak Orion kripto/BAT tartışmalarından kaçınıyor ve daha iyi Apple entegrasyonu sunuyor.



## Önerilen kullanım durumları



**İdealdir**:




- Apple kullanıcıları Safari'den daha fazla gizlilik istiyor
- Uzantılar olmadan tüm reklamları (YouTube dahil) engellemek isteyen kişiler
- Geliştiriciler, entegre gizlilik korumasına sahip WebKit geliştirme araçlarına ihtiyaç duyuyor
- IPhone kullanıcılarının mobil cihazlarında masaüstü uzantıları istemesi (benzersiz yenilik)
- Faaliyetlerini bölümlere ayırması gereken profesyoneller (çoklu profiller)
- Daha iyi pil yönetimi arayan mobil kullanıcılar (Düşük Güç Modu)



**Avoid if**:




- Genelde Windows/Linux kullanıyorsunuz (sürüm mevcut değil)
- Tehdit modeliniz için tam açık kaynak esastır
- Çalışmayabilecek belirli uzantılara bağlısınız
- Apple ekosisteminin ötesinde platformlar arası senkronizasyona ihtiyacınız var
- Kanıtlanmış, istikrarlı bir çözümü tercih ediyorsunuz (2021'den beri kalıcı beta durumu)



## Dikkat edilmesi gereken noktalar ve güvenlik



### Benzersiz güvenlik özellikleri



**Devrim niteliğinde parmak izi koruması**: Orion, sisteminizi taramadan önce parmak izi komut dosyalarının yürütülmesini tamamen engelleyen tek tarayıcıdır. Bu "komut dosyası çalışmıyor = parmak izi mümkün değil" yaklaşımı, diğer tarayıcılar tarafından kullanılan geleneksel maskeleme yöntemlerinden daha iyi performans gösterir.



**Şeffaf Beyaz Liste**: Orion, arızaları önlemek için engellemenin otomatik olarak devre dışı bırakıldığı küçük bir genel site listesi (browserbench.org, wizzair.com) tutar. Bu şeffaflık, kullanıcıların engellemenin tam olarak ne zaman ve neden hafifletildiğini anlamalarını sağlar.



**Denetlenmemiş uzantılar**: Chrome/Firefox uzantıları için destek, bu uzantılar WebKit için tasarlanmadığından ve bu ortam için özel olarak denetlenmediğinden ek riskler getirir.



### Bakım ve güncellemeler





- Otomatik güncellemeler**: Orion, macOS'ta Sparkle aracılığıyla otomatik olarak güncellenir
- Güvenlik açığı izleme**: Güvenlik yamaları için sürüm notlarını düzenli olarak kontrol edin
- Hata raporlama**: Sorunları bildirmek için [orionfeedback.org](https://orionfeedback.org) adresini kullanın




## Sonuç



Orion Browser, macOS ve iOS'ta gizlilik için önemli bir adımı temsil ediyor. Sıfır telemetri yaklaşımı, ultra verimli bir yerel engelleyici ve evrensel uzantılar için benzersiz destek ile birleştiğinde, gizlilik bilincine sahip Apple kullanıcıları için mükemmel bir seçim haline geliyor.



**Önemli**: Orion, uzantı uyumluluğu sınırlamaları ve doğal WebKit riskleri ile 2021'den beri kalıcı beta sürümünde kalmaktadır. Bu değiş tokuşları tehdit modelinize göre değerlendirin.



Mac veya iPhone'da günlük kullanım için, sınırlamalarını kabul etmeniz koşuluyla, muhtemelen Apple ekosisteminde mevcut olan gizlilik, performans ve kullanım kolaylığı arasındaki en iyi uzlaşmadır.



Unutmayın: gizliliğinizi korumak sadece tarayıcınıza bağlı değildir. Optimum çevrimiçi güvenlik için Orion'u en iyi uygulamalarla (güçlü parolalar, 2FA, gerekirse VPN) birleştirin.



## Kaynaklar ve destek



### Resmi belgeler




- Resmi web sitesi**: [kagi.com/orion](https://kagi.com/orion/)
- Tam SSS**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Topluluk forumu**: [community.kagi.com](https://community.kagi.com)
- Hata izleme**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Açık kaynaklı bileşenler
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Haberler ve güncellemeler



### Önerilen doğrulama testleri



Yapılandırmadan sonra kurulumunuzu test edin:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Parmak izi testi
- [DNS Leak Test](https://www.dnsleaktest.com/) - DNS sızıntılarını kontrol edin
- [BrowserLeaks](https://browserleaks.com/) - Eksiksiz gizlilik testleri paketi



### Plan ₿ Network üzerindeki alternatifler


Maksimum koruma için diğer kılavuzlarımıza başvurun:




- [Firefox sertleştirilmiş](https://planb.network/tutorials/computer-security/firefox) - Gelişmiş çoklu platform yapılandırması
- [Tor Browser](https://planb.network/tutorials/computer-security/tor-browser) - Tam ağ anonimliği
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - Maksimum parmak izi koruması



Tarayıcıların tarihi ve işleyişinin yanı sıra günlük hayatınızdaki başlıca dijital nesneler hakkında daha fazla bilgi edinmek istiyorsanız, sizi Plan ₿ Network'de bulunan yeni ücretsiz eğitim kursumuz SCU 202'yi keşfetmeye davet ediyorum:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1