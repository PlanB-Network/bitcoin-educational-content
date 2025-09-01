---
name: LNbits

description: Tüccar Muhasebe Platformu
---

![presentation](assets/lnbits-intro.webp)

# Muhasebe sistemi


LNbits, gelen ve giden fonlarınızı kontrol etmek ve yönlendirmek, web mağazanızı ve hatta kendi oluşturduğunuz Hardware Wallet veya ATM gibi cihazları bağlamak için birçok araçla doludur. Kullanıcı türleri şunları içerir:


- LNbits'i fon yönetimi ve ekstra özellikleri için bir Interface olarak kullanmak isteyen Wallet sahipleri.
- Bitcoin onchain ve Lightning Network ödemelerini kabul etmek isteyen çevrimiçi ve çevrimdışı tüccarlar veya hizmet sağlayıcılar.
- Lightning Network uygulamaları oluşturmak isteyen geliştiriciler.
- Node'larını muhasebe amacıyla LNbits sistemine entegre etmek isteyen node operatörleri.
- Bunların hepsinin farklı ihtiyaçları var. LNbits'i modüler bir şekilde inşa ediyoruz, böylece her kullanıcı özelliklerimizi size en uygun şekilde kullanabilir.


# Wallet yöneticisi


LNbits ücretsiz ve açık kaynaklı bir muhasebe sistemidir - bir düğüm yöneticisi değildir. Kanal yönetimi, LNbits'e LND veya c-lightning gibi bir fon kaynağı olarak bağlı olan Lightning düğümünün etki alanıdır. LNbits sistemindeki Süper Kullanıcı veya Yönetici Kullanıcılar, muhasebe özelliklerinin ve dahili uzantıların genel erişilebilirliğini ve yapılandırmasını yönetmekten sorumludur.


LNbits, kullanıcı ile Lightning düğümü arasında bir Interface görevi görerek ödeme ağını yönetmek ve etkileşimde bulunmak için basit, kullanıcı dostu bir yol sağlar.


LNbits'i node'unuz için bir "wordpress modüler çerçevesi" gibi düşünün. Çok sayıda kullanım durumu için birleştirebileceğiniz uzantılara dayalı, yönetimi kolay bir platform.


LNbits'i kendi banka finansal yönetim yazılımınız olarak düşünün. Düğümünüz ödeme yapabileceğiniz kanallar sunar ve LNbits, düğümünüzle birlikte gelen birden fazla yıldırım Wallet'u çalıştırabilmeniz için düğümünüzü genişletir. Bu cüzdanların mutlaka size ait olması gerekmez. Diyelim ki LN düğümünü çalıştıran kişi olarak zaten yeterli kanal likiditesine ve fonlara sahipsiniz ve şimdi arkadaşlarınıza, ailenize, kendi mağazanıza veya diğer normal tüccarlara bazı Bitcoin bankacılık hizmetleri sunmak istiyorsunuz.


Onlara node'unuzdaki diğer cüzdanlara ve tüm node likiditenize erişimleri olmadan node'unuzda bir "banka hesabı" açmaları için basit bir yol sunacaksınız, ancak yalnızca kendi bölümlerine. Düğümünüz (banka) yalnızca ödemeleri için bir taşıma sağlayıcısı olarak hareket eder (giriş / çıkış).


NOT: "müşterilerinizin" düğümünüzdeki LNbits banka hesaplarına yatırdıkları tüm fonlar doğrudan düğümünüzün LN kanallarına gidecektir. Bu, aslında bu fonların gerçek sahibinin SİZ olduğunuz anlamına gelir. Onların fonları için büyük bir sorumluluğunuz olacak. Kötü olmayın ve fonları alıp kaçmayın, kötü olmayın ve yüksek ücretler talep etmeyin. Fiat bankacılarını becermek istiyoruz, birbirimizi (Bitcoin kullanıcıları) becermek değil.


# Demo platformu


Demo [https://legend.lnbits.com](https://legend.lnbits.com) adresinde bulunabilir. Tamamen işlevseldir ve genel olarak LNbits ve LNURL'ün Lightning Network ve özellikleri hakkında bilgi edinmek için kullanılabilir. Sizi bundan alıkoyamasak da, üretim kurulumunuz için kullanmamanızı rica ediyoruz. Sadece yeni özellikleri test etmek için sunucular üzerinde sık sık çalışmakla kalmıyor, aynı zamanda sizi kendi düğümünüzü ve LNbits'i egemen bir şekilde çalıştırmaya teşvik etmek istiyoruz. Şu an için bir node çalıştırmanın çok fazla talep edildiğini düşünüyorsanız, LNbits'i buluttaki Opennode, Luna veya Votage gibi bir saklama fonu hizmetine veya Telegram'daki Lightning Tipbot'a bağlayabilirsiniz.


# LNbits broşürü


Bir tüccara veya bir inşaat arkadaşınıza bazı temel bilgileri vermek ister misiniz? Herkesin kullanabileceği ilk el ilanımızı duyurmaktan çok mutluyuz. Boyut, 6 sayfa (2 kat) ve 3508 genişlik ve 2480 piksel yükseklik ile küresel olarak tipik bir el ilanı formatıdır.


Tüccarlar için LNbits: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


İnşaatçılar için LNbits: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Bazı Temel Bilgiler


LNbits, LNURL protokolüne dayalı olarak çalışır, bu da isteklerin iki şekilde geçerli olduğu anlamına gelir: https:// clearnet bağlantısı (kendinden imzalı sertifikalara izin verilmez) veya http:// v2 / v3 onion bağlantısı olarak. LNURLp/w QR kodları veya NFC Kartları gibi vahşi ortamda kullanılabilecek LNbits hizmetleri sunmak için LNbits'i clearnet'e (https) açmanız gerekecektir.


LNbits'i kurmadan önce, LNbits'in ne olduğu ve sizin için hangi olasılıkları ortaya çıkardığı hakkında aşağıdaki genel kılavuzları okuyup anladığınızdan emin olun.



- [LND Kılavuzu](https://docs.lightning.engineering/) | LND'in Kurulması
- [LND Yapılandırma Örneği] (https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND Ayarları
- [CLN Kılavuzu](https://docs.corelightning.org/docs/installation) | CLN'nin Kurulması
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Watchtower çalıştır](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Çok önemli!


Belirli kullanım senaryolarında LNbits kullanan daha ayrıntılı kılavuzlar burada:



- [LNbits ile Başlarken] (https://darthcoin.substack.com/p/getting-started-lnbits) | Alt yığın kılavuzu
- [LNbits ile güvenliğiniz için ToDos](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Lightning Network'daki Özel Bankalar](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Alt Yığın Kılavuzu
- [Arkadaşlarınız ve aileniz için saklama cüzdanları çalıştırın](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Alt yığın kılavuzu
- [Küçük bir restoran / otel için LNbits](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Alt yığın kılavuzu
- [LNbits Streamer yardımcı pilotunu kullanma](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Alt yığın kılavuzu
- [NOSTR Marketinizi LNbits ile başlatın](https://darthcoin.substack.com/p/lnbits-nostr-market) | Alt yığın kılavuzu
- [Okul projeleri veya festival etkinlikleri için LNbits kullanımı](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Alt yığın kılavuzu



# LNbits'i yükleyin


## Temel kurulum kılavuzu


LNbits herhangi bir Linux OS makinesine kurulabilir. Güçlü bir makine veya sunucu gerektirmez, sadece yeterli RAM belleği ve veritabanı için biraz disk alanı gerektirir. Bir BTC/LN düğümünden (yerel PC veya uzak VPS) ayrı olarak veya düğümle aynı makinede birlikte çalıştırılabilir veya bir paket düğüm yazılım makinesine zaten yüklenmiş olabilir.


Poetry ve nix gibi en yaygın paket yöneticileri arasından seçim yapabilirsiniz. Varsayılan olarak, LNbits veritabanı olarak SQLite kullanacaktır. Yüksek yüke sahip uygulamalar için önerilen PostgreSQL'i de kullanabilirsiniz. [Poetry veya nix kullanarak temel kurulum için bir kılavuz](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Bu konuda yeni olan herkes için, LNbits'inizi belirli ortamlarda çalıştırmak için daha ayrıntılı adım adım kılavuzlar bulacaksınız:


- axel tarafından [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/)
- hannes tarafından [VPS üzerinde LNbits](https://github.com/TrezorHannes/vps-lnbits)
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) Leo tarafından


Ayrıca [nginx kullanarak bir fon kaynağı olarak PostgreSQ, LightningTipBot ile bir VPS üzerinde dockerised Kurulumu] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) hakkında bir video bulabilirsiniz.


[Daha fazla kurulum senaryosu burada](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


Paket yazılım düğümleri için lütfen LNbits hakkındaki özel belgelerine bakın: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


Teknik konularla ilgilenmiyorsanız ve ne fon kaynağınızı ne de lnbits'inizi kendiniz barındırmak istemiyorsanız, kullanabileceğiniz bir [LNbits SaaS sürümü] (https://saas.lnbits.com) (Hizmet olarak yazılım) vardır. Temelde buluttaki LNbits gibidir, ancak fon kaynağını (örneğin Node'unuz, bir LNbits Wallet, LNtipbot, fakewallet vb.) ve ortam değişkenlerini kendiniz tanımlayabilirsiniz - bu çoğunlukla diğer bulut çözümlerinde geçerli değildir.


[LNbits SaaS'ın belirli kullanım durumları için nasıl kullanılacağına dair ayrıntılı bir kılavuz] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Finansman kaynakları


LNbits bir düğüm yönetim yazılımı değil, bir LND veya CLN finansman kaynağının üzerinde LN odaklı bir muhasebe sistemidir. İlk kurulumdan sonra LNbits'inizi http://localhost:5000/ adresinden ziyaret edebilirsiniz.


Finansman kaynağını değiştirmek için süper kullanıcı URL'nize gidin ve "Sunucuyu Yönet" içinden bir finansman kaynağı seçin veya `.env` dosyasında `adminUI=TRUE` ayarını yaparsanız `LNBITS_BACKEND_WALLET_CLASS`ı gerekli kaynağınızla değiştirerek .env dosyasını düzenleyin.


.env dosyasını lnbits/ veya lnbits/apps/data klasörünüzün içinde, dizininizdeki dosyaları listelemek için komutu `ls -a` ile genişleterek bulabilirsiniz.


Ayrıca, istediğiniz fon kaynağını seçerek ek paketler yüklemeniz veya ek kurulum adımları gerçekleştirmeniz gerekebilir. Yeniden başlattıktan sonra yeni kurulumunuz aktif olacaktır.


LNbits için hangi fon kaynaklarını kullanabilirim?


LNbits birçok lightning-network finansman kaynağının üzerinde çalışabilir. Şu anda CoreLightning, LND, LNbits, LNPay, OpenNode için destek var ve daha fazlası düzenli olarak ekleniyor.

İyi bir likiditeye sahip ve iyi eşlerin bağlı olduğu bir kaynak seçmek önemlidir. Kamu hizmetleri için LNbits kullanırsanız, kullanıcılarınızın ödemeleri ancak o zaman her iki yönde de mutlu bir şekilde akabilir.


Bir arka uç Wallet (fon kaynağı), `.env` dosyasındaki veya Manage-Server bölümü altındaki süper kullanıcı hesabınızdaki aşağıdaki LNbits ortam değişkenleri kullanılarak yapılandırılabilir.

Eğer .env versiyonunu kullanmak isterseniz parametreleri burada bulabilirsiniz:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- Kıvılcım (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - lND_REST_MACAROON`: /file/path/admin.macaroon veya Bech64/Hex
  - lND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - lND_GRPC_ENDPOINT`: ip_adresi
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - lND_GRPC_MACAROON`: /file/path/admin.macaroon veya Bech64/Hex

Bunun yerine AES şifreli bir macaroon (daha fazla bilgi) da kullanabilirsiniz


  - lND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Makaronunuzu şifrelemek için `./venv/bin/python lnbits/wallets/macaroon/macaroon.py` dosyasını çalıştırın.


### LNbits (başka bir LNbits örneği)



- Bir bulut sunucusunda veya kendi ev sunucunuzda barındırılan LNbits örneği
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Sunucusu (!! Bunu üretim / ticari amaçlar için KULLANMAYIN, sadece test için !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot


Lightning Tipbot] (https://t.me/LightningTipBot) cihazınızı Telegram'dan bağlamak için aşağıdaki parametreyi ayarlamanız gerekecektir:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - lNBITS_KEY`: Anahtarı almak için Telegram'da LightningTipbot ile özel bir sohbette bir kez /api çalıştırmanız gerekecektir.


Ayrıca [LightningTipBot ile LNbits'in vps üzerinden] nasıl kurulacağına dair bu eğiticiye bakın (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


Buradan] (https://ibexpay.ibexmercado.com/onboard) kaydolun, ardından anahtarlarınızı/tokenlarınızı buradan alın, uç nokta https://ibexpay-api.ibexmercado.com'dur.

Daha fazla bilgi için bakınız [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

Invoice dinleyicisinin çalışması için LNbits'inizde herkese açık bir URL'ye sahip olmanız ve "Wallet Receive" olayı ile `<your LNbits host>/Wallet/webhook` adresini işaret eden bir [LNPay webhook] (https://dashboard.lnpay.co/webhook/) kurmanız gerekir. Ayar `https://mylnbits/Wallet/webhook`, herhangi bir ödeme hakkında bilgilendirilen uç nokta url'si olacaktır.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Invoice'in çalışması için LNbits'inizde herkes tarafından erişilebilir bir URL'ye sahip olmanız gerekir. Web kancası ayarı isteğe bağlıdır.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby, LN Wallet işlevlerine ve LNbits için fon kaynağı olarak kullanılabilecek LNDHUB hesabına sahip bir tarayıcı uzantısıdır. [Daha fazla ayrıntı burada] (https://getalby.com/).


Invoice'un çalışması için LNbits'inizde herkes tarafından erişilebilir bir URL'ye sahip olmanız gerekir. Manuel web kancası ayarına gerek yoktur. generate ve Alby token'a buradan erişebilirsiniz: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Ek / Sorun Giderme Kılavuzları


İhtiyaç duymanız halinde bazı ek talimatları burada bulabilirsiniz. Açıklamayı genişletmek için oka tıklayın.


### The Killswitch 🚨


Son zamanlarda sadece tüm dünyada değil LNbits'te de o kadar çok tehlikeli hata ortaya çıktı ki bu konuda bir şeyler yapmaya karar verdik. Artık bir güvenlik açığı veya fon kaybına yol açabilecek bir hata tekrar ortaya çıktığında uyarılar almayı ve/veya doğrudan harekete geçmeyi seçebilirsiniz.


![killswitchn](assets/lnbits-killswitch.webp)


Eğer void-Wallet'e geçilirse, örnekteki tüm kullanıcı tipleri normalde sağdaki tema/dil alanının yanında "LNbits Beta'da" uyarısını bulacağınız yerde sarı bir başlık görecektir - ve bu bir şeyler olduğuna dair en belirgin ipucudur. Pencerenin sol kısmında Green ile vurgulanan yeni sunucu sekmenize bir göz atın.


Nasıl çalışır? Killswitch etkinleştirildiğinde, yalnızca LNbits çekirdek ekibi tarafından kullanılabilen gizli bir github deposu X dakikalık bir aralıkta (belirtilebilir) kontrol edilecektir. Bu depoda savunmasız bir hata yayınlanırsa, abone olan tüm kurulumlarda killswitch'i tetikleyen ve lnbits örneğinizi void Wallet'ü kullanmaya geçiren bir sinyal görevi görür. Bulutlar temizlendiyse ve güvenlik güncellemesini yüklediyseniz, fon kaynağınızı düğümünüze, Wallet'e veya Sunucuyu Yönet bölümünden tekrar kullandığınız her şeye ayarlayabilirsiniz. Ne yapılandıracağınızı bilmiyorsanız, bu wiki'de fon kaynaklarını değiştirme hakkında bir bölüm vardır.



### Yönetici ve süper kullanıcı arasındaki fark


LNbits Yönetici Arayüzü, LNbits ayarlarını LNbits ön ucu üzerinden değiştirmenizi sağlar. Varsayılan olarak devre dışıdır ve `.env` dosyasında `LNBITS_ADMIN_UI=true` enviroment değişkenini ilk kez ayarladığınızda, ayarlar başlatılır ve kullanılır. Bundan sonra .env dosyasındakiler yerine veritabanındaki uygun ayarlar kullanılır.


### Süper Kullanıcı


Yönetici kullanıcı arayüzü ile sunucuya erişimi olan süper kullanıcıyı tanıttık, böylece sunucuyu çökertebilecek veya ön uç ve api aracılığıyla yanıt vermeyecek hale getirebilecek ayarları değiştirebiliriz, örneğin fon kaynağını değiştirmek gibi. Süper kullanıcı yalnızca veritabanının ayarlar tablosunda saklanır. Ayarlar "varsayılanlara sıfırlandıktan" ve yeniden başlatıldıktan sonra yeni bir süper kullanıcı oluşturulur. Ayrıca bir süper kullanıcının varlığını kontrol etmek için API rotalarına bir dekoratör ekledik. Kimliği api ve ön uç üzerinden asla gönderilmez ve yalnızca süper kullanıcı olup olmadığınızı bir bool (evet / hayır) alır.


Yalnızca süper kullanıcının "Yükleme" bölümü aracılığıyla farklı cüzdanlara satoshileri brrrr etmesine izin verilir.


Süper kullanıcıyı, oluşturulduğunda webhook aracılığıyla başka bir servise de gönderebilirsiniz. Daha fazla bilgi için https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


Ön uçta, Sunucuyu Yönet bölümünü açıp Tema -> Özel Logo'yu seçerek "Wallet oluştur" sayfasında gösterilen mağaza görüntüsünü değiştirme olanağını da bulacaksınız.


### Yönetici Kullanıcılar


Çevre değişkeni: `LNBITS_ADMIN_USERS`, kullanıcı kimliklerinin virgülle ayrılmış listesi. Yönetici Kullanıcılar yönetici kullanıcı arayüzündeki ayarları değiştirebilir - fon kaynağı ayarları hariç, çünkü bu sunucunun yeniden başlatılmasını gerektirir ve potansiyel olarak sunucuyu erişilemez hale getirebilir. Ayrıca `LNBITS_ADMIN_EXTENSIONS` içinde kendilerine ayrılmış tüm uzantılara erişimleri vardır.


### İzin Verilen Kullanıcılar


Çevre değişkeni: `LNBITS_ALLOWED_USERS`, virgülle ayrılmış kullanıcı kimlikleri listesi. Bu kullanıcıların tanımlanmasıyla LNbits artık herkes tarafından kullanılamayacaktır. Yalnızca tanımlı kullanıcılar ve yöneticiler LNbits önyüzüne erişebilir.




#### LNbits'i Güncelle

LNbits yerel örneğinizin normal bir güncellemesi, aşağıdaki CLI komutlarını kopyalayıp yapıştırarak yapılır:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Raspiblitz veya MyNode çalıştırıyorsanız, ek olarak bir

```
sudo systemctl restart lnbits
```

çünkü LNbits'i bir hizmet olarak çalıştırır.


Umbrel/Citadel'de komutlar şöyle olacaktır

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### SQLite'tan PostgreSQL'e geçiş


LNbits'i SQLite veritabanına kurup çalıştırdıysanız, LNbits'i büyük ölçekte çalıştırmayı planlıyorsanız postgres'e geçmenizi şiddetle tavsiye ederiz.


Taşıma işlemini kolayca yapabilen bir betik bulunmaktadır. Postgres'in zaten kurulu olması ve kullanıcı için bir parola olması gerekir (yukarıdaki Postgres yükleme kılavuzuna bakın). Ek olarak, geçişin çalışabilmesi için LNbits örneğinizin Schema veritabanını uygulamak için postgres üzerinde bir kez çalışması gerekir:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Umarım şimdi her şey çalışır ve taşınır... LNbits'i tekrar başlatın ve her şeyin düzgün çalışıp çalışmadığını kontrol edin.



#### Veritabanının yedeklenmesi ve geri yüklenmesi


Lütfen [yedekleme ve geri yükleme işlemi hakkındaki bu çok ayrıntılı kılavuza] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore) bakın.



#### LNbits Wallet'yi düğümümden finanse etmek işe yaramıyor


Sats'i LNbit'lerinizin fon kaynağı olan aynı düğümden göndermek istiyorsanız, LND.conf dosyasını düzenlemeniz gerekecektir.


Dahil edilecek parametreler şunlardır: `allow-circular-route=1`


Lütfen bunu LND.conf dosyanızın Uygulama seçenekleri bölümünde yapın. Bazı paket düğümlerinde LND'nin başlatılması aksi takdirde başarısız olabilir.


NOT: Bir LNbits hesabına para eklemek için bunun yerine yeni adminUI uzantısının "TopUp" seçeneği ile kullanılması önerilir.


#### Hata 426

Hata alıyorum: "lnurl'nin genel erişime açık https alanı veya tor üzerinden teslim edilmesi gerekir. 426 yükseltme gerekli"</summary>


Bu hata genellikle bir ngnix tünelinin arkasındaki LNbits'inizin LNURL Address'i doğru iletmemesinden kaynaklanır. LNbits'inizi durdurun ve .env dosyasını bu satırı ekleyerek düzenleyin:

`FORWARDED_ALLOW_IPS=*`


Ayrıca bir ngnix kurulumu kullanıyorsanız, ngnix yapılandırmasında bu başlıklara sahip olduğunuzdan emin olun:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Ağ Hatası

QR tararken "https hatası", ağ hatası" veya başka bir hata alıyorum</summary>


Kötü haber, bu pek çok nedeni olabilecek bir yönlendirme hatasıdır. Öncelikle QR'nin LNURL'sini [Lightning Decoder] (https://lightningdecoder.com/) ile kontrol edin, eğer orada garip bir şey bulabilirseniz. En olası sorunlardan birkaçını ve çözümlerini deneyelim.


LNbits yalnızca Tor üzerinden çalışır, lnbits.yourdomain.com gibi kamuya açık bir alanda açamazsınız



- Kurulumunuzun bu şekilde kalmasını istiyorsanız .onion URI kullanarak LNbits Wallet'ünüzü açın ve tekrar oluşturun. Bu şekilde QR, bu .onion URI üzerinden, yani yalnızca tor üzerinden erişilebilir olacak şekilde oluşturulur. Bu QR'yi bir .local URI'den generate yapmayın, çünkü internet üzerinden erişilemez - sadece ev LAN'ınızdan erişilebilir.
- QR'yi taramak için kullandığınız LN Wallet uygulamanızı bu kez tor kullanarak açın (bkz. Wallet uygulama ayarları). Uygulama tor sunmuyorsa, bunun yerine Orbot (Android) kullanabilirsiniz. LNbits'inizi clearnet/https için nasıl açacağınıza ilişkin ayrıntılı talimatlar için kurulum bölümüne bakın.



#### Başkalarının LNbit'lerim üzerinde cüzdan oluşturmasını engelleme


LNbit'lerinizi clearnet'te çalıştırdığınızda temelde herkes üzerinde generate bir Wallet yapabilir. Düğümünüzün fonları bu cüzdanlara bağlı olduğundan, bunu önlemek isteyebilirsiniz. Bunu yapmanın iki yolu vardır:


İzin verilen kullanıcıları ve uzantıları `.env` dosyasında yapılandırın ([env örneğine buradan bakın](https://github.com/lnbits/lnbits/blob/main/.env.example)). Bu yalnızca .env dosyasında `adminUI=FALSE` ayarını kullanırsanız çalışır, aksi takdirde bunu Sunucuyu Yönet -> Kullanıcılar -> İzin Verilen Kullanıcılar bölümünde yapmanız gerekir. Daha sonra diğer herkese izin verilmeyecektir.




#### Invoice sona erme zaman dilimini özelleştirin


Artık generate faturalarını özel bir son kullanma tarihi ile düzenleyebilirsiniz. Arka uçlarla uyumludur: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet şimdiye kadar!


.env dosyanızda `LIGHTNING_INVOICE_EXPIRY` ayarlayabilir veya tüm faturalar için varsayılan değeri değiştirmek için AdminUI'yi kullanabilirsiniz. Ayrıca /api/v1/payments uç noktasında, JSON verilerinde sona erme süresini ayarlayabileceğiniz yeni bir alan vardır.




## Wallet-URL silindi


### Wallet demo sunucusunda legend.lnbits


Kendi cüzdanlarınız için Wallet-URL, Export2phone-QR veya LNDhub'ınızın bir kopyasını her zaman güvenli bir yere kaydedin. LNbits kaybolduğunda bunları kurtarmanıza yardımcı OLAMAZ.


### Wallet kendi finansman kaynağınızda / düğümünüzde

Kendi cüzdanlarınız için Wallet-URL, Export2phone-QR veya LNDhub'ınızın bir kopyasını her zaman güvenli bir yere kaydedin. Tüm LNbits kullanıcılarını ve Wallet-ID'lerini LNbits kullanıcı yöneticisi uzantınızda veya sqlite veritabanınızda bulabilirsiniz. LNbits veritabanını düzenlemek veya okumak için LNbits /data klasörüne gidin ve sqlite.db adlı dosyayı arayın. Bu dosyayı excel ile ya da [SQLite browser] (https://sqlitebrowser.org/) gibi özel bir SQL-Editor ile açabilir ve düzenleyebilirsiniz.


Ayrıca cüzdanları CLI aracılığıyla dökebilir ve veritabanınızdaki her Wallet'i görüntüleyebilirsiniz.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


Çıktı aşağıdaki gibi görünecektir


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

ve bu değerleri aşağıdaki gibi bir url'ye koymak istiyorsunuz


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Burada f8a43fc363ea428db5c53b3559935f1f yerine addan önce gelen değeri (örneğimizde f8a43fc363ea428db5c53b3559935f1f) ve 1280ff5910a9c485a782a2376f338b6c sizin kullanıcınızdır ve addan sonra gösterilen değer olmalıdır. Sqlite3'ten çıkmak için


```
.quit
```

#### Lightning-Address tersi için LNURL


Fiatjaf'tan bu [kodlayıcıyı](https://lnurl-codec.netlify.app/) veya [bunu](https://lightningdecoder.com/) deneyin. Bir LNURLp'yi ödemek veya kontrol etmek için [LNurlpay](https://wwww.lnurlpay.com/)'i de kullanabilirsiniz. HTTP DEĞİL HTTPS belirtmelidir.



#### İnsanların LNURLp QR'ime ödeme yaparken görecekleri bir yorum yapılandırma

Bir LNURL-p oluşturduğunuzda, varsayılan olarak yorum kutusu doldurulmaz. Bu, ödemelere yorum eklenmesine izin verilmediği anlamına gelir.


Yorumlara izin vermek için, kutunun karakter uzunluğunu 1 ila 250 arasında ekleyin. Oraya bir sayı koyduğunuzda, yorum kutusu ödeme sürecinde görüntülenecektir. Ayrıca önceden oluşturulmuş bir LNURL-p'yi düzenleyebilir ve bu numarayı ekleyebilirsiniz.


![lnbits comments](assets/lnbits-comments.webp)


#### LNbits'e onchain BTC yatırın

Onchain BTC'den LN BTC'ye (LNbits'e) Exchange Sats yapmanın iki yolu vardır.


##### Harici bir takas hizmeti aracılığıyla.


LNb'nize erişimi olmayan diğer kullanıcılar [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) veya [ZigZag](https://zigzag.io/) gibi bir takas hizmeti kullanabilir. Bu, LNbits örneğinizden yalnızca LNURL/LN faturaları sağlıyorsanız, ancak bir ödeyenin yalnızca zincir üzerinde Sats'ü varsa, bu nedenle önce bu Sats'ü kendi taraflarında değiştirmeleri gerekecektir. Prosedür basittir: kullanıcı takas hizmetine onchain btc gönderir ve takasın hedefi olarak LNbits'ten LNURL / LN Invoice sağlar.


##### Onchain ve Boltz LNbits uzantısını kullanma.


Bunun ayrı bir Wallet olduğunu, LN fon kaynağınız üzerine LNbits tarafından "Wallet'iniz" olarak temsil edilen LN btc olmadığını unutmayın. Bu zincir üzerindeki Wallet, LNbits Boltz veya Deezy uzantısı kullanılarak LN btc'yi (örneğin hardwarewallet'ınıza) takas etmek için de kullanılabilir. LN ödemeleri için LNbits'inize bağlı bir web mağazası işletiyorsanız, tüm Sats'yı düzenli olarak LN'den onchain'e boşaltmak çok kullanışlıdır. Bu, LN kanallarınızda yeni taze Sats alabilmek için daha fazla alan sağlar.


Bitcoin Hardware Wallet'i olmayanlar için prosedür:



- Yeni bir zincirleme Wallet oluşturmak için Electrum veya Sparrow wallet kullanın ve yedek seed'yi güvenli bir yere kaydedin.
- Wallet bilgilerine gidin ve xpub'ı kopyalayın.
- LNbits - Onchain uzantısına gidin ve bu xpub ile yeni bir Watch-only wallet oluşturun.
- LNbits - Tipjar uzantısına gidin ve yeni bir Tipjar oluşturun. LN Wallet'in yanı sıra onchain seçeneğini de seçin.
- İsteğe bağlı - LNbits - SatsPay uzantısına gidin ve onchain btc için yeni bir ücret oluşturun. Onchain ve LN veya her ikisi arasında seçim yapabilirsiniz. Daha sonra paylaşılabilecek bir Invoice oluşturacaktır.
- İsteğe bağlı - LNbits'inizi bir Wordpress + Woocommerce sayfasına bağlı olarak kullanırsanız, LN btc mağazanız Wallet'a bir Watch-only wallet oluşturduğunuzda / bağladığınızda, müşteri aynı ekranda ödeme yapmak için her iki seçeneğe de sahip olacaktır.


LNbits'te bir ödeme aldığınızda, işlem günlüğü yalnızca işlemin devam ettirilmiş bir türünü gösterecektir.


![lnbits payment details](assets/lnbits-payment-details.webp)


İşlem genel görünümünüzde, alınan fonlar için küçük bir Green oku ve gönderilen fonlar için kırmızı bir ok bulacaksınız.


Bu oklara tıklarsanız, bir ayrıntı açılır penceresi ekli mesajları ve varsa gönderenin adını gösterir.


Ödemeler içinde görünecek bir isim yapılandırmak için, LNbits'te bunu yapmak şu anda mümkün değildir - ancak almak mümkündür. Bu yalnızca gönderenin LN Wallet'ü [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents) gibi [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) destekliyorsa mümkündür.


Daha sonra LNbits işlemlerinizin ayrıntılar bölümünde bir takma ad/takma isim göreceksiniz (oklara tıklayın). Orada herhangi bir isim verebileceğinizi ve eğer böyle bir isim alırsanız bunun gerçek gönderenin ismiyle ilgili olmayabileceğini unutmayın.


![lnbits namedesc](assets/lnbits-namedesc.webp)


LNbits hesabınızı bir Wallet uygulamasına aktarmak için, LNbits'inizi kullanmak istediğiniz hesap / Wallet ile açın, "uzantıları yönet "e gidin ve LNDHUB uzantısını etkinleştirin. LNDHUB uzantısını açın, kullanmak istediğiniz Wallet'yı seçin ve o Wallet için istediğiniz güvenlik seviyesine bağlı olarak "admin" veya "sadece Invoice" QR'ını tarayın.


Bir lndhub hesabı için Wallet uygulaması olarak [Zeus] (https://zeusln.app/) veya [Bluewallet] (https://bluewallet.io/) kullanabilirsiniz, böylece BW birden fazla Wallet'yi destekler.


Bunu yaparken LN ağ URI'sini de kendi düğümünüzünkine ayarlamanızı öneririz. LNbits örneğiniz yalnızca Tor ise, bu uygulamaları Tor etkinleştirilmiş olarak da kullanmanız gerekir. Ayrıca bu durumda LNbits sayfasını Tor .onion Address üzerinden açmanız gerekir.


On-Chain uzantısında bir ypub kullanırken "desteklenmeyen Hash türü" hatası alıyorsanız, LNbits örneğinizin python 3.10 kullanıp kullanmadığını kontrol edin, [bu sorundan] etkilenmiş olabilir (https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Stackoverflow yanıtında açıklandığı gibi openssl.cnf dosyasını düzenleyin ve LNbits'inizi yeniden başlatın.



## LNbits ile Takım Oluşturma ve İnşa Etme


LNbits her türlü [açık API] (https://legend.lnbits.com/docs) ve milyonlarca kullanım durumu için birçok farklı cihazı programlamak ve bunlara bağlanmak için araçlara sahiptir.


İnşa etmeye yeni başladığınızda, Ben Arc'ın LNbit'lere dayalı araçlar inşa etme hakkındaki bu [MakerBits sunumları] (https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) ile başlayın.


### ÖNEMLİ:


- LNbits, isteklerin iki şekilde geçerli olduğu LNURL protokolüne dayalı olarak çalışır: https:// clearnet bağlantısı (kendinden imzalı sertifikalara izin verilmez) veya http:// v2 / v3 onion bağlantısı olarak. LNURLp/w QR kodları veya NFC Kartları gibi vahşi ortamda kullanılabilecek LNbits hizmetleri sunmak için LNbits'i clearnet'e (https) açmanız gerekecektir.
- Esp32'nize güç sağlamak için yalnızca DATA-Kablolarını kullanın. Tüm kablolar esp'ye güç sağlamanın yanı sıra verileri de desteklemez. esp ile birlikte gelen kablo yalnızca güç sağlayan bir kabloysa ilk kişi siz olmazsınız
- Başka cihazların takılı olduğu bir USB-Hub kullanmadığınızdan emin olun. Bu, hata ayıklamak için Hard olan garip etkilere yol açabilir (örneğin başlamama veya durma).
- MacOS ile esp projelerini gerçekleştirmek için bir UART Köprü Sürücüsüne ihtiyacınız olacaktır. Mac veya Linux sistemlerinde sürücüyle ilgili sorun yaşarsanız, bunları burada veya bir TTGO Ekranı söz konusuysa bunu bulabilirsiniz. Windows kullanıyorsanız ve bağlanmakta sorun yaşıyorsanız ESKİ 11.1.0 sürümünü indirdiğinizden emin olun çünkü yenisi çalışmıyor! Bağlantınızı kontrol etmek için burada bir seri terminal de bulabilirsiniz - baudrate 115200'e ayarlayın.
- Platform.io'yu kullanmak çok daha rahat olsa da (örneğin, bağımlılıklar otomatik olarak yüklenir), inşa etmeye yeni başlayan herkes için Arduino'yu kullanmanızı öneririz.
- TT-Go Ekran S3: Ekran koruyucu filmin sekmesinin rengi, onu oluşturmak için tam olarak hangi denetleyicinin (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) kullanıldığını gösterir. Kendinizi programladığınızda ve ekran grafikleri doğru göstermediğinde, örneğin renkler yanlış, yansıtılmış görüntüler veya kenarlarda başıboş pikseller gibi, hata ayıklayabilmek için saklayın. Eğer bunu yapmanız gerekirse, farklı ekranlar için ayarlama konusunda epik bir rehber var
- LNURLl239xx yerine her zaman küçük harf lnurl239xx kullanın
- Lightning:lnurl1234xyz eklenmesi, taramada bu Invoice için Wallet kullanıcılarını açmayı talep eden bir QR oluşturacaktır (iOS'ta son yüklenen lightning uygulaması, Android'de ayar)
- Bir esp32'yi web üzerinden yanıp sönüyorsanız yalnızca bu tarayıcılarla çalışacaktır (TL:DR Chrome, Edge ve Opera).
- Lütfen esp için bu PIN-OUT referansına dikkat edin
- FOSSoftware veya FOSGuides kullandığınızda lütfen her zaman yazarla bağlantı kurun. Herkes bebeğinin büyümesini izlemeyi sever ve bu aynı zamanda izlemesi oldukça harika olan bir yapı zincirini başlatır:)


Bir projede yardıma ihtiyacınız varsa [Makerbits Telegram Group]'a (https://t.me/makerbits) gelin - sizi bulduk!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


İşte LNbits ile oluşturabileceğiniz bazı proje kategorileri:



- [Nostr İmzalama Cihazı](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lambası](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Otomat](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora ve Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [YARDIMCILAR & KAYNAKLAR](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- ["Powered by LNbits" projelerine daha fazla örnek için] (https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [LNbits için kullanım durumları](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)