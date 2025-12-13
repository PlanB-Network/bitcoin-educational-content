---
name: Specter DIY
description: Spectre DIY için kurulum kılavuzu
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunk'lar kod yazar. Birilerinin mahremiyeti savunmak için yazılım yazması gerektiğini biliyoruz ve hepimiz bunu yapmazsak mahremiyeti elde edemeyeceğimize göre, bunu biz yazacağız.

*Bir Cypherpunk'ın Manifestosu - Eric Hughes - 9 Mart 1993*


Projenin amacı, kullanıma hazır bileşenlerden bir donanım wallet oluşturmaktır.

Her şeyi güzel bir form faktörüne sokan ve lehimlemeden kaçınmanıza yardımcı olan bir uzatma kartımız olsa da, standart bileşenlerle uyumluluğu desteklemeye ve sürdürmeye devam edeceğiz.


![image](assets/fr/01.webp)


Ayrıca projeyi, minimum değişiklikle başka herhangi bir bileşen setinde çalışabilecek şekilde esnek tutmak istiyoruz. Belki de farklı bir mimaride (RISC-V?), iletişim kanalı olarak bir ses modemi ile bir donanım wallet yapmak istiyorsunuz - bunu yapabilmelisiniz. Spectre'nin işlevselliğini eklemek veya değiştirmek kolay olmalıdır ve mantıksal modülleri olabildiğince soyutlamaya çalışıyoruz.


QR kodları, Spectre'nin ana bilgisayarla iletişim kurması için varsayılan bir yoldur. QR kodları oldukça kullanışlıdır ve kullanıcının veri iletimini kontrol etmesini sağlar - her QR kodunun çok sınırlı bir kapasitesi vardır ve iletişim tek yönlü olarak gerçekleşir. Ve hava bağlantılıdır - wallet'ü herhangi bir zamanda bilgisayara bağlamanız gerekmez.


Sır saklama için agnostik modu (wallet kapatıldığında tüm sırları unutur), pervasız modu (sırları uygulama mikrodenetleyicisinin flaşında saklar) destekliyoruz ve secure element entegrasyonu yakında geliyor.


Ana odak noktamız diğer donanım cüzdanlarıyla çoklu imza kurulumudur, ancak wallet tek bir imzalayıcı olarak da çalışabilir. İmzasız işlemler için PSBT, çoklu imza cüzdanlarını içe/dışa aktarmak için wallet tanımlayıcıları gibi elimizden geldiğince Bitcoin Core ile uyumlu hale getirmeye çalışıyoruz. Bitcoin Core ile daha kolay iletişim kurmak için [Spectre Desktop app] (https://github.com/cryptoadvance/specter-desktop) üzerinde de çalışıyoruz - Bitcoin Core düğümünüzle konuşan küçük bir python flask sunucusu.


Aygıt yazılımının çoğu MicroPython'da yazılmıştır, bu da kodun denetlenmesini ve değiştirilmesini kolaylaştırır. Eliptik eğri hesaplamaları için Bitcoin Core'dan [secp256k1](https://github.com/bitcoin-core/secp256k1) kütüphanesini ve GUI için [LittlevGL](https://lvgl.io/) kütüphanesini kullanıyoruz.


## Sorumluluk Reddi


Proje, Spectre-DIY'nin güvenlik seviyesinin artık piyasadaki ticari donanım cüzdanlarıyla karşılaştırılabilir olduğu ölçüde önemli ölçüde olgunlaştı. Ürün yazılımı yükseltmelerini doğrulayan güvenli bir önyükleyici uyguladık, böylece ilk kurulumdan sonra cihaza yalnızca imzalı ürün yazılımının yüklenebileceğinden emin olabilirsiniz. Ancak, ticari imzalı cihazların aksine, önyükleyicinin kullanıcı tarafından manuel olarak yüklenmesi gerekir ve cihaz satıcısının fabrikasında ayarlanmaz. Bu nedenle, ilk aygıt yazılımı yüklemesi sırasında ekstra dikkat gösterin ve PGP imzalarını doğruladığınızdan ve aygıt yazılımını güvenli bir bilgisayardan flash'ladığınızdan emin olun.


Bir şey çalışmazsa burada bir sorun açın veya [Telegram grubumuzda] bir soru sorun (https://t.me/+VEinVSYkW5TUl5Ai).


## Spectre-DIY için alışveriş listesi


Burada ne satın alacağınızı açıklıyoruz ve bir sonraki montaj bölümünde nasıl bir araya getireceğinizi ve kartla ilgili birkaç notu açıklıyoruz - güç atlama telleri, USB bağlantı noktaları vb.


### Keşif panosu


Cihazın ana parçası geliştirici kartıdır:



- STM32F469I-DISCO geliştirici kartı (örneğin [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) veya [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB kablo
- USB üzerinden iletişim için standart MicroUSB kablosu


İsteğe bağlı ama tavsiye edilir:


- [Waveshare QR kod tarayıcı](https://www.waveshare.com/barcode-scanner-module.htm) ile tarayıcıyı panoya bağlamak için [bunlar](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) veya [bunlar](https://www.amazon.com/gp/product/B015KA0RRU/) gibi uzun pin başlıkları (4 pin başlığı gereklidir).


Şu anda bir akıllı kart yuvası, QR kod tarayıcı, pil ve 3 boyutlu baskılı bir kasa içeren bir uzatma kartı üzerinde çalışıyoruz, ancak ana parçayı içermiyor - ayrı olarak sipariş etmeniz gereken keşif kartı. Bu şekilde, güvenlik açısından kritik bileşenler rastgele bir elektronik mağazasından satın alındığı için tedarik zinciri saldırısı hala bir sorun değildir.


Spectre'yi herhangi bir ekstra bileşen olmadan da kullanmaya başlayabilirsiniz, ancak onunla USB veya dahili SD kart yuvası üzerinden iletişim kurabilirsiniz. Spectre'yi USB üzerinden kullanmak, hava bağlantısının olmadığı anlamına gelir, bu nedenle önemli bir güvenlik özelliğini kaybedersiniz.


### QR tarayıcı


QR kod tarayıcısı için birkaç seçeneğiniz vardır.


**Seçenek 1. Tavsiye edilir.** Waveshare'den oldukça iyi bir tarayıcı (40$)


[Waveshare tarayıcı](https://www.waveshare.com/barcode-scanner-module.htm) - güzelce monte etmenin bir yolunu bulmanız gerekecek, belki bir çeşit Arduino Prototip kalkanı ve biraz ducktape kullanabilirsiniz.


Lehimleme gerekmez, ancak lehimleme becerileriniz varsa wallet'u çok daha güzel hale getirebilirsiniz ;)


**Seçenek 2.** Mikroe'dan çok güzel bir tarayıcı ama oldukça pahalı (150$):


[Barkod Tıklama](https://www.mikroe.com/barcode-click) + [Adaptör](https://www.mikroe.com/arduino-uno-click-shield)


**Seçenek 3.** Başka herhangi bir QR tarayıcı


Çin'de bazı ucuz tarayıcılar bulabilirsiniz. Kaliteleri genellikle o kadar iyi değildir, ancak şansınızı deneyebilirsiniz. Belki ESPcamera bile işinizi görebilir. Sadece güç, UART (D0 ve D1 pinleri) ve D5'e tetikleyici bağlamanız gerekir.


**Seçenek 4.** Tarayıcı yok.


O zaman Spectre'yi yalnızca USB / SD Kart ile kullanabilirsiniz.


QR kodları yerine başka bir şey kullanan kendi iletişim modülünüzü oluşturmadığınız sürece - audiomodem, bluetooth veya başka bir şey. Tetiklenebildiği ve verileri seri üzerinden gönderebildiği anda istediğinizi yapabilirsiniz.


### İsteğe bağlı bileşenler


Küçük bir güç bankası veya bir pil ve güç şarj cihazı / güçlendirici eklerseniz, wallet'iniz tamamen bağımsız hale gelir ;)



## Specter-DIY'nin Montajı



![video](https://youtu.be/1H7FqG_FmCw)


### Waveshare Barkod tarayıcıyı bağlama


wallet aygıt yazılımı ilk çalıştırmada tarayıcıyı sizin için yapılandıracaktır, bu nedenle manuel ön yapılandırma gerekmez.


Tarayıcıyı panoya şu şekilde bağlayabilirsiniz:


![image](assets/fr/02.webp)


Kolaylık sağlamak için bir Arduino Protype shield satın alabilir ve her şeyi üzerine lehimleyip monte edebilirsiniz (örneğin [bu](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Güç yönetimi


Kartın üst tarafında, gücü nereden alacağını tanımlayan bir jumper vardır. Jumper'ın konumunu değiştirebilir ve güç kaynağını USB portlarından biri veya VIN pini olarak seçebilir ve harici pili buraya bağlayabilirsiniz (5V olmalıdır).


### DIY için Muhafaza


Enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) klasörüne göz atın.


### Yaratıcı olun!


Kendi Spectre-DIY'ınızı bir araya getirin ve resimleri bize gönderin (bir çekme talebi oluşturun veya bize ulaşın).


Topluluk tarafından bir araya getirilen Hayaletler ile [Galeri](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md)'ye göz atın!




## Derlenmiş kodun yüklenmesi


Güvenli önyükleyici ile aygıt yazılımının ilk kurulumu biraz farklıdır. Yükseltmeler daha kolaydır ve wallet donanımının bilgisayara bağlanmasını gerektirmez.


![video](https://youtu.be/eF4cgK_L6T4)


### İlk ürün yazılımının yanıp sönmesi


**Not** Sürümlerdeki ikili dosyaları kullanmak istemiyorsanız, bizimkiler yerine ortak anahtarlarınızı kullanmak için nasıl derleyeceğinizi ve yapılandıracağınızı açıklayan [bootloader belgelerine] (https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) göz atın.



- 1.4.0`ın altındaki sürümlerden yükseltme yapıyorsanız veya aygıt yazılımını ilk kez yüklüyorsanız, [releases](https://github.com/cryptoadvance/specter-diy/releases) sayfasındaki `initial_firmware_<version>.bin` dosyasını kullanın.
 - Sha256.signed.txt` dosyasının imzasını [Stepan'ın PGP anahtarı] ile doğrulayın (https://stepansnigirev.com/ss-specter-release.asc)
 - Initial_firmware_<version>.bin` dosyasının hash'ini `sha256.signed.txt` dosyasında saklanan hash ile karşılaştırarak doğrulayın
- Boş bir önyükleyiciden yükseltme yapıyorsanız veya önyükleyici hata mesajında aygıt yazılımının geçerli olmadığını görüyorsanız, bir sonraki bölüme göz atın - İmzalı Spectre aygıt yazılımını flaş etme.
- Keşif kartınızın güç jumper'ının STLK konumunda olduğundan emin olun
- Keşif kartını, kartın üst kısmındaki **miniUSB** kablosu aracılığıyla bilgisayarınıza bağlayın.
    - Kart, `DIS_F469NI` adlı çıkarılabilir bir disk olarak görünmelidir.
- Initial_firmware_<version>.bin` dosyasını `DIS_F469NI` dosya sisteminin kök dizinine kopyalayın.
- Kartın aygıt yazılımının yanıp sönmesi tamamlandığında kart kendini sıfırlayacak ve önyükleyiciye yeniden başlayacaktır. Önyükleyici aygıt yazılımını kontrol edecek ve ana aygıt yazılımına önyükleme yapacaktır. Aygıt yazılımı bulunamadığına dair bir hata mesajı görürseniz güncelleme talimatlarını izleyin ve aygıt yazılımını SD kart aracılığıyla yükleyin.
- Artık güç jumper'ını istediğiniz yere getirebilir ve kartı powerbank veya bataryadan çalıştırabilirsiniz.


İlk aygıt yazılımını `.bin` dosyasını kopyalayıp yapıştırarak flaş etmek bazen başarısız olur - genellikle kablo nedeniyle veya cihazı bir USB hub üzerinden bağlarsanız. Bu durumda birkaç kez daha deneyebilirsiniz (normalde 2-3 denemede çalışır).


Eğer her zaman başarısız oluyorsa [stlink](https://github.com/stlink-org/stlink/releases/latest) açık kaynak aracını kullanabilirsiniz. Yükleyin ve terminalinize yazın: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Genellikle çok daha güvenilir çalışır.


### Ürün yazılımını yükseltme



- Specter_upgrade_<version>.bin` dosyasını [releases](https://github.com/cryptoadvance/specter-diy/releases) adresinden indirin.
- Bu ikili dosyayı SD kartın kök dizinine kopyalayın (FAT formatlı, maksimum 32 GB)
 - Kök dizinde yalnızca bir `specter_upgrade***.bin` dosyası olduğundan emin olun
- SD kartı keşif kartının SD yuvasına takın ve kartı açın
- Bootloader aygıt yazılımını flaş edecek ve tamamlandığında sizi bilgilendirecektir.
- Kartı yeniden başlatın - şimdi Spectre-DIY arayüzünü göreceksiniz, PIN kodunuzu seçmenizi önerecektir


Yeni bir sürüm çıktığında, sürümlerden `specter_upgrade_<version>.bin` dosyasını indirin, SD karta bırakın ve önceki adımda olduğu gibi cihazı yükseltin. Bootloader, karta yalnızca imzalı ürün yazılımının yüklenebildiğinden emin olacaktır.


### Aygıt yazılımı sürümü nasıl öğrenilir


Cihaz ayarları menüsüne gidin - ekran başlığının altında sürüm numarasını gösterecektir.


## Specter-DIY wallet kullanın



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Spectre-DIY'nin Güvenliği


### Donanım


Ekran, uygulama MCU'su tarafından kontrol edilir.


Güvenli eleman entegrasyonu henüz mevcut değildir - şu anda sırlar da ana MCU'da saklanmaktadır. Ancak wallet'yı sırrı saklamadan kullanabilirsiniz - her seferinde kurtarma cümlenizi girmeniz gerekir. Tüm anımsatıcıyı hatırlayabiliyorsanız neden uzun passphrase'i hatırlayasınız ki?


Cihaz bazı dosyaları depolamak için harici flaş kullanır (QSPI), ancak tüm kullanıcı dosyaları wallet tarafından imzalanır ve yüklendiğinde kontrol edilir.


QR tarama işlevi ayrı bir mikrodenetleyicidedir, böylece tüm görüntü işleme güvenlik açısından kritik MCU'nun dışında gerçekleşir. Şu anda USB ve SD kart hala ana MCU tarafından yönetilmektedir, bu nedenle saldırı yüzeyini azaltmak istiyorsanız SD kart ve USB kullanmayın.


### PIN koruması (kullanıcı kimlik doğrulaması)


İlk açılış sırasında ana MCU üzerinde benzersiz bir sır oluşturulur. Bu sır, cihazın kötü niyetli bir cihazla değiştirilmediğini doğrulamanızı sağlar - PIN kodunu girdiğinizde, sır orada olduğu sürece aynı kalacak bir kelime listesi görürsünüz.


PIN kodunuz bu benzersiz sır ile birlikte generate anahtarlarınız için bir şifre çözme anahtarı Bitcoin için kullanılır (eğer onları saklarsanız). Dolayısıyla, saldırgan PIN ekranını atlayabilirse, şifre çözme yine de başarısız olacaktır.


Aygıt yazılımını kilitlediyseniz (TODO: buraya talimatlar bağlantısını ekleyin), sırrı da etkili bir şekilde kilitleyecektir, bu nedenle saldırgan karta farklı bir aygıt yazılımı yüklerse sır silinir ve PIN kodunu girmeye başladığınızda bunu tanıyabilirsiniz - kelime dizisi farklı olacaktır.


### Kurtarma cümlesinin oluşturulması


Bu, wallet'in en önemli parçalarından biridir - anahtarı güvenli bir şekilde generate yapmak. Bunu iyi yapmak için birden fazla entropi kaynağı kullanırız:



- Mikrodenetleyicinin TRNG'si. Tescilli, sertifikalı ve muhtemelen iyi ama biz buna güvenmiyoruz
- Dokunmatik ekran. Ekrana her dokunduğunuzda, konumu ve bu dokunuşun gerçekleştiği anı ölçüyoruz (180MHz'de mikrodenetleyici tiklerinde).
- Dahili mikrofonlar - henüz değil. Kartın iki mikrofonu vardır, böylece donanım wallet sizi dinleyebilir ve bu verileri entropi havuzuna karıştırabilir.


Tüm bu entropi bir araya getirilir ve kurtarma cümlenize dönüştürülür. Elde edilen entropi her zaman tek tek kaynakların herhangi birinden daha iyidir.


### Yüksek seviye mantık - cüzdanlar


Spectre bir anahtar deposu olarak çalışır. Cüzdanlarda yer alabilecek HD özel anahtarlarını tutar. Cüzdanlar tanımlayıcıları tarafından tanımlanır. Miniscript'i de destekliyoruz.


Her wallet belirli bir ağa aittir. Bu, `testnet` üzerinde bir wallet içe aktardıysanız, `mainnet` veya `regtest` üzerinde mevcut olmayacağı anlamına gelir - bu ağa geçmeniz ve wallet'ü ayrı olarak içe aktarmanız gerekir.


### İşlem doğrulama


wallet'in imzalayacağı işlemler için aşağıdaki kurallar geçerlidir:



- farklı cüzdanlardan karışık girdiler bulunursa kullanıcı uyarılır ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- değişiklik çıktıları gönderildikleri wallet'nın adını gösterir
- multisig veya miniscript kullanmak için öncelikle wallet tanımlayıcısını ekleyerek wallet'yi içe aktarmanız gerekir (QR, USB veya SD kart üzerinden)


## Tanımlayıcılar desteği


Tüm normal Bitcoin tanımlayıcıları çalışır. Bunun dışında birkaç uzantımız var:


### Tanımlayıcılarda çoklu dallar


QR kodlarında biraz yer kazanmak için tek seferde birden fazla dal içeren tanımlayıcıların eklenmesine izin veriyoruz. Eğer adres almak için `wpkh(xpub/0/*)` ve adres değiştirmek için `wpkh(xpub/1/*)` kullanmak istiyorsanız, bunları tek bir tanımlayıcıda birleştirebilirsiniz: `wpkh(xpub/{0,1}/*)` - wallet `{}` setinin ilk indeksini adres alma dalı, ikincisini ise adres değiştirme dalı olarak değerlendirecektir.


Ayrıca ikiden fazla dal belirtebilirsiniz ve dal indeksleri farklı kefiller için farklı olabilir, bu nedenle bu tanımlayıcı çok garip ama tamamen geçerlidir:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Burada 17 numaralı adresi almak için wallet `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))` komut dosyasını kullanacaktır.


Tek gereklilik, tüm kümelerdeki dizin sayısının aynı olmasıdır (yukarıdaki durumda 3).


### Varsayılan türetmeler


Tanımlayıcı ana genel anahtarlar içeriyor ancak joker karakter türetmeleri içermiyorsa, tanımlayıcıdaki tüm genişletilmiş anahtarlara varsayılan `/{0,1}/*` türetmesi eklenecektir. Eğer xpub'lardan en az birinde joker türetme varsa, tanımlayıcı değiştirilmeyecektir.


Wpkh(xpub)` tanımlayıcısı `wpkh(xpub/{0,1}/*)` tanımlayıcısına dönüştürülecektir.


### Miniscript


Spectre miniscript'i destekler, ancak politikadan miniscript'e derlemeyi desteklemez (çünkü çok pahalıdır). Miniscript üzerinde bazı kontroller gerçekleştiriyoruz, bu nedenle üst seviyede sadece `B` scriptlerine izin veriliyor ve alt-miniscriptlerdeki tüm argümanların [spec](http://bitcoin.sipa.be/miniscript/)'e göre özelliklere sahip olması gerekiyor.


Bir ilkeden bir tanımlayıcıyı generate'e aktarmak için [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) adresini kullanabilir ve ardından bunu wallet'ye aktarabilirsiniz.


Örneğin, "Şimdi harcayabilirim veya 100 gün içinde eşim harcayabilir" şeklindeki bir politika wallet'e şu şekilde dönüştürülebilir:


Politika: `or(9@pk(xpubA),and(older(14400),pk(B)))` (benim anahtarım 9 kat daha olası)


Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Burada herhangi bir joker karakter türevimiz olmadığından, varsayılan `/{0,1}/*` türevleri xpub'lara eklenecektir.



---

MIT Lisansı


Telif hakkı (c) 2019 cryptoadvance


---