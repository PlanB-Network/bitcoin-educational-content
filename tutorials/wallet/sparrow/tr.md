---
name: Sparrow Wallet
description: Sparrow wallet'in kurulması, yapılandırılması ve kullanılması
---
![cover](assets/cover.webp)


![video](https://youtu.be/yJpvfRl03Tw)


Sparrow wallet, Craig Raw tarafından geliştirilen bir öz saklama Bitcoin Wallet yönetim yazılımıdır. Bu açık kaynaklı yazılım, birçok özelliği ve sezgisel Interface nedeniyle bitcoin kullanıcıları tarafından takdir edilmektedir.


Sparrow'yı kullanmanın iki yolu vardır:




- Özel anahtarlarınızın bilgisayarınızda depolandığı bir Hot Wallet gibi.
- Özel anahtarların Hardware Wallet'da tutulduğu bir Cold Wallet yöneticisi olarak. Bu modda, Sparrow yalnızca genel Wallet bilgilerini manipüle eder, fonları izler, adresler oluşturur ve işlemler oluşturur, ancak bu işlemleri geçerli kılmak için Hardware Wallet imzası gereklidir. Bu nedenle Ledger Live veya Trezor Suite gibi uygulamaların yerini alabilir.


Sparrow tek imzalı ve çok imzalı cüzdanları destekler ve birden fazla cüzdanın akıcı bir şekilde yönetilmesini sağlar. Örneğin, aynı anda bir Wallet'yı bir Ledger'e, diğerini bir Trezor'a bağlı olarak kontrol edebilir ve ayrıca bir Hot Wallet'ya sahip olabilirsiniz.


Yazılım ayrıca gelişmiş Coin kontrol özellikleri sunarak gizliliğinizi optimize etmek için işlemlerinizde hangi UTXO'ların kullanılacağını tam olarak seçmenize olanak tanır.


Bağlantı açısından Sparrow, bir Electrum Sunucusu aracılığıyla uzaktan veya Bitcoin core ile kendi Bitcoin düğümünüze bağlanmanıza izin verir. Henüz kendi düğümünüz yoksa, herkese açık bir düğüm kullanmak da mümkündür. Uzak bağlantılar Tor üzerinden yapılır.


## Sparrow wallet'yi kurun


Resmi Sparrow wallet indirme sayfasına] (https://sparrowwallet.com/download/) gidin ve işletim sisteminize karşılık gelen yazılım sürümünü seçin.


![Image](assets/fr/01.webp)


Yüklemeden önce yazılımın bütünlüğünü ve gerçekliğini kontrol etmek önemlidir. Bunu nasıl yapacağınızı bilmiyorsanız, burada tam bir öğretici bulacaksınız:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow kurulduktan sonra, ilk açıklayıcı ekranları atlayabilir ve doğrudan bağlantı yönetimi ekranına gidebilirsiniz.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Bitcoin ağına bağlanma


Bitcoin ağı ile etkileşime geçmek ve işlemlerinizi yayınlamak için Sparrow'nin bir Bitcoin düğümüne bağlanması gerekir. Bu bağlantıyı kurmanın üç ana yolu vardır:



- 🟡 Genel bir düğüm kullanmak, yani bu tür bağlantılara izin veren üçüncü taraf bir düğüme bağlanmak. Kendi Bitcoin düğümünüz yoksa, bu seçenek Sparrow'u hızlı bir şekilde kullanmaya başlamanızı sağlar. Ancak, bağlandığınız düğüm tüm işlemlerinizi görecektir ve bu da gizliliğinizi tehlikeye atabilir. Anahtarlarınız üzerinde kontrol sahibi olmak önemlidir, ancak kendi düğümünüze sahip olmak daha da iyidir. Bu nedenle bu seçeneği yalnızca yeni başlıyorsanız ve gizliliğinize yönelik risklerin farkındaysanız kullanın.
- 🟢 Bir Bitcoin core düğümüne bağlanma. Kendi Bitcoin core düğümünüz varsa, Bitcoin core aynı makinede kuruluysa yerel olarak veya uzaktan Sparrow wallet'a bağlayabilirsiniz.
- 🔵 Bir Electrum sunucusu üzerinden bağlantı. Bitcoin düğümünüz, Umbrel veya Start9 gibi kutu içinde düğüm çözümlerinde olduğu gibi Electrs ile donatılmışsa, Sparrow'ten uzaktan bağlanabilirsiniz.


**Üçüncü bir tarafa güvenme ihtiyacını azaltmak ve gizliliğinizi optimize etmek için kendi düğümünüzde Electrs veya Bitcoin core üzerinden bir bağlantı kullanmanız tercih edilir**


### Genel bir düğüme bağlanın 🟡


Genel bir düğüme bağlanmak çok basittir. "*Public Server*" sekmesine tıklayın.


![Image](assets/fr/03.webp)


Açılır listeden bir düğüm seçin.


![Image](assets/fr/04.webp)


Ardından "*Test Bağlantısı*" üzerine tıklayın.


![Image](assets/fr/05.webp)


Bağlandıktan sonra Sparrow wallet, genel bir düğüme bağlı olduğunuzu belirtmek için Interface'nın sağ alt köşesinde sarı bir tik işareti gösterecektir.


![Image](assets/fr/06.webp)


### Bir Bitcoin core'ye bağlanma 🟢


Bir Bitcoin düğümüne bağlanmanın ikinci yöntemi Sparrow'ı bir Bitcoin core'e bağlamaktır. Bitcoin core aynı makinede kuruluysa, kimlik doğrulama çerez dosyası aracılığıyla yapılacaktır. Bitcoin core uzak bir makinede ise, `Bitcoin.conf` dosyasında tanımlanan şifreyi kullanmanız gerekecektir.


Bir pruned Bitcoin core düğümü kullanırsanız, yerel olarak depolanan bloklardan önceki işlemleri içeren bir Wallet'ü geri yükleyemeyeceğinizi lütfen unutmayın. Ancak, Sparrow üzerinde oluşturulan yeni bir Wallet için bu bir sorun olmayacaktır: yeni işlemleriniz bir pruned düğümüyle bile görünür olacaktır.


Bir Bitcoin core düğümünü yapılandırmak için, işletim sisteminize bağlı olarak aşağıdaki eğitimlerden birine başvurabilirsiniz:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Sparrow'de "*Bitcoin core*" sekmesine gidin.


![Image](assets/fr/07.webp)


**Bitcoin core yerel ile:**


Bilgisayarınızda Bitcoin core yüklüyse, yazılım dosyaları arasında `Bitcoin.conf` dosyasını bulun. Eğer bu dosya mevcut değilse, oluşturabilirsiniz. Bir metin editörü ile açın ve aşağıdaki satırı ekleyin:


```ini
server=1
```


Ardından değişikliklerinizi kaydedin.


Bunu Bitcoin-QT'nin Interface grafiği üzerinden "*Ayarlar*" kısmına giderek de yapabilirsiniz > "*Seçenekler...*" ve "*RPC sunucusunu etkinleştir*" seçeneğini etkinleştirin.


Bu değişiklikleri yaptıktan sonra yazılımı yeniden başlatmayı unutmayın.


![Image](assets/fr/08.webp)


Ardından Sparrow wallet'e dönün ve işletim sisteminize bağlı olarak genellikle `Bitcoin.conf` ile aynı klasörde bulunan çerez dosyanızın yolunu girin:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


Diğer parametreleri varsayılan olarak bırakın, URL `127.0.0.1` ve port `8332`, ardından "*Test Bağlantısı*" üzerine tıklayın.


![Image](assets/fr/10.webp)


Bağlantı kurulmuştur. Bir Bitcoin core düğümüne bağlı olduğunuzu belirtmek için sağ alt köşede bir Green işareti görünecektir.


![Image](assets/fr/11.webp)


**Bitcoin core uzaktan kumanda ile:**


Bitcoin core aynı ağa bağlı başka bir makineye kuruluysa, önce yazılım dosyaları arasında `Bitcoin.conf` dosyasını bulun. Eğer bu dosya henüz mevcut değilse, oluşturabilirsiniz. Bu dosyayı bir metin editörü ile açın ve aşağıdaki satırı ekleyin:


```ini
server=1
```


Dosyayı düzenledikten sonra, işletim sisteminiz için uygun klasöre kaydettiğinizden emin olun:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

Bu işlem Bitcoin-QT Interface grafiksel Interface üzerinden de gerçekleştirilebilir. "*Ayarlar*" menüsüne gidin, ardından "*Seçenekler...*" ve ilgili kutuyu işaretleyerek "*RPC sunucusunu etkinleştir*" seçeneğini etkinleştirin. Eğer `Bitcoin.conf` dosyası mevcut değilse, "*Open Configuration File*" seçeneğine tıklayarak doğrudan bu Interface'den oluşturabilirsiniz.


![Image](assets/fr/12.webp)


Yerel ağınızda Bitcoin core'ü barındıran makinenin IP Address'ini bulun. Bunu yapmak için [Angry IP Scanner] (https://angryip.org/) gibi bir araç kullanabilirsiniz. Tartışma adına, düğümünüzün IP Address'inin `192.168.1.18` olduğunu varsayalım.


Bitcoin.conf` dosyasına aşağıdaki satırları ekleyin ve `rpcbind=192.168.1.18` ayarını düğümünüzün IP Address'sı ile eşleşecek şekilde yapın.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


Bitcoin.conf` dosyasına uzak bağlantılar için bir kullanıcı adı ve parola ekleyin. Kullanıcı adınızı `loic` ve parolanızı `my_password` olarak değiştirdiğinizden emin olun:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


Dosyayı değiştirip kaydettikten sonra Bitcoin-QT yazılımını yeniden başlatın.


Artık Sparrow wallet'e geri dönebilirsiniz. "*Kullanıcı/Şifre*" sekmesine gidin. Bitcoin.conf` dosyasında yapılandırdığınız kullanıcı adı ve şifreyi girin. Diğer parametreleri varsayılan olarak bırakın, yani URL `127.0.0.1` ve port `8332`. Ardından "*Test Bağlantısı*" üzerine tıklayın.


![Image](assets/fr/15.webp)


Bağlantı kurulmuştur. Bir Bitcoin core düğümüne bağlı olduğunuzu belirtmek için sağ alt köşede bir Green işareti görünecektir.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### Bir Electrum sunucusuna bağlanma 🔵


Bağlanmak için son seçenek ise uzak bir Electrum sunucusu kullanmaktır. Bu yöntem, başka bir cihazdan Tor aracılığıyla node'unuza bağlanmanızı sağlar ve Sparrow'teki cüzdanlarınıza daha hızlı göz atmak için bir indeksleyiciden yararlanır. Özellikle Umbrel veya Start9 gibi tek bir tıklamayla Electrum yüklemenize olanak tanıyan bir node-in-a-box çözümünüz varsa uygundur.


Bunu yapmak için, Electrum sunucunuzun Tor `.onion' Address'ini edinin. Örneğin Umbrel ile bunu Electrs uygulamasında bulabilirsiniz.


![Image](assets/fr/17.webp)


Sparrow wallet'da "*Özel Elektrum*" sekmesine erişin.


![Image](assets/fr/18.webp)


Sağlanan alana Tor Address ayarınızı girin. Diğer ayarlar varsayılan olarak kalabilir. Ardından "*Bağlantıyı Test Et*" seçeneğine tıklayın.


![Image](assets/fr/19.webp)


Bağlantı onaylandı. Bu pencereyi kapatırsanız, sağ alt köşede bir Electrum sunucusuna bağlı olduğunuzu gösteren mavi bir tik işareti görünecektir.


![Image](assets/fr/20.webp)


## Bir Hot Wallet oluşturun


Artık Sparrow wallet, Bitcoin ağıyla iletişim kuracak şekilde yapılandırıldığına göre, ilk Wallet'ünüzü oluşturmaya hazırsınız. Bu bölüm size bir Hot Wallet, yani özel anahtarları bilgisayarınızda depolanan bir Wallet oluşturma konusunda rehberlik edecektir. Bilgisayarınız internete bağlı karmaşık bir makine olduğundan, çok geniş bir saldırı yüzeyi sunar. Sonuç olarak, bir Hot Wallet yalnızca sınırlı miktarda bitcoin için kullanılmalıdır. Daha büyük miktarları saklamak için Hardware Wallet ile güvenli bir Wallet tercih edin. Eğer aradığınız şey buysa, bir sonraki bölüme geçebilirsiniz.


Bir Hot Wallet oluşturmak için, Sparrow wallet ana ekranından "*Dosya*" sekmesine ve ardından "*Yeni Wallet*"ya tıklayın.


![Image](assets/fr/21.webp)


Wallet'iniz için bir ad girin ve "*Wallet Oluştur*" düğmesine tıklayın.


![Image](assets/fr/22.webp)


Interface'un üst kısmında "*Tek İmza*" veya "*Çoklu İmza*" oluşturmayı seçebilirsiniz Wallet. Hemen aşağıda, UTXO'larınızı kilitlemek için komut dosyası türünü seçin. En son standardı kullanmanızı tavsiye ederim: "*Taproot (P2TR)*".


![Image](assets/fr/23.webp)


Ardından "*Yeni veya İçe Aktarılmış Software Wallet*" üzerine tıklayın.


![Image](assets/fr/24.webp)


Neredeyse tüm Bitcoin Wallet yazılımları tarafından desteklendiği için BIP39 standardını seçin. Ardından, kurtarma ifadenizin uzunluğunu seçin. Şu anda, her ikisi de benzer güvenlik sunduğundan 12 kelimelik bir ifade yeterlidir, ancak 12 kelimelik ifadenin kaydedilmesi daha kolaydır.


![Image](assets/fr/25.webp)


Wallet'inizin Mnemonic ifadesini generate yapmak için "*generate Yeni*" düğmesine tıklayın. Bu ifade tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herkes, bilgisayarınıza fiziksel erişimi olmasa bile fonlarınızı çalabilir.


12 kelimelik ifade, bilgisayarınızın kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir.


Kağıda yazabilir veya daha fazla güvenlik için yangından, selden veya çökmeden korumak amacıyla paslanmaz çelik üzerine kazıyabilirsiniz. Mnemonic'unuz için ortam seçimi güvenlik stratejinize bağlı olacaktır, ancak Sparrow'ü orta miktarda içeren Wallet'i sıcak bir harcama olarak kullanıyorsanız, kağıt yeterli olacaktır.


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**Açıkçası, bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu Wallet örneği sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**


"*passphrase* Kullan" kutusuna tıklayarak bir passphrase BIP39 eklemeyi de seçebilirsiniz. Uyarı: passphrase kullanmak çok faydalı olabilir, ancak nasıl çalıştığını anlamazsanız çok riskli olabilir. Bu yüzden konuyla ilgili bu kısa teorik makaleyi okumanızı şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Mnemonic ve tüm passphrase'larınızı fiziksel bir ortama kaydettikten sonra "*Yedeklemeyi Onayla*" seçeneğine tıklayın.


![Image](assets/fr/27.webp)


Doğru kaydedildiklerini onaylamak için 12 kelimenizi tekrar girin ve ardından "*Anahtar Deposu Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/28.webp)


Ardından Wallet anahtarlarınızı Mnemonic ifadesinden generate'a aktarmak için "*Anahtar Deposunu Aktar*" seçeneğine tıklayın.


![Image](assets/fr/29.webp)


Wallet oluşturma işlemini tamamlamak için "*Uygula*" üzerine tıklayın.


![Image](assets/fr/30.webp)


Sparrow wallet'nize erişimi güvence altına almak için güçlü bir parola belirleyin. Bu parolayı bir parola yöneticisinde saklamak iyi bir fikirdir, böylece unutmazsınız. Bu parolanın anahtarlarınızın türetilmesinde hiçbir rol oynamadığını unutmayın. Yalnızca Sparrow wallet aracılığıyla Wallet'ünüze erişmek için kullanılır. Dolayısıyla, bu parola olmasa bile, Mnemonic ifadeniz herhangi bir BIP39 uyumlu uygulamadan bitcoinlerinize erişmek için yeterli olacaktır.


![Image](assets/fr/31.webp)


Hot Wallet'niz artık oluşturulmuştur. Hardware Wallet'i Sparrow ile kullanmayı planlamıyorsanız bu eğitimin *Bitcoinlerin Alınması* bölümüne geçebilirsiniz.


## Bir Cold Wallet'u Yönetme


Sparrow wallet'yi kullanmanın ikinci yolu, onu bir Hardware Wallet ile bir Wallet yöneticisi olarak kurmaktır. Bu yapılandırmada, Bitcoin Wallet'inizin özel anahtarları yalnızca Hardware Wallet'de kalırken, Sparrow yalnızca genel bilgilere erişir. Bu yaklaşım, yukarıda tartışılan Hot cüzdanlarından daha yüksek bir güvenlik seviyesi sunar, çünkü özel anahtarlar, genellikle güvenli bir çipe sahip, internete bağlı olmayan ve bu nedenle geleneksel bir bilgisayardan çok daha küçük bir saldırı yüzeyi sunan özel bir cihazda tutulur.


Hardware Wallet'nizi Sparrow'e bağlamanın iki ana yolu vardır:




- Kablo ile, genellikle Trezor Safe 3 veya Ledger Nano S Plus gibi giriş seviyesi modellerle kullanılır;
- Air-Gap modunda, yani doğrudan kablolu bağlantı olmadan, bir MicroSD kart veya QR kodu Exchange aracılığıyla.


Sparrow tüm bu iletişim yöntemlerini destekler ve piyasadaki çoğu donanım cüzdanı ile uyumludur.


Bu eğitim için kablolu bir Ledger Nano S kullanacağım, ancak prosedür Hava Boşluğu modunda da benzerdir. Hardware Wallet'nize özgü ayrıntıları Plan ₿ Network'e özel eğitimde bulabilirsiniz.


Başlamadan önce, Wallet'nın Hardware Wallet'inizde zaten yapılandırılmış olduğundan emin olun. Kablolu bağlantı kullanıyorsanız, kabloyla bilgisayarınıza bağlayın.


"*Anahtar Deposu*"nu (Wallet'i yönetmek için gereken genel bilgiler) Sparrow wallet'ye aktarmak için, "*Dosya*" sekmesine ve ardından "*Yeni Wallet*"e tıklayın.


![Image](assets/fr/32.webp)


Wallet'ınıza bir isim verin ve "*Wallet* Oluştur "a tıklayın. Daha sonra kolayca tanımlayabilmek için Hardware Wallet'unuzun adını girmenizi tavsiye ederim.


![Image](assets/fr/33.webp)


Interface'in üst kısmında, "*Tek İmza*" veya "*Çoklu İmza*" arasında seçim yapın Wallet. Örneğimiz için, bir single-sig Wallet yapılandıracağız.


Hemen aşağıda, UTXO'larınızı kilitlemek için komut dosyası türünü seçin. Eğer Hardware Wallet destekliyorsa, "*Taproot (P2TR)*" seçmenizi öneririm.


![Image](assets/fr/34.webp)


Ardından, prosedür bağlantı yönteminize göre farklılık gösterir. Hava Aralıklı bir yöntem kullanıyorsanız, "*Hava Aralıklı Hardware Wallet*" seçeneğini seçin. Ardından cihazınıza özel talimatları izleyin.


![Image](assets/fr/35.webp)


Benim durumumda olduğu gibi kablo bağlantısı kullanıyorsanız, "*Bağlı Hardware Wallet*" seçeneğini seçin.


![Image](assets/fr/36.webp)


Sparrow'un cihazınızı algılaması için "*Tarama*" üzerine tıklayın. Cihazın takılı ve kilidinin açık olduğundan emin olun. Ledger gibi bazı modellerde, algılamayı etkinleştirmek için "*Bitcoin*" uygulamasını açmanız gerekecektir.


![Image](assets/fr/37.webp)


"*Anahtar Deposunu Aktar*" öğesini seçin.


![Image](assets/fr/38.webp)


Wallet oluşturma işlemini tamamlamak için "*Uygula*" üzerine tıklayın.


![Image](assets/fr/39.webp)


Sparrow wallet'nize erişimi güvence altına almak için güçlü bir parola belirleyin. Bu parola genel anahtarlarınızı, adreslerinizi ve işlem geçmişinizi koruyacaktır. Bu parolayı bir parola yöneticisine kaydetmenizi öneririz. Bu parolanın anahtarlarınızın türetilmesinde hiçbir rol oynamadığını unutmayın. Bu şifre olmasa bile, BIP39 uyumlu herhangi bir yazılım aracılığıyla Mnemonic'ünüzle bitcoinlerinize erişimi geri kazanabilirsiniz.


![Image](assets/fr/40.webp)


Wallet yönetiminiz artık Sparrow üzerinde yapılandırılmıştır.


![Image](assets/fr/41.webp)


## Bitcoin alma


Artık Wallet'niz Sparrow'ya kurulduğuna göre bitcoin alabilirsiniz. "*Alma*" menüsüne erişmeniz yeterlidir.


![Image](assets/fr/42.webp)


Sparrow, Wallet'ınızda kullanılmayan ilk Address'i gösterecektir. Gelecekte bu satoshilerin kaynağını size hatırlatması için bu Address'e bir "*Etiket*" ekleyebilirsiniz.


![Image](assets/fr/43.webp)


Bir Hot Wallet kullanıyorsanız, görüntülenen Address kopyalanarak veya ilgili QR kodu taranarak hemen kullanılabilir.


Bir Hardware Wallet kullanıyorsanız, kullanmadan önce cihaz ekranında Address'i kontrol etmeniz çok önemlidir. Kablolu cihazlar için, Hardware Wallet'ünüzü bağlayın ve kilidini açın, ardından Sparrow'da "*Address'i Göster*" seçeneğine tıklayın. Hardware Wallet'ünüzde görüntülenen Address'in Sparrow'da gösterilenle eşleştiğinden emin olun.


![Image](assets/fr/44.webp)


Hardware Wallet Air-Gap kullanıcıları için Address doğrulaması cihaz modeline göre değişir. Kesin talimatlar için özel Plan ₿ Network eğitimine bakın.


İşlem ödeyici tarafından yayınlandıktan sonra, "*İşlemler*" sekmesinde göründüğünü göreceksiniz. txid gibi daha fazla ayrıntı için üzerine tıklayabilirsiniz.


![Image](assets/fr/45.webp)


"*Adresler*" sekmesinde, tüm gelen kutusu adreslerinizin bir listesini bulacaksınız. Daha önce kullanılıp kullanılmadıklarını ve bir etiket eklenip eklenmediğini görebilirsiniz. *Receive*" adresleri, "*Receive*" seçeneğine tıkladığınızda Sparrow'nin gösterdiği adreslerdir ve gelen ödemeler için tasarlanmıştır. "*Değiştir*" adresleri işlemlerinizde Exchange için, yani UTXO'larınızın kullanılmayan kısmını girdilerde geri kazanmak için kullanılır.


![Image](assets/fr/46.webp)


"*UTXOs*" sekmesi size tüm UTXO'larınızı, yani elinizdeki Bitcoin parçalarını gösterir. Her bir UTXO'ün miktarını ve ilgili etiketi görebilirsiniz.


![Image](assets/fr/47.webp)


## Bitcoin gönder


Artık Wallet'inizde birkaç satoshiniz olduğuna göre, biraz gönderme seçeneğiniz de var. Bunu yapmanın birkaç yolu olmasına rağmen, harcadığınız jetonlar üzerinde daha hassas kontrol için (*Coin kontrolü*) doğrudan "*Gönder*" menüsüne gitmek yerine "*UTXO'lar*" menüsünü kullanmanızı tavsiye ederim (ancak yeni başlayan biriyseniz ikincisi yeterli olabilir).


![Image](assets/fr/48.webp)


Bu işlem için girdi olarak kullanmak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. Bu yaklaşım, ödemelerinizin gizliliğini optimize etmek için UTXO'larınız arasından harcamalarınıza ve alındıklarında uygulanan etiketlere göre en uygun kaynakları seçmenize olanak tanır. Seçilen UTXO'ların toplamının göndermek istediğiniz tutardan büyük olduğundan emin olun.


![Image](assets/fr/49.webp)


Alıcının Address numarasını "*Pay to*" alanına girin. Kamera simgesine tıklayarak Address'yi web kameranızla da tarayabilirsiniz. "*+Ekle*" düğmesi tek bir işlemde birden fazla adrese ödeme yapmanızı sağlar.


![Image](assets/fr/50.webp)


İşleminize amacını size hatırlatacak bir etiket ekleyin. Bu etiket aynı zamanda nihai Exchange ile de ilişkilendirilecektir.


![Image](assets/fr/51.webp)


Bu Address'a gönderilecek tutarı girin.


![Image](assets/fr/52.webp)


Ücret oranını mevcut piyasa koşullarına göre ayarlayın. Bunu mutlak bir ücret değeri girerek veya ücret oranını kaydırıcı ile ayarlayarak yapabilirsiniz.


![Image](assets/fr/53.webp)


Interface'in alt kısmında "*Efficiency*" ve "*Privacy*" arasında seçim yapabilirsiniz. Benim durumumda "*Gizlilik*" seçeneği mevcut değil, çünkü bu Wallet'de yalnızca bir UTXO var. "*Efficiency*" klasik bir işleme karşılık gelirken, "*Privacy*" Stonewall tipi bir işlemdir, mini bir CoinJoin simüle ederek gizliliğinizi güçlendiren bir işlem yapısıdır, bu da zincir analizini daha karmaşık hale getirir.


![Image](assets/fr/54.webp)


Sparrow girdilerinizi, çıktılarınızı ve işlem ücretlerinizi gösteren bir özet diyagram görüntüler (bu diyagramın önerdiğinin aksine ücretlerin aslında bir çıktı olmadığını unutmayın). Her şeyden memnunsanız, "*İşlem Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/55.webp)


Bu sizi işleminizin Elements ayrıntılarını içeren bir sayfaya götürür. Tüm bilgilerin doğru olup olmadığını kontrol edin ve ardından "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![Image](assets/fr/56.webp)


Varsayılan Sighash'ı korumak önemlidir. Nedenini anlamak için, Sighash hakkında bilmeniz gereken her şeyi açıkladığım bu eğitim kursuna bir göz atın:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Bir sonraki ekranda, seçenekler kullandığınız Wallet türüne göre değişir:




- Bir Hardware Wallet Air-Gap için, cihazınızla imzalayabileceğiniz bir PSBT görüntülemek için "*Show QR*" seçeneğine tıklayın, ardından imzalı PSBT'u "*Scan QR*" kullanarak Sparrow'e yükleyin. "*İşlemi Kaydet*" seçeneği de benzer şekilde çalışır, ancak microSD'deki alışverişler için geçerlidir;
- Hot Wallet için "*İmzala*" düğmesine tıklamanız ve imzalamak için Wallet şifresini girmeniz yeterlidir;
- Kablolu bir Hardware Wallet için, imzasız işlemi cihazınıza göndermek üzere "*İmzala*" seçeneğine de tıklayın.


![Image](assets/fr/57.webp)


Hardware Wallet'ünüzde alıcının Address'ünü, gönderilen miktarı ve ücretleri kontrol edin. Her şey doğruysa, imzalamaya devam edin.


İşlem imzalandıktan sonra, Sparrow'da yeniden görünecek ve daha sonra bir bloğa dahil edilmek üzere Bitcoin ağında yayınlanmaya hazır olacaktır. Her şey doğruysa, "*İşlemi Yayınla*" düğmesine tıklayın.


![Image](assets/fr/58.webp)


İşleminiz şu anda yayındadır ve onay beklemektedir.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Sparrow'de cüzdanları yönetme ve yapılandırma


"*Ayarlar*" sekmesinde, Wallet'iniz hakkında ayrıntılı bilgi bulabilirsiniz, örneğin :



- Portföy türü (single-sig veya multi-sig) ;
- Kullanılan senaryo türü ;
- Wallet'e atadığınız ad;
- Ana anahtar baskısı;
- Baypas yolu ;
- Hesabın genişletilmiş genel anahtarı.


![Image](assets/fr/60.webp)


"*Dışa Aktar*" düğmesi, Wallet bilgilerinizi dışa aktarmanıza olanak tanır, böylece Sparrow'de ayarlanan bilgileri korurken diğer yazılımlarda kullanabilirsiniz.


"*Hesap Ekle*" düğmesi Wallet'ünüze ek bir hesap eklemenizi sağlar. Bir hesap, ayrı bir gelen kutusu adresleri kümesine karşılık gelir. Bu özellik, örneğin, tek bir Mnemonic ifadesiyle kişisel ve ticari bir hesabı ayırmak istiyorsanız yararlı olabilir.


"*Gelişmiş*" düğmesi, Sparrow'nın Address aramasını özelleştirme ve Wallet şifresini değiştirme gibi gelişmiş ayarlara erişim sağlar.


![Image](assets/fr/61.webp)


Sparrow wallet'i kapattığınızda, Wallet'unuz otomatik olarak kilitlenir. Yazılımı bir sonraki açışınızda, bir pencere sizden Wallet'unuzun kilidini şifresiyle açmanızı isteyecektir.


![Image](assets/fr/62.webp)


Bu pencere açılmazsa veya Sparrow üzerinde başka bir Wallet açmak isterseniz, "*Dosya*" sekmesine tıklayın ve "*Wallet* Aç" seçeneğini seçin.


![Image](assets/fr/63.webp)


Bu, Dosya Yöneticinizi Sparrow'nin cüzdanlarınızı depoladığı klasöre açacaktır. Açmak istediğiniz Wallet'ü seçin ve kilidini açmak için şifreyi girin.


![Image](assets/fr/64.webp)


"*Ayarlar*" altındaki "*Dosya*" menüsünde, önceki bölümlerde incelenmiş olan Bitcoin ağ bağlantısı parametrelerini bulacaksınız. Ayrıca kullanılan birim, dönüşümler için fiat para birimi ve bilgi kaynakları gibi çeşitli parametreleri de ayarlayabilirsiniz.


![Image](assets/fr/65.webp)


"*Görünüm*" sekmesi, özelleştirme seçenekleri ve Wallet'iniz için işlem aramasını yenileyen "*Wallet'i Yenile*" gibi bazı yararlı komutlara erişim sunar.


![Image](assets/fr/66.webp)


"*Araçlar*" sekmesi, aşağıdakiler de dahil olmak üzere çeşitli gelişmiş araçları bir araya getirir:



- "*Mesajı İmzala/Doğrula*", alıcı Address'ya sahip olduğunuzu kanıtlamanızı veya bir imzayı doğrulamanızı sağlar.
- "*Birçoğuna Gönder*", toplu harcamalar için uygun olan, aynı anda birden fazla alıcı adresine işlem gerçekleştirmek için basitleştirilmiş bir Interface sunar.
- "*Sweep Private Key*" basit bir özel anahtarla güvence altına alınmış bitcoinleri almanızı ve Sparrow wallet'inize aktarmanızı sağlar. Bu, özellikle HD cüzdanlar döneminden önce, 2010'ların başlarına kadar uzanan bitcoinleri olanlar için yararlı olabilir.
- "İndirmeyi Doğrula", cihazınıza yüklemeden önce indirilen yazılımın bütünlüğünü ve gerçekliğini doğrular.
- "*Restart In*" Testnet veya Signet ağlarındaki cüzdanlarınıza geçiş yapmanızı sağlar. Bu, gerçek değeri olmayan madeni paralarla test ağlarına erişmek istiyorsanız yararlı olabilir.


![Image](assets/fr/67.webp)


Artık Sparrow wallet cüzdanlarınızı günlük olarak yönetmek için mükemmel bir araç olan Bitcoin yazılımı hakkında her şeyi biliyorsunuz.


Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız çok minnettar olurum. Sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Hardware Wallet COLDCARD Q'nun Sparrow wallet ile nasıl yapılandırılacağını açıkladığım bu diğer öğreticiyi de tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3