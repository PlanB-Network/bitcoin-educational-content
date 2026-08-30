---
name: Sparrow Wallet - Çoklu imza
description: Sparrow üzerinde çoklu imzalı bir cüzdan oluşturun
---
![kapak](assets/cover.webp)


Çoklu imzalı cüzdan (sıklıkla "*Multisig*" olarak adlandırılır), bir harcamayı yetkilendirmek için farklı anahtarlardan birden fazla kriptografik imza gerektiren bir Bitcoin cüzdan yapısıdır. Bir UTXO'nun kilidini açmak için tek bir özel anahtarın yeterli olduğu geleneksel ("*singlesig*") cüzdandan farklı olarak Multisig, **m-of-n** modeline dayanır: cüzdanla ilişkili _n_ anahtarın içinden _m_ tanesi her işlemi mutlaka birlikte imzalamalıdır.


Bu mekanizma, bir cüzdanın kontrolünün birkaç varlık veya cihaz arasında paylaşılmasını sağlar. Örneğin, 3'te 2 yapılandırmada üç bağımsız anahtar seti oluşturulur, ancak fonları serbest bırakmak için yalnızca ikisi gerekir. Bu mimari, bir anahtarın ele geçirilmesi veya kaybolmasıyla ilişkili riskleri ciddi ölçüde azaltır: yalnızca bir anahtara erişimi olan bir hırsız cüzdanı boşaltamaz ve bir anahtarını kaybeden kullanıcı kalan iki anahtarla fonlarına hâlâ erişebilir.


![Görsel](assets/fr/01.webp)


Ancak bu daha yüksek güvenlik, daha yüksek karmaşıklıkla birlikte gelir. Bir Multisig cüzdanı kurmak, birkaç mnemonic ifadeyi (imza faktörü başına bir tane) ve genişletilmiş açık anahtarları ("*xpub*") güvenceye almayı gerektirir. Gerçekten de, 3'te 2 bir Multisig cüzdan kullanıyorsanız cüzdanı geri almak için ya üç mnemonic ifadenin tamamına ya da üç ifadenin en az ikisine sahip olmanız gerekir. Ancak üç ifadeden yalnızca ikisine sahipseniz üç *xpub*'a da erişmeniz gerekir; bunlar olmadan korudukları bitcoinlere erişmek için gerekli açık anahtarları geri almak imkânsız olur.


Özetlemek gerekirse, bir Multisig cüzdanı kurtarmak için şunlara sahip olmanız gerekir:


- Ya her imza faktörüyle ilişkili tüm mnemonic ifadelere erişim;
- Ya da imza atabilmek için eşik tarafından gerekli kılınan asgari mnemonic ifade sayısı ve gerekli açık anahtarları geri almak için tüm faktörlerin xpub'larına erişim.


![Görsel](assets/fr/02.webp)


Multisig cüzdan yedeklerinin bu yönetimi, fonlara erişmek için gereken tüm açık verileri bir araya getiren *Çıktı betiği tanımlayıcıları* sayesinde kolaylaşır. Ancak bu işlev henüz tüm cüzdan yönetim yazılımlarında uygulanmış değildir.


Multisig, özellikle daha yüksek güvenlik veya fonların kolektif yönetimini arayan bitcoin kullanıcıları için uygundur: şirketler, dernekler, aileler veya kayda değer miktarda bitcoin tutan bireysel kullanıcılar. Örneğin imza yetkisini birkaç yönetici veya ekip üyesi arasında dağıtmak için merkeziyetsiz yönetişim düzenleri oluşturmakta kullanılabilir.


Bu öğreticide, **Sparrow Wallet** ile klasik bir çoklu imza cüzdanı oluşturmayı ve kullanmayı öğreneceğiz. Zaman kilitleriyle özelleştirilmiş bir çoklu imza cüzdanı oluşturmak isterseniz bunun yerine Liana kullanmanızı öneririm:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Ön koşullar


Bu öğreticide, [Sparrow Wallet cüzdan yönetim yazılımı](https://sparrowwallet.com/download/) ile nasıl Multisig yapılacağını göstereceğim. Bu yazılımı henüz kurmadıysanız lütfen şimdi kurun. Yardıma ihtiyacınız varsa Sparrow Wallet yapılandırması hakkında ayrıntılı bir öğreticimiz de var:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Çoklu imzalı bir cüzdan kurmak için farklı donanım cüzdanlarına ihtiyacınız olacaktır. Örneğin 3'te 2 bir Multisig için şunları kullanabilirsiniz:


- Bir Trezor Model One;
- Ledger Flex;
- Bir Passport Core.


![Görsel](assets/fr/03.webp)


Multisig yapılandırmanızda farklı donanım cüzdanı markaları kullanmak iyi bir fikirdir. Bu, belirli bir model ciddi bir sorunla karşılaşırsa bunun Multisig'inizin genel güvenliğini etkilememesini sağlar. Ayrıca her cihazın kendine özgü avantajlarından yararlanmanıza olanak tanır. Örneğin benim yapılandırmamda:



- Trezor Model One tamamen açık kaynaklıdır; bu da seed oluşturmayı doğrulamayı mümkün kılar. Ancak Secure Element ile donatılmadığı için fiziksel saldırılara karşı savunmasız kalır;



- Ledger Flex ise doğrulanamayan tescilli firmware'den yararlanır, ancak mükemmel fiziksel koruma sunan bir Secure Element içerir;



- Passport Core tamamen açık kaynaklı firmware'i, bir Secure Element'i ve air-gapped QR kod alışverişlerini birleştirir. USB veri bağlantısı olmadan adresleri doğrulayabilen ve PSBT'leri imzalayabilen bağımsız üçüncü imzalayıcıdır.


Multisig cüzdanınızı yapılandırmadan önce, her donanım cüzdanının doğru yapılandırıldığından emin olun (mnemonic oluşturma ve kaydetme, PIN tanımlama). Ayrıntılı talimatlar için her donanım cüzdanı hakkındaki öğreticilerimize bakabilirsiniz, örneğin:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Bu öğreticinin ilerleyen kısmında göreceğimiz gibi, Multisig yapılandırmanıza donanım cüzdanıyla ilişkili olmayan, özel anahtarları bilgisayarınızda saklanan bir faktör entegre etmek de mümkündür. Bu yöntem doğal olarak yalnızca donanım cüzdanlarının kullanılmasına göre daha az güvenlidir, ancak belirli durumlarda anlamlı olabilir. Örneğin 3'te 2 bir Multisig için iki donanım cüzdanı ve bir yazılım cüzdanı seçebilirsiniz.

> ⚠️ **Coldcard MK3 güvenlik bildirimi:** 4.2.0'dan eski firmware çalıştıran bir MK3 üzerinde yeni bir seed oluşturmayın. Daha eski firmware üzerinde oluşturulan seed'ler değiştirilmelidir ve fonlar taşınmalıdır. Bu nedenle bu öğretici, air-gapped referans imzalayıcı olarak Passport Core kullanır.


## Multisig cüzdanı oluşturma


Sparrow Wallet'ı açın, "*File*" sekmesine tıklayın, ardından "*New Wallet*" öğesini seçin.


![Görsel](assets/fr/04.webp)


Çoklu imzalı cüzdanınıza bir ad atayın, ardından onaylamak için "*Create Wallet*" üzerine tıklayın.


![Görsel](assets/fr/05.webp)


"*Policy Type*" açılır menüsünde "*Multi Signature*" seçeneğini seçin.


![Görsel](assets/fr/06.webp)


Sağ üst köşede artık Multisig'inizdeki toplam anahtar sayısını ve bir harcamayı yetkilendirmek için gereken ortak imzalayıcı sayısını tanımlayabilirsiniz. Benim örneğimde bu, 3'te 2 şemasıdır.


![Görsel](assets/fr/07.webp)


Pencerenin alt kısmında Sparrow Wallet üç "*Keystore*" gösterir. Her biri bir anahtar setini temsil eder. Burada üç donanım cüzdanı kullanıyorum, bu nedenle her "*Keystore*" bunlardan birine karşılık gelir. Şimdi bunları yapılandıracağız.


Passport Core ile başlıyorum. "*Keystore 1*" sekmesinde "*Airgapped Hardware Wallet*" seçeneğini seçiyorum.


![Görsel](assets/fr/08.webp)


Passport üzerinde kullanmak istediğiniz hesabı açın, ardından "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*" öğelerini seçin. Passport, açık anahtar bilgilerini içeren hareketli bir QR kodu gösterir.

Sparrow'da "*Passport*" yanında "*Scan...*" seçeneğini seçin ve bu hareketli QR kodunu bilgisayarınızın web kamerasıyla tarayın. Sparrow tarafından gösterilen ana anahtar parmak izini Passport tarafından gösterilenle karşılaştırın, ardından keystore'u içe aktarın.

Passport xpub'ınız artık içe aktarılmıştır. Ledger Flex ve Trezor Model One için uygun prosedürü tekrarlayın.


Ledger Flex için "*Keystore 2*" seçeneğini seçiyorum, ardından "*Connected Hardware Wallet*" üzerine tıklıyorum. Ledger'ın bilgisayara bağlı, kilidi açık ve Bitcoin uygulamasının açık olduğundan emin olun.


![Görsel](assets/fr/15.webp)


Ardından "*Scan...*" düğmesine tıklayın.


![Görsel](assets/fr/16.webp)


Donanım cüzdanınızın adının yanında "*Import Keystore*" üzerine tıklayın.


![Görsel](assets/fr/17.webp)


İkinci imzalayıcı artık Sparrow Wallet'ta doğru şekilde kaydedilmiştir.


![Görsel](assets/fr/18.webp)


Multisig yapılandırmasını tamamlamak için Trezor One ile tam olarak aynı prosedürü tekrarlıyorum.


![Görsel](assets/fr/19.webp)


Benim yapılandırmamda bu durumu ele almıyoruz, ancak Multisig'inize Sparrow içinde bir yazılım cüzdanı (sıcak cüzdan) aracılığıyla imza dahil etmek isterseniz yalnızca "*New or Imported Software Wallet*" düğmesine tıklamanız yeterlidir.


Artık tüm imza cihazlarınız Sparrow Wallet'a içe aktarıldığına göre "*Apply*" üzerine tıklayarak Multisig oluşturma işlemini tamamlayabilirsiniz.


![Görsel](assets/fr/20.webp)


Sparrow Wallet cüzdanınıza erişimi güvenceye almak için güçlü bir parola seçin. Bu parola açık anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı korur.


Bu parolayı kaybetmemek için parola yöneticisi gibi güvenli bir yerde saklamayı unutmayın.


![Görsel](assets/fr/21.webp)


## Multisig cüzdanını yedekleme


Şimdi *Çıktı betiği tanımlayıcısını* bağımsız bir ortamda kaydedeceğiz ve birkaç kopyasını saklayacağız.


*Tanımlayıcı*, Multisig cüzdanınızdaki tüm xpub'ları ve anahtarları oluşturmak için kullanılan türetme yollarını içerir. Bölüm 1'de gördüklerimizi hatırlayın: Bir Multisig cüzdanını geri yüklemek için ya **tüm** mnemonic ifadelere ya da imza eşiğine ulaşmak için gereken asgari sayıya sahip olmanız gerekir. Ancak ikinci durumda, eksik imzalayıcıların **xpub'larına** sahip olmak da zorunludur. *Tanımlayıcı*, Multisig'inizin tüm xpub'larını içerir.


Bu açık değilse yalnızca şunu hatırlayın: Bir Multisig'i geri almak için kullanılan her donanım cüzdanı için eşiğe bağlı olarak asgari sayıda mnemonic ifadeye (benim durumumda: 2 ifade) ve ayrıca *Tanımlayıcı*'ya ihtiyacınız vardır.


Bu *Tanımlayıcı* hiçbir özel anahtar içermez, yalnızca açık anahtarlar içerir. Bu, fonlara erişim sağlamadığı anlamına gelir. Bu nedenle bitcoinlerinize tam erişim sağlayan mnemonic ifadeler kadar kritik değildir. *Tanımlayıcı* ile ilgili risk yalnızca gizlilikle ilgilidir: ele geçirilmesi durumunda üçüncü bir taraf tüm işlemlerinizi gözlemleyebilir, ancak fonlarınızı harcayamaz.


Bu *Tanımlayıcı*'nın birkaç kopyasını oluşturmanızı ve bunları Multisig'inizdeki her imza cihazıyla birlikte saklamanızı güçlü şekilde öneririm. Örneğin benim durumumda *Tanımlayıcı*'yı kâğıda yazdırıyorum ve bir kopyasını Passport ile, birini Trezor ile, birini de Ledger ile saklıyorum. Ayrıca bu *Tanımlayıcı*'yı üç USB belleğe PDF dosyası olarak kaydediyorum; her biri donanım cüzdanlarından biriyle birlikte saklanıyor. Bu şekilde, bu *Tanımlayıcı*'yı asla kaybetmeme ihtimalimi en üst düzeye çıkarıyorum ve her cihazla birlikte iki kopyaya (biri fiziksel, biri dijital) sahip olduğumdan emin oluyorum.


Multisig cüzdanınız oluşturulduktan sonra Sparrow size bu *Tanımlayıcı*'yı otomatik olarak sağlar. Hem metin hem de QR kod olarak kaydetmek için "*Save PDF...*" düğmesine tıklayın.


![Görsel](assets/fr/22.webp)


Ardından bu PDF'yi yazdırabilir ve USB belleklerinize kopyalayabilirsiniz.


![Görsel](assets/fr/23.webp)


Passport, QR eşleştirme ve imzalama akışı sırasında ilgili anahtar bilgilerini göstermek ve doğrulamak için Sparrow tarafından içe aktarılan multisig yapılandırmasını kullanır. *Tanımlayıcı*'yı bağımsız olarak saklayın: bir imzalayıcı kullanılamaz durumdaysa cüzdanı kurtarmak için hâlâ zorunludur.


*Tanımlayıcı*'yı kaydetmenin yanı sıra, imza cihazlarınızın her biri için mnemonic ifadeleri kaydetmeye özellikle dikkat etmeyi unutmayın. Yeni başlıyorsanız bunları doğru şekilde kaydetmeyi ve yönetmeyi öğrenmek için bu diğer öğreticiye bakmanızı şiddetle tavsiye ederim:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Multisig'inize ilk bitcoinlerinizi almadan önce **boş bir kurtarma testi yapmanızı şiddetle tavsiye ederim**. İlk alım adresi gibi bazı referans bilgilerini not edin, ardından cüzdan hâlâ boşken donanım cüzdanlarınızı sıfırlayın. Daha sonra mnemonic ifade kâğıt yedeklerinizi kullanarak donanım cüzdanlarında Multisig cüzdanınızı, ardından *Tanımlayıcı*'yı kullanarak Sparrow'da geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan ilk adresin başlangıçta not ettiğiniz adresle eşleştiğini kontrol edin. Eşleşiyorsa kâğıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer öğreticiye bakmanızı öneririm:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Multisig'inizde bitcoin alma


Cüzdanınız artık bitcoin almaya hazır. Sparrow'da "*Receive*" sekmesine tıklayın.


![Görsel](assets/fr/30.webp)


Sparrow Wallet tarafından oluşturulan adresi kullanmadan önce, bunu doğrudan donanım cüzdanlarınızın ekranında kontrol etmek için zaman ayırın. Bu, adresin değiştirilmediğinden ve cihazlarınızın ilişkili fonları harcamak için gereken özel anahtarları tuttuğundan emin olmanızı sağlar. Bu, sizi birçok saldırı vektörüne karşı korumaya yardımcı olur.


Bunu yapmak için kabloyla bağlıyken adresi Trezor veya Ledger'ınızda göstermek üzere "*Display Address*" üzerine tıklayın.


![Görsel](assets/fr/31.webp)


Passport ile multisig hesabını seçin ve "*Verify Address*" öğesini seçin. Sparrow tarafından gösterilen alım adresinin QR kodunu tarayın. Passport, adresin multisig cüzdana ait olup olmadığını ekranında onaylar.


Her donanım cüzdanında gösterilen adresin Sparrow Wallet'taki adresle tam olarak aynı olduğunu kontrol edin. Bunu adresi ödeyen kişiyle paylaşmadan hemen önce yapmanız, bütünlüğünden emin olmak için tavsiye edilir.


Daha sonra alınan bitcoinlerin kaynağını belirtmek için bu adrese bir "*Label*" atayabilirsiniz. Bu, UTXO'larınızın yönetimini düzenlemenin iyi bir yoludur.


![Görsel](assets/fr/34.webp)


Bu doğrulandıktan sonra adresi bitcoin almak için kullanabilirsiniz.


![Görsel](assets/fr/35.webp)


## Multisig'inizle bitcoin gönderme


Multisig cüzdanınıza ilk satoshilerinizi aldığınıza göre artık onları harcayabilirsiniz! Sparrow'da yeni bir işlem oluşturmak için "*Send*" sekmesine gidin.


![Görsel](assets/fr/36.webp)


*Coin Control* kullanmak, yani harcamak istediğiniz UTXO'ları manuel olarak seçmek isterseniz "*UTXOs*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin, ardından "*Send Selected*" üzerine tıklayın. UTXO'lar önceden doldurulmuş şekilde otomatik olarak "*Send*" sekmesine yönlendirileceksiniz.


![Görsel](assets/fr/37.webp)


Hedef adresi girin. "*+ Add*" üzerine tıklayarak birden fazla adres eklenebilir.


![Görsel](assets/fr/38.webp)


Bu harcamanın amacını açıklamak ve işlemlerinizi takip etmeyi kolaylaştırmak için bir "*Label*" ekleyin.


![Görsel](assets/fr/39.webp)


Seçilen adrese gönderilecek tutarı girin.


![Görsel](assets/fr/40.webp)


Ücret oranını mevcut ağ koşullarına göre ayarlayın. Örneğin uygun bir ücret seviyesi seçmek için [Mempool.space](https://Mempool.space/) adresine bakın.


Tüm işlem parametrelerini kontrol ettikten sonra "*Create Transaction*" üzerine tıklayın.


![Görsel](assets/fr/41.webp)


Her şeyden memnunsanız "*Finalize Transaction for Signing*" üzerine tıklayın.


![Görsel](assets/fr/42.webp)


Ekranın alt kısmında Sparrow'un 2 imza beklediğini göreceksiniz. Bu normaldir: burada kullanılan cüzdan 3'te 2 Multisig'dir.


![Görsel](assets/fr/43.webp)


İmzalamaya Passport'umla başlıyorum. Sparrow'da PSBT'yi (*Partially Signed Bitcoin Transaction*) hareketli QR kodları olarak göstermek için "*Show QR*" üzerine tıklayın. Passport üzerinde multisig hesabını seçin ve "*Sign with QR Code*" öğesini seçin, ardından Sparrow tarafından gösterilen QR kodunu tarayın.


Donanım cüzdanınızın ekranında işlem parametrelerini dikkatlice kontrol edin: alıcının adresi, gönderilen tutar ve ücretler. İşlem onaylandıktan sonra imzaya geçmek için doğrulayın.


İşlemi onayladıktan sonra Passport imzalanmış PSBT'yi hareketli QR kodları olarak gösterir. Sparrow'da "*Scan QR*" üzerine tıklayın ve bu kodları web kameranızla tarayın. Ardından Passport imzası eklenir. Şimdi gereken ikinci imza için Ledger'ı kullanıyorum: bağlayıp kilidini açıyorum, ardından Sparrow'da "*Sign*" üzerine tıklıyorum.


![Görsel](assets/fr/48.webp)


Donanım cüzdanınızın adının yanında "*Sign*" üzerine tıklayın.


![Görsel](assets/fr/49.webp)


Ledger'ınızı bu Multisig ile ilk kez kullandığınızda Sparrow, ortak imzalayıcıların genişletilmiş açık anahtarlarını (xpub'larını) doğrulamanızı isteyecektir. Passport'ta olduğu gibi bu adım, daha sonra körlemesine imza atmanızı engeller. Bu bilgileri doğrulamak için Ledger ekranında gösterilen xpub'ı diğer donanım cüzdanlarınız tarafından doğrudan sağlananlarla karşılaştırın.


![Görsel](assets/fr/50.webp)


Alıcının adresini, aktarılan tutarı ve işlem ücretini kontrol edin, ardından işlemi imzalayın.


![Görsel](assets/fr/51.webp)


İmzalamak için ekrana basın.


![Görsel](assets/fr/52.webp)


Sparrow artık fonları Multisig cüzdanından serbest bırakmak için gereken iki imzaya sahiptir. İşlemi son bir kez kontrol edin ve her şey yolundaysa ağ üzerinde yayınlamak için "*Broadcast Transaction*" üzerine tıklayın.


![Görsel](assets/fr/53.webp)


Bu işlemi Sparrow Wallet'ın "*Transactions*" sekmesinde bulacaksınız.


![Görsel](assets/fr/54.webp)


Tebrikler, artık Sparrow üzerinde çoklu imzalı bir cüzdanı nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi yararlı bulduysanız aşağıya yeşil başparmak bırakmanızdan memnun olurum. Lütfen bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


Daha ileri gitmek için Bitcoin cüzdanınızın güvenliğini artırmaya yönelik başka bir yöntem olan BIP39 passphrase hakkındaki bu öğreticiye bakmanızı öneririm:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
