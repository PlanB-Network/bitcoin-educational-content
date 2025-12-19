---
name: Joinstr
description: Egemen Bitcoin gizliliği için Nostr ağı üzerinden merkezi olmayan CoinJoins
---

![cover](assets/cover.webp)



Bitcoin blok zincirinin şeffaflığı, işlem geçmişinin izlenmesini mümkün kılmaktadır. CoinJoins, birden fazla eşzamanlı işlemi karıştırarak bu bağlantıları kırar ve nakit ile karşılaştırılabilir bir gizlilik seviyesini geri kazandırır.



Bununla birlikte, geleneksel çözümler tek bir arıza noktası olarak merkezi bir koordinatöre dayanmaktadır. Wasabi ve Samourai, mevzuat baskısı altında 2024 yılında faaliyetlerini durdurmuştur.



**Joinstr** koordinasyon için merkezi olmayan Nostr ağını kullanarak bu zayıflığı ortadan kaldırır. Bu açık kaynak uygulaması, hiçbir merkezi otoritenin sansürleyemeyeceği, izleyemeyeceği veya hizmeti kesintiye uğratamayacağı gerçek anlamda egemen CoinJoin'ler sağlar.



## Joinstr nedir?



Joinstr, bir koordinasyon altyapısı olarak Nostr protokolünden yararlanarak CoinJoins yaklaşımında devrim yaratan açık kaynaklı bir araçtır. Özel bir sunucu gerektiren merkezi çözümlerin aksine Joinstr, katılımcıların eşler arasında doğrudan koordine olmasını sağlamak için dağıtılmış bir Nostr aktarıcı ağına güvenir.



**Merkezi olmayan mimari** : Nostr ağı merkezi koordinatörün yerini alır. Katılımcılar, Nostr röleleri aracılığıyla şifreli duyurular göndererek "havuzlar" oluşturur veya bunlara katılır. Bu bilgiler (miktarlar, katılımcılar, adresler) röleler için anlaşılmaz kalır ve hiçbir merkezi varlığın CoinJoins'i izleyememesini, sansürleyememesini veya filtreleyememesini sağlar.



**SIGHASH_ALL|ANYONECANPAY mekanizması**: Joinstr bu Bitcoin imza bayrağını kullanarak her katılımcının tüm çıktıları doğrularken yalnızca kendi girdisini imzalamasına izin verir. Her kullanıcı kendi PSBT'ünü yerel olarak üretir, ardından Nostr aracılığıyla dağıtır. Her kullanıcı kendi PSBT'ünü yerel olarak üretir, imzalar ve ardından Nostr aracılığıyla dağıtır. Bitcoinleriniz son imzaya kadar sizin özel kontrolünüz altında kalır.



**Felsefe**: Joinstr, üç hedefi amaçlayan Bitcoin cypherpunk ethosunu takip eder: **sansüre karşı direnç** (hiçbir otorite hizmeti durduramaz), **total non-custodiality** (özel anahtarlarınız sizde kalır) ve **equal treatment** (hiçbir UTXO'ya karşı ayrımcılık yapılamaz).



### Ana Özellikler



**Esnek havuzlar**: Sabit mezheplerin aksine, herhangi bir kullanıcı tam olarak istediği miktarda ve hedef katılımcı sayısında bir havuz oluşturabilir ve yapay bölünme olmadan UTXO kullanımını optimize edebilir.



**Şeffaf ücretler**: Koordinasyon ücreti yok. Sadece Bitcoin işlem ücretleri katılımcılar arasında eşit olarak paylaşılır (kişi başına birkaç bin satoshi).



**Geçicilik**: Hiçbir kullanıcı verisi saklanmaz. Bilgi, işlemden hemen sonra unutulan şifrelenmiş geçici Nostr mesajları aracılığıyla aktarılır.



### Mevcut platformlar



Bu eğitim, şu anda kararlı ve önerilen tek çözüm olan **Android uygulamasına** odaklanmaktadır. Bir Electrum eklentisi mevcuttur ancak onu kararsız hale getiren uyumluluk sorunları vardır. Bir web arayüzü geliştirilme aşamasındadır.



## Bitcoin Çekirdek yapılandırması



Joinstr Android, RPC aracılığıyla bir Bitcoin düğümüne bağlantı gerektirir. Telefonunuzdan gelen bağlantıları kabul etmek için önce bilgisayarınızda Bitcoin Core'u yapılandırmanız gerekir.



**Not**: Bitcoin Core'un tam yapılandırması hakkında daha fazla ayrıntı için özel eğitimlerimize bakın:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Ağ gereksinimleri



#### Yerel IP adresinizi bulun



Android telefonunuz yerel ağdaki Bitcoin düğümünüze ulaşabilmelidir. Bilgisayarınızın IP adresini bulun:



**macOS üzerinde** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Basit bir alternatif:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Linux üzerinde** :



```bash
hostname -I | awk '{print $1}'
```



**Windows'ta** :



```cmd
ipconfig
```



IPv4 adresini bulun (format `192.168.x.x` veya `10.0.x.x`)



### RPC yapılandırması



#### bitcoin.conf'yı Düzenle



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



bitcoin.conf` dosyanızı bulun:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Dosyayı favori metin düzenleyicinizle açın ve RPC sunucusunu etkinleştirmek için bu yapılandırmayı ekleyin.



**Başlamak için önerilen yapılandırma (yer imi)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** yapılandırması (üretim kullanımı için) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Önemli** :




- Signet ilk testleriniz için şiddetle tavsiye edilir**: uygulama hala geliştirme aşamasındadır (beta) ve hatalar hala mevcut olabilir. Signet, gerçek fonları riske atmadan ücretsiz olarak test etmenizi sağlar
- 192.168.1.0/24` yerine ağ alt ağınızı yazın (örneğin IP adresiniz `192.168.68.57` ise `192.168.68.0/24` kullanın)



**Güvenlik**: Güçlü bir parola oluşturun :



```bash
openssl rand -base64 32
```



### Başlatma



#### Yeniden başlatın ve kontrol edin



1. Bitcoin Çekirdeğini tamamen kapatın


2. Yapılandırmayı uygulamak için yeniden başlatın




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Bitcoin Core ilk kez başlatıldığında, yer imi blok zincirini indirecek ve senkronize edecektir. Bu işlem mainnet'dekinden çok daha hızlıdır (sadece birkaç dakika). Lütfen devam etmeden önce senkronizasyon tamamlanana kadar bekleyin.



![CRÉATION DE WALLET](assets/fr/04.webp)



Senkronize edildikten sonra, "Yeni bir wallet oluştur" seçeneğine tıklayarak yeni bir portföy oluşturun. Buna `tuto_joinstr_signet` gibi açık bir isim verin.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet'unuz artık oluşturulmuştur ve test için yer imli bitcoinleri almaya hazırdır.



#### Yer imli bitcoinleri alın (test)



Joinstr'i yer iminde test etmek için ücretsiz test bitcoinlerine ihtiyacınız var :



![SIGNET FAUCET](assets/fr/06.webp)



Gibi herkese açık bir yer imi kullanın:




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Bitcoin Core'da, generate yeni bir alma adresi ("Al" sekmesi), kopyalayın ve musluk formuna yapıştırın. Gerekirse captcha'yı çözün. Saniyeler içinde ücretsiz yer imli bitcoinler alacaksınız.



## Android uygulaması



### Kurulum



![APPLICATION ANDROID](assets/fr/07.webp)



En son APK sürümünü indirmek için [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) adresine gidin. Android tarayıcınızda dosyayı indirin, ardından kurulumu başlatmak için açın. Gerekirse telefonunuzun güvenlik ayarlarında bilinmeyen kaynaklardan yüklemeye izin vermeniz gerekir.



### Uygulama yapılandırması



![PERMISSIONS VPN](assets/fr/08.webp)



İlk açılışta Joinstr uygulaması yerleşik VPN'i kontrol etmek için izinler isteyecektir. Her iki izin talebini de kabul edin: OpenVPN kontrolü ve VPN bağlantısı. Bu izinler, ağ gizliliğinizi koruyan VPN entegrasyonu için gereklidir.



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr uygulaması üç ana sekme halinde düzenlenmiştir:




- Ev**: Ana ekran
- Havuzlar**: CoinJoin havuzları oluşturma ve yönetme
- Ayarlar**: Uygulama yapılandırması



![CONFIGURATION SETTINGS](assets/fr/13.webp)



"Ayarlar" sekmesinde ayarları yapılandırın:



**1. Nostr Röle**: Havuz koordinasyonu için Nostr röle adresi




- Örnek: `wss://relay.damus.io`
- Önerilen diğer röleler: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Önemli**: Tüm katılımcılar aynı havuzları görmek ve katılmak için **aynı Nostr rölesini** kullanmalıdır. Farklı bir aktarıcı kullanırsanız, diğer aktarıcılarda oluşturulan havuzları göremezsiniz



**2. Düğüm URL'si**: Bitcoin düğümünüzün IP adresi (bağlantı noktası olmadan)




- Biçim: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC Kullanıcı Adı** : bitcoin.conf'ünüzde `rpcuser=` içinde yapılandırılan kullanıcı adı




- Örnek: `satoshi



**4. RPC Parolası** : bitcoin.conf'nizde `rpcpassword=` içinde ayarlanan parola



**5. RPC Bağlantı Noktası** : Ağa bağlı olarak RPC bağlantı noktası




- Mainnet** : `8332`
- Yer imi**: `38332`



**6. Wallet**: Karıştırılacak UTXO'ları içeren Bitcoin Çekirdek portföyünü seçin




- Örnek: `tuto_joinstr_signet`



**7. VPN Ağ Geçidi**: Bir Riseup VPN sunucusu seçin




- Örnek: `(Paris) vpn07-par.riseup.net`
- Diğerleri mevcut: Amsterdam, Seattle, vb.
- ⚠️ **Önemli**: Aynı havuzdaki tüm katılımcılar CoinJoin'e katılmak için **aynı VPN Ağ Geçidini** kullanmalıdır. Karıştırma turu sırasında, ağ analizinin katılımcıları ilişkilendirmesini önlemek için tüm katılımcılar aynı çıkış IP adresiyle görünmelidir



Joinstr uygulaması, Riseup VPN'i **yerel olarak** entegre ederek katılımcılar arasındaki koordinasyonu basitleştirir.



**Önemli** :




- Telefonunuzun ve bilgisayarınızın aynı yerel WiFi ağında olduğundan emin olun
- Bir havuza katılırken VPN bağlantısı otomatik olarak etkinleştirilecektir
- Tüm parametreleri ayarladıktan sonra **"Kaydet "** üzerine tıklayın



## Pratik kullanım



### Havuz oluşturma veya havuza katılma



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Bir CoinJoin'e katılmak için iki seçeneğiniz vardır:



**Seçenek 1: Yeni bir havuz oluşturun**



"Havuzlar" sekmesinde "Yeni Havuz Oluştur" seçeneğine tıklayın. BTC cinsinden değeri (örneğin 0,002 BTC) ve istediğiniz katılımcı sayısını (en az 2, daha fazla anonimlik için önerilen 3-5) belirtin. Uygulama daha sonra diğer kullanıcıların havuzunuza katılmasını bekler. Gerekli sayıya ulaşıldığında, çıktı kayıt süreci otomatik olarak başlar ve karıştırmak için UTXO'inizi seçmeniz ve "Kayıt Ol" seçeneğine tıklamanız gerekir.



**⏱️ Önemli**: Havuzlar **10 dakika** hareketsiz kaldıktan sonra sona erer. Gerekli katılımcı sayısına ulaşılamazsa, havuz otomatik olarak kapatılacaktır.



**2. Seçenek: Mevcut bir havuza katılın**



"Diğer Havuzları Görüntüle" sekmesinde, diğer kullanıcılar tarafından oluşturulan mevcut havuzlara göz atın. Miktarınıza karşılık gelen bir havuz seçin ve ona katılın. Diğer katılımcılarla aynı Nostr aktarıcısını ve VPN Ağ Geçidini yapılandırdığınızdan emin olun (Yapılandırma bölümüne bakın).



**UTXO seçim kuralı**: UTXO'nız havuz değerinden biraz daha yüksek olmalıdır (+500 ile +5000 sats fazlası arasında).



**Örnek**: 0,002 BTC'lik (200.000 sats) bir havuz için 200.500 ile 205.000 sats arasında bir UTXO kullanın.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Süreç tamamen otomatiktir**: girdiniz kaydedildikten sonra uygulama tüm katılımcıların girdilerini kaydetmesini bekler. Tüm girdiler kaydedildikten sonra, PSBT oluşturulur, anahtarlarınızla otomatik olarak imzalanır ve ardından diğer katılımcıların imzalarıyla birleştirilir. Son olarak, işlemin tamamı Bitcoin ağında yayınlanır. Yayın tamamlandığında TXID'yi (işlem tanımlayıcısı) alırsınız. Android'de PSBT'in manuel olarak değiştirilmesine gerek yoktur.



### on-chain doğrulama



![TRANSACTION MEMPOOL](assets/fr/12.webp)



İşlem yayınlandıktan sonra TXID (işlem tanımlayıcısı) alacaksınız. Bunu [mempool.space](https://mempool.space) adresinde veya favori tarayıcınızda görüntüleyin. Bir yer iminde test etmek için [mempool.space/signet](https://mempool.space/signet) adresini kullanın.



Gözlemleyebilirsiniz :





- N giriş**: Katılımcı başına bir adet (örneğimizde 2 giriş)
- N özdeş çıktı**: tam kupür miktarı (burada, her biri 0,00199800 BTC'lik 2 çıktı)
- Akış şeması**: mempool.space giriş ve çıkışların karışımını görsel olarak gösterir
- Özellikler** : İşlem SegWit, Taproot, RBF, vb. olarak tanımlanabilir.



Tüm ana çıktılar aynı miktarda olduğundan, hangisinin kime ait olduğunu belirlemek **imkansızdır**. Bu, CoinJoin'nın temel ilkesidir: çıktıların ayırt edilemezliği.



**İşlem imzası örneği** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Lütfen dikkat**: UTXO'larınız havuz değerinden daha büyükse, döviz çıkışlarınız (fazlalıklarınız) olacaktır. Bu döviz UTXO'ları izlenebilir olmaya devam eder ve anonimleştirilmiş çıktılarınızdan ayrı olarak yönetilmelidir. Bunları asla karma çıktılarınızla birleştirmeyin.



## CoinJoin kalite ve anonimlik paketleri



Bir CoinJoin'in verimliliği **anonset** ile ölçülür: işlem tarafından üretilen aynı değerdeki çıktıların sayısı. Bu sayı ne kadar yüksek olursa, hangi girdinin hangi çıktıya karşılık geldiğini belirlemek o kadar zor olur.



Joinstr şu anda ortalama **2 ila 5 katılımcıdan** oluşan havuzlar oluşturmaktadır. Bu rakamlar Wasabi (50-100 katılımcı) veya Whirlpool (5-10 katılımcı) gibi geleneksel merkezi koordinatörlerden daha düşüktür, ancak bu ademi merkeziyetçiliğin bedelidir.



💡 **Anonimlik kümelerini ve bunların hesaplanmasını ayrıntılı olarak anlamak için** tam kursumuza bakın: [Anonimlik kümeleri] (https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. diğer CoinJoinler



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Diğer aktif CoinJoin çözümleri** :




- Ashigaru**: Whirlpool protokolünün merkezi koordinatörlü ancak merkezi olmayan bir şekilde konuşlandırılabilen açık kaynaklı uygulaması. Samourai Wallet'nin 2024'te ele geçirilmesinden sonra çalışmaya devam eder.
- JoinMarket**: Merkezi koordinatörü olmayan, "yapıcıların" likidite sağladığı ve "alıcılar" tarafından ücretlendirildiği bir yapıcı/alıcı iş modeline dayanan merkezi olmayan P2P çözümü.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Temel değiş tokuş**: Joinstr ve JoinMarket, merkezi bir koordinatörü olmayan tek iki çözümdür. JoinMarket finansal teşvikler içeren bir P2P iş modeli kullanırken Joinstr maliyetsiz koordinasyon için Nostr kullanmaktadır. Joinstr, basitlik (yapan/alan yönetimi yok) ve koordinasyon ücretlerinin tamamen yokluğu lehine anında büyük ölçekli anonimliği feda eder.



**Pratik öneri**: Daha küçük havuzları telafi etmek için, farklı katılımcılarla CoinJoin'in birkaç ardışık turunu çalıştırın. Gizliliğinizi en üst düzeye çıkarmak için turlarınızı aralıklı yapın ve her tur arasında Nostr rölelerini değiştirin.



Bu konu hakkında daha fazla bilgi için bitcoin gizliliği hakkındaki eksiksiz kursumuza başvurmaktan çekinmeyin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Avantajlar ve sınırlamalar



### Önemli Noktalar



**Gelişmiş gizlilik**: Nostr iletişim şifrelemesi, katılımcılar arasında paylaşılan VPN ve önerilen Tor kullanımı kombinasyonu, aşılması zor çok katmanlı koruma sağlar.



**Şeffaf, minimum maliyet**: Koordinasyon maliyeti yok, sadece mining maliyetleri katılımcılar arasında eşit olarak paylaşılıyor. Herhangi bir operatör tarafından yüzde alınmaz.



### Dikkate alınması gereken kısıtlamalar





- Değişken likidite**: Daha küçük havuzlar, katılımcıların bir araya gelmesini bekleyebilir
- Proje devam ediyor**: Uygulama beta aşamasındadır, hatalar olabilir. Önce yer iminde küçük miktarlarla test edin
- Sybil saldırıları**: Bir rakibin birden fazla havuz katılımcısını kontrol etme olasılığı



## En iyi uygulamalar



**UTXO izolasyonu**: Karıştırılmış bir UTXO'yi asla karıştırılmamış bir UTXO ile birleştirmeyin. Anonimleştirilmiş çıktılarınız için ayrı bir portföy kullanın.



**Birden fazla tur gereklidir**: Farklı katılımcılarla birbirini takip eden en az 3 tur gerçekleştirin. Kalıplardan kaçınmak için miktarları ve zamanlamaları değiştirin. Turları birkaç saat arayla gerçekleştirin.



**Ağ koruması**: Yerleşik VPN'e ek olarak sistematik olarak Tor kullanın. Her önemli oturum için geçici Nostr anahtarları oluşturun.



**Dikkatli ilerleme**: Yer imlerine küçük miktarlarla başlayın.



## Sonuç



Joinstr, gerçek anlamda merkezi olmayan bir Bitcoin gizlilik çözümünü temsil etmektedir. Koordinasyon için Nostr kullanarak, kullanıcı egemenliğini korurken merkezi koordinatörlere bağımlılığı ortadan kaldırır.



**Sansüre karşı dirence önem veren ve daha küçük havuzları telafi etmek için birkaç tur CoinJoin gerçekleştirmeye hazır olan kullanıcılar için.



Finansal incelemelerin arttığı bir ortamda, gizliliği korumaya yönelik merkezi olmayan araçlar elzem hale gelmektedir.



## Kaynaklar



### Resmi belgeler




- [Joinstr resmi web sitesi](https://joinstr.xyz)
- [Kullanıcı belgeleri](https://docs.joinstr.xyz/users/using-joinstr)
- [Teknik dokümantasyon](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab kaynak kodu](https://gitlab.com/invincible-privacy/joinstr)
- [Android uygulaması](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Öğreticiler




- [Electrum eklenti eğitimi](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Uncensored Tech tarafından eksiksiz kılavuz



### Topluluk ve destek




- [Telegram Joinstr Group](https://t.me/joinstr) - Topluluk desteği ve yer imi köşeleri
- [DelvingBitcoin hakkında teknik tartışma](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Ek araçlar




- [Bookmark Faucet](https://signetfaucet.com) - Ücretsiz test Bitcoinleri
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternatifi
- [Mempool.space](https://mempool.space) - Gizlilik analizi ile Block explorer