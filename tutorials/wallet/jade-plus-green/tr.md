---
name: Jade Plus - Green
description: Jade Plus'ı Green ile kolayca yapılandırın
---
![cover](assets/cover.webp)


![video](https://youtu.be/rv_cN7F7-TM)


Jade Plus, Blockstream tarafından tasarlanmış sadece Bitcoin'e özel bir Hardware Wallet'dir. Yazılım geliştirmeleri, daha fazla seçenek ve daha sezgisel kullanım için yeniden tasarlanmış ergonomi ile klasik Jade'in halefidir. Bu yeni sürüm, öncekinden daha geniş bir renk gamına sahip muhteşem bir 1,9 inç LCD ekrana sahiptir. Düğmeler ve menü navigasyonu da optimize edilmiştir.


Jade Plus çeşitli şekillerde kullanılabilir: USB-C kablolu bağlantı yoluyla, mikro SD kartla "*Air-Gap*" modunda (adaptör gereklidir), Bluetooth yoluyla ve hatta entegre kamera sayesinde QR kodları alışverişi yaparak. Bu Hardware Wallet pille çalışır.


Temel siyah versiyonu 149,99$'dan satılmaktadır ve "*Genesis Grey*" veya "*Lunar Silver*" versiyonları için fiyat 20$'a kadar yükselebilmektedir. Bu nedenle Jade Plus, Coldcard Q veya Passport V2 gibi üst düzey donanım cüzdanlarıyla karşılaştırılabilir gelişmiş işlevlere sahip, ancak orta sınıf modellere yakın, oldukça düşük bir fiyata ilginç bir seçimdir.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus çoğu Wallet yönetim yazılımı ile uyumludur. İşte yazının yazıldığı tarihte (Ocak 2025) uyumluluğun bir özeti:


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

Bu eğitimde, Jade Plus'ı Blockstream'in Green Wallet mobil uygulaması ile Bluetooth bağlantısı üzerinden kuracak ve kullanacağız. Bu kurulum yeni başlayanlar için idealdir. Daha gelişmiş bir yaklaşım arıyorsanız, Jade Plus'ı QR kodları modunda Sparrow wallet ile kullandığımız bu eğitime göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Jade Plus güvenlik modeli


Jade Plus, bir "kör kahin" tarafından gerçekleştirilen "sanal secure element "e dayalı bir güvenlik modeli kullanmaktadır. Somut olarak, bu mekanizma kullanıcı tarafından seçilen PIN'i, Jade üzerinde barındırılan bir sırrı ve oracle (Blockstream tarafından tutulan bir sunucu) tarafından tutulan bir sırrı birleştirerek iki varlığa dağıtılan bir AES-256 anahtarı oluşturur. Başlatma sırasında, bir ECDH Exchange oracle ile iletişimi güvence altına alır ve Hardware Wallet üzerindeki kurtarma ifadesini şifreler. Pratik açıdan, işlemleri imzalamak için seed'e erişmek istediğinizde, :




- Jade Plus cihazının kendisine;
- Cihaz kilidini açmak için PIN girmek için ;
- Ve kahinin sırrına.


Bu yaklaşımın en büyük avantajı, donanım düzeyinde tek bir hata noktasının olmamasıdır, çünkü bir saldırgan Jade'inize erişirse, anahtarların çıkarılması aynı anda Jade ve oracle'ın tehlikeye atılmasını gerektirir. Bu model aynı zamanda Jade Plus'ın tamamen açık kaynaklı olduğu ve örneğin Ledger'te kullanılanlar gibi gerçek fiziksel güvenli Elements kullanımıyla ilişkili kısıtlamalardan kaçındığı anlamına gelir.


Bu sistemin dezavantajı Jade Plus'ın kullanımının Blockstream tarafından tutulan oracle'a bağlı olmasıdır. Bu kahine erişilemez hale gelirse, Hardware Wallet'yı doğrudan PIN ile kullanmak artık mümkün değildir. Ancak, bu bitcoinlerinizin kaybolduğu anlamına gelmez, çünkü Jade Plus'a "*durumsuz*" modda girebileceğiniz kurtarma cümlenizi kullanarak hala kurtarılabilirler. Bu bağımlılığı aşmak için kendi oracle sunucunuzu da yapılandırabilir ve yönetebilirsiniz.


## Jade Plus'ın kutu açılışı


Jade Plus'ınızı teslim aldığınızda, paketinizin açılmadığından emin olmak için kutunun ve Seal'nin iyi durumda olduğunu kontrol edin.


![JADE-PLUS-GREEN](assets/fr/02.webp)


Kutunun içinde şunları bulacaksınız:




- Le Jade Plus;
- USB-C kablosu;
- Mnemonic ifadenizi kelime olarak veya "*CompactSeedQR*" olarak kaydetmek için kartlar;
- Bazı kullanım talimatları ;
- Bir kordon;
- Bazı çıkartmalar.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Cihazda 4 adet navigasyon butonu bulunmaktadır:




- Sağ alttaki düğme Jade'i açar;
- Cihazın ön tarafındaki büyük düğme bir öğe seçmek için kullanılır;
- Üstteki iki küçük düğme sağa ve sola gitmenizi sağlar;
- Cihazın üst kısmındaki iki düğmeye aynı anda tıklayarak da bir öğe seçebilirsiniz.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Yeni bir Bitcoin Wallet kurulumu


Başlat düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/05.webp)


"*Setup Jade*" üzerine tıklayın.


![JADE-PLUS-GREEN](assets/fr/06.webp)


"Kuruluma Başla "yı seçin. "*Advanced Setup*" seçeneği de aynı şeyi yapar, ancak gelişmiş ayarlara erişim sağlar.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Ardından yeni bir generate oluşturmak için "*Yeni bir Wallet* Oluştur" seçeneğine tıklayın.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Yeni kurtarma ifadenizi görüntülemek için "*Devam*" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Jade Plus'ınızda 12 kelimelik Mnemonic ifadeniz görüntülenir. **Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herkes, Jade Plus'ınıza fiziksel erişimi olmasa bile paralarınızı çalabilir. 12 kelimelik ifade, Jade'inizin kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle bu ifadeyi dikkatli bir şekilde saklamak ve güvenli bir yerde muhafaza etmek çok önemlidir.


Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir


Aşağıdaki kelimeleri görüntülemek için ekranın sağındaki oka tıklayın.


![JADE-PLUS-GREEN](assets/fr/11.webp)


İfadenizi kaydettikten sonra Jade Plus sizden onaylamanızı ister. Cihazın üst kısmındaki düğmeleri kullanarak sıraya göre doğru kelimeyi seçin ve bir sonraki kelimeye geçmek için ortadaki düğmeye tıklayın.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Jade Plus'ı Green Wallet'e bağlama


Bu eğitimde, Jade Plus üzerinde barındırılan Wallet'yi yönetmek için Green Wallet uygulamasını kullanacağız. Bu yöntem özellikle yeni başlayanlar için uygundur. Bitcoin Wallet'nizi daha ayrıntılı olarak yönetmek isterseniz, ayrı bir eğitimde ele alacağımız Sparrow wallet'u da kullanabilirsiniz:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Blockstream Green uygulamasının kurulumu ve ayarlanması ile ilgili talimatlar için lütfen bu diğer eğitimin ilk bölümüne bakın:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Blockstream Green uygulamasına girdikten sonra, "*Yeni bir Wallet* yapılandır" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/13.webp)


"*Hardware Wallet* üzerinde" öğesini seçin.


![JADE-PLUS-GREEN](assets/fr/14.webp)


Akıllı telefonunuzda Bluetooth'u etkinleştirin, ardından "*Jade'inizi bağlayın*" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/15.webp)


Bluetooth bağlantılarına erişmek için Green uygulamasını yetkilendirin.


![JADE-PLUS-GREEN](assets/fr/16.webp)


Uygulama Jade Plus'ınızı arıyor.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Jade Plus'ta "*Bluetooth*" menüsüne tıklayın.


![JADE-PLUS-GREEN](assets/fr/18.webp)


Green uygulamasında cihazınızı seçin.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Jade Plus cihazınızdaki eşleştirme kodunu onaylayın.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green, Jade'inizin orijinal olduğundan emin olmanız için size bir test sunar. Bunu yapmak için düğmeye tıklayın.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Jade'i onaylayın.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green cihazınızın orijinal olduğunu onaylar.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## PIN kodunun ayarlanması


Jade'inizin PIN kodunu seçmek için "*Devam*" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN kodu Jade'inizin kilidini açar. Bu nedenle yetkisiz fiziksel erişime karşı bir korumadır. Bu PIN kodu Wallet'ünüzün kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, bu PIN koduna erişiminiz olmasa bile, 12 kelimelik Mnemonic ifadenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır. Mümkün olduğunca rastgele bir PIN kodu seçmenizi öneririz. Ve bu kodu Jade'inizin saklandığı yerden ayrı bir yere (örneğin bir şifre yöneticisine) kaydettiğinizden emin olun.


Rakamlar arasında gezinmek için sağ ve sol düğmeleri ve bir rakamın girişini onaylamak için orta düğmeyi kullanarak Jade cihazınızdaki 6 haneli PIN kodunu seçin.


![JADE-PLUS-GREEN](assets/fr/25.webp)


PIN kodunuzu ikinci kez onaylayın.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Bitcoin Wallet'iniz oluşturuldu.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Bir Bitcoin hesabı oluşturun


Şimdi Wallet'nizde bir hesap oluşturmanız gerekmektedir. "*Hesap oluştur*" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/28.webp)


Klasik bir single-sig Wallet oluşturmak istiyorsanız "*Standard*" seçeneğini seçin.


![JADE-PLUS-GREEN](assets/fr/29.webp)


"*2FA*" seçeneği hakkında daha fazla bilgi için bu diğer öğreticiyi takip edebilirsiniz:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Hesabınız oluşturuldu.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Green Wallet'unuzu kişiselleştirmek isterseniz, sağ üstteki üç küçük noktaya tıklayın.


![JADE-PLUS-GREEN](assets/fr/31.webp)


"*Rename*" seçeneği Wallet'ünüzün adını özelleştirmenizi sağlar, bu özellikle aynı uygulama üzerinde birkaç cüzdan yönetiyorsanız kullanışlıdır. "*Unit*" menüsü Wallet'ünüzün temel birimini değiştirmenizi sağlar. Örneğin, bitcoin yerine satoshi cinsinden görüntülemeyi seçebilirsiniz. Son olarak, "*Parametreler*" menüsü diğer seçeneklere erişmenizi sağlar. Burada, örneğin, Jade'inizden bir Watch-only wallet kurmayı planlıyorsanız yararlı olan genişletilmiş genel anahtarınızı ve Descriptor'sini bulacaksınız.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Jade cihazınızı kapattıktan sonra yeniden bağlanmak için cihazın altındaki açma/kapama düğmesine basın. Green uygulamasında, ana sayfadan cihazınızı seçin:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Ardından Jade'inizdeki PIN kodunu girin ve tekrar bağlanacaksınız.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Jade cihazınızın kilidi Blockstream'in "sanal secure element "i aracılığıyla açılır (bu eğitimin ilk bölümüne bakın). Bu, Green uygulamasıyla bir Bluetooth bağlantısı gerektirir. Kilit açma sırasında Bluetooth bağlantısıyla ilgili zorluklarla karşılaşırsanız, iki cihazı ayırmayı ve yeniden ilişkilendirmeyi deneyin. Sorun devam ederse, "*QR Scan*" seçeneğini seçerek ve [Blockstream web sitesinde] (https://jadefw.blockstream.com/pinqr/index.html) bulunan talimatları izleyerek Jade cihazınızın kilidini açabilirsiniz.


Wallet'unuzdaki ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ilk aldığınız Address gibi bazı referans bilgilerini not edin, ardından Wallet'unuzu Green uygulamasında ve Jade Plus'ta hala boşken silin (`Options -> Device -> Factory Reset`). Ardından Wallet ifadesinin kağıt yedeklerini kullanarak Mnemonic'nizi geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan çerez bilgilerinin orijinal olarak yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz. Test kurtarma işleminin nasıl gerçekleştirileceği hakkında daha fazla bilgi edinmek için lütfen bu diğer eğitime başvurun:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoin alma


Artık Bitcoin Wallet'niz ayarlandığına göre, ilk Sats'ünüzü almaya hazırsınız! Green uygulamasındaki "*Al*" düğmesine tıklamanız yeterlidir.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green bir Address alımı görüntüler, ancak kullanmadan önce, aslında Wallet'mıza ait olduğunu doğrulamak için Jade üzerinde kontrol etmek önemlidir. Bunu yapmak için "*Cihaz üzerinde doğrula*" düğmesine tıklayın.


![JADE-PLUS-GREEN](assets/fr/36.webp)


Jade üzerinde Address'in Green ile aynı olup olmadığını kontrol edin, ardından onaylamak için düğmeye tıklayın.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Artık Wallet'inizdeki bitcoinleri almak için Address'i ödeme yapan kişiyle paylaşabilirsiniz. İşlem ağda yayınlandığında, Wallet'inizde görünecektir. İşlemi kesin olarak değerlendirmek için yeterli onay alana kadar bekleyin.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Bitcoin gönder


Wallet'nizdeki bitcoinler ile artık bitcoin de gönderebilirsiniz. "*Gönder*" üzerine tıklayın.


![JADE-PLUS-GREEN](assets/fr/39.webp)


Sonraki sayfada, alıcının Address numarasını girin. Manuel olarak girebilir veya bir QR kodu tarayabilirsiniz.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Ödeme tutarını seçin.


![JADE-PLUS-GREEN](assets/fr/41.webp)


Ekranın alt kısmında, bu işlem için ücret oranını seçebilirsiniz. Uygulamanın önerilerini takip etme veya ücretlerinizi özelleştirme seçeneğiniz vardır. Bekleyen diğer işlemlere göre ücret ne kadar yüksekse, işleminiz o kadar hızlı işlenecektir. Ücret piyasası bilgileri için lütfen [Mempool.space] (https://Mempool.space/) adresindeki "*İşlem Ücretleri*" bölümünü ziyaret edin.


![JADE-PLUS-GREEN](assets/fr/42.webp)


İşlem özeti ekranına erişmek için "*Sonraki*" üzerine tıklayın. Address, tutar ve masrafların doğru olup olmadığını kontrol edin.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Her şey yolunda giderse, işlemi imzalamak ve Bitcoin ağında yayınlamak için ekranın altındaki Green düğmesini sağa kaydırın.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Şimdi Jade üzerinde işlemi onaylamanız istenir.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Alıcının Address'inin doğru olduğundan emin olun. Onaylamak için onay işaretine tıklayın.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Ücret tutarının doğru olup olmadığını kontrol edin, ardından doğrulayın.


![JADE-PLUS-GREEN](assets/fr/47.webp)


İşleminiz imzalanmış ve Green'dan yayınlanmıştır.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Tebrikler, artık Jade Plus'ı Blockstream Green mobil uygulaması ile Bluetooth bağlantısı üzerinden nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


İşleri bir adım öteye taşımak için, Jade Plus'ı QR modunda Sparrow wallet yazılımı ile yapılandırdığımız bu öğreticiyi tavsiye ederim. Ayrıca Hardware Wallet'nizin gelişmiş ayarlarını nasıl kullanacağınızı da öğreneceksiniz:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

