---
name: Pears
description: Pears'a uygulamaları nasıl yükleyebilir ve kullanabilirim?
---

![cover](assets/cover.webp)



Bu eğitimde, **Holepunch** tarafından geliştirilen ve **Tether** tarafından desteklenen bir eşler arası (P2P) teknoloji olan **Pears** üzerinde uygulamaların nasıl çalıştırılacağını öğreneceğiz. Amaç basit: web uygulamalarını herhangi bir merkezi altyapıya (sunucu yok, ana bilgisayar yok, aracı yok) dayanmadan dağıtmayı ve kullanmayı mümkün kılmak. Başka bir deyişle, bir bulut sağlayıcısı kapansa veya bir ülke bir alanı engellese bile, uygulama ağ eşleri arasında yaşamaya devam eder.



## 1. Armut nedir?



Pears, eşler arası uygulamalar için bir çalışma zamanı ortamı, geliştirme aracı ve dağıtım platformudur. Bu açık kaynaklı araç, bir sunucu veya altyapı olmadan, doğrudan kullanıcılar arasında yazılım oluşturmayı, paylaşmayı ve çalıştırmayı mümkün kılar. Somut olarak bu, bir uygulamayı merkezi bir sunucuda barındırmak yerine, her kullanıcının uygulamanın bir bölümünü ve verileri diğer eşlerle paylaşan bir ağ düğümü haline geldiği anlamına gelir. Tüm sistem, her bir örneğin hizmeti erişilebilir tutmak için işbirliği yaptığı dağıtılmış bir ağ oluşturur.



![Image](assets/fr/01.webp)



Bu yaklaşım Holepunch tarafından geliştirilen bir dizi modüler yazılım tuğlasına dayanmaktadır:




- Hypercore**: merkezi bir veritabanı olmadan veri tutarlılığını ve güvenliğini garanti eden dağıtılmış bir günlük.
- Hyperbee**: verimli veri organizasyonu ve tarama için Hypercore üzerinde bir indeksleyici.
- Hyperdrive**: Uygulama dosyalarını eşler arasında depolamak ve senkronize etmek için kullanılan dağıtılmış bir dosya sistemi.
- Hyperswarm** ve **HyperDHT**: merkezi bir sunucu olmadan dünya çapındaki eşler arasında keşif ve bağlantı sağlayan ağ katmanları.
- Secretstream**: iki eş arasındaki alışverişleri güvence altına almak için bir E2E şifreleme protokolü.



Bu bileşenleri bir araya getiren Pears, her kullanıcının ağa aktif olarak katıldığı otonom, şifrelenmiş ve dağıtılmış uygulamalar oluşturmayı mümkün kılar. Bu merkezi olmayan mimari altyapı maliyetlerini, sansür risklerini ve SPOF'ları (*Tek Arıza Noktası*) ortadan kaldırır.



## 2. Projenin kökeni ve felsefesi



Pears, Mathias Buus ve Paolo Ardoino (Tether CEO'su ve Bitfinex CTO'su) tarafından kurulan Holepunch şirketi tarafından, eşler arası mantığı Bitcoin'in ötesine genişletme misyonuyla geliştirilmektedir. Amaçları, her uygulamanın yetkilendirme olmadan, sunucular olmadan ve aracılar olmadan çalışabileceği "Eşler Arası İnternet" inşa etmektir. Holepunch halihazırda tamamen P2P video konferans ve mesajlaşma uygulaması olan **Keet**'in arkasındadır.



*Bu Pears kurulum eğitimi, işletim sisteminize bağlı olarak birkaç bölüme ayrılmıştır. Uygun talimatları takip etmek için doğrudan ortamınıza karşılık gelen bölüme gidin :*




- Linux (Debian)** → Bölüm **3**
- Windows** → Bölüm **4**
- macOS** → Bölüm **5**



## 3. Linux (Debian) üzerinde Pears nasıl kurulur



Pears'ı bir Debian sistemine kurmak nispeten basittir, ancak bu bölümde detaylandıracağımız birkaç ön koşul gerektirir.



### 3.1. sistemi güncelleyin



Her şeyden önce, sisteminizin güncel olduğundan emin olmanız önemlidir.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. bağımlılıkları yükleyin



Pears, özellikle Bare JavaScript çalışma zamanı tarafından kullanılan `libatomic1` olmak üzere belirli sistem kütüphanelerine dayanır. Aşağıdaki komut ile yükleyin:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. NVM aracılığıyla Node.js ve npm yükleyin



Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla dağıtılmaktadır. Pears çalışmak için doğrudan *Node.js*'ye bağımlı olmasa da, kurulum için gereklidir. Linux üzerinde *Node.js* kurulumu için önerilen yöntem, Node'un çeşitli sürümlerini paralel olarak yönetmenizi sağlayan *NVM* (*Node Version Manager*) yöntemidir.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Ardından *NVM* 'yi etkinleştirmek için terminalinizi yeniden yükleyin:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



NVM*'nin kurulu olup olmadığını kontrol edin:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Ardından *Node.js'nin* kararlı bir sürümünü yükleyin (örneğin, mevcut LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Node.js* ve *npm* kurulumlarını kontrol edin:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Pears'ın npm ile Kurulumu



Bir kez *npm* kullanılabilir olduğunda, Pears CLI'ü sisteminize global olarak yükleyebilirsiniz. Bu, `pear` komutunu herhangi bir dizinden çalıştırmanıza izin verecektir.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Armutları Başlatma



Kurulumdan sonra, terminalinizde aşağıdaki komutu çalıştırmanız yeterlidir:



```bash
pear
```



İlk açılışta, Pears gerekli bileşenleri indirmek için eşler arası ağa bağlanacaktır. Bu işlem merkezi bir sunucu gerektirmez: dosyalar doğrudan diğer eşlerden elde edilir.



![Image](assets/fr/10.webp)



İndirme işlemi tamamlandığında, her şeyin çalışıp çalışmadığını kontrol etmek için komutu tekrar çalıştırın:



```bash
pear
```



![Image](assets/fr/11.webp)



Her şey doğru bir şekilde yüklendiyse, Pears Help mevcut komutların bir listesiyle birlikte görüntülenecektir.



### 3.6. Armutların Keet ile Test Edilmesi



Pears'ın tam olarak çalışıp çalışmadığını kontrol etmek için, Holepunch'ın açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda zaten mevcut olan bir P2P uygulamasını başlatabilirsiniz.



```bash
pear run pear://keet
```



Bu komut Keet uygulamasını merkezi bir sunucudan geçirmeden doğrudan Pears ağından yükler. Keet doğru şekilde başlatılırsa, Pears kurulumunuz tamamen işlevseldir.



![Image](assets/fr/12.webp)



Linux sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazırdır.



## 4. Windows'a Pears nasıl kurulur



Pears'ı Windows'a yüklemek Linux'a yüklemek kadar kolaydır, ancak birkaç özel araç gerektirir.



*Eğer Linux kullanıyorsanız, 6.* adımına geçebilirsiniz



### 4.1. PowerShell'i yönetici modunda açın



Öncelikle PowerShell'i yönetici haklarıyla çalıştırın :




- Başlat menüsüne tıklayın;
- PowerShell yazın;
- "*Windows PowerShell*" üzerine sağ tıklayın;
- "*Yönetici olarak çalıştır*" seçeneğini seçin.



![Image](assets/fr/15.webp)



### 4.2. NVS'yi indirin



Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla yüklenir. Windows'ta Holepunch tarafından önerilen yöntem, bu sistemde *NVM*'den daha kararlı olan *NVS* (*Node Version Switcher*) kullanmaktır.



PowerShell'de, *NVS* 'nin en son sürümünü yüklemek için aşağıdaki komutu çalıştırın:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Node.js'yi yükleyin



Kurulumdan sonra PowerShell'i yeniden başlatın ve aşağıdaki komutu girin:



```powershell
nvs
```



Kullanılabilir *Node.js* sürümlerinin bir listesini görmelisiniz. Klavyenizdeki `a` tuşuna basarak ilkini seçin.



![Image](assets/fr/17.webp)



*Node.js* yüklü.



![Image](assets/fr/18.webp)



### 4.4. Kurulumları kontrol edin



Node.js* ve *npm*'in erişilebilir olduğundan emin olun:



```powershell
node -v
npm -v
```



Her iki komut da bir sürüm numarası döndürmelidir.



![Image](assets/fr/19.webp)



### 4.5. Pears'ı npm ile Yükleme



Node.js* ve *npm* kullanılabilir olduğunda, **Pears CLI**'i sisteminize global olarak yükleyin:



```powershell
npm install -g pear
```



Bu, `pear` ikili dosyasını global *npm* dizininize yükleyecektir.



![Image](assets/fr/20.webp)



### 4.6. Pears'ı kontrol edin ve başlatın



Kurulum tamamlandıktan sonra çalıştırın :



```powershell
pear
```



İlk açılışta, Pears gerekli bileşenleri eşler arası ağdan otomatik olarak indirecektir. Bu işlem birkaç dakika sürebilir.



![Image](assets/fr/21.webp)



Her şey yolunda gittiyse, mevcut alt komutların (run, seed, info...) bir listesini içeren CLI Pears yardım ekranını görmelisiniz.



### 4.7. Armutların Keet ile Test Edilmesi



Pears'ın tam olarak çalışıp çalışmadığını kontrol etmek için, Holepunch'ın açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda zaten mevcut olan bir P2P uygulamasını başlatabilirsiniz.



```bash
pear run pear://keet
```



Bu komut Keet uygulamasını merkezi bir sunucudan geçirmeden doğrudan Pears ağından yükler. Keet doğru şekilde başlatılırsa, Pears kurulumunuz tamamen işlevseldir.



![Image](assets/fr/22.webp)



Windows sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazırdır.



## 5. Pears'ı macOS'a nasıl yüklerim?



Pears'ı macOS'a kurmak Linux'a kurmaya benzer, ancak Apple ortamına özgü birkaç ayarlama gerektirir. Gelin bu adımları birlikte keşfedelim.



*Linux veya Windows kullanıyorsanız ve Pears'ı zaten yüklediyseniz, doğrudan **adım 6**'ya geçebilirsiniz.*



### 5.1. Sistem gereksinimlerini kontrol edin



Yüklemeden önce lütfen sisteminizde *Xcode Komut Satırı Araçlarının* mevcut olduğundan emin olun. Bu paket _Node.js_ ve bağımlılıkları için gerekli derleme araçlarını sağlar.



Bunu yapmak için, `Cmd + Boşluk çubuğu` klavye kısayolunu kullanarak bir terminal açın, ardından `Terminal` yazın ve `Enter` tuşuna basın. Daha sonra kurulumu başlatmak için bu komutu terminale girebilirsiniz:



```bash
xcode-select --install
```



Araçlar sisteminizde zaten yüklüyse, macOS sizi bilgilendirecektir.



### 5.2. NVM'yi yükleyin



Pears, *Node.js* paket yöneticisi olan *npm* aracılığıyla dağıtılmaktadır. Pears çalışmak için doğrudan *Node.js*'ye bağımlı olmasa da, kurulum için gereklidir. MacOS üzerinde *Node.js* kurulumu için önerilen yöntem, Node'un çeşitli sürümlerini paralel olarak yönetmenize olanak tanıyan *NVM* (*Node Version Manager*) yöntemidir.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Ardından *NVM* 'yi etkinleştirmek için terminalinizi yeniden yükleyin:



```bash
source ~/.zshrc
```



Eğer *zsh* yerine *bash* kullanıyorsanız, :



```bash
source ~/.bashrc
```



Ardından *NVM*'nin kurulu olup olmadığını kontrol edin:



```bash
nvm --version
```



Terminal, sisteminizde kurulu *NVM* sürümünü döndürmelidir.



### 5.3. Node.js ve npm'yi yükleyin



Ardından *Node.js'nin* kararlı bir sürümünü yükleyin (örneğin, mevcut LTS):



```bash
nvm install --lts
```



Kurulum tamamlandığında, yüklü sürümleri kontrol edin:



```bash
node -v
npm -v
```



Her iki komut da bir sürüm numarası döndürmelidir.



### 5.4 Pears'ın npm ile Kurulumu



Bir kez *npm* kullanılabilir olduğunda, Pears CLI'u sisteminize global olarak yükleyebilirsiniz. Bu, `pear` komutunu herhangi bir dizinden çalıştırmanıza izin verecektir.



```bash
npm install -g pear
```



### 5.5. Armutları Başlatma



Kurulumdan sonra, terminalinizde aşağıdaki komutu çalıştırmanız yeterlidir:



```bash
pear
```



İlk açılışta, Pears gerekli bileşenleri indirmek için eşler arası ağa bağlanacaktır. Bu işlem merkezi bir sunucu gerektirmez: dosyalar doğrudan diğer eşlerden elde edilir.



İndirme işlemi tamamlandığında, her şeyin çalışıp çalışmadığını kontrol etmek için komutu tekrar çalıştırın:



```bash
pear
```



Her şey doğru bir şekilde yüklendiyse, Pears Help mevcut komutların bir listesiyle birlikte görüntülenecektir.



### 5.6. Armutların Keet ile Test Edilmesi



Pears'ın tam olarak çalışıp çalışmadığını kontrol etmek için, Holepunch'ın açık kaynaklı mesajlaşma ve video konferans yazılımı Keet gibi ağda zaten mevcut olan bir P2P uygulamasını başlatabilirsiniz.



```bash
pear run pear://keet
```



Bu komut Keet uygulamasını merkezi bir sunucudan geçirmeden doğrudan Pears ağından yükler. Keet doğru şekilde başlatılırsa, Pears kurulumunuz tamamen işlevseldir.



MacOS sisteminiz artık Pears ile eşler arası uygulamaları çalıştırmaya ve barındırmaya hazır.



## 6. Armutlar üzerinde bir uygulamayı nasıl kullanabilirim?



Pears kurulup çalışmaya başladıktan sonra, aşağıdaki komutla seçtiğiniz uygulamayı doğrudan çalıştırabilirsiniz:



```bash
pear run pear://[KEY]
```



Sadece `[KEY]` yerine kullanmak istediğiniz uygulama anahtarını yazın.



![Image](assets/fr/13.webp)



Plan ₿ Academy platformumuzu Pears üzerinde nasıl çalıştıracağınızı öğrenmek için bu kapsamlı eğitime göz atın:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Ve Pears'ta yeni başlattığınız Keet mesajlaşma uygulamasını nasıl kullanacağınızı öğrenmek için bu eğitime göz atın :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b