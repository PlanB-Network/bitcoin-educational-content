---
name: SwapMarket
description: Bitcoin ve Lightning takas hizmetleri toplayıcısı
---

![cover](assets/cover.webp)



Bitcoin on-chain ve Lightning Network arasında fon transferi yapmak genellikle ya Lightning kanallarının manuel olarak açılmasını (teknik ve maliyetli) ya da KYC ile merkezi takas platformlarının kullanılmasını gerektirir. SwapMarket bir alternatif sunuyor: KYC olmadan, rekabetçi sağlayıcılar aracılığıyla güvenilir atomik takaslar.



Yenilik: sağlayıcılar aracı olmasına rağmen, HTLC (*Hash Zaman Kilitli Sözleşmeler*) fonlarınızın kontrolünüz altında kalmasını matematiksel olarak garanti eder. Birkaç sağlayıcının (Boltz, ZEUS Swaps, Eldamar, Middle Way) bir araya gelmesi fiyat rekabeti yaratır. Interface web açık kaynaklı kendi kendine barındırılabilir.



## SwapMarket nedir?



2024'te başlatılan açık kaynaklı bir toplayıcı olan SwapMarket, Bitcoin/Lightning takas sağlayıcılarının bir karşılaştırıcısı olarak işlev görür. Kullanıcı, koşulları (ücretler, likidite, limitler) anında karşılaştırır ve en uygun sağlayıcıyı seçer.



### Teknik mimari



**Ön uç istemci tarafı**: 100 istemci tarafı uygulaması (fork Boltz Web App) GitHub Pages üzerinde barındırılmaktadır. Kod, arka uç sunucusu olmadan tarayıcıda çalışır. Geçmiş yerel olarak saklanır (çerezler/önbellek). Herkese açık ve denetlenebilir kaynak kodu.



**Sağlayıcı keşfi** : Src/configs/mainnet.ts` içinde sabit kodlanmış liste. Yeni sağlayıcılar Pull Request veya e-posta yoluyla eklenir.



**Bağımsız arka uçlar**: Her sağlayıcı kendi Boltz arka ucunu işletir. Arayüz, teklifleri anında karşılaştırmak için API'leri gerçek zamanlı olarak sorgular.



**HTLC Atomik Takaslar**: Hash Zaman Kilitli Sözleşmeler atomikliği garanti eder: ya takas gerçekleşir ya da her bir taraf fonlarını geri alır. Karşı taraf riski matematiksel olarak ortadan kaldırılmıştır.



### Felsefe



SwapMarket, ücretler ve likidite için sağlayıcılar arasında rekabet yaratarak merkezileşmeyi azaltır. KYC yok, açık kaynaklı kendi kendine barındırılabilir kod, tek hata noktalarını önlemek için bağımsız operatörlerin çoğaltılması.



## Ana Özellikler



### Sağlayıcı Pazaryeri



Arayüz tüm aktif sağlayıcıları görüntüler: sağlayıcının adı, uygulanan ücretler (yüzde ve/veya sabit), mevcut minimum/maksimum tutarlar ve desteklenen takas türleri. Uygulama, teklifleri gerçek zamanlı olarak almak için yapılandırma dosyasında başvurulan her sağlayıcının API'lerini doğrudan sorgular. Sağlayıcılar arasındaki rekabet, standart swaplar için genellikle %0,5 civarında olan optimum oranları garanti eder.



### Çift yönlü takaslar



**Swap-in (on-chain → Lightning)**: on-chain BTC'leri Lightning satoshilerine dönüştürün. Kullanım alanı: Mobil bir wallet Lightning'e güç sağlamak, bir düğümde gelen kapasiteyi elde etmek veya anında likiditeye sahip olmak.



**Swap-out (Lightning → on-chain)**: Lightning satoshilerini on-chain BTC'ye dönüştürün. Kullanım durumu: Bir wallet Lightning'i soğuk depoya boşaltın veya katmanlar arasında likiditeyi yeniden dengeleyin.



### Güvenlik ve kurtarma



**Trustless atomik takaslar**: HTLC'ler ya takasın tam olarak tamamlanmasını ya da her bir tarafın hissesini geri almasını garanti eder. Karşı taraf riski matematiksel olarak ortadan kaldırılmıştır.



**Geri ödeme mekanizması**: Her takasın bir zaman kilidi vardır. Takas başarısız olursa, fonlar sürenin dolmasından sonra otomatik olarak iade edilebilir. Kullanıcı her zaman bitcoinlerini geri alma seçeneğini elinde tutar.



**Kurtarma anahtarları**: SwapMarket, devam eden takaslar için kurtarma anahtarlarını dışa aktarmanıza olanak tanır. Bir sorun olması durumunda, bu anahtarlar herhangi bir cihazdan takası sonlandırmak veya iptal etmek için kullanılabilir.



## Kurulum ve erişim



### Interface web



SwapMarket kurulum gerektirmez. Erişim tarayıcı üzerinden https://swapmarket.github.io adresini ziyaret ederek sağlanır. Maksimum gizlilik için Brave, izleme karşıtı uzantılara sahip Firefox veya LibreWolf kullanın. Ağ anonimliği için Tor Browser önerilir.



Kayıt, e-posta veya kimlik doğrulaması gerekmez.



### Kendi kendine barındırma (isteğe bağlı)



Resmi GitHub Pages etki alanına herhangi bir bağımlılığı ortadan kaldırmak isteyen teknik kullanıcılar için SwapMarket yerel olarak çalıştırılabilir :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Docker aracılığıyla** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Uygulamaya `http://localhost:3000` adresinden erişilebilecektir. Kendi kendine barındırma, arayüz üzerinde tam kontrolü garanti eder, resmi alanın sansürlenmesi riskini ortadan kaldırır ve kaynak kodunun yürütülmeden önce denetlenmesine olanak tanır.



### İlk yapılandırma



**Wallet Lightning**: Çalışır durumda bir wallet Lightning'iniz (Phoenix, Zeus, BlueWallet, vb.) olduğundan emin olun. Takas için generate bir Lightning faturası ödeyeceksiniz. Takaslar için bir Lightning faturası ödeyeceksiniz.



**Wallet on-chain**: Takas girişleri için, para göndermek üzere bir wallet Bitcoin on-chain'ye ihtiyacınız olacaktır. Takaslar için bir Bitcoin alıcı adresi hazırlayın.



**İsteğe bağlı yapılandırma**: SwapMarket takas geçmişini ve tercihlerini tarayıcı çerezlerinde saklar. Hesap oluşturmaya gerek yoktur.



## Ayarlara ve Kurtarma Anahtarına erişim



İlk takaslarınızı yapmadan önce, **Kurtarma Anahtarınızı** indirmenizi şiddetle tavsiye ederiz. Bu acil durum anahtarı, teknik bir sorun veya cihazınıza erişim kaybı durumunda fonlarınızı kurtarmanızı sağlar.



### Erişim parametreleri



SwapMarket ana sayfasından, arayüzün sağ üst köşesinde, takas formunun yanında bulunan dişli simgesine (⚙️) tıklayın.



![Accès aux paramètres](assets/fr/01.webp)



### Sayfa Ayarları



Ayarlar sayfası açılır ve çeşitli yapılandırma seçenekleri görüntülenir:





- Mezhep**: BTC veya sats seçimi
- Ondalık Ayırıcı**: Ondalık ayırıcı (, veya .)
- Sesli/Tarayıcı Bildirimleri**: Ses ve tarayıcı bildirimleri
- Kurtarma Anahtarı** : Kurtarma anahtarını indirin
- Günlükler**: Günlükleri görüntüleyin, indirin veya silin



![Page Settings](assets/fr/02.webp)



### Kurtarma Anahtarını İndirin



"Rescue Key "in yanındaki **Download** düğmesine tıklayın.



**Önemli noktalar** :




- Kurtarma Anahtarı, gelecekteki tüm takaslarınız için çalışan bir **tek duraklı acil durum anahtarıdır**
- Bu anahtarı **güvenli ve kalıcı** bir yerde saklayın (şifre yöneticisi, dijital kasa)
- Bir takas sorunu (zaman aşımı, teknik arıza) durumunda, bu anahtar fonlarınızı kurtarmanıza olanak tanır



## Adım adım takas oluşturma



### Değiştirme: Yıldırım → Bitcoin



Bu ilk örnek Lightning satoshilerinin on-chain bitcoinlerine nasıl dönüştürüleceğini göstermektedir.



**Adım 1: Yapılandırmayı değiştirin



Ana sayfadan takas formunu seçin :




- LIGHTNING** (üst alan): sats Lightning olarak göndermek istediğiniz miktarı girin (örnek: 30.000 sats)
- BITCOIN** (alt alan): Ücretler düşüldükten sonra alacağınız miktar otomatik olarak görüntülenir (örnek: 29,320 sats)



En alttaki alana, parayı almak istediğiniz **receiving Bitcoin adresinizi** yapıştırın. Bu adresi dikkatlice kontrol edin.



Varsayılan sağlayıcı genellikle Boltz Exchange'dir. Ağ ücretleri ve sağlayıcı ücretleri açıkça gösterilir.



![Configuration swap-out](assets/fr/03.webp)



**2. Adım: Sağlayıcı seçimi**



Mevcut tüm likidite sağlayıcılarını görüntülemek için sağlayıcı açılır menüsüne (varsayılan: "Boltz Exchange") tıklayın.



Bir karşılaştırma tablosu görüntüleyen modal bir pencere açılır:




- Durum**: Sağlayıcı aktifse Green göstergesi
- Takma ad**: Sağlayıcı adı (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Ücret**: Sağlayıcı tarafından uygulanan ücretler (genellikle %0,49 ile %0,5 arasında)
- Maksimum Takas**: Bir takas için kabul edilen maksimum miktar



Ücretleri ve azami tutarları karşılaştırın, ardından istediğiniz sağlayıcıyı seçin.



**Lütfen dikkat**: Sağlayıcı seçim arayüzü her bir sağlayıcı için **minimum tutarları** göstermez. Bu bilgi yalnızca bir sağlayıcı seçildikten sonra takas oluşturma arayüzünde görünür. Minimum ve maksimum tutarlar sağlayıcıdan sağlayıcıya değişebilir ve zaman içinde değişebilir. **Takas sırasında her zaman bu limitleri kontrol edin**: takas etmek istediğiniz miktar bir sağlayıcının limitlerinin dışındaysa, işleminiz için daha uygun başka bir sağlayıcı seçebilirsiniz.



![Sélection du provider](assets/fr/04.webp)



**3. Adım: Swap oluşturma ve Lightning** ödemesi



Sarı renkli **"ATOMİK TAKAS OLUŞTUR "** düğmesine tıklayın. SwapMarket, generate Lightning'inizden ödemeniz için bir **Lightning faturası** (BOLT11) oluşturacaktır.



Sayfa görüntülenir :




- Takas Kimliği**: Benzersiz takas tanımlayıcısı (örnek: J4ymFIMVR6Hm)
- Durum**: "swap.created" (takas oluşturuldu, ödeme bekleniyor)
- QR kodu**: wallet Lightning'iniz ile tarayın
- Invoice Lightning**: "lnbc" ile başlayan karakter dizisi (örnek: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Bu faturayı wallet Lightning'inizden (Phoenix, Zeus, BlueWallet, vb.) ödeyin. Ödenecek tam tutar görüntülenir (örnek: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**4. Adım: Onay ve kabul**



Lightning ödemesi onaylandıktan sonra, SwapMarket ödemenizi anında alır ve sağlayıcı Bitcoin işlemini adresinize yayınlar.



Durum **"invoice.settled "** (fatura ödendi) olarak değişir ve bir onay mesajı görüntülenir.



on-chain bitcoinleriniz, işlem onaylanır onaylanmaz (sağlayıcı tarafından seçilen mining ücretlerine bağlı olarak genellikle birkaç dakika ila birkaç saat arasında) kullanılabilir olacaktır.



![Confirmation swap-out](assets/fr/06.webp)



Bitcoin işlemini bir blok zinciri tarayıcısında görüntülemek için **"TALEP İŞLEMİNİ AÇ "** seçeneğine tıklayabilirsiniz.



### Değiştirin: Bitcoin → Yıldırım



Bu ikinci örnek, on-chain bitcoinlerinin Lightning satoshilerine nasıl dönüştürüleceğini göstermektedir.



**Adım 1: Yapılandırmayı değiştirin



Ana sayfadan takas formunu seçin :




- BITCOIN** (üst alan): sats Bitcoin cinsinden göndermek istediğiniz miktarı girin (örnek: 63.400 sats)
- AYDINLATMA** (alt alan): Ücretler düşüldükten sonra alacağınız miktar otomatik olarak görüntülenir (örnek: 62 884 sats)



Alt alana, wallet Lightning'inizden oluşturulan bir Lightning** faturası (BOLT11) yapıştırın veya wallet'niz destekliyorsa LNURL adresinizi kullanın.



![Configuration swap-in](assets/fr/07.webp)



**2. Adım: Kurtarma Anahtarı kontrolü**



"ATOMİK TAKAS OLUŞTUR "** seçeneğine tıkladıktan sonra, Kurtarma Anahtarınızı doğrulamanızı isteyen modal bir pencere belirir.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Kurtarma Anahtarı**: İlk yapılandırma sırasında kurtarma anahtarınızı zaten yüklediğinizden (önceki bölüme bakın), kaydettiğiniz anahtarı içe aktarmak için **"MEVCUT ANAHTARI DOĞRULA "** düğmesine tıklayın.



Önceden indirilmiş Kurtarma Anahtarı dosyasını seçin. Başarılı doğrulamanın ardından arayüz otomatik olarak bir sonraki adıma geçer.



**3. Adım: Bitcoin** para yatırma adresi



SwapMarket artık Lightning faturanıza bağlı HTLC sözleşmesini içeren **benzersiz bir Bitcoin adresi** oluşturuyor.



Sayfa görüntülenir :




- Takas Kimliği**: Benzersiz tanımlayıcı (örnek: 1kGmB6JyGqU4)
- Durum**: "invoice.set" (fatura ayarlandı, ödeme bekleniyor Bitcoin)
- QR kodu**: Bitcoin depo adresi
- Bitcoin** adresi: Genellikle "bc1p..." ile başlar (örnek: bc1p5mvtwxapjkds...9d4n9f)
- Sarı renkte uyarı** : "İşleminizin bu takasın oluşturulmasından sonra ~24 saat içinde onaylandığından emin olun!"



Bu ~24 saatlik süre, HTLC sözleşmesinin **zaman aşımı** süresidir. Bitcoin işleminiz bu süre içinde onaylanmazsa, takas başarısız olur ve paranızı kurtarmak için Kurtarma Anahtarınızı kullanmanız gerekir.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Adresi **"ADRES "** düğmesine tıklayarak kopyalayabilir veya QR kodunu doğrudan wallet on-chain cihazınızdan tarayabilirsiniz.



**4. Adım: Bitcoin gönderme**



wallet Bitcoin on-chain'ünüzden, belirtilen miktarı (örneğin 63.400 sats) oluşturulan adrese **tam olarak** gönderin.



**Önemli**: Hızlı onayı garanti etmek için uygun mining ücretlerini kullanın. Ücret çok düşükse ve işlem zaman aşımından (~24 saat) sonra mempool'da kalırsa, takas başarısız olur.



İşlem gönderildikten sonra, SwapMarket işlemin mempool'da olduğunu algılar ve :




- Durum** : "transaction.mempool
- Mesaj**: "İşlem mempool'da - Takasın tamamlanması için onay bekleniyor"



![Transaction en mempool](assets/fr/10.webp)



**Adım 5: Onay ve Yıldırım** alımı



Bitcoin işlemi ilk onayını alır almaz, sağlayıcı otomatik olarak Lightning faturanızı öder. wallet Lightning'inizdeki satoshileri anında alırsınız.



Durum **"transaction.claim.pending "** olarak değişir, ardından bir onay mesajı görüntülenir:



![Confirmation swap-in](assets/fr/11.webp)



Yıldırım satoshileriniz hemen wallet'inizde kullanılabilir.



## Avantajlar ve sınırlamalar



### Avantajlar



**Ücret rekabeti**: Sağlayıcıların bir araya gelmesi, ücretleri aşağı çeken doğal bir rekabet yaratır (%0,49 ila %0,5).



**Gizlilik**: KYC yok, %100 istemci tarafı arayüz (kişisel veri aktarımı yok), Tor Browser uyumlu.



**Velayetsiz**: HTLC, fonlarınızın münhasır kontrolünü matematiksel olarak garanti eder. Ya takas başarılı olur ya da bitcoinlerinizi geri alırsınız.



**Açık kaynaklı kendi kendine barındırılabilir**: denetlenebilir kamu kodu, sansüre karşı maksimum direnç için yerel olarak dağıtılabilir.



### Sınırlamalar



**Sınırlı likidite**: Sınırlı sayıda aktif sağlayıcı (döneme bağlı olarak Boltz, Eldamar, MiddleWay). Maksimum tutarlar sınırlı olabilir.



**Son kullanma süresi**: 24 saat ila 48 saat arasında zaman aşımı. on-chain işlemi sona ermeden önce onaylanmazsa, manuel kurtarma gerekir.



**Interface merkezileştirme**: Kendi kendine barındırılabilir olmasına rağmen, resmi arayüz GitHub Pages üzerinde barındırılmaktadır. GitHub depoyu sansürlerse, swapmarket.github.io üzerinden erişim engellenecektir (çözüm: kendi kendini barındırma).



**on-chain İzleri**: HTLC komut dosyaları gelişmiş blok zinciri analizi ile potansiyel olarak tanımlanabilir.



## En iyi uygulamalar



### Güvenli yapılandırma



**Kurtarma Anahtarınızı indirin**: İlk takaslarınızdan önce, Kurtarma Anahtarınızı Ayarlar'dan indirin (yukarıdaki özel bölüme bakın). Bu benzersiz anahtar, gelecekteki tüm takaslarınız için çalışacak ve bir sorun olması durumunda fonlarınızı kurtarmanızı sağlayacaktır.



**Tor Tarayıcı Kullanın**: Maksimum gizlilik için, IP adresinizi gizlemek amacıyla SwapMarket'e Tor Browser üzerinden erişin.



**Kendi kendini barındırmayı düşünün**: Teknik kullanıcılar için kendi SwapMarket örneğinizi çalıştırmak, resmi GitHub Pages etki alanına bağımlılığı ortadan kaldırır.



### Takas optimizasyonu



**Mempool'a göz kulak olun**: Bir takastan önce mempool.space dosyasını kontrol edin. mining maliyetlerini en aza indirmek için etkinliğin düşük olduğu zamanları seçin.



**Adresleri kontrol edin**: Takaslar için alıcı adresinizi titizlikle kontrol edin. Kopyala ve yapıştır yöntemini kullanın ve ilk 5 ve son 5 karakteri kontrol edin.



**Küçük miktarlarla test edin**: İzin verilen minimum miktarla başlayın (25.000 ila 50.000 sats). Süreçte ustalaştıktan sonra kademeli olarak artırın.



**Takaslarınızı belgeleyin**: Her bir takasın kimliğini, itfa adresini ve son kullanma tarihini not edin. Bu bilgiler, teknik bir sorun olması durumunda takibi ve kurtarmayı kolaylaştırır.



### Kullanım stratejisi



**Nakit akışınızı dengeleyin**: on-chain (tasarruf, uzun vadeli güvenlik) ve Lightning (günlük harcamalar, anlık ödemeler) arasındaki dağılımınızı gerçek ihtiyaçlarınıza göre ayarlamak için SwapMarket'i kullanın.



**Kârlılığı hesaplayın**: Kalıcı Lightning likidite ihtiyaçları için, doğrudan bir Lightning kanalı açmak yerine tekrarlanan takasların kümülatif maliyetini karşılaştırın. SwapMarket, büyük düzenli akışlar için değil, tek seferlik ayarlamalar için mükemmeldir.



## SwapMarket vs Boltz: Aradaki fark nedir?



### Boltz: Teknoloji ve Hizmet



**Boltz, Bitcoin, Lightning ve Liquid arasında HTLC aracılığıyla atomik takasları uygulayan açık kaynak teknolojisidir** (GitHub'da `boltz-backend`).



**Kritik nokta**: Tüm SwapMarket sağlayıcıları (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) Boltz arka ucunun kendi örneklerini kullanmaktadır. Bu nedenle altta yatan teknoloji aynıdır. Boltz arka ucundaki bir güvenlik açığı potansiyel olarak tüm sağlayıcıları etkileyecektir, ancak sistemin açık kaynaklı yapısı topluluk denetimine izin vermektedir.



**Boltz Exchange** Boltz ekibi tarafından işletilen tek bir hizmettir, **SwapMarket** ise hepsi Boltz teknolojisini kullanan birkaç sağlayıcıyı bir araya getirerek rekabetçi bir fiyatlandırma ortamı yaratır.



Daha fazla ayrıntı için Boltz ve Zeus Takası eğitimlerimize bakın:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Temel farklılıklar



| Açıklık       | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Doğa          | Benzersiz hizmet     | Çok sağlayıcılı toplayıcı            |
| Sağlayıcılar  | Yalnızca Boltz       | Boltz, ZEUS, Eldamar, Middle Way     |
| Rekabet       | Sabit ücretler        | Serbest rekabet                      |
| Arayüz        | boltz.exchange       | swapmarket.github.io (kendin-barındırılabilir) |
| Güvenlik      | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**SwapMarket avantajları**: Fiyat rekabeti, arka uç örneklerinin çeşitlendirilmesi, gerçek zamanlı karşılaştırma.



**Teknolojik alternatifler** (SwapMarket uyumlu değil): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Bu çözümler kendi denizaltı takas uygulamalarını kullanmaktadır.



**Öneri**: Basitlik için Boltz Exchange veya rekabet yoluyla maliyetleri optimize etmek için SwapMarket kullanın. Her ikisi de güvenlik açısından eşdeğerdir (HTLC gözetim altında değildir).



## Sonuç



SwapMarket, birden fazla sağlayıcıyı tek bir arayüzde toplayarak Bitcoin/Lightning borsalarını kolaylaştırır. HTLC mimarisi, takasların gözetim dışı doğasını garanti eder, KYC'nin olmaması gizliliği korur ve kendi kendine barındırılabilir açık kaynak kodu sansüre karşı direnci güçlendirir.



Sağlayıcılar arasındaki rekabet oranları iyileştirir ve likidite kaynaklarını çoğaltır. İki katmanlı yönetimi (on-chain tasarrufları, Lightning giderleri) optimize etmek için SwapMarket, finansal egemenliği ve gizliliği koruyan pratik bir araçtır.



## Kaynaklar



### Resmi belgeler




- [SwapMarket - Web uygulaması](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Teknik dokümantasyon](https://docs.boltz.exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### İlgili projeler




- [Boltz Exchange](https://boltz.exchange) - Orijinal atomik takas hizmeti
- [ZEUS Swaps](https://zeusln.com) - Yıldırım takas sağlayıcısı