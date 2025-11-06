---
name: Plan ₿ Akademi - Pears Uygulaması
description: Plan ₿ Academy uygulaması Pears'a nasıl kurulur ve kullanılır?
---

![cover](assets/cover.webp)


Plan ₿ Academy'nin Bitcoin'a adanmış en büyük eğitim veritabanı olduğunu, kursları, eğitimleri ve binlerce açık kaynak kaynağı bir araya getirdiğini muhtemelen zaten biliyorsunuzdur. Başlangıçta, Plan ₿ Academy bir web sitesiydi. Ancak, örneğin sansür durumunda artık normal olarak erişemezseniz ne olur?


Bu eğitimde, **Holepunch** tarafından geliştirilen ve **Tether** tarafından desteklenen bir eşler arası (P2P) teknolojisi olan **Pears** kullanarak **Plan ₿ Academy** platformunu sansüre gerçekten dayanıklı bir şekilde nasıl çalıştıracağımızı öğreneceğiz.


Pears, Plan ₿ Academy platformunu merkezi bir web sitesine bağlı kalmadan çalıştırmamızı sağlayan yazılımdır. Bu eğitimde, Pears aracılığıyla Plan ₿ Academy'ye erişmek için bilgisayarınıza Pears'ı kuracağız.


Pears'ın amacı basittir: web uygulamalarını herhangi bir merkezi altyapıya bağlı olmadan (sunucu yok, ana bilgisayar yok, aracı yok) dağıtmayı ve kullanmayı mümkün kılmak. Başka bir deyişle, bir bulut sağlayıcısı kapansa veya bir ülke bir alan adını engellese bile, uygulama ağın eşleri arasında yaşamaya devam eder. Bu yaklaşım, eğitim platformumuz Plan ₿ Academy'nin tek bir arıza noktası olmadan dünya çapında erişilebilir kalmasını sağlar.


---

**TL;DR:**



- Armutları yükleyin;



- Plan ₿ Academy uygulamasını başlatmak için aşağıdaki komutu çalıştırın:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Armut nedir?


Pears aynı anda bir çalışma zamanı ortamı, bir geliştirme aracı ve eşler arası uygulamalar için bir dağıtım platformudur. Bu açık kaynaklı araç, sunucular veya altyapı olmadan, doğrudan kullanıcılar arasında yazılım oluşturmanıza, paylaşmanıza ve çalıştırmanıza olanak tanır. Pratik açıdan bu, bir uygulamayı merkezi bir sunucuda barındırmak yerine, her kullanıcının ağdaki bir düğüm haline geldiği anlamına gelir: uygulamanın ve verilerin bir kısmını diğer eşlerle paylaşırlar. Tüm sistem, her bir örneğin hizmeti erişilebilir tutmak için işbirliği yaptığı dağıtılmış bir ağ oluşturur.


![Image](assets/fr/01.webp)


Bu yaklaşım Holepunch tarafından geliştirilen bir dizi modüler yazılım bileşenine dayanmaktadır:



- Hypercore**: merkezi bir veritabanı olmadan veri tutarlılığı ve güvenliği sağlayan dağıtılmış bir günlük.
- Hyperbee**: Hypercore üzerine inşa edilmiş, verilerin verimli bir şekilde düzenlenmesini ve sorgulanmasını sağlayan bir dizin.
- Hyperdrive**: Uygulama dosyalarını eşler arasında depolamak ve senkronize etmek için kullanılan dağıtılmış bir dosya sistemi.
- Hyperswarm** ve **HyperDHT**: merkezi bir sunucu olmadan dünya çapında eş keşfi ve bağlantıları sağlayan ağ katmanları.
- Secretstream**: eşler arasındaki iletişimi güvence altına alan uçtan uca bir şifreleme protokolü.


Bu bileşenleri bir araya getiren Pears, her kullanıcının ağa aktif olarak katıldığı otonom, şifrelenmiş ve dağıtılmış uygulamaların oluşturulmasını sağlar. Bu merkezi olmayan mimari altyapı maliyetlerini, sansür risklerini ve SPOF'ları (*Tek Arıza Noktası*) ortadan kaldırır.


Pears, Mathias Buus ve Paolo Ardoino (Tether CEO'su ve Bitfinex CTO'su) tarafından kurulan Holepunch tarafından, eşler arası mantığı Bitcoin'nin ötesine genişletme misyonuyla geliştirilmiştir. Amaçları, her uygulamanın izin almadan, sunucular olmadan ve aracılar olmadan çalışabileceği "*Eşlerin İnterneti*" ni inşa etmektir. Holepunch halihazırda tamamen P2P video konferans ve mesajlaşma uygulaması olan **Keet**'in arkasında yer alıyor.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Bu Pears kurulum eğitimi, işletim sisteminize bağlı olarak birden fazla bölüme ayrılmıştır. Uygun talimatları takip etmek için doğrudan ortamınıza karşılık gelen bölüme gidin:*



- Linux (Debian)** → Bölüm **2**
- Windows** → Bölüm **3**
- macOS** → Bölüm **4**


## 2. Linux (Debian) üzerinde Pears nasıl kurulur?


Pears'ı Debian'a kurmak nispeten basittir ancak bu bölümde detaylandıracağımız birkaç önkoşul gerektirir.


### 2.1. Sistemi güncelleyin


Her şeyden önce, sisteminizin güncel olduğundan emin olmanız önemlidir.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Bağımlılıkları yükleyin


Pears, Bare JavaScript çalışma zamanı motoru tarafından kullanılan `libatomic1` dahil olmak üzere bazı sistem kütüphanelerine dayanır. Aşağıdaki komut ile yükleyin:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. NVM aracılığıyla Node.js ve npm yükleyin


Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla dağıtılır. Pears çalışmak için doğrudan *Node.js*'ye bağımlı olmasa da, kurulum için gereklidir. Linux'ta *Node.js* kurmanın önerilen yolu, birden fazla Node sürümünü yan yana yönetmenizi sağlayan *NVM* (*Node Sürüm Yöneticisi*) kullanmaktır.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Ardından, *NVM*'yi etkinleştirmek için terminalinizi yeniden yükleyin:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


NVM*'nin doğru şekilde kurulduğunu kontrol edin:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Ardından, *Node.js'nin* kararlı bir sürümünü yükleyin (örneğin, mevcut LTS sürümü):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Node.js* ve *npm*'in düzgün bir şekilde yüklendiğini doğrulayın:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Pears'ı npm ile yükleyin


Bir kez *npm* kullanılabilir olduğunda, Pears CLI'ü sisteminize global olarak yükleyebilirsiniz. Bu, `pear` komutunu herhangi bir dizinden çalıştırmanıza olanak tanır.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Armutları Başlatma


Kurulumdan sonra, terminalinizde aşağıdaki komutu çalıştırmanız yeterlidir:


```bash
pear
```


İlk açılışta, Pears gerekli bileşenleri indirmek için eşler arası ağa bağlanacaktır. Bu işlem herhangi bir merkezi sunucuya bağlı değildir - dosyalar doğrudan diğer eşlerden alınır.


![Image](assets/fr/10.webp)


İndirme işlemi tamamlandığında, her şeyin çalıştığını onaylamak için komutu tekrar çalıştırın:


```bash
pear
```


![Image](assets/fr/11.webp)


Her şey doğru bir şekilde kurulduysa, Pears yardım menüsü mevcut komutların bir listesiyle birlikte görünecektir.


### 2.6. Armutları Keet ile Test Edin


Pears'ın tamamen çalışır durumda olduğunu doğrulamak için, Holepunch tarafından geliştirilen açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda bulunan mevcut bir P2P uygulamasını başlatabilirsiniz.


```bash
pear run pear://keet
```


Bu komut Keet uygulamasını merkezi bir sunucu kullanmadan doğrudan Pears ağından yükler. Keet doğru şekilde başlatılırsa, Pears kurulumunuzun tamamen işlevsel olduğu anlamına gelir.


![Image](assets/fr/12.webp)


Linux sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazırdır.


## 3. Pears Windows'a Nasıl Yüklenir


Pears'ı Windows'a yüklemek Linux'ta olduğu kadar basittir ancak birkaç özel araç gerektirir.


*Linux kullanıyorsanız ve Pears'ı zaten yüklediyseniz, doğrudan **Adım 5**'e geçebilirsiniz.*


### 3.1. PowerShell'i Yönetici olarak açın


İlk olarak, PowerShell'i yönetici ayrıcalıklarıyla başlatın:



- Başlat menüsüne tıklayın;
- "PowerShell" yazın;
- "*Windows PowerShell*" üzerine sağ tıklayın;
- "*Yönetici olarak çalıştır*" seçeneğini seçin.


![Image](assets/fr/15.webp)


### 3.2. NVS'yi İndirin


Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla yüklenir. Windows'ta Holepunch tarafından önerilen yöntem, bu sistemde *NVM*'den daha kararlı olan *NVS* (*Node Version Switcher*) kullanmaktır.


PowerShell'de, *NVS*'nin en son sürümünü yüklemek için aşağıdaki komutu çalıştırın:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Node.js'yi yükleyin


Kurulumdan sonra PowerShell'i yeniden başlatın ve ardından aşağıdaki komutu girin:


```powershell
nvs
```


Kullanılabilir *Node.js* sürümlerinin bir listesini görmelisiniz. Klavyenizdeki `a` tuşuna basarak ilkini seçin.


![Image](assets/fr/17.webp)


*Node.js* artık yüklü.


![Image](assets/fr/18.webp)


### 3.4. Kurulumları Doğrulayın


Node.js* ve *npm*'in erişilebilir olduğundan emin olun:


```powershell
node -v
npm -v
```


Her iki komut da bir sürüm numarası döndürmelidir.


![Image](assets/fr/19.webp)


### 3.5. Pears'ı npm ile yükleyin


Node.js* ve *npm* kullanılabilir olduğunda, **Pears CLI**'yı sisteminize global olarak yükleyin:


```powershell
npm install -g pear
```


Bu, `pear` ikili dosyasını global *npm* dizininize yükler.


![Image](assets/fr/20.webp)


### 3.6. Armutları Doğrulama ve Başlatma


Kurulum tamamlandıktan sonra çalıştırın:


```powershell
pear
```


İlk açılışta, Pears gerekli bileşenleri eşler arası ağdan otomatik olarak indirecektir. Bu işlem birkaç dakika sürebilir.


![Image](assets/fr/21.webp)


Her şey yolunda gittiyse, mevcut alt komutların (run, seed, info...) listesini içeren Pears CLI yardım menüsünü görmelisiniz.


### 3.7. Armutları Keet ile Test Edin


Pears'ın tamamen çalışır durumda olduğunu doğrulamak için, Holepunch tarafından geliştirilen açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda bulunan mevcut bir P2P uygulamasını başlatabilirsiniz.


```bash
pear run pear://keet
```


Bu komut Keet uygulamasını herhangi bir merkezi sunucu kullanmadan doğrudan Pears ağından yükler. Keet başarıyla başlatılırsa, Pears kurulumunuzun tamamen işlevsel olduğu anlamına gelir.


![Image](assets/fr/22.webp)


Windows sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazırdır.


## 4. Pears macOS'a Nasıl Yüklenir


Pears'ı macOS'a kurmak Linux'a benzer ancak Apple'ın ortamına özgü birkaç ayarlama gerektirir. Bu adımları birlikte gözden geçirelim.


*Linux veya Windows kullanıyorsanız ve Pears'ı zaten yüklediyseniz, doğrudan **Adım 5**'e geçebilirsiniz.*


### 4.1. Sistem Ön Koşullarını Kontrol Edin


Kurulumdan önce sisteminizde *Xcode Command Line Tools* yüklü olduğundan emin olun. Bu paket *Node.js* ve bağımlılıkları için gerekli derleme araçlarını sağlar.


Bunu yapmak için, `Cmd + Boşluk çubuğu` kısayolunu kullanarak bir terminal açın, `Terminal` yazın ve `Enter` tuşuna basın. Ardından, yüklemek için terminalde aşağıdaki komutu çalıştırın:


```bash
xcode-select --install
```


Araçlar sisteminizde zaten yüklüyse macOS sizi bilgilendirecektir.


### 4.2. NVM'yi yükleyin


Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla dağıtılır. Pears çalışmak için doğrudan *Node.js*'ye bağımlı olmasa da, kurulum için gereklidir. MacOS'ta *Node.js* yüklemek için önerilen yöntem, aynı anda birden fazla Node sürümünü yönetmenize olanak tanıyan *NVM* (*Node Version Manager*) yöntemidir.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Ardından *NVM*'yi etkinleştirmek için terminalinizi yeniden yükleyin:


```bash
source ~/.zshrc
```


Eğer *zsh* yerine *bash* kullanıyorsanız, çalıştırın:


```bash
source ~/.bashrc
```


Ardından, *NVM*'nin doğru şekilde kurulup kurulmadığını kontrol edin:


```bash
nvm --version
```


Terminaliniz kurulu *NVM* sürümünü göstermelidir.


### 4.3. Node.js ve npm yükleyin


Ardından, *Node.js'nin* kararlı bir sürümünü yükleyin (örneğin, mevcut LTS sürümü):


```bash
nvm install --lts
```


Kurulum tamamlandığında, yüklü sürümleri doğrulayın:


```bash
node -v
npm -v
```


Her iki komut da bir sürüm numarası döndürmelidir.


### 4.4. Pears'ı npm ile yükleyin


Bir kez *npm* kullanılabilir olduğunda, Pears CLI'u sisteminize global olarak yükleyebilirsiniz. Bu, `pear` komutunu herhangi bir dizinden çalıştırmanıza izin verecektir.


```bash
npm install -g pear
```


### 4.5. Armutları Başlatma


Kurulumdan sonra, terminalinizde aşağıdaki komutu çalıştırmanız yeterlidir:


```bash
pear
```


İlk açılışta, Pears gerekli bileşenleri indirmek için eşler arası ağa bağlanır. Bu işlem herhangi bir merkezi sunucu gerektirmez - dosyalar doğrudan diğer eşlerden alınır.


İndirme işlemi tamamlandığında, her şeyin çalıştığını doğrulamak için komutu yeniden çalıştırın:


```bash
pear
```


Her şey doğru şekilde yüklendiyse, Pears yardım menüsü mevcut komutların listesiyle birlikte görünecektir.


### 4.6. Armutları Keet ile Test Edin


Pears'ın tamamen çalışır durumda olduğunu doğrulamak için, Holepunch'ın açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda zaten mevcut olan bir P2P uygulamasını başlatabilirsiniz.


```bash
pear run pear://keet
```


Bu komut Keet uygulamasını merkezi bir sunucu kullanmadan doğrudan Pears ağından yükler. Keet başarıyla başlatılırsa, Pears kurulumunuzun tamamen işlevsel olduğu anlamına gelir.


MacOS sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazır.


## 5. Armutlarda Plan ₿ Akademi Nasıl Kullanılır


Pears kurulup çalıştırıldıktan sonra, **Plan ₿ Academy** platformunu P2P ağı üzerinden doğrudan başlatabilirsiniz. Terminalinizde aşağıdaki komutu çalıştırmanız yeterlidir (aynı komut Linux, Windows ve macOS'ta da çalışır):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Yükleme tamamlandığında, Plan ₿ Academy Pears ortamınızda açılacak ve tıpkı orijinal web sitesi gibi kullanılmaya hazır olacaktır - ancak merkezi bir sunucuya bağlı kalmadan.


![Image](assets/fr/14.webp)


## 6. Tohum Planı Nasıl Yapılır ₿ Armut Akademisi


Pears ağında, bir uygulamayı *seed* yapmak, onu kendi makinenizden diğer eşlere yeniden dağıtmak anlamına gelir. Pratikte, seed Plan ₿ Academy yaptığınızda, bilgisayarınız diğer kullanıcıların merkezi bir sunucuya bağlı kalmadan uygulamayı indirmelerine olanak tanıyan bir veri kaynağı haline gelir.


Bu mekanizma, uygulamamızın Pears ağındaki esnekliğini ve sansüre karşı direncini güçlendirmektedir. Bir uygulama ne kadar çok eş seed olursa, bazı orijinal düğümler çevrimdışı olsa bile o kadar kullanılabilir ve merkezi olmayan hale gelir.


Plan ₿ Academy'nin dağıtılmasına yardımcı olmak için aşağıdaki komutu çalıştırmanız yeterlidir:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Bu komut etkin kaldığı sürece, cihazınız uygulamanın dosyalarının dağıtımına katılacaktır. Terminali kapatırsanız, paylaşım işlemi durur.


Yeniden başlatmadan sonra ekime devam etmek için komutu arka planda çalıştırabilir veya bir sistem hizmeti oluşturabilirsiniz - örneğin, Linux'ta bir systemd hizmeti, macOS'ta bir LaunchAgent veya Windows'ta zamanlanmış bir görev. Bu yöntemler, Plan ₿ Academy uygulamasının sistem başlangıcında otomatik olarak ekime devam etmesini sağlar.


Plan ₿ Academy on Pears'ın merkezi olmayan dağıtımına katkıda bulunduğunuz ve Bitcoin eğitiminin sansüre karşı gerçekten dirençli olmasına yardımcı olduğunuz için teşekkür ederiz!