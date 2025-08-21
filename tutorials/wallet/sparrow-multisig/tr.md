---
name: Sparrow wallet - Multisig
description: Sparrow üzerinde çoklu imzalı bir Wallet oluşturun
---
![cover](assets/cover.webp)



Çoklu-imzalı Wallet (genellikle "*Multisig*" olarak adlandırılır), bir harcamayı yetkilendirmek için farklı anahtarlardan birkaç kriptografik imza gerektiren bir Bitcoin Wallet yapısıdır. Bir UTXO'nin kilidini açmak için tek bir özel anahtarın yeterli olduğu geleneksel ("*singlesig*") Wallet'nın aksine, Multisig bir **m-of-n** modeline dayanır: Wallet ile ilişkili _n_ anahtardan _m_'si her işlemi zorunlu olarak birlikte imzalamalıdır.



Bu mekanizma, bir Wallet'in kontrolünün birkaç varlık veya cihaz arasında paylaşılmasını sağlar. Örneğin, 3'te 2 yapılandırmasında, üç bağımsız anahtar seti oluşturulur, ancak fonları serbest bırakmak için yalnızca iki tanesine ihtiyaç vardır. Bu mimari, bir anahtarın ele geçirilmesi veya kaybedilmesiyle ilişkili riskleri büyük ölçüde azaltır: sadece bir anahtara erişimi olan bir hırsız Wallet'i boşaltamaz ve birini kaybeden bir kullanıcı kalan iki anahtarla fonlarına erişmeye devam edebilir.



![Image](assets/fr/01.webp)



Ancak, bu daha fazla güvenlik daha fazla karmaşıklığı da beraberinde getirir. Bir Multisig Wallet kurmak, birkaç Mnemonic ifadesinin (imza faktörü başına bir tane) ve genişletilmiş açık anahtarların ("*xpub*") güvenliğini sağlamayı gerektirir. Gerçekten de, Multisig 2-of-3 Wallet kullanıyorsanız, Wallet'i almak için ya üç Mnemonic ifadesinin hepsine ya da üç ifadeden en az ikisine sahip olmanız gerekir. Ancak üç ifadeden yalnızca ikisine sahipseniz, üç *xpubs*'a da erişmeniz gerekir, bu olmadan korudukları bitcoinlere erişmek için gereken açık anahtarları almak imkansız olacaktır.



Özetlemek gerekirse, bir Multisig Wallet'ü kurtarmak için şunları yapmanız gerekir:




- Veya her bir imza faktörüyle ilişkili tüm Mnemonic ifadelerine erişin;
- İmzalayabilmek için eşiğin gerektirdiği minimum sayıda Mnemonic ifadesine sahip olmak ve ayrıca gerekli açık anahtarları almak için tüm faktörlerin xpub'larına erişmek.



![Image](assets/fr/02.webp)



Multisig Wallet yedeklerinin bu yönetimi, fonlara erişmek için gereken tüm genel verileri bir araya getiren *Çıkış Komut Dosyası Tanımlayıcıları* ile kolaylaştırılmıştır. Ancak bu işlevsellik henüz tüm Wallet yönetim yazılımlarında uygulanmamaktadır.



Multisig özellikle gelişmiş güvenlik veya toplu fon yönetimi arayan bitcoin kullanıcıları için uygundur: şirketler, dernekler, aileler veya önemli miktarda bitcoin tutan bireysel kullanıcılar. Örneğin, imza yetkisini birkaç yönetici veya ekip üyesi arasında dağıtmak için merkezi olmayan yönetişim planları oluşturmak için kullanılabilir.



Bu eğitimde, **Sparrow wallet** ile klasik bir çoklu imza Wallet'nin nasıl oluşturulacağını ve kullanılacağını öğreneceğiz. Zaman kilitleri ile özelleştirilmiş bir çoklu imza Wallet oluşturmak istiyorsanız, bunun yerine Liana kullanmanızı öneririm:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Ön Koşullar



Bu eğitimde size [Sparrow wallet Wallet yönetim yazılımı] (https://sparrowwallet.com/download/) ile nasıl Multisig yapacağınızı göstereceğim. Eğer bu yazılımı henüz yüklemediyseniz, lütfen şimdi yükleyin. Yardıma ihtiyacınız olursa, Sparrow wallet'nin yapılandırılması hakkında ayrıntılı bir eğitimimiz de var:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Çoklu imzalı bir Wallet kurmak için farklı donanım cüzdanlarına ihtiyacınız olacaktır. Örneğin bir Multisig 2-de-3 için, :




- Trezor Model 1;
- Ledger Flex;
- Bir Coldcard MK3.



![Image](assets/fr/03.webp)



Multisig konfigürasyonunuzda farklı marka Hardware Wallet kullanmak iyi bir fikirdir. Bu, belirli bir modelin ciddi bir sorunla karşılaşması halinde bunun Multisig'unuzun genel güvenliğini etkilememesini sağlar. Dahası, her cihazın kendine özgü avantajlarından yararlanmanıza olanak tanır. Örneğin, benim yapılandırmamda :





- Trezor Model One tamamen açık kaynaklıdır ve bu da seed neslini doğrulamayı mümkün kılmaktadır. Ancak, bir secure element ile donatılmadığı için fiziksel saldırılara karşı savunmasız kalmaktadır;





- Öte yandan Ledger Flex, doğrulanamayan tescilli ürün yazılımından yararlanır, ancak mükemmel fiziksel koruma sunan bir secure element içerir;





- Coldcard bir secure element ile donatılmıştır ve kodu aranabilir. Diğer modellerde bulunmayan doğrulama özellikleri sunduğu için konfigürasyonumuz için ilginç bir seçimdir.



Multisig Wallet'inizi yapılandırmadan önce, her bir Hardware Wallet'in doğru yapılandırıldığından emin olun (Mnemonic oluşturma ve kaydetme, PIN tanımı). Ayrıntılı talimatlar için, her bir Hardware Wallet için eğitimlerimize başvurabilirsiniz, örneğin :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Bu eğitimde daha sonra göreceğimiz gibi, Multisig yapılandırmanıza bir Hardware Wallet ile ilişkili olmayan, ancak özel anahtarları bilgisayarınızda depolanan bir faktörü entegre etmek de mümkündür. Bu yöntemin donanım cüzdanlarının özel kullanımından daha az güvenli olduğu açıktır, ancak bazı durumlarda uygun olabilir. Örneğin, bir Multisig 2-de-3 için iki donanım cüzdanı ve bir Software Wallet tercih edebilirsiniz.



## Multisig Wallet Oluşturma



Sparrow wallet'ü açın, "*Dosya*" sekmesine tıklayın, ardından "*Yeni Wallet*"i seçin.



![Image](assets/fr/04.webp)



Çoklu imza Wallet'nıza bir ad atayın, ardından onaylamak için "*Wallet* Oluştur "a tıklayın.



![Image](assets/fr/05.webp)



"*Policy Type*" açılır menüsünde "*Multi Signature*" seçeneğini seçin.



![Image](assets/fr/06.webp)



Sağ üst köşede, artık Multisig'nizdeki toplam anahtar sayısını ve bir harcamayı yetkilendirmek için gereken ortak imzalayan sayısını tanımlayabilirsiniz. Benim örneğimde, bu 3'te 2'lik bir şemadır.



![Image](assets/fr/07.webp)



Pencerenin alt kısmında, Sparrow wallet üç adet "*Keystore*" görüntüler. Her biri bir anahtar kümesini temsil eder. Burada üç donanım cüzdanı kullanıyorum, bu nedenle her "*Keystore*" bunlardan birine karşılık geliyor. Şimdi bunları yapılandıracağız.



Coldcard ile başlıyorum. "*Keystore 1*" sekmesinde "*Airgapped Hardware Wallet*" seçeneğini seçiyorum.



![Image](assets/fr/08.webp)



Coldcard'da, cihazın kilidi açıldıktan sonra, "*Ayarlar*" menüsüne, ardından "*Multisig Cüzdanlar*"a gidiyorum.



![Image](assets/fr/09.webp)



Bu menü Coldcard'ın katıldığı Multisig cüzdanlarını yönetmenizi sağlar. Yeni bir tane oluşturmak istiyorum, bu yüzden "*Export XPUB*" seçeneğini seçiyorum.



![Image](assets/fr/10.webp)



"*Hesap numarası*" alanı için, yalnızca bir hesabı yönetiyorsanız, boş bırakabilir ve onay düğmesine basarak doğrudan doğrulayabilirsiniz.



![Image](assets/fr/11.webp)



Coldcard daha sonra Mikro SD karta kaydedilmiş xpub'ınızı içeren bir dosyayı generate yapacaktır.



![Image](assets/fr/12.webp)



Bu Micro SD'yi bilgisayarınıza takın. Sparrow wallet'te, "*Coldcard Multisig*"ün yanındaki "*Dosya Aktar...*" düğmesine tıklayın, ardından karttaki Coldcard tarafından oluşturulan dosyayı seçin.



![Image](assets/fr/13.webp)



Xpub'ınız başarıyla içe aktarıldı. Şimdi prosedürü diğer iki donanım cüzdanı ile tekrarlayacağız.



![Image](assets/fr/14.webp)



Ledger Flex için "*Keystore 2*" öğesini seçiyorum, ardından "*Connected Hardware Wallet*" öğesine tıklıyorum. Ledger'nin bilgisayara bağlı olduğundan, kilidinin açık olduğundan ve Bitcoin uygulamasının açık olduğundan emin olun.



![Image](assets/fr/15.webp)



Ardından "*Tarama...*" düğmesine tıklayın.



![Image](assets/fr/16.webp)



Hardware Wallet'inizin adının yanında "*Anahtar Deposunu Aktar*" seçeneğine tıklayın.



![Image](assets/fr/17.webp)



İkinci imza sahibi artık Sparrow wallet'a doğru şekilde kaydedilmiştir.



![Image](assets/fr/18.webp)



Multisig yapılandırmasını sonlandırmak için Trezor One ile aynı prosedürü tekrarlıyorum.



![Image](assets/fr/19.webp)



Yapılandırmamda bu durumu ele almıyoruz, ancak Multisig'nize Sparrow (Hot Wallet) içindeki bir Software Wallet aracılığıyla bir imza eklemek istiyorsanız, "*Yeni veya İçe Aktarılan Software Wallet*" düğmesine tıklamanız yeterlidir.



Artık tüm imza cihazlarınız Sparrow wallet'ya aktarıldığına göre, "*Uygula*" düğmesine tıklayarak Multisig'nin oluşturulmasını tamamlayabilirsiniz.



![Image](assets/fr/20.webp)



Sparrow wallet Wallet cihazınıza erişimi güvence altına almak için güçlü bir parola seçin. Bu parola genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı korur.



Kaybetmemek için bu parolayı parola yöneticisi gibi güvenli bir yere kaydetmeyi unutmayın.



![Image](assets/fr/21.webp)



## Bir Multisig Wallet'i yedekleme



Şimdi *Çıktı Senaryomuzu Descriptor* Coldcard'a kaydedeceğiz (bu sadece Multisig'lerinde Coldcard olan kullanıcılar için geçerlidir) ve hepsinden önemlisi, bunun bir yedeğini bağımsız bir ortamda tutacağız.



Descriptor*, Multisig Wallet'inizdeki tüm xpub'ları ve anahtarları generate yapmak için kullanılan türetme yollarını içerir. Bölüm 1'de gördüklerimizi hatırlayın: bir Multisig Wallet'i geri yüklemek için ya **tüm** Mnemonic ifadelerine ya da yalnızca imza eşiğine ulaşmak için gereken minimum sayıya sahip olmanız gerekir. Ancak, ikinci durumda, eksik imzacıların **xpub'larına** sahip olmak da şarttır. Descriptor* tüm Multisig'larınızın xpub'larını içerir.



Bu açık değilse, şunu hatırlayın: bir Multisig almak için, eşiğe bağlı olarak kullanılan her Hardware Wallet için minimum sayıda Mnemonic ifadesine (benim durumumda: 2 ifade) ve *Descriptor*'e ihtiyacınız vardır.



Bu *Descriptor* özel anahtarlar içermez, sadece genel anahtarlar içerir. Bu, fonlara erişim sağlamadığı anlamına gelir. Bu nedenle, bitcoinlerinize tam erişim sağlayan Mnemonic ifadeleri kadar kritik değildir. Descriptor* ile ilgili risk yalnızca gizlilikle ilgilidir: ele geçirilmesi durumunda, üçüncü bir taraf tüm işlemlerinizi gözlemleyebilir, ancak paranızı harcayamaz.



Bu *Descriptor*'in birkaç kopyasını oluşturmanızı ve bunları Multisig'nızdaki her bir imzalama cihazında saklamanızı şiddetle tavsiye ederim. Örneğin, benim durumumda, *Descriptor*'i kağıda yazdırıyorum ve bir kopyasını Coldcard'da, diğerini Trezor'da ve bir kopyasını da Ledger'de saklıyorum. Ayrıca bu *Descriptor*'i PDF dosyası olarak her biri donanım cüzdanlarından birinde saklanan üç USB belleğe kaydediyorum. Bu şekilde, bu *Descriptor*'i asla kaybetmeme şansımı en üst düzeye çıkarıyorum ve her cihazda iki kopyaya (bir fiziksel ve bir dijital) sahip olduğumdan emin oluyorum.



Multisig Wallet oluşturulduktan sonra, Sparrow size otomatik olarak bu *Descriptor*'i sağlar. Hem metin hem de QR kodu olarak kaydetmek için "*PDF Kaydet...*" düğmesine tıklayın.



![Image](assets/fr/22.webp)



Daha sonra bu PDF'yi yazdırabilir ve USB belleklerinize kopyalayabilirsiniz.



![Image](assets/fr/23.webp)



Ayrıca bu *Descriptor*'yi Coldcard'a da kaydedeceğiz (yapılandırmanızda bir tane kullanıyorsanız). Bu, Coldcard'ın daha sonra imzalanan her işlemin orijinal Wallet'e karşılık geldiğini doğrulamasını sağlayacaktır: doğru xpub'lar, doğru Address formatı, doğru türetme yolu... Bu içe aktarılmış *Descriptor* olmadan Coldcard, Exchange adreslerinin ele geçirilmediğini veya PSBT ile oynanmadığını doğrulayamaz.



Coldcard'ı Multisig'de bu kadar ilginç kılan da budur: diğer donanım cüzdanlarının izin vermediği bazı karmaşık saldırılara karşı ek kontroller sunar (tabii ki imzalamak için kullanmanız şartıyla).



Sparrow'de "*Ayarlar*" menüsüne erişin, ardından "*Dışa Aktar...*" seçeneğine tıklayın.



![Image](assets/fr/24.webp)



"*Coldcard Multisig*" seçeneğinin yanında, "*Dosyayı Dışa Aktar...*" seçeneğine tıklayın ve metin dosyasını Micro SD karta kaydedin.



![Image](assets/fr/25.webp)



Ardından kartı Coldcard'a takın. "*Ayarlar*" menüsüne gidin, ardından "*Multisig Cüzdanları*" ve "*SD'den Aktar*" öğesini seçin.



![Image](assets/fr/26.webp)



Uygun dosyayı seçin ve içe aktarmayı onaylayın.



![Image](assets/fr/27.webp)



Yeni içe aktardığınız Multisig'in adına tıklayın.



![Image](assets/fr/28.webp)



Multisig yapılandırma parametrelerini kontrol edin, ardından kaydı onaylayın.



![Image](assets/fr/29.webp)



Multisig'ünüz artık Coldcard'ınıza doğru şekilde kaydedilmiştir. Aynı Multisig'te birden fazla Coldcard'ınız varsa, bu prosedürü her biri için tekrarlayın.



Descriptor*'ü kaydetmenin yanı sıra, imza cihazlarınızın her biri için Mnemonic cümlelerini kaydetmeye özellikle dikkat etmeyi unutmayın. Yeni başlıyorsanız, bunları nasıl kaydedeceğinizi ve doğru şekilde yöneteceğinizi öğrenmek için bu diğer eğitime başvurmanızı şiddetle tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Multisig'inizdeki ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. İlk alınan Address gibi bazı referans bilgilerini not edin, ardından Wallet hala boşken donanım cüzdanlarınızı sıfırlayın. Ardından, Mnemonic ifade kağıdı yedeklerinizi kullanarak Multisig Wallet'inizi Donanım Cüzdanlarında, ardından *Descriptor* kullanarak Sparrow'da geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan ilk Address'un başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.



Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime başvurmanızı öneririm:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Multisig'niz üzerinden bitcoin alın



Wallet'ünüz artık bitcoin almaya hazır. Sparrow'te "*Receive*" sekmesine tıklayın.



![Image](assets/fr/30.webp)



Sparrow wallet tarafından üretilen Address'yı kullanmadan önce, doğrudan donanım cüzdanlarınızın ekranında kontrol etmek için zaman ayırın. Bu, Address'nın değiştirilmediğinden ve cihazlarınızın ilgili fonları harcamak için gereken özel anahtarlara sahip olduğundan emin olmanızı sağlayacaktır. Bu, sizi bir dizi saldırı vektörüne karşı korumaya yardımcı olur.



Bunu yapmak için, kabloyla bağlıyken Address'yi Trezor'unuzda veya Ledger'de görüntülemek için "*Address'yi Görüntüle*" seçeneğine tıklayın.



![Image](assets/fr/31.webp)



Coldcard ile bu doğrulama Sparrow ile herhangi bir etkileşim olmadan gerçekleştirilebilir. Basitçe "*Address Explorer*" menüsünü açın, ardından en alttan Multisig'unuzu seçin.



![Image](assets/fr/32.webp)



Daha sonra Multisig tarafından oluşturulan alım adreslerini göreceksiniz.



![Image](assets/fr/33.webp)



Her bir Hardware Wallet'te görüntülenen Address'in Sparrow wallet'tekine tam olarak karşılık geldiğini kontrol edin. Bütünlüğünden emin olmak için bunu Address'i mükellefle paylaşmadan hemen önce yapmanız tavsiye edilir.



Daha sonra alınan bitcoinlerin kaynağını belirtmek için bu Address'ya bir "*Etiket*" atayabilirsiniz. Bu, UTXO'larınızın yönetimini organize etmenin iyi bir yoludur.



![Image](assets/fr/34.webp)



Bu doğrulandıktan sonra, bitcoin almak için Address'yi kullanabilirsiniz.



![Image](assets/fr/35.webp)



## Multisig'iniz ile bitcoin gönderme



Artık Multisig Wallet'inizdeki ilk Sat'larınızı aldığınıza göre, onları da harcayabilirsiniz! Sparrow'da yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.



![Image](assets/fr/36.webp)



Eğer *Coin Kontrolü* kullanmak istiyorsanız, yani harcamak istediğiniz UTXO'ları manuel olarak seçmek istiyorsanız, "*UTXOs*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. UTXO'ların önceden doldurulmuş olduğu "*Gönder*" sekmesine otomatik olarak yönlendirileceksiniz.



![Image](assets/fr/37.webp)



Hedef Address'ü girin. "*+ Ekle*" üzerine tıklayarak birden fazla adres eklenebilir.



![Image](assets/fr/38.webp)



İşlemlerinizi takip etmeyi kolaylaştırmak için bu giderin amacını açıklayan bir "*Etiket*" ekleyin.



![Image](assets/fr/39.webp)



Seçilen Address'e gönderilecek tutarı girin.



![Image](assets/fr/40.webp)



Şarj oranını mevcut şebeke koşullarına göre ayarlayın. Örneğin, uygun bir şarj seviyesi seçmek için [Mempool.space](https://Mempool.space/) adresine bakın.



Tüm işlem parametrelerini kontrol ettikten sonra "*İşlem Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/41.webp)



Her şeyden memnunsanız, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.



![Image](assets/fr/42.webp)



Ekranın alt kısmında Sparrow'nin 2 imza beklediğini göreceksiniz. Bu normaldir: burada kullanılan Wallet bir Multisig 2-de-3'tür.



![Image](assets/fr/43.webp)



Coldcard'ım ile imzalamaya başlıyorum. Bunu yapmak için bilgisayara bir Micro SD kart takıyorum, ardından "*İşlemi Kaydet*" seçeneğine tıklıyorum.



![Image](assets/fr/44.webp)



İmzalanacak işlemi Hardware Wallet'unuza aktarmanın ve ardından Sparrow'tan almanın 3 yolu vardır. Birincisi, burada Coldcard için yapacağımız gibi bir Micro SD kart kullanmaktır. İkincisi, ikinci imza için kullanacağımız kablo bağlantısıdır (Ledger ve Trezor). Son olarak, Coldcard Q, Jade Plus veya Passport V2 gibi kamera donanımlı cihazlar için QR kod iletişimini kullanmak mümkündür.



PSBT (*Partially Signed Bitcoin Transaction*) Micro SD'ye kaydedildikten sonra, bunu Coldcard MK3'e takıyorum, ardından "*İmzalamaya Hazır*" menüsünü seçiyorum.



![Image](assets/fr/45.webp)



Hardware Wallet ekranınızda işlem parametrelerini dikkatlice kontrol edin: alıcının Address'i, gönderilen tutar ve ücretler. İşlem onaylandıktan sonra, imzaya geçmek için doğrulayın.



![Image](assets/fr/46.webp)



Ardından Micro SD'yi bilgisayarınıza geri koyun ve Sparrow'da "*İşlem Yükle*" seçeneğine tıklayın. Dosyalarınızdan Coldcard tarafından imzalanmış PSBT'yi seçin.



![Image](assets/fr/47.webp)



Coldcard imzasının eklendiğini görebilirsiniz. Şimdi gerekli ikinci imzayı gerçekleştirmek için ikinci bir cihaz, bu durumda Ledger kullanacağım. Bağlıyorum, kilidini açıyorum ve ardından Sparrow'de "*İmzala*" seçeneğine tıklıyorum.



![Image](assets/fr/48.webp)



Hardware Wallet'nizin adının yanındaki "*İmzala*" düğmesine tıklayın.



![Image](assets/fr/49.webp)



Ledger'ünüzü bu Multisig ile ilk kez kullandığınızda, Sparrow sizden ortak imzalayanların genişletilmiş açık anahtarlarını (xpubs) doğrulamanızı isteyecektir. Coldcard'da olduğu gibi, bu adım daha sonra körü körüne imzalama yapmanızı engeller. Bu bilgiyi doğrulamak için, Ledger ekranında görüntülenen xpub'ı doğrudan diğer donanım cüzdanlarınız tarafından sağlananlarla karşılaştırın.



![Image](assets/fr/50.webp)



Alıcının Address'ünü, aktarılan tutarı ve işlem ücretini kontrol edin, ardından işlemi imzalayın.



![Image](assets/fr/51.webp)



İmzalamak için ekrana basın.



![Image](assets/fr/52.webp)



Sparrow artık Multisig Wallet'den fonları serbest bırakmak için gereken iki imzaya sahiptir. İşlemi son bir kez kontrol edin ve her şey yolunda giderse, ağ üzerinden yayınlamak için "*İşlemi Yayınla*" seçeneğine tıklayın.



![Image](assets/fr/53.webp)



Bu işlemi Sparrow wallet'in "*İşlemler*" sekmesinde bulabilirsiniz.



![Image](assets/fr/54.webp)



Tebrikler, artık Sparrow üzerinde çoklu imza Wallet'ı nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Lütfen bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!



Daha ileri gitmek için, Bitcoin Wallet'ünüzün güvenliğini artırmaya yönelik bir başka yöntem olan passphrase BIP39 hakkındaki bu eğitime başvurmanızı tavsiye ederim:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7