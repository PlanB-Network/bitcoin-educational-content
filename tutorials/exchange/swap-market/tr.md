---
name: SwapMarket
description: Bitcoin ve Lightning takas hizmetleri toplayıcısı
---

![cover](assets/cover.webp)



Bitcoin On-Chain ve Lightning Network arasında fon transferi yapmak genellikle ya Lightning kanallarının manuel olarak açılmasını (teknik ve maliyetli) ya da KYC ile merkezi takas platformlarının kullanılmasını gerektirir. SwapMarket bir alternatif sunuyor: KYC olmadan rekabetçi sağlayıcılar aracılığıyla Trustless atomik swaplar.



Yenilik: sağlayıcılar aracı olmasına rağmen, HTLC (*Hash Zaman Kilitli Sözleşmeler*) fonlarınızın kontrolünüz altında kalmasını matematiksel olarak garanti eder. Birkaç sağlayıcının (Boltz, ZEUS Swaps, Eldamar, Middle Way) bir araya gelmesi fiyat rekabeti yaratır. Interface web açık kaynaklı kendi kendine barındırılabilir.



## SwapMarket nedir?



2024'te başlatılan açık kaynaklı bir toplayıcı olan SwapMarket, Bitcoin/Lightning takas sağlayıcılarının bir karşılaştırıcısı olarak işlev görür. Kullanıcı, koşulları (ücretler, likidite, limitler) anında karşılaştırır ve en uygun sağlayıcıyı seçer.



### Teknik mimari



**Ön uç istemci tarafı**: 100 istemci tarafı uygulaması (Fork Boltz Web App) GitHub Pages üzerinde barındırılmaktadır. Kod, arka uç sunucusu olmadan tarayıcıda çalışır. Geçmiş yerel olarak saklanır (çerezler/önbellek). Herkese açık ve denetlenebilir kaynak kodu.



**Sağlayıcı keşfi** : Hard kodlu liste `src/configs/Mainnet.ts` içinde. Yeni sağlayıcılar Pull Request veya e-posta yoluyla eklenir.



**Bağımsız arka uçlar**: Her sağlayıcı kendi Boltz arka ucunu çalıştırır. Interface, teklifleri anında karşılaştırmak için API'leri gerçek zamanlı olarak sorgular.



**HTLC Atomik Takaslar**: Hash Zaman Kilitli Sözleşmeler atomikliği garanti eder: ya takas gerçekleşir ya da her bir taraf fonlarını geri alır. Karşı taraf riski matematiksel olarak ortadan kaldırılmıştır.



### Felsefe



SwapMarket, ücretler ve likidite için sağlayıcılar arasında rekabet yaratarak merkezileşmeyi azaltır. KYC yok, açık kaynaklı kendi kendine barındırılabilir kod, tek hata noktalarını önlemek için bağımsız operatörlerin çoğaltılması.



## Ana Özellikler



### Sağlayıcı Pazaryeri



Interface tüm aktif sağlayıcıları görüntüler: sağlayıcının adı, uygulanan ücretler (yüzde ve/veya sabit), mevcut minimum/maksimum tutarlar ve desteklenen takas türleri. Uygulama, teklifleri gerçek zamanlı olarak almak için yapılandırma dosyasında başvurulan her sağlayıcının API'lerini doğrudan sorgular. Sağlayıcılar arasındaki rekabet, standart swaplar için genellikle %0,5 civarında olan optimum oranları garanti eder.



### Çift yönlü takaslar



**Swap-in (On-Chain → Lightning)**: On-Chain BTC'lerini Lightning satoshilerine dönüştürün. Kullanım alanı: Mobil bir Wallet Lightning'e güç sağlamak, bir düğümde gelen kapasiteyi elde etmek veya anında likiditeye sahip olmak.



**Swap-out (Lightning → On-Chain)**: Lightning satoshilerini On-Chain BTC'ye dönüştürün. Kullanım durumu: Wallet Lightning'i Cold deposuna boşaltın veya katmanlar arasında likiditeyi yeniden dengeleyin.



### Güvenlik ve kurtarma



**Trustless Atomik Takaslar: HTLC, Exchange'nin tam olarak tamamlanmasını ya da her bir tarafın hissesini geri almasını garanti eder. Karşı taraf riski matematiksel olarak ortadan kaldırılmıştır.



**Geri ödeme mekanizması**: Her takasın bir son kullanma tarihi vardır (TIMELOCK). Takas başarısız olursa, fonlar sona erdikten sonra otomatik olarak iade edilebilir. Kullanıcı her zaman bitcoinlerini geri alma seçeneğini elinde tutar.



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



Uygulamaya `http://localhost:3000` adresinden erişilebilecektir. Kendi kendine barındırma, Interface üzerinde tam kontrolü garanti eder, resmi alanın sansürlenmesi riskini ortadan kaldırır ve kaynak kodunun yürütülmeden önce denetlenmesine olanak tanır.



### İlk yapılandırma



**Wallet Lightning**: Çalışan bir Wallet Lightning'iniz olduğundan emin olun (Phoenix, Zeus, BlueWallet, vb.). Takas için generate bir Lightning Invoice ödeyeceksiniz. Takaslar için bir Lightning Invoice ödeyeceksiniz.



**Wallet On-Chain**: Takas işlemlerinde, para göndermek için bir Wallet Bitcoin On-Chain'e ihtiyacınız olacaktır. Takaslar için, Bitcoin alan bir Address hazırlayın.



**İsteğe bağlı yapılandırma**: SwapMarket takas geçmişini ve tercihlerini tarayıcı çerezlerinde saklar. Hesap oluşturmaya gerek yoktur.



## Ayarlara ve Kurtarma Anahtarına erişim



İlk takaslarınızı yapmadan önce, **Kurtarma Anahtarınızı** indirmenizi şiddetle tavsiye ederiz. Bu acil durum anahtarı, teknik bir sorun veya cihazınıza erişim kaybı durumunda fonlarınızı kurtarmanızı sağlar.



### Erişim parametreleri



SwapMarket ana sayfasından, Interface'in sağ üst köşesinde, takas formunun yanındaki dişli simgesine (⚙️) tıklayın.



![Accès aux paramètres](assets/fr/01.webp)



### Sayfa Ayarları



Ayarlar sayfası açılır ve çeşitli yapılandırma seçenekleri görüntülenir:





- Mezhep**: BTC veya Sats arasında seçim
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



### Değiştir: Yıldırım → Bitcoin



Bu ilk örnek Lightning satoshilerinin On-Chain bitcoinlerine nasıl dönüştürüleceğini göstermektedir.



**Adım 1: Yapılandırmayı değiştirin



Ana sayfadan takas formunu seçin :




- LIGHTNING** (üst alan): Sats Lightning olarak göndermek istediğiniz miktarı girin (örnek: 30.000 Sats)
- Bitcoin** (alt alan): Ücretler düşüldükten sonra alacağınız miktar otomatik olarak görüntülenir (örnek: Sats 29,320)



En alttaki alana, fonları almak istediğiniz **alıcı Bitcoin Address**'nizi yapıştırın. Bu Address'yi dikkatlice kontrol edin.



Varsayılan sağlayıcı genellikle Boltz Exchange'tür. Ağ ücretleri ve sağlayıcı ücretleri açıkça gösterilir.



![Configuration swap-out](assets/fr/03.webp)



**2. Adım: Sağlayıcı seçimi**



Mevcut tüm likidite sağlayıcılarını görüntülemek için sağlayıcı açılır menüsüne (varsayılan: "Boltz Exchange") tıklayın.



Bir karşılaştırma tablosu görüntüleyen modal bir pencere açılır:




- Durum**: Sağlayıcı aktifse Green göstergesi
- Takma ad**: Sağlayıcı adı (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Ücret**: Sağlayıcı tarafından uygulanan ücretler (genellikle %0,49 ile %0,5 arasında)
- Maksimum Takas**: Bir takas için kabul edilen maksimum miktar



Ücretleri ve azami tutarları karşılaştırın, ardından istediğiniz sağlayıcıyı seçin.



**Lütfen dikkat**: Sağlayıcı seçimi Interface her bir sağlayıcı için **minimum tutarları** göstermez. Bu bilgi yalnızca bir sağlayıcı seçildikten sonra takas oluşturma Interface'de görünür. Minimum ve maksimum tutarlar sağlayıcıdan sağlayıcıya değişebilir ve zaman içinde değişebilir. **Takas sırasında her zaman bu limitleri kontrol edin**: takas etmek istediğiniz miktar bir sağlayıcının limitlerinin dışındaysa, işleminiz için daha uygun başka bir sağlayıcı seçebilirsiniz.



![Sélection du provider](assets/fr/04.webp)



**3. Adım: Swap oluşturma ve Lightning** ödemesi



Sarı renkli **"ATOMİK TAKAS OLUŞTUR "** düğmesine tıklayın. SwapMarket, generate Lightning'inizden ödemeniz için bir **Lightning Invoice** (BOLT11) Wallet yapacaktır.



Sayfa görüntülenir :




- Takas Kimliği**: Benzersiz takas tanımlayıcısı (örnek: J4ymFIMVR6Hm)
- Durum**: "swap.created" (takas oluşturuldu, ödeme bekleniyor)
- QR kodu**: Wallet Lightning'iniz ile tarayın
- Invoice Lightning**: "lnbc" ile başlayan karakter dizisi (örnek: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Bu Invoice'ü Wallet Lightning'inizden (Phoenix, Zeus, BlueWallet, vb.) ödeyin. Ödenecek tam tutar görüntülenir (örnek: 30.000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**4. Adım: Onay ve kabul**



Lightning ödemesi onaylandıktan sonra, SwapMarket ödemenizi anında alır ve sağlayıcı Bitcoin işlemini Address'inize yayınlar.



Durum **"Invoice.settled "** (Invoice ödendi) olarak değişir ve bir onay mesajı görüntülenir.



On-Chain bitcoinleriniz, işlem onaylanır onaylanmaz (sağlayıcı tarafından seçilen Mining ücretlerine bağlı olarak genellikle birkaç dakika ila birkaç saat içinde) kullanılabilir olacaktır.



![Confirmation swap-out](assets/fr/06.webp)



Bitcoin işlemini bir Blockchain gezgininde görüntülemek için **"TAZMİNAT İŞLEMİNİ AÇ "** seçeneğine tıklayabilirsiniz.



### Değiştirin: Bitcoin → Lightning



Bu ikinci örnek, On-Chain bitcoinlerinin Lightning satoshilerine nasıl dönüştürüleceğini göstermektedir.



**Adım 1: Yapılandırmayı değiştirin



Ana sayfadan takas formunu seçin :




- Bitcoin** (üst alan): Sats Bitcoin'de göndermek istediğiniz tutarı girin (örnek: 63.400 Sats)
- AYDINLATMA** (alt alan): Ücretler düşüldükten sonra alacağınız miktar otomatik olarak görüntülenir (örnek: 62 884 Sats)



Alt alana, Wallet Lightning'inizden oluşturulan bir Lightning** Invoice (BOLT11) yapıştırın veya Wallet'niz destekliyorsa LNURL Address'inizi kullanın.



![Configuration swap-in](assets/fr/07.webp)



**2. Adım: Kurtarma Anahtarı kontrolü**



"ATOMİK TAKAS OLUŞTUR "** seçeneğine tıkladıktan sonra, Kurtarma Anahtarınızı doğrulamanızı isteyen modal bir pencere belirir.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Kurtarma Anahtarı**: İlk yapılandırma sırasında kurtarma anahtarınızı zaten yüklediğinizden (önceki bölüme bakın), kaydettiğiniz anahtarı içe aktarmak için **"MEVCUT ANAHTARI DOĞRULA "** düğmesine tıklayın.



Önceden indirilmiş Kurtarma Anahtarı dosyasını seçin. Başarılı doğrulamanın ardından Interface otomatik olarak bir sonraki adıma geçer.



**3. Adım: Bitcoin** depozito Address



SwapMarket artık Lightning Invoice'unuza bağlı HTLC Contract'yı içeren **benzersiz bir Bitcoin Address** oluşturuyor.



Sayfa görüntülenir :




- Takas Kimliği**: Benzersiz tanımlayıcı (örnek: 1kGmB6JyGqU4)
- Durum** : "Invoice.set" (Invoice ayarlandı, Bitcoin ödemesi bekleniyor)
- QR kodu**: Bitcoin depo Address
- Bitcoin** Address: Genellikle "bc1p..." ile başlar (örnek: bc1p5mvtwxapjkds...9d4n9f)
- Sarı renkte uyarı** : "İşleminizin bu takasın oluşturulmasından sonra ~24 saat içinde onaylandığından emin olun!"



Bu ~24 saatlik süre HTLC Contract'nin **zaman aşımı** süresidir. Bitcoin işleminiz bu süre içinde onaylanmazsa, takas başarısız olur ve paranızı kurtarmak için Kurtarma Anahtarınızı kullanmanız gerekir.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Address'i **"Address"** düğmesine tıklayarak kopyalayabilir veya QR kodunu doğrudan Wallet On-Chain'ınızdan tarayabilirsiniz.



**4. Adım: Bitcoin gönderme**



Wallet Bitcoin On-Chain'ünüzden, oluşturulan Address'e **tam olarak** belirtilen miktarı (örneğin 63.400 Sats) gönderin.



**Önemli**: Hızlı onayı garanti etmek için uygun Mining ücretlerini kullanın. Ücret çok düşükse ve işlem zaman aşımından (~24 saat) sonra Mempool'de kalırsa, takas başarısız olur.



İşlem gönderildikten sonra, SwapMarket işlemin Mempool'de olduğunu algılar ve :




- Durum** : "işlem.Mempool"
- Mesaj**: "İşlem Mempool'de - Takasın tamamlanması için onay bekleniyor"



![Transaction en mempool](assets/fr/10.webp)



**Adım 5: Onay ve Yıldırım** alımı



Bitcoin işlemi ilk onayını alır almaz, sağlayıcı otomatik olarak Lightning Invoice'ünüzü öder. Wallet Lightning'inizdeki satoshileri anında alırsınız.



Durum **"transaction.claim.pending "** olarak değişir, ardından bir onay mesajı görüntülenir:



![Confirmation swap-in](assets/fr/11.webp)



Lightning satoshileriniz Wallet'nızda hemen kullanılabilir.



## Avantajlar ve sınırlamalar



### Avantajlar



**Ücret rekabeti**: Sağlayıcıların bir araya gelmesi, ücretleri aşağı çeken doğal bir rekabet yaratır (%0,49 ila %0,5).



**Gizlilik**: KYC yok, Interface %100 istemci tarafı (kişisel veri aktarımı yok), Tor Browser uyumlu.



**Velayetsiz**: HTLC, fonlarınızın münhasır kontrolünü matematiksel olarak garanti eder. Ya takas başarılı olur ya da bitcoinlerinizi geri alırsınız.



**Açık kaynaklı kendi kendine barındırılabilir**: denetlenebilir kamu kodu, sansüre karşı maksimum direnç için yerel olarak dağıtılabilir.



### Sınırlamalar



**Sınırlı likidite**: Sınırlı sayıda aktif sağlayıcı (döneme bağlı olarak Boltz, Eldamar, MiddleWay). Maksimum tutarlar sınırlı olabilir.



**Son kullanma süresi**: 24 saat ila 48 saat arasında zaman aşımı. On-Chain işlemi sona ermeden önce onaylanmazsa, manuel kurtarma gerekir.



**Interface merkezileştirme**: Kendi kendine barındırılabilir olmasına rağmen, resmi Interface GitHub Pages üzerinde barındırılmaktadır. GitHub depoyu sansürlerse, swapmarket.github.io üzerinden erişim engellenecektir (çözüm: kendi kendine barındırma).



**On-Chain izleri**: HTLC komut dosyaları gelişmiş Blockchain analizi ile potansiyel olarak tanımlanabilir.



## En iyi uygulamalar



### Güvenli yapılandırma



**Kurtarma Anahtarınızı indirin**: İlk takaslarınızdan önce, Kurtarma Anahtarınızı Ayarlar'dan indirin (yukarıdaki özel bölüme bakın). Bu benzersiz anahtar, gelecekteki tüm takaslarınız için çalışacak ve bir sorun olması durumunda fonlarınızı kurtarmanızı sağlayacaktır.



**Tor Tarayıcı Kullanın**: Maksimum gizlilik için, IP Address'ünüzü gizlemek amacıyla SwapMarket'e Tor Browser üzerinden erişin.



**Kendi kendini barındırmayı düşünün**: Teknik kullanıcılar için kendi SwapMarket örneğinizi çalıştırmak, resmi GitHub Pages etki alanına bağımlılığı ortadan kaldırır.



### Takas optimizasyonu



**Mempool'e göz kulak olun**: Bir takastan önce Mempool.space'i kontrol edin. Mining maliyetlerini en aza indirmek için etkinliğin düşük olduğu zamanları seçin.



**Adresleri kontrol edin**: Değişimler için alıcı Address'nizi titizlikle kontrol edin. Kopyala ve yapıştır yöntemini kullanın ve ilk 5 ve son 5 karakteri kontrol edin.



**Küçük miktarlarla test edin**: İzin verilen minimum miktarla başlayın (25.000 ila 50.000 Sats). Süreçte ustalaştıktan sonra kademeli olarak artırın.



**Takaslarınızı belgeleyin**: Her takasın ID'sini, itfa Address'unu ve son kullanma tarihini not edin. Bu bilgiler, teknik bir sorun olması durumunda takibi ve kurtarmayı kolaylaştırır.



### Kullanım stratejisi



**Nakit akışınızı dengeleyin**: On-Chain (tasarruf, uzun vadeli güvenlik) ve Lightning (günlük harcamalar, anlık ödemeler) arasındaki dağılımınızı gerçek ihtiyaçlarınıza göre ayarlamak için SwapMarket'i kullanın.



**Kârlılığı hesaplayın**: Kalıcı Lightning likidite ihtiyaçları için, doğrudan bir Lightning kanalı açmak yerine tekrarlanan takasların kümülatif maliyetini karşılaştırın. SwapMarket, büyük düzenli akışlar için değil, tek seferlik ayarlamalar için mükemmeldir.



## SwapMarket vs Boltz: Aradaki fark nedir?



### Boltz: Teknoloji ve Hizmet



**Boltz, Bitcoin, Lightning ve Liquid arasında HTLC aracılığıyla atomik takasları uygulayan açık kaynak teknolojisidir** (GitHub'da `boltz-backend`).



**Kritik nokta**: Tüm SwapMarket sağlayıcıları (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) Boltz arka ucunun kendi örneklerini kullanmaktadır. Bu nedenle altta yatan teknoloji aynıdır. Boltz arka ucundaki bir güvenlik açığı potansiyel olarak tüm sağlayıcıları etkileyecektir, ancak sistemin açık kaynaklı yapısı topluluk denetimini mümkün kılmaktadır.



**Boltz Exchange** Boltz ekibi tarafından işletilen tek bir hizmettir, **SwapMarket** ise hepsi Boltz teknolojisini kullanan birkaç sağlayıcıyı bir araya getirerek rekabetçi bir fiyatlandırma ortamı yaratır.



Daha fazla ayrıntı için Boltz ve Zeus Takası eğitimlerimize bakın:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Temel farklılıklar



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket avantajları**: Fiyat rekabeti, arka uç örneklerinin çeşitlendirilmesi, gerçek zamanlı karşılaştırma.



**Teknolojik alternatifler** (SwapMarket uyumlu değil): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Bu çözümler kendi denizaltı takas uygulamalarını kullanmaktadır.



**Öneri**: Basitlik için Boltz Exchange veya rekabet yoluyla maliyetleri optimize etmek için SwapMarket kullanın. Her ikisi de güvenlik açısından eşdeğerdir (HTLC gözetim altında değildir).



## Sonuç



SwapMarket, birden fazla sağlayıcıyı tek bir Interface'da toplayarak Bitcoin/Lightning borsalarını kolaylaştırır. HTLC mimarisi, takasların gözetim dışı doğasını garanti eder, KYC'nin olmaması gizliliği korur ve açık kaynaklı kendi kendine barındırılabilir kod sansüre karşı direnci güçlendirir.



Sağlayıcılar arasındaki rekabet oranları iyileştirir ve likidite kaynaklarını çoğaltır. İki Layer yönetimini (On-Chain tasarrufları, Yıldırım giderleri) optimize etmek için SwapMarket, finansal egemenliği ve gizliliği koruyan pratik bir araçtır.



## Kaynaklar



### Resmi belgeler




- [SwapMarket - Web uygulaması](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Teknik dokümantasyon](https://docs.boltz.Exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### İlgili projeler




- [Boltz Exchange](https://boltz.Exchange) - Orijinal atomik takas hizmeti
- [ZEUS Swaps](https://zeusln.com) - Yıldırım takasları sağlayıcısı