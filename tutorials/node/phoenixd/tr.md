---
name: Phoenixd
description: Phoenixd ile kendi minimalist Lightning düğümünüzü dağıtın
---

![cover](assets/cover.webp)



Finansal özerklik aynı zamanda Lightning altyapınızı kontrol etmek anlamına gelir. Bitcoin Lightning'i uygulamalarına entegre etmek isteyen geliştiriciler ve şirketler için **Phoenixd** ideal çözümü temsil ediyor: otomatik likidite yönetimine sahip minimalist, özel bir Lightning düğümü.



Phoenixd, ACINQ tarafından geliştirilen ve özellikle bir HTTP API aracılığıyla Lightning ödemeleri göndermek ve almak için tasarlanmış bir Lightning sunucusudur. LND veya Core Lightning gibi tam özellikli uygulamaların aksine Phoenixd, fonlarınızın kendi kendini korumasını korurken kanal yönetiminin tüm karmaşıklığını soyutlar.



Bu eğitimde, kendi kendine barındırılan bir altyapı ve kullanımı kolay bir API ile Lightning uygulamaları geliştirmek için Phoenixd'nin nasıl kurulacağına, yapılandırılacağına ve kullanılacağına bakacağız.



## Phoenixd nedir?



Phoenixd, ACINQ tarafından geliştirilen minimal, özel bir Lightning düğümüdür. Bir Full node'nin yönetim karmaşıklığı olmadan Lightning'i uygulamalarına entegre etmek isteyen geliştiriciler ve işletmeler için tasarlanmış bir çözümdür.



### Çalışma prensibi



**Phoenixd, otomatik likidite için LSP (Lightning Service Provider) olarak ACINQ kullanan minimal bir Lightning düğümüdür. Lightning ödemeleri aldığınızda, gerekli gelen kapasiteyi tahsis etmek için ACINQ düğümleriyle otomatik olarak kanallar açar. Bu "anında" likidite anlıktır, ancak alınan miktarın tam olarak **%1 + Mining ücretleri** üzerinden ücretlendirilir.



**Otomatik yönetim:** Sistem üç anahtar Elements'ü yönetir:




- Lightning** kanalları: Gerektiğinde otomatik olarak açın, kapatın ve yönetin
- Gelen/giden likidite**: Ekleme ve kanal açma yoluyla otomatik provizyon
- Ücret kredisi** : Bir kanalı haklı çıkarmak için yeterli olmayan küçük ödemeler, gelecekteki ücretler için bir karşılık olarak saklanır



### Phoenixd avantajları



**Özel anahtarlarınızı (12 kelimelik seed) ve fonlarınızı kontrol edersiniz. Phoenixd, anahtarlarınızı hiç paylaşmadan Wallet'inizi yerel olarak üretir.



**Kişisel altyapı:** Phoenixd sunucunuzda çalışır ve size ayrıntılı günlüklere, yapılandırmaya ve API kontrolüne erişim sağlar. Artık fonlarınıza erişim için üçüncü taraf bir hizmete bağımlı değilsiniz.



**Entegre API:** Phoenixd, diğer hizmetlerle entegrasyon, yerel LNURL desteği ve özel uygulama geliştirme için bir HTTP API'sine sahiptir.



**Entegrasyon kolaylığı:** Basit REST API'si sayesinde Phoenixd, Lightning ödemeleri gerektiren herhangi bir uygulama veya hizmete entegre edilebilir.



**Önemli not:** Otomatik likidite hala LSP (Lightning Service Provider) olarak ACINQ'dan geliyor. Phoenixd, otomatik kanal yönetimi için Phoenix mobile ile aynı mekanizmayı kullanır.



## Phoenixd'nin Kurulumu



### Ön Koşullar



Phoenixd, bazı temel komut satırı becerilerine sahip bir Linux ortamı (Ubuntu / Debian önerilir) gerektirir. Optimum performans için, ihtiyacınız olacak :





- Linux sunucusu**: Sabit bağlantıya sahip VPS veya yerel makine
- OpenJDK 21** : Java çalışma zamanı ortamı
- Sabit İnternet bağlantısı**: Lightning Network ile senkronizasyon için
- Alan adı** (isteğe bağlı) : API'ye güvenli HTTPS erişimi için



### İndirme ve kurulum



**1. Phoenixd'yi indirin**



GitHub sürümleri] sayfasına gidin (https://github.com/ACINQ/phoenixd/releases) ve mimariniz için en son sürümü indirin:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. İlk çalıştırma



Başlatma için Phoenixd'yi başlatın:



```bash
./phoenixd
```



İlk açılışta, "Anlıyorum" yazarak iki önemli adımı onaylamanız istenecektir:



**Mesaj 1 - Yedekleme:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Bu 12 kelimeyi saklayın** - iyileşmenizin tek garantisi budur.



**Mesaj 2 - Otomatik likidite:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Her onay için `Anladım` yazın.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd ilk kez başlıyor: yedekleme onayları ve otomatik likidite*



**3. Hizmet içi yapılandırma** (yalnızca Fransızca)



Sürekli çalışma için bir systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Phoenixd hizmeti systemd ve `auto-liquidity` aracılığıyla 2m sat*'da aktif ve çalışır durumda



## Yapılandırma ve güvenlik



### Yapılandırma dosyası



Phoenixd otomatik olarak temel parametreleri içeren `~/.phoenix/phoenix.conf` dosyasını oluşturur:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Anahtar parametreler:**




- `otomatik likidite`: Otomatik olarak açılan kanalların boyutu (varsayılan: 2M Sats)
- http-password`: API için yönetici şifresi (Invoice oluşturma VE ödeme gönderimi)
- http-password-limited-access`: Kısıtlı parola (yalnızca Invoice oluşturma)



### HTTPS ile güvenli erişim



Varsayılan olarak, Phoenixd API'sine yalnızca yerel HTTP (`http://127.0.0.1:9740`) üzerinden erişilebilir. Düğümünüzü dışarıdan kullanmak için (mobil uygulamalar, diğer sunucular, web entegrasyonları), güvenli HTTPS erişimini yapılandırmanız gerekir.



**Ters vekalet ilkesi:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** bir **ters proxy** görevi görür: 443 numaralı bağlantı noktasından İnternet'ten gelen HTTPS isteklerini dinler, bunları yerel olarak Phoenixd'ye (9740 numaralı bağlantı noktası) yönlendirir ve ardından şifrelenmiş yanıtları istemciye geri gönderir.



**SSL/TLS** sertifikası dijital bir dosyadır:




- Sunucunuzun kimliğini kanıtlayın** (ortadaki adam saldırılarını önler)
- HTTPS** şifrelemesini etkinleştirir: API parolalarınız dahil tüm veriler aktarım sırasında şifrelenir
- Let's Encrypt tarafından certbot aracı aracılığıyla ücretsiz olarak verilir**



Bu yapılandırma şunları yapmanıza olanak tanır:




- İnternetten API'ye güvenli erişim**
- Taşıma sırasında API** parolalarınızı şifreleyin (açık metin olarak iletilmelerini önlemek için)
- Phoenixd**'yi HTTPS gerektiren harici uygulamalara entegre edin
- Finansal API'ler için güvenlik standartlarına** uygunluk



Bu HTTPS ters proxy'yi nginx ile yapılandırın :



**1. Nginx** yapılandırması



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL** sertifikası



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Fonksiyon testi



Phoenixd'nin düzgün çalışıp çalışmadığını kontrol edin:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Bu komutlar düğümün durumu ve bakiyesi hakkında JSON bilgisi döndürmelidir (başlangıçta boş).



![Commandes CLI](assets/fr/03.webp)



*Düğüm durumunu kontrol etmek için getinfo ve getbalance komutları*



## API Kullanımı



### İlk alım testi



**1. Bir Lightning** Invoice oluşturun



İlk Invoice'nizi oluşturmak için API'yi kullanın:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Otomatik likidite mekanizmasının anlaşılması



**Temel ilke:** Bir Lightning ödemesi aldığınızda, Phoenixd bazen onu alabilmek için yeni bir kanal açmak zorundadır. Bu kanalın açılması, alınan miktardan ** otomatik olarak düşülen ** bir ücrete mal olur.



**100.000 Sats ile somut örnek:**



![Premier test de réception](assets/fr/04.webp)



*İlk kabul testi: Sats 100 bin teslim alındı, likidite maliyetleri düşüldükten sonra Sats'ün nihai bakiyesi 75.561*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Ücret hesaplaması:**




- Hizmet bedeli**: kanal kapasitesinin %1'i (2.115.000 Sats) = 21.150 Sats
- Mining ücretleri**: ~3,289 Sats (On-Chain işlemi için)
- Toplam**: 24,439 Sats otomatik olarak düşülür



**CLI komutları ile doğrulama:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Ödeme gönderildikten sonra nihai bakiye: Yıldırım sevkiyatından sonra kalan 257 Sats*



**Küçük ödemeler için ücret kredisi:** Bir kanal açmayı haklı çıkaramayacak kadar küçük ödemeler alırsanız (< yaklaşık 25k Sats), bunlar iade edilmeyen bir "ücret kredisinde" saklanır. Bu kredi, yeterli miktarda ödeme aldığınızda gelecekteki kanal ücretlerini ödemek için kullanılacaktır.



**2. Kanal açıklığını takip edin**



Phoenixd kayıtlarını izleyin:



```bash
journalctl -u phoenixd -f
```



Kanalın açıldığını ve likidite ücretlerinin otomatik olarak kesildiğini göreceksiniz. Ücretler Mempool Bitcoin koşullarına göre değişir, ancak her zaman %1 hizmet ücreti artı mevcut Mining ücretini içerir.



**3. Kanalı kontrol edin**



```bash
./phoenix-cli listchannels
```



Bu komut aktif kanallarınızı durumları ve bakiyeleriyle birlikte görüntüler.



### API işlemlerini tamamlayın



Phoenixd, 9740 numaralı bağlantı noktasında bir REST API'si sunar:



**Temel işlemler:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Maliyetler konusunda önemli:**




- Makbuz**: otomatik likidite için %1 + Mining ücreti
- Nakliye**: 0.gW-27 için %4 yönlendirme ücreti



**Webhooks:** Webhooks, Phoenixd'in bir olay meydana geldiğinde (ödeme alındığında, Invoice ödendiğinde, kanal açıldığında vb.) Uygulamalarınızı ** otomatik olarak bildirmesini ** sağlar. Phoenixd'den sürekli güncellemeler istemek yerine, uygulamanız anında bir HTTP bildirimi alır.



**Online mağazanız, bir müşteri sipariş için ödeme yaptığında otomatik olarak bir bildirim alır ve işlemin anında doğrulanmasını sağlar.



Phoenix.conf` içinde yapılandırma:


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Gelişmiş uygulamalar



### LNURL entegrasyonları



Phoenixd, gelişmiş entegrasyon için LNURL protokollerini yerel olarak destekler:



**LNURL-Pay:** LNURL uyumlu hizmetler için ödeme yapın


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** LNURL hizmetlerinden fon alma


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Hizmetlere erişmek için Lightning üzerinden kimlik doğrulama


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### LNbits ile Entegrasyon



LNbits, [resmi belgelerine] (https://docs.lnbits.org/guide/wallets.html) göre Phoenixd'yi bir finansman kaynağı olarak kullanabilir:



**LNbits yapılandırması:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Bu entegrasyon, Phoenixd düğümünüz tarafından desteklenen LNbits alt hesapları oluşturmanıza olanak tanır ve birden fazla Lightning cüzdanını yönetmek için web tabanlı bir Interface sağlar.



### Özel uygulamalar



Kapsamlı REST API'si sayesinde, :



**E-ticaret:** Lightning ödemelerinin mağazanıza doğrudan entegrasyonu


**Bağış hizmetleri:** Faturalar ve otomatik web kancaları ile bağış sistemleri


**Sosyal ağ botları:** İpucu işlevlerine sahip Telegram/Discord botları


**Paywall Lightning:** Lightning ücreti karşılığında sunulan premium içerik



## Güvenlik ve en iyi uygulamalar



### Erişim koruması



**API parolaları:** Otomatik olarak oluşturulan parolalar Lightning hazinenizin anahtarlarıdır. Bunları asla paylaşmayın ve şüpheniz varsa değiştirin.



**Güvenlik Duvarı:** 9740 numaralı bağlantı noktasını asla doğrudan İnternet'e açık bırakmayın. Her zaman HTTPS ile nginx kullanın.



**Gelişmiş kimlik doğrulama:** Sunucunuza erişimi yalnızca yetkili cihazlarla kısıtlamak için bir VPN veya Tailscale düşünün.



### Temel yedeklemeler



**seed kurtarma:** 12 kelimenizi sunucu dışında güvenli bir yere kaydedin. Bu sizin tek kurtarma garantinizdir.



*~/.phoenix dizini:** Kanal durumunu korumak ve geri yüklemeyi hızlandırmak için bu klasörü düzenli olarak (Phoenixd kapatıldıktan sonra) yedekleyin.



**Hizmet kurtarma kodları:** Ayrıca Phoenix ile 2FA'yı etkinleştirdiğiniz tüm hizmetler için yedek kodları saklayın.



### İzleme ve bakım



**İzleme günlükleri:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Güncellemeler:** Yeni sürümler için [GitHub sürümlerini] (https://github.com/ACINQ/phoenixd/releases) izleyin. Güncelleme, ikiliyi değiştirmek ve hizmeti yeniden başlatmak kadar basittir.



## Alternatiflerle karşılaştırma



### Phoenixd vs Phoenix standardı



**Phoenix standardı (mobil) :**




- ✅ Anında kurulum, sıfır yapılandırma
- ✅ Interface mobil sezgisel
- ✅ Phoenixd ile aynı otomatik kaydetme
- ❌ Geliştiriciler için API yok
- ❌ Ayrıntılı günlüklere erişim yok



**Phoenixd (sunucu) :**




- ✅ Entegrasyonlar için HTTP API
- ✅ Günlüklere tam erişim
- ✅ Kişisel altyapı
- ❌ Teknik beceri gerektirir
- ❌ Sunucu bakımı gerekli



**Her ikisi de otomatik likidite için LSP olarak ACINQ kullanmaktadır.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Tam kontrol, tam Yıldırım protokolü
- ✅ Büyük topluluk, olgun ekosistem
- ❌ Karmaşık manuel likidite yönetimi
- ❌ Büyük öğrenme eğrisi



**Phoenixd :**




- ✅ Otomatik likidite yönetimi (Phoenix Mobile gibi)
- ✅ Geliştiriciler için API
- ✅ Basitleştirilmiş konfigürasyon
- aCINQ'yu LSP olarak kullanır (bağımsız yönlendirme yok)
- ❌ Tam düğümlerden daha az esnek



## Yaygın sorunların çözülmesi



### API erişim sorunları



**Kimlik doğrulama başarısız oldu" hatası:**


1. ~/.phoenix/phoenix.conf` dosyasındaki parolayı kontrol edin


2. Kimlik doğrulama biçimini kontrol edin `-u:password`


3. Phoenixd'nin çalıştığından emin olun (`./phoenix-CLI getinfo`)



**Bağlantı zaman aşımları:**




- Phoenixd'nin doğru bağlantı noktasını (9740) dinlediğini kontrol edin
- HTTPS'yi yapılandırmadan önce yerel erişimi test edin
- Günlükleri kontrol edin: `journalctl -u phoenixd -f`



### Likidite sorunları



**Ödemeler gelmiyor :**


1. Miktarın minimum eşiği aşıp aşmadığını kontrol edin (~30k Sats)


2. Kanal hatalarını belirlemek için günlüklere başvurun


3. Gerekirse Phoenixd'yi yeniden başlatın



**"Gider kredisi" bakiyesi:**


Küçük ödemeler karşılık olarak saklanır. Kanal açılışını tetiklemek ve bu fonları serbest bırakmak için daha büyük bir miktar alın.



## Sonuç



Phoenixd, geliştiriciler için kullanım kolaylığı ve teknik egemenlik arasında mükemmel bir uzlaşmayı temsil eder. Geleneksel Lightning düğümlerinin karmaşıklığını ortadan kaldırarak otomatik likidite yönetimi ile basit ama güçlü bir Lightning API sunar.



Bu çözüm özellikle geliştiriciler ve şirketler için çok uygundur:




- Bitcoin Lightning'i uygulamalarınıza entegre edin
- Lightning kanal yönetiminin karmaşıklığından kaçının
- Kendi kendine barındırılan bir altyapıdan yararlanın
- Basit, güvenilir bir API



Phoenixd ile, modern bir REST API ve teknik yönlerin otomatik yönetimi ile kendi özel Lightning altyapınızı oluşturursunuz. Projelerinizde Lightning entegrasyonunu demokratikleştirmek için ideal çözümdür.



## Yararlı kaynaklar



### Resmi belgeler




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Kaynak kodu ve sürümler
- Phoenix Sunucusu** sitesi: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Tam dokümantasyon
- SSS Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Sıkça sorulan sorular



### Toplum desteği




- GitHub Sorunları** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Teknik destek
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Haberler ve duyurular