---
name: RoninDojo

description: RoninDojo Bitcoin düğümünüzü yükleme ve kullanma.
---
***UYARI:** Samourai Wallet'nin kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, RoninDojo'nun Whirlpool gibi bazı özellikleri artık çalışmıyor. Bununla birlikte, bu araçların önümüzdeki haftalarda eski haline getirilmesi veya farklı bir şekilde yeniden başlatılması mümkündür. Ayrıca, RoninDojo kodu Samourai'nin GitLab'ında barındırıldığından ve bu GitLab'a da el konulduğundan, kodu uzaktan indirmek şu anda mümkün değil. RoninDojo ekipleri muhtemelen kodu yeniden yayınlamak için çalışıyorlar.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


bu eğitim RoninDojo v1'in kurulumuna adanmıştır. En son iyileştirmelerden ve özelliklerden yararlanmak için, RoninDojo v2'nin Raspberry Pi'nize doğrudan kurulumuna adanmış eğitimimize başvurmanızı şiddetle tavsiye ederim:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Kendi düğümünüzü çalıştırmak ve kullanmak, Bitcoin ağına gerçekten katılmak için gereklidir. Bir Bitcoin düğümü çalıştırmak kullanıcıya herhangi bir maddi fayda sağlamasa da, gizliliklerini korumalarına, bağımsız hareket etmelerine ve ağa duydukları güven üzerinde kontrol sahibi olmalarına olanak tanır.


Bu makalede, kendi Bitcoin düğümünüzü çalıştırmak için harika bir çözüm olan RoninDojo'ya ayrıntılı bir şekilde bakacağız.


### İçindekiler:



- RoninDojo nedir?
- Hangi donanım seçilmeli?
- RoninDojo nasıl kurulur?
- RoninDojo nasıl kullanılır?
- Sonuç


Bir Bitcoin düğümünün nasıl çalıştığını ve rolünü bilmiyorsanız, bu makaleyi okuyarak başlamanızı tavsiye ederim: Bitcoin Düğümü - Bölüm 1/2: Teknik Kavramlar.


![Samourai](assets/1.webp)


## RoninDojo nedir?


Dojo, Samourai Bitcoin ekibi tarafından geliştirilen tam bir Wallet düğüm sunucusudur. Herhangi bir makineye özgürce kurabilirsiniz.


RoninDojo, Dojo ve diğer çeşitli araçlar için bir kurulum asistanı ve yönetim aracıdır. RoninDojo, Dojo'nun orijinal uygulamasını alır ve ona birçok başka araç eklerken, kurulum ve yönetimi de kolaylaştırır.


Ayrıca, RoninDojo'nun kendi ekipleri tarafından monte edilmiş bir makineye önceden yüklenmiş olduğu bir "tak ve çalıştır" donanımı olan RoninDojo Tanto'yu da sunuyorlar. Tanto, ellerini kirletmek istemeyenler için uygun, ücretli bir çözümdür.


RoninDojo'nun kodu açık kaynak kodludur, dolayısıyla bu çözümü kendi donanımınıza kurmanız da mümkündür. Bu seçenek uygun maliyetlidir ancak biraz daha fazla manipülasyon gerektirir, biz de bu makalede bunu yapacağız.


RoninDojo bir Dojo'dur, bu nedenle mümkün olan en iyi CoinJoin deneyimine sahip olmak için Whirlpool CLI'in Bitcoin düğümünüze kolayca entegre edilmesini sağlar. Whirlpool CLI ile, kişisel bilgisayarınızı açık tutmanıza gerek kalmadan bitcoinlerinizin 7/24 remiks yapmasına izin vermekle kalmaz, aynı zamanda gizliliğinizi de büyük ölçüde artırabilirsiniz.


RoninDojo, bir işlemin gizlilik seviyesini belirleyen Boltzmann hesaplayıcısı, farklı Bitcoin cüzdanlarınızı düğümünüze bağlamak için Electrum sunucusu veya işlemlerinizi özel olarak gözlemlemek için Mempool sunucusu gibi Dojo'nuza dayanan diğer birçok aracı entegre eder.

Bu makalede size sunduğum Umbrel gibi başka bir düğüm çözümüyle karşılaştırıldığında RoninDojo, kullanıcı gizliliğini optimize eden "on chain" çözümlerine ve araçlarına derinlemesine odaklanmıştır. Bu nedenle, RoninDojo Lightning Network ile etkileşime izin vermez.

RoninDojo, Umbrel'e kıyasla daha az araç sunar, ancak Ronin'de bulunan bir Bitcoiner için birkaç temel özellik inanılmaz derecede kararlıdır.


Dolayısıyla, bir Umbrel sunucusunun tüm özelliklerine ihtiyacınız yoksa ve yalnızca Whirlpool veya Mempool gibi birkaç temel araca sahip basit ve kararlı bir düğüm istiyorsanız, RoninDojo muhtemelen sizin için iyi bir çözümdür.


Bana göre Umbrel'in geliştirme odağı büyük ölçüde Lightning Network ve çok yönlü araçlardır. Hala bir Bitcoin düğümüdür, ancak amaç onu çok görevli bir mini sunucu haline getirmektir. Buna karşılık, RoninDojo'nun geliştirme odağı Samourai Wallet'deki ekiplerle daha uyumludur ve bir Bitcoiner için temel araçlara odaklanarak Bitcoin'da tam bağımsızlık ve optimize edilmiş gizlilik yönetimi sağlar.


Lütfen bir RoninDojo düğümü kurmanın bir Umbrel düğümünden biraz daha karmaşık olduğunu unutmayın.


Artık RoninDojo'nun bir resmini çizebildiğimize göre, bu düğümü nasıl kuracağımızı birlikte görelim.


## Hangi donanım seçilmeli?


RoninDojo'yu barındıran ve çalıştıran makineyi seçmek için birkaç seçeneğiniz vardır.


Daha önce açıklandığı gibi, en basit seçim, özellikle bu amaç için tasarlanmış bir tak ve çalıştır makinesi olan Tanto'yu sipariş etmektir. Kendinizinkini sipariş etmek için buraya gidin: [link](https://shop.ronindojo.io/product-category/nodes/).


RoninDojo ekipleri açık kaynaklı kod ürettiğinden, RoninDojo'yu başka makinelerde de uygulamak mümkündür. Kurulum sihirbazının en son sürümlerini bu sayfada bulabilirsiniz: [link](https://ronindojo.io/en/downloads.html) ve kodun en son sürümlerini bu sayfada bulabilirsiniz: [link](https://code.samourai.io/ronindojo/RoninDojo).


Şahsen ben Raspberry Pi 4 8GB üzerine kurdum ve her şey mükemmel çalışıyor.


Ancak, RoninDojo ekiplerinin kasa ve SSD adaptörü ile ilgili sıklıkla sorunlar yaşandığını belirttiğini lütfen unutmayın. Bu nedenle makinenizin SSD'si için kablolu bir kasa kullanmanız önerilmez. Bunun yerine, bunun gibi anakartınız için özel olarak tasarlanmış bir depolama genişletme kartı kullanmanız tercih edilir: Raspberry Pi 4 Depolama Genişletme Kartı.


İşte kendi RoninDojo düğümünüzü nasıl kuracağınıza dair bir örnek:



- Bir Raspberry Pi 4.
- Vantilatörlü bir kasa.
- Uyumlu bir depolama genişletme kartı.
- Bir güç kablosu.
- 16GB veya daha fazla endüstriyel bir mikro SD kart.
- 1 TB veya daha büyük bir SSD.
- Bir RJ45 Ethernet kablosu, kategori 8 önerilir.


## RoninDojo Nasıl Kurulur?


### Adım 1: Önyüklenebilir mikro SD kartı hazırlayın.


Makinenizi bir araya getirdikten sonra, RoninDojo'nun kurulumuna başlayabilirsiniz. Bunu yapmak için, uygun disk görüntüsünü üzerine yazarak önyüklenebilir bir mikro SD kart oluşturarak başlayın.


Mikro SD kartınızı kişisel bilgisayarınıza takın, ardından RoninOS disk görüntüsünü indirmek için resmi RoninDojo web sitesine gidin: https://ronindojo.io/en/downloads.html.


Donanımınıza karşılık gelen disk görüntüsünü indirin. Benim durumumda, "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" imajını indirdim:


![Download RoninOS disk image](assets/2.webp)


Görüntü indirildikten sonra, ilgili .SHA256 dosyasını kullanarak bütünlüğünü doğrulayın. Bu makalede bunun nasıl yapılacağını ayrıntılı olarak açıklayacağım: Windows'ta Bitcoin yazılımının bütünlüğü nasıl doğrulanır?


RoninOS'un bütünlüğünü doğrulamak için özel talimatlar da bu sayfada mevcuttur: https://wiki.ronindojo.io/en/extras/verify.


Bu görüntüyü mikro SD kartınıza yazmak için buradan indirebileceğiniz Balena Etcher gibi bir yazılım kullanabilirsiniz: https://www.balena.io/etcher/.


Bunu yapmak için, Etcher'da görüntüyü seçin ve mikro SD karta flaşlayın:


![Burn disk image with Etcher](assets/3.webp)


İşlem tamamlandıktan sonra, önyüklenebilir mikro SD kartı Raspberry Pi'ye takabilir ve makineyi açabilirsiniz.


### Adım 2: RoninOS'u yapılandırın.


RoninOS, RoninDojo düğümünüzün işletim sistemidir. Bir Linux dağıtımı olan Manjaro'nun değiştirilmiş bir sürümüdür. Makinenizi başlattıktan ve birkaç dakika bekledikten sonra yapılandırmaya başlayabilirsiniz.


Uzaktan bağlanmak için, RoninDojo makinenizin IP Address'sini bulmanız gerekecektir. Bunu yapmak için, örneğin, internet kutunuzun yönetim paneline bağlanabilir veya yerel ağınızı taramak ve makinenin IP'sini bulmak için https://angryip.org/ gibi bir yazılım da indirebilirsiniz.


IP'yi bulduktan sonra, SSH kullanarak aynı yerel ağa bağlı başka bir bilgisayardan makinenizin kontrolünü ele geçirebilirsiniz.


MacOS veya Linux çalıştıran bir bilgisayardan terminali açmanız yeterlidir. Windows çalıştıran bir bilgisayardan Putty gibi özel bir araç kullanabilir veya doğrudan Windows PowerShell'i kullanabilirsiniz.


Terminal açıldıktan sonra aşağıdaki komutu yazın:

```
ssh root@192.168.?.?
```


İki soru işaretini daha önce bulduğunuz RoninDojo'nun IP'si ile değiştirmeniz yeterlidir.

İpucu: Bir Kabukta, bir öğeyi yapıştırmak için sağ tıklayın.


Ardından, Manjaro kontrol paneline ulaşacaksınız. Açılır listedeki hedefi değiştirmek için okları kullanarak doğru klavye düzenini seçin.


![Manjaro Keyboard Configuration](assets/4.webp)


Oturumunuz için bir kullanıcı adı ve parola seçin. Güçlü bir parola kullanın ve güvenli bir yedekleme yapın. İsteğe bağlı olarak kurulum sırasında zayıf bir parola kullanabilir ve daha sonra bunu RoninUI'ye "kopyalayıp yapıştırarak" kolayca değiştirebilirsiniz. Bu, Manjaro'nun kurulumu sırasında elle yazmak için çok fazla zaman harcamadan çok güçlü bir şifre kullanmanıza izin verecektir.


![Manjaro Username Configuration](assets/5.webp)


Ardından, bir kök parolası seçmeniz de istenecektir. Kök parolası için doğrudan güçlü bir parola girin. RoninUI'den değiştirmeniz mümkün olmayacaktır. Ayrıca, bu kök parolayı güvenli bir şekilde yedeklemeyi unutmayın.


Ardından konumunuzu ve saat diliminizi girin.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Ardından, bir ana bilgisayar adı seçin.


![Manjaro Hostname Configuration](assets/8.webp)


Son olarak, Manjaro yapılandırma bilgilerini doğrulayın ve onaylayın.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### 3. Adım: RoninDojo'yu indirin.


RoninOS'un ilk yapılandırması yapılacaktır. Tamamlandığında, yukarıdaki ekran görüntüsünde gösterildiği gibi, makine yeniden başlayacaktır. Birkaç dakika bekleyin, ardından RoninDojo makinenize yeniden bağlanmak için aşağıdaki komutu girin:

```
ssh username@192.168.?.?
```


Sadece "kullanıcı adı" yerine daha önce seçtiğiniz kullanıcı adını yazın ve soru işaretlerini RoninDojo'nuzun IP'si ile değiştirin.


Ardından kullanıcı şifrenizi girin.


Terminalde şu şekilde görünecektir:


![SSH Connection to RoninOS](assets/10.webp)


Şu anda sadece RoninOS'a sahip olan makinenize bağlandınız. Şimdi üzerine RoninDojo'yu yüklemeniz gerekiyor.


Aşağıdaki komutu girerek RoninDojo'nun en son sürümünü indirin:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


İndirme işlemi hızlı olacaktır. Terminalde şunu göreceksiniz:


![Cloning RoninDojo](assets/11.webp)


İndirme işleminin bitmesini bekleyin, ardından aşağıdaki komutu kullanarak RoninDojo kullanıcı Interface'ü kurun ve erişin:

```
~/RoninDojo/ronin
```


Kullanıcı şifrenizi girmeniz istenecektir:


![Bitcoin Node Password Verification](assets/12.webp)


Bu komut yalnızca RoninDojo'nuza ilk kez eriştiğinizde gereklidir. Daha sonra, SSH aracılığıyla RoninCLI'ye erişmek için, [SSH username@192.168.?.?] komutunu "kullanıcı adı" yerine kullanıcı adınızla değiştirerek ve düğümünüzün IP Address'ünü girmeniz yeterli olacaktır. Kullanıcı parolanız istenecektir.


Ardından, bu muhteşem animasyonu göreceksiniz:


![RoninCLI launch animation](assets/13.webp)


Sonunda RoninDojo CLI kullanıcısı Interface'e ulaşacaksınız.


### Adım 4: RoninDojo'yu yükleyin.


Ana menüden, klavyenizdeki ok tuşlarını kullanarak "Sistem" menüsüne gidin. Seçiminizi onaylamak için enter tuşuna basın.


![RoninCLI navigation menu to System](assets/14.webp)


Ardından "Sistem Kurulumu ve Yükleme" menüsüne gidin.


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Son olarak, boşluk çubuğunu kullanarak "Sistem Kurulumu" ve "RoninDojo'yu Kur" seçeneğini işaretleyin, ardından kurulumu başlatmak için "Kabul Et" seçeneğini seçin.


![RoninDojo installation confirmation](assets/16.webp)


Kurulumun sessizce ilerlemesine izin verin. Benim durumumda yaklaşık 2 saat sürdü. İşlem sırasında terminalinizi açık tutun.


Örneğin burada olduğu gibi, kurulumun belirli aşamalarında bir tuşa basmanız isteneceğinden ara sıra terminalinizi kontrol edin:


![RoninDojo installation in progress](assets/17.webp)


Kurulumun sonunda, farklı konteynerlerin başladığını göreceksiniz:


![Node container startup](assets/18.webp)


Ardından düğümünüz yeniden başlayacaktır. Bir sonraki adım için RoninCLI'ye tekrar bağlanın.


![Bitcoin node restart](assets/19.webp)


### Adım 5: Proof-of-Work zincirini indirin ve RoninUI'ye erişin.


Kurulum tamamlandığında, düğümünüz Bitcoin Proof-of-Work zincirini indirmeye başlayacaktır. Buna İlk Blok İndirme (IBD) adı verilir. İnternet bağlantınıza ve cihazınıza bağlı olarak genellikle 2 ila 14 gün arasında sürer.


RoninUI web Interface'a erişerek zincir indirme işleminin ilerleyişini takip edebilirsiniz.


Yerel bir ağdan erişmek için tarayıcınızın Address çubuğuna aşağıdakileri yazın:



- Ya doğrudan makinenizin IP Address'sini girin (192.168.???)
- Veya girin: ronindojo.local


VPN kullanıyorsanız VPN'inizi devre dışı bırakmayı unutmayın.


### Olası bükülme


Tarayıcınızdan RoninUI'ye bağlanamıyorsanız, SSH aracılığıyla düğümünüze bağlı Terminalinizden uygulamanın düzgün çalışıp çalışmadığını kontrol edin. Önceki adımları takip ederek ana menüye bağlanın:



- Yazın: SSH username@192.168.?.? kimlik bilgilerinizle değiştirin.



- Kullanıcı şifrenizi girin.


Ana menüye girdikten sonra, şuraya gidin: **RoninUI > Yeniden Başlat**


Uygulama doğru şekilde yeniden başlatılırsa, tarayıcınızdan gelen bağlantıyla ilgili bir sorun vardır. VPN kullanmadığınızı kontrol edin ve düğümünüzle aynı ağa bağlı olduğunuzdan emin olun.


Yeniden başlatma bir hata oluşturursa, işletim sistemini güncellemeyi ve ardından RoninUI'yi yeniden yüklemeyi deneyin. İşletim sistemini güncellemek için: **Sistem > Yazılım Güncellemeleri > İşletim Sistemini Güncelle**


Güncelleme ve yeniden başlatma tamamlandığında, SSH aracılığıyla düğümünüze yeniden bağlanın ve RoninUI'yi yeniden yükleyin: **RoninUI > Yeniden Yükle**


RoninUI'yi tekrar indirdikten sonra, tarayıcınız üzerinden RoninUI'ye bağlanmayı deneyin.


**İpucu:** Yanlışlıkla RoninCLI'dan çıkar ve kendinizi Manjaro terminalinde bulursanız, doğrudan RoninCLI ana menüsüne dönmek için "ronin" komutunu girmeniz yeterlidir.


### Web oturum açma


Tor kullanarak herhangi bir ağdan RoninUI web Interface'e de giriş yapabilirsiniz. Bunu yapmak için RoninUI'nizin Tor Address'ünü RoninCLI'dan alın: **Kimlik Bilgileri > Ronin UI**


.onion ile biten Tor Address'i alın ve ardından Tor tarayıcınıza bu Address'i girerek Ronin UI'de oturum açın. Hassas bilgiler olduğu için çeşitli kimlik bilgilerinizi sızdırmamaya dikkat edin.


![RoninUI web login interface](assets/20.webp)


Giriş yaptıktan sonra kullanıcı parolanız sorulacaktır. Bu, SSH üzerinden oturum açmak için kullandığınız parolanın aynısıdır.


![RoninUI web interface management panel](assets/21.webp)


IBD'nin (İlk Blok İndirme) ilerleyişini buradan görebiliriz. Sabırlı olun, 3 Ocak 2009'dan bu yana Bitcoin'da yapılan tüm işlemleri alıyorsunuz.


Blockchain'nin tamamını indirdikten sonra indeksleyici veritabanını sıkıştıracaktır. Bu işlem yaklaşık 12 saat sürer. İlerlemesini RoninUI'de "Dizinleyici" altında da takip edebilirsiniz.


RoninDojo düğümünüz bundan sonra tamamen işlevsel olacaktır:


![Indexer synchronized at 100% functional node](assets/22.webp)


Kullanıcı parolasını daha güçlü bir parola ile değiştirmek isterseniz, bunu şimdi "Ayarlar" sekmesinden yapabilirsiniz. RoninDojo'da, ek bir güvenlik Layer yoktur, bu yüzden gerçekten güçlü bir şifre seçmenizi ve yedeklemesine dikkat etmenizi öneririm.


## RoninDojo nasıl kullanılır?


Zincir indirildikten ve sıkıştırıldıktan sonra, yeni RoninDojo düğümünüzün sunduğu hizmetlerden yararlanmaya başlayabilirsiniz. Bunları nasıl kullanacağımızı görelim.


### Wallet yazılımının elektriğe bağlanması.


Yeni kurulan ve senkronize edilen düğümünüzün ilk faydası işlemlerinizi Bitcoin ağına yayınlamak olacaktır. Bu nedenle, muhtemelen farklı Wallet yönetim yazılımınızı buna bağlamak isteyeceksiniz.


Bunu Electrum Rust Server (electrs) kullanarak yapabilirsiniz. Uygulama normalde RoninDojo düğümünüze önceden yüklenmiştir. Değilse, RoninCLI Interface'den manuel olarak yükleyebilirsiniz.


Basitçe şuraya gidin: **Uygulamalar > Uygulamaları Yönet > Electrum Server'ı Yükle**


Electrum Sunucunuzun Tor Address'ünü almak için RoninCLI menüsünden şu adrese gidin:

**Kimlik Bilgileri > Electrs**


Wallet yazılımınıza .onion bağlantısını girmeniz yeterlidir. Örneğin, Sparrow wallet'te sekmeye gidin:

**Dosya > Tercihler > Sunucu**


Sunucu türünde, `Private Electrum` seçeneğini seçin, ardından ilgili alana Electrum Sunucunuzun Tor Address'sini girin. Son olarak, bağlantınızı test etmek ve kaydetmek için "Bağlantıyı Test Et" seçeneğine tıklayın.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Wallet yazılımının Samourai Dojo'ya bağlanması.


Electrs kullanmak yerine, uyumlu Software Wallet'unuzu RoninDojo düğümünüze bağlamak için Samourai Dojo'yu da kullanabilirsiniz. Örneğin, Samourai Wallet bu seçeneği sunar.


Bunu yapmak için Dojo'nuzun bağlantı QR kodunu taramanız yeterlidir. RoninUI'den erişmek için, "Dashboard" sekmesine ve ardından Dojo'nuzun kutusundaki "Manage" düğmesine tıklayın. Daha sonra Dojo'nuz ve BTC-RPC Explorer'ınız için bağlantı QR kodlarını görebileceksiniz. Bunları görüntülemek için "Değerleri göster" üzerine tıklayın.


![Retrieving the connection QR code to Dojo](assets/24.webp)


Samourai Wallet'nizi Dojo'nuza bağlamak için, uygulama kurulumu sırasında bu QR kodunu taramanız gerekecektir:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Kendi Mempool Explorer'ınızı kullanarak.


Bitcoin kullanıcıları için vazgeçilmez bir araç olan gezgin, Bitcoin zinciri hakkında çeşitli bilgileri kontrol etmenizi sağlar. Örneğin Mempool ile, kendi ücretinizi buna göre ayarlamak için diğer kullanıcılar tarafından uygulanan ücretleri gerçek zamanlı olarak kontrol edebilirsiniz. Ayrıca işlemlerinizden birinin onay durumunu kontrol edebilir veya bir Address'ün bakiyesini görüntüleyebilirsiniz.


Bu gezgin araçları sizi gizlilik risklerine maruz bırakabilir ve bir üçüncü tarafın veritabanına güvenmenizi gerektirebilir. Bu çevrimiçi aracı kendi düğümünüzden geçmeden kullandığınızda:



- Wallet'niz hakkında bilgi sızdırma riskiniz var.



- Barındırdıkları Proof-of-Work zinciri için web sitesi yöneticisine güveniyorsunuz.


Bu risklerden kaçınmak için Tor ağı üzerinden düğümünüzde kendi Mempool örneğinizi kullanabilirsiniz. Bu çözümle, yalnızca hizmeti kullanırken gizliliğinizi korumakla kalmaz, aynı zamanda kendi veritabanınızı sorguladığınız için artık bir sağlayıcıya güvenmeniz gerekmez.


Bunu yapmak için, RoninCLI'dan Mempool Space Visualizer'ı yükleyerek başlayın:


**Uygulamalar > Uygulamaları Yönet > Mempool Space Visualizer'ı Yükle**


Kurulduktan sonra, Mempool'ünüzün bağlantısını alın. Tor Address herhangi bir ağdan erişmenize izin verecektir. Benzer şekilde, bu bağlantıyı RoninCLI aracılığıyla alıyoruz:


**Kimlik Bilgileri > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Kendi verilerinize dayalı olarak kendi Mempool örneğinizin keyfini çıkarmak için Tor tarayıcısına Mempool Tor Address'inizi girmeniz yeterlidir. Daha hızlı erişim için bu Tor Address'i favorilerinize eklemenizi öneririm. Masaüstünüzde bir kısayol da oluşturabilirsiniz.


![Mempool Space interface](assets/27.webp)


Henüz Tor tarayıcısına sahip değilseniz, buradan indirebilirsiniz: https://www.torproject.org/download/


Tor Browser'ı yükleyerek ve aynı Address'yi girerek akıllı telefonunuzdan da erişebilirsiniz. Herhangi bir yerden, kendi düğümünüzü kullanarak Bitcoin zincirinin durumunu görüntüleyebilirsiniz.


### Whirlpool CLI kullanılıyor.


RoninDojo düğümünüz ayrıca Whirlpool karışımlarını otomatikleştirmek için uzak bir komut satırı Interface olan WhirlpoolCLI'yi de içerir.


Whirlpool uygulamasıyla bir CoinJoin gerçekleştirdiğinizde, miks ve remiksleri yürütmek için kullandığınız uygulamanın açık kalması gerekir. Whirlpool ile uygulamayı barındıran cihazın sürekli açık kalması gerektiğinden, bu işlem yüksek anon setlere sahip olmak isteyen kullanıcılar için sıkıcı olabilir. Pratik açıdan bu, UTXO'larınızı 7/24 remikslere dahil etmek istiyorsanız, kişisel bilgisayarınızı veya telefonunuzu uygulama açıkken sürekli açık tutmanız gerektiği anlamına gelir.


Bu kısıtlamaya bir çözüm, Bitcoin düğümü gibi sürekli açık olması amaçlanan bir makinede WhirlpoolCLI kullanmaktır. Bu sayede UTXO'larımız, Bitcoin düğümümüz dışında başka bir makineyi çalışır durumda tutmaya gerek kalmadan 7/24 yeniden karıştırılabilir.

WhirlpoolCLI, Coinjoins'in kolay yönetimi için kişisel bir bilgisayara kurulacak grafiksel bir Interface olan WhirlpoolGUI ile birlikte kullanılır. Bu makalede Whirlpool CLI'i kendi dojonuzla nasıl kuracağınızı ayrıntılı olarak açıklayacağım: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


Genel olarak CoinJoin hakkında daha fazla bilgi edinmek için bu makalede her şeyi açıklıyorum: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Whirlpool İstatistik Aracını Kullanma.


Whirlpool ile CoinJoins gerçekleştirdikten sonra, karışık UTXO'larınızın gerçek gizlilik seviyesini bilmek isteyebilirsiniz. Whirlpool Stat Tool bunu kolayca yapmanızı sağlar. Bu araçla, karma UTXO'larınızın ileriye dönük puanını ve geriye dönük puanını hesaplayabilirsiniz. Bu Anon Setlerinin hesaplanması ve nasıl çalıştıkları hakkında daha fazla bilgi edinmek için bu bölümü okumanızı tavsiye ederim: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


Araç RoninDojo'nuza önceden yüklenmiştir. Şimdilik sadece RoninCLI'dan kullanılabilir. Ana menüden başlatmak için şu adrese gidin:

**Samourai Araç Seti > Whirlpool İstatistik Aracı**


Kullanım talimatları görünecektir. Bitirdiğinizde, komut satırlarına erişmek için herhangi bir tuşa basın:


![Whirlpool Stats Tool software home](assets/28.webp)


Terminal görüntülenecektir:

**wst#/tmp>**


Bu Interface'den çıkmak ve RoninCLI menüsüne dönmek için komutu girmeniz yeterlidir:

```
quit
```


Başlamak için, OXT verilerini tam gizlilikle çıkarmak için Tor'da proxy ayarlayacağız. Komutu girin:

```
socks5 127.0.0.1:9050
```


Ardından işleminizi içeren havuzdan verileri indirin:

```
download 0001
```


**Not:** `0001` yerine sizi ilgilendiren havuz mezhep kodunu yazın.


Mezhep kodları WST'de aşağıdaki gibidir:



- Havuz 0,5 bitcoin: 05
- Havuz 0,05 bitcoin: 005
- Havuz 0.01 bitcoin: 001
- Havuz 0.001 bitcoin: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Veriler indirildikten sonra, komutla yükleyin:

```
load 0001
```


**Not:** `0001` yerine sizi ilgilendiren havuz mezhep kodunu yazın.


![Loading data from pool 0001](assets/30.webp)

Yükleme işleminin gerçekleşmesine izin verin, birkaç dakika sürebilir. Verileri yükledikten sonra, Anon Setlerini elde etmek için score komutunu ve ardından txid (işlem tanımlayıcınızı) yazın:

```
score TXID
```


**Not:** `txid` yerine işleminizin tanımlayıcısını yazın.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST daha sonra geriye dönük skoru (Geriye dönük metrikler) ve ardından ileriye dönük skoru (İleriye dönük metrikler) görüntüleyecektir. Anon setlerinin puanlarına ek olarak, WST size anon setine dayalı olarak havuzdaki çıktınızın yayılma oranını da sağlar.


Lütfen UTXO'inizin ileriye dönük puanının son karışımınıza göre değil, ilk karışımınızın txid'sine göre hesaplandığını unutmayın. Tersine, bir UTXO'in geriye dönük puanı, son döngünün txid'sine göre hesaplanır.


Bir kez daha, Anon Setlerinin bu kavramlarını anlamadıysanız, CoinJoin ile ilgili makalemin her şeyi diyagramlarla ayrıntılı olarak açıkladığım bu bölümünü okumanızı tavsiye ederim: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### Boltzmann hesap makinesini kullanarak.


Boltzmann hesaplayıcı, entropi seviyesi de dahil olmak üzere bir Bitcoin işlemi üzerinde çeşitli gelişmiş ölçümleri kolayca hesaplamanıza olanak tanıyan bir araçtır. Tüm bu veriler, bir işlemin gizlilik düzeyini ölçmenize ve olası hataları tespit etmenize olanak tanır. Bu araç RoninDojo düğümünüze önceden yüklenmiştir.


RoninCLI'dan erişmek için SSH ile bağlanın, ardından menüye gidin:

**Samourai Toolkit > Boltzmann Hesaplayıcı**


RoninDojo'da nasıl kullanılacağını açıklamadan önce, bu metriklerin neyi temsil ettiğini, nasıl hesaplandıklarını ve ne için kullanıldıklarını açıklayacağım.


Bu göstergeler herhangi bir Bitcoin işlemi için kullanılabilir, ancak bir CoinJoin işleminin kalitesini incelemek için özellikle ilginçtirler.


1. Bu yazılım tarafından hesaplanan ilk gösterge olası kombinasyonların sayısıdır. Hesap makinesinde "nb kombinasyonları" olarak belirtilir. UTXO'ların değerleri göz önüne alındığında, bu gösterge girişlerden çıkışlara olası eşlemelerin sayısını temsil eder.


**Not:** `UTXO` terimine aşina değilseniz, bu kısa makaleyi okumanızı tavsiye ederim:


> Bir Bitcoin işleminin mekanizması: UTXO, girdiler ve çıktılar.

Başka bir deyişle, bu gösterge belirli bir işlem için olası yorumların sayısını temsil eder. Örneğin, bir Whirlpool 5x5 CoinJoin yapısı 1496'ya eşit sayıda olası kombinasyona sahip olacaktır:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Kredi: KYCP


2. Hesaplanan ikinci gösterge bir işlemin entropisidir. Bir işlem için olası kombinasyonların sayısı çok yüksek olabileceğinden, bunun yerine entropi kullanılması tercih edilebilir. Entropi, olası kombinasyon sayısının ikili logaritmasını temsil eder. Formülü aşağıdaki gibidir:



- E: işlemin entropisi.
- C: işlem için olası kombinasyon sayısı.


**E = log2(C)**


Matematikte ikili logaritma (2 tabanı), 2'nin kuvveti fonksiyonunun ters fonksiyonudur. Başka bir deyişle, x'in ikili logaritması, x değerini elde etmek için 2 sayısının yükseltilmesi gereken kuvvettir.


Böylece:


**E = log2(C)**


**C = 2^E**


Bu gösterge bit cinsinden ifade edilir. Örneğin, burada daha önce belirtilen olası kombinasyon sayısı 1496'ya eşit olan bir Whirlpool 5x5 CoinJoin işleminin entropisinin hesaplanması yer almaktadır:


**C = 1496**


**E = log2(1496)**


**E = 10,5469 bit**


Dolayısıyla, bu CoinJoin işleminin entropisi 10,5469 bittir ve bu çok iyidir.


Bu gösterge ne kadar yüksekse, işlemin o kadar farklı yorumu vardır ve dolayısıyla işlem o kadar gizlidir.


Başka bir örnek verelim. Burada bir girişi ve iki çıkışı olan "klasik" bir işlem var:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Kredi: OXT


Bu işlemin tek bir olası yorumu vardır:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Bu yüzden entropisi 0'a eşit olacaktır:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. Boltzmann hesaplayıcısı tarafından döndürülen üçüncü gösterge, "Wallet Verimliliği" olarak adlandırılan Tx'in verimliliğidir. Bu gösterge basitçe girdi işleminin aynı konfigürasyonda mümkün olan en iyi işlemle karşılaştırılmasını sağlar.


Şimdi, belirli bir işlem yapısı için elde edilebilecek en yüksek entropiyi temsil eden maksimum entropi kavramını tanıtacağız. Örneğin, bir Whirlpool 5x5 CoinJoin yapısı 10.5469 maksimum entropiye sahip olacaktır. Verimlilik göstergesi bu maksimum entropiyi girdi işleminin gerçek entropisi ile karşılaştırır. Formülü aşağıdaki gibidir:



- ER: Bit cinsinden ifade edilen gerçek entropi.
- EM: Bit cinsinden ifade edilen aynı yapıya sahip maksimum entropi.
- Ef: Bit cinsinden ifade edilen verimlilik.


**Ef = ER - EM**


**Ef = 10.5469 - 10.5469**


**Ef = 0 bit**


Bu gösterge aynı zamanda yüzde olarak da ifade edildiğinden formül şöyle olur:



- CR: Olası kombinasyonların gerçek sayısı.
- CM: Aynı yapıya sahip olası kombinasyonların maksimum sayısı.
- Ef: Yüzde olarak ifade edilen verimlilik.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = %100**


100 verimlilik, bu işlemin yapısına göre mümkün olan en yüksek gizliliğe sahip olduğu anlamına gelir.


4. Hesaplanan dördüncü gösterge entropi yoğunluğudur. Entropiyi her bir girdi veya çıktı ile ilişkilendirmemizi sağlar. Bu gösterge, farklı boyutlardaki işlemler arasındaki verimliliği karşılaştırmak için kullanılabilir.


Hesaplaması çok basittir: işlemin entropisini mevcut giriş ve çıkışların sayısına böleriz. Örneğin, bir Whirlpool 5x5 CoinJoin için şunu elde ederiz:


ED: Bit cinsinden ifade edilen entropi yoğunluğu.

E: Bit cinsinden ifade edilen işlem entropisi.

T: İşlemdeki toplam girdi ve çıktı sayısı.


T = 5 + 5 = 10

ED = E / T

ED = 10.5469 / 10

ED = 1,054 bit


Boltzmann hesaplayıcısı tarafından sağlanan beşinci bilgi parçası, girdiler ve çıktılar arasındaki bağlantıların olasılık tablosudur. Bu tablo size basitçe belirli bir girdinin belirli bir çıktıya karşılık gelme olasılığını (Boltzmann skoru) verir.


Örneğimizi bir Whirlpool CoinJoin ile ele alırsak, olasılık tablosu şöyle olacaktır:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Burada her bir girdinin her bir çıktıya bağlanma olasılığının eşit olduğunu görebiliriz.


Ancak, bir girdi ve iki çıktıya sahip bir işlem örneğini ele alırsak, şöyle görünecektir:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

Bu örnekte, her bir çıktının 0 girişinden gelme olasılığının %100 olduğunu görebiliriz.


Bu olasılık ne kadar düşükse, gizlilik seviyesi de o kadar yüksek olur.


6. Hesaplanan altıncı bilgi deterministik bağlantıların sayısıdır. Deterministik bağlantıların oranı da sağlanacaktır. Bu gösterge, söz konusu işlemin girdileri ve çıktıları arasında %100 olasılığa sahip, yani inkar edilemez olan bağlantıların sayısını vurgular.


Oran, toplam bağlantı sayısına kıyasla işlemdeki deterministik bağlantı sayısını gösterir.


Örneğin, bir CoinJoin Whirlpool işleminin girdiler ve çıktılar arasında hiçbir deterministik bağlantısı yoktur. Gösterge sıfır olacak ve oran da %0 olacaktır.


Ancak, incelenen ikinci işlem (1 girdi ve 2 çıktı) için gösterge 2 ve oran %100'dür.


Dolayısıyla, bu göstergenin sıfır olması iyi bir gizliliğe işaret eder.


Şimdi göstergeleri incelediğimize göre, bu yazılımı kullanarak bunları nasıl hesaplayacağımızı görelim. RoninCLI'dan menüye gidin:

**Samourai Toolkit > Boltzmann Hesaplayıcı**


![Boltzmann Calculator software homepage](assets/35.webp)


Yazılım başlatıldığında, incelemek istediğiniz transaction ID'i girin. Birden fazla işlemi virgülle ayırarak aynı anda girebilir ve ardından enter tuşuna basabilirsiniz:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Hesap makinesi daha sonra daha önce gördüğümüz tüm göstergeleri geri getirecektir:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Yazılımdan çıkmak ve RoninCLI menüsüne dönmek için "Quit" komutunu yazın.


Boltzmann hesap makinesi hakkında daha fazla bilgi edinmek için bu makaleleri okumanızı tavsiye ederim:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Bisq'e bağlanıyor.


Bisq, bitcoin alıp satmanızı sağlayan eşler arası bir Exchange platformudur. Tor üzerinde çalışan bir masaüstü yazılımı ile kullanılır ve kimliğinizi vermenize gerek kalmadan Exchange bitcoin almanızı sağlar.

Bisq, 2/2 çoklu imza sistemi aracılığıyla eşler arası alışverişleri güvence altına alır. Borsalarınızın gizliliğini optimize etmek ve kendi düğümünüzün Blockchain'sinden gelen verilere güvenmek için bu yazılımı kendi RoninDojo düğümünüzle kullanabilirsiniz.


Bisq yazılımını indirmek için resmi web sitesine gidin: https://bisq.network/


Yazılımı kullanmaya başlamak için şu sayfayı okumanızı tavsiye ederim: https://bisq.network/getting-started/


RoninDojo'nuzdan bağlantı bağlantısını almak için SSH üzerinden RoninCLI'ya bağlanmanız gerekecektir. Ardından menüye gidin:

**Uygulamalar > Uygulamaları Yönet**


Parolanızı girin, ardından boşluk tuşuyla kutuyu işaretleyin:

**[ ] Bisq Bağlantısını Etkinleştir**


Seçiminizi onaylayın. Düğümünüzün yüklenmesine izin verin, ardından Tor V3 Address'i şuradan alın:

**Kimlik Bilgileri > bitcoind**


Address'yi "Bitcoin daemon" altına kopyalayın.


bitcoind Tor V3 Address'nızı RoninUI Interface'ten "Dashboard" üzerindeki "Bitcoin core" kutusundaki "Manage" seçeneğine tıklayarak da alabilirsiniz:


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Düğümünüzü Bisq'ten bağlamak için menüye gidin:

**Ayarlar > Ağ Bilgisi**


![Access the node connection interface from the Bisq software](assets/39.webp)


"Özel Bitcoin core düğümlerini kullan" balonuna tıklayın. Ardından Bitcoin TorV3 Address'inizi ".onion" ile ancak "http://" olmadan belirtilen kutuya girin.


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Bisq yazılımını yeniden başlatın. Düğümünüz artık Bisq'inize bağlanmıştır.


### Diğer özellikler.


RoninDojo düğümünüz diğer temel özellikleri de içerir. Dikkate alındığından emin olmak için belirli bilgileri tarama olanağına sahipsiniz.


Örneğin, bazen RoninDojo'nuza bağlı Wallet'inizin size ait bitcoinleri bulamaması mümkündür. Bu Wallet'de Bitcoin'unuz olduğundan emin olmanıza rağmen bakiye 0'dır. Türetme yollarındaki bir hata da dahil olmak üzere dikkate alınması gereken birçok olası neden vardır ve bunların arasında düğümünüzün adreslerinizi gözlemlememesi de mümkündür.


Bunu düzeltmek için, düğümünüzün xpub'ınızı "xpub aracı" ile takip edip etmediğini kontrol edebilirsiniz. RoninUI'den erişmek için menüye gidin:

**Bakım > XPUB Aracı**


Sorunlu xpub'ı girin ve bu bilgileri doğrulamak için "Kontrol Et "e tıklayın.


![XPUB Tool from RoninUI](assets/41.webp)


Eğer xpub'ınız düğüm tarafından takip ediliyorsa, bunun göründüğünü göreceksiniz:


![XPUB Tool result showing successful analysis](assets/42.webp)


Tüm işlemlerin doğru göründüğünü kontrol edin. Ayrıca, türetme türünün Wallet'nizinkiyle eşleştiğini doğrulayın. Burada düğümün bu xpub'ı bir BIP44 türetme olarak yorumladığını görebiliriz. Bu türetme türü Wallet'nizinkiyle eşleşmiyorsa, "Yeniden Yaz" düğmesine tıklayın, ardından seçiminize göre BIP44/BIP49/BIP84'ü seçin:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Xpub'ınız düğümünüz tarafından izlenmiyorsa, sizi içe aktarmaya davet eden bu ekranı göreceksiniz:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Diğer bakım araçlarını da kullanabilirsiniz:



- İşlem Aracı: Belirli bir işlemin ayrıntılarını gözlemlemenizi sağlar.
- Address Aracı: Belirli bir Address'ün Dojo'nuz tarafından izlendiğini doğrulamanızı sağlar.
- Blokları Yeniden Tara: Düğümünüzü seçilen bir blok aralığını yeniden taramaya zorlar.


Ayrıca RoninUI üzerinde "Push Tx" aracını da bulacaksınız. Bitcoin ağına imzalı bir işlem yayınlamanızı sağlar. Onaltılık formatta girilmelidir:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Sonuç.


RoninDojo adlı bu harika aracı nasıl kuracağımızı ve kullanmaya başlayacağımızı gördük. Kendi Bitcoin düğümünüzü çalıştırmak için mükemmel bir seçimdir. Bir Bitcoiner için gerekli tüm araçları entegre eden ve güncel tutan istikrarlı bir çözümdür.


Terminal kullanmak sizi korkutmuyorsa ve Lightning Network ile ilgili araçlara ihtiyacınız yoksa, RoninDojo size hitap edebilir.


Eğer yapabiliyorsanız, bu açık kaynaklı yazılımları sizin için özgürce üreten geliştiricilere bağış yapmayı düşünün: https://donate.ronindojo.io/


RoninDojo hakkında daha fazla bilgi edinmek için aşağıdaki harici kaynaklarımdaki bağlantılara göz atmanızı tavsiye ederim.


### Daha fazla okuma:



- CoinJoin'yi Bitcoin üzerinde anlama ve kullanma.
- Hash fonksiyonlar - Bitcoin Démocratisé 1 adlı e-kitaptan alıntıdır.
- Bitcoin passphrase hakkında bilmeniz gereken her şey.


### Dış kaynaklar:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/