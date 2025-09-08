---
name: Nerdminer
description: 0'a yakın kazanma şansı ile Mining Bitcoin'a başlayın
---

![cover](assets/cover.webp)

**NerdMiner_v2** cihazınızı ayarlama


Bu eğitimde, Bitcoin Mining'e adanmış bir donanım cihazı (bir ESP-32 S3) olan NerdMiner_v2'yi kurmak için gerekli adımlarda size rehberlik edeceğiz.

Açıkçası, böyle bir cihazın hesaplama gücü amatör veya profesyonel madencilerin ASIC'leriyle rekabet edemez. Yine de NerdMiner, Bitcoin Mining'i somut hale getirmek için mükemmel bir eğitim aracıdır. Ve kim bilir, (çok) şanslıysanız, bir blok ve onunla birlikte gelen ödülü bulabilirsiniz. Meraklısı için, [Kazanma olasılığının tahmini] (#estimation-de-la-probabilite-de-gain) bölümünde göreceğiz. Güç tüketimi açısından, bir NerdMiner 0,5W tüketir; karşılaştırma için, bir LED lamba ortalama 20 kat daha fazla tüketir.


Farklı adımlara geçmeden önce, bunu yapmak için gerekli ekipmanı listeleyelim:



- a [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- a [USB-C güç Supply](https://amzn.eu/d/gIOot90)
- 3D kılıf: 3D yazıcınız varsa [3D dosyasını] (https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) indirebilirsiniz, aksi takdirde [Silexperience çevrimiçi mağazasından] (https://silexperience.company.site/NerdMiner_V2-p544379757) bir tane satın alabilirsiniz.
- chrome Tarayıcı yüklü bir bilgisayar
- bir internet bağlantısı
- a Bitcoin Address


Ayrıca, aşağıdaki gibi çeşitli satıcılardan önceden monte edilmiş bir NerdMiner kiti satın alabilirsiniz:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


İlk olarak, yazılımı ESP-32 S3'e nasıl yükleyeceğimizi göreceğiz ve ardından wifi ağını değiştirmek için nasıl yeniden başlatacağımızı göreceğiz. Bu adımlar Windows kullanıcıları içindir, eğer bir Linux işletim sistemi kullanıyorsanız, ESP-32 S3'ün sisteminiz tarafından tanınmasını sağlamak için lütfen [ön adımları] (#etapes-preliminaires-pour-utilisateurs-linux) gerçekleştirin.


NerdMiner_v2 Yazılımının** kurulumu webflasher kullanımı sayesinde büyük ölçüde basitleştirilmiştir.


## Adım 1: Webflasher'ın Hazırlanması


Öncelikle [online NM2 flasher] (https://bitmaker-hub.github.io/diyflasher/) adresine gitmeniz gerekir.


Ardından ESP-32'nize karşılık gelen ürün yazılımını seçin. Çoğu zaman bu varsayılan olandır: T-Display S3. Ardından "Flash" üzerine tıklayın.


**Note⚠️ :** varsayılan olarak flash kullanımına ve USB bağlantı noktalarınıza erişime izin verdiği için Chrome tarayıcısını kullanmanız önemlidir.


![image](assets/webflasher.webp)


## Adım 2: ESP-32'nin Bağlanması


Webflasher başlatıldığında, tarayıcı tarafından tanınan farklı USB bağlantı noktalarını gösteren bir açılır pencere açılacaktır.

Daha sonra ESP-32'nizi bağlayabilirsiniz ve yeni bir port görüntülenecektir (bu durumda, bu ttyACM0 portudur). Daha sonra bunu seçmeli ve "bağlan "a tıklamalısınız.


![image](assets/flasher-port-serial.webp)


Yazılım daha sonra birkaç saniye içinde ESP32'nize indirilecektir.


![image](assets/NM2-sucessfully-installed.webp)


## Adım 3: NerdMiner Yapılandırması


NerdMiner'ınızın yapılandırması bir akıllı telefon veya bilgisayar aracılığıyla yapılacaktır.

WiFi'yi etkinleştirin ve yerel NerdMinerAP ağına bağlanın. Bir akıllı telefon kullanıyorsanız, yapılandırma portalı otomatik olarak açılacaktır. Aksi takdirde, bir tarayıcıya Address 192.168.4.1 yazın.

Ardından "WiFi Yapılandır" öğesini seçin.


Artık NerdMiner'ınızı yapılandırabilirsiniz.

İlk olarak, ağ adınızı seçerek ve ilgili şifreyi girerek WiFi ağınıza bağlanarak başlayın.


Daha sonra katılmak istediğiniz Mining pool'i seçebilirsiniz. Aslında, Bitcoin Mining endüstrisinde, sağlanan Hashrate ile orantılı olarak ödülü paylaşmak için Exchange'de bir blok bulma şansını artırmak için hesaplama gücünü bir araya getirmek yaygındır.

NerdMiners için bu havuzlardan birine bağlanmayı seçebilirsiniz:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Havuzunuzu seçtikten sonra, (istisnai olarak) bir blok bulunması durumunda ödülü almak için Bitcoin Address'nızı girmeniz gerekir.


Ayrıca, NerdMiner'ın saati doğru görüntüleyebilmesi için saat diliminizi seçin.

Şimdi "kaydet "e tıklayabilirsiniz.


![image](assets/wifi-configuration.webp)


Tebrikler, artık Bitcoin Mining ağının bir parçasısınız!


## NerdMiner Operasyonu


NerdMinerv2 yazılımı, ekranınızın sağ tarafındaki üst düğmeye tıklayarak erişebileceğiniz 3 farklı ekrana sahiptir:



- Ana ekran NerdMiner'ınızın istatistiklerine erişim sağlar.
- İkinci ekran saate, Hashrate'nize, Bitcoin fiyatına ve blok yüksekliğine erişim sağlar.
- Üçüncü ekran küresel Bitcoin Mining ağına ilişkin istatistiklere erişim sağlar.

![image](assets/NM2-screens.webp)


NerdMiner'ınızı yeniden başlatmak istiyorsanız, örneğin WiFi ağını değiştirmek için, üst düğmeye 5 saniye boyunca basmanız gerekir.


Alttaki düğmeye bir kez basmak NerdMiner'ınızı kapatacaktır. İki kez tıklamak ekran yönünü döndürür.


### Linux kullanıcıları için ön adımlar


Chrome'un Linux'ta seri bağlantı noktanızı algılaması için gereken adımları aşağıda bulabilirsiniz.


1. İlişkili bağlantı noktasını tanımlayın:



- ESP-32'nizi bilgisayarınıza bağlayın.
- Bir terminal açın.
- Tüm bağlantı noktalarını listelemek için aşağıdaki komutu girin:
  - `dmesg | grep tty`
  - veya `ls /dev/tty*`
- Bağlantı noktasından emin olmak için, ESP-32 bağlı olmadan komutu tekrarlayarak eleme yöntemiyle ilerleyebilirsiniz.


2. İlişkili bağlantı noktasının iznini değiştirin:



- Varsayılan olarak, seri portlara erişim root izinleri gerektirebilir, bu nedenle kullanıcınızı `dialout` grubuna ekleyerek bunları kullanılabilir hale getireceğiz.
  - `sudo usermod -a -G dialout YOUR_USERNAME`, `YOUR_USERNAME` yerine kullanıcı adınızı yazın.
  - ardından oturumu kapatıp bu kullanıcı olarak tekrar oturum açın veya grup değişikliklerinin etkili olmasını sağlamak için sistemi yeniden başlatın.


Artık ESP-32'niz sisteminiz tarafından tanındığına göre, yazılım kurulumu için [ilk adıma] (#etape-1-preparation-du-webflasher) geri dönebilirsiniz.


## Sonuç


Ve işte oldu! NerdMiner_v2'niz artık yapılandırıldı ve kullanıma hazır.


Mutlu Mining'ler ve şans sizden yana olsun!


### Kazanma olasılığının tahmin edilmesi


Bir Block reward kazanma olasılığını tahmin ederken biraz eğlenelim. Bu tahmin kaba olacak ve yalnızca olasılığın büyüklük sırasını elde etmeyi amaçlayacaktır.

Bir NerdMiner'ın bağlanabileceği havuz yalnızca "solo Mining pool "dır, bu da havuzun bağlı tüm madencilerin Hashrate'lerini karşılıklı hale getirmediği, yalnızca bir koordinatör olarak hareket ettiği anlamına gelir.

Şimdi NerdMiner'ımızın yaklaşık 45kH/s'lik bir Hashrate'e sahip olduğunu varsayalım.


Toplam Hashrate'un yaklaşık 450 EH/s (veya saniyede 4,5 x 10^20 hash) olduğunu bilerek, bir sonraki bloğu bulma olasılığının 100 milyon milyarda 1 olduğunu düşünebiliriz ki bu da gerçekleşmesi çok çok düşük bir ihtimaldir. Dolayısıyla bir NerdMiner, bir eğitim aracı ve merak nesnesi olmanın yanı sıra, Bitcoin Mining'de 0,5 W'lık marjinal bir elektrik maliyetiyle bir piyango bileti olarak da kullanılabilir - ancak az önce gördüğümüz gibi kazanma olasılığı gülünç derecede düşüktür. Yine de neden şansınızı zorlamıyorsunuz?


### Ek Bilgi


Konu hakkında daha fazla okumak isterseniz işte bazı bağlantılar:



- [NerdMiner_v2 proje sayfası](http://github.com/BitMaker-hub/NerdMiner_v2)
- [NerdMiners'ın eksiksiz dokümantasyonu](https://docs.bitwater.ch/nerd-Miner-v2/)