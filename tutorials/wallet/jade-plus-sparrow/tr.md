---
name: Jade Plus - Sparrow
description: Jade Plus'ın Sparrow wallet ile gelişmiş yapılandırması
---
![cover](assets/cover.webp)


Jade Plus, Blockstream tarafından tasarlanmış sadece Bitcoin'e özel bir Hardware Wallet'dir. Yazılım geliştirmeleri, daha fazla seçenek ve daha sezgisel kullanım için yeniden tasarlanmış ergonomi ile klasik Jade'in halefidir. Bu yeni sürüm, öncekinden daha geniş bir renk gamına sahip muhteşem bir 1,9 inç LCD ekrana sahiptir. Düğmeler ve menü navigasyonu da optimize edilmiştir.


Jade Plus çeşitli şekillerde kullanılabilir: USB-C kablolu bağlantı yoluyla, mikro SD kartla "*Air-Gap*" modunda (adaptör gereklidir), Bluetooth yoluyla ve hatta entegre kamera sayesinde QR kodları alışverişi yaparak. Bu Hardware Wallet pille çalışır.


Temel siyah versiyonu 149,99$'dan satılmaktadır ve "*Genesis Grey*" veya "*Lunar Silver*" versiyonları için fiyat 20$'a kadar yükselebilmektedir. Bu nedenle Jade Plus, Coldcard Q veya Passport V2 gibi üst düzey donanım cüzdanlarıyla karşılaştırılabilir gelişmiş işlevlere sahip, ancak orta sınıf modellere yakın, oldukça düşük bir fiyata ilginç bir seçimdir.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


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

Bu eğitimde, QR kodları modunda masaüstü Sparrow wallet yazılımı ile Jade Plus'ın gelişmiş bir yapılandırmasını kuracağız. Bu yapılandırma orta düzey veya deneyimli kullanıcılar için idealdir. Yeni başlayanlar için daha basit bir yaklaşım arıyorsanız, Jade Plus'ı Bluetooth bağlantısı üzerinden Green Wallet ile kullandığımız bu eğitime göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Jade Plus güvenlik modeli


Jade Plus, bir "kör kahin" tarafından gerçekleştirilen "sanal secure element "e dayalı bir güvenlik modeli kullanmaktadır. Somut olarak, bu mekanizma kullanıcı tarafından seçilen PIN'i, Jade üzerinde barındırılan bir sırrı ve oracle (Blockstream tarafından tutulan bir sunucu) tarafından tutulan bir sırrı birleştirerek iki varlığa dağıtılan bir AES-256 anahtarı oluşturur. Başlatma sırasında, bir ECDH Exchange oracle ile iletişimi güvence altına alır ve Hardware Wallet üzerindeki kurtarma ifadesini şifreler. Pratik açıdan, işlemleri imzalamak için seed'e erişmek istediğinizde, :




- Jade Plus cihazının kendisi;
- Cihaz kilidini açmak için PIN girmek için ;
- Ve kahinin sırrına.


Bu yaklaşımın en büyük avantajı, donanım düzeyinde tek bir hata noktasının olmamasıdır, çünkü bir saldırgan Jade'inize erişirse, anahtarların çıkarılması aynı anda Jade ve oracle'ın tehlikeye atılmasını gerektirir. Bu model aynı zamanda Jade Plus'ın tamamen açık kaynaklı olduğu ve örneğin Ledger'te kullanılanlar gibi gerçek fiziksel güvenli Elements kullanımıyla ilişkili kısıtlamalardan kaçındığı anlamına gelir.


Bu sistemin dezavantajı Jade Plus'ın kullanımının Blockstream tarafından tutulan oracle'a bağlı olmasıdır. Bu kahine erişilemez hale gelirse, Hardware Wallet'yı doğrudan PIN ile kullanmak artık mümkün değildir. Ancak, bu bitcoinlerinizin kaybolduğu anlamına gelmez, çünkü Jade Plus'a "*durumsuz*" modda girebileceğiniz kurtarma cümlenizi kullanarak hala kurtarılabilirler. Bu bağımlılığı aşmak için kendi oracle sunucunuzu da yapılandırabilir ve yönetebilirsiniz.


seed'inizi yönetmek için bir başka seçenek de Jade Plus'a kaydetmemektir. Bu durumda Jade yalnızca bir imza cihazı haline gelir. Başlatma sırasında, kurtarma cümlesinin kelimeler olarak kaydedilmesine ek olarak, elle oluşturulmuş bir QR kodu olarak da kaydedeceksiniz. Bu şekilde, Wallet'nizi her kullandığınızda, Jade'inizin kamerasını kullanarak seed'i içe aktarabilirsiniz. Bu, güvenlik stratejinize bağlı olarak ileri düzey kullanıcılar için ilginç bir seçenek olabilir, ancak hem seed'inizi kaydetmek hem de korumak için dikkatli olmanız gerekir, çünkü QR kodu olarak bile, herhangi birinin paranızı çalmasına izin verebilir. Bu eğitimde bu seçeneğe bakacağız, ancak zorunlu değil.


## Jade Plus'ın kutu açılışı


Jade Plus'ınızı teslim aldığınızda, paketinizin açılmadığından emin olmak için kutunun ve Seal'un iyi durumda olduğunu kontrol edin.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


Kutunun içinde şunları bulacaksınız:




- Le Jade Plus;
- USB-C kablosu;
- Mnemonic ifadenizi kelime olarak veya "*CompactSeedQR*" olarak kaydetmek için kartlar;
- Bazı kullanım talimatları ;
- Bir kordon;
- Bazı çıkartmalar.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


Cihazda 4 adet navigasyon butonu bulunmaktadır:




- Sağ alttaki düğme Jade'i açar;
- Cihazın ön tarafındaki büyük düğme bir öğe seçmek için kullanılır;
- Üstteki iki küçük düğme sağa ve sola gitmenizi sağlar;
- Cihazın üst kısmındaki iki düğmeye aynı anda tıklayarak da bir öğe seçebilirsiniz.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## Yeni bir Bitcoin Wallet kurulumu


Başlat düğmesine tıklayın.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


"*Setup Jade*" üzerine tıklayın.


![JADE-PLUS-SPARROW](assets/fr/06.webp)


"Gelişmiş Kurulum*" öğesini seçin.


![Image](assets/fr/07.webp)


Ardından yeni bir generate oluşturmak için "*Yeni bir Wallet* Oluştur "a tıklayın. 12 veya 24 kelimelik bir Mnemonic cümlesi arasında seçim yapabilirsiniz. Wallet'inizin güvenliği her iki seçenekte de eşdeğer kalır, bu nedenle kaydetmek için en basit seçeneği, yani 12 kelimeyi seçmek daha uygun olabilir.


![Image](assets/fr/08.webp)


Yeni kurtarma ifadenizi görüntülemek için "*Devam*" düğmesine tıklayın.


![Image](assets/fr/09.webp)


Jade Plus'ınızda 12 kelimelik Mnemonic ifadeniz görüntülenir. **Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herkes, Jade Plus'ınıza fiziksel erişimi olmasa bile paralarınızı çalabilir. 12 kelimelik ifade, Jade'inizin kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle bu ifadeyi dikkatli bir şekilde saklamak ve güvenli bir yerde muhafaza etmek çok önemlidir.


Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.


![Image](assets/fr/10.webp)


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tabii ki, benim bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**_


Aşağıdaki kelimeleri görüntülemek için ekranın sağındaki oka tıklayın.


![Image](assets/fr/11.webp)


İfadenizi kaydettikten sonra Jade Plus sizden onaylamanızı ister. Cihazın üst kısmındaki düğmeleri kullanarak sıraya göre doğru kelimeyi seçin ve bir sonraki kelimeye geçmek için ortadaki düğmeye tıklayın.


![Image](assets/fr/12.webp)


Daha sonra 2 seçeneğiniz vardır. Giriş bölümünde açıklandığı gibi, seed'ünüzü doğrudan cihaza kaydetmeyi ve Wallet'nize erişmek için Blockstream'in "*Sanal secure element*" koruma sistemini kullanmayı (Seçenek 1) veya seed'ünüzü bir QR kodu olarak kaydetmeyi ve her kullandığınızda taramayı (Seçenek 2) seçebilirsiniz.


Seçenek 1 için "*Hayır*" ve Seçenek 2 için "*Evet*" seçeneğini seçin.


![Image](assets/fr/13.webp)


### Seçenek 1: QR PIN Kilit Açma


Eğer 1. seçeneği seçtiyseniz (CompactSeedQR: "*Hayır*"), doğrudan bağlantı yöntemi seçimine yönlendirileceksiniz. Bu eğitimde, cihazı QR kod alışverişi yoluyla Air-Gap modunda kullanmak istiyoruz, bu nedenle "*QR*" seçeneğini seçin.


![Image](assets/fr/27.webp)


"*Devam*" üzerine tıklayın.


![Image](assets/fr/28.webp)


PIN kodu Jade cihazınızın kilidini açmak için kullanılır ve yetkisiz fiziksel erişime karşı koruma sağlar. Bu PIN kodu Wallet'inizin kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, bu PIN koduna erişiminiz olmasa bile, 12 kelimelik Mnemonic ifadenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır. Mümkün olduğunca rastgele bir PIN kodu seçmenizi öneririz. Ayrıca, bu kodu Jade'inizin depolandığı yerden ayrı bir yere, örneğin bir şifre yöneticisine kaydettiğinizden emin olun.


Rakamlar arasında gezinmek için sol ve sağ düğmeleri ve her rakamı onaylamak için orta düğmeyi kullanarak Jade cihazınızda 6 basamaklı bir PIN kodu seçin.


![Image](assets/fr/29.webp)


PIN kodunuzu ikinci kez onaylayın.


![Image](assets/fr/30.webp)


Giriş bölümünde açıklandığı gibi, seed'nız Jade Plus'ta şifrelenmiş olarak saklanır. Şifreyi çözmek için, :




- Geçerli PIN kodu (az önce ayarladığımız) ;
- Blockstream tarafından korunan kahinin sırrı.


Bu ileri düzey eğitimde, Sparrow wallet'yi Bitcoin Wallet'ımızı yönetmek için kullanacağız. Bununla birlikte, Blockstream'in Green Wallet yazılımının aksine, Sparrow'un Blockstream'in sunucularındaki kahine erişimi yoktur. Bu nedenle, Jade Plus'ın kilidini her açtığımızda oracle sırrını almak için Blockstream'in web sitesini kullanacağız.


Https://jadefw.blockstream.com/pinqr/index.html adresini ziyaret edin


"*Start QR Unlock*" üzerine tıklayın.


![Image](assets/fr/31.webp)


Jade Plus'ta PIN kodunuzu zaten seçmiş olduğunuz için "*Bitti*" üzerine tıklayın.


![Image](assets/fr/32.webp)


Jade'inizin ekranında görüntülenen QR kodlarını taramak için bilgisayarınızın kamerasını kullanın.


![Image](assets/fr/33.webp)


Bir sonraki ekrana erişmek için Jade cihazınızda onaylayın.


![Image](assets/fr/34.webp)


Kahinin sırrını öğrenmek için şimdi web sitesinde görünen QR kodunu tarayın.


![Image](assets/fr/35.webp)


Artık Wallet'niz oluşturulduğuna göre, sonraki adımlara geçebilir ve "*Opsiyon 2: CompactSeedQR*" alt bölümünü atlayabilirsiniz.


![Image](assets/fr/36.webp)


Her başlattığınızda "*QR Modu*" üzerine tıklayın.


![Image](assets/fr/37.webp)


"*QR PIN Kilit Açma*" öğesini seçin.


![Image](assets/fr/38.webp)


PIN kodunuzu girin.


![Image](assets/fr/39.webp)


Ardından oracle ile Exchange QR kodları için [Blockstream web sitesine] (https://jadefw.blockstream.com/pinqr/qrpin.html) gidin.


![Image](assets/fr/40.webp)


Jade'inizin kilidi açıldı.


![Image](assets/fr/41.webp)


### Seçenek 2: CompactSeedQR


Eğer 2. seçeneği seçtiyseniz (CompactSeedQR: "*Evet*"), tekrar "*Evet*" üzerine tıklayın.


![Image](assets/fr/14.webp)


"*Başlat*" üzerine tıklayın.


![Image](assets/fr/15.webp)


Jade Plus kutusunda verilen QR kod tabanını kullanabilirsiniz. 12 veya 24 kelimelik bir cümle seçmiş olmanıza bağlı olarak uygun kutuyu seçin. Ayrıca [Blockstream web sitesinden şablonu yazdırabilirsiniz] (https://help.blockstream.com/hc/article_attachments/41928319071769).


Jade Plus cihazınız QR kodunuzun her bir bölgesini görüntüleyecektir.


![Image](assets/fr/16.webp)


Kareleri renklendirmek için bir kalem kullanın ve seed'ünüzü bir QR kodu olarak yeniden oluşturun. Jade Plus kameranın daha sonra tarayabilmesini sağlamak için hassas olun. Bir sonraki alana geçmek için oku kullanın.


![Image](assets/fr/17.webp)


Bitirdiğinizde, "*Bitti*" üzerine tıklayın.


![Image](assets/fr/18.webp)


Geçerliliğini kontrol etmek için el yapımı QR kodunuzu Jade Plus ile tarayın.


![Image](assets/fr/19.webp)


Kağıt yedeğiniz doğruysa, "*Devam*" düğmesine tıklayın.


![Image](assets/fr/20.webp)


Bu eğitimde, yalnızca QR kod taramasına dayalı bir bağlantı modu kullanacağız, bu nedenle "*QR*" öğesini seçin.


![Image](assets/fr/21.webp)


Ayrıca 1. seçenekte olduğu gibi CompactSeedQR yedeklemenize ek olarak bir PIN eklemeyi de seçebilirsiniz. Bu, Wallet'nıza erişmenin iki yolunu sunar: PIN ve Blockstream'in "Sanal secure element" sistemi aracılığıyla veya CompactSeedQR aracılığıyla.


Çift PIN seçeneğini tercih ederseniz, "*PIN*" öğesini seçin ve PIN kodunuzu ayarlamak için 1. seçenekteki adımların aynısını izleyin.


Yalnızca CompactSeedQR ile devam etmeyi tercih ediyorsanız, "*SeedQR*" öğesini seçin.


![Image](assets/fr/22.webp)


Artık Wallet'niz oluşturulduğuna göre sonraki adımlara geçebilirsiniz.


![Image](assets/fr/23.webp)


Her başlattığınızda, "*QR Modu*" düğmesine ve ardından "*TohumQR* Tara" düğmesine tıklayın.


![Image](assets/fr/24.webp)


Kayıtlı seed'inizi QR kodu olarak taramak için cihazın kamerasını kullanın.


![Image](assets/fr/25.webp)


Jade'inizin kilidi açıldı.


![Image](assets/fr/26.webp)


## Bir BIP39 passphrase ekleyin


BIP39 passphrase, serbestçe seçebileceğiniz ve Wallet güvenliğini güçlendirmek için Mnemonic ifadenize eklenen isteğe bağlı bir paroladır. Bu özellik etkinleştirildiğinde, Bitcoin Wallet'ünüze erişim için hem Mnemonic hem de passphrase gerekir. İkisi de olmadan Wallet'ü kurtarmak imkansız olacaktır.


Jade Plus'ınızda bu seçeneği yapılandırmadan önce, passphrase'ün teorik çalışmasını tam olarak anlamak ve bitcoinlerinizin kaybına yol açabilecek hatalardan kaçınmak için bu makaleyi okumanız şiddetle tavsiye edilir:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jade'iniz hala kilitliyken (passphrase'e yalnızca cihazın kilidi açık değilken girilebilir), "*Seçenekler*" menüsüne erişin.


![Image](assets/fr/42.webp)


"*BIP39 passphrase*" öğesini seçin.


![Image](assets/fr/43.webp)


"*Sıklık*" seçeneğinde, Jade Plus'ın her başlatıldığında passphrase'nizi girmenizi isteyip istemeyeceğini seçebilirsiniz:




- "*Devre Dışı*" passphrase kullanımını devre dışı bırakır;
- "*Sadece Bir Sonraki Giriş*" bir sonraki başlangıçta passphrase'unuzun talebini etkinleştirmek için bu menüye dönmenizi gerektirecektir. Bu seçenek, kullanımını açıklamamanızı sağlar;
- "*Her Zaman Sor*" Jade'in her başlatıldığında sistematik olarak passphrase'ınızı sormasına neden olur, böylece Wallet'inizin bir passphrase tarafından korunduğunu ortaya çıkarır.


Güvenlik stratejinize göre seçeneği belirleyin. Şahsen ben örnek için "*Her Zaman Sor*" seçeneğini seçiyorum.


![Image](assets/fr/44.webp)


Daha sonra passphrase'nizi girmek için iki yöntem arasından seçim yapabilirsiniz:




- "*Manuel*: Sanal bir klavye harfleri (büyük ve küçük harf), sayıları ve sembolleri karakter karakter girmenizi sağlar. Bu, tüm donanım cüzdanları için standart yöntemdir;
- "*WordList*": Blockstream tarafından Jade için tasarlanan, passphrase girişini hızlandıran ve entropisini artıran özel yöntem. Giriş sırasında, sistem BIP39 listesinden kelimeler önererek kilidin açılmasını kolaylaştırır. Bu yöntem, seçilen kelimeleri boşluklarla ayırarak birleştirerek otomatik olarak bir cümle oluşturur (örnek: `abandon ability able`).


Şahsen, diğer tüm Wallet desteklerinde bulacağınız standart olduğu için ilk yöntemi kullanmanızı tavsiye ederim.


![Image](assets/fr/45.webp)


Daha sonra ana ekrana dönebilir ve PIN kodunuzu ya da CompactSeedQR'nizi (yukarıda görüldüğü gibi) kullanarak Wallet'nızın kilidini normal şekilde açabilirsiniz. Daha sonra passphrase'inizi girmeniz istenecektir.


![Image](assets/fr/46.webp)


Jade klavyesinde girin ve fiziksel ortamda (kağıt veya metal) bir veya daha fazla yedekleme yaptığınızdan emin olun. Örnek için çok zayıf bir passphrase kullanıyorum, ancak her tür karakteri içeren ve yeterince uzun olan (güçlü bir parola gibi) güçlü, rastgele bir passphrase seçmeniz gerekir.


![Image](assets/fr/47.webp)


passphrase'iniz geçerliyse onaylayın.


![Image](assets/fr/48.webp)


Lütfen BIP39 parolalarının büyük/küçük harfe ve yazım hatasına duyarlı olduğunu unutmayın. Başlangıçta yapılandırılandan biraz farklı bir passphrase girerseniz, Jade bir hata bildirmeyecek, ancak ilk Wallet'inizde olmayan başka bir kriptografik anahtar seti türetecektir.


Bu nedenle, yapılandırma sırasında ekranın sağ alt köşesinde bulunan ana anahtar parmak izinizi not etmeniz önemlidir. Örneğin, passphrase `PBN` ile ana anahtar parmak izim `3AD1AE65`.


![Image](assets/fr/49.webp)


Jade cihazınızın kilidini passphrase ile her açtığınızda, parmak izinin yapılandırma sırasında girdiğinizle aynı olup olmadığını kontrol edin. Eğer öyleyse, passphrase'niz doğrudur ve doğru Bitcoin Wallet'e erişiyorsunuz demektir. Değilse, yanlış Wallet'tesinizdir ve herhangi bir giriş hatası yapmamaya dikkat ederek tekrar denemeniz gerekir.


Wallet'inizdeki ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ilk aldığınız Address gibi bazı referans bilgilerini not edin, ardından Jade Plus'ta Wallet'inizi hala boşken silin (`Seçenekler -> Cihaz -> Fabrika Ayarlarına Sıfırla`). Ardından Wallet'inizi Mnemonic ifadesinin ve herhangi bir passphrase'in kağıt yedeklerini kullanarak geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan çerez bilgilerinin başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz. Test kurtarma işleminin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime göz atın:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Wallet'i Sparrow wallet üzerinde yapılandırma


Bu eğitimde, Sparrow wallet kullanarak Jade Plus'ın gelişmiş bir kullanımını sunuyorum. Ancak, bu Hardware Wallet, Liana, Nunchuk, Spectre, Green ve Keeper gibi diğer birçok programla uyumludur. Bu uyumluluklar bağlantılar açısından değişiklik gösterir: USB, Bluetooth veya QR kodu (ayrıntılar için giriş bölümündeki tabloya bakın).


Henüz yapmadıysanız, Sparrow wallet'i [resmi web sitesinden] (https://sparrowwallet.com/) bilgisayarınıza indirip yükleyerek başlayın.


![Image](assets/fr/50.webp)


Kurulumdan önce yazılımın orijinalliğini ve bütünlüğünü kontrol ettiğinizden emin olun. Bunu nasıl yapacağınızı bilmiyorsanız, lütfen bu eğiticiye başvurun:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow wallet açıldığında, "*Dosya*" sekmesine ve ardından "*Yeni Wallet*" seçeneğine tıklayın.


![Image](assets/fr/51.webp)


Wallet'inize bir isim verin ve ardından "*Wallet* Oluştur "a tıklayın.


![Image](assets/fr/52.webp)


"*Havalandırılmış Hardware Wallet*" öğesini seçin.


![Image](assets/fr/53.webp)


"*Jade*" seçeneğinin yanındaki "*Scan...*" düğmesine tıklayın.


![Image](assets/fr/54.webp)


Jade Plus'ınızın kilidini açın ve eğer kullanıyorsanız passphrase'ınızı girin. Ardından "*Seçenekler*" menüsüne gidin, "*Wallet*"i seçin ve "*Export Xpub*"a tıklayın.


![Image](assets/fr/55.webp)


Jade ürününüz Keystore'unuzu birkaç QR kodu aracılığıyla gösterecektir. Sparrow kullanarak bunları makinenizde tarayın.


![Image](assets/fr/56.webp)


Şimdi xpub'ınızı ve Jade Plus'ınızdakiyle eşleşmesi gereken ana anahtar parmak izinizi görmelisiniz. "*Uygula*" üzerine tıklayın.


![Image](assets/fr/57.webp)


Sparrow wallet'ünüze erişimi güvence altına almak için güçlü bir parola belirleyin. Bu parola genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı koruyacaktır. Bu parolayı bir parola yöneticisine kaydetmek iyi bir fikirdir, böylece unutmazsınız.


![Image](assets/fr/58.webp)


Wallet'iniz artık Sparrow üzerinde doğru şekilde yapılandırılmıştır.


![Image](assets/fr/59.webp)


## Bitcoin alma


Jade Plus'ınız yapılandırıldığına göre, ilk Sats'unuzu yeni Bitcoin Wallet'inize almaya hazırsınız. Bunu yapmak için, Sparrow'de "*Alma*" menüsüne tıklayın.


![Image](assets/fr/60.webp)


Sparrow, Wallet'nizdeki ilk boş alım Address'ü görüntüleyecektir.


![Image](assets/fr/61.webp)


Kullanmadan önce, Bitcoin Wallet'ya ait olduğundan emin olmak için Jade Plus ekranında kontrol edelim. Jade'de "*Karekodu Tara*" seçeneğine tıklayın, ardından Sparrow'te görüntülenen Address'ün QR kodunu tarayın.


![Image](assets/fr/62.webp)


Jade'inizin ekranında görüntülenen Address'in Sparrow wallet'de görüntülenenle aynı olup olmadığını kontrol edin. Eğer uyuyorsa, devam etmek için onay işaretine tıklayın.


![Image](assets/fr/63.webp)


Hardware Wallet'unuz daha sonra bu Address'un Wallet'inizin bir parçası olduğunu ve ilişkili özel anahtarı tuttuğunu onaylayacaktır.


![Image](assets/fr/64.webp)


Address Jade'iniz tarafından onaylanırsa, artık bitcoin almak için kullanabilirsiniz. İşlem ağda yayınlandığında, Sparrow'te görünecektir. İşlemi kesin olarak değerlendirmek için yeterli onay alana kadar bekleyin.


![Image](assets/fr/65.webp)


## Bitcoin gönder


Artık Wallet'ünüzde birkaç Sats olduğuna göre, bazılarını da gönderebilirsiniz. Bunu yapmak için "*UTXOs*" menüsüne tıklayın.


![Image](assets/fr/66.webp)


Bu işlem için girdi olarak kullanmak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın.


![Image](assets/fr/67.webp)


Alıcının Address numarasını, işlemin amacını size hatırlatacak bir etiket ve bu Address numarasına göndermek istediğiniz tutarı girin.


![Image](assets/fr/68.webp)


Ücret oranını mevcut piyasa koşullarına göre ayarlayın, ardından "*İşlem Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/69.webp)


Tüm işlem parametrelerinin doğru olduğunu kontrol edin ve ardından "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![Image](assets/fr/70.webp)


PSBT'u (*Partially Signed Bitcoin Transaction*) görüntülemek için "*Show QR*" üzerine tıklayın. Sparrow işlemi oluşturdu, ancak hala girişte kullanılan bitcoinlerin kilidini açacak imzalardan yoksun. Bu imzalar yalnızca işlemi imzalamak için gereken özel anahtarlara erişim sağlayan seed'nizi barındıran Jade Plus tarafından gerçekleştirilebilir.


![Image](assets/fr/71.webp)


Jade Plus cihazınızda, Sparrow üzerinde görüntülenen PSBT'yi taramak için "*Karekodu Tara*" seçeneğine tıklayın.


![Image](assets/fr/72.webp)


Address teslimatının ve gönderilen miktarın doğru olduğunu onaylayın, ardından onaylamak için oka tıklayın.


![Image](assets/fr/73.webp)


Ücret tutarının seçtiğiniz tutar olduğundan emin olun, ardından işlemi imzalamak için Interface'ün sol üst köşesindeki onay simgesine tıklayın.


![Image](assets/fr/74.webp)


Sparrow wallet'te "*Karekodu Tara*" seçeneğine tıklayın ve Jade'inizde görüntülenen QR kodunu tarayın.


![Image](assets/fr/75.webp)


İmzalı işleminiz artık Bitcoin ağında yayınlanmaya ve bir Miner tarafından bir bloğa dahil edilmeye hazırdır. Her şey doğruysa, "*İşlemi Yayınla*" düğmesine tıklayın.


![Image](assets/fr/76.webp)


İşleminiz yayınlandı ve onay bekliyor.


![Image](assets/fr/77.webp)


Tebrikler, artık Jade Plus'ı QR modunda nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


Daha ileri gitmek için Jade Plus'ı Green mobil uygulaması ile Bluetooth üzerinden yapılandırdığımız bu diğer eğitimi tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0