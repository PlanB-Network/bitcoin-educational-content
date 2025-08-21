---
name: RoninDojo v2
description: RoninDojo v2 Bitcoin düğümünüzü bir Raspberry Pi'ye yükleme
---
![cover RoninDojo v2](assets/cover.webp)


***UYARI:** Samourai Wallet'nin kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, RoninDojo'nun Whirlpool gibi bazı özellikleri artık çalışmıyor. Bununla birlikte, bu araçların önümüzdeki haftalarda eski haline getirilmesi veya farklı bir şekilde yeniden başlatılması mümkündür. Ayrıca, RoninDojo kodu Samourai'nin GitLab'ında barındırıldığından ve bu GitLab'a da el konulduğundan, kodu uzaktan indirmek şu anda mümkün değil. RoninDojo ekipleri muhtemelen kodu yeniden yayınlamak için çalışıyorlar.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> Bitcoin'ü gizlilikle kullanın.

Önceki bir eğitimde, RoninDojo v1'i kurma ve kullanma prosedürünü zaten açıklamıştık. Ancak, geçen yıl RoninDojo ekipleri, yazılımın mimarisinde önemli bir dönüm noktası olan uygulamalarının 2. sürümünü yayınladılar. Gerçekten de, Debian lehine Linux Manjaro dağıtımından uzaklaştılar. Sonuç olarak, artık Raspberry Pi'ye otomatik kurulum için önceden yapılandırılmış bir görüntü sunmuyorlar. Ancak manuel kurulumla devam etmek için hala bir yöntem var. Ben kendi node'um için bu yöntemi kullandım ve o zamandan beri RoninDojo v2 Raspberry Pi 4'ümde harika bir şekilde çalışıyor. Bu nedenle, RoninDojo v2'nin Raspberry Pi'ye manuel olarak nasıl kurulacağına dair yeni bir eğitim sunuyorum.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## İçindekiler:


- RoninDojo nedir?
- RoninDojo v2'yi yüklemek için hangi donanımı seçmeliyim?
- Raspberry Pi 4 nasıl monte edilir?
- Raspberry Pi 4 üzerine RoninDojo v2 nasıl kurulur?
- RoninDojo v2 düğümünüzü nasıl kullanabilirsiniz?


## RoninDojo nedir?

Dojo başlangıçta Bitcoin'e dayanan ve Samourai Bitcoin core ekipleri tarafından geliştirilen tam bir Wallet düğüm uygulamasıdır. Bu çözüm herhangi bir ekipmana kurulabilir. Diğer Çekirdek uygulamalarının aksine Dojo, Samourai Wallet'nın Android uygulama ortamıyla entegre olacak şekilde özel olarak optimize edilmiştir. RoninDojo ise bir Dojo'nun ve diğer çeşitli tamamlayıcı araçların kurulumunu ve yönetimini kolaylaştırmak için tasarlanmış bir yardımcı programdır. Kısacası RoninDojo, kurulumunu ve yönetimini basitleştirirken çok sayıda ek aracı entegre ederek Dojo'nun temel uygulamasını zenginleştirir.


Ronin ayrıca "*Tanto*" olarak adlandırılan [kutu içinde düğüm çözümü] (https://ronindojo.io/en/products), RoninDojo'nun kendi ekipleri tarafından bir araya getirilmiş bir sisteme zaten yüklenmiş olduğu bir cihaz sunmaktadır. Tanto ücretli bir seçenektir ve teknik komplikasyonlardan kaçınmayı tercih edenler için ilginç olabilir. Ancak RoninDojo'nun kaynak kodu açık olduğundan, kendi donanımınıza yerleştirmek de mümkündür. Daha ekonomik olan bu alternatif, yine de bu eğitimde ele alacağımız bazı ek manipülasyonlar gerektirir.

RoninDojo bir Dojo'dur, bu nedenle mümkün olan en iyi CoinJoin deneyimini sağlamak için Whirlpool CLI'un Bitcoin düğümünüze kolayca entegre edilmesini sağlar. Whirlpool CLI ile, kişisel bilgisayarınızın açık kalmasına gerek kalmadan, haftanın 7 günü, günün 24 saati bitcoinlerinizi sürekli olarak yeniden karıştırmak mümkün hale gelir.


RoninDojo, Whirlpool CLI'ün ötesinde Dojo'nuzun işlevlerini geliştirmek için çeşitli araçlar içerir. Bunlar arasında Boltzmann hesap makinesi işlemlerinizin gizlilik seviyesini analiz eder, Electrum sunucusu Bitcoin cüzdanlarınızın node'unuza bağlanmasına izin verir ve Mempool sunucusu işlemlerinizi bilgi sızdırmadan yerel olarak görüntülemenizi sağlar.


Umbrel gibi diğer node çözümleriyle karşılaştırıldığında, RoninDojo açıkça On-Chain çözümlerine ve gizlilik araçlarına odaklanmıştır. Umbrel'in aksine, RoninDojo bir Lightning düğümü kurmayı veya daha genel sunucu uygulamalarının entegrasyonunu desteklemez. RoninDojo, Umbrel'den daha az çok yönlü araç sunmasına rağmen, On-Chain etkinliğinizi yönetmek için gerekli tüm işlevlere sahiptir.


Umbrel tarafından sunulan genel işlevlere veya Lightning Network ile ilgili işlevlere ihtiyacınız yoksa ve Whirlpool veya Mempool gibi temel araçlara sahip basit, kararlı bir düğüm arıyorsanız, RoninDojo ideal çözüm olabilir. Umbrel, Lightning Network ve çok yönlülüğe yönelik mini bir çoklu görev sunucusu olma eğilimindeyken, RoninDojo, Samourai Wallet felsefesine uygun olarak, kullanıcı gizliliği için temel araçlara odaklanmaktadır.


Şimdi RoninDojo'nun ana hatlarını belirlediğimize göre, bu düğümü nasıl kuracağımızı birlikte görelim.


## RoninDojo v2'yi yüklemek için hangi donanımı seçmeliyim?

RoninDojo, yazılımının [RockPro64] (https://ronindojo.io/en/download) üzerine otomatik kurulumu için bir görüntü sunmaktadır. Ancak, bizim eğitimimiz Raspberry Pi 4'e manuel kurulum prosedürüne odaklanmaktadır. Raspberry Pi 5 yakın zamanda piyasaya sürülmüş olmasına ve bu öğreticinin teorik olarak bu yeni modelle uyumlu olması gerekmesine rağmen, henüz kişisel olarak test etme şansım olmadı ve topluluktan herhangi bir geri bildirim bulamadım. Pi 5'i ve uyumlu bileşenleri edinir edinmez, sizi bilgilendirmek için bu öğreticiyi güncelleyeceğim. Bu arada, benim node'umda mükemmel çalıştığı için Pi 4'e öncelik vermenizi öneririm.

Kendi adıma, RoninDojo'yu 8 GB RAM ile donatılmış bir Raspberry Pi üzerinde çalıştırıyorum. Bazı topluluk üyeleri yalnızca 4 GB RAM'e sahip cihazlarda çalıştırmayı başarmış olsa da, bu yapılandırmayı kendim test etmedim. Aradaki küçük fiyat farkı göz önüne alındığında, 8 GB RAM versiyonunu tercih etmek akıllıca görünüyor. Bu, Raspberry Pi'nizi gelecekte başka kullanımlar için yeniden kullanmayı planlıyorsanız da yararlı olabilir.

RoninDojo ekiplerinin kasa ve SSD adaptörü ile ilgili sık sık sorunlar bildirdiğini belirtmek önemlidir. Bu sorunlarla ben de karşılaştım. **Bu nedenle, düğümünüzün SSD'si için bir USB kablosuyla donatılmış kasalardan kaçınmanız şiddetle tavsiye edilir.** Bunun yerine, Raspberry Pi'niz için özel olarak tasarlanmış bir depolama genişletme kartını tercih edin:


![storage expansion card RPI4](assets/notext/1.webp)


Bitcoin Blockchain'yi depolamak için seçtiğiniz depolama genişletme kartıyla uyumlu bir SSD'ye ihtiyacınız olacaktır. Şu anda (Şubat 2024) bir geçiş aşamasındayız. Birkaç ay içinde 1 TB disklerin, özellikle düğümünüze entegre etmeyi planladığınız çeşitli uygulamalar göz önüne alındığında, Blockchain'nin büyüyen boyutunu içermek için artık yeterli olmayacağı beklenmektedir. Bu nedenle bazıları uzun vadede içinizin rahat etmesi için 2 TB SSD'ye yatırım yapmanızı önermektedir. Ancak SSD fiyatlarının yıldan yıla düşme eğilimi göstermesi nedeniyle bazıları da 1 TB'lık bir diskin bir ya da iki yıl için yeterli olacağını ve bu disk eskidiğinde 2 TB'lık modellerin maliyetinin muhtemelen düşmüş olacağını savunmaktadır. Dolayısıyla seçim kişisel tercihlerinize bağlıdır. RoninDojo'nuzu uzun bir süre kullanmayı planlıyorsanız ve önümüzdeki yıllarda herhangi bir teknik işlemden kaçınmak istiyorsanız, 2 TB SSD seçeneği size gelecek için rahat bir marj sunduğundan en ihtiyatlı seçenek gibi görünmektedir.


Buna ek olarak, çeşitli küçük bileşenlere ihtiyacınız olacaktır:


- Raspberry Pi'nizi ve depolama genişletme kartınızı barındırmak için bir fan ile donatılmış bir kasa. Hem SSD genişletme kartını hem de uyumlu bir kasayı içeren kitler çevrimiçi olarak mevcuttur;
- Raspberry Pi'niz için bir güç kablosu;
- En az 16 GB'lık bir mikro SD kart (8 GB teknik olarak yeterli olsa da, 8 ve 16 GB kartlar arasındaki fiyat farkı genellikle ihmal edilebilir düzeydedir);
- Ağ bağlantısı için bir RJ45 Ethernet kablosu.


![node material](assets/notext/2.webp)


## Raspberry Pi 4 nasıl monte edilir?

Node'unuzun montajı, seçilen donanıma, özellikle de kasanın türüne bağlı olarak değişecektir. Bununla birlikte, montajda izlenecek adımların genel hatları genellikle benzer kalır.

Arka taraftaki iki kilitleme vidasını sabitlemeye dikkat ederek SSD'nizi depolama genişletme kartına takarak başlayın.


![assembly1](assets/notext/3.webp)


Ardından Raspberry Pi'nizi genişleme kartına takın.


![assembly2](assets/notext/4.webp)


Ayrıca, fanı Raspberry Pi'ye takın.


![assembly3](assets/notext/5.webp)


Kasanızın kılavuzuna bakarak doğru pinleri kullanmaya dikkat ederek çeşitli bileşenleri bağlayın. Kasa üreticileri genellikle montajda size yardımcı olacak video eğitimleri sunarlar. Benim durumumda, açma/kapama düğmesi ile donatılmış ek bir genişletme kartım var. Bu bir Bitcoin düğümü yapmak için gerekli değildir. Esas olarak bir güç düğmesine sahip olmak için kullanıyorum.


Eğer siz de benim gibi açma/kapama düğmesi olan bir genişleme kartına sahipseniz, küçük "Otomatik Açma" jumper'ını takmayı unutmayın. Bu, düğümünüzün açılır açılmaz otomatik olarak başlamasını sağlayacaktır. Bu özellik özellikle elektrik kesintisi durumunda kullanışlıdır, çünkü düğümünüzün sizin manuel müdahalenize gerek kalmadan kendi kendine yeniden başlamasını sağlar.


![assembly4](assets/notext/6.webp)


Tüm donanımı kasaya yerleştirmeden önce, Raspberry Pi'nizin, depolama genişletme kartının ve fanın düzgün çalışıp çalışmadığını kontrol etmeniz önemlidir.


![assembly5](assets/notext/7.webp)


Son olarak, Raspberry Pi'nizi kutusuna yerleştirin. Unutmayın, daha sonraki bir adımda mikro SD kartı Raspberry Pi üzerindeki uygun porta takmanız gerekecektir. Eğer kılıfınızda SD kartı açmak zorunda kalmadan takmanıza izin veren bir açıklık varsa (fotoğrafta gösterilen benimkinde olduğu gibi), şimdi kılıfı kapatmaya devam edebilirsiniz. Ancak, kasanızın mikro SD portuna doğrudan erişimi yoksa, montajı tamamlamadan önce mikro SD kartı takmak için hazırlayana kadar beklemeniz gerekecektir.


![assembly6](assets/notext/8.webp)


## Raspberry Pi 4 üzerine RoninDojo v2 nasıl kurulur?


### Adım 1: Önyüklenebilir mikro SD'yi hazırlayın

Donanımınızı monte ettikten sonra, bir sonraki adım RoninDojo'yu kurmaktır. Bunun için, bilgisayarınızdan önyüklenebilir bir mikro SD kart hazırlayacağız, uygun disk görüntüsünü üzerine yazarak.

Raspberry Pi ile kullanılmak üzere mikro SD karta işletim sistemi indirmeyi, yapılandırmayı ve yazmayı kolaylaştırmak için tasarlanmış _**Raspberry Pi Imager**_ yazılımını kullanmanız gerekecektir. Bu yazılımı kişisel bilgisayarınıza kurarak başlayın:


- Ubuntu/Debian için: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Windows için: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Mac için: https://downloads.raspberrypi.org/imager/imager_latest.dmg


Yazılım yüklendikten sonra açın ve mikro SD kartınızı kişisel bilgisayarınıza takın. Raspberry Pi Imager Interface'ten `İşletim Sistemi Seç` seçeneğini seçin:


![choose OS](assets/notext/9.webp)


Ardından, `Raspberry Pi OS (diğer)` menüsüne gidin:


![choose OS others](assets/notext/10.webp)


Boyut olarak `0.3 GB` olan `Raspberry Pi OS (Legacy, 64-bit) Lite` isimli işletim sistemini seçin:


![choose OS Legacy Lite](assets/notext/11.webp)


İşletim sistemini seçtikten sonra, Raspberry Pi Imager'ın ana menüsüne yönlendirileceksiniz. DEPOLAMA SEÇ` seçeneğine tıklayın:


![choose storage](assets/notext/12.webp)


Mikro SD kartınızı seçin:


![choose micro sd](assets/notext/13.webp)


İşletim sistemini ve mikro SD kartı seçtikten sonra `NEXT` üzerine tıklayın:


![choose next](assets/notext/14.webp)


Yeni bir pencere açılacaktır. KONFİGÜRASYONU DÜZENLE'yi seçin:


![edit settings](assets/notext/15.webp)


Bu pencerede `GENERAL` sekmesine gidin ve aşağıdaki ayarları yapın (çalışması için çok önemlidir):


- Seçeneği etkinleştirin ve ana bilgisayar adı olarak `RoninDojo` atayın;
- Kullanıcı adı ve parola belirle` seçeneğini etkinleştirin, kullanıcı adı olarak `pi` girin, bir parola seçin ve daha sonra gerekeceği için bu bilgileri not edin. Bu kimlik bilgileri geçicidir ve daha sonra silinecektir;
- Wi-Fi'yi Yapılandır'ı devre dışı bırakın;
- Yerel ayarları ayarla` seçeneğini etkinleştirin ve saat diliminizin yanı sıra bilgisayarınıza karşılık gelen klavye türünü seçin;


![general settings](assets/notext/16.webp)


SERVİSLER sekmesinde, `SSH`yi etkinleştir` kutusuna tıklayın ve `Kimlik doğrulama için bir parola kullan` seçeneğini seçin:


![services settings](assets/notext/17.webp)


Ayrıca, `OPTIONS` sekmesinde telemetrinin devre dışı bırakıldığından emin olun:


![options settings](assets/notext/18.webp)


`KAYDET` üzerine tıklayın:


![settings save](assets/notext/19.webp)

Önyüklenebilir mikro SD kartı oluşturmaya başlamak için `Evet` seçeneğine tıklayarak onaylayın:

![settings yes](assets/notext/20.webp)


Bir mesaj size mikro SD karttaki tüm verilerin silineceğini bildirecektir. İşlemi başlatmak için `EVET` üzerine tıklayarak onaylayın:


![overwrite micro SD](assets/notext/21.webp)


Yazılım mikro SD kartınızı hazırlamayı bitirene kadar bekleyin:


![writing micro SD](assets/notext/22.webp)


İşlemin sonunu belirten mesaj göründüğünde, mikro SD kartı bilgisayarınızdan çıkarabilirsiniz:


![writing micro SD completed](assets/notext/23.webp)


### Adım 2: Düğüm Montajını Tamamlayın

Artık mikro SD kartı Raspberry Pi'nizin uygun portuna takabilirsiniz.


![micro SD](assets/notext/24.webp)


Ardından Ethernet kablosunu kullanarak Raspberry Pi'nizi yönlendiricinize bağlayın. Son olarak, güç kablosunu bağlayarak ve güç düğmesine basarak düğümünüzü açın (kurulumunuzda varsa).


### Adım 3: Düğüm ile SSH Bağlantısı Kurun

İlk olarak, düğümünüzün IP Address'ini bulmak gerekir. Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ veya _[Angry IP Scanner](https://angryip.org/)_ gibi bir araç kullanma veya yönlendiricinizin yönetim Interface'ünü kontrol etme seçeneğiniz vardır. IP Address `192.168.1.??` şeklinde olmalıdır. **Aşağıdaki tüm komutlar için `[IP]` yerine düğümünüzün** gerçek IP Address'ini yazın (parantezleri kaldırın).


Bir terminal başlatın.


Düğümünüzün IP Address'sı ile zaten ilişkili olan olası bir anahtarı kaldırmak için komutu çalıştırın:

`ssh-keygen -R [IP]`.


Bu komutu takip eden bir hata ciddi değildir; sadece anahtarın bilinen ana bilgisayarlar listenizde bulunmadığı anlamına gelir (ki bu oldukça muhtemeldir). Örneğin, düğümünüzün IP adresi `192.168.1.40` ise, komut şöyle olur: `ssh-keygen -R 192.168.1.40`.


Ardından, komutu çalıştırarak düğümünüzle bir SSH bağlantısı kurun:

`ssh pi@[IP]`.

Ana bilgisayarın orijinalliği ile ilgili bir mesaj görüntülenecektir: `The authenticity of host '[IP]' can't be established.` Bu, bağlanmaya çalıştığınız cihazın orijinalliğinin bilinen bir genel anahtarın olmaması nedeniyle doğrulanamadığını gösterir. SSH aracılığıyla yeni bir ana bilgisayara ilk kez bağlanırken, bu mesaj her zaman görünecektir. Açık anahtarı yerel dizininize eklemek için `evet` yanıtını vermelisiniz, böylece bu düğüme yapılacak sonraki SSH bağlantılarında bu uyarı mesajının görünmesini engellemiş olursunuz. Bu nedenle, `evet` yazın ve doğrulamak için `enter` tuşuna basın.

Ardından, daha önce 1. adımda geçici olarak ayarlanmış olan şifrenizi girmeniz istenecektir. Enter` ile doğrulayın. Daha sonra SSH aracılığıyla düğümünüze bağlanacaksınız.


Özetle, çalıştırılacak komutlar şunlardır:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- "Evet
- Geçici parolayı girin ve doğrulayın.


### Adım 4: Güncelleme ve Hazırlık

Artık düğümünüze bir SSH oturumu aracılığıyla bağlısınız. Terminalinizde komut istemi şu şekilde olmalıdır: `pi@RoninDojo:~ $`. Başlamak için, aşağıdaki komutla mevcut paketlerin listesini güncelleyin ve mevcut paketler için güncellemeleri yükleyin:

`sudo apt update && sudo apt upgrade -y`


Güncellemeler tamamlandıktan sonra, komutu kullanarak *Git* ve *Dialog* yüklemeye devam edin:

`sudo apt install git dialog -y`


Ardından, _RoninOS_ Git deposunun `master` dalını çalıştırarak klonlayın:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Komutu ile `customize-image.sh` betiğini çalıştırın:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Komut dosyasının kesintisiz çalışmasına izin vermek ve yaklaşık 10 dakika süren işleminin** bitmesini sabırla beklemek önemlidir. Kurulum tamamlandı mesajı göründüğünde, bir sonraki adıma geçebilirsiniz.


### Adım 5: RoninOS'un Başlatılması

RoninOS'u şu komutla başlatın:

`sudo systemctl start ronin-setup`


Komutu ile günlük dosyasının satırlarını görüntüleyin:

`tail -f /home/ronindojo/.logs/setup.logs`


Bu aşamada, **RoninOS'un başlamasına izin vermek ve çalışmasının bitmesini beklemek** önemlidir. Bu yaklaşık 40 dakika sürer. Tüm RoninDojo özellik kurulumları tamamlandı!" mesajı göründüğünde, 6. adıma geçebilirsiniz.


### Adım 6: RoninUI'ye Erişme ve Kimlik Bilgilerini Değiştirme

Kurulumu tamamladıktan sonra, bir tarayıcı aracılığıyla düğümünüze bağlanmak için, kişisel bilgisayarınızın düğümünüzle aynı yerel ağa bağlı olduğundan emin olun. Makinenizde bir VPN kullanıyorsanız, geçici olarak devre dışı bırakın. Tarayıcınızda Interface düğümüne erişmek için URL çubuğuna girin:


- Doğrudan düğümünüzün IP Address'i, örneğin, `192.168.1.??`;
- Veya `ronindojo.local` yazın.


RoninUI ana sayfasına girdiğinizde, kurulumu başlatmanız istenecektir. Bunu yapmak için `Başlayalım` düğmesine tıklayın.


![lets start](assets/notext/25.webp)


Bu aşamada RoninUI size `root` şifrenizi sunar. Bunu güvende tutmak çok önemlidir. Fiziksel bir yedekleme, kağıt üzerinde veya bir [şifre yöneticisi] (https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f) içinde kaydetmeyi tercih edebilirsiniz.


![root password](assets/notext/26.webp)


Root` parolasını kaydettikten sonra, `Kök kullanıcı kimlik bilgilerini yedekledim` kutusunu işaretleyin ve devam etmek için `Devam` düğmesine tıklayın.


![confirm root password](assets/notext/27.webp)


Bir sonraki adım, hem RoninUI web Interface'a erişmek hem de düğümünüzle SSH oturumları kurmak için kullanılacak bir kullanıcı şifresi oluşturmayı içerir. Güçlü bir parola seçin ve güvenli bir şekilde kaydettiğinizden emin olun. Doğrulamak için `Bitir` seçeneğine tıklamadan önce bu şifreyi iki kez girmeniz gerekecektir. Kullanıcı adına gelince, varsayılan seçim olan `ronindojo`nun korunması tavsiye edilir. Değiştirmeye karar verirseniz, aşağıdaki adımlardaki komutları buna göre ayarlamayı unutmayın.


![user credentials](assets/notext/28.webp)


Bu işlemler tamamlandıktan sonra düğümünüzün başlatılmasını bekleyin. Daha sonra RoninUI web Interface'a erişeceksiniz. Sürecin neredeyse sonuna geldiniz, sadece birkaç küçük adım kaldı!

![Ronin UI](assets/notext/29.webp)


### Adım 7: Geçici Kimlik Bilgilerini Kaldırın

Kişisel bilgisayarınızda yeni bir terminal açın ve aşağıdaki komutu kullanarak düğümünüzle bir SSH bağlantısı kurun:

`SSH ronindojo@[IP]`


Örneğin, düğümünüzün IP Address'i `192.168.1.40` ise, uygun komut şu şekilde olacaktır:

`SSH ronindojo@192.168.1.40`


Önceki adımda kullanıcı adınızı değiştirdiyseniz, varsayılan kullanıcı adını (`ronindojo`) başka bir adla değiştirdiyseniz, komutta bu yeni adı kullandığınızdan emin olun. Örneğin, kullanıcı adı olarak `planb` seçtiyseniz ve IP Address `192.168.1.40` ise, girilecek komut şöyle olacaktır:

`SSH planb@192.168.1.40`

Kullanıcı şifresini girmeniz istenecektir. Şifreyi girin ve ardından doğrulamak için `enter` tuşuna basın. Daha sonra RoninCLI Interface'e erişeceksiniz. Klavyenizdeki ok tuşlarını kullanarak `Exit RoninDojo` seçeneğine gidin ve seçmek için `enter` tuşuna basın.

![RoninCLI](assets/notext/30.webp)


Bu noktada, node'unuzun terminalindesiniz ve şuna benzer bir komut istemine sahipsiniz: `ronindojo@RoninDojo:~ $`. Önyüklenebilir mikro SD kartın yapılandırılması sırasında oluşturulan geçici kullanıcıyı kaldırmak için aşağıdaki komutu girin ve `enter` tuşuna basın:

`sudo deluser --remove-home pi`


Kullanıcı şifrenizi onaylamanız istenecektir. Şifrenizi girin ve `enter` tuşuna basarak doğrulayın. İşlemin tamamlanmasını bekleyin, ardından terminalden çıkmak için `exit` komutunu kullanın.


Tebrikler! RoninDojo v2 düğümünüz artık yapılandırıldı ve kullanıma hazır. IBD'ye (*İlk Blok İndirme*) başlayacak ve Bitcoin Blockchain'ü Genesis bloğundan indirmeye ve doğrulamaya devam edecektir. Bu adım, 3 Ocak 2009'dan bu yana yapılan tüm Bitcoin işlemlerinin alınmasını içerir ve biraz zaman alır. Blockchain tamamen indirildikten sonra, indeksleyici veritabanını sıkıştırmaya devam edecektir. IBD'nin süresi önemli ölçüde değişebilir. Bu işlem tamamlandığında RoninDojo düğümünüz tamamen çalışır durumda olacaktır.


**Eğer eski bir RoninDojo v1 node'undan** aynı SSD'yi koruyarak bu öğretici ile bu yeni sürüme geçiş yapıyorsanız, node'unuz diskteki mevcut verileri otomatik olarak algılamalı ve yeniden kullanmalı, böylece IBD'yi tekrar gerçekleştirme zorunluluğundan kurtulmalısınız. Bu durumda, düğümünüzün en son bloklarla yeniden senkronize olmasını beklemeniz yeterli olacaktır.


### Adım 8: "veth* düzeltmesi"

Raspberry Pi üzerindeki RoninDojo v2'nizde, sorunsuz bir kurulumdan sonra düğümünüzün aniden SSH üzerinden erişilemez hale geldiği ancak basit bir yeniden başlatmadan sonra düzeldiği bir hatayla karşılaşırsanız, bu adımı 8 izlemeniz gerekir. Bu yaygın hata, topluluk tarafından geliştirilen bir çözümle kolayca düzeltilebilir: "_veth fix_". Bu küçük düzeltme, ani bağlantı kesilmelerini kalıcı olarak giderir. İşte nasıl uygulanacağı.


Kişisel bilgisayarınızda yeni bir terminal açın ve aşağıdaki komutu kullanarak düğümünüzle bir SSH bağlantısı kurun:

`SSH ronindojo@[IP]`


Örneğin, düğümünüzün IP Address adresi `192.168.1.40` ise, uygun komut şu şekilde olacaktır:

`SSH ronindojo@192.168.1.40`


Kullanıcı şifresini girmeniz istenecektir. Şifreyi girin ve doğrulamak için `enter` tuşuna basın. Daha sonra RoninCLI Interface'e erişeceksiniz. Klavyenizin oklarını kullanarak `Exit RoninDojo` seçeneğine gidin ve seçmek için `enter` tuşuna basın.


Bu noktada, node'unuzun terminalindesiniz ve şuna benzer bir komut istemine sahipsiniz: `ronindojo@RoninDojo:~ $`. Veth* düzeltmesini uygulamak için aşağıdaki komutu yazın ve `enter` tuşuna basın:

`sudo nano /etc/dhcpcd.conf`


Şifrenizi tekrar onaylayın ve `enter` tuşuna basın.


Dhcpcd.conf` dosyasına ulaşacaksınız. Aşağıdaki metni yıldız işaretini de içerecek şekilde kopyalamanız ve dosyanın en altına eklemeniz gerekmektedir:

`denyinterfaces veth*`


Bunu yapmak için, klavyenizdeki aşağı oku kullanarak dosyanın en altına gidin, ardından metni bağımsız bir satıra yapıştırmak için farenizin sağ tuşunu kullanın.


Metni ekledikten sonra, çıkmaya başlamak için `ctrl X` tuşuna basın, ardından değişiklikleri kaydetmeyi onaylamak için `ctrl Y` tuşuna basın ve sonlandırmak ve komut istemine dönmek için `enter` tuşuna basın. Değişikliğin doğru şekilde uygulandığından emin olmak için, uygun komutu kullanarak `dhcpcd.conf` dosyasını yeniden açın.


Düzeltmenin uygulanmasını tamamlamak için düğümünüzü yeniden başlatın:

`sudo reboot now`


Bu noktada terminalinizi kapatabilirsiniz. RoninDojo'nuzun yeniden başlatılması için gerekli süreyi bekleyin, ardından tarayıcınızın grafik Interface'u aracılığıyla yeniden bağlanabilmeniz gerekir. Bu işlem karşılaşılan hatayı düzeltmelidir.


## RoninDojo v2 düğümünüzü nasıl kullanabilirsiniz?


### Wallet yazılımınızı Electrs'e bağlama

Yeni kurulmuş ve senkronize edilmiş node'unuzun ilk kullanımı, işlemlerinizi Bitcoin ağına yayınlamak olacaktır. İşlemlerinizi gizli bir şekilde yayınlamak için muhtemelen çeşitli cüzdanlarınızı düğümünüze bağlamak isteyeceksiniz. Bunu Electrum Rust Sunucusu (electrs) aracılığıyla yapabilirsiniz. Bu uygulama genellikle RoninDojo node'unuza önceden yüklenmiştir. Değilse, RoninCLI Interface aracılığıyla `Uygulamalar > Uygulamaları Yönet > Electrum Sunucusunu Yükle` bölümünden manuel olarak yükleyebilirsiniz.


Electrum Sunucunuzun Tor Address'ini almak için, RoninUI web Interface'ten şu adrese gidin:

`Eşleştirme > Electrum sunucusu > Şimdi eşleştir`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Daha sonra Address yazılımınıza `.onion` ile biten `Hostname` Wallet'yi `50001` portu ile birlikte girmeniz gerekecektir. ![hostname](assets/notext/33.webp)

Örneğin, Sparrow wallet'de sekmeye gitmeniz yeterlidir:

`Dosya > Tercihler > Sunucu > Özel Electrum`


![Sparrow](assets/notext/34.webp)


### Wallet yazılımınızı Samourai Dojo'ya bağlama

Electrs kullanmaya alternatif olarak Dojo, uyumlu Software Wallet'nizi doğrudan RoninDojo düğümünüze bağlamanıza olanak tanır. Samourai Wallet ve Sentinel gibi cüzdanlar bu işlevi sunar.


Bağlantı kurmak için Dojo'nuzun QR kodunu taramanız yeterli olacaktır. Bu QR koduna RoninUI üzerinden erişmek için şu adrese gidin:

`Eşleştirme > Samourai Dojo > Şimdi eşleştir`

![Samourai Dojo](assets/notext/35.webp)

Samourai Wallet'nizi Dojo'nuza bağlamak için, uygulama kurulumu sırasında bu QR kodunu taramanız yeterlidir:


![Samourai Wallet connection](assets/notext/36.webp)


Ronin Dojo'nuzu kurmadan önce zaten bir Samourai Wallet'ünüz varsa, Wallet'ünüzü geri yüklemeden önce Wallet'ünüzü yedeklemeniz, Samourai Wallet uygulamasını kaldırmanız ve ardından yeniden yüklemeniz gerekir. Yeniden yüklenen uygulamayı başlattıktan sonra, yeni bir Dojo'ya bağlanma seçeneğiniz olacaktır. **Dikkatli olun, bu işlem doğru yapılmazsa bitcoinlerinizi kaybetme riski taşır ** Samourai Wallet'ünüzün yedeğinin dosyalarınızda olduğundan emin olun ve passphrase'ünüzün geçerliliğini `Ayarlar > Sorun Giderme > passphrase` aracılığıyla doğrulayın. Kurtarma ifadenizin ve passphrase'ünüzün okunabilir bir yedeğinin olması da önemlidir. Bu işlemde daha fazla hassasiyet için bu ayrıntılı öğreticiyi izlemeniz önerilir: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Kendi Mempool.space Block explorer'inizi kullanma

Bir Block explorer, Bitcoin Blockchain'den gelen ham bilgileri yapılandırılmış ve kolayca okunabilir bir formata dönüştürür. Mempool.space* gibi araçlarla, işlemleri analiz etmek, belirli adresleri aramak ve hatta ağın mempool'larının ortalama ücret oranlarına gerçek zamanlı olarak danışmak mümkündür.


Bununla birlikte, çevrimiçi blok kaşiflerini kullanmak gizliliğiniz için riskler oluşturur ve üçüncü taraflarca sağlanan verilere güvenmeyi gerektirir. Gerçekten de, bu hizmetleri kendi düğümünüzden geçmeden kullanarak, işlemlerinizle ilgili bilgileri yanlışlıkla ifşa edebilirsiniz ve site sahibi tarafından sunulan bilgilerin doğruluğuna güvenmeniz gerekir.

Bu riskleri azaltmak için, Tor ağı üzerinden doğrudan düğümünüzde barındırılan kendi *Mempool.space* örneğinizi kullanmanız önerilir. Bu çözüm, gizliliğinizin korunmasını ve verilerinizin özerkliğini sağlar.

Bunu yapmak için RoninUI'den *Mempool Space Visualizer* yükleyerek başlayın. Web Interface'de `Dashboard` sekmesine gidin ve `Mempool Space` altındaki `Manage` seçeneğine tıklayın:

`Pano > Mempool Alanı > Yönet`

![Manage mempool](assets/notext/37.webp)

Ardından `Mempool görselleştiricisini yükle` düğmesine tıklayın:

![install mempool](assets/notext/38.webp)

Kullanıcı şifrenizi onaylayın:

![password mempool](assets/notext/39.webp)

Kurulumun tamamlanmasını bekleyin, ardından `Yönet` düğmesine tekrar tıklayın:

![Mempool Manage](assets/notext/40.webp)

Tor ağı üzerinden kendi *Mempool.space* örneğinize erişmek için bir `.onion` bağlantısı alacaksınız.

![Mempool link](assets/notext/41.webp)

Her yerden kolay ve güvenli erişim için bu bağlantıyı Tor tarayıcısında favorilerinize kaydetmenizi veya akıllı telefonunuzdaki Tor Browser uygulamasına eklemenizi tavsiye ederim. Henüz Tor tarayıcısına sahip değilseniz, buradan indirebilirsiniz: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Bitcoinlerinizi karıştırmak için Whirlpool'yi kullanma

RoninDojo düğümünüz ayrıca Whirlpool coinjoins'in otomasyonunu sağlayan bir komut satırı Interface olan _WhirlpoolCLI_ ve _WhirlpoolCLI_ ile etkileşim kurmak için tasarlanmış bir grafik Interface olan _WhirlpoolGUI_'yi de entegre eder.


Whirlpool aracılığıyla bir CoinJoin gerçekleştirmek, kullanılan uygulamanın remiksleri gerçekleştirmek için aktif olmasını gerektirir. Bu koşul, yüksek düzeyde anonslar elde etmek isteyenler için kısıtlayıcı olabilir. Gerçekten de, Whirlpool'i entegre eden uygulamaya ev sahipliği yapan cihaz sürekli açık kalmalıdır. Bu, günün 24 saati remikslere katılmak için bilgisayarınızın veya akıllı telefonunuzun Samourai veya Sparrow ile sürekli açık kalması gerektiği anlamına gelir. Bu kısıtlamaya bir çözüm, Bitcoin düğümü gibi her zaman açık olan bir makinede _WhirlpoolCLI_ kullanmaktır, böylece paralarınız kesintisiz olarak ve başka bir cihazı açık tutmaya gerek kalmadan remiks yapabilir.


Samourai Wallet ve RoninDojo v2 ile coinjoining sürecinde size A'dan Z'ye adım adım rehberlik edecek ayrıntılı bir eğitim hazırlanmaktadır.


CoinJoin'i ve Bitcoin'da kullanımını daha iyi anlamak için sizi bu diğer makaleye de bakmaya davet ediyorum: CoinJoin'i Bitcoin üzerinde anlamak ve kullanmak, bu teknik hakkında bilmeniz gereken her şeyi detaylandırıyorum.


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

### Whirlpool İstatistik Aracını (WST) Kullanma


Whirlpool ile coinjoins gerçekleştirdikten sonra, karışık UTXO'larınız için elde edilen gizlilik seviyesini tam olarak değerlendirmek yararlıdır. Bunu yapmak için Python aracını *Whirlpool Stat Tool* kullanabilirsiniz. Bu araç, UTXO'larınızın hem ileriye dönük hem de geriye dönük puanlarını ölçmenize ve havuzdaki yayılma oranlarını analiz etmenize olanak tanır.


Bu anons setlerinin hesaplama mekanizmalarını daha iyi anlamak için makaleyi okumanızı tavsiye ederim: Bu endekslerin işleyişini detaylandıran REMIX - Whirlpool.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



WST aracına erişmek için RoninCLI'ye gidin. Bunu yapmak için, kişisel bilgisayarınızda bir terminal açın ve aşağıdaki komutu kullanarak düğümünüzle bir SSH bağlantısı kurun:

`SSH ronindojo@[IP]`


Örneğin, düğümünüzün IP Address değeri `192.168.1.40` ise, uygun komut şu şekilde olacaktır:

`SSH ronindojo@192.168.1.40`


Eğer 6. adımda kullanıcı adınızı değiştirdiyseniz, varsayılan kullanıcı adını (`ronindojo`) bir başkasıyla değiştirdiyseniz, komutta bu yeni adı kullandığınızdan emin olun. Örneğin, kullanıcı adı olarak `planb` seçtiyseniz ve IP Address `192.168.1.40` ise, girilecek komut şöyle olacaktır:

`SSH planb@192.168.1.40`


Kullanıcı şifresini girmeniz istenecektir. Şifreyi girin ve doğrulamak için `enter` tuşuna basın. Daha sonra RoninCLI Interface'ye erişeceksiniz. Klavyenizdeki ok tuşlarını kullanarak `Samourai Toolkit` menüsüne gidin ve seçmek için `enter` tuşuna basın:


![Samourai Toolkit](assets/notext/43.webp)


Ardından `Whirlpool Stat Tool` öğesini seçin:


![WST](assets/notext/44.webp)


WST başlatıldıktan sonra, araç otomatik kurulumuna devam edecektir. Bu adım sırasında bekleyin. Kullanım talimatları ilerleyecektir. Kurulum tamamlandığında, WST terminaline erişmek için herhangi bir tuşa basın:


![WST commands](assets/notext/45.webp)


Aşağıdaki komut istemi görüntülenecektir:

`wst#/tmp>`


Bu Interface'ten çıkmak ve RoninCLI menüsüne dönmek isterseniz, enter tuşuna basmanız yeterlidir:

`quit`


İlk olarak, OXT'den veri çekerken gizliliği sağlamak için proxy'yi Tor kullanacak şekilde yapılandırmak gerekir. Şu komutu girin:

`socks5 127.0.0.1:9050`


Daha sonra, işleminizi içeren havuz bilgilerini indirmeye devam edin:

`download 0001`

0001` yerine ilgilendiğiniz havuzun mezhep kodunu yazın. Mezhep kodları WST'de aşağıdaki gibidir:


- Havuz 0,5 bitcoin: `05`
- Havuz 0,05 bitcoin: `005`
- Havuz 0.01 bitcoins: `001`
- Havuz 0.001 bitcoins: `0001`


İndirdikten sonra, aşağıdaki komutta `0001` yerine havuzunuzun kodunu yazarak verileri yükleyin: `load 0001`


![WST loading](assets/notext/46.webp)


Yüklemenin tamamlanmasını bekleyin, bu işlem birkaç dakika sürebilir. Veriler yüklendikten sonra, Coin'inizin anonset skorlarını öğrenmek için, `score` komutunu ve ardından txid'nızı (parantezler olmadan) çalıştırın:

`score [txid]`


![WST score](assets/notext/47.webp)


WST daha sonra geriye dönük skoru (_Geriye dönük metrikler_) ve ardından ileriye dönük skoru (_İleriye dönük metrikler_) görüntüleyecektir. Anonset puanlarının yanı sıra WST, işleminizin anonsetine göre havuz içindeki yayılma oranını da gösterecektir.


**Coin'in ileriye dönük puanının en son karışımınızdan değil, ilk karışımınızın txid'ından hesaplanması gerektiğini unutmamak önemlidir. Tersine, bir UTXO'un geriye dönük puanı, son döngünün txid'ından hesaplanır.**


### Boltzmann Hesaplayıcısını Kullanma

Boltzmann hesaplayıcı, bir Bitcoin işlemini analiz etmek için bir araçtır ve diğer gelişmiş ölçümlerin yanı sıra entropi seviyesini ölçme olanağı sunar. Bu veriler, bir işlemin gizliliğinin niceliksel bir değerlendirmesini sağlar ve potansiyel kusurların belirlenmesine yardımcı olur. Bu araç RoninDojo düğümünüze zaten entegre edilmiştir, böylece erişimi ve kullanımı kolaydır.


Boltzmann Hesaplayıcıyı kullanma prosedürünü detaylandırmadan önce, bu göstergelerin anlamını, hesaplama yöntemini ve faydalarını anlamak önemlidir. Herhangi bir Bitcoin işlemi için geçerli olmakla birlikte, bu göstergeler özellikle bir CoinJoin işleminin kalitesini değerlendirmek için kullanışlıdır.


**Yazılımın hesapladığı ilk gösterge**, araçta `nb kombinasyonları` altında gösterilen toplam olası kombinasyon sayısıdır. İlgili UTXO'ların değerlerine dayanan bu gösterge, girdilerin çıktılarla ilişkilendirilebileceği yolların sayısını ölçer. Başka bir deyişle, bir işlemin generate yapabileceği makul yorumların sayısını belirler. Örneğin, Whirlpool 5x5 modeline göre yapılandırılmış bir CoinJoin `1496` olası kombinasyon sunar:

![combinations](assets/notext/50.webp)

Kredi: KYCP


**Hesaplanan ikinci gösterge** bir işlemin entropisidir ve `Entropi` ile gösterilir. Bir işlem çok sayıda olası kombinasyona sahip olduğunda, genellikle entropisine atıfta bulunmak daha uygun olur. Bu, olası kombinasyon sayısının ikili logaritması olarak tanımlanır. İşte kullanılan formül:


- e$: işlemin entropisi;
- c$: işlem için olası kombinasyon sayısı.

$$E = \log_2(C)$$


Matematikte ikili logaritma (2 tabanında logaritma), 2'yi bir kuvvete yükseltmenin ters işlemine karşılık gelir. Başka bir deyişle, $x$ değerinin ikili logaritması, $x$ değerini elde etmek için 2'nin yükseltilmesi gereken üs değeridir. Dolayısıyla bu gösterge bit cinsinden ifade edilir. Whirlpool 5x5 modeline göre yapılandırılmış bir CoinJoin işlemi için entropiyi hesaplama örneğini ele alalım; bu işlem, daha önce de belirtildiği gibi, `1496`lık bir dizi olası kombinasyon sunar:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \yaklaşık 10.5469 \text{ bits}$


Dolayısıyla, bu CoinJoin işlemi 10.5469 bitlik bir entropi gösterir ki bu da oldukça tatmin edici bir değer olarak kabul edilir. Bu değer ne kadar yüksek olursa, işlem o kadar çok farklı yorum kabul eder ve böylece gizlilik seviyesi artar.


Bir girdi ve iki çıktı içeren daha geleneksel bir işlemle ek bir örnek alalım: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

Bu işlem söz konusu olduğunda, tek olası yorum şudur: `(inp 0) > (Outp 0 ; Outp 1)`. Sonuç olarak, entropisi `0` olarak belirlenir:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \yaklaşık 0 \text{ bits}$

**Boltzmann Hesaplayıcı tarafından sağlanan üçüncü gösterge** `Wallet Verimlilik` olarak adlandırılmıştır. Bu gösterge, işlemin verimliliğini, aynı kurulumda düşünülebilecek en uygun işlemle karşılaştırarak değerlendirir. Bu bizi, belirli bir işlem yapısının teorik olarak ulaşabileceği en yüksek entropiye karşılık gelen maksimum entropi kavramını tartışmaya götürür. Böylece, bir Whirlpool 5x5 CoinJoin yapısı için maksimum entropi `10.5469` olarak belirlenir. İşlemin verimliliği daha sonra bu maksimum entropi ile analiz edilen işlemin gerçek entropisi karşı karşıya getirilerek hesaplanır. Kullanılan formül aşağıdaki gibidir:


- eR$: işlemin bit cinsinden ifade edilen gerçek entropisi;
- eM$: belirli bir işlem yapısı için mümkün olan maksimum entropi, yine bit cinsinden;
- ef$: bit cinsinden işlemin verimliliği.

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{ bits}$


Bu gösterge de yüzde olarak ifade edilir, formülü şu şekildedir:


- cR$: gerçek olası kombinasyonların sayısı;
- $CM$: aynı yapıya sahip olası kombinasyonların maksimum sayısı;
- ef$: yüzde olarak ifade edilen verimlilik.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


Dolayısıyla `%100` verimlilik, işlemin yapısına bağlı olarak gizlilik potansiyelini en üst düzeye çıkardığını gösterir.


**Dördüncü gösterge** olan entropi yoğunluğu veya `Entropi Yoğunluğu`, işlemin her bir girdi veya çıktısına göre entropi hakkında bir bakış açısı sunar. Bu gösterge, farklı boyutlardaki işlemlerin verimliliğini değerlendirmek ve karşılaştırmak için kullanışlıdır. Bunu hesaplamak için, işlemin toplam entropisini ilgili toplam girdi ve çıktı sayısına bölmeniz yeterlidir. Whirlpool 5x5 CoinJoin örneğini ele alalım:


- eD$: bit cinsinden ifade edilen entropi yoğunluğu;
- e$: işlemin bit cinsinden ifade edilen entropisi;
- t$: işlemdeki toplam girdi ve çıktı sayısı.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$

$$ED = \frac{10.5469}{10}$$

$$ED = 1,054 \text{ bits}$

**Boltzmann Hesaplayıcı tarafından sağlanan beşinci bilgi**, girdiler ve çıktılar arasındaki eşleşme olasılıkları tablosudur. Bu tablo, `Boltzmann skoru` aracılığıyla, belirli bir girdinin belirli bir çıktıya bağlanma olasılığını gösterir. Bir Whirlpool CoinJoin örneğini ele alırsak, olasılık tablosu her bir girdi ve çıktı arasındaki bağlantı olasılığını vurgulayarak işlemdeki ilişkilerin belirsizliği veya öngörülebilirliğinin nicel bir ölçüsünü sağlayacaktır:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Burada, her bir girdinin herhangi bir çıktı ile ilişkilendirilme şansının eşit olduğu açıktır, bu da işlemin belirsizliğini ve gizliliğini güçlendirir. Ancak, tek bir girdi ve iki çıktı içeren basit bir işlem söz konusu olduğunda durum farklıdır:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Burada, her bir çıktının 0 numaralı girdiden gelme olasılığının %100 olduğunu görüyoruz. Dolayısıyla daha düşük bir olasılık, girdiler ve çıktılar arasındaki doğrudan bağlantıları seyrelterek daha fazla gizlilik anlamına gelir.


**Sağlanan altıncı bilgi** deterministik bağlantıların sayısıdır ve bu bağlantıların oranı ile tamamlanmaktadır. Bu gösterge, analiz edilen işlemdeki girdiler ve çıktılar arasındaki kaç bağlantının %100 olasılıkla tartışılmaz olduğunu ortaya koymaktadır. Oran ise bu deterministik bağlantıların işlemin toplam bağlantıları içindeki ağırlığına ilişkin bir perspektif sunmaktadır.


Örneğin, Whirlpool tipi bir CoinJoin işlemi hiçbir deterministik bağlantı sunmaz ve bu nedenle %0'lık bir gösterge ve oran gösterir. Öte yandan, incelenen ikinci işlemimizde (bir girdi ve iki çıktı ile) gösterge 2 olarak ayarlanmış ve oran %100'e ulaşmıştır. Dolayısıyla, boş bir gösterge, girdiler ve çıktılar arasında doğrudan ve tartışılmaz bağlantıların olmaması sayesinde mükemmel gizliliğe işaret etmektedir.


**RoninDojo'da Boltzmann Hesaplayıcısına nasıl erişilir?

Boltzmann Hesaplayıcı* aracına erişmek için RoninCLI'ye gidin. Bunu yapmak için, kişisel bilgisayarınızda bir terminal açın ve aşağıdaki komutu kullanarak düğümünüzle bir SSH bağlantısı kurun: `SSH ronindojo@[IP]`


Örneğin, düğümünüzün Address IP adresi `192.168.1.40` ise, uygun komut şu şekilde olacaktır:

`SSH ronindojo@192.168.1.40`


Eğer 6. adımda kullanıcı adınızı değiştirdiyseniz, varsayılan kullanıcı adını (`ronindojo`) bir başkasıyla değiştirdiyseniz, komutta bu yeni adı kullandığınızdan emin olun. Örneğin, kullanıcı adı olarak `planb` seçtiyseniz ve IP Address `192.168.1.40` ise, girilecek komut şöyle olacaktır:

`SSH planb@192.168.1.40`


Kullanıcı şifresini girmeniz istenecektir. Şifreyi girin ve ardından doğrulamak için `enter` tuşuna basın. Daha sonra RoninCLI Interface'ye erişeceksiniz. Klavyenizdeki okları kullanarak `Samourai Toolkit` menüsüne gidin ve seçmek için `enter` tuşuna basın:


![Samourai Toolkit](assets/notext/43.webp)


Ardından `Boltzmann Hesaplayıcı` öğesini seçin:


![boltzmann](assets/notext/49.webp)


Yazılımın ana sayfasına ulaşacaksınız:


![boltzmann home](assets/notext/51.webp)


İncelemek istediğiniz işlemin txid numarasını girin ve `enter` tuşuna basın:


![boltzmann txid](assets/notext/52.webp)


Hesaplayıcı daha sonra size daha önce tartıştığımız tüm göstergeleri sunar:


![boltzmann result](assets/notext/53.webp)


### RoninDojo v2'nizin diğer özellikleri

RoninDojo düğümünüz çeşitli diğer özellikleri entegre eder. Özellikle, dikkate almak için belirli bilgileri tarama yeteneğine sahipsiniz. Örneğin, bazen RoninDojo'ya bağlı Samourai Wallet'ünüz gerçekte sahip olduğunuz bitcoinleri göstermeyebilir. Bu Wallet'te bitcoinleriniz olduğundan emin olmanıza rağmen bakiye 0 gösteriyorsa, türetme yollarındaki bir hata gibi çeşitli nedenler bu durumu açıklayabilir. Ancak nedenlerden biri, node'unuzun adreslerinizi düzgün bir şekilde izlememesi de olabilir. Bu sorunu çözmek için, _xpub aracını_ kullanarak düğümünüzün gerçekten `xpub`ınızı takip ettiğinden emin olabilirsiniz. Bu araca RoninUI üzerinden erişmek için şu yolu izleyin:

`Bakım > XPUB Aracı`


Soruna neden olan `xpub`ı girin ve bu bilgiyi doğrulamak için `Check` düğmesine tıklayın:

![xpub tool](assets/notext/54.webp)

Tüm işlemlerin düzgün bir şekilde listelendiğinden emin olun. Kullanılan türetme tipinin Wallet'inizinkiyle eşleştiğini doğrulamak da önemlidir. Eğer durum böyle değilse, `Türetme Tipi` üzerine tıklayın, ardından ihtiyaçlarınıza göre `BIP44`, `BIP49` veya `BIP84` arasından seçim yapın.

Bu aracın ötesinde, RoninUI'nin `Bakım' sekmesi diğer yararlı özelliklerle doludur:


- İşlem Aracı*: Belirli bir işlemin detaylarının incelenmesini sağlar;
- Address Aracı*: Belirli bir Address'nın Dojo'nuz tarafından izlenmesinin onaylanmasını sağlar;
- Blokları Yeniden Tara*: Düğümünüzü belirli bir blok aralığında yeni bir tarama yapmaya zorlar.


"Push Tx" sekmesi, RoninUI'nin Bitcoin ağında imzalı bir işlemin yayınlanmasını sağlayan bir başka ilginç özelliğidir. İşlem onaltılık biçimde girilmelidir.


RoninUI kontrol panelinizde bulunan diğer sekmelerle ilgili olarak:


- uygulamalar: Whirlpool uygulamasını barındırır ve gelecekte yeni uygulamaları entegre etmek için kesinlikle kullanılacaktır;
- günlükler`: Yazılımınızın olay günlüklerine gerçek zamanlı erişim sağlar;
- sistem Bilgisi`: Düğümünüz hakkında CPU sıcaklığı, depolama alanı kullanımı veya RAM verileri gibi genel bilgiler sağlar. Ayrıca düğümünüzü yeniden başlatmak veya kapatmak için `Reboot` ve `Shut down` seçeneklerini de bulacaksınız;
- `Ayarlar`: Kullanıcı şifrenizi değiştirmenizi sağlar.


İşte bu kadar! Bu dersi sonuna kadar takip ettiğiniz için teşekkür ederim. Eğer hoşunuza gittiyse, sosyal medyada paylaşmanızı tavsiye ederim. Ayrıca, fırsatınız varsa, bu ücretsiz ve açık kaynaklı yazılımları topluluğumuzun kullanımına sunan geliştiricileri bir bağışla desteklemeyi düşünün: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). RoninDojo hakkındaki bilgilerinizi derinleştirmek ve daha fazla kaynak keşfetmek için, aşağıda belirtilen harici kaynakların bağlantılarına başvurmanızı şiddetle tavsiye ederim.


**Harici kaynaklar:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)