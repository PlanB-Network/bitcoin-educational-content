---
name: Ride The Lightning (RTL)
description: Yıldırım düğümünüzü yönetmek için Ride The Lightning (RTL) kullanın
---
![cover](assets/cover.webp)


## 1. Giriş



**Ride The Lightning (RTL)** bir Lightning Network düğümünü yönetmek için eksiksiz bir Interface web uygulamasıdır. Kendi kendine barındırılan bu web uygulaması, tarayıcınızdan erişilebilen bir Lightning** "kokpiti" sunar. RTL, tüm büyük Lightning uygulamalarıyla (LND, Core Lightning/CLN ve Eclair) çalışır ve size düğümünüz ve kanallarınız üzerinde tam kontrol sağlar. Açık kaynaklı (MIT lisansı) ve ücretsiz olan RTL, birçok anahtar teslim node çözümüne (RaspiBlitz, MyNode, Umbrel, vb.) varsayılan olarak entegre edilmiştir.



**Grafiksel bir Interface olmadan, Lightning düğümleri yalnızca kullanıcı dostu CLI komutları ile yönetilebilir. RTL bu işlemleri ergonomik bir Interface ile basitleştirir. İşte **ana uygulamalar**:





- Kanallarınızı ve düğümünüzü görüntüleyin** - Kontrol panelinde On-Chain bakiyesi, Lightning likiditesi (yerel/uzaktan), senkronizasyon durumu, düğüm takma adı ve daha fazlası görüntülenir. Kanal listenizi, kapasitenizi, yerel/uzaktan dağıtımınızı ve durumunuzu görüntüleyebilirsiniz. RTL, etkinliği farklı açılardan analiz etmek için içeriğe duyarlı gösterge tabloları sunar.





- Lightning kanal yönetimi** - Birkaç tıklama ile kanalları açın/kapatın. RTL, bir eşe bağlanmanızı ve komut vermeden bir kanal açmanızı sağlar. Yönlendirme ücretlerini ayarlayabilir, bakiye puanını görüntüleyebilir veya kanallar arasında fonları yeniden dengelemek için döngüsel bir yeniden dengeleme başlatabilirsiniz.





- Ödemeleri takip edin ve yapın** - RTL, Lightning işlemlerini yönetir: ödemeleri faturalar aracılığıyla gönderin, generate faturaları alın, işlemleri (ödemeler, yönlendirme) ayrıntılı geçmişle takip edin. Interface ayrıca hangi ödemelerin düğümünüzden geçtiğini görmek için yönlendirmeyi analiz eder.





- Wallet On-Chain yönetimi ve yedekleme** - On-Chain sekmesi generate adreslerini ve gönderme işlemlerini yapmanızı sağlar. RTL, her kanal değişikliği için otomatik güncelleme ile LND için SCB dosyasını dışa aktararak kanalları kaydetmeyi kolaylaştırır.



Kısacası, RTL, Lightning Network** için **güçlü bir gösterge tablosudur ve düğümünüzü günlük olarak pilot olarak kullanmak için eğitici bir Interface sunar. Bu eğitim, kanallarınızı ve ödemelerinizi yönetmek için kurulumu ve kullanımı konusunda size rehberlik edecektir.



## 2. RTL'nin teknik işleyişi



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



İşin özüne inmeden önce, teknik düzeyde **RTL'nin Lightning düğümünüzle nasıl etkileşime girdiğini** kısaca anlamak faydalı olacaktır.



**Genel mimari:** RTL, Node.js (arka uç) ve Angular (ön uç) ile oluşturulmuş bir web uygulamasıdır. Somut olarak, RTL, Lightning uygulamanızla API'leri aracılığıyla diyalog kuran küçük bir yerel web sunucusu (varsayılan olarak 3000 numaralı bağlantı noktasında) olarak çalışır. Türüne bağlı olarak :





- LND** ile RTL, Lightning komutlarını yürütmek için LND'ün REST API'sini (port 8080) kullanır. Bağlantı TLS ile güvence altına alınmıştır ve kimlik doğrulama için LND'ün **admin macaroon** dosyasını gerektirir.





- Çekirdek Lightning (CLN)** ile RTL, *c-lightning-REST* tarafından sağlanan REST API'sini ya da `commando` eklentisi aracılığıyla bir **erişim rune** kullanır. Umbrel gibi çözümler bu Elements'i otomatik olarak yapılandırır.





- Eclair** ile RTL, yapılandırılmış kimlik doğrulama parolasını kullanarak Eclair REST API'sine bağlanır.



**Yapılandırma ve güvenlik:** RTL, web bağlantı noktasını, erişim şifresini ve düğümünüze bağlantı bilgilerini tanımladığınız bir JSON dosyası (`RTL-Config.json`) aracılığıyla yapılandırılır. Interface web bir giriş/parola ile korunur (varsayılan `parola` değiştirilebilir) ve 2FA`yı destekler. Varsayılan olarak, RTL yerel HTTP (`http://localhost:3000`) olarak çalışır, ancak uzaktan erişim için her zaman güvenli bir bağlantı kullanın (ters proxy, Tor veya VPN aracılığıyla HTTPS).



Kısacası RTL, düğümünüze güvenli API'ler aracılığıyla bağlanan, uygun erişim belirteçleri gerektiren ve kendi güvenlik Layer'sini sunan ek bir bileşendir. Bu modüler mimari, **birden fazla Lightning düğümünü tek bir RTL örneği** ile yönetmenize bile olanak tanır.



## 3. RTL kurulumu



RTL açık kaynaklı bir yazılım olarak dağıtıldığından, sisteminize kurmanın birkaç yolu vardır. Bu bölümde, iki ana yaklaşımı ele alacağız: manuel kurulum ve Umbrel aracılığıyla kurulum.



### Manuel yöntem



Eğer kontrolü elinizde tutmak istiyorsanız ya da RTL'yi özel bir yapılandırmaya entegre ediyorsanız manuel kurulum uygundur. Aşağıdaki adımlar Linux çalıştıran bir LND düğümü içindir (örneğin Raspberry Pi veya Ubuntu/Debian çalıştıran VPS), ancak CLN/Eclair için de benzerdir.



**Önkoşul:** makinede **senkronize edilmiş** bir Bitcoin düğümü ve çalışan bir Lightning düğümü (LND, CLN veya Eclair) olduğundan emin olun. RTL kendi başına bir Lightning düğümü içermez, mevcut bir düğüme bağlanır. Ayrıca **Node.js** yüklü olmalıdır (sürüm 14+ önerilir). Node'u `node -v` ile kontrol edebilir veya resmi sitesinden (https://nodejs.org/en/download/) veya paket yöneticinizden yükleyebilirsiniz.



Ana kurulum aşamaları şunlardır:



**RTL kodunu indirin**: Resmi RTL GitHub deposunu seçtiğiniz dizinde klonlayın. Örneğin:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Bağımlılıkları yükleyin**: RTL bir Node.js uygulamasıdır, bu nedenle gerekli modüllerini yüklemeniz gerekir. RTL klasöründe, :



```bash
npm install --omit=dev --legacy-peer-deps
```



Bu komut gerekli NPM paketlerini yükler (geliştirme bağımlılıklarını göz ardı ederek). Olası Node bağımlılık çakışmalarını önlemek için `--legacy-peer-deps` seçeneği önerilir.



**RTL-Config**: Bağımlılıklar yerine oturduktan sonra yapılandırma dosyasını hazırlayın. Proje kökündeki `Sample-RTL-Config.json` dosyasını `RTL-Config.json` olarak kopyalayın/adını değiştirin. İçinde açın :





   - UI parolası**: güvenli bir parola seçin ve `multiPass` içine girin (varsayılan `"parola"` yerine).
   - Port**: varsayılan `3000`. Makinenizde bu bağlantı noktası zaten alınmışsa değiştirebilirsiniz.
   - Node**: `nodes[0]` bölümünde node'unuz için parametreleri ayarlayın:
     - `lnNode`: düğümünüz için açıklayıcı bir ad (örneğin `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (veya uygun şekilde `"CLN"`/`"ECL"`).
     - Kimlik doğrulama' altında:
       - macaroonPath`: LND'ün macaroon yöneticisini içeren klasörün tam yolunu belirtin.
       - `configPath`: düğümün yapılandırma dosyasının yolu (LND için `LND.conf`).
     - Ayarlar' altında:
       - fiatConversion`: fiat para birimi dönüşümü istiyorsanız `true` olarak ayarlayın.
       - unannouncedChannels`: duyurulmamış kanalları görmek için `true` olarak ayarlayın.
       - themeColor` ve `themeMode`: Interface özelleştirme.
       - channelBackupPath`: LND kanal yedekleri için yol.
       - `lnServerUrl`: Lightning düğümünüzün URL'si (örneğin `https://127.0.0.1:8080`).



**RTL sunucusunu başlatın**: RTL klasöründe, çalıştırın :



```bash
node rtl
```



Uygulama başlar ve `http://localhost:3000` adresinden erişilebilir.



**(İsteğe bağlı) RTL'yi bir hizmet olarak çalıştırın**: Otomatik başlatma için bir systemd :



Bunu yapmak için:




- Makinenizde bir terminal açın.
- Aşağıdaki komutla yeni bir servis dosyası oluşturun (`nano` yerine favori editörünüzü kullanın):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Aşağıdaki içeriği kopyalayıp bu dosyaya yapıştırın:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Path/to/RTL/rtl` yerine makinenizdeki `rtl` dosyasının gerçek yolunu, `<your_user>` yerine de Linux kullanıcı adınızı yazın.
- Dosyayı kaydedin ve kapatın.
- Systemd yapılandırmasını yeniden yükleyin:


```bash
sudo systemctl daemon-reload
```




- RTL hizmetini etkinleştirin ve başlatın:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL artık makine her yeniden başlatıldığında otomatik olarak başlayacaktır. Durumunu şu şekilde kontrol edebilirsiniz: :


```bash
sudo systemctl status RTL
```



### Umbrel aracılığıyla kurulum



Umbrel](https://getumbrel.com) kullanıyorsanız, RTL kurulumu çok daha basittir:





- Interface Umbrel'e erişim (genellikle `http://umbrel.local` üzerinden)
- Uygulama Mağazasına** gidin
- "Ride The Lightning" için arama yapın



**Önemli not: Umbrel App Store'da iki ayrı RTL uygulaması bulunmaktadır:**




- Ride The Lightning** (LND için): Umbrel'in varsayılan Lightning düğümü (LND) ile kullanım içindir.
- Ride The Lightning (Core Lightning)**: yalnızca Umbrel'e *Core Lightning* uygulamasını yüklediyseniz ve bu düğümü RTL ile yönetmek istiyorsanız kullanın.



*Her RTL sürümü, ilgili uygulama (LND veya Core Lightning) ile diyalog kuracak şekilde önceden yapılandırılmıştır. Lightning düğümünüzü değiştirmediyseniz, klasik LND sürümünü seçmeniz yeterlidir*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Yükle** üzerine tıklayın



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Önemli:** Kurulumdan sonra, RTL varsayılan şifreyi içeren bir ekran görüntüler. **Bu şifreyi kopyalayın ve kaydedin** - Interface RTL'de oturum açmak için bu şifreye ihtiyacınız olacak. Bu şifre, siz "Bir daha gösterme" seçeneğini işaretleyene kadar RTL her başlatıldığında görüntülenecektir.



Umbrel otomatik olarak ilgilenir :




- RTL'yi indirin ve yapılandırın
- Lightning düğümüne erişimi yapılandırma
- Güncellemeleri yönetin
- Interface'e erişimin güvence altına alınması



Uygulama yüklendikten sonra Umbrel'deki *Uygulamalar* menünüzde görünür. Başlatmak için **Ride The Lightning** üzerine tıklayın.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Giriş ekranında, daha önce kopyaladığınız şifreyi girin. Giriş yaptıktan sonra, Interface web RTL'ye doğrudan Umbrel kontrol panelinden erişilebilecek ve ek yapılandırma gerekmeyecektir!



## 4. Interface RTL'nin tanıtımı ve kullanımı



RTL hazır ve çalışır durumda olduğuna göre, şimdi Interface web'ini ve temel özelliklerini keşfedelim. Size eksiksiz bir genel bakış sunmak için uygulamanın farklı bölümlerinden geçeceğiz.



### Ana kontrol paneli



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Oturum açar açmaz, Lightning düğümünüze genel bir bakış sağlayan **ana kontrol paneline** erişirsiniz. Bu sayfa temel bilgileri merkezileştirir:




- Toplam Lightning bakiyeniz
- On-Chain bakiyesi mevcut
- Likiditenizin dağılımı (gelen/giden)
- Lightning düğümünüz aracılığıyla Satss göndermek ve almak için hızlı erişim



### Fon yönetimi On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



On-Chain** sekmesi, bitcoinlerinizi doğrudan ana zincir üzerinde yönetmenizi sağlar:




- Farklı birimlerde bakiye gösterimi (Sats, BTC, USD)
- İşlemlerin tam listesi
- Address nesil Taproot (P2TR), P2SH (NP2WKH) veya Bech32 (P2WKH)
- UTXO yönetimi, bitcoin alma ve gönderme



### Lightning: alt menülerin ayrıntılı sunumu



Interface RTL, Lightning Network'e adanmış bir yan menüye sahiptir ve düğümünüzü yönetmek için tüm temel işlevleri bir araya getirir. İşte ekran görüntüsündeki sırayla her bir alt menünün ayrıntıları:



#### 1. Eşler/Kanallar



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Bu alt menü aşağıdakileri yapmanızı sağlar:




- Bağlı eşlerinizin ve açık veya bekleyen Lightning kanallarının listesini görüntüleyin.
- Yeni bir eş ekleyin (başka bir Lightning düğümüne bağlanın).
- Mevcut kanalları açın, kapatın veya yönetin.
- Her kanalın ayrıntılarını görüntüleyin: kapasite, yerel/uzak bakiyeler, durum, işlem geçmişi, bakiye puanı, vb.



#### 2. İşlemler



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Bu alt menüde şunları yapabilirsiniz :




- Lightning ödemelerini gönderin (Invoice aracılığıyla).
- generate ve ödemeleri almak için faturaları yönetin.
- Gönderilen ve alınan ödemelerin tüm geçmişini ayrıntılarıyla birlikte görüntüleyin (tutar, tarih, durum, ücretler, atlama sayısı vb.).



#### 3. Yönlendirme



Bu alt menü görüntülenir :




- Düğümünüz tarafından diğer Lightning Network kullanıcıları için yönlendirilen ödemeler.
- Yönlendirme istatistikleri: aktarılan işlem sayısı, kazanılan ücretler, karşılaşılan hatalar.
- Gelişmiş analiz için dışa aktarılabilir geçmiş.



#### 4. Ertelemeler



Bu alt menü şunları sunar :




- Lightning düğümünüzün etkinliği hakkında ayrıntılı raporlar.
- Kanallar, ödemeler, ücretler, kapasite vb. ile ilgili grafikler ve tablolar.
- Düğümünüzün performansını daha iyi anlamak için araçlar.



#### 5. Grafik Arama



Bu alt menü aşağıdakileri yapmanızı sağlar:




- Lightning Network'un topolojisini keşfedin.
- Belirli düğümleri veya kanalları arayın.
- Bağlantı ve genel ağ kapasitesi hakkında bilgi edinin.



#### 6. İmzalayın/Doğrulayın



Bu alt menü şunları sunar :




- Düğümünüzün anahtarı ile bir mesajı imzalama yeteneği (Ownership kanıtı).
- Diğer düğümlerden gelen mesajların kimliğini doğrulamak için imza doğrulama.



#### 7. Yedekleme



Bu alt menü yedeklemeye ayrılmıştır:




- Kanal yedekleme dosyasını dışa aktarın (LND için SCB).
- Gerekirse yapılandırmayı veya kanalları geri yükleyin.
- Yedeklerinizin güvenliğini sağlamak için ipuçları.



#### 8. Düğüm/Ağ



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Bu alt menüde şunları bulacaksınız :




- Lightning düğümünüzün durumunun tam bir özeti: takma ad, sürüm, renk, senkronizasyon durumu.
- Kanallarla ilgili istatistikler (aktif, bekleyen, kapalı), toplam kapasite, bağlanabilirlik.
- Küresel Lightning Network ve düğümünüzün içindeki konumu hakkında bilgi.



### Hizmetler Boltz Takasları



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz, bitcoinleri Lightning Network ve Blockchain Bitcoin (On-Chain) arasında dönüştüren gizlilik dostu, gözetim dışı bir Exchange hizmetidir. İki tür işlem sunmaktadır: Ters Denizaltı Takası (**Swap Out**) ve Denizaltı Takası (**Swap In**).



#### Takas (Ters Denizaltı Takası)



Swap Out, Lightning Network'de bulunan Sat'ları On-Chain bitcoinlerine dönüştürür. Bu mekanizma, bir düğümün gelen kapasitesi tükendiğinde veya bir On-Chain Address'tan fonları kurtarmak istediğinizde kullanışlıdır. İşlem aşağıdaki gibi çalışır:




- Kullanıcı değiştirilecek bir miktar seçer
- Düğüm Boltz'a bir Lightning ödemesi gönderir
- Exchange'de Boltz, On-Chain bitcoinlerinde eşdeğer bir miktarı bloke eder
- İşlem onaylandıktan sonra, kullanıcı takasta kullanılan bir sırrı ifşa ederek fonları talep edebilir



Bu süreç gözetim altında değildir ve Boltz kullanıcının fonlarını asla elinde tutmaz.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Denizaltı Takası)



Diğer yandan Takas Girişi, On-Chain fonlarının Lightning Network'e yeniden enjekte edilmesini sağlar. Bu özellikle kanallarınızdaki çıkış kapasitesini geri kazanmak için kullanışlıdır. Prosedür aşağıdaki gibidir:




- Kullanıcı, Boltz tarafından oluşturulan belirli bir Address'e bitcoin gönderir
- Bu fonlar Boltz tarafından ancak kullanıcının düğümü tarafından üretilen Lightning Invoice'yı ödediği takdirde serbest bırakılabilir
- Invoice ödendikten sonra, fonlar Yıldırım kanalında kullanılabilir hale gelir ve düğümün çıkış kapasitesini artırır



![Configuration d'un swap-in](assets/fr/12.webp)



Bu iki mekanizma, Lightning kanalı likiditesinin verimli bir şekilde yönetilmesini sağlarken, kullanıcının fonları üzerindeki egemenliğini de korur.



### Yapılandırma ve özelleştirme



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Düğüm Yapılandırması** sekmesi deneyiminizi özelleştirmenizi sağlar:




- Haber verilmeyen kanalların etkinleştirilmesi
- Satış ekranını özelleştirin
- Block explorer yapılandırması
- Interface'un Ayarlanması



### Dokümantasyon ve yardım



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Son olarak, **Yardım** bölümü, :




- İlk yapılandırma
- Eş ve kanal yönetimi
- Ödemeler ve işlemler
- Yedeklemeler ve geri yüklemeler
- Raporlar ve istatistikler
- İmzalar ve doğrulamalar
- Düğüm ve uygulama parametreleri



Bu kapsamlı Interface, temel işlemlerden gelişmiş özelliklere kadar Lightning düğümünüzü sezgisel, iyi organize edilmiş bir Interface ile verimli bir şekilde yönetmenizi sağlar.



## 5. Gelişmiş kullanım durumları ve güvenlik



Bu bölümde, RTL ile daha ileri gitmek ve Lightning düğümünüzün güvenliğini sağlamak için bilmeniz gerekenler yer almaktadır:



### İzleme ve sorun giderme



Düğümünüzü izlemek için RTL verilerini (günlükler, CSV) dışa aktarabilir ve bunları Grafana gibi araçlarda görüntüleyebilirsiniz. Bir sorun olması durumunda (engellenmiş ödeme, etkin olmayan kanal), LND/CLN günlüklerine bakın ve tanılama komutlarını kullanın (`lncli listchannels`, `lncli pendingchannels`, vb.). RTL ayrıca yönlendirme olaylarını izlemek için Interface günlükleri sunar.



### Güvenli uzaktan erişim



RTL'yi asla doğrudan internette ifşa etmeyin. Şunları tercih edin :




- Özel, şifreli erişim için VPN** (örn. Tailscale)
- Güvenli, anonim erişim için Tor**
- Ters proxy HTTPS** (Nginx/Caddy) yalnızca nasıl yapılandırılacağını biliyorsanız



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### İyi güvenlik uygulamaları





- Erişiminizi koruyun**: admin.macaroon veya RTL şifrenizi asla paylaşmayın. Hassas dosyalar üzerindeki izinleri sınırlayın.
- Düzenli yedeklemeler**: her değişiklikten sonra kanal yedekleme dosyasını (SCB) dışa aktarın ve düğümün dışında saklayın.
- Güncellemeler**: RTL'yi, düğümünüzü ve Umbrel'i en son güvenlik düzeltmeleriyle güncel tutun.
- Gizlilik**: günlükleri ve ekran görüntülerini paylaşmadan önce anonimleştirin. Bakiyelerinizi veya eş listelerinizi asla herkese açık olarak paylaşmayın.
- Tek erişim**: RTL çok kullanıcılı değildir. Yönetici erişimini paylaşmayın. Salt okunur erişim için gerekirse özel bir makaron kullanın.



Bu ilkeleri uygulayarak riskleri büyük ölçüde sınırlandırabilir ve Lightning düğümünüz üzerindeki kontrolü elinizde tutabilirsiniz.



## 7. Sonuç



**Ride The Lightning**, ister yeni başlayan ister ileri düzey bir kullanıcı olun, bir Bitcoin/Lightning düğümünü etkili bir şekilde yönetmek için gerekli bir araçtır. Lightning Network anlayışınızı derinleştirirken kanallarınızı, ödemelerinizi ve düğüm sağlığınızı kontrol etmek için net bir Interface sağlar.



RTL, çoklu uygulama uyumluluğu, gelişmiş işlevleri (yeniden dengeleme, takaslar, raporlar) ve pedagojik yaklaşımı ile öne çıkmaktadır. Basit ihtiyaçlar için Interface Umbrel veya bir Wallet mobil yeterli olacaktır, ancak RTL aktif, optimize edilmiş düğüm yönetimi için mükemmel bir anlam ifade eder.



Daha fazlasını öğrenmek için :




- Resmi RTL web sitesi: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Teknik tartışmalar, proje duyuruları, geri bildirim ve eğitim kaynakları
- Umbrel Topluluk Forumu**: [community.getumbrel.com](https://community.getumbrel.com) - Özel Bitcoin/Lightning bölümü, kılavuzlar ve yaygın sorunlara çözümler içeren resmi forum
- Lightning Network Geliştiricileri**: [github.com/lightning](https://github.com/lightning) - Geliştirmeyi takip etmek ve kaynak koduna katkıda bulunmak için resmi GitHub deposu
- Stack Exchange Bitcoin** : [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Geliştiriciler ve ileri düzey kullanıcılar ile Teknik Soru-Cevap



Kısacası, RTL size modern, tam özellikli bir Interface'de Lightning düğümünüz üzerinde tam kontrol sağlar.



**Kaynaklar :** RTL resmi web sitesi; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network kaynakları.



Lightning Network'ün nasıl çalıştığına dair anlayışınızı derinleştirmek için bu ücretsiz kursa katılmanızı da tavsiye ederim:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb