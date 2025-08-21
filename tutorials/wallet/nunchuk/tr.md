---
name: Nunchuk
description: Wallet mobil herkes için uygun
---
![cover](assets/cover.webp)



## Güçlü bir Wallet


Nunchuk 2020'nin sonlarında net bir felsefeyle ortaya çıktı: çoklu imzayı bir standart haline getirmek. Bu nedenle, tasarımı doğrudan Bitcoin ekosistemi için referans yazılım olan Bitcoin core üzerine inşa etmek gibi değerli bir seçimle çok gelişmiş işlevleri yerine getirmek üzere tasarlandı.



4 yıldan fazla süren geliştirme ve kullanım sürecinin ardından, geniş ölçekte denenmeye hazır. Yeni başlayan biriyseniz ve Nunchuk'a aşina değilseniz, bu kılavuz ilk adımlarınızı atmanıza ve ilk etkiyi atlattıktan sonra gelişmiş işlevlerini öğrenebileceğiniz bu yazılımı keşfetmenize yardımcı olacaktır. Eğitimin kendisi, tüm adımları takip etmek için gerekli becerilere sahip olan orta düzey kullanıcılara adanmıştır, ancak becerilerin nasıl artırılacağını öğrenmek için herkes için bir ilham kaynağı olabilir. Mobil versiyonla başlayacağız ve Nunchuk bilgisayarlarda da çalışacak yazılıma sahip olduğu için bu işaret gereklidir.



## İndir


İlk adım kesinlikle uygulamayı nereden indireceğinize karar vermektir. Bazı belgeleri (fazla değil ama bir başlangıç), özellik sunumunu ve sayfanın sonuna doğru tüm indirme bağlantılarını bulabileceğiniz [resmi siteye] (https://nunchuk.io/) gidin.



📌 Bu eğitim için size Software Wallet'ü Github deposundan nasıl indireceğinizi ve cep telefonunuza yüklemeden önce sürümü nasıl doğrulayacağınızı göstermeye karar verdim. **Aşağıdaki prosedür yalnızca bilgisayarınızdan yapılabilir**, bu nedenle tüm bu adımları masaüstü veya dizüstü bilgisayarınızdan yapmanızı ve - tüm doğrulamalardan sonra - `.apk` dosyasını cep telefonunuza aktarmanızı öneririm.



![image](assets/en/01.webp)



Becerileriniz çok gelişmiş değilse, resmi mağazalardan `.apk` indirmeye karar verebilir ve doğrudan bu eğitimin yapılandırma bölümüne geçebilirsiniz. Öte yandan, sıçrama yapmak istiyorsanız, adım adım takip etmeye devam edin.



Yani masaüstü bilgisayarınızdan _Açık kaynak depomuzu ziyaret edin_ seçeneğine tıklayın



Bağlantı sizi Nunchuk'un Github sayfasına götürecektir, burada bir dizi repo bulacaksınız. Biz _nunchuk-android_ olanına odaklanacağız



![image](assets/en/02.webp)



Bir sonraki ekranda, sağdaki _Yayınlar_ bölümünü bulun ve _En Son_ öğesini seçin



![image](assets/en/03.webp)



Assets_ altında, sürümü (bu örnekte 1.67.apk) SHA256SUMS dosyası ve SHA256SUMS.asc ile birlikte indirin.



![image](assets/en/04.webp)



Geliştiricinin GPG anahtarını bulmak için, deponun _Releases_ bölümüne geri dönün ve _GPG Key_ edinme ve indirme bağlantısını taşıyan 1.9.53 (veya daha önceki bir sürümü) arayın



![image](assets/en/05.webp)



Sparrow wallet tarafından sunulan, bu amaç için özel bir pencereye sahip olan ve PGP imzalarını ve SHA256 Manifestolarını destekleyen kullanışlı bir araç aracılığıyla doğrulamaya devam edeceğiz.



Ardından Sparrow'yı başlatın ve _Araçlar_ menüsünden _İndirmeyi Doğrula_ seçeneğini seçin.



![image](assets/en/06.webp)



Açılan pencerede "doldurmanız" gereken alanlar bulacaksınız: sağdaki _Browse_ düğmesini seçin ve her alan için Github'dan yeni indirdiğiniz ilgili dosyaları seçin. Tüm adımları tamamladığınızda, pencere Green onay işaretleri ve Hash manifesto onayı ile aşağıdaki gibi görünecektir.



![image](assets/en/07.webp)


**Ekran görüntüsü bir Windows PC'den alınmıştır, aynı uygulama bilgisayarınızdaki herhangi bir işletim sistemi için kullanılabilir, sadece Sparrow wallet'un yüklü olması yeterlidir. Ve doğrulandı!**



Bu Software Wallet'u indirmek için Sparrow wallet kılavuzunu bulabilirsiniz


https://planb.network/en/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Daha sonra `.apk` dosyasını bilgisayarınızdan telefonunuza aktarabilirsiniz



![image](assets/en/08.webp)



ve Nunchuk'u yükleyin



![image](assets/en/09.webp)



Telefonunuzda Nunchuk'u başlatmadan önce, Orbot'u açın ve yeni gelen uygulamayı Tor altında yönlendirilecek uygulamalar listesine koyun.



![image](assets/en/11.webp)



Şimdi Nunchuk'u çalıştırın. Bu eğitimin konusu olmayan proje özellikleri için, Nunchuk bir kez açıldığında sizi bir e-posta veya Google profili aracılığıyla oturum açmaya davet edecektir. Nunchuk Inc'in gelişmiş planlarından yararlanmayı planlamadığınız sürece, **giriş yapmaktan kaçının** ve _COPYMisafir olarak devam et_ seçeneğini seçerek devam edin.



![image](assets/en/12.webp)



## Ayarlar


Nunchuk kendisini, çalışma felsefesini anlamanın kolay olduğu ve birazdan detaylandıracağımız bir _Home_ sunum penceresi ile sunar.



En altta menüleri bulabilir ve ilk adım olarak ayarlara erişmek için _Profil_ öğesini seçebilirsiniz.



![image](assets/en/10.webp)



Ardından, hesap oluşturma davetini görmezden gelmeye devam ederek _Görüntü ayarları_ öğesini seçin.



![image](assets/en/14.webp)



Aşağıdaki ekranda Wallet'nin çevrimiçi olup olmadığını kontrol edebilir ve _bu kılavuza_ tıklayarak sunulan bağlantıdaki talimatlara çok dikkat ederek sunucunuzu bağlayabilirsiniz.



![image](assets/en/15.webp)



Ayarları _Ağ ayarlarını kaydet_ komutuyla kaydedin, _Profil_ menüsüne dönün ve _Güvenlik ayarları_ öğesini seçin.



![image](assets/en/16.webp)



Bu menüden uygulamanın açılışının nasıl savunulacağını ayarlarsınız. İstenmeyen erişimi önlemek için Nunchuk'u telefonun biyometrik özelliği ile koruyabilir ve/veya bir güvenlik PIN'i ekleyebilirsiniz.



![image](assets/en/17.webp)



Ayrıca _Profil_ penceresinde her zaman bulabileceğiniz _Hakkında_ menüsüne de bir göz atın



![image](assets/en/18.webp)



bu, uygulamanın sürümünü kontrol etmenize veya gerekirse geliştiricilerle iletişime geçmenize olanak tanır.



![image](assets/en/19.webp)



## Anahtar Üretimi ve Wallet


Nunchuk'un felsefesinden de kolayca tahmin edilebileceği gibi, yazılım çoklu imza Cüzdanlarını yönetmek için kullanışlı bir araç olarak tasarlanmıştır. Bu işlevi yerine getirmek için Nunchuk, dijital imzaları düzenlemek için gereken anahtarlardan ayırarak Wallet'ün oluşturulmasına izin verir.



Aslında, Nunchuk'un ideal çalışması, "Soğuk" olabilen anahtarlara bağlı olarak yalnızca izlenebilen Cüzdanların oluşturulmasını içerir



Önceki ekranlarda en altta _Tuşlar_ adında bir menü olduğunu fark etmiş olabilirsiniz. Nunchuk'u yeni indirdiyseniz, hem _Home_ hem de _Keys_ içinde sizi bir tuş eklemeye davet eden büyük bir düğme göreceksiniz, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Nunchuk bu şekilde çalışır:** önce generate/anahtarları içe aktarırsınız ve ardından Wallet'yı oluşturarak hangi anahtarların üzerinde depolanan fonların kilidinin açılmasına izin vereceğini seçecek şekilde yapılandırırsınız.



Wallet singlesig durumunda bile, önce anahtarı ve ardından Wallet'yi yaratırsınız. Ve şimdi yapacağımız şey de tam olarak bu, buzları kırmak ve Nunchuk'un işlevlerini keşfetmek için bir Wallet singlesig ile başlayacağız.



Anahtar Ekle_'ye tıklayın



![image](assets/en/22.webp)



Nunchuk desteklenen bir dizi imza cihazı gösterir ancak başlamak için _Yazılım_ öğesini seçin.



![image](assets/en/23.webp)



Nunchuk, cihazda saklanacak olan bir generate Mnemonic olacaktır. Daha sonra yedekleme için kelime dizisini yazmanız, en iyi çevresel koşulları yaratmanız ve bunu iyi ve sessizce yapmak için zamanınız olduğundan emin olmanız gerekir. Yazılım, ister şimdi ister daha sonra göstermeyi seçin, Mnemonic'i yalnızca bir kez gösterir, bu nedenle _Create and backup now_ seçeneğini seçin.



![image](assets/en/24.webp)



Nunchuk, hemen bir sonraki ekranda görünen 24 kelimelik Mnemonic cümleleri oluşturur



![image](assets/en/25.webp)



ve ardından hızlı bir kontrol yaparak Mnemonic dizisindeki sayıya karşılık gelen 3 seçenek arasından doğru kelimeyi seçmenizi istedi.


Eğer Mnemonic'yi doğru yazdıysanız,_Continue_ düğmesi çalışır hale gelir. Devam etmek için basın.



![image](assets/en/26.webp)



Anahtarınıza bir isim verin ve _COPYontinue_ tuşuna basın.



![image](assets/en/27.webp)



Bu adımların sonunda, Mnemonic ifadenize bir [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) ekleyip eklemeyeceğiniz sorulacaktır. passphrase'ü nasıl kullanacağınız, yedeklemesini nasıl ayarlayacağınız veya nasıl çalıştığı konusunda gerekli farkındalığa sahip değilseniz, _Bir parolaya ihtiyacım yok_ seçeneğini seçmenizi tavsiye ederim.



![image](assets/en/28.webp)



Anahtar nihayet oluşturulur ve menüde size gösterilir:




- _Key Spec_ ile ana parmak izi belirtilir
- Sağ üstteki üç noktadan oluşan ve anahtarı silebileceğiniz veya bir mesajı imzalayabileceğiniz ayarlarınız vardır
- Anahtarın adının yanında, örneğin gelecekte anahtarlarınızı düzenli tutmak için Anahtarın adını düzenleyebileceğiniz bir uç simgesi bulacaksınız.
- Son komut olarak, anahtarın sağlık durumunu kontrol edebilirsiniz: _Sağlık kontrolünü çalıştır_ tuşuna basarak, uygulamanın bir anahtarın tehlikede olup olmadığını kontrol etmesini sağlayabilirsiniz.



İşiniz bittiğinde _Done_ düğmesine tıklayın



![image](assets/en/29.webp)



Tuşlar_ menüsünde ilk tuşunuzun göründüğünü göreceksiniz.



![image](assets/en/30.webp)



Ana Sayfa_ menüsüne giderek, Wallet oluşturma seçeneği görünür. _Create new wallet_ seçeneğine tıklayın.



![image](assets/en/31.webp)



Nunchuk size, çoğunlukla şirketin sunduğu ve bu eğitimin konusu olmayan hizmetlerle ilgili bir dizi olasılık gösterir.



Bu kılavuzda detayları detaylandırarak bir _Hot Wallet ve bir _Custom wallet_ oluşturacağız.


Özel cüzdan_ ile başlayalım.



![image](assets/en/32.webp)



Basit bir şekilde, uygulama sizden bu yeni Wallet'yi adlandırmanızı ve adresler için komut dosyasını seçmenizi isteyecektir. Bu eğitim için varsayılan ayar olan _Native segwit_ ayarını bırakmayı tercih ettim. İşiniz bittiğinde, _COPYDevam_'ı seçin



![image](assets/en/33.webp)



Wallet'in yapılandırması, bu Wallet'in fonlarının hangi anahtarla açılacağını ayarlamanızı isteyerek devam eder. Birden fazla anahtar olması durumunda, aralarından seçim yapabileceğiniz bir liste gösterilecektir. Şu an için sadece bir tane oluşturduk, bu yüzden ona bir onay işareti koymayı seçiyoruz. Sağ alt köşede, Nunchuk'un sizden gelecekteki Wallet çoklu imzalarınızı nasıl ayarlamanızı isteyeceğini ve _Gerekli anahtarların_ sayısını nasıl artıracağını görebilirsiniz.



![image](assets/en/34.webp)



Bir singlesig oluşturduğumuz için `1`i bırakıyoruz ve_Continue_ butonuna tıklıyoruz.



Son olarak, Wallet'un özelliklerini kontrol edebileceğiniz bir doğrulama ekranı görünür:




- isim
- nunchuk'un Wallet singlesig'i adlandırdığı gibi `1/1 Multisig` tage
- komut dosyası türü, `Native SegWit`
- parmak izi ve türetme yolu ile birlikte `Keys` anahtarı



Memnun kaldığınızda _COPYCüzdan oluştur_ tuşuna basın



![image](assets/en/35.webp)



Wallet oluşturuldu ve [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) dosyasını yedek olarak indirebilirsiniz. Ana menüye dönmek için sol üst köşedeki oka tıklayın.



![image](assets/en/36.webp)



Yeni oluşturulan Wallet'in bakiye ve bağlantı durumunu bildirdiği _Home_ konumundasınız. Mavi alana tıklayarak Wallet'in ana işlevlerine erişebilirsiniz.



![image](assets/en/37.webp)





- Sağ üst köşedeki mercek simgesi bir işlem araması yapmanızı sağlar;
- `View Wallet config`, Wallet'nın adını düzenleyebileceğiniz ve sağ üstteki gelişmiş seçenekleri etkinleştirebileceğiniz (ekran görüntüsü alamayacağınız) yapılandırma menüsüne erişim sağlar. Burada Wallet yapılandırmasını, etiketleri dışa aktarabilir, tuşları değiştirebilir, [boşluk sınırını] (https://planb.network/en/resources/glossary/gap-limit) ve daha fazlasını değiştirebilirsiniz.



## Nunchuk ile İşlemler



Ödüller _Alınır_



![image](assets/en/38.webp)



Uygulama, Address'nin QR Kodunu gösterecek veya zincir içi fonları almak için scriptPubKey'i kopyalayacak/paylaşacak şekilde programlanmıştır.



![image](assets/en/39.webp)



Bu ilk Address'in üzerine bir UTXO geldi,



![image](assets/en/40.webp)



ancak yine de başka bir tane almak için _Receive_ düğmesine tıklıyoruz.



![image](assets/en/41.webp)



Amaç, Nunchuk'un bu yeni Address'ı size bir _Kullanılmayan adres_ olarak bildirdiğini, ancak aynı zamanda _Kullanılan adresleriniz_ olduğunu ve bunların sayısını gösterdiğini öğrenmenizdir.



### Coin kontrolü ile harcama işlemi



Bu ikinci UTXO de geldiğinde, gelen iki işlemin durumunu kontrol etmek için Wallet ana ekranına geri dönün ve en önemlisi _Madeni paraları görüntüle_ seçeneğine tıklayın



![image](assets/en/42.webp)



burada size ayrı ayrı UTXO'lar gösterilecektir. Burada, miktarın yanındaki küçük oka tıklayarak özellikle birini görüntülemeyi seçebilirsiniz



![image](assets/en/43.webp)



ve ne zaman geldiğini, açıklamayı, UTXO bloğunu kontrol edin, böylece harcanmaz ve daha fazlası.



![image](assets/en/44.webp)



Ancak sağ üst köşedeki oka tıklayarak _Coins_ menüsüne geri dönerseniz, UTXO'larınızı daha kontrollü bir şekilde harcamak için "Coin Control" seçeneğini açabilirsiniz.



Aşağıdaki örnekte, 21.000 Sats'dan UTXO'yi seçtim ve ardından sol alt köşedeki simgeye tıkladım.



![image](assets/en/45.webp)



Nunchuk bu UTXO'u harcamak için otomatik olarak _Yeni işlem_ penceresini açar. Harcama işleminde, önce tutarı manuel olarak veya _Seçilenlerin tümünü gönder_ seçeneğini seçerek, kalan oluşturmadan tüm Coin kontrol bakiyesini göndermelisiniz. Tutar ayarlandıktan sonra _Devam_ seçeneğini seçin



![image](assets/en/46.webp)



Şimdi Nunchuk, bu fonların aktarılacağı Address'nin nereye yapıştırılacağını, bir açıklamanın detaylandırılacağını ve işlemin sonlandırılacağını gösterir.



![image](assets/en/47.webp)



Create transaction_ seçeneğini seçmek, otomatik ücret ve işlem yönetimini uygulamaya devreder. Daha fazla kontrol için _Custom transaction_ seçeneğini seçmenizi öneririm.



Bu yeni ekranda aşağıdakileri seçmek önemlidir




- gW-51'de bulunan başka bir UTXO tarafından ücretlerin ödenmesini, harcanmasını ve bir kalıntı oluşturmasını (bu önlenebilir bir gizlilik kaybıdır) önlemek için _Gönderme tutarından ücreti çıkarın_;
- ve ardından gezgini kontrol ettikten sonra ücretleri manuel olarak ayarlayın.



Tüm bu adımları tamamladıktan sonra _COPYDevam_ üzerine tıklayın



![image](assets/en/48.webp)



Bir sonraki ekran işlemin tam özetidir. Her şey tamamsa, _Confirm and create transaction_ seçeneğini seçerek onaylayın.



![image](assets/en/49.webp)



Bekleyen imzalar_ ile Nunchuk, işlemin harcamayı onaylamak için sizin imzanızı beklediğini bildirir ve siz de _İmzala_ düğmesine tıklayarak bu imzayı eklersiniz.



![image](assets/en/50.webp)



Sonlandırılmış ve imzalanmış işlemi yaymak için en altta _Broadcast_ komutu görünür.



![image](assets/en/51.webp)



### Menüden harcama işlemi _Gönder_



Wallet'ün ana sayfasında işlemin dışarı çıktığını ve onay beklediğini görürken, günlük bir harcamayı simüle etmek için _Gönder_ menüsünü kullanırız.



![image](assets/en/52.webp)



Aslında _Send_ (Gönder) düğmesine tıklandığında, az önce görülenle aynı olan ancak Coin kontrolünden geçmeyen işlem gönderme ekranı açılır.



Ayrıca bu ikinci örnekte _Custom transaction_ seçeneğini seçip tüm tutarı göndermeye karar verdim, ancak bunu manuel olarak da ayarlayabilirdim. Gönderilecek tutara karar verdikten sonra _Continue_ tuşuna basın.



![image](assets/en/53.webp)



Ardından her zaman ücretlerin söz konusu UTXO'dan çıkarılıp çıkarılmayacağına karar verin (bu örnekte seçim zorunludur, çünkü sadece bir tane vardır), ücretleri Mempool'teki o anki duruma göre manuel olarak ayarlayın ve _Continue_ tuşuna basın.



![image](assets/en/54.webp)



Özet ekranı tatmin edici ise, _Confirm and create transaction_ (Onayla ve işlemi oluştur) seçeneğini seçin.



![image](assets/en/55.webp)



İşlemi _Sign_ ile imzalayın



![image](assets/en/56.webp)



ve ağa yaymak.



![image](assets/en/57.webp)



Wallet, bakiyenin sıfır olduğu ve geçmişin güncellendiği bu noktadadır.



![image](assets/en/58.webp)



## Bir "Hot Wallet" oluşturulması



Son olarak ve Nunchuk mobile'ın ilk aşamalarından hiçbir şeyi dışarıda bırakmamak için, bunun uygulamanın "Hot Wallet" dediği şeyi nasıl yarattığını görelim



Nunchuk'un _Home_ menüsünde, Cüzdanlar listesinin göründüğü yerde, sağ üst köşedeki `+` işaretine tıklayın.



![image](assets/en/59.webp)



Seçeneklerden _Sıcak cüzdan_ öğesini seçin



![image](assets/en/60.webp)



Nunchuk, sunum sayfasında Hot Cüzdanlarının kullanımı hakkında bazı tavsiyelerde bulunur ve devam etmek için _COPY Devam_ seçeneğini seçersiniz.



![image](assets/en/61.webp)



Birkaç dakika sonra Wallet oluşturulur ve listede kahverengimsi renkte görünür. Bu, Nunchuk'un Wallet'ü henüz yedeklemediğinize dair sizi uyardığı renktir.



![image](assets/en/62.webp)



Yapılandırmalarına erişmek için Wallet'in adına tıklayın ve Mnemonic ifadesini hemen yedeklemek için bir davet görebilirsiniz.



![image](assets/en/63.webp)



Prosedür daha önce gördüğümüzle aynıdır, bu yüzden tekrar üzerinde durmayacağız. İşlem tamamlandığında, Nunchuk sizi _COPYustom_ prosedürü ile oluşturduğunuz gibi düzenleyebileceğiniz ilgili anahtar sayfasına götürecektir.



![image](assets/en/64.webp)



Ayrıca _Sağlık kontrolünü çalıştır_'ı deneyin



![image](assets/en/65.webp)



veya tüm Cüzdanlarınızı uygulamanın _Home_ bölümünde nasıl görüntüleyeceğinizi görmek için.



![image](assets/en/66.webp)



## Bağımsız olarak devam etmeyi akılda tutmak için


Oluşturma için nasıl bir sıra varsa, yani önce anahtarları sonra Wallet'yı oluşturuyorsanız, bu öğeleri uygulamanızdan silmek için de ters sırayı korumanız gerekecektir.



Anahtarlardan birini silmeniz gerekiyorsa, önce Wallet'yi veya işlemler için imza anahtarlarından birini kullanan Cüzdanları silme öngörüsüne sahip olmalısınız: önce Cüzdanları, ardından anahtarları silersiniz. Bu sırayı takip etmezseniz, kendinizi anahtarı kaldıramaz halde bulursunuz.



Artık Nunchuk ile nasıl başlayacağınızı bildiğinize göre, bu uygulamayı incelemeye ve sırlarını keşfetmeye devam edebilirsiniz. Bu eğitimde sadece ilk adımları attık, ancak bu Software Wallet'in karşılamanıza yardımcı olabileceği daha sofistike uygulamalar ve gelişmiş ihtiyaçlar var.