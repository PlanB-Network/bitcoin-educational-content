---
name: be-BOP
description: Be-BOP ile işletmenizden para kazanmaya yönelik pratik kılavuz
---

![cover-bebop](assets/cover.webp)



**be-BOP**, Bitcoin, banka hesabı ve Nakit olarak ödeme kabul ederken, tam bir özerklik içinde çevrimiçi ve çevrimdışı satış yapmak isteyen girişimciler için tasarlanmış bir e-ticaret platformudur. Çözüm, bağış toplamak veya çeşitli faaliyetlerinden para kazanmak isteyen her tür kuruluş için de kullanışlıdır.



Çözüm basit, hafif ve otonomdur. Geleneksel finansal hizmetlerin sınırlı olduğu veya hiç bulunmadığı bir ortamda bile çevrimiçi bir mağaza oluşturulmasını sağlar. Gerçekten de **be-BOP**, ödeme altyapısı olarak Bitcoin'i kullanarak bankalara erişimi olsun ya da olmasın verimli bir şekilde çalışacak şekilde tasarlanmıştır.



Bu eğitimde sizi adım adım:





- İlk online mağazanızı **be-BOP** ile oluşturun
- Vitrininizi ve ürünlerinizi kişiselleştirin
- Mevcut ödeme yöntemlerini yapılandırın
- Be-BOP** ile etkin online satış için en iyi uygulamaları anlayın



Bu eğitim ileri düzey teknik beceri gerektirmemektedir. Geliştiricilerin yanı sıra dijital ticarete egemen ve esnek bir şekilde başlamak isteyen esnaf, tüccar, kooperatif veya girişimcilere yöneliktir.



## Be-BOP'u kendi sunucunuza kurmak için ön koşullar



Be-BOP'u kurmaya başlamadan önce aşağıdaki teknik altyapıya sahip olduğunuzdan emin olun. Bu Elements platformun doğru çalışması için gereklidir:



### S3 uyumlu depolama



be-BOP, dosyaları (ürün resimleri gibi) yönetmek için bir depolama sistemi kullanır. Bu, bir S3 hizmetine erişim gerektirir, örneğin:





- [MinIO](https://min.io/) kendi kendine barındırılan
- Amazon S3 (AWS)
- Scaleway Nesne Depolama



Bir kova yapılandırmanız ve aşağıdaki bilgileri sağlamanız gerekecektir:





- S3_BUCKET**: kova adı
- S3_ENDPOINT_URL**: S3 hizmetinize erişim bağlantısı
- S3_KEY_ID** ve S3_KEY_SECRET: erişim kodlarınız
- S3_REGION**: S3 hizmetinizin bölgesi



### ReplicaSet modunda MongoDB veritabanı



be-BOP, mağaza, kullanıcı, ürün ve diğer verileri depolamak için MongoDB kullanır.



İki seçeneğiniz var:





- MongoDB'yi yerel olarak **ReplicaSet modu etkin** olarak yükleyin
- MongoDB Atlas** gibi çevrimiçi bir hizmet kullanın



Aşağıdaki değişkenlere ihtiyacınız olacak:





- MONGODB_URL**: veritabanı bağlantısı Address
- MONGODB_DB**: veritabanı adı



## Node.js ortamı



be-BOP Node.js ile çalışır. Node.js** sürüm 18 veya daha yüksek ve **Corepack** etkin olduğundan emin olun (pnpm gibi paket yöneticilerini yönetmek için gereklidir). Çalıştırılacak komut `corepack enable`



### Git LFS yüklü



Bazı kaynaklar (büyük resimler gibi) Git LFS (Büyük Dosya Depolama) aracılığıyla yönetilir. Git LFS'nin makinenizde `git lfs install` komutu ile kurulu olduğundan emin olun. Bu önkoşullar yerine getirildikten sonra, bir sonraki adıma geçmeye hazırsınız: be-BOP'u indirmek ve yapılandırmak.



**Not:** Yazılım dağıtımı için teknik bir kılavuz ayrı bir eğitimde mevcuttur.



## Super-Admin hesabı oluşturma



Be-BOP ilk kez başlatıldığında, bir **Super Admin** hesabı oluşturulur. Bu hesap, arka ofis işlevlerini yönetmek için gereken tüm yetkilere sahiptir. Bir hesap oluşturmak için aşağıdaki adımları izleyin:





- Yourresiteweb/admin/login` adresine gidin
- Güvenli bir kullanıcı adı ve parola ile bir süper yönetici hesabı oluşturun



Bu hesap size tüm arka ofis işlevlerine erişim sağlayacaktır. Oluşturulduktan sonra kullanıcı adınızı ve şifrenizi girerek giriş yapabilirsiniz.



![login](assets/fr/001.webp)



## Back-Office yapılandırması ve güvenliği



Interface arka ofis bağlantınızı yapılandırmadan önce benzersiz bir Hash oluşturmanız gerekir. Bu, Interface yöneticinize giden bağlantı bağlantısını çalmaya çalışan kötü niyetli kişilere karşı koruma sağlar.



Hash oluşturmak için `/admin/Ayarlar` bölümüne gidin. Güvenliğe ayrılmış bölümde (örn. "Yönetici Hash") benzersiz bir dize (Hash) tanımlayın. Kaydedildikten sonra, yetkisiz kişilerin erişimini kısıtlamak için arka ofis URL'si değiştirilecektir (örn. `/admin-yourhash/login`).



![hash-login](assets/fr/002.webp)



2.2. Bakım modunu etkinleştirin (gerekirse)



Yine /admin/Ayarlar'da, (Ayarlar > Interface grafikleri üzerinden Genel) sayfanın altındaki "bakım modunu etkinleştir" seçeneğini kontrol edin.



![maintenance-mode](assets/fr/003.webp)



Gerekirse, bakım sırasında ön ofise erişimi etkinleştirmek için yetkili IPv4 adreslerinin bir listesini (virgülle ayrılmış) belirtebilirsiniz. Arka ofis yöneticilerin erişimine açık kalır.



![ip-bebop](assets/fr/004.webp)



## İletişim kurulumu



Be-BOP'un bildirim göndermesini sağlamak için (örneğin siparişler, kayıtlar veya sistem mesajları için) en az bir iletişim yöntemi yapılandırmanız gerekir. İki seçenek mevcuttur: e-posta (SMTP) veya Nostr.



### SMTP yapılandırması (e-posta)



be-BOP bir SMTP sunucusu üzerinden e-posta gönderebilir. Genellikle bir e-posta hizmeti (örneğin Mailgun, Gmail, vb.) tarafından sağlanan geçerli SMTP kimlik bilgilerine ihtiyacınız olacaktır.



İşte bilmeniz gerekenler:



SMTP_HOST: SMTP sunucusu Address (örn. smtp.mailgun.org)



SMTP_PORT: kullanılacak bağlantı noktası (genellikle 587 veya 465)



SMTP_USER: kullanıcı adınız (genellikle bir e-posta Address)



SMTP_PASSWORD: şifreniz veya API anahtarınız



SMTP_FROM: gönderen olarak görünecek e-posta Address




### Nostr yapılandırması



be-BOP, merkezi olmayan bir mesajlaşma altyapısı olan Nostr protokolü aracılığıyla bildirimler göndermenizi sağlar. Bunu yapmak için, bir Nostr özel anahtarını (NSEC) generate veya Supply yapmanız gerekir. Bu anahtarı doğrudan be-BOP'un Nostr'a ayrılmış bölümündeki Interface aracılığıyla generate yapabilirsiniz. Bu Elements doğru şekilde yapılandırıldığında, be-BOP kullanıcılarınıza otomatik olarak mesaj ve uyarı gönderebilecektir.



## Uyumlu ödeme yöntemleri



be-BOP, müşterilerinize daha fazla esneklik sunmanıza olanak tanıyan çeşitli ödeme çözümleriyle uyumludur. Size en uygun ödeme yöntemini ayarlamak için ihtiyacınız olan şey burada.



### Bitcoin Onchain



be-BOP, Bitcoin ödemelerini doğrudan Blockchain (On-Chain) üzerinden basit ve güvenli bir şekilde kabul etmenizi sağlar.



**Yapılandırma adımları:**





- Ödeme Ayarları** menüsüne gidin
- On-Chain ödeme parametrelerine erişmek için **Bitcoin Nodeless** üzerine tıklayın.
- Aşağıdaki alanları doldurun:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**İpucu:** Genişletilmiş genel anahtarınızı (Zpub) elde etmek için Bitcoin Wallet'ünüzün (Sparrow wallet, BlueWallet, Spectre, vb.) gelişmiş ayarlarına başvurabilirsiniz. İşlem geçmişini kullanmak istiyorsanız Wallet'ünüzün ** salt okunur olmadığından** emin olun.



### Lightning Network



be-BOP, Lightning Network sayesinde anında Bitcoin ödemelerini de kabul edebilir. Şu anda iki yapılandırma seçeneği mevcuttur:



**Phoenixd**



Ödeme Ayarları` menüsüne gidin, `Phoenixd` seçeneğine tıklayın



![phoenixd](assets/fr/006.webp)



Daha sonra, sizi Acinq tarafından geliştirilen ve Lightning ödemelerini kendi düğümünüzle yönetmenize olanak tanıyan bir arka uç olan Phoenixd örneğinize bağlayan ** şifreyi veya token kimlik doğrulamasını ** girmeniz gerekir, ancak ödeme kanallarını yönetmenin karmaşıklığı olmadan.



**İsviçre Bitcoin Ödemesi**



Bir Lightning düğümünü kendiniz yönetmek istemiyorsanız, **Swiss Bitcoin Pay** karmaşık bir altyapı olmadan Lightning ödemelerini kabul etmeye başlamak için ideal olan kullanıma hazır, yapılandırması kolay bir çözümdür.



Yapılandırma adımları:





- "Ödeme Ayarları" menüsünde `Swiss Bitcoin Pay` seçeneğine tıklayın
- Swiss Bitcoin Pay hesabınıza giriş yapın (veya henüz bir hesabınız yoksa bir tane oluşturun).
- Swiss Bitcoin Pay tarafından sağlanan API Anahtarını girin, ardından "Kaydet "e tıklayın



Kurulduktan sonra, be-BOP müşterileriniz için otomatik olarak generate Lightning faturaları oluşturacak ve ödemeleri doğrudan Swiss Bitcoin Pay hesabınıza alacaksınız. Bu çözüm, hızlı ve düşük maliyetli ödemeleri kabul ederken kişisel bir düğümün teknik karmaşıklığından kaçınmak isteyen kullanıcılar için idealdir.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Bitcoin'e ek olarak be-BOP, iyi bilinen ve yaygın olarak kullanılan uluslararası bir çözüm olan PayPal aracılığıyla nakit ödeme kabul etmenize de olanak tanır.



Yapılandırma adımları:





- Ödeme Ayarları` menüsüne gidin
- PayPal üzerine tıklayın
- Paypal hesabınıza (geliştirici bölümü) `Müşteri Kimliği` ve `Şifre` girin
- İstediğiniz para birimini seçin (örneğin **USD**, **EUR**, **XOF**, vb.)
- Kaydet'e tıklayın



![paypal](assets/fr/008.webp)



**Not:** Bu tanımlayıcıları generate'ya yüklemek için bir PayPal işletme hesabınızın olması gerekir. Bunları [geliştirici] portalı üzerinden edinebilirsiniz (https://developer.paypal.com)



### SumUp



Yazılım artık **SumUp** ödeme çözümünü entegre ederek kredi kartı ödemelerini basit, güvenli ve verimli bir şekilde kabul etmenizi sağlıyor. Bu işlevsellikten yararlanmak için bir başlangıç yapılandırması gereklidir. Net ve aşamalı bir uygulama için izlenecek adımlar burada numaralandırılmıştır:





- Geliştirici hesabınızı oluşturduğunuzda SumUp tarafından sağlanan gizli bir anahtar olan **API Anahtarınızı** girerek başlayın. Bu anahtar, SumUp hesabınız ile yazılım arasında güvenli bir bağlantı kurar.
- SumUp platformunda işletmenizi tanımlayan benzersiz kod ile `Tacir Kodu` alanını doldurun. Bu kod, işlemleri işletmenizle ilişkilendirmek için gereklidir.
- Para Birimi` alanında, işlemleriniz için kullandığınız ana para birimini seçin (örn. **EUR**, **USD**, **CDF**, vb.).
- Tüm alanlar doğru bir şekilde doldurulduktan sonra, ayarlarınızı kaydetmek için `Kaydet` düğmesine tıklayın. Sistem daha sonra SumUp hesabınızla bağlantıyı kuracak ve yazılımınız ödemeleri kabul etmeye hazır olacaktır.



![payment-sumup](assets/fr/009.webp)



Bu yapılandırmadan sonra, **SumUp** entegrasyonu aktif ve çalışır durumda olacak ve işlemlerinizi doğrudan yazılımdan hızlı bir şekilde nakde çevirmenize ve izlemenize olanak tanıyacaktır.



### Şerit



be-BOP ayrıca en popüler çevrimiçi ödeme platformlarından biri olan **Stripe** ile tam entegrasyon sunar. Stripe, kredi kartı, dijital Wallet ve diğer çeşitli ödeme yöntemleri aracılığıyla çevrimiçi ödemeleri kabul etmenizi sağlar. İşte nasıl etkinleştirileceği:





- Stripe kontrol panelinde sağlanan **gizli anahtarı** girin.
- Stripe tarafından da sağlanan **Genel Anahtar** alanını doldurun.
- Ana para birimini** seçin.
- Yapılandırmayı kaydedin, ardından `Kaydet` seçeneğine tıklayın.



![payment-stripe](assets/fr/010.webp)



⚠️ **Lütfen dikkat:** **be-BOP** içindeki faturalama seçeneklerini doğru şekilde yapılandırmak için faaliyetiniz için geçerli olan KDV rejimini (örneğin: satıcının ülkesinde KDV kapsamında satış, gerekçe kapsamında muafiyet veya alıcının ülkesinin KDV oranında satış) bilmeniz çok önemlidir.



## Para birimi yapılandırması



**be-BOP** gelişmiş para birimi yönetimi sunar ve çoklu para birimi ortamlarına ve özel muhasebe gereksinimlerine uyarlanmıştır. Finansal işlemlerde ve raporlamada tutarlılığı sağlamak için, sistemde kullanılan farklı para birimlerini uygun şekilde yapılandırmak çok önemlidir. İşte bu yapılandırma için izlenecek adımlar:





- Ana para birimini** seçin (`Ana para birimi`)
- Seçiniz `İkincil para birimi
- Referans para birimini** tanımlayın (`Fiyat referans para birimi`)
- Muhasebe para birimini belirtiniz



Tüm para birimleri doğru bir şekilde yapılandırıldıktan sonra, yazılım çoklu para birimi işlemlerinin otomatik ve doğru bir şekilde dönüştürülmesini sağlarken, sıkı muhasebe tutarlılığını da korur.



![settings-currencies](assets/fr/011.webp)



## E-posta veya Nostr aracılığıyla kurtarma erişiminin yapılandırılması



Yine `/admin/settings` içinde, **ARM** modülü aracılığıyla, süper yönetici hesabının bir **email Address** veya bir **recovery pub** içerdiğinden emin olun, böylece şifrenizi unutursanız prosedürü kolaylaştırır.



![settings-users](assets/fr/012.webp)



## Dil ayarları



Yazılım, uluslararası bir kitleye uyum sağlamak ve kullanıcı deneyimini geliştirmek için çoklu dil özelliği sunar. Çok dilli işlevselliği etkinleştirmek için mevcut dilleri yapılandırmak ve bir **varsayılan dil** tanımlamak önemlidir.



![settings-languages](assets/fr/13.webp)



## Be-BOP'ta Interface ve Kimlik yapılandırması



**be-BOP** tasarımcılara bir web sitesi tasarlamak için ihtiyaç duydukları tüm araçları sağlar. İlk adım, ayarlardan `/Admin > Merch > Layout` bölümünü açmaktır. Üst Çubuğu**, **Navbar** ve **Alt Çubuğu** yapılandırarak başlayın.



### Le Top Bar



Üst Çubuk** yapılandırması, önemli bilgileri doğrudan Interface'ın ilk satırında görüntüleyerek yazılımınızın görsel kimliğini kişiselleştirmenizi sağlar. Bu, marka tanınırlığını güçlendirir ve kullanıcılar için net bir bağlam sağlar.



#### Yapılandırma adımları:





- Marka adı` alanına şirketinizin, kuruluşunuzun veya ürününüzün adını girin. Bu isim Interface'in üst kısmında görünecek ve ana görsel kimliğinizi temsil edecektir.
- Web sitesi başlığını belirtin**: seçilen başlık platformun amacını özetlemelidir. Bu başlık başlıkta veya tarayıcı sekmesinde görünebilir.
- Web sitesi açıklaması ekle**: Burası girişiminizin kısa bir açıklamasını girdiğiniz yerdir. Bu açıklama, aracı kullanıcılar için bağlamsallaştırmaya yardımcı olur ve SEO amacıyla da kullanılabilir.



Bu bilgiler girildikten sonra **Üst Çubuk** çözümünüzün net, profesyonel ve tutarlı bir sunumunu gösterecektir.



#### Üst Çubuktaki Bağlantılar



Üst Çubuğun `Bağlantılar` bölümü, uygulamanızdaki veya harici sitelerdeki önemli sayfalara kısayollar eklemenizi sağlar. Bu bağlantılar doğrudan Üst Çubukta görüntülenerek kullanıcılarınıza hızlı ve yapılandırılmış erişim sunar.



#### Yapılandırma adımları:





- Bağlantı adını girin (Metin)**: `Metin` alanına, görüneceği şekilde bağlantının adını veya etiketini girin (örneğin, Ana Sayfa, İletişim, Yardım...).
- Address (Url)** bağlantısını belirtin: `Url` alanına hedef sayfanın (dahili veya harici) tam Address'sini girin.
- Gerekirse başka bağlantılar ekleyin**: her yapılandırma satırı `Text` ve `Url` alanlarını kullanarak ek bir bağlantı eklemenizi sağlar.
- Bağlantıları kaydet**: tüm bağlantılar girildikten sonra, bunları kaydetmek için "Üst çubuk bağlantısı ekle" düğmesine tıklayın.



Bu yapılandırma, web sitenizin farklı bölümlerinde veya tamamlayıcı kaynaklarda net, akıcı ve erişilebilir gezinme sunmanıza olanak tanır.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Navbar** bölümü be-BOP'unuzun genellikle Interface'ün yan veya üst kısmında bulunan ana navigasyon menüsünü yapılandırmanızı sağlar. Bu menü kullanıcıları uygulamanın çeşitli sayfalarına ve işlevlerine yönlendirir. Bağlantı yapılandırması basit ve sezgiseldir. İşte nasıl çalıştığı:





- Bağlantı adını girin (`Metin`)**: yapılandırma satırında, `Metin` alanını doldurarak başlayın. Bu, gezinti çubuğunda görüntülenen bağlantının adına karşılık gelir (örnekler: *Dashboard*, *Users*, *Settings*...).
- Bağlantı Address'ü (`Url`)** girin: `Metin` alanının yanında `Url` alanını bulacaksınız. Bu alana, bağlantının yönlendirilmesi gereken sayfanın Address'ünü girin. Bu, dahili bir rota veya harici bir sayfaya giden bir bağlantı olabilir.
- Gerekirse birden fazla bağlantı ekleyin**: İlk satırın altında, gerektiği kadar bağlantı eklemek için yeni `Text` ve `Url` alanları mevcuttur. Her satır ek bir navigasyon bağlantısını temsil eder.
- Bağlantıları kaydet**: Tüm Elements'i girdikten sonra, sonuçları kaydetmek ve gezinti çubuğunda görüntülemek için `Nav çubuğu bağlantısı ekle` düğmesine tıklayın.



Bu yapılandırma, yazılımın farklı bölümlerine erişimin verimli bir şekilde yapılandırılmasına olanak tanıyarak ergonomiyi ve kullanıcı deneyimini iyileştirir.



![navbar](assets/fr/015.webp)



### Altbilgi



Altbilgi** bölümü, faydalı bilgiler veya bağlantılar ekleyerek yazılımınızın altbilgisini özelleştirmenizi sağlar. Bağlantıları yapılandırmadan önce, belirli bir seçeneği etkinleştirerek başlayın:





- "Powered by be-BOP "** etiketinin görüntülenmesini etkinleştirin: bu etiketi altbilgide görüntülemek için `Display Powered by be-BOP` düğmesini etkinleştirin.
- Bağlantının adını girin (`Metin`)**: altbilgideki bağlantının ifadesine karşılık gelen `Metin` alanını doldurun (örnekler: *Şartlar*, *Gizlilik*, *İletişim*...).
- Bağlantı Address'yı belirtin (`Url`)**: `Url` alanına hedef sayfanın Address'sını girin (dahili veya harici).
- Gerekirse daha fazla bağlantı ekleyin**: istediğiniz kadar bağlantı oluşturmak için ek satırları kullanın.
- Bağlantıları kaydet**: bağlantıları kaydetmek için "Altbilgi bağlantısı ekle" düğmesine tıklayın.



![footer](assets/fr/016.webp)



### Görsel kişiselleştirme



**⚠️ Açık ve koyu temalar için logoların yanı sıra favicon'u** `Admin > Merch > Pictures` üzerinden ayarlamayı unutmayın.



Sitenizin görünümünü ve hissini nasıl özelleştireceğiniz aşağıda açıklanmıştır:



#### Resimler bölümüne gidin



Menü `Admin` > `Merch` > `Pictures`.



#### Yeni bir resim ekleyin



Yeni Resim'e tıklayın.



#### Yerel bir dosya seçin



Dosyaları Seç`e tıklayın, ardından Hard diskinizden bir görüntü seçin.



#### İçe aktarılacak dosyayı seçin



İçe aktarılacak resme çift tıklayın (açık logo, koyu logo veya favicon).



#### Görüntünün adlandırılması



`Resmin adı` alanını doldurun.



#### Resim ekle



İçe aktarma işlemini tamamlamak için `Ekle` seçeneğine tıklayın.



![pictures](assets/fr/017.webp)



### Satıcı Kimliği Kurulumu



#### Kimlik ayarları



Yönetici > Kimlik (veya Ayarlar > Kimlik) üzerinden erişilebilen bu bölüm, şirketinizin idari ve yasal bilgilerini yapılandırmanıza olanak tanır.



#### Yasal bilgiler





- İşletme adı**: resmi şirket adı.
- İşletme Kimliği**: yasal tanımlayıcı veya kayıt numarası (RCCM, SIRET...).



#### İşletme Address





- Sokak**: posta Address (sokak, numara...).
- Ülke**: ülke.
- Eyalet**: il veya bölge.
- Şehir**: şehir.
- Posta kodu**: posta kodu.



#### İletişim bilgileri





- E-posta**: profesyonel e-posta Address.
- Telefon**: şirket telefon numarası.



#### Banka hesabı





- Hesap sahibi adı**: hesap sahibinin adı.
- Hesap sahibi Address**: hesap sahibinin Address'i.
- IBAN**: Uluslararası Banka Hesap Numarası.
- BIC**: SWIFT/BIC kodu.



![bank-account](assets/fr/019.webp)



#### Faturalandırma





- Verileri önceden doldurmak için `Ana mağaza bilgileriyle doldur` seçeneğine tıklayın.
- Çok üst-sağ düzenleyici bilgileri**: faturalarda görünen yasal/vergi bilgileri için alan.
- Değişiklikleri kaydetmek için `Güncelle` düğmesine tıklayın.



**Not:** İhtiyaçlarınıza göre Invoice üzerinde görüntülenecek ek bilgileri de girebilirsiniz.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fiziksel mağaza Address



Fiziksel mağazası olanlar için, `Yönetici > Ayarlar > Kimlik` veya özel bir bölüme belirli bir tam Address ekleyin. Bu, resmi belgelerde ve gerekirse altbilgide görüntülenmesini sağlayacaktır.



![seller-id](assets/fr/021.webp)



## Ürün Yönetimi



### Yeni bir ürün oluşturma



Bir ürün eklemek veya değiştirmek için `Admin > Merch > Products` bölümüne gidin. Aşağıdaki alanları doldurun:



#### Temel bilgiler





- Ürün Adı**: ürünün adı (örneğin *BOP T-shirt limited edition*).
- Slug**: Boşluksuz URL tanımlayıcısı (örneğin `tshirt-bop-edition-limitee`).
- Takma ad** *(isteğe bağlı)*: özel bir alan aracılığıyla sepete hızlı ekleme yapmak için kullanışlıdır.



![product-config](assets/fr/028.webp)



#### Fiyatlandırma





- Fiyat Tutarı**: ürün fiyatı (örneğin `25,00`).
- Fiyat Para Birimi**: para birimi (EUR, USD, BTC, vb.).
- Özel ürünler**:
  - bu ücretsi̇z bi̇r üründür.
  - bu bi̇r i̇stedi̇ği̇ni̇ öde ürünüdür.



#### Ürün seçenekleri





- Tek ürün (`standalone`)**: sipariş başına yalnızca bir ekleme mümkündür (örn. bağış, giriş bileti).
- Varyasyonlu ürün**:
  - Standalone'u kontrol etme.
  - Üründe hafif farklılıklar var (stok farkı yok)` seçeneğini işaretleyin.
  - Ekle:
    - İsim** (örneğin *Boyut*),
    - Değerler** (örneğin: S, M, L, XL),
    - Varsa fiyat farkları** (örneğin: XL için `+2 USD`).



![product-details](assets/fr/029.webp)



## Stok yönetimi



### Ürün oluştururken gelişmiş seçenekler (Stok, Teslimat, Biletler, vb.)



#### Sınırlı stoklu ürün



Ürününüz sınırsız miktarda mevcut değilse, `Ürünün sınırlı stoğu var` seçeneğini işaretleyin. Bu, kalan miktarların otomatik olarak izlenmesini etkinleştirir. Bu kutu işaretlendiğinde, **mevcut stoku** gösteren bir alan görünür.



Sistem yönetir:





- Rezerve stok** → henüz ödemesi yapılmamış sepetlerdeki ürünler
- Satılan stok** → halihazırda satın alınmış ürünler



**Sepet rezervasyon süresi**: Bir müşteri sepetine bir ürün eklediğinde, bu ürün sınırlı bir süre için "rezerve edilir". Bu süreyi şuradan değiştirebilirsiniz: `Admin > Config > Cart reservation` (dakika cinsinden değer)



#### Teslim edilecek ürün?



`Ürünün müşterinin Address`ine gönderilecek fiziksel bir bileşeni var` seçeneğini işaretleyin. Bu, fiziksel olarak gönderilecek tüm ürünler için kullanışlıdır (kitaplar, tişörtler vb.)



#### Diğer seçenekler





- Bilet**: ürün bir etkinlik için bilet ise işaretleyin
- Rezervasyon**: bunun bir rezervasyon yuvası olup olmadığını kontrol edin (örneğin: oturum, randevu)



![product-options](assets/fr/030.webp)



### Eylem Ayarları (alt)



Bu bölüm, ürünün **nerede** ve **nasıl** görülebileceğini ve satın alınabileceğini belirler:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Sadece kullanmak istediğiniz kanalları kontrol edin.



## CMS sayfalarının ve widget'larının oluşturulması ve özelleştirilmesi



### Zorunlu CMS sayfaları



Yönetici > Merch > CMS'ye gidin. Mevcut sayfaların bir listesini göreceksiniz ve **CMS sayfası ekle** ile yenilerini ekleyebilirsiniz.



CMS sayfaları aşağıdakiler için önemlidir:





- Ziyaretçilerinizi bilgilendirin (örn. kullanım koşulları)
- Yasalara uymak (örn. gizlilik politikası)
- Belirli mağaza özelliklerini açıklayın (örn. IP toplama, %0 KDV)



Gerektiğinde başka sayfalar da ekleyebilirsiniz:





- Hakkımızda / Biz Kimiz
- Bizi destekleyin / Bağışlar
- SSS
- İletişim
- vs.



**İpucu: Her bir sayfanın **içeriğini**, **başlığını** veya **seo görünürlüğünü** değiştirmek için her bir bağlantıya veya simgeye tıklayın.



### Düzen ve grafik Elements



Adresine gidin: `Yönetici > Merch > Düzen`. Sitenizin görsel Elements'sini özelleştirebilirsiniz:



![product-options](assets/fr/032.webp)



#### Üst Bar





- Bağlantıları değiştirin veya silin (ÖR: ANA SAYFA, HAKKIMIZDA,...)
- Sitenin önemli bölümleri arasında gezinme



#### Navbar (ana gezinti çubuğu)





- Üst çubuğun altındaki gri alanda bulunur
- Hızlı erişim içerir: konfigürasyon`, `Ödeme Ayarları`, `İşlem`, `Node Yönetimi`, `Widgets`, vb.
- Sadece yöneticiler



#### Altbilgi





- Yönetici > Merch > Düzen'den düzenlenebilir
- İçerikler: iletişim bilgileri, faydalı bağlantılar, yasal bildirimler...



#### Görselleri özelleştirin



Gitmek için: `Yönetici > Merch > Resimler`



Yapabilirsin:





- Ana logoyu** değiştirin
- Düzeni değiştirin veya ekleyin **images**



#### Site açıklaması



Ayrıca `Resimler` bölümünde değiştirilebilir, temaya bağlı olarak üstbilgi veya altbilgide bir **özet veya slogan** görüntülemenize olanak tanır.



**Not:** Bu, görünümü marka kimliğinize (eğitim, ticari veya topluluk) göre ayarlamanıza olanak tanır.



### Widget'ları CMS sayfalarına entegre etme



Widget'lar** CMS sayfalarınızı dinamik veya görsel Elements ile zenginleştirir.



#### Widget oluşturma



Adresine gidin: `Yönetici > Widget`



Kullanılabilir widget örnekleri:





- Challenges**: zorluklar veya görevler
- Etiketler**: kategoriler veya anahtar kelimeler
- Kaydırıcılar**: görüntü karuselleri
- Teknik Özellikler**: Teknik özellikler tabloları
- Formlar**: formlar (iletişim, geri bildirim, vb.)
- Geri sayımlar**: zamanlayıcılar
- Galeriler**: resim galerileri
- Lider tabloları**: kullanıcı sıralamaları



![widgets](assets/fr/033.webp)



#### CMS sayfalarına entegrasyon



CMS sayfalarınızın içeriğinde **kısa kodlar** kullanın:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Mevcut parametreler**:





- `slug`: benzersiz widget tanımlayıcısı
- `display=img-1`: ürüne özel görsel
- width`, `height`, `fit`: görüntü boyutları ve stili
- autoplay=3000`: iki slayt arasındaki ms cinsinden süre



**Avantajlar**:





- Eklemesi kolay (kopyala ve yapıştır)
- Dinamik: Widget'ta yapılan herhangi bir değişiklik otomatik olarak yansıtılır
- Geliştirici gerekmez



## Sipariş yönetimi ve raporlama



### Sipariş takibi



Geçmiş siparişleri görüntülemek ve yönetmek için şu adrese gidin: `Yönetici > İşlemler > Siparişler`



Burada sitenizde verilen siparişlerin **tam listesini** bulacaksınız.



![orders](assets/fr/034.webp)



#### Görselleştirme ve arama



Interface, siparişleri çeşitli kriterlere göre aramanıza ve filtrelemenize olanak tanır:





- sipariş Numarası: sipariş numarası
- product alias: ürün tanımlayıcısı veya adı
- payment Mean": kullanılan ödeme yöntemi (kart, kripto, vb.)
- `Email`: müşteri e-postası



Bu filtreler hızlı aramaları ve hedefli yönetimi kolaylaştırır.



#### Her siparişin ayrıntıları



Bir siparişin üzerine tıklayarak, . içeren eksiksiz bir dosyaya erişebilirsiniz:





- Sipariş edilen ürünler
- Müşteri bilgileri
- Teslimat Address (varsa)
- Siparişle ilişkili tüm notlar



#### Bir siparişle ilgili olası eylemler



Yapabilirsin:





- Siparişi onayla (beklemedeyse)
- Bir siparişi iptal etme (bir sorun veya müşteri talebi durumunda)
- Etiket** ekleyin (dahili organizasyon için)
- Danışın / **iç notlar** ekleyin



**Not:** Bu bölüm iyi lojistik ve müşteri ilişkileri için gereklidir.



### Raporlama ve dışa aktarma



Satış ve ödeme istatistiklerine erişmek için:


yönetici > Ayarlar > Raporlama



![reporting](assets/fr/035.webp)



Burada **aylık ve yıllık raporlar** şeklinde işletmenize genel bir bakış bulacaksınız.



#### Rapor içeriği



Raporlar bölümlere ayrılmıştır:





- Sipariş Detayı**: sipariş sayısı, durum (onaylandı, iptal edildi, beklemede), evrim
- Ürün Detayı**: satılan ürünler, miktarlar, popüler ürünler
- Ödeme Detayı**: tahsil edilen tutarlar, ödeme yöntemine göre dağılım



#### Veri aktarımı



Her bölümde bir **Export CSV** düğmesi bulunur ve bu düğme ile:





- Verileri CSV formatında indirin
- Bunları Excel, Google E-Tablolar vb. programlarda açın.
- İdari veya muhasebe kullanımı için arşivleme
- Bunları dahili raporlar için kullanın



**Not:** performans takibi, muhasebe ve sunumlar için idealdir.



## Nostr Mesajlaşma yapılandırması (isteğe bağlı)



![nostr-config](assets/fr/036.webp)



Platform, belirli gelişmiş işlevler için **Nostr** protokolünü destekler:





- Merkezi olmayan bildirimler
- Şifresiz giriş
- Interface ışık idaresi



### Nostr özel anahtarının oluşturulması ve eklenmesi



Git:


admin > Düğüm Yönetimi > Nostr





- Eğer bir nsec'iniz yoksa **Nsec oluştur** seçeneğine tıklayın.
- Sistem bunu otomatik olarak generate yapabilir.
- Alternatif olarak, mevcut bir anahtarı kullanabilirsiniz (örneğin Damus veya Amethyst'ten).



Sıradaki:





- Nsec` anahtarını kopyalayın
- Bunu `.env.local` (veya `.env`) dosyanıza ekleyin: ``env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Nostr ile etkinleştirilen özellikler



Yapılandırıldıktan sonra çeşitli işlevler kullanılabilir:



**Nostr** aracılığıyla bildirimler





- Siparişler, ödemeler veya sistem olayları için uyarılar gönderin
- Yöneticiler veya kullanıcılar için



**Interface ışık idaresi**





- Bir Nostr istemcisi aracılığıyla erişilebilir
- Hızlı, mobil uyumlu yönetim sağlar



**Şifresiz bağlantı**





- Güvenli bağlantı ile giriş yapın (Nostr aracılığıyla gönderilir)
- Daha fazla kullanıcı güvenliği ve akışkanlık



## Tasarım ve tema özelleştirme



Mağazanızın görünümünü grafik tüzüğünüze uyarlamak için şu adrese gidin: `Yönetici > Ürün > Tema`



Burada özel bir tema **oluşturmak** ve **konfigüre etmek** için tüm seçenekleri bulacaksınız.



### Bir tema oluşturma



![theme](assets/fr/037.webp)



Bir tema oluştururken veya değiştirirken,:





- Renkler**: düğmeler, arka planlar, metin, bağlantılar vb. için.
- Yazı tipleri**: başlıklar, paragraflar, menüler için yazı tipi seçimi
- Grafik stilleri**: kenarlıklar, kenar boşlukları, aralıklar, blok şekilleri



### Özelleştirilebilir bölümler



Sitenin her bir bölümü bağımsız olarak ayarlanabilir:





- Başlık**: üst gezinme çubuğu
- Gövde**: ana içerik
- Altbilgi**: sayfanın altı



**Not:** Bu ayrıntı düzeyi, sitenin görselleri ile markanızın kimliği arasında tutarlılık sağlar.



### Tema aktivasyonu



Tema yapılandırıldıktan sonra:





- Kaydet** üzerine tıklayın
- Mağazanın **ana teması** olarak etkinleştirin



**Not:** aktif tema ziyaretçiler tarafından görülebilecek olan temadır.



## E-posta şablonlarını yapılandırma



Platform, kullanıcılara otomatik olarak gönderilen e-postaları kişiselleştirmenize olanak tanır. Adresine gidin: `Yönetici > Ayarlar > Şablonlar`



![emails-templates](assets/fr/038.webp)



### Şablon oluşturma / düzenleme



Her e-posta (sipariş onayı, unutulan şifre vb.):





- Konu**: e-postanın konusu (örneğin, "Siparişiniz onaylandı")
- HTML Gövde**: E-postada görüntülenen HTML içeriği



**Not:** Gerektiği gibi metin, resim, bağlantı vb. ekleyebilirsiniz.



### Dinamik değişkenleri kullanma



E-postaları dinamik hale getirmek için aşağıdaki gibi değişkenler ekleyin:





- `{orderNumber}}: gerçek sipariş numarası ile değiştirilir
- `{invoiceLink}}`: Invoice'e bağlantı
- `{websiteLink}}: Web sitenizin URL'si



**Not:** bu etiketler gönderildiğinde otomatik olarak değiştirilir.



### Gelişmiş ipuçları





- Mobil cihazlarda kolay okunabilmesi için **duyarlı** e-postalar oluşturun
- Eylem düğmeleri** ekleyin (ödeme, indirme, sipariş takibi)
- E-postalarınızı yayınlamadan önce kendinize göndererek test edin



## Belirli etiketleri ve widget'ları yapılandırma



### Etiket yönetimi



Etiketler içeriğinizi yapılandırmak ve zenginleştirmek için kullanılabilir. Bunlara erişmek için: `Yönetici > Widget`lar > Etiket`



![tags-config](assets/fr/039.webp)



### Etiket oluşturma



Aşağıdaki alanları doldurun:





- Etiket Adı**: görüntülenen etiket adı
- Slug**: benzersiz tanımlayıcı (boşluk veya aksan yok)
- Etiket Ailesi**: etiketleri kategoriye göre gruplar



![targsconfig](assets/fr/040.webp)



#### Mevcut aileler:





- creators`: yazarlar veya yapımcılar
- perakendeciler: satış elemanları veya satış noktaları
- `Temporal`: dönemler veya tarihler
- olaylar: ilişkili olaylar



### İsteğe bağlı alanlar



Bu alanlar, bir etiketi bir içerik sayfasıymış gibi zenginleştirmek için kullanılabilir:





- Başlık
- Altyazı
- Kısa** içerik
- Tam içerik** (Fransızca)
- CTA'lar** (eylem düğmeleri)



### Etiketleri kullanma



Etiketler olabilir:





- Ürünlere tahsis edilen
- CMS sayfalarına bir etiketle entegre edilir: [Tag=slug?display=var-1]



## İndirilebilir dosyaların yapılandırılması



Müşterilerinize indirilebilir belgeler sunmak için: `Admin > Merch > Files`



### Dosya ekleme



1. Yeni dosya** üzerine tıklayın


2. Bilgilendir:




   - Dosya adı** (örn. *Kurulum kılavuzu*)
   - Yüklenecek dosya** (PDF, resim, Word...)



**Not:** bir kez eklendiğinde, platform otomatik olarak bir **kalıcı bağlantı** oluşturur.



### Bağlantıyı kullanarak



Bu bağlantı daha sonra:





- CMS** sayfası (metin bağlantısı veya düğme olarak)
- Bir **e-posta istemcisi** (bir şablon aracılığıyla)
- Bir **ürün sayfası** (örn. kılavuz indirme)



Harici barındırmaya ihtiyaç duymadan *kullanım kılavuzları, teknik kılavuzlar, ürün sayfaları...* sağlamak için idealdir.



## Nostr-bot



Platform, otomatik bir bot aracılığıyla **Nostr** protokolü ile gelişmiş entegrasyon sunar.



Şu adrese gidin: Düğüm Yönetimi > Nostr



### Ana Özellikler



#### Röle yönetimi





- Bot tarafından kullanılan **röleleri** ekleyin veya kaldırın
- Gönderilen mesajların **erişimini** ve **güvenilirliğini** optimize edin



#### Otomatik tanıtım mesajı





- İlk kullanıcı etkileşiminde** otomatik bir mesajı etkinleştirin
- İçin idealdir:
  - Hizmetinizi sunma
  - Yararlı bir bağlantı gönderin (örn. SSS, iletişim, sipariş)



#### Yayınınızın belgelendirilmesi





- Bir **logo** ve bir **genel ad** ekleyin
- Doğrulanmış bir web alanına bağlantı**
- Nostr kimliğinizin güvenilirliğini ve tanınırlığını artırır



### Nostr-bot kullanım örnekleri





- Size **sipariş onayları** gönderiliyor
- Olaylara otomatik yanıt (örn. yeni sipariş)**
- Merkezi olmayan bir müşteri etkileşimi yaratmak**



## Çeviri etiketlerinin aşırı yüklenmesi



be-BOP çok dillidir (FR, EN, ES...), ancak çevirileri ihtiyaçlarınıza göre uyarlayabilirsiniz.



Bunu yapmak için şuraya gidin: `Ayarlar > Dil`



### Yükleme ve düzenleme



Çeviri dosyaları JSON'dadır. Yapabilirsin:





- İndir** dil dosyaları
- Mevcut metinleri değiştirin**
- Kendi çevirilerinizi ekleyin**



Orijinal dosyalara bağlantı:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Örnek:** `Add to cart` yerine `Ajouter au panier` veya `Acheter` yazın.



## Ekip Çalışması ve Satış Noktası (POS)



### Kullanıcı ve erişim hakları yönetimi



#### Roller oluşturma



Adresine gidin: `Yönetici > Ayarlar > ARM`



Bir rol oluşturmak için **Rol oluştur** seçeneğine tıklayın (örn. `Süper Yönetici`, `POS`, `Bilet denetleyicisi`).



Her rol şunları içerir:





- yazma erişimi**: yazma erişimi
- okuma erişimi**: okuma erişimi
- yasak eri̇şi̇m**: bölümler arasi



#### Kullanıcı oluşturma



Aynı menüde `Yönetici > Ayarlar > ARM`, ile bir kullanıcı ekleyin:





- giriş
- diğer ad
- e-posta kurtarma
- (isteğe bağlı) Nostr üzerinden bağlantı için `recovery npub`



Önceden tanımlanmış bir rolü atayın.



![pos-users](assets/fr/045.webp)



Salt okunur** kullanıcılar menüleri *italik* olarak görecek ve içeriği değiştiremeyecektir.



## Satış Noktası (POS) yapılandırması



### POS rolünün atanması



Bir kullanıcıya POS erişimi vermek için, `Point of Sale (POS)` rolünü atayın: `Yönetici > Yapılandırma > ARM`



Güvenli URL üzerinden bağlanabilir: `/pos` veya `/pos/touch`



### POS'a özgü özellikler



Be-BOP, fiziksel satışlara (mağaza, etkinlik vb.) adanmış bir Interface sunar.



#### Takma ad aracılığıyla hızlı ekleme



Cart` içinde bir alan ürün eklemenizi sağlar:





- Bir **bar kodunu** (ISBN, EAN13) tarayarak
- Manuel olarak bir **ürün takma adı** girerek



**Not:** ürün otomatik olarak sepete eklenir.



#### Ödeme araçları



POS destekleri:





- Türler
- Kredi kartı
- Lightning Network (kripto)
- Konfigürasyona göre diğerleri



İki gelişmiş seçenek mevcuttur:





- KDV muafiyeti**: gerekçelendirmede uygulanabilir (STK'lar, yabancılar...)
- Hediye indirimi**: zorunlu yorum ile istisnai indirim



#### İstemci tarafı görüntüleme



URL `/pos/session` bir **ikincil ekran** (HDMI, tablet...) için tasarlanmıştır:



Poster:





- Devam eden ürünler
- Toplam tutar
- Ödeme yöntemi
- Uygulanan indirimler



**Not:** müşteri siparişi canlı olarak takip ederken, satıcı `/pos` üzerine kaydeder.



### POS özeti



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Bu eğitimi dikkatle takip ettiğiniz için teşekkür ederiz.