---
name: Zeus Swap
description: On-Chain ve Lightning Network bitcoinleri arasında gözetim dışı Exchange hizmeti
---

![cover](assets/cover.webp)



Bitcoin ekosistemi bir ikilik sunar: ana ağ (On-Chain) maksimum güvenlik sunarken, Lightning Network anlık işlemlere olanak tanır. Bu iki Layer mimarisi pratik bir zorluk yaratır: fonlar merkezi aracılar olmadan bu iki katman arasında nasıl verimli bir şekilde aktarılabilir?



Sorun somut: bir Lightning ödemesi alıyorsunuz ancak bunu Cold deposunda tutmak istiyorsunuz ya da tam tersi, On-Chain bitcoin'leriniz var ancak Lightning likiditesine ihtiyacınız var. Geleneksel çözümler, Lightning kanallarının manuel olarak açılıp kapatılmasını (maliyetli ve teknik) veya KYC gerektiren merkezi platformları içerir.



Zeus Swap bu sorunu otomatik, gözetimsiz bir Exchange hizmetiyle çözüyor. Zeus LSP tarafından geliştirilen bu hizmet, fonlarınızı bir aracıya emanet etmeden On-Chain bitcoinlerini çift yönlü olarak Lightning satoshis'e dönüştürmenize olanak tanır. Süreç, Exchange'un tamamlanacağını ya da iptal edileceğini garanti eden atomik sözleşmeler (HTLC) kullanır.



Yenilik basitliğinde yatıyor: kayıt veya KYC gerekmeden finansal egemenliğinizi koruyan bir Exchange için sadece birkaç tıklama.



## Zeus Swap nedir?



Zeus Swap, Zeus LSP tarafından geliştirilen ve ana Bitcoin ağı ile Lightning Network arasında atomik takas sağlayan bir likidite Exchange hizmetidir. On-Chain BTC ve Lightning satoshileri arasında iki yönlü dönüşümü kolaylaştırmak için denizaltı takasları ve ters takasları kullanan ve aynı zamanda operasyonun gözetim dışı doğasını koruyan teknik bir altyapıdır.



### Teknik mimari



Zeus Swap, Boltz'un açık kaynaklı Bitcoin/Lightning atomik takas teknolojisini kullanır. Protokol Hash Zaman Kilitli Sözleşmeleri (HTLC) kullanır: iki serbest bırakma koşuluyla (kriptografik bir sırrın ifşa edilmesi veya zaman aşımı) fonları kilitleyen sözleşmeler.



Bir denizaltı takası için (On-Chain → Lightning), kullanıcı bir Lightning Invoice'nin Hash'ünü içeren bir Address'e bitcoin gönderir. Zeus LSP bu fonların kilidini yalnızca ilgili Invoice'ye ödeme yaparak açar ve bitcoinlerin kilidini otomatik olarak açan ön görüntüyü ortaya çıkarır. Bu mekanizma atomikliği garanti eder.



Ters takas için (Lightning → On-Chain), kullanıcı Zeus LSP'den bir Lightning Invoice öder ve hazırlanmış bir Bitcoin işleminin hedef Address'e bırakılmasını sağlayan bir ön görüntüyü ortaya çıkarır.



Lightning Network'in nasıl çalıştığına dair daha fazla ayrıntı için özel kursumuza göz atın:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### İş modeli



Zeus LSP, swapları onurlandırmak için On-Chain ve Lightning likiditesini koruyarak piyasa yapıcı olarak hareket eder. Zeus, swaplar için değişken bir ücret (yön ve koşullara bağlı olarak tipik olarak %0,1 ila %0,5) artı Bitcoin'un Mining ücretini uygular ve bu ücret doğrulama öncesinde şeffaf bir şekilde görüntülenir.



Bir Yıldırım Hizmet Sağlayıcısı olarak Zeus, isteğe bağlı kanal açma, verimli yönlendirme ve özelleştirilmiş likidite çözümlerindeki uzmanlığı sayesinde maliyetleri optimize eder.



### Entegrasyon



Zeus Wallet, hizmeti yerel olarak entegre ederek Interface Bitcoin/Lightning'den ayrılmadan takas yapılmasını sağlar. Bu, uygulamalar arasında kopyalama ve yapıştırma sürtünmesini ortadan kaldırır.



Bağımsız Interface ağı, tüm cüzdanlar için erişilebilir olmaya devam ederek maksimum kullanım esnekliğini garanti eder.



## Ana Özellikler



### Çift yönlü takaslar



Zeus Swap iki tür Exchange sunmaktadır:



**Denizaltı takasları (On-Chain → Lightning)**: Bitcoin rezervlerinizden Lightning likiditesi enjekte edin, manuel olarak kanal açmadan mobil bir Wallet veya Lightning düğümünü beslemek için kullanışlıdır.



**Ters takas (Lightning → On-Chain)**: Lightning satoshilerini uzun vadeli depolama için On-Chain bitcoinlerine dönüştürerek maliyetli kanal kapanmalarını önler.



### Kullanıcı arayüzleri



**Interface web** (swaps.zeuslsp.com): kayıt olmadan basitleştirilmiş deneyim, ücretlerin ve durumun gerçek zamanlı gösterimi ile rehberli süreç.



**Zeus Wallet entegrasyonu**: uygulamadan doğrudan takas, faturaların ve adreslerin otomatik yönetimi, işlem hatalarını ortadan kaldırma.



### Güvenlik ve kurtarma



Her takas, değişmez parametrelere sahip benzersiz bir Contract üretir: Hash Yıldırım, zaman aşımı, geri ödeme Address. Arıza durumunda, Zeus LSP'den bağımsız olarak sağlanan Address aracılığıyla otomatik kurtarma.



**Zeus Swaps Kurtarma Anahtarı**: On-Chain → Lightning takası sırasında Zeus otomatik olarak eski bireysel iade dosyalarının yerine evrensel bir kurtarma anahtarı oluşturur. Bu benzersiz anahtar, herhangi bir cihazda ve onunla oluşturulan tüm takaslar için çalışır. Bir takas hatası durumunda paranızı kurtarabilmek için bu anahtarı indirip güvenli bir yere kaydetmeniz çok önemlidir.



### Ağ optimizasyonu



Zeus Swap, son kullanma sürelerini ve Mining ücretlerini ağ koşullarına göre otomatik olarak ayarlar. Zeus kullanıcıları gelişmiş seçeneklerden yararlanır: LSP seçimi, özelleştirilmiş gecikmeler, diğer hizmetlerle uyumluluk (Boltz).



## Kurulum ve kullanım



### Erişim yöntemleri



**Interface web** (swaps.zeuslsp.com): tüm cüzdanlarla uyumlu evrensel çözüm, kurulum gerektirmez, ara sıra kullanım için idealdir.



**Zeus uygulaması** (iOS/Android): Wallet ve takasları birleştiren entegre deneyim, düzenli kullanıcılar için uygundur.



Bu eksiksiz Wallet hakkında daha fazla bilgi edinmek için Zeus eğitimimize bakın:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Web yapılandırması



**On-Chain → Lightning**: İşlem, Interface web Zeus Swap üzerinde takasın yapılandırılmasıyla başlar. Kullanıcı, takasın yönünü tersine çevirmek için On-Chain ve Lightning alanları arasındaki oku kullanabilir.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: ağ ücretlerinin (Sats 302) ve Zeus hizmetinin (Sats 50) şeffaf gösterimi ile miktar seçimi (Sats 50.000 → ücretlerden sonra Sats 49.648).*



İşlem sırasında Zeus size evrensel kurtarma anahtarını indirmenizi önerir:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Zeus Swaps Kurtarma Anahtarı için indirme iletişim kutusu - eski bireysel geri ödeme dosyalarının yerini alan evrensel bir anahtar*



Zaten bir anahtarınız varsa, Zeus bunu kontrol etmenize izin verir:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface mevcut bir Zeus Swaps Kurtarma Anahtarının geçerliliğini kontrol etmek için*



Yapılandırıldıktan sonra Zeus, Bitcoin deposu Address'yı oluşturur ve talimatları görüntüler:



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Takas tamamlama sayfası: QR kodu ve Bitcoin 50.000 Sat göndermek için Address, 24 saatlik son kullanma tarihi hatırlatması ile*



Takas daha sonra Bitcoin onayı için bekler:



![Attente de confirmation](assets/fr/05.webp)



*Durum "İşlem Mempool'de" - takasın sonuçlandırılması için Bitcoin onayı bekleniyor*



Onaylandıktan sonra takas işlemi otomatik olarak tamamlanır:



![Swap réussi](assets/fr/06.webp)



*Başarı teyidi: 49.648 Sats, şebeke ve hizmet ücretleri düşüldükten sonra Yıldırım'da alındı*



### Zeus Uygulamasını Kullanma



**Lightning → On-Chain**: Zeus uygulaması ters takaslar için entegre bir deneyim sunar (Lightning'den Bitcoin'e).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Lightning (69,851 Sats) ve On-Chain (38,018 Sats) bakiyelerini gösteren Zeus ana ekranı, yan menü üzerinden takaslara erişim*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface ters takas oluşturma: 50.000 Sats Lightning → 49.220 Sats On-Chain, şebeke ücretleri (530 Sats) ve servis (250 Sats) açıkça görüntülenir. Kullanıcılar "generate On-Chain Address" düğmesi aracılığıyla Wallet Zeus'tan Address alan bir Bitcoin'yi manuel olarak veya generate'i otomatik olarak girebilirler.*



![Finalisation du swap mobile](assets/fr/09.webp)



*Sonuçlandırma ekranları: "BU Invoice'İ ÖDE" ile Lightning Invoice ödeme ekranı, 9,96 saniyede başarılı Lightning ödemesi onayı ve onay bekleyen 49.162 Sats ile bakiye ekstresi*



### Gözetim ve güvenlik



Her takasın gerçek zamanlı izleme ile benzersiz bir tanımlayıcısı vardır. Tam ilerleme göstergesi, son kullanma tarihleri için otomatik uyarılar. Şebeke koşullarına göre otomatik şarj önerileri.



## Avantajlar ve sınırlamalar



### Avantajlar





- Basitlik**: Manuel kanal manipülasyonuna kıyasla birkaç tıklamayla değiştirme
- Gözetim dışı**: KYC yok, hesap yok, fonlar asla üçüncü bir tarafa emanet edilmiyor
- Şeffaflık**: ücretler doğrulamadan önce açıkça gösterilir (kullanıcı testlerine bağlı olarak %0,1 ila %0,5 + minage - her takasta mevcut ücretleri kontrol edin)
- Mobil entegrasyon**: Zeus Wallet'de yerel deneyim



### Sınırlamalar





- Geçerlilik süreleri**: maksimum 24-48 saat, Bitcoin zamanında onaylanmazsa başarısızlık
- Tutar limitleri**: minimum 25.000 Sats, Zeus LSP likiditesi koşullara göre değişken
- On-Chain**'i izler: Blockchain analizi ile potansiyel olarak tanımlanabilen HTLC komut dosyaları
- Onay gerekli**: Bitcoin doğrulaması için en az 10 dakika



## En iyi uygulamalar



### Zamanlama ve maliyetler





- Yoğunluğun düşük olduğu zamanlar için Mempool.space'i izleyin
- Mining maliyetlerini azaltmak için hafta sonlarını ve yoğun olmayan saatleri tercih edin
- Kârlılığı hesaplayın: küçük miktarlar vs. doğrudan kanal açma



### Güvenlik





- Bitcoin adreslerini dikkatlice kontrol edin (kopyala-yapıştır önerilir)
- Zeus Swaps Kurtarma Anahtarını yedekleyin**: kurtarma anahtarını indirin ve güvenli bir yerde saklayın
- Belge: Contract ID, iade Address, son kullanma tarihi
- Zamanında onay için uygun Mining ücretlerini kullanın



### Kullanım stratejisi





- On-Chain/Lightning likiditesini ihtiyaçlarınıza göre dengeleyin
- Tek seferlik ayarlamalar için Zeus Swap, kalıcı ihtiyaçlar için doğrudan kanallar



## Diğer takas hizmetleri ile karşılaştırma



### Zeus Swap vs Boltz Exchange



Zeus Swap, Boltz'un arka uç teknolojisini kullanıyor, ancak bazı önemli iyileştirmeler yapıyor:



**Zeus Swap avantajları** :




- Interface birleşik**: Zeus'ta yerel entegrasyon Wallet vs Interface web tekniği Boltz
- WebSocket API**: manuel yoklamaya karşı gerçek zamanlı güncellemeler
- Otomatik yönetim**: otomatik faturalandırma ve Address yönetimi
- Mobil destek**: yalnızca akıllı telefon ve masaüstü optimizasyonu
- Swagger belgeleri**: geliştiriciler için eksiksiz REST API



*tam bağımsızlık ve herhangi bir Bitcoin/Lightning kurulumuyla kullanım için *Boltz avantajlı olmaya devam etmektedir**.



Zeus Swap, kanıtlanmış Boltz teknolojisini, ham bir protokol ile kullanıcı dostu bir uygulama arasındaki farka benzer şekilde ana akım bir kullanıcı deneyimine dönüştürür.



### Zeus Swap vs Phoenix/Breez (entegre swaplar)



Phoenix ve Breez, teknik karmaşıklığı son kullanıcıdan gizleyen şeffaf takas işlevlerini entegre eder. Phoenix, kullanıcının Bitcoin katmanları arasında açıkça ayrım yapmadığı otomatik bir takas/değiştirme sistemi kullanır: "bir Bitcoin Address'ya gönderir" ve uygulama takası arka planda gerçekleştirir.



Bu ultra basitleştirilmiş yaklaşım yeni başlayanlar için mükemmeldir, ancak işlemlerin anlaşılmasını ve kontrolünü sınırlar. Zeus Swap daha eğitici bir felsefe benimser: kullanıcılar iki farklı katman arasında geçiş yaptıklarını anlar ve iki Layer Bitcoin ekosistemi hakkındaki anlayışlarını kademeli olarak geliştirirler.



## Ücret ve limitlerin detaylı karşılaştırması (2024)



⚠️ **Uyarı**: Ücretler piyasa koşullarına ve hizmet güncellemelerine bağlı olarak zaman içinde değişebilir. Bir takası onaylamadan önce her zaman Interface'de görüntülenen ücretleri kontrol edin.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap kullanım kolaylığı ve teknik kontrol arasında bir denge sunar: Boltz'dan daha erişilebilir, Phoenix/Breez'den daha esnek, katı ve gözetimci olmayan bir yaklaşım.



## Sonuç



Zeus Swap, Bitcoin ekosisteminde önemli bir yeniliği temsil etmekte ve ana ağ ile Lightning Network arasındaki birlikte çalışabilirlik sorununu zarif bir şekilde çözmektedir. Atomik takasların kriptografik sağlamlığını erişilebilir bir kullanıcı deneyimi ile birleştiren bu hizmet, finansal egemenlik ilkelerinden ödün vermeden Bitcoin dual-Layer yönetimini demokratikleştirmektedir.



Zeus Swap'ın kanıtlanmış Boltz teknolojisinden miras alınan gözetimsiz mimarisi, fonlarınızın takas süreci boyunca münhasır kontrolünüz altında kalmasını sağlar. Bu yaklaşım, Bitcoin'ün ruhuna saygı gösterirken, ana akım benimseme için gereken kullanıcı rahatlığını sunar. Fiyatlandırma şeffaflığı ve KYC süreçlerinin olmaması bu benzersiz değer önerisini güçlendirmektedir.



Modern Bitcoin kullanıcısı için Zeus Swap, likidite dağılımını ihtiyaçlara göre optimize etmek için stratejik bir araçtır: Uzun vadeli tasarruflar için On-Chain güvenli depolama, günlük harcamalar ve mikro işlemler için Lightning kullanılabilirliği. Bu esneklik, Bitcoin yönetimini teknik bir kısıtlamadan rekabet avantajına dönüştürür.



Deneyimli Zeus LSP ekibi ve Boltz açık kaynak topluluğu tarafından desteklenen Zeus Swap'ın gelecekteki gelişimi, maliyetler, işlem süreleri ve kullanıcı deneyimi açısından sürekli iyileştirmeler vaat ediyor. Bu hizmet, teknik karmaşıklığın son kullanıcı için şeffaf hale geldiği Bitcoin altyapısının olgunlaşmasına yönelik daha geniş eğilimin bir parçasıdır.



## Kaynaklar



### Resmi belgeler




- [Zeus Swap - Web portalı](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobil uygulama](https://zeusln.app)
- [Blog Zeus - Duyurular ve eğitimler](https://blog.zeusln.com)
- [Zeus teknik belgeleri](https://docs.zeusln.app)



### Topluluk ve destek




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)