---
name: Dojo
description: Gizlilik ve özerklik için açık kaynaklı bir Bitcoin düğümü
---

![cover](assets/cover.webp)



*Bu eğitim, devraldığım ve genişlettiğim [resmi Ashigaru belgelerine] (https://ashigaru.rs/docs/) dayanmaktadır. Anlaşılırlığı artırmak için tüm bölümleri yeniden yazdım, daha ayrıntılı açıklamalar ekledim ve yeni başlayanlar için kurulum ve kullanımı daha kolay anlaşılır hale getirmek için resimler ekledim.*



---

Dojo, bir Bitcoin düğümüne dayanan belirli gizlilik odaklı Bitcoin core cüzdanları için bir arka uç sunucusu olarak hareket etmek üzere tasarlanmış açık kaynaklı bir programdır. Tarihsel olarak, Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym gibi gelişmiş gizlilik özellikleri sunan mobil bir Wallet olan Samourai Wallet ile çalışmak üzere geliştirilmiştir. Samourai Wallet, geliştiricilerinin tutuklanmasının ardından kapatıldı, ancak topluluk halefi **Ashigaru Wallet** devraldı ve Bitcoin kullanırken verilerinin kontrolünü elinde tutmak isteyen kullanıcılar için eksiksiz bir deneyim sunmak için Dojo'ya güvenmeye devam ediyor.



![Image](assets/fr/01.webp)



Pratik anlamda Dojo, Wallet'niz ile Bitcoin ağı arasında bir ağ geçidi görevi görür. Dojo olmadan, hafif bir mobil Wallet, UTXO'larınızın durumunu ve geçmişinizi elde etmek veya işlemlerinizi yayınlamak için üçüncü taraf sunucuları sorgulamak zorunda kalacaktır. Bu, üçüncü taraf sunucuya bağımlılık ve hassas verilerin sızması anlamına gelir (kullanılan adresler, tutarlar, ödeme sıklığı vb.). Dojo ile bu sunucuyu doğrudan kendi Bitcoin düğümünüze bağlı olarak kendiniz barındırırsınız. Bu şekilde, tüm portföy talepleriniz aracısız olarak sizin kontrolünüzdeki bir altyapıdan geçerek gizliliğinizi ve egemenliğinizi güçlendirir.



## Bir Dojo kurmak için gerekenler



Bir Dojo sunucusu kurmak ultra güçlü bir makine gerektirmez. Giriş seviyesinde bir bilgisayarı, sabit bir İnternet bağlantısı ve sürekli (7/24) açık bırakma yeteneği olan herkes çalışan bir Dojo kurabilir.



### Makine tipinizi seçin



Kullanabilirsiniz :




- bir dizüstü bilgisayar;
- bir masaüstü bilgisayar ;
- bir mini bilgisayar (örneğin Intel NUC, Lenovo Thincentre Tiny...).



Her seçeneğin avantajları ve dezavantajları vardır:




- Fiyat: Yenilenmiş bir mini-PC veya masaüstü bilgisayar genellikle yeni bir dizüstü bilgisayardan daha ucuz olacaktır.
- Kapladığı alan: Mini-PC daha az yer kaplar.
- Güç Supply: Bir dizüstü bilgisayarın batarya avantajı vardır, bu da mini PC'nin aksine elektrik kesintisi durumunda kapanmayacağı anlamına gelir.
- Yükseltilebilirlik: barbonlar genellikle bellek eklemenize veya bir Hard diskini kolayca değiştirmenize olanak tanır.



Ekipman seçimi hakkında daha fazla bilgi için bu kursa katılmanızı tavsiye ederim:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Önerilen ekipman



Yeni bir makine almanıza gerek yok. Aşağıdaki özelliklere sahip yenilenmiş bir bilgisayar, tek kartlı elektroniklerden (Raspberry Pi gibi) çok daha iyi performans verecektir.



**Minimum özellikler:**




- X86-64 mimarisi (64 bit işlemci).
- 2 GHz veya daha hızlı çift çekirdekli işlemci.
- minimum 8 GB RAM.
- 2 TB veya daha fazla NVMe SSD (Bitcoin'in Blockchain'unu ve gerekli dizinleri depolamak için).



**Önerilen işletim sistemi: **




- Ubuntu 24.04 LTS gibi Debian tabanlı bir dağıtım.



**Tavsiye edilen ekipman:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- vs.



Bir Dojo sunucusunu diğer donanım yapılandırmalarında çalıştırmak tamamen mümkündür. Ancak, en iyi performansı elde etmek ve sorunları sınırlamak için yukarıdaki önerileri uygulamanızı tavsiye ederiz.



Bu eğitimde Intel Pentium Dual-Core G4400T işlemcili, 8 GB RAM'li ve 2 TB SSD'li eski bir ThinkCentre Tiny kullanacağım.



## 1 - Ubuntu'nun Kurulması



*Dojo'yu zaten yapılandırılmış bir cihaza kurmak istiyorsanız, bu adımı atlayabilir ve doğrudan 2.* adımına geçebilirsiniz



Seçilen donanımı hazırladıktan sonra sıra bir işletim sistemi kurmaya gelir. Neredeyse tüm Debian dağıtımlarını kullanabilirsiniz, ancak amaçlarımıza mükemmel bir şekilde uyduğu için Ubuntu'nun LTS sürümünü tercih etmenizi öneririm. İşte izlenecek adımlar:



### 1.1. önyüklenebilir bir USB anahtarı oluşturun



Halihazırda çalışan bir bilgisayardan (her zamanki makineniz), Ubuntu LTS ISO imajını [resmi siteden] (https://ubuntu.com/download/desktop) indirin (yazım sırasında `24.04`, ancak başka bir tane mevcutsa en yenisini alın).



![Image](assets/fr/02.webp)



Bu bilgisayara en az 8 GB'lık bir USB anahtarı takın, ardından [Balena Etcher] (https://etcher.balena.io/) gibi bir yazılım kullanarak önyüklenebilir bir anahtar oluşturun. İndirdiğiniz Ubuntu ISO imajını seçin, hedef aygıt olarak USB anahtarı seçin, ardından oluşturma işlemini başlatın (sabırlı olun, birkaç dakika sürebilir).



![Image](assets/fr/03.webp)



Önyüklenebilir USB anahtarını kapalı bilgisayara (Dojo'yu çalıştırmak istediğiniz bilgisayara) takın. Makineyi başlatın ve önyükleme menüsüne erişmek için hemen klavyenizdeki **F12** veya **F10** tuşlarına basın (modele bağlı olarak). Ardından bilgisayarın önyükleme sıralamasında öncelikli aygıt olarak USB anahtarınızı seçin.



![Image](assets/fr/04.webp)



### 1.2. işletim sistemini kurun



Ubuntu ana ekranı görünür. "Ubuntu'yu Dene veya Kur*" öğesini seçin.



![Image](assets/fr/05.webp)



Ardından klasik Ubuntu kurulum sürecini takip edin:




- Dil seçin.
- Klavye türünü seçin.
- RJ45 kablosuyla bağlıysanız Wi-Fi'yi yapılandırmanıza gerek yoktur.
- "*Ubuntu* Yükle" seçeneğine tıklayın ve üçüncü taraf yazılımları (Wi-Fi sürücüleri, multimedya kodekleri, vb.) yükleme seçeneğini işaretleyin.
- Sihirbaz kurulum türünü sorduğunda, "*Diski sil ve Ubuntu'yu kur*" seçeneğini seçin. **Uyarı**: bu işlem diskin içeriğini tamamen silecektir. Seçtiğiniz diskin Dojo için tasarlanan NVMe SSD'ye karşılık geldiğini dikkatlice kontrol edin.
- Basit bir kullanıcı adı oluşturun (örneğin "*loic*").
- Makineye bir ad atayın (örneğin "*dojo-node*").
- Güçlü bir parola belirleyin ve parolanızı güvende tutun.
- Güvenliği güçlendirmek için "*Giriş yapmak için şifremi iste*" seçeneğini etkinleştirin.
- Saat diliminizi belirtin ve ardından "*Yükle*" seçeneğine tıklayın.
- Kurulumun tamamlanmasını bekleyin. Tamamlandığında, sistem otomatik olarak yeniden başlayacaktır.
- Bilgisayarı yeniden başlatırken USB kurulum anahtarını çıkarın.



Ubuntu kurulum süreci hakkında daha fazla bilgi için lütfen özel eğitimimize bakın:



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. sistem güncellemesi



İlk açılıştan sonra, ***Ctrl + Alt + T*** tuş kombinasyonunu kullanarak bir terminal açın ve sistemi güncellemek için aşağıdaki komutları çalıştırın:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Ek bina kurulumu



Dojo'nun düzgün çalışması için sisteminizde belirli yazılım tuğlalarının bulunması gerekir. Bunlar yazılım depolarını yönetmek, iletişim, arşiv açma ve Dojo'nun Docker konteynerleri içinde çalıştırılması için kullanılır. Tüm bu işlemler terminalde gerçekleştirilir.



### 2.1. Hazırlık



Aşağıdaki komut sizi kişisel klasörünüze döndürür. Bu, bir dizi kurulumu çalıştırmadan önce iyi bir uygulamadır.



```bash
cd ~/
```



Herhangi bir yazılım yüklemeden önce, makinenizde bulunan yazılım veritabanının güncel olduğundan emin olun. Bu, eski sürümlerin yüklenmesini önler.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. yardımcı programları yükleyin



Sisteme çeşitli araçların eklenmesi gerekmektedir:




- `apt-transport-https`: HTTPS aracılığıyla paketleri güvenli bir şekilde indirmenize olanak tanır
- `ca-certificates`: şifrelenmiş bağlantılar için gerekli sertifikaları yönetir
- `curl`: İnternet'ten dosya almak için
- `gnupg-agent`: GPG anahtar yönetimi için
- software-properties-common`: APT depolarını manipüle etmek için yardımcı programlar sağlar
- `unzip`: ZIP biçimindeki dosyaları açar



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Kurulum sırasında sistem sizden onay isteyebilir. "*y*" tuşuna basın, ardından "*Enter*" tuşuna basın.



![Image](assets/fr/08.webp)



### 2.3. Torsocks'u yükleyin



Torsocks, belirli komutların Tor ağı üzerinden yürütülmesini sağlayarak iletişimin gizliliğini artırır.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Docker ve Docker Compose'u yükleyin



Dojo, Docker konteynerlerinin içinde çalışır. Bu, her hizmetin bağımsız bir ortamda izole edildiği, bakım ve güvenliği basitleştirdiği anlamına gelir. Bunu yapmak için Docker'ı ve aynı anda birkaç konteyneri yönetmenizi sağlayan Docker Compose aracını yüklemeniz gerekir.



#### Docker imzalama anahtarı ekleme



Docker kendi dijital imza anahtarını sağlar. Bunu eklemek, indirilen paketlerin gerçekliğini doğrular.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Resmi Docker deposu eklendi



Ardından, sisteme resmi Docker paketlerini nerede bulacağını söylemeniz gerekir. Bu komut, paket yöneticisi yapılandırmanıza yeni bir depo ekler.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Docker ve Docker Compose Kurulumu



Ana Docker bileşenleri artık kurulabilir.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Kullanıcı yetkilendirme



Varsayılan olarak, yalnızca yönetici haklarıyla çalıştırılan komutlar Docker'ı başlatabilir. Daha fazla kolaylık için, mevcut kullanıcınızı "*docker*" grubuna eklemenizi öneririm. Bu, Docker'ı her seferinde `sudo` yazmak zorunda kalmadan kullanmanızı sağlar.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Tek kullanıcı oluşturma (isteğe bağlı)



Sisteminizin güvenliğini artırmak istiyorsanız, yalnızca Dojo'yu çalıştırmak için ayrı bir kullanıcı oluşturmanızı öneririm. Bu ayrım riskleri sınırlar: Dojo'da bir güvenlik sorunu meydana gelirse, bu doğrudan ana hesabınızı tehlikeye atmaz.



### 3.1. kullanıcı hesabı oluşturma



Aşağıdaki komut "*dojo*" adında yeni bir kullanıcı oluşturur. Bu kullanıcı `/home/dojo` ev dizinine ve bash terminaline erişime sahip olacaktır. Ayrıca yönetici komutlarının yürütülmesini sağlamak için sudo grubuna eklenecektir.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Şifre belirleme



Bu hesaba güçlü bir parola atamak önemlidir. İdeal olarak, generate gibi uzun, Hard gibi tahmin edilmesi zor bir kombinasyon için Bitwarden gibi bir parola yöneticisi kullanmalısınız.



```bash
sudo passwd dojo
```



Sistem daha sonra sizden seçtiğiniz şifreyi girmenizi ve ardından ikinci kez onaylamanızı isteyecektir.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Kullanıcıyı Docker kullanmak için yetkilendirin



"*dojo*" kullanıcısının Dojo'yu çalıştırmak için gereken konteynerleri başlatmasını sağlamak için Docker grubuna eklenmesi gerekir. Bu, her komutun önüne `sudo` eklemek zorunda kalmayı önler.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Sistem yeniden başlatma



Grup değişikliklerinin etkili olabilmesi için makinenin yeniden başlatılması gerekir.



```bash
sudo reboot
```



### 3.5. Yeni kullanıcı ile giriş yapın



Sistem yeniden başlatıldığında, ***dojo*** kullanıcı adı ve daha önce tanımladığınız parola ile oturum açın. Sonraki tüm adımlar bu özel hesaptan gerçekleştirilmelidir.



## 4. Dojo'yu indirin ve kontrol edin



Dojo'yu yüklemeden önce, dosyaların resmi geliştiriciden geldiğinden ve değiştirilmediğinden emin olmak çok önemlidir. Bu adım, dosyanın gerçekliğini ve bütünlüğünü doğrulamak için PGP ve hash kullanımına dayanır.



### 4.1. geliştiricinin PGP anahtarını içe aktarın



Geliştiricinin genel anahtarını Tor üzerinden indirin ve yerel anahtar zincirinize aktarın. Bu anahtar, Dojo dosyalarıyla ilişkili imzaları doğrulamak için kullanılacaktır.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Dojo'nun en son sürümünü indirin



Dojo kaynak kodunu içeren sıkıştırılmış arşivi alın. Bu örnekte, en son sürüm `1.27.0`dır: komutu [resmi GitHub deposundaki en son sürüm]'e göre değiştirin (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Parmak izlerini ve imzayı indirin



Geliştiriciler, arşivlerin dijital parmak izlerini listeleyen bir dosyanın yanı sıra PGP anahtarları tarafından imzalanmış bir dosya yayınlarlar. Dosyalarınızı yerel olarak karşılaştırmak için bunları indirin.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. PGP imzasını kontrol edin



Parmak izi dosyasının içe aktarılan anahtar tarafından imzalanıp imzalanmadığını kontrol edin.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Doğru bir sonuç `E53AD419B242822F19E23C6D3033D463D6E544F6` anahtarı ve ilişkili Address `dojocoder@pm.me` ile geçerli bir imza görüntüler. Anahtarın sertifikalı olmadığını belirten bir uyarı görüntülenebilir: bunu görmezden gelebilirsiniz.



Öte yandan, imza geçersizse, yükleme işlemini derhal durdurun ve baştan başlayın.



![Image](assets/fr/17.webp)



### 4.5. Arşiv bütünlüğünü kontrol edin



İndirilen dosyanın SHA256 parmak izini hesaplayın, ardından iki değeri karşılaştırmak için parmak izi dosyasını açın.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



İki parmak izi aynıysa, arşivin değiştirilmediğinden emin olabilirsiniz. Eğer farklılarsa, daha fazla ilerlemeyin ve dosyaları silin.



![Image](assets/fr/18.webp)



### 4.6. Dosyaları ayıklayın ve düzenleyin



Doğrulama başarıyla tamamlandıktan sonra, arşivi açabilir ve Dojo kurulumu için ayrılmış bir klasör hazırlayabilirsiniz.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Gereksiz dosyaları temizleyin



Ortamınızı temiz tutmak için artık gerekli olmayan geçici dosyaları ve arşivleri silin.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojo yapılandırması



Dojo, portföyünüzle etkileşim kurmak ve Bitcoin düğümünüzü yönetmek için çeşitli hizmetleri bir araya getiren bir arka uç sunucusudur. Yapılandırması karmaşık olabilir, ancak proje aşağıdaki bileşenleri otomatik olarak yükleyen ve yapılandıran basitleştirilmiş bir yöntem sunar:




- Dojo (ana API)
- Bitcoin core (Bitcoin düğümünü tamamlayın)
- BTC-RPC Explorer (web Block explorer)
- Fulcrum Indexer (blokların ve işlemlerin hızlı indekslenmesi)
- Fulcrum Electrum Sunucusu Tor ağında kullanılabilir
- Yerel ağda bulunan Fulcrum Electrum Sunucusu
- Yönetim kimlik bilgileri



### 5.1. yönetim kimlik bilgileri



Çeşitli hizmetlere erişimi güvence altına almak için generate birkaç benzersiz tanımlayıcıya ihtiyacınız vardır:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Bu tanımlayıcılar ** benzersiz** olmalı (bu çok önemlidir: aynı şifreyi birden fazla hizmet için kullanmamalısınız), yalnızca rakamlardan, büyük harflerden ve küçük harflerden (alfanümerik) oluşmalı ve yüksek düzeyde güvenlik sağlamak için yaklaşık 40 karakter uzunluğunda olmalıdır. Bir kez daha, bir şifre yöneticisi kullanmanızı şiddetle tavsiye ederim.



### 5.2. Yapılandırma dosyalarına erişim



Dojo yapılandırma dosyaları `conf/` klasöründe bulunur. Bu dizine taşıyın:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core yapılandırması



Bitcoin core yapılandırma dosyasını nano metin düzenleyicisi ile açın:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Bu dosyada, oluşturulan tanımlayıcıları girin:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ *** `your-ID-here` ve `your-password-here` girişlerini kendi girişlerinizle (güçlü bir parola ile) değiştirin.***



Performansı artırmak için Bitcoin core tarafından kullanılan ön belleğin boyutunu da ayarlayabilirsiniz (çok fazla RAM'iniz varsa daha fazlasını bile kullanabilirsiniz):



```
BITCOIND_DB_CACHE=2048
```



Değişikliklerinizi kaydetmek ve düzenleyiciyi kapatmak için :




- ctrl + X tuşlarına basın
- type `y`
- ardından "*Enter*" tuşuna basın



### 5.4. MySQL yapılandırması



Ardından MySQL veritabanı yapılandırmasını açın:



```bash
nano docker-mysql.conf.tpl
```



Lütfen giriş bilgilerinizi girin:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***"your-ID-here" ve "your-password-here" yerine kendi oturum açma bilgilerinizi (güçlü, benzersiz parolalarla) girin.***



Aynı şekilde kaydedin (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Fulcrum indeksleyici yapılandırması



Aşağıdaki dosyayı açın:



```bash
nano docker-indexer.conf.tpl
```



Fulcrum'u etkinleştirmek ve Dojo'ya doğru şekilde entegre etmek için parametreleri ekleyin:



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Daha sonra, yapılandırmanıza bağlı olarak 2 olasılık vardır. Dojo günlük bilgisayarınızdan ayrı bir makineye kuruluysa (özel bir makinede, bir sunucuda...), yerel ağınızdaki IP Address'ünü girin, örneğin :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Makinenizin yerel IP Address'ini bulmak için başka bir terminal açın ve aşağıdaki komutu girin:



```bash
hostname -I
```



İkinci olasılık: Dojo doğrudan günlük kişisel bilgisayarınızda çalıştırılıyorsa, yapılandırma dosyasında zaten mevcut olan varsayılan değeri koruyun :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Kaydedin ve editörden çıkın (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Düğüm hizmeti yapılandırması



Son olarak, ana Dojo hizmetinin yapılandırmasını açın:



```bash
nano docker-node.conf.tpl
```



Lütfen giriş bilgilerinizi girin:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Buradaki `şifrenizi` kendi kimlik bilgilerinizle (güçlü, benzersiz şifrelerle) değiştirin.***



![Image](assets/fr/26.webp)



Ardından yerel dizinleyiciyi etkinleştirin:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Kaydedin ve editörden çıkın (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Giriş yönetimi



Yapılandırma tamamlandığında, oluşturulan tüm tanımlayıcıları kaydetmek gerekli değildir. Kesinlikle kaydedilmesi gereken tek tanımlayıcı :



```
NODE_ADMIN_KEY
```



Bu giriş, daha sonra Dojo bakım aracına giriş yapmanızı sağlayacaktır. Diğer tüm girişler parola yöneticinizden veya el yazısı notlarınızdan kaldırılabilir. Gelecekte onları geri almanız gerektiğinde Dojo yapılandırma dosyalarından erişilebilir kalırlar.



## 6. Dojo kurulumu



Bu aşamada Dojo makinenize kurulacak ve başlatılacaktır. İşlem birkaç hizmeti (Bitcoin core, Fulcrum indeksleyici, Dojo arka ucu, vb.) başlatacak ve Blockchain Bitcoin'in tam senkronizasyonunu başlatacaktır. Bu, donanımınıza ve İnternet bağlantınıza bağlı olarak birkaç gün sürebilir.



### 6.1. Docker'ın düzgün çalışıp çalışmadığını kontrol edin



Kuruluma başlamadan önce Docker'ın çalışır durumda olduğundan emin olun. Aşağıdaki komutu çalıştırın:



```bash
docker run hello-world
```



Bu komut küçük bir test konteynerini indirir ve başlatır. Her şey doğru çalışıyorsa, şuna benzer bir mesaj görmelisiniz :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Bu mesaj görüntülenmezse, makinenizi . ile yeniden başlatarak başlayın:



```bash
sudo reboot
```



Ardından **dojo** hesabınıza tekrar giriş yapın ve test komutunu tekrar çalıştırın. Hata devam ederse, Docker doğru şekilde kurulmamış demektir. Bu durumda, Docker kurulumu ile ilgili `2.4.` adımına geri dönün ve her komutu dikkatlice kontrol edin.



### 6.2. Dojo kurulum dizinine gidin



Kurulum için gerekli betikler `my-dojo` klasöründe bulunur. Bu dizine taşıyın:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Dojo.sh` dosyasının mevcut olup olmadığını kontrol etmek için `ls` komutunu kullanın. Bu, Dojo'nun kurulumunu ve tüm hizmetlerinin başlatılmasını otomatikleştiren ana betiktir.



![Image](assets/fr/29.webp)



### 6.3. Kurulumu başlatın



'yi çalıştırarak kurulumu başlatın:



```bash
./dojo.sh install
```



Yüklemeyi `y` ve ardından "*Enter*" tuşlarına basarak onaylayın.



![Image](assets/fr/30.webp)



Bu komut dosyası :




- gerekli Docker kapsayıcılarını indirin ve başlatın,
- gW-29'u başlatın ve Blockchain'u senkronize etmeye başlayın,
- işlemleri ve adresleri izlemek için Fulcrum indeksleyiciyi başlatın,
- dojo arka ucunu ve API'lerini etkinleştirin.



bitcoind`, `soroban`, `nodejs` veya `fulcrum` gibi renkli referanslarla sürekli bir günlük akışının kaydığını göreceksiniz. Bu kaydırma işlemi Dojo'nun çalıştığını ve çeşitli hizmetleri yürütmeye başladığını gösterir.



![Image](assets/fr/31.webp)



### 6.4. Günlük ekranından çık



Günlükler terminalinizde gerçek zamanlı olarak görünür. Dojo arka planda çalışırken komut istemine dönmek için :



```
Ctrl + C
```



Endişelenmeyin: günlük ekranını durdurmak hizmetleri durdurmaz. Docker arka planda Dojo'yu çalıştırmaya devam eder (IBD'nin devam etmesini istiyorsanız bilgisayarı durdurmanız gerekmez).



### 6.5. İlk Blok İndirmeyi* (IBD) Anlama



Başlangıçta, Bitcoin core 2009'dan bu yana tüm Blockchain'ü indirmeli ve doğrulamalıdır. Bu adım ***İlk Blok İndirme* (IBD)** olarak adlandırılır. Dojo düğümünüzün her bir Bitcoin bloğunu ve işlemini bağımsız olarak doğrulamasını sağladığı için çok önemlidir.



Bu senkronizasyonun süresi çeşitli faktörlere bağlıdır:




- işlemcinizin gücü ve mevcut RAM bellek miktarı,
- diskinizin hızı,
- düğümünüzün bağlandığı eşlerin sayısı ve kalitesi,
- i̇nternet bağlantınızın hızı.



Pratikte bu işlem genellikle **2 ila 7 gün** arasında sürer. Bu süre boyunca makinenizi sürekli çalışır durumda bırakabilirsiniz. Makine ne kadar uzun süre açık kalırsa, senkronizasyon o kadar hızlı tamamlanacaktır. Bitcoin core günlüklerine bakarak veya kurulduktan sonra Dojo bakım aracını kullanarak senkronizasyon durumunu düzenli olarak kontrol etmenizi tavsiye ederim (sonraki bölüme bakın).



IBD ve daha genel olarak Bitcoin düğümünüzün çalışması ve rolü hakkındaki bilgilerinizi derinleştirmek için bu kursa göz atmanızı tavsiye ederim:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Senkronizasyon izleme



Dojo'yu ilk kez kurarken, iki ana işlemin tamamen tamamlanmasını beklemeniz gerekir: Blockchain Bitcoin'in (*IBD*) tamamen indirilmesi ve bu Blockchain'nin Fulcrum tarafından indekslenmesi. Bağlantınıza ve makine gücüne bağlı olarak bu işlem birkaç gün sürebilir. Bu süre zarfında, her şeyin sorunsuz çalıştığından emin olmak için sürecin ilerleyişini izleyebilirsiniz.



Senkronizasyon durumunu izlemenin iki yolu vardır:




- iBD sırasında basit ancak çok az ayrıntı sağlayan Dojo Bakım Aracı (veya DMT) kullanımı;
- makinenizdeki Dojo günlüklerine doğrudan danışma, daha teknik ama çok daha kesin.



### 7.1. Dojo Bakım Aracı (DMT) ile kontrol edin



Dojo Bakım Aracı, tesisinizin durumunu izlemenizi ve belirli işlemleri gerçekleştirmenizi sağlayan güvenli, web tabanlı bir Interface'dur. IBD'nin ilerlemesini izlemenin en kolay ve en erişilebilir yoludur. İlk senkronizasyon aşamasında görüntülenen bilgiler sınırlı olabilir. Örneğin, DMT Fulcrum indekslemesinin ayrıntılı ilerlemesini göstermez. Öte yandan, senkronizasyon tamamlandığında, DMT açıkça gösterecektir :




- gW-40'taki tüm ışıklar;
- her hizmet (Node, Indexer, Dojo DB) için son doğrulanan blok.



Erişmek için, DMT'nizin URL'sini bilmeniz ve [Tor tarayıcısı aracılığıyla] ona bağlanmanız gerekir (https://www.torproject.org/download/). Bunu yapmak için bir terminal açın ve `/my-dojo` dizinine gidin:



```bash
cd ~/dojo-app/docker/my-dojo
```



Ardından aşağıdaki komutu çalıştırın:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Daha sonra Dojo'nuza Tor üzerinden yapılan bağlantılarla ilgili tüm bilgilere erişebileceksiniz. Burada ilgilendiğimiz bağlantı aşağıdaki URL'dir:



```
Dojo API and Maintenance Tool =
```



DMT'ye herhangi bir ağdaki herhangi bir makineden (uzaktan bile) erişmek için Tor Browser'ı açın ve bu URL'yi girin ve ardından `/admin` yazın. Örneğin, URL'niz `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion` ise, [Tor Browser] (https://www.torproject.org/download/) çubuğuna girmeniz gerekir:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Lütfen bu Address'i kesinlikle gizli tutun



Daha sonra bir kimlik doğrulama sayfasına yönlendirileceksiniz. DMT, daha önce oluşturduğunuz `NODE_ADMIN_KEY` şifresini kullanarak oturum açar.



![Image](assets/fr/33.webp)



Giriş yaptıktan sonra *Dojo Bakım Aracına* erişebilirsiniz! IBD sırasında, Bitcoin düğümünüzün mevcut durumunu bilmenizi sağlayan "*Full node*" menüsünde "*En Son Blok*" bilgisini görebilirsiniz.



![Image](assets/fr/34.webp)



Daha sonra kolayca erişebilmek için bu Address'ü Tor Browser'da yer imlerine eklemeyi unutmayın.



Dojo'nuz tamamen senkronize olduğunda, DMT ana sayfasındaki tüm göstergelerde Green onayını ✅ görmelisiniz.



### 7.2. Dojo günlükleri aracılığıyla doğrulama



IBD'nizin ilerleyişini izlemenin ikinci yolu, doğrudan makine günlüklerinize başvurmaktır. Bu yaklaşım çok daha hassas, gerçek zamanlı izleme sunar. Bitcoin core'nın blokları indirmede nasıl ilerlediğini ve Fulcrum'un bunları nasıl indekslediğini görebilirsiniz.



Dojo'nuzu barındıran makineye bağlanın ve bir terminal açın. Tüm komutlar `my-dojo` dizininden yürütülmelidir. Kendinizi bu klasörde konumlandırın:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core günlükleri



IBD ilerlemesini izlemek için Bitcoin core günlüklerini görüntüleyin:



```bash
./dojo.sh logs bitcoind
```



Başlangıçta, blok başlıklarının bir ön senkronizasyon aşamasını göreceksiniz:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Bu rakam %100'e ulaştığında, Bitcoin core, Blockchain'nin tamamen indirilmesine başlayacaktır. IBD ilerlemesini göreceksiniz. Geçerli blok yüksekliğini öğrenmek için `height=` ile gösterilen değere bakın. IBD ilerleme yüzdesini gösteren `progress=` anahtarını da takip edebilirsiniz.



![Image](assets/fr/36.webp)



Her zaman olduğu gibi, günlükleri kapatmak ve komut istemine dönmek için `Ctrl + C` kombinasyonunu kullanın.



#### Fulcrum günlükleri



Bitcoin core başlık ön senkronizasyonunu tamamladıktan sonra, Fulcrum ilerledikçe Blockchain'yi indekslemeye başlar. Günlüklerini ile görüntüleyin :



```bash
./dojo.sh logs fulcrum
```



Daha sonra `height:` ifadesinden sonra dizine eklenen son bloğun yüksekliğini ve dizine ekleme ilerleme yüzdesini göreceksiniz.



![Image](assets/fr/37.webp)



### 7.3. Fulcrum veritabanı bozulması



Fulcrum özellikle güçlü bir indeksleyicidir, ancak kurulumu karmaşık olabilir, özellikle de hassas veritabanı yönetimi nedeniyle. İlk senkronizasyon sırasında bir elektrik kesintisi veya makinenin aniden kapanması durumunda, indeksleyicinin veritabanı bozulabilir. Örneğin, aşağıdaki günlüklere sahipseniz bunu görebilirsiniz:



```bash
fulcrum | The database has been corrupted etc...
```



**Not:** Bu tür bir hata, Fulcrum 2.0'ın gelecek sürümüyle birlikte düzeltilmelidir.



Bu sizin başınıza gelirse, bitcoind (Bitcoin düğümünüz) üzerinde hiçbir etkisi olmayacaktır: IBD'si Fulcrum'dan bağımsız olarak ilerlemeye devam edecektir. Ancak, Fulcrum'un bozuk verilerini silene ve senkronizasyonunu baştan başlatana kadar Fulcrum'u kullanamazsınız. İşte nasıl çalıştığı:



Dojo'yu durdur:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Yalnızca Fulcrum kapsayıcısını ve birimini silin:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalde isim `my-dojo_data-fulcrum`dur, eğer sizin için durum böyle değilse, önceki komut tarafından döndürülen ismi uyarlayın.



Sonra Dojo'yu yeniden başlatın ve Fulcrum'u sıfırdan inşa edin:



```bash
./dojo.sh upgrade
```



Daha sonra günlüklere bakarak Fulcrum'un düzgün çalışıp çalışmadığını kontrol edebilirsiniz:



```bash
docker logs -f fulcrum
```




## 8. Dojo Bakım Aracını Kullanma



Bitcoin düğümünüz en fazla Proof of Work ile çözgü kafasına senkronize edildiğinde ve Blockchain Fulcrum tarafından %100 indekslendiğinde, Dojo'nuzu kullanmaya başlayabilirsiniz.



Dojo'nuz, her yeni sürümde düzenli olarak geliştirilmiş çok çeşitli özellikler sunar. Bana göre en önemli 2 özellik şunlardır:




- gW-58 verilerine danışmak ve işlemlerinizi yayınlamak için kendi düğümünüzü kullanmak üzere Ashigaru Wallet'unuzu bağlama imkanı,
- ve verilerinizi kontrol etmediğiniz harici bir örneğe maruz bırakmadan Blockchain Bitcoin hakkındaki bilgilere erişmenizi sağlayan Block explorer.



Bunları nasıl kullanacağımızı öğrenelim.


### 8.1. Ashigaru'yu Dojo'nuza bağlayın



Ashigaru Wallet'ünüzü Dojo'nuza bağlamak çok basittir: DMT'nizdeyken "*Pairing*" menüsünü açın. Doğrudan Ashigaru uygulaması ile tarayabileceğiniz bir QR kodu görünür.



![Image](assets/fr/38.webp)



Ashigaru uygulamasında, Wallet'ünüzü oluşturduktan veya geri yükledikten sonra ilk kez başlattığınızda, "*Dojo sunucunuzu yapılandırın*" sayfasına yönlendirileceksiniz. "*Karekodu tara*" düğmesine basın, ardından DMT'nizde görüntülenen QR kodunu tarayın.



![Image](assets/fr/39.webp)



Ardından "*Devam*" düğmesine tıklayın.



![Image](assets/fr/40.webp)



Şimdi Dojo'nuza bağlandınız.



![Image](assets/fr/41.webp)



### 8.2. Block explorer'in Kullanımı



Dojo otomatik olarak bir Block explorer, [BTC-RPC Explorer] (https://github.com/janoside/btc-RPC-explorer) yükler, bu da doğrudan kendi Bitcoin düğümünüzdeki verilerden yararlanır. Gezgin, anlaşılması kolay bir Interface ağı aracılığıyla Blockchain ve Mempool'inizden ham bilgilere erişmenizi sağlar. Böylece, örneğin, bekleyen bir işlemin durumunu kontrol edebilir, bir Address'un bakiyesini görüntüleyebilir veya bir bloğun bileşimini kolaylıkla inceleyebilirsiniz.



Buna erişmek için Tor Address'ü tarayıcınızdan almanız yeterlidir. Bunu yapmak için, DMT'nizin Address'ünü elde etmek için kullandığınız komutun aynısını çalıştırın:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Tor aracılığıyla tüm Dojo bağlantı bilgilerinize erişebileceksiniz. Burada ilgilendiğimiz URL aşağıdaki URL'dir:



```
Block Explorer =
```



DMT'nize zaten bağlıysanız, bu Address'ü bağlantı JSON'unun içindeki "*Pairing*" menüsünde de bulabilirsiniz:



![Image](assets/fr/43.webp)



Herhangi bir ağdaki herhangi bir makineden (uzaktan bile) tarayıcınıza erişmek için [Tor Browser] (https://www.torproject.org/download/) adresini açın ve az önce aldığınız URL'yi girin.



⚠️ **Lütfen bu Address'i kesinlikle gizli tutun



Daha sonra kendi Block explorer'nıza erişiminiz olacak.



![Image](assets/fr/44.webp)



*Resim kredisi: https://ashigaru.rs/.*



Bir işlemi takip etmek için, sağ üstteki arama çubuğuna txid'yi girmeniz yeterlidir.



![Image](assets/fr/45.webp)



*Resim kredisi: https://ashigaru.rs/.*



Bir Address ile ilişkili hareketleri kontrol etmek için, arama çubuğuna Address'i girerek aynı şekilde devam edin.



![Image](assets/fr/46.webp)



*Resim kredisi: https://ashigaru.rs/.*



Ayrıntıları görüntülemek için arama çubuğuna bir bloğun Hash veya yüksekliğini de girebilirsiniz.



![Image](assets/fr/47.webp)



*Resim kredisi: https://ashigaru.rs/.*



## 9. Dojo bakımı



### 9.1 Dojo'nuzu durdurun



Dojo'nuzun gücünü asla aniden kesmeyin, çünkü bu belirli veritabanlarını, özellikle de Fulcrum indeksleyicisini bozabilir. Kapatmanız gerekiyorsa, her zaman Dojo'yu temiz bir şekilde kapatın, ardından tüm prosedürler tamamlandıktan sonra makineyi de kapatın:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Dojo'nuzu güncelleyin



Dojo düzenli olarak gelişir ve hataları düzeltmek, kararlılığı artırmak ve özellikler eklemek için yeni sürümler yayınlanır. Bu nedenle [güncellemeleri düzenli olarak kontrol etmek](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) ve Dojo'nuzu güncellemek önemlidir. Bu işlem ilk kuruluma benzer, ancak yapılandırmanızı korurken belirli dosyaları mevcut en son sürümle değiştirmenizi gerektirir. İşte temiz ve güvenli bir güncelleme için izlenecek ayrıntılı adımlar:



Dojo'nuzun mevcut sürümünü öğrenmek için komutu çalıştırın :



```bash
./dojo.sh version
```



Bu adım isteğe bağlı olsa da, işletim sisteminizi güncelleyerek başlamanızı tavsiye ederim. Bu, uyumsuzluk riskini azaltır ve Dojo tarafından kullanılan bağımlılıkların güncel olmasını sağlar:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Dojo dizinine gidin ve mevcut hizmetleri durdurun:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Ardından temiz bir sayfa açmak için sisteminizi yeniden başlatın:



```bash
sudo reboot
```



Dojo dijital olarak imzalanmış dosyalarla birlikte gelir. Bu PGP imzaları, dosyaların geliştiriciden geldiğini ve herhangi bir şekilde değiştirilmediğini garanti eder. Dojo'yu her güncellediğinizde, tıpkı ilk yüklediğinizde yaptığınız gibi bunları kontrol etmeniz önemlidir. Geliştiricinin açık anahtarını Tor üzerinden indirerek başlayın, ardından içe aktarın :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kişisel dizininize geri dönün:



```bash
cd ~/
```



Tor aracılığıyla GitHub'dan Dojo'nun en son sürümünü indirin. Bu örnekte, `1.28.0` sürümüdür (yazım sırasında henüz mevcut değildir: bu sadece bir örnek vermek içindir). Dosyayı ve bağlantıyı [yüklemek istediğiniz sürümle] değiştirmeyi unutmayın (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Ayrıca PGP parmak izlerini ve imzasını içeren dosyayı da indirin (bir kez daha, komuttaki sürümü ayarlamayı unutmayın):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



İndirilen parmak izi dosyasının geliştiricinin anahtarı tarafından imzalanıp imzalanmadığını kontrol edin:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Doğru bir sonuç görüntülenmelidir :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Anahtarın sertifikasız olduğuna dair bir uyarı görünebilir, ancak bunun bir önemi yoktur. Öte yandan, imza geçersizse veya başka bir anahtara karşılık geliyorsa, daha ileri gitmeyin ve bağlantıları kontrol ederek yeniden başlayın.



Ardından arşivin SHA256 parmak izini hesaplayın ve resmi parmak izi dosyasıyla karşılaştırın :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



İki parmak izi mükemmel bir şekilde eşleşirse, arşiv orijinal ve sağlamdır. Farklılarsa, dosyaları hemen silin ve devam etmeyin.



Ev dizininizdeki arşivin sıkıştırmasını açın:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Ardından içeriği Dojo dizinine kopyalayın ve eski :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Bu işlem `~/dojo-app/docker/my-dojo/conf` içinde bulunan yapılandırma dosyalarınızı korur, ancak diğer tüm dosyaları güncellenmiş sürümlerle değiştirir.



Ortamınızı temiz tutmak için gereksiz dosyaları silin :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Dojo betikleri dizinine dönün ve güncelleme komutunu çalıştırın:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Bu komut Docker'a görüntüleri yeni dosyalarla yeniden oluşturmasını ve ardından tüm hizmetleri otomatik olarak yeniden başlatmasını söyler. İşlemin sonunda, Bitcoin core, Fulcrum ve Dojo'nun düzgün çalıştığından emin olmak için günlükleri kontrol edin:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Hizmetler hatasız başlarsa ve günlükler blokların işlendiğini gösterirse, Dojo'nuz artık güncel ve çalışır durumdadır.