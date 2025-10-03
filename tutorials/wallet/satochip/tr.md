---
name: Satochip
description: Satochip akıllı kartın kurulumu ve kullanımı
---
![cover](assets/cover.webp)


Bir Hardware Wallet, bir Bitcoin Wallet'nin özel anahtarlarını yönetmeye ve güvence altına almaya adanmış elektronik bir cihazdır. Genellikle internete bağlı genel amaçlı makinelere kurulan yazılım cüzdanlarının (veya Hot cüzdanlarının) aksine, donanım cüzdanları özel anahtarların fiziksel olarak izole edilmesini sağlayarak bilgisayar korsanlığı ve hırsızlık risklerini azaltır.


Bir Hardware Wallet'ün ana hedefi, saldırı yüzeyini azaltmak için cihazın işlevlerini en aza indirmektir. Daha küçük bir saldırı yüzeyi aynı zamanda daha az potansiyel saldırı vektörü, yani saldırganların bitcoinlere erişmek için yararlanabileceği sistemde daha az zayıflık anlamına gelir.


Özellikle mutlak değer olarak veya toplam varlıklarınızın bir oranı olarak önemli miktarlara sahipseniz, bitcoinlerinizi güvence altına almak için bir Hardware Wallet kullanmanız önerilir.


Donanım cüzdanları, bir bilgisayar veya akıllı telefondaki Wallet yönetim yazılımı ile birlikte kullanılır. Bu yazılım işlemlerin oluşturulmasını yönetir, ancak bu işlemleri doğrulamak için gerekli kriptografik imza yalnızca Hardware Wallet içinde yapılır. Bu, özel anahtarların hiçbir zaman potansiyel olarak savunmasız bir ortama maruz kalmadığı anlamına gelir.


Donanım cüzdanları kullanıcı için ikili koruma sunar: bir yandan özel anahtarları çevrimdışı tutarak bitcoinlerinizi uzaktan saldırılara karşı korurlar, diğer yandan da genellikle anahtarları çıkarma girişimlerine karşı daha iyi fiziksel direnç sunarlar. İşte tam da bu 2 güvenlik kriterine göre piyasada bulunan farklı modeller değerlendirilebilir ve sıralanabilir.


Bu eğitimde, bu çözümlerden birini keşfetmeyi öneriyorum: Satochip.


## Satochip'e Giriş


Satochip, çok yüksek bir güvenlik standardı olan (*NXP JCOP*) *EAL6+* sertifikalı bir çipe sahip kart şeklinde bir Hardware Wallet'dir. Belçikalı bir şirket tarafından üretilmektedir.


![SATOCHIP](assets/notext/01.webp)


Bu akıllı kart, piyasadaki diğer donanım cüzdanlarına kıyasla çok uygun bir fiyat olan 25 € karşılığında satılmaktadır. Çip, fiziksel saldırılara karşı çok iyi direnç sağlayan bir secure element'dur. Dahası, kodu açık kaynaklıdır (*AGPLv3*).

Ancak formatı nedeniyle Satochip diğer donanımlar kadar çok seçenek sunmuyor. Bir kart olduğu için bataryası, kamerası ya da mikro SD kart okuyucusu yok. Bence en büyük dezavantajı, Hardware Wallet'da ekran olmaması ve bu da onu belirli uzaktan saldırı türlerine karşı daha savunmasız hale getiriyor. Gerçekten de bu durum kullanıcıyı körü körüne imza atmaya ve bilgisayar ekranında gördüklerine güvenmeye zorluyor.


Sınırlamalarına rağmen, Satochip düşük fiyatı nedeniyle ilgi çekici olmaya devam etmektedir. Bu Wallet, özellikle ekranlı bir Hardware Wallet ile korunan bir tasarruf Wallet'e ek olarak bir harcama Wallet'ün güvenliğini arttırmak için kullanılabilir. Ayrıca küçük miktarlarda bitcoin bulunduran ve daha sofistike bir cihaza yüz avro yatırmak istemeyenler için de iyi bir çözüm oluşturmaktadır. Dahası, Satochips'in Multisig konfigürasyonlarında veya potansiyel olarak gelecekte zaman kilitli Wallet sistemlerinde kullanılması ilginç avantajlar sunabilir.


Satochip şirketi ayrıca 2 ürün daha sunmaktadır. Bitcoinleri çevrimdışı olarak saklamak için tasarlanmış bir hamiline kart olan Satodime var, ancak işlemlere izin vermiyor. Çok daha güvenli olan ve örneğin hediye vermek için kullanılabilen bir tür kağıt Wallet. Son olarak, bir Mnemonic ifade yöneticisi olan Seedkeeper var. seed'mızı doğrudan bir kağıt parçasına not edilmeden güvenli bir şekilde kaydetmek için kullanılabilir.


## Satochip nasıl satın alınır?


Satochip [resmi web sitesinde] (https://satochip.io/product/satochip/) satışa sunulmuştur. Fiziksel bir mağazadan satın almak için, Satochip web sitesinde [sertifikalı satıcıların listesini] (https://satochip.io/resellers/) de bulabilirsiniz.


Wallet yönetim yazılımınızla etkileşim için Satochip iki seçenek sunar: NFC iletişimi veya bir akıllı kart okuyucu aracılığıyla. NFC seçeneği için makinenizin bu teknolojiyle uyumlu olduğundan emin olun veya harici bir NFC okuyucu edinin. Satochip standart 13.56 MHz frekansında çalışır. Aksi takdirde, bir akıllı kart okuyucu da satın alabilirsiniz. Satochip web sitesinde veya başka bir yerde bir tane bulabilirsiniz.


![SATOCHIP](assets/notext/02.webp)


## Sparrow ile bir Satochip nasıl kurulur?


Satochip'inizi aldıktan sonra ilk adım, ambalajın açılmadığından emin olmak için ambalajı incelemektir. Satochip'in ambalajında bir mühürleme etiketi bulunmalıdır. Bu etiket eksik veya hasarlıysa, akıllı kartın ele geçirildiğini ve orijinal olmayabileceğini gösterebilir.

![SATOCHIP](assets/notext/03.webp)

Satochip'i içeride bulacaksın.


![SATOCHIP](assets/notext/04.webp)


Bu eğitimde Wallet'i yönetmek için Sparrow'yi kullanmanızı öneriyorum. Henüz yazılıma sahip değilseniz, [indirmek için resmi web sitesini ziyaret edin] (https://sparrowwallet.com/download/). Ayrıca Sparrow wallet hakkındaki eğitimimize de göz atabilirsiniz (yakında).


![SATOCHIP](assets/notext/05.webp)


Satochip'inizi akıllı kart okuyucuya takın veya NFC okuyucuya yerleştirin ve okuyucuyu Sparrow'nin açık olduğu bilgisayarınıza bağlayın.


![SATOCHIP](assets/notext/06.webp)


Sparrow wallet'ü açın ve bir Bitcoin düğümüne doğru şekilde bağlandığınızdan emin olun. Bunu yapmak için sağ alttaki tik işaretini kontrol edin: genel bir düğüme bağlıysanız sarı, Green'ya bağlantı için Bitcoin core veya Electrum için mavi olmalıdır.


![SATOCHIP](assets/notext/07.webp)


Sparrow wallet'de "*Dosya*" sekmesine tıklayın.


![SATOCHIP](assets/notext/08.webp)


Ardından "*Yeni Wallet*" menüsünde.


![SATOCHIP](assets/notext/09.webp)


Wallet'unuz için bir isim seçin ve ardından "*Wallet Oluştur*" seçeneğine tıklayın.


![SATOCHIP](assets/notext/10.webp)


"*Bağlı Hardware Wallet*" düğmesine tıklayın.


![SATOCHIP](assets/notext/11.webp)


"*Tarama...*" düğmesine tıklayın.


![SATOCHIP](assets/notext/12.webp)


Satochip'iniz görünmelidir. "*Anahtar Deposunu Aktar*" üzerine tıklayın.


![SATOCHIP](assets/notext/13.webp)


Ardından, Satochip'inizin kilidini açmak için bir PIN kodu ayarlamanız gerekir. Güçlü bir şifre seçin, 4 ila 16 karakter arasında. Bu parolanın bir yedeğini alın.


Bu şifrenin bir passphrase olmadığını unutmayın. Bu, bu şifre olmadan da Mnemonic ifadenizin gerektiğinde Wallet'ünüzü yazılıma yeniden aktarmanıza izin vereceği anlamına gelir. Şifre yalnızca Satochip'in kendisine erişimi güvence altına almak için kullanılır. Diğer donanım cüzdanlarında bulunan PIN koduna eşdeğerdir.


Şifre girildikten sonra, "*Anahtar Deposunu* Aktar" düğmesine tekrar tıklayın.


![SATOCHIP](assets/notext/14.webp)


Parolayı tekrar not edin, ardından "*Başlat*" düğmesine tıklayın.


![SATOCHIP](assets/notext/15.webp)


Daha sonra Mnemonic ifadenizi oluşturmak için pencereye ulaşırsınız. "*generate Yeni*" düğmesine tıklayın.


![SATOCHIP](assets/notext/16.webp)

Kurtarma ifadenizi bir kağıda veya metal bir ortama yazarak bir veya daha fazla fiziksel kopyasını oluşturun. Unutmayın, bu ifade herhangi bir ek koruma olmaksızın bitcoinlerinize tam erişim sağlar. Bu nedenle, eğer birisi bunu keşfederse, Satochip'inize veya PIN koduna erişimi olmasa bile bitcoinlerinizi anında çalabilir. Bu nedenle bu yedeklerin güvenliğini sağlamak önemlidir. Ayrıca, bu ifade, Satochip'in kaybolması, hasar görmesi veya PIN kodunuzu unutmanız durumunda bitcoinlerinize yeniden erişmenizi sağlar.

![SATOCHIP](assets/notext/17.webp)


Bitcoin Wallet'niz başarıyla oluşturulmuştur.


![SATOCHIP](assets/notext/18.webp)


"*Import Keystore*" düğmesine tekrar tıklayın.


![SATOCHIP](assets/notext/19.webp)


Wallet'iniz şimdi oluşturuldu. Özel anahtarlarınız artık Satochip'inizin akıllı kartında saklanmaktadır. Devam etmek için "*Apply*" düğmesine tıklayın.


![SATOCHIP](assets/notext/20.webp)


Satochip'inizin PIN koduna ek olarak Sparrow wallet tarafından yönetilen genel bilgileri güvence altına almak için ek bir şifre belirlemeniz önerilir. Bu şifre, Sparrow wallet'a erişimin güvenliğini sağlayacak ve genel anahtarlarınızı, adreslerinizi ve işlem geçmişinizi herhangi bir yetkisiz erişime karşı korumaya yardımcı olacaktır.


![SATOCHIP](assets/notext/21.webp)


Şifrenizi iki alana girin ve ardından "*Şifre Ayarla*" düğmesine tıklayın.


![SATOCHIP](assets/notext/22.webp)


Ve işte, Satochip'iniz artık Sparrow wallet üzerinde yapılandırıldı.


![SATOCHIP](assets/notext/23.webp)


Artık Wallet'iniz oluşturulduğuna göre, Satochip'inizin bağlantısını kesebilirsiniz. Güvenli bir yerde saklayın!


## Satochip ile bitcoin nasıl alınır?


Wallet'nize girdikten sonra "*Alma*" sekmesine tıklayın.


![SATOCHIP](assets/notext/24.webp)


Sparrow wallet, Wallet'iniz için bir Address oluşturur. Genellikle, diğer donanım cüzdanları için, Address'ü doğrudan cihazın ekranında doğrulamak için "*Address'ü Göster*" seçeneğine tıklamanız önerilir. Ne yazık ki, bu seçenek Satochip'te mevcut değildir, ancak diğer cüzdanlarınız için kullandığınızdan emin olun.


![SATOCHIP](assets/notext/25.webp)


Bu Address ile güvence altına alınacak bitcoinlerin kaynağını açıklamak için bir "*Etiket*" ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenize yardımcı olan iyi bir uygulamadır.


![SATOCHIP](assets/notext/26.webp)


Etiketleme hakkında daha fazla bilgi için bu diğer eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Daha sonra bu Address'yi bitcoin almak için kullanabilirsiniz.


![SATOCHIP](assets/notext/27.webp)

## Satochip ile Bitcoin Nasıl Gönderilir?

Artık Satochip ile güvenli Wallet'unuzda ilk Sats'nizi aldığınıza göre, onları da harcayabilirsiniz! Satochip'inizi bilgisayarınıza bağlayın, Sparrow wallet'i başlatın ve ardından yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.


![SATOCHIP](assets/notext/28.webp)


Coin kontrolü yapmak, yani işlemde hangi UTXO'ların tüketileceğini özellikle seçmek istiyorsanız, "*UTXOs*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesinin aynı ekranına yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçili olacaktır.


![SATOCHIP](assets/notext/29.webp)


Hedef Address'yi girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.


![SATOCHIP](assets/notext/30.webp)


Bu harcamanın amacını hatırlamak için bir "*Etiket*" not edin.


![SATOCHIP](assets/notext/31.webp)


Bu Address'e gönderilen miktarı seçin.


![SATOCHIP](assets/notext/32.webp)


İşleminizin ücret oranını mevcut piyasaya göre ayarlayın.


![SATOCHIP](assets/notext/33.webp)


İşleminizin tüm parametrelerinin doğru olduğundan emin olun ve ardından "*İşlem Oluştur*" seçeneğine tıklayın.


![SATOCHIP](assets/notext/34.webp)


Her şey sizi tatmin ediyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![SATOCHIP](assets/notext/35.webp)


"*İmzala*" üzerine tıklayın.


![SATOCHIP](assets/notext/36.webp)


Satochip'inizin yanındaki "*İmzala*" düğmesine tekrar tıklayın.


![SATOCHIP](assets/notext/37.webp)


Satochip'inizin PIN kodunu girin, ardından işleminizi imzalamak için tekrar "*İmzala*" düğmesine tıklayın.


![SATOCHIP](assets/notext/38.webp)


İşleminiz artık imzalanmıştır. İşlemi Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" seçeneğine tıklayın.


![SATOCHIP](assets/notext/39.webp)


Bunu Sparrow wallet'in "*İşlemler*" sekmesinde bulabilirsiniz.


![SATOCHIP](assets/notext/40.webp)


Tebrikler, artık Satochip kullanımı hakkında bilgi sahibisiniz! Bu öğreticiyi yararlı bulduysanız, aşağıda bir başparmak yukarı takdir ediyorum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!