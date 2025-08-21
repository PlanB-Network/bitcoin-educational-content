---
name: ThunderHub
description: Interface Yıldırım düğümü yönetim ağı LND
---
![cover](assets/cover.webp)



## Giriş



ThunderHub, Lightning düğümleri (LND)** için açık kaynaklı bir yöneticidir ve herhangi bir cihazdan veya tarayıcıdan erişilebilen sezgisel bir Interface sunar.



**Ana özellikler:**




- İzleme**: Bakiyelerin, kanalların, işlemlerin, yönlendirme istatistiklerinin global görünümü
- Yönetim**: Kanal açma/kapama, gelen/giden ödemeler, kanal dengeleme
- Entegrasyonlar**: LNURL desteği, Boltz üzerinden takas, Amboss yedekleme
- Interface duyarlı**: Koyu/açık temalar ile mobil, tablet ve masaüstü cihazlarla uyumlu



ThunderHub, **Umbrel**, **Voltage**, **RaspiBlitz** ve **MyNode** ile kolayca entegre olarak düğümünüzün günlük yönetimini basitleştirir.



**ThunderHub, kanallarını yönetmek, likiditeyi kontrol etmek (yeniden dengeleme), işlemleri izlemek ve Amboss gibi üçüncü taraf hizmetlerini entegre etmek için ergonomik bir Interface arayan operatörler için özellikle uygundur. Güvenlik, yerel veya Tor bağlantısı aracılığıyla sağlanır.



Henüz bir Lightning düğümünüz yoksa, LND Umbrel eğitimimizi takip etmenizi öneririz:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Kurulum



ThunderHub, Lightning node barındırma ortamınıza bağlı olarak birkaç farklı şekilde kurulabilir. İster anahtar teslim bir çözüm (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, vb.) ister manuel kurulum kullanın, ThunderHub genellikle büyük bir çaba gerektirmeden kullanılabilir. Aşağıda, iki yaygın yaklaşımı açıklıyoruz: Umbrel Uygulama Mağazası aracılığıyla ve manuel kurulum yoluyla (bir sunucu veya kendi kendine barındırılan dağıtım için geçerlidir).



### Umbrel aracılığıyla kurulum



Umbrel, ThunderHub'ı **Uygulama Mağazasına** entegre ederek kurulumu son derece basit hale getirir. Komut satırına veya manuel yapılandırmaya gerek yok: her şey Interface Umbrel aracılığıyla yapılır. Sadece bu adımları izleyin:





- Umbrel kontrol panelini** açın: Umbrel düğümünüzün Interface ağına bağlanın (örneğin, yerel ağınızdaki `http://umbrel.local` veya Tor kullanıyorsanız `.onion` Address üzerinden).
- App Store'a** erişin: Umbrel'in ana menüsünde "App Store" (veya "App") üzerine tıklayın. Mevcut uygulamalar listesinde **ThunderHub** için arama yapın.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- ThunderHub'ı yükleyin**: ThunderHub uygulamasına ve ardından yükle düğmesine tıklayın. Gerekirse onaylayın. Umbrel, ThunderHub'ı düğümünüze otomatik olarak indirecek ve dağıtacaktır.





- Uygulamayı başlatın**: Kurulum tamamlandığında (birkaç on saniye), ThunderHub ana sayfanızda görünür. Açmak için simgeye tıklayın. ThunderHub tarayıcınızda başlatılır.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Önemli:** ThunderHub ilk açıldığında, oturum açmak için gereken **varsayılan parolayı** otomatik olarak görüntüler. "Bunu bir daha gösterme" seçeneği, gelecekteki bağlantılar için bu ekranı gizlemenizi sağlar. **Şunları yapmanızı şiddetle tavsiye ederiz:**




- Bu şifreyi hemen** şifre yöneticinize kaydedin
- Bir sonraki adımda kullanmak üzere kopyalayın**
- Parola kaydedildikten sonra "Bunu bir daha gösterme" seçeneğini işaretleyin



![Page de connexion de ThunderHub](assets/fr/03.webp)



Ardından, Interface'un kilidini açmak için önceki adımda kopyaladığınız şifreyi girmeniz gereken oturum açma sayfasına yönlendirileceksiniz.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel, ThunderHub'a arka planda LND bağlantı bilgilerini (TLS sertifikası, yönetim makaronu vb.) sağlamayı üstlenir, böylece herhangi bir ek yapılandırma yapmanıza gerek kalmaz. Sadece birkaç tıklamayla Umbrel düğümünüzde ThunderHub'ı kurup çalıştırabilirsiniz.



### Manuel kurulum (kendi kendine barındırılan, Umbrel hariç)



Umbrel dışındaki kullanıcılar için (örneğin kişisel bir sunucuda, RaspiBlitz'li bir Raspberry Pi'de veya *tek başına* bir kurulumda), ThunderHub kurulumu birkaç ekstra adım gerektirir. Aşağıda [resmi ThunderHub belgelerine] (https://docs.thunderhub.io) göre kaynaktan kurulumu ve yapılandırmayı açıklıyoruz.



#### Kurulum



**Önkoşullar:** Sisteminizin [documentation setup](https://docs.thunderhub.io/setup)'a göre minimum gereksinimleri karşıladığından emin olun:




- Node.js** sürüm 18 veya üstü
- npm** yüklü
- LND kimlik doğrulama dosyalarına erişim :
  - LND TLS sertifikası (`tls.cert`)
  - LND yönetim makaronu (`admin.macaroon`)
  - LND gRPC hizmeti Address (ana bilgisayar adı:bağlantı noktası) (yerel olarak varsayılan `127.0.0.1:10009`)



**1. ThunderHub kodunu alın:** Projenin GitHub deposunu [kurulum belgelerinde] (https://docs.thunderhub.io/installation) açıklandığı gibi klonlayın:



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. Bağımlılıkları yükleyin ve uygulamayı oluşturun:**



```bash
npm install
npm run build
```



Bu komutlar gerekli tüm modülleri yükler ve ardından uygulamayı derler (ThunderHub TypeScript/React ile yazılmıştır).



**3. Daha sonra güncelleme:** ThunderHub gelecekteki güncellemeler için çeşitli yöntemler sunar:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Yapılandırma (Kurulum)



**1. Ana yapılandırma dosyası:** Yapılandırmayı özelleştirmek için ThunderHub klasörünün kök dizininde bir `.env.local` dosyası oluşturun (bu, güncellemeler sırasında ayarlarınızın üzerine yazılmasını önleyecektir). Ana değişkenler [kurulum belgeleri](https://docs.thunderhub.io/setup) uyarınca:



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Sunucu Hesapları yapılandırması:** `ACCOUNT_CONFIG_PATH` içinde belirtilen YAML dosyasını oluşturun:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Uzaktan Erişim:** Uzak bir LND düğümüne bağlanmak için `LND.conf` dosyasına ekleyin:



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Güvenlik:** İlk başlangıçta, ThunderHub **otomatik olarak** `masterPassword` ve YAML dosyasındaki tüm hesap parolalarını gizleyerek parolaların sunucuda açık metin olarak bulunmasını önler.



**5. ThunderHub'ı başlatın:**



```bash
npm start
```



Varsayılan olarak, sunucu 3000 numaralı bağlantı noktasını dinler. Http://localhost:3000` (veya yerel ağdan `http://ip-serveur:3000`) adresine erişin.



**6. Docker alternatifi:** ThunderHub resmi Docker görüntüleri sağlar:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



ThunderHub oturum açma sayfası görünür. Yapılandırılmış hesabı seçin ve kontrol paneline erişmek için parolayı girin.



**Diğer dağıtımlara kurulum:** Önceden paketlenmiş düğüm dağıtımları (RaspiBlitz, MyNode, Start9, vb.) genellikle kendi yönetim arayüzleri aracılığıyla yerel ThunderHub desteği sunar.



**Daha fazla bilgi için:** Resmi belgelerin tamamına bakın:




- Kurulum:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- Yapılandırma:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Bu kaynaklar SSO hesapları, şifrelenmiş makaronlar, TOR yapılandırması ve çok daha fazlası gibi gelişmiş seçenekleri ayrıntılı olarak açıklamaktadır.



ThunderHub kurulduktan ve erişilebilir olduktan sonra, tüm özelliklerinden yararlanmaya hazırsınız demektir. Aşağıdaki bölümde, Interface ThunderHub'a ve kullanımında size rehberlik edecek çeşitli sekmelerine bir göz atacağız.



## Interface sunumu



Interface ThunderHub, birkaç temel bölümden oluşan bir ana menü (genellikle sol taraftaki sütunda görüntülenir) etrafında yapılandırılmıştır. Her biri Lightning düğümünüzü yönetmenin bir yönüne karşılık gelir. Şimdi bunları teker teker inceleyelim:





- Ana Sayfa** - Genel gösterge tablosunu içeren Ana Sayfa sekmesi (düğümünüze genel bakış ve hızlı eylemler).
- Gösterge Tablosu** - Widget'lar ve gelişmiş ölçümlerle özelleştirilebilir gösterge tablosu.
- Eşler** - Lightning eş yönetimi (diğer düğümlere bağlantılar).
- Kanallar** - Lightning kanallarının detaylı yönetimi.
- Rebalance** - Kanal dengeleme aracı (döngüsel ödemeler).
- İşlemler** - Yıldırım ödeme geçmişi (LN işlemleri).
- Forwards** - Yönlendirme istatistikleri (düğümünüz tarafından aktarılan ödemeler).
- Zincir** - Node'un On-Chain Wallet (On-Chain BTC: UTXO'lar, işlemler).
- Amboss** - Amboss ile entegrasyon (düğüm izleme, yedeklemeler, vb.).
- Araçlar** - Çeşitli araçlar (yedeklemeler, imzalı mesajlar, makaronlar, raporlar, vb.)
- Takas** - Boltz aracılığıyla On-Chain/Lightning takas işlevleri.
- Stats** - Gelişmiş istatistikler ve düğüm performans ölçümleri.



*(Not: ThunderHub sürümüne bağlı olarak, bazı bölümler biraz farklı başlıklara veya ek özelliklere sahip olabilir, ancak genel ilkeler aynı kalır)*



### Ana Sayfa (Genel kontrol paneli)



ThunderHub'ın **Ana Sayfa** sekmesi, oturum açtıktan sonra görüntülenen ana sayfadır. Lightning düğümünüzün durumu hakkında **global bir genel bakış** sunan ve rutin işlemler için **hızlı eylemler** öneren **Genel Gösterge Tablosu** içerir. Genellikle bulacağınız şeyler şunlardır:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- Bakiyeler ve kapasiteler:** Sayfanın üst kısmında ThunderHub mevcut bakiyelerinizi görüntüler. Burada genellikle On-Chain bakiyesini (düğümün Wallet'undaki Bitcoin On-Chain, Anchor ⚓ ile sembolize edilir) ve Lightning bakiyesini (kanallarınızın kapasiteleri, yıldırım Bolt ⚡ ile sembolize edilir) görürsünüz. Bu size On-Chain ve Lightning'de sahip olduğunuz fonlar hakkında anında bir fikir verir. Birden fazla hesabınız veya kanalınız varsa, doğru hesapta olduğunuzdan emin olun (örneğin Mainnet vs Testnet).





- Temel istatistikler:** Gösterge paneli düğümünüz için bazı genel ölçümleri gösterebilir - örneğin, açık kanal sayısı, bağlı eşlerin sayısı, kazanılan yönlendirme ücretleri (varsa) vb. Bu, düğümün son faaliyetlerinin ve sağlığının bir özetidir.





- Hızlı Eylemler:** Kontrol paneli, menüler arasında gezinmek zorunda kalmadan en yaygın görevleri hızlı bir şekilde yürütmek için düğmeler içerir. Bu hızlı eylemler şunları içerir :





  - Hayalet**: Amboss aracılığıyla özel bir Lightning Address kurun.
  - Bağış yapın**: Lightning üzerinden bağış yapın.
  - Giriş/Giriş Yap**: Amboss hesabınıza bağlanın (Quick Connect) ve düğümünüzün bilgilerini görüntülemek için doğrudan Amboss.space'e gidin.
  - Address** : Ödeme yapmak için bir Lightning Address girin.
  - Aç**: Yeni bir Lightning kanalı açın. Tıklandığında, kanalın açılacağı uzak düğümün URI'sini, miktarı ve varsa kullanılacak maksimum On-Chain ücretini girmek için bir form açılır.
  - Kod çöz**: Ödeme yapmadan önce ayrıntıları görüntülemek için bir Lightning Invoice veya LNURL kodunu çözün.
  - LNURL**: Lightning ödemeleri veya para çekme işlemleri için LNURL'leri işleyin.
  - LnMarkets Giriş**: Ticaret için LnMarkets'e giriş yapın.



Bu hızlı eylemler, Interface'nın çeşitli sekmelerinde gezinmek zorunda kalmadan en sık yapılan işlemleri doğrudan ana sayfadan gerçekleştirmenize olanak tanır.



Kısacası, ThunderHub kontrol paneli düğümünüze **hızlı bir bakış** sağlar ve en sık yapılan işlemleri (gönderme/alma, kanal açma) tek bir tıklamayla gerçekleştirmenize olanak tanır. Günlük yönetim için ideal bir başlangıç noktasıdır.



### Gösterge Tablosu



Gösterge Panosu** bölümü Ana Sayfa sekmesinden ayrıdır ve daha gelişmiş, özelleştirilebilir bir gösterge panosu sunar. Bu bölüm, bir düğüm operatörü olarak ihtiyaçlarınıza göre belirli widget'larla özelleştirilmiş bir görünüm oluşturmanıza olanak tanır.





- Özelleştirilebilir widget'lar:** Sabit bir düzene sahip olan Ana sayfanın aksine, Dashboard tam olarak hangi Elements'nin görüntüleneceğini ve bunların nasıl düzenleneceğini seçmenize olanak tanır.



![Dashboard sans widgets activés](assets/fr/06.webp)



Hiçbir widget etkinleştirilmemişse, özelleştirme parametrelerine erişmek için bir "Ayarlar" düğmesiyle birlikte bir "Etkin Widget Yok!" mesajı görürsünüz.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Ayarlarda, kategoriler halinde düzenlenmiş çok çeşitli widget'lar arasından seçim yapabilirsiniz: "Lightning - Bilgi", "Lightning - Tablo", "Lightning - Grafik" vb. Her widget "Göster/Gizle" düğmeleriyle ayrı ayrı etkinleştirilebilir veya devre dışı bırakılabilir.



![Bas de la page des paramètres](assets/fr/08.webp)



Ayarların alt kısmında, gösterge tablosuna dönmek için "Gösterge Tablosuna" düğmesini ve varsayılan ekranı sıfırlamak için "Widget'ları Sıfırla" düğmesini bulacaksınız.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Yapılandırıldıktan sonra, gösterge tablonuz çeşitli grafikler ve metrikler görüntüleyebilir: Yıldırım ödeme grafikleri, kesilen fatura sayısı, iletme istatistikleri, ayrıntılı bakiyeler vb.





- Gelişmiş ölçümler:** Grafikler ve gerçek zamanlı verilerle düğümünüzün performansı hakkında daha ayrıntılı istatistiklere erişin.





- Yapılandırılabilir genel bakış:** İster sıradan bir kullanıcı ister birden fazla yönlendirme kanalını yöneten profesyonel bir operatör olun, ekranı kendinize göre uyarlayın.





- Modüler Interface:** Gerektiği gibi widget ekleyin veya kaldırın: ileriye dönük grafikler, likidite ölçümleri, düğüm sağlığı uyarıları vb.



Bu bölüm özellikle belirli ölçümleri izlemek veya Lightning düğümlerine daha teknik bir genel bakış elde etmek isteyen ileri düzey kullanıcılar için kullanışlıdır. Bilgilerin nasıl görüntüleneceği konusunda daha fazla esneklik ve kontrol sunarak Ana Sayfa bölümünü tamamlar.



### Akranlar



Eşler** bölümü, eşler olarak size bağlı olan tüm Lightning düğümlerini listeler. Bir **eş**, Lightning Network üzerinde doğrudan düğümden düğüme bağlantıdır. Düğümünüz açık bir kanal olmadan da eşlere bağlanabilir (örneğin, sadece ağdaki Exchange dedikodu bilgilerine) veya elbette her açık kanal otomatik olarak bağlı bir eş anlamına gelir.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Eşler sekmesinde şunu göreceksiniz :





- Bilgi sütunları:** Interface, senkronizasyon durumu, bağlantı türü (clearnet veya Tor), ping, alınan/gönderilen satoshiler ve değiş tokuş edilen veri hacmi gibi yararlı ayrıntıları görüntüler.
- Bir eş ekleyin:** ThunderHub, sağ üst köşedeki **"Ekle "** düğmesi aracılığıyla yeni bir eşe manuel olarak bağlanmanıza olanak tanır. Düğümün URI'sini girmeniz gerekir (format `<public_key>@<socket>`). Doğrulandıktan sonra, ThunderHub ilgili `lncli connect` komutunu gönderir. Düğüm çevrimiçi ve erişilebilir durumdaysa, eşler listenize eklenecektir.



### Kanallar



Kanallar** sekmesi Lightning kanal yönetiminin kalbidir. Muhtemelen en sık başvuracağınız bölümdür. Tüm Lightning kanallarınızı** ayrıntılarıyla birlikte sunar ve bu kanallar üzerinde yönetim eylemleri gerçekleştirmenize olanak tanır.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



İşte Kanallar sayfasında bulacaklarınız:





- Kanal listesi görünümü:** Her açık (veya açılan/kapanan) kanal, genellikle uzak düğümün takma adı, toplam kanal kapasitesi ve yerel ile uzak likiditenin dağılımını gösteren renkli bir çubukla birlikte listelenir. ThunderHub kanal dengesini göstermek için bir renk kodu (genellikle mavi/Green) veya yüzde kullanır: örneğin, yerel payınız için mavi, uzak pay için Green. Bir kanal mükemmel şekilde dengelenmişse (50/50), çubuk her rengin yarısı olacaktır. Bu, hangi kanalların dengesiz olduğunu bir bakışta belirlemenizi sağlar (tüm mavi = neredeyse tüm yerel, tüm Green = neredeyse tüm uzak).





- Bilgi sütunları:** Interface, Durum, Mevcut Eylemler, Eş Bilgisi, Kanal Kimliği, Kapasite, Etkinlik, Ücretler ve Bakiye gibi ayrıntılı sütunları grafik likidite ekranı ile görüntüler.





- Ekran yapılandırması:** Sağ üst köşedeki bir dişli çark, kanal ekranını tercihlerinize göre özelleştirmenizi sağlar.





- Durum:** Ayrıca durum göstergelerini de göreceksiniz - örneğin `Aktif` (kanal açık ve çalışır durumda), `Çevrimdışı` (eşin bağlantısı kesildi, bu nedenle kanal anlık olarak kullanılamıyor), `Beklemede` (On-Chain onayı bekleyen açılışlar veya kapanışlar için).





- Bir kanaldaki eylemler:** Her kanal için ThunderHub eylem düğmeleri (genellikle simge şeklinde) sağlar:



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





  - Ücretleri düzenleyin:** Interface "Kanal Politikasını Güncelle" tüm kanal parametrelerini ayarlamanızı sağlar: Temel Ücret, Ücret Oranı (ppm cinsinden), CLTV Delta, Maks HTLC ve Min HTLC. Bu, yönlendirme trafiğini çekmek (veya caydırmak) amacıyla ücret politikalarınızı kanal başına ayrı ayrı ayarlamanıza olanak tanır. *(Not: ThunderHub otomatik bir ücret yönetimi aracının yerini tutmaz, ancak manuel ayarlama için çok etkilidir)*
  - Kapatma Kanalı (*Kapat*)**: Interface "Kapatma Kanalı", ücretleri (Sats/vByte cinsinden) tanımlayarak size **işbirlikçi kapatma** (varsayılan) veya **zorla kapatma** (*Zorla Kapatma*) arasında seçim yapma imkanı verir. **Önemli:** On-Chain mutabakat gecikmelerinden ve daha yüksek ücretlerden kaçınmak için mümkün olduğunda her zaman işbirlikçi kapatmayı tercih edin. ThunderHub eşin çevrimiçi (işbirliği mümkün) olup olmadığını size söyleyecektir. Zorla kapatma durumunda, bu geri döndürülemez olduğundan ve bir zaman kilidiyle (genellikle 144 blok veya Bitcoin Mainnet'de ~ 1 gün) bir süpürme işlemini tetikleyeceğinden onayladığınızdan emin olun.
  - Yeni bir kanal açın:** Yeni bir kanal açmak için Kanallar sayfasının sağ üst köşesindeki dişli çarka tıklayın ve ardından "Aç "ı seçin. Daha sonra yeni veya mevcut bir eşe bir kanal başlatabilirsiniz. Bu sayfayı kullanmanın avantajı, önünüzde mevcut kanallarınızın bir listesinin bulunmasıdır, bu da yeni bir kanalı nerede açacağınıza karar vermenize yardımcı olabilir.



Kısacası, Kanallar bölümü size **her kanal üzerinde ince kontrol** sağlar. Burası likidite tahsisini yönlendirdiğiniz, hangi kanalların tutulacağına veya kapatılacağına karar verdiğiniz ve kanal başına yönlendirme parametrelerinizi ayarladığınız yerdir. ThunderHub, bu önemli düğüm yönetimi işlemleri için net bir Interface sunar.



### Yeniden dengeleme



Yeniden Dengeleme** sekmesi **kanal dengelemeye** ayrılmıştır. Dengeleme (veya *yeniden dengeleme*), Lightning Network aracılığıyla kanallarınızdan birinden diğerine **dairesel bir ödeme** yaparak, giden ve gelen kanallarınız arasındaki fon dağılımını yeniden ayarlamayı içerir. Bu, yeni fon getirmeden, likiditeyi çok dolu bir kanaldan çok boş bir kanala kaydırmanıza ve kanallarınızı daha kullanışlı hale getirmenize olanak tanır (dengeli bir kanal hem ödeme gönderebilir hem de alabilir).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub, aksi takdirde komut satırında sıkıcı olabilecek bu işlemi büyük ölçüde kolaylaştırır. Yeniden Dengeleme bölümünün nasıl kullanılacağı aşağıda açıklanmıştır:





- İlk kanal görünümü:** Yeniden Dengeleme'ye girdiğinizde, ThunderHub kanallarınızın bir listesini ve her biri için bir denge göstergesi görüntüler (Kanallar sayfasındakine benzer). Hangi kanalların dengede olmadığını hemen görebilirsiniz. ThunderHub kanalları artan denge sırasına göre sıralayabilir, böylece en dengesiz kanallar listenin en üstünde öne çıkar (0.0 tamamen yerel veya uzak anlamına gelir).





- Eş seçimi:** Interface, yeniden dengeleme için giden ve gelen eşlerin seçilmesini kolaylaştırır.





- Parametre ayarları:** Ayarlayabilirsiniz :
  - Ödemeye razı olduğunuz **maksimum ücret** (Sats ve ppm cinsinden)
  - "Sabit" veya "Hedef" seçeneği ile **yeniden dengelenecek miktar**
  - Yönlendirme yaparken kaçınılması gereken düğümler**
  - Rota bulma için maksimum deneme süresi**





- Kaynak**** kanalını seçin: Önce **giden (kaynak)** kanalı, yani taşınamayacak kadar fazla yerel likiditeye sahip olduğunuz kanalı seçin. Pratikte bu, yerel payınızın yüksek olduğu (>%50) bir kanaldır. 900,000'i yerel olmak üzere 1,000,000 Sat'a sahip bir A kanalı hayal edelim - Sat'ları başka bir yere göndermek için iyi bir aday. Bu A kanalına "giden" olarak tıkladığınızda ThunderHub bunu bir kaynak olarak işaretler.





- Hedef kanalı**** seçin: Ardından, likidite alması gereken **gelen (hedef)** kanalı seçin. Tipik olarak bu, tam tersinin olduğu bir kanal olacaktır - çoğu fon uzak taraftadır (örneğin, 1.000.000'dan yalnızca 100.000 yerel Sats). ThunderHub, kaynak kanal seçildikten sonra, en tamamlayıcı kanalların belirlenmesine yardımcı olmak için diğer kanalları ters sırada (azalan bakiye) sıralayacaktır. Yerel tarafta yer olan bir B kanalı seçin. ThunderHub daha sonra hangi iki kanalın seçildiğini açıkça gösterecektir (kaynak A ve hedef B).





- Ücret miktarını ve toleransı ayarlayın:** Bir form girmenize olanak tanır:





  - Yeniden dengelenecek **miktar** (Sats cinsinden). Genellikle, her iki kanalı \~50/50'de dengeleyecek miktara eşit bir miktar seçeriz. Örneğin ThunderHub kaynak kanalın fazla kapasitesinin yarısını önceden doldurabilir.
  - Bu işlem için ödemeye razı olduğunuz **maksimum ücret** (isteğe bağlı). Bu ücret Sats (dairesel yönlendirmenin toplam maliyeti) olarak ifade edilir. Boş bırakırsanız, ThunderHub maliyetten bağımsız olarak bir yol arayacaktır ki bu genellikle tavsiye edilmez (küçük bir yeniden dengeleme için 10 Sats veya maksimum ppm gibi bir sınır belirlemek daha iyidir).





- Rota Bul:** Bir rota bulmak için düğmeye tıklayın. ThunderHub, kaynak kanalınızdan ağ üzerinden kendi hedef kanalınıza bir rota hesaplamak için LND'u sorgular. Ücret kriterlerinizi karşılayan olası bir rota bulursa, bunu atlamaların ayrıntıları ve ücret maliyetiyle birlikte görüntüler. Örneğin, toplam 2 Sats ücretiyle 3 atlamalı bir yol bulduğunu gösterebilir.





- Yeniden dengelemeyi başlatın:** Önerilen rotadan memnunsanız, **Dengeleme Kanalı** üzerine tıklayın. ThunderHub daha sonra LND üzerinden dairesel ödeme başlatacaktır. Ödeme başarılı olursa, bir başarı bildirimi görürsünüz ve A ve B kanallarının bakiyeleri gerçek zamanlı olarak değiştirilir. ThunderHub bu kanallar için bakiye göstergesini güncelleyecektir (ideal olarak, daha iyi bakiyeyi gösteren öncekinden daha yeşil olacaktır).





- Ayarlamalar ve yinelemeler:** İlk denemede hiçbir rota bulunamazsa (veya çok pahalıysa), parametreleri ayarlayabilirsiniz :





  - Daha küçük bir miktar deneyin (bazen büyük bir miktar başarısız olurken kısmi bir yeniden dengeleme gerçekleşir).
  - Azami ücreti kademeli olarak artırın, ancak değerinden daha fazla ücret ödememeye dikkat edin.
  - Varsa, bir alternatif denemek için **Başka Bir Rota Al** düğmesini kullanın.
  - İşler gerçekten yapışkan hale gelirse başka bir çift kanal deneyin.



ThunderHub süreci çok **sezgisel ve görsel** hale getirir. Sadece 4 adımda (giden kanalı seçin, gelen kanalı seçin, tutar, doğrulama), eskiden karmaşık manuel komutlar gerektiren işlemleri yapabilirsiniz. Bu araç, iyi dengelenmiş bir düğümü korumak, yönlendirme performansınızı ve deneyiminizi iyileştirmek (tüm kanallarınızda ödeme göndermek ve almak daha kolay) için çok değerlidir.



Son olarak, yeniden dengelemenin yönlendirme maliyetlerini (ara düğümlere ödenen) tükettiğini, bu nedenle düğümünüzü daha akıcı hale getirmek için bir **yatırım** olduğunu unutmayın. Bunu akıllıca kullanın, örneğin sık kullandığınız bir hizmete giden bir kanalı desteklemek (gelen likidite) veya büyük bir yönlendirme kanalını dengelemek için. ThunderHub bunu **basit ve verimli bir şekilde** yapmanızı sağlar.



### İşlemler



ThunderHub'daki **İşlemler** bölümü düğümünüzün **Lightning** işlem geçmişine, yani kanallar aracılığıyla ödenen veya alınan ödemelere ve faturalara karşılık gelir. Bu, LN operasyonlarınız için bir tür hesap özetidir.



![Historique des transactions Lightning](assets/fr/14.webp)



Bu sekmede şunları bulacaksınız :





- Invoice grafiği:** Sağ üst köşede, zaman içinde alınan faturaların gelişimini gösteren bir grafik, düğümünüzün etkinliğini görselleştirmenize olanak tanır.





- Düğümünüzden* veya düğümünüze* yapılan tüm Lightning işlemlerinin kronolojik bir listesi. Her giriş şunları gösterebilir :





  - İşlem türü: **ödeme gönderdi** (giden ödeme) veya **ödeme aldı** (gelen, ücretli bir Invoice aracılığıyla).
  - Sats cinsinden tutar.
  - Tarih/saat.
  - Ödeme kimliği (Hash veya RHash ön görüntüsü) veya açıklama (Invoice'e bir not eklediyseniz).
  - Durum: **tamamlandı** veya muhtemelen **devam ediyor**/*başarısız* (örneğin, çözüm bekleyen bir ödeme, ancak genellikle LND bunu hızlı bir şekilde işler, bu nedenle On-Chain işlemlerine kıyasla burada çok az "beklemede" vardır).



Kısacası, İşlemler bölümü **LN etkinlik günlüğünüz** olarak işlev görür. Bir ödemenin geçip geçmediğini, kaç ücrete mal olduğunu kontrol etmek veya Lightning alışverişlerinizin geçmişini izlemek için çok kullanışlıdır. Forwards bölümü ile birlikte (daha sonra açıklanacaktır), node'unuzdan geçen paranın tam bir görünümüne sahip olacaksınız.



### Forvetler



Yönlendirme** sekmesi düğümünüzün **yönlendirme** faaliyetine, yani kanallarınızdan **geçen** ödemelere (Lightning Network üzerinde aracı düğüm olarak hareket ettiğinizde) ayrılmıştır. Düğümünüzü bir yönlendirme düğümü olarak işletiyorsanız, bu performansınızı izlemek için önemli bir bölümdür.



![Statistiques de routage Lightning](assets/fr/15.webp)



Forwards'da ThunderHub şunları sunar :





- Filtreler ve görüntüleme seçenekleri:** Sağ üstteki filtreler, verileri gün/hafta/ay/yıla göre sıralamanıza ve grafik veya tablo görüntüleme arasında seçim yapmanıza olanak tanır.





- Etkinlik mesajı:** Seçilen dönem boyunca herhangi bir yönlendirme yapılmamışsa, Interface bu örnekte gösterildiği gibi "Bu dönem için yönlendirme yok" mesajını görüntüler.





- Son yönlendirmelerin** bir **tablosu: her giriş, düğümünüz aracılığıyla **yönlendirilen** bir ödemeye karşılık gelir. Her yönlendirme için genellikle :





  - Timestamp,
  - yönlendirilen miktar (Sats cinsinden),
  - bu iletimden kazanılan **ücret** (Sats'te bu, gelen kanalda aldığınız ve giden kanalda gönderdiğiniz arasındaki farktır),
  - kullanılan gelen ve giden kanallar (genellikle eş takma adı veya kanal kimliği ile tanımlanır).
  - durumu (normalde *tamamlandı* veya bir iletim yolda başarısız olduysa başarısız).





- Toplanmış istatistikler**: ThunderHub, belirli bir dönemdeki (örneğin son 24 saat veya 7 gün vb., bazen yapılandırılabilir) toplamları ve istatistikleri hesaplar ve sayfanın üst kısmında görüntüler.



Kısacası, Forwards bölümü Lightning düğümünüzün yönlendirme etkinliğine **gerçek zamanlı bir genel bakış** sunar. Kanallar ve Yeniden Dengeleme bölümleriyle birlikte bu, düğümünüzü optimize etmek için eksiksiz bir paket oluşturur: Likidite için Kanallar / Yeniden Dengeleme, sonuçları (akışlar ve karlar) gözlemlemek için Forwards.



### Zincir



Zincir** bölümü LND düğümünüzün Bitcoin On-Chain Wallet yönetimine karşılık gelir. Bu Interface, kanal açmak veya kapalı kanallardan fon almak için kullanılan Bitcoin fonlarını görüntülemenizi ve yönetmenizi sağlar.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Chain'de şunları bulacaksınız:





- Bakiye On-Chain :** Wallet LND'de bulunan toplam BTC bakiyesini görüntüler.





- UTXO'ların Listesi:** Tüm harcanmamış çıktıları (UTXO) miktar, onaylar, Address ve her çıktı için formatla birlikte görüntüleyin.





- İşlem geçmişi:** Tüm Bitcoin işlemlerinin tür (giriş/çıkış), tarih, tutar, masraflar, onaylar, dahil etme bloğu, adresler ve txid ile ayrıntılı tablosu.



### Amboss



ThunderHub, Lightning düğümleri hakkında ayrıntılı bilgi, bir likidite pazarı ve şifreli kanal yedekleme ve kullanılabilirlik izleme gibi kullanışlı özellikler sunan **Amboss** platformuyla (amboss.space) entegre olur.



![Intégration Amboss avec ses options](assets/fr/17.webp)



ThunderHub'da Amboss bölümü, düğümünüzü Amboss hesabınıza **bağlamanıza** olanak tanır:





- Ghost Address:** Düğümünüz için gelen ödemeleri kolaylaştıran **kişiselleştirilmiş bir Lightning Address** kurun.





- Otomatik kanal yedeklemeleri:** Amboss'ta şifrelenmiş kanal yedeklemeleri** (SCB dosyaları) için amiral gemisi özelliği. Her kanal değiştirdiğinizde şifreli yedekleme güncellemelerini otomatik olarak göndermek için ayarlarda **Amboss Otomatik Yedekleme = Evet** seçeneğini etkinleştirin. Bir arıza durumunda, bu harici yedekleme sayesinde fonlarınızı kurtarabileceksiniz.





- Sağlık Kontrolleri:** Düğümünüzün Amboss'a düzenli ping göndermesini sağlamak için **Amboss Healthcheck = Yes** seçeneğini etkinleştirin. Düğümünüz çevrimdışı görünüyorsa uyarı alırsınız.





- Diğer özellikler:** Otomatik bakiye aktarımı, **Magma/Hydro** entegrasyonu (likidite piyasası) ve ayrıntılı performans istatistiklerine erişim.



Amboss entegrasyonu, doğrudan ThunderHub'dan erişilebilen otomatik harici yedekleme ve kullanılabilirlik izleme ile önemli bir **güvenlik Layer** ekler.



### Araçlar



Araçlar** bölümü, düğümünüzü yönetmek için çeşitli gelişmiş araçları bir araya getirir. İşte ana Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- Yedeklemeler:** Kanal yedeklemelerinizi (SCB) manuel olarak yönetin. ThunderHub kanallarınızın **tüm yedek dosyasını** indirmenize izin verir ("Tüm kanalları yedekle -> İndir" seçeneği). Bu `channel-all.bak` dosyasını güvenli bir yerde saklayın - bir çökme durumunda fonlarınızı kurtarmak için gereklidir. Ayrıca bir düğümü yeniden dağıtırken bir yedekleme dosyasını ** içe aktarabilirsiniz**.





- Muhasebe:** Kazanılan/ödenen ücretler ve belirli bir dönem boyunca yönlendirilen hacimler dahil olmak üzere finansal raporlar için dışa aktarma aracı.
- İmzalı mesajlar:** **Lightning düğümünüzün Ownership'ını kriptografik imza ile kanıtlamak için düğümünüzle mesajları** imzalayın veya doğrulayın.
- Makaronlar (Fırın bölümü):** Özelleştirilmiş erişim oluşturmak için LND** makaronlarını yönetin. Interface "Fırın" her bir izni tam olarak seçmenize olanak tanır: "Eşler Ekle veya Kaldır", "Zincir Adresleri Oluştur", "Fatura Oluştur", "Makaron Oluştur", "Anahtar Türet", "Erişim Anahtarlarını Al", "Zincir İşlemlerini Al", "Faturaları Al", "Wallet Bilgilerini Al", "Ödemeleri Al", "Eşleri Al", "Faturaları Öde", "Erişim Kimliklerini İptal Et", "Zincir Adreslere Gönder", "Baytları İmzala", "Mesajları İmzala", "daemon'ü Durdur", "Bayt imzasını doğrula", "Mesajları doğrula" vb. Her izin, kişiye özel bir makaron oluşturmak için "Evet/Hayır" düğmeleriyle ayrı ayrı etkinleştirilebilir.
- Sistem bilgisi:** Wallet sürümünün ve etkinleştirilmiş RPC'lerin görüntülenmesi.



Kısacası, Araçlar bölümü gelişmiş yönetim işlevlerini - yedekleme, muhasebe, güvenlik ve erişim yönetimi - birleşik bir Interface'da bir araya getirir.



### Takas



ThunderHub'ın **Swap** sekmesi, Boltz hizmeti aracılığıyla Lightning satoshilerini Bitcoin On-Chain ile takas etmenizi sağlar. Bu özellik, bir kanalı kapatmadan fazla Lightning likiditesini kanala "boşaltmak" için kullanışlıdır.



![Interface de swap via Boltz](assets/fr/19.webp)



İşlem basittir:





- Tutar**: Değiştirilecek tutarı tanımlayın
- Address** : Bitcoin alımı Address girin
- Yürütme**: ThunderHub, Exchange'i otomatik olarak işlemek için Boltz ile iletişim kurar



**Avantajlar:**




- Velayet dışı hizmet (nakit velayet yok)
- Mevcut kanallarınızı koruyun
- Kullanımı kolay entegre Interface



Boltz küçük bir komisyon alır ve siz standart Bitcoin işlem ücretini ödersiniz. ThunderHub onaylamadan önce tüm masrafları gösterir.



### İstatistikler



ThunderHub'ın **Stats** bölümü, performansı analiz etmek ve yönlendirmeyi optimize etmek için Lightning düğümünüz hakkında **gelişmiş istatistikler** sunar.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Bu bölüm maliyetlerinizi optimize etmek, başarılı kanalları belirlemek ve düğümünüzün genişlemesini planlamak için çok önemlidir.



## Sonuç



**ThunderHub**, Lightning **LND** düğümünün kolay yönetimi için temel araç olarak kendini kanıtlamıştır. Bu modern Interface, tüm temel işlevleri sunar: kanal yönetimi, ödemeler, izleme, otomatik yeniden dengeleme ve Amboss entegrasyonu gibi gelişmiş özellikler.



**Temel avantajlar:**




- Interface şık ve sezgisel
- Güçlü araçlar (yeniden dengeleme, Boltz takasları, otomatik yedeklemeler)
- Umbrel, Voltage, RaspiBlitz ve diğer dağıtımlarla uyumlu



ThunderHub, gelişmiş Lightning düğümü yönetimini demokratikleştirerek daha önce karmaşık teknik komutlar gerektiren işlemleri erişilebilir hale getirir. İster yeni başlayan ister deneyimli bir operatör olun, ThunderHub modern, kapsamlı bir Interface aracılığıyla Lightning düğümünüzü verimli bir şekilde yönetmenizi sağlar.



## Kaynaklar



**Resmi bağlantılar:**




- Resmi web sitesi:** [thunderhub.io](https://thunderhub.io)
- Dokümantasyon:** [docs.thunderhub.io](https://docs.thunderhub.io)
- GitHub kaynak kodu:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)