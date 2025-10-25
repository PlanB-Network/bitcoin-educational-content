---
name: Bitcoin Knots
description: Bitcoin Knots alternatif istemcisi ile bir düğümü nasıl başlatabilirim?
---
![cover](assets/cover.webp)


![video](https://youtu.be/zT4NuAaH3EM)


Bitcoin Knots, Bitcoin core'den türetilen Bitcoin protokolünün alternatif bir uygulamasıdır. Luke Dashjr tarafından tasarlanan ve sürdürülen bu uygulama, ağdaki diğer düğümlerle uyumlu kalırken Mempool'ten bazı ek özellikler ve kural ayarlamaları sunar. Bitcoin Knots, bir Bitcoin Wallet'i entegre eder, ancak diğer Wallet yazılımlarının yanında basit bir Bitcoin düğümü olarak da kullanılabilir.


## Neden Core yerine Knots kullanıyorsunuz?


Şu anda Core, ağ üzerinde Bitcoin protokolünün çoğunluk uygulamasıdır. Bitcoin protokolü sadece bir dizi kuraldır. Bunları uygulamak için yazılım gerektirir. Bitcoin protokolünü uygulayan yazılımı çalıştıran bir makineye düğüm adı verilir ve tüm bu düğümler birlikte Bitcoin ağını oluşturur.


Bitcoin'in tarihi boyunca, Satoshi Nakamoto tarafından geliştirilen ilk yazılımdan türetilen çok sayıda istemci ortaya çıkmıştır. Bugün (Mart 2025), Bitcoin core ezici çoğunluktadır ve Bitcoin ağındaki düğümlerin neredeyse %98'i bu istemciyi kullanmaktadır.


Bununla birlikte, alternatif yazılımlar da mevcuttur. Bunlar Bitcoin Cash gibi Altcoin bağlantılı düğümler değil, gerçek Bitcoin ağıyla uyumlu alternatif istemcilerdir. Bunlar arasında Bitcoin Knots en iyi bilinendir. Şu anda ağın yaklaşık %1,4'ünü temsil etmektedir. Diğer alternatif müşteriler hala çok azınlıktadır.


![Image](assets/fr/01.webp)


Core yerine Knots gibi alternatif bir istemci kullanmanın iki ana nedeni vardır:




- **Teknik**: Bu istemciler, düğümünüz tarafından hangi işlemlerin kabul edileceğini ve yayınlanacağını belirleyerek, özellikle Mempool yönetimi açısından Core'a genellikle farklı seçenekler sunar.
- **Politika**: Bazı insanlar Knots gibi alternatif istemcileri teknik olmayan nedenlerle, özellikle de Core'a bir alternatifi desteklemek ve böylece onun tekelini azaltmak için kullanmayı tercih etmektedir. Eğer Core tehlikeye girerse, sadece sağlam, iyi bakımlı alternatif istemcilere sahip olmak değil, aynı zamanda bunların nasıl kullanılacağını bilmek de yararlı olacaktır. Diğerleri Knots'u protesto amacıyla kullanmaktadır, çünkü Core'un geliştiricilerine olan güvenlerini kaybetmişlerdir ya da çoğunluk istemcisinin yönetimini onaylamamaktadırlar.


## Bitcoin Düğümlerini nasıl kurabilirim?


İşletim sisteminize uygun sürümü indirmek için [resmi Bitcoin Knots web sitesine] (https://bitcoinknots.org/#download) gidin. Yazılımı doğrulamak için parmak izini ve imzaları indirmeyi unutmayın. Bu dosyalar ayrıca [Bitcoin Knots GitHub deposunda](https://github.com/bitcoinknots/Bitcoin) da mevcuttur.


![Image](assets/fr/02.webp)


Yazılımı makinenize yüklemeden önce, orijinalliğini ve bütünlüğünü kontrol etmenizi şiddetle tavsiye ederiz. Nasıl yapılacağını bilmiyorsanız, bu diğer eğiticiye bir göz atın:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Yazılım doğrulandıktan sonra, kurulum panelinde belirtilen adımları izleyerek yazılımı yükleyin.


![Image](assets/fr/03.webp)


## IBD'yi başlatın


Bitcoin Knots'u ilk kez başlattığınızda, düğüm verilerinizin (Blockchain, UTXO seti ve parametreler dahil) depolanacağı yerel dizini seçebileceksiniz.


![Image](assets/fr/04.webp)


Blockchain verilerini yalnızca en yeni blokları tutacak şekilde budamayı da seçebilirsiniz. Bu seçenek, düğümünüzün belirli bir depolama sınırı dahilinde her bloğu bütünüyle kontrol etmesini ve böylece en eski blokları kademeli olarak kaldırmasını sağlar. Yeterli disk alanınız varsa (şu anda yaklaşık 650 GB, ancak bu sayı artıyor), bu seçeneği işaretlemeyin. Disk alanınız sınırlıysa, budama özelliğini etkinleştirin ve izin verilen maksimum kapasiteyi belirtin.


Lütfen dikkat: Düğümünüz pruned ise ve onu kurtarılmış bir Wallet'yi senkronize etmek için kullanırsanız, yerel olarak depolanan en eski bloktan önceki işlemleri geri alamazsınız.


![Image](assets/fr/05.webp)


Kullanılabilir bir diğer seçenek de "*Geçerli Varsay*"dır. Belirli bir bloktan önceki bloklarda yer alan işlemler için imza doğrulamasını atlayarak ilk senkronizasyonu hızlandırır.


"*Assume Valid*"in amacı, bu işlemlerin önceden ağ tarafından büyük ölçüde doğrulandığını varsayarak, güvenliği önemli ölçüde azaltmadan düğümün ilk senkronizasyonunu hızlandırmaktır. Tek önemli uzlaşma, düğümünüzün önceki Bitcoin hırsızlıklarını tespit etmeyeceği, ancak yine de verilen toplam bitcoin sayısının doğruluğunu garanti edeceğidir. Düğümünüz belirtilen bloktan sonra tüm işlem imzalarını doğrulayacaktır. Bu yaklaşım, ağ tarafından uzun süredir itiraz edilmeden kabul edilen bir işlemin büyük olasılıkla geçerli olduğu varsayımına dayanmaktadır.


Örneğin, burada "*Geçerli Olduğunu Varsay*" blok no. olarak ayarlanmıştır. 855 000 `0000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, 1 Ağustos 2024 tarihinde yayınlanmıştır. Bu nedenle IBD sırasında düğümüm tam imza doğrulamasını yalnızca bu bloktan başlatacaktır.


![Image](assets/fr/06.webp)


Ardından *İlk Blok İndirme* işlemini başlatmak için "*Tamam*" düğmesine tıklayın. İlk düğüm senkronizasyonu sırasında sabırlı olmanız gerekecektir. Senkronizasyona daha sonra devam etmek isterseniz, yazılımı kapatmanız ve bilgisayarınızı kapatmanız yeterlidir. Programı bir sonraki açışınızda senkronizasyon sorunsuz bir şekilde devam edecektir.


![Image](assets/fr/07.webp)


## Bitcoin Düğümünüzün Kurulumu


"*Ayarlar*" sekmesine tıklayın, ardından "*Seçenekler*"i seçin.


![Image](assets/fr/08.webp)


"*Ana*" sekmesinde, düğümün ana parametrelerine erişirsiniz:




- "*Başlat...*", senkronizasyona hemen başlamak için bilgisayarınız başlatıldığında düğümü otomatik olarak başlatır;
- "*Prune...*", Blockchain'ü budamayı seçtiyseniz depolama sınırını ayarlar;
- "*Veritabanı önbelleği...*" düğümünüze izin verilen maksimum RAM miktarını ayarlar;
- Son olarak, Bitcoin Knots düğümünüzü örneğin Sparrow wallet veya Liana gibi diğer Wallet yazılımlarına bağlamak istiyorsanız "*RPC sunucusunu etkinleştir*" seçeneğini etkinleştirin.


![Image](assets/fr/09.webp)


"*Wallet*" sekmesinde, daha sonra Knots üzerinde oluşturabileceğiniz entegre Wallet için ayarları bulacaksınız. RBF ve Coin kontrolünü etkinleştirmenizi tavsiye ederim. Kullanılacak komut dosyası türünü de tanımlayabilirsiniz.


![Image](assets/fr/10.webp)


"*Ağ*" sekmesi, özel ihtiyaçlarınıza göre uyarlayabileceğiniz ağ parametrelerini içerir.


![Image](assets/fr/11.webp)


"*Mempool*" sekmesi *Bellek Havuzunu*, yani bellekte saklanan onaylanmamış işlemlerin yönetimini ve bu işlev için ayrılan maksimum boyutu (varsayılan olarak 300 MB) yapılandırmanıza olanak tanır.


![Image](assets/fr/12.webp)


"Spam filtreleme" sekmesi bir Bitcoin Knots özelliğidir. Burada, hangi işlemleri kabul edeceğinizi veya yayınlamayı reddedeceğinizi seçmenize olanak tanıyan bir dizi ayar bulacaksınız. Ana amaç, Bitcoin'ün belirli marjinal kullanımlarını, özellikle de meta-protokolleri sınırlandırmak, düğümünüze aşırı yüklenmekten kaçınırken bu uygulamalarla mücadele etmektir. Bu, Bitcoin'e ilişkin kişisel vizyonunuza bağlı olarak politik bir seçimdir.


Ayrıca "*Dust*" eşiğinin tanımı gibi klasik parametreleri de bulacaksınız.


Ancak bu parametreler yalnızca standartlaştırma kurallarını etkiler. Düğümünüz, Bitcoin ağının geri kalanıyla uyumlu kalabilmek için onaylanmamış işlemleri yalnızca bir bloğa dahil edildiklerinde kabul etmeye devam edecektir. Bu ayarlar yalnızca düğümünüzün onaylanmamış işlemleri işleme ve eşlerine dağıtma şeklini değiştirir. Pratikte, Knots azınlıkta olduğu için, ağdaki standardizasyonu tanımlayan Bitcoin core'te varsayılan olarak oluşturulan kurallardır.


![Image](assets/fr/13.webp)


"*Mining*" sekmesi, bu işlevi etkinleştirmek isterseniz düğümünüzün Mining'ye olası katılımını yapılandırmanıza olanak tanır.


![Image](assets/fr/14.webp)


Son olarak, "*Görüntü*" sekmesi, yazılım dili de dahil olmak üzere Interface grafikleriyle ilgili parametrelerle ilgilidir.


![Image](assets/fr/15.webp)


## Bitcoin Wallet Oluşturma


İlk senkronizasyon tamamlandığında, Bitcoin Knots düğümünüz tamamen işlevsel hale gelir. Artık bu düğümü diğer Wallet yazılımlarına bağlama ya da dahili Hot Wallet'yi doğrudan kullanma seçeneğine sahipsiniz. Bunu yapmak için "*Yeni bir Wallet* oluştur" düğmesine tıklayın.


![Image](assets/fr/16.webp)


Wallet'inize bir isim verin. Ayrıca "*Wallet'i Şifrele*" düğmesine tıklayarak bir passphrase BIP39 ile koruyabilirsiniz. Hazır olduğunuzda, "*Oluştur*" düğmesine tıklayın.


![Image](assets/fr/17.webp)


passphrase BIP39, Wallet'inizin güvenliğini artırmak için Mnemonic ifadenize ek olarak özgürce seçebileceğiniz isteğe bağlı bir paroladır. Bu özelliği yapılandırmadan önce, passphrase'nın teoride nasıl çalıştığını ve bitcoinlerinizin kalıcı olarak kaybedilmesine yol açabilecek hatalardan nasıl kaçınacağınızı ayrıntılı olarak açıklayan aşağıdaki makaleyi okumanızı şiddetle tavsiye ederiz:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
passphrase seçeneğini etkinleştirdiyseniz, sağlam bir tane seçin ve bir veya daha fazla güvenli fiziksel ortama dikkatlice kaydedin.


![Image](assets/fr/18.webp)


Bitcoin Wallet'iniz artık oluşturulmuştur.


![Image](assets/fr/19.webp)


## Bitcoin Wallet'ünüzü yedekleme


İlk bitcoinlerinizi almadan önce bile, kayıp veya bilgisayar arızası durumunda paranızı kurtarabilmeniz için Bitcoin Wallet'inizin bir yedeğini almanız çok önemlidir. Bunu yapmak için "*Dosya*" sekmesine ve ardından "*Wallet'i Yedekle*" seçeneğine tıklayın.


![Image](assets/fr/20.webp)


Bu işlem, tüm bitcoinlerinizi geri yüklemek için kullanılabilecek tek bir dosya oluşturur. Bu yüzden çok dikkatli olun ve güvenli bir harici ortama kaydedin.


## Bitcoin alma


Doğrudan Knots Wallet'nıza bitcoin almak için "*Al*" düğmesine tıklayın.


![Image](assets/fr/21.webp)


Address'nize bir "*Etiket*" atayarak amacını kolayca belirleyebilir ve ileride *Coin Kontrolü* kullanımını kolaylaştırabilirsiniz. Ayrıca bu Address'den alınacak kesin bir tutarı önceden tanımlayabilir veya ödeme yapacak kişi için bir mesaj ekleyebilirsiniz. Parametreleri ayarladıktan sonra "*Ödeme talep et*" seçeneğine tıklayın.


![Image](assets/fr/22.webp)


Bitcoin Knots daha sonra kopyalayabileceğiniz veya tarayıp ödeyene gönderebileceğiniz bir alıcı Address görüntüler.


![Image](assets/fr/23.webp)


Bir işlem yayınlandıktan sonra, durumunu doğrudan "*İşlemler*" menüsünden takip edebilirsiniz.


![Image](assets/fr/24.webp)


## Bitcoin gönder


Artık Knots Wallet'inizde bitcoinler olduğuna göre, onları gönderebilirsiniz. Bunu yapmak için "*Gönder*" düğmesine tıklayın.


![Image](assets/fr/25.webp)


Bu işlem için harcamak istediğiniz UTXO'yi tam olarak seçmek için "*Girişler...*" düğmesine tıklayın.


![Image](assets/fr/26.webp)


Alıcının Bitcoin Address numarasını girin.


![Image](assets/fr/27.webp)


Bu işlemin amacını hatırlamak için bir etiket ekleyin.


![Image](assets/fr/28.webp)


Bu Address'e göndermek istediğiniz tutarı girin.


![Image](assets/fr/29.webp)


Mevcut ağ durumuna göre işleminiz için uygun ücret oranını seçmek için "*Seç...*" düğmesine tıklayın.


![Image](assets/fr/30.webp)


Her şey sizi tatmin ediyorsa, "*Gönder*" düğmesine tıklayın. Eğer bir passphrase kullanıyorsanız, bu aşamada bunu doldurmanız istenecektir.


![Image](assets/fr/31.webp)


İşlem parametrelerinizi son bir kez kontrol edin, ardından her şey doğruysa işleminizi imzalamak ve dağıtmak için tekrar "*Gönder*" düğmesine tıklayın.


![Image](assets/fr/32.webp)


Onay bekleyen işleminiz artık "*İşlemler*" sekmesinde görünmektedir.


![Image](assets/fr/33.webp)


## Düğümünüzü başka bir programa bağlama


Bitcoin Knots'un Bitcoin Wallet'inizi yönetmek için entegre Interface'i her zaman en sezgisel değildir ve işlevselliği nispeten sınırlı kalır. Bununla birlikte, Bitcoin Knots düğümünüzü özel Wallet yönetim yazılımına bağlayarak Blockchain Bitcoin verilerine kolayca erişebilir ve işlemlerinizi yayınlayabilirsiniz.


Prosedür kullanılan yazılıma bağlıdır, ancak iki ana senaryo vardır: Bitcoin Knots, Wallet yazılımınızla aynı bilgisayara kurulur veya ayrı bir makinede çalışır.


### Yerel Bitcoin Düğümleri ile :


Bilgisayarınızda Bitcoin Knots yüklüyse, yazılım dosyaları arasında `Bitcoin.conf` dosyasını bulun. Eğer bu dosya mevcut değilse, oluşturabilirsiniz. Bir metin editörü ile açın ve aşağıdaki satırı ekleyin:


```ini
server=1
```


Ardından değişikliklerinizi kaydedin.


Bunu Bitcoin-QT'nin Interface grafiği üzerinden "*Ayarlar*" kısmına giderek de yapabilirsiniz > "*Options...*" ve "*Enable RPC server*" seçeneğini etkinleştirin.


Bu değişiklikleri yaptıktan sonra yazılımı yeniden başlatmayı unutmayın.


![Image](assets/fr/34.webp)


Ardından Wallet yönetim yazılımınıza (örn. Sparrow wallet veya Liana) gidin ve işletim sisteminize bağlı olarak genellikle `Bitcoin.conf` ile aynı klasörde bulunan çerez dosyanızın yolunu girin:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


Diğer parametreleri varsayılan olarak bırakın, URL `127.0.0.1` ve port `8332`, ardından "*Test Bağlantısı*" üzerine tıklayın.


![Image](assets/fr/36.webp)


### Uzaktan kumandalı Bitcoin Düğümleri ile :


Bitcoin Knots aynı ağa bağlı başka bir makinede kuruluysa, önce yazılım dosyaları arasında `Bitcoin.conf` dosyasını bulun. Eğer bu dosya henüz mevcut değilse, oluşturabilirsiniz. Bu dosyayı bir metin editörü ile açın ve aşağıdaki satırı ekleyin:


```ini
server=1
```


Dosyayı düzenledikten sonra, işletim sisteminiz için uygun klasöre kaydettiğinizden emin olun:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

Bu işlem Bitcoin-QT'nin Interface grafikleri üzerinden de gerçekleştirilebilir. "*Ayarlar*" menüsüne gidin, ardından "*Seçenekler...*" ve ilgili kutuyu işaretleyerek "*RPC sunucusunu etkinleştir*" seçeneğini etkinleştirin. Eğer `Bitcoin.conf` dosyası mevcut değilse, "*Open Configuration File*" seçeneğine tıklayarak doğrudan bu Interface'ten oluşturabilirsiniz.


![Image](assets/fr/37.webp)


Yerel ağınızda Bitcoin Knots'u barındıran makinenin IP Address'sini bulun. Bunu yapmak için [Angry IP Scanner] (https://angryip.org/) gibi bir araç kullanabilirsiniz. Tartışma adına, düğümünüzün IP Address'sinin `192.168.1.18` olduğunu varsayalım.


Bitcoin.conf` dosyasına aşağıdaki satırları ekleyin ve `rpcbind=192.168.1.18` değerini düğümünüzün IP Address'u ile eşleşecek şekilde ayarlayın.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


Ayrıca `Bitcoin.conf` dosyasına uzak bağlantılar için bir kullanıcı adı ve parola ekleyin. Kullanıcı adınızı `loic` ve parolanızı `my_password` olarak değiştirdiğinizden emin olun:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


Dosyayı değiştirip kaydettikten sonra Bitcoin Knots'u yeniden başlatın.


Artık Wallet yönetim yazılımınıza (örneğin Sparrow wallet veya Liana) gidebilirsiniz. Sparrow'te "*Kullanıcı/Şifre*" sekmesine gidin. Bitcoin.conf dosyasında yapılandırdığınız kullanıcı adı ve şifreyi girin. Diğer parametreleri varsayılan olarak bırakın, yani URL `127.0.0.1` ve port `8332`. Ardından "*Test Bağlantısı*" üzerine tıklayın.


![Image](assets/fr/40.webp)


Bağlantı kurulmuştur.


Artık alternatif Bitcoin Knots uygulaması hakkında her şeyi biliyorsunuz.


Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca kendi Lightning düğümünüzü nasıl kuracağınızı açıkladığım bu diğer öğreticiyi de tavsiye ederim:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a