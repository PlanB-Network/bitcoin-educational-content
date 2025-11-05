---
name: Spectre Masaüstü
description: Çoklu imzalı Bitcoin portföylerinizi kendi düğümünüzle tam egemenlik içinde yönetin
---

![cover](assets/cover.webp)



Spectre Desktop, Cryptoadvance tarafından 2019'dan beri geliştirilen, donanım cüzdanlarınız (Ledger, Trezor, Coldcard, BitBox02, Passport, vb.) ve kendi Bitcoin altyapınız (Bitcoin Core node veya Electrum sunucusu) ile Bitcoin cüzdanlarının yönetimini kolaylaştıran açık kaynaklı bir uygulamadır (MIT lisansı). Uygulama, özellikle çoklu imza yapılandırmalarında mükemmeldir ve imzalama gücünü birkaç bağımsız donanım cüzdanı arasında dağıtarak büyük meblağları güvence altına almanızı sağlar.



**Bu eğitimde aşağıdakileri nasıl yapacağınızı öğreneceksiniz:**




- Spectre Desktop'ı bilgisayarınıza kurun ve yapılandırın (Windows, macOS veya Linux)
- Spectre'yi bir Electrum sunucusuna bağlayın (bu örnekte Umbrel kullanacağız)
- wallet donanımı ile basit bir wallet oluşturma (Coldcard)
- Tam egemenlikle bitcoin alın ve gönderin
- Birkaç donanım cüzdanı ile 2'ye 3 çoklu imza wallet kurulumu
- Spectre'yi bir Umbrel sunucusuna yükleme (gelişmiş bonus)



Tüm işlemleriniz, harici sunuculara herhangi bir bilgi aktarılmadan kendi altyapınız üzerinden yerel olarak doğrulanacak, gizliliğinizi ve finansal egemenliğinizi garanti altına alacaktır. İmzalamadan önce her zaman wallet donanım ekranınızdaki işlemleri kontrol edin.



## İndirme ve kurulum



Uygulamayı indirmek için resmi Spectre Desktop web sitesini ziyaret edin.



![Page d'accueil Specter](assets/fr/01.webp)



İndirme sayfasında, işletim sisteminize karşılık gelen sürümü seçin: macOS, Windows veya Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



İndirdikten sonra, uygulamayı işletim sisteminizin normal talimatlarına göre yükleyin. MacOS için simgeyi Uygulamalar'a sürükleyin. Windows için yükleyiciyi çalıştırın. Linux için paket talimatlarını izleyin.



## İlk yapılandırma



İlk açılışta Spectre Desktop sizden bağlantı türünüzü seçmenizi ister. Bir Electrum sunucusuna veya kendi Bitcoin Çekirdek düğümünüze bağlanabilirsiniz.



![Choix du type de connexion](assets/fr/03.webp)



Bu örnekte, Umbrel üzerinde çalışan bir Electrum sunucusuna bağlantı kullanacağız.



Daha fazla bilgi için lütfen Umbrel eğitimimize bakın:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bu seçenek Bitcoin Core'dan daha hızlı senkronizasyon sunar. Tercih ederseniz, "Bitcoin Core" seçeneğini seçebilir ve bağlantıyı yerel düğümünüze yapılandırabilirsiniz. Seçiminiz ne olursa olsun aşağıdaki adımlar aynı kalır.



"Electrum Bağlantısı "nı seçin ve ardından kendi Electrum sunucunuzu yapılandırmak için "Kendiminkini gir "i seçin.



![Configuration Electrum](assets/fr/04.webp)



Electrum sunucunuzun adresini girin. Umbrel örneğimizde, adres `umbrel.local` ve port `50001` olacaktır. Bağlantıyı kurmak için "Bağlan "a tıklayın.



Bağlandıktan sonra, başlamanız için bir kontrol listesi içeren karşılama ekranı görünür. Şimdi donanım cüzdanlarınızı eklemeniz gerekiyor.



![Écran d'accueil](assets/fr/05.webp)



## wallet donanımının eklenmesi



Sol taraftaki menüde, wallet donanımınızı eklemek için "Cihaz ekle "ye tıklayın.



Spectre Desktop çok sayıda donanım cüzdanını destekler: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault ve diğerleri.



Daha fazla bilgi edinmek isterseniz, donanım wallet eğitimlerimize göz atın.



![Sélection du type de hardware wallet](assets/fr/06.webp)



wallet donanımınızı seçin. Bu örnekte, bir Coldcard MK4 kullanıyoruz.



Aşağıda bu wallet donanımı için öğreticimizi bulacaksınız:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcard için, açık anahtarları wallet donanımından bir USB bağlantısı veya bir microSD kart aracılığıyla dışa aktarmanız gerekir.



![Import des clés du Coldcard](assets/fr/07.webp)



Anahtarları Coldcard'ınızdan dışa aktarmak için görüntülenen talimatları izleyin. wallet donanımınıza bir isim verin (burada "MK4 Tuto"). Anahtarlar içe aktarıldıktan sonra, tek bir anahtarla bir wallet oluşturabilir veya çoklu imzalı bir wallet için başka donanım cüzdanları ekleyebilirsiniz.



![Dispositif ajouté](assets/fr/08.webp)



## Portföy oluşturma



wallet donanımınızı ekledikten sonra, tek imzalı bir wallet oluşturmak için "Tek anahtarlı wallet oluştur" seçeneğine tıklayın.



Portföyünüze bir isim verin (örneğin "Wallet for tuto") ve adres türünü seçin. İşlem maliyetlerini optimize eden yerel bech32 adreslerini kullanmak için "Segwit "i seçin.



![Configuration du portefeuille](assets/fr/09.webp)



Portföyünüz oluşturulduktan sonra Spectre, portföyünüzü geri yüklemek için gereken tüm genel bilgileri (tanımlayıcılar, genişletilmiş genel anahtarlar) içeren bir yedek PDF dosyası kaydetmeyi teklif eder. Bu dosya özel anahtarlarınızı içermez.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Bitcoin alma



Bitcoin almak için sol taraftaki menüden wallet'ünüzü seçin ve ardından "Al" sekmesine tıklayın.



Spectre otomatik olarak bir QR kodu ile yeni bir alım adresi oluşturur.



![Génération d'une adresse de réception](assets/fr/11.webp)



Adresi kopyalayabilir veya QR kodunu tarayabilirsiniz. Adresi birine vermeden önce her zaman wallet donanım ekranınızdan kontrol edin.



## Geçmişi ve adresleri görüntüleyin



Bitcoin aldıktan sonra, işlemlerinizi "İşlemler" sekmesinden görüntüleyebilirsiniz.



![Historique des transactions](assets/fr/12.webp)



"Adresler" sekmesi, portföyünüz tarafından oluşturulan tüm adresleri, kullanım durumları ve ilişkili tutarlarıyla birlikte görüntülemenizi sağlar.



![Liste des adresses](assets/fr/13.webp)



## Bitcoin gönder



Bitcoin göndermek için "Gönder" sekmesine tıklayın. Alıcının adresini, gönderilecek miktarı girin ve UTXO'ları (coin kontrolü) manuel olarak seçmek istiyorsanız gelişmiş seçenekleri kontrol edin.



![Création d'une transaction](assets/fr/14.webp)



İşlemi oluşturmak için "İmzasız İşlem Oluştur" seçeneğine tıklayın. Spectre daha sonra sizden işlemi wallet donanımınızla imzalamanızı isteyecektir.



![Signature de la transaction](assets/fr/15.webp)



Coldcard kullanıyorsanız, USB üzerinden veya microSD kartı (hava boşluklu) kullanarak imzalama seçeneğiniz olacaktır. Hedef adresi ve tutarı dikkatlice kontrol ederek wallet donanım ekranınızda işlemi onaylayın.



İşlem imzalandıktan sonra, bunu Bitcoin ağında yayınlayabilirsiniz.



![Options de diffusion](assets/fr/16.webp)



İşlemi göndermek için "İşlemi gönder" üzerine tıklayın. Spectre işleminizin gönderildiğini onaylayacaktır ve işlemin durumunu İşlemler sekmesinden takip edebilirsiniz.



![Diffusion de la transaction](assets/fr/17.webp)



## Çoklu imza portföyü oluşturma ve kullanma



Spectre Desktop'ın en önemli özelliklerinden biri çoklu imza portföylerinin yönetimini basitleştirebilmesidir. Bir multisig wallet, bir işlemi yetkilendirmek için birkaç imza gerektirir, böylece tek hata noktasını ortadan kaldırır. Örneğin 2-on-3 yapılandırması, herhangi bir harcamayı doğrulamak için üç ayrı donanım cüzdanından iki imza gerektirir.



Bir multisig wallet oluşturmak için, "Cihaz ekle" aracılığıyla tüm imzalama donanım cüzdanlarını ekleyerek başlayın. Bu örnekte, üç farklı donanım cüzdanı kullanacağız: bir Coldcard MK4 (daha önce eklenmişti), bir Passport ve bir Ledger. Üreticilerin bu şekilde çeşitlendirilmesi, tek bir tedarik zincirine veya ürün yazılımına bağımlılıktan kaçınarak güvenliği güçlendirir.



İşte Ledger ve Passport eğitimlerinin bağlantıları:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

wallet donanımını adlandırarak (örneğin "Passport multi") ve anahtarlarını microSD kart veya QR kodu aracılığıyla içe aktararak Passport'u ekleyin. Ardından devam etmek için "Devam Et "e tıklayın.



![Ajout du Passport](assets/fr/23.webp)



Ardından USB ile bağlayarak ve Bitcoin donanımında wallet uygulamasını açarak Ledger'i ekleyin. Adlandırın (örneğin "ledger multi") ve açık anahtarlarını içe aktarmak için "USB ile Al" ve ardından "Devam Et" seçeneğine tıklayın.



![Ajout du Ledger](assets/fr/24.webp)



Üç donanım cüzdanınızı Spectre'ye kaydettikten sonra, "wallet Ekle "ye tıklayın ve çoklu imzalı bir wallet oluşturmak için "Çoklu İmza" seçeneğini seçin.



![Choix du type de wallet](assets/fr/25.webp)



Çoklu imza çekirdeğinize dahil etmek istediğiniz üç donanım cüzdanını seçin: MK4 Tuto, Passport multi ve ledger multi. Bir sonraki adıma geçmek için "Devam "a tıklayın.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Çoklu imza yapılandırmanızı seçin. Optimize edilmiş ücretlerden faydalanmak için adres türü olarak "Segwit" seçin. "İşlemleri Yetkilendirmek için Gerekli İmzalar (m of 3)" parametresi eşiği tanımlamanızı sağlar: 2'ye 3 yapılandırma için 2 imza gereklidir. Her wallet donanımı ilgili multisig anahtarını görüntüler. Oluşturmayı tamamlamak için "wallet Oluştur" üzerine tıklayın.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



"Multi tuto" çoklu imza portföyünüz artık oluşturulmuştur. Spectre, portföy tanımlayıcısını içeren yedek PDF dosyasını hemen kaydetmenizi önerir. Bu kritik dosyayı indirmek için "Yedek PDF Kaydet" üzerine tıklayın.



![Wallet multisig créé](assets/fr/28.webp)



Spectre ayrıca wallet bilgilerini QR kodu veya dosya aracılığıyla donanım cüzdanlarınızın her birine aktarmanıza olanak tanır. Bu, belirli donanım cüzdanlarının (Coldcard veya Passport gibi) multisig yapılandırmasını doğrudan belleklerinde saklamasını sağlar.



Passport için cihazınızın kilidini açın, ardından "Hesabı Yönet" > "Wallet'i Bağla" > "Spectre" > "Multisig" > "QR Kodu" bölümüne gidin, ardından Spectre tarafından oluşturulan QR kodunu tarayın. Passport'unuz daha sonra multisig yapılandırmasını doğrulamak için wallet'nizden bir alıcı adresi taramanızı isteyecektir.



MK4 için, bilgisayarınıza takın ve kilidini açın. Ardından "MK4 Tuto dosyasını kaydet" seçeneğine tıklayın ve dosyayı MK4'ünüze kaydedin. wallet donanımınızı bir dahaki sefere imzaladığınızda, MK4 multisig yapılandırmasını tamamlamak için bu dosyayı kullanacaktır.



![Export vers les hardware wallets](assets/fr/29.webp)



Bilginiz olsun, yedeklere portföyünüzün "Ayarlar" sekmesinden ve ardından "Dışa Aktar" seçeneğinden istediğiniz zaman erişebilirsiniz:



![Accès au backup PDF](assets/fr/30.webp)



Günlük kullanım basit bir wallet'e benzer: normal olarak generate alıcı adresleri. Bitcoin göndermek için "Gönder" sekmesine gidin, alıcının adresini ve tutarı girin, ardından "İmzasız İşlem Oluştur" seçeneğine tıklayın.



![Création d'une transaction multisig](assets/fr/31.webp)



Spectre bir PSBT (Partially Signed Bitcoin Transaction) oluşturur ve "2 imzanın 0'ı alındı" mesajını görüntüler. Şimdi üç donanım cüzdanınızdan en az ikisiyle imza atmalısınız. Coldcard'ınızla imzalamak için ilk wallet donanımına (örneğin "MK4 Tuto"), ardından gerekli ikinci imzayı almak için ikincisine (örneğin "Passport multi") tıklayın.



![Signature de la transaction](assets/fr/32.webp)



Gerekli 2 imzayı aldıktan sonra (arayüzde "2 imzadan 2'si alındı" ve "İşlem gönderilmeye hazır" görüntülenir), işlemi Bitcoin ağında yayınlamak için "İşlemi Gönder "e tıklayın.



![Transaction prête à être diffusée](assets/fr/33.webp)



Bu çoklu imza yaklaşımı özellikle şirketler (birkaç yöneticinin harcamaları onaylaması gerekir), aileler (çok nesilli bir mirasın korunması) veya büyük meblağları yöneten bireyler (yerel felaketlere dayanmak için donanım cüzdanlarının coğrafi dağılımı) için çok uygundur.



### Çoklu imza yedeklemelerinin kritik önemi



**Lütfen dikkat**: çoklu bir portföyü yedeklemek, tek bir portföyü yedeklemekten temelde farklıdır. Kurtarma cümleleriniz (seed cümleleri) tek başına bir multisig portföyünü geri yüklemek için yeterli değildir. Multisig portföyünüzün yapılandırma bilgilerini içeren **output descriptor**'yi (output descriptor) de yedeklemeniz gerekir.



output descriptor temel verileri içerir: her bir ortak imzalayanın genişletilmiş açık anahtarları (xpubs), imza eşiği (örneğimizde 2'ye 3), kullanılan komut dosyası türü (yerel, yuvalanmış veya eski Segwit) ve her bir wallet donanımı için bypass yolları. Bu tanımlayıcı olmadan, üç kurtarma cümlesinden ikisine sahip olsanız bile, wallet'inizi yeniden inşa edemez veya bitcoinlerinize erişemezsiniz. Tanımlayıcı, yazılımınızın açık anahtarları generate ile fonlarınıza karşılık gelen Bitcoin adreslerini nasıl birleştireceğini bilmesini sağlar.



Specter Desktop, multisig portföyünüzü oluşturduğunuzda otomatik olarak bir yedek PDF dosyası oluşturur. Bu PDF tüm tanımlayıcıyı, her bir wallet donanımının parmak izlerini ve geri yükleme için gerekli tüm genel bilgileri içerir. **Bu dosya özel anahtarlarınızı** içermez ve bu nedenle tek başına bitcoinlerinizi harcamanıza izin vermez, ancak dosyaya erişen herkesin tüm işlem geçmişinizi ve bakiyenizi görmesini sağlar.



Çoklu imza yapılandırmanızı doğru bir şekilde yedeklemek için şu prosedürü izleyin: portföyünüzü oluşturduktan sonra "Ayarlar" sekmesine tıklayın, ardından "Dışa Aktar" ve "Yedek PDF Kaydet" seçeneğini seçin. Bu PDF'nin birkaç kopyasını oluşturun: en az iki kopyasını kağıda yazdırın ve ayrıca şifrelenmiş bir dijital kopyasını saklayın. PDF'nin bir kopyasını kurtarma ifadelerinizin her biriyle birlikte coğrafi olarak ayrı yerlerde saklayın.



Uzun ömürlü olmalarını garanti altına almak için kurtarma ifadelerinizi yanmaz ve su geçirmez metal plakalar üzerine kazıyın. Bu yedeklemelerin önemini asla küçümsemeyin: bilgisayarınızdaki `~/.specter` klasörünü kaybederseniz VE tanımlayıcı yedeği olmadan donanım cüzdanlarınızdan birini kaybederseniz, 2'ye 3 yapılandırmada bile tüm fonlarınız geri alınamaz şekilde kaybolacaktır. Çoklu imza yedekliliği wallet donanımının kaybına karşı koruma sağlar, ancak yalnızca wallet'nizin tanımlayıcısını doğru şekilde yedeklediyseniz.



## Spectre Desktop'ın avantajları ve sınırlamaları



**Avantajlar**: Üçüncü taraf sunucular olmadan tam yerel doğrulama ile optimum gizlilik. Gelişmiş yapılandırmalar için çoklu imza esnekliği (kurumsal, aile, bireysel). Tam birlikte çalışabilirlik ile kapsamlı donanım wallet desteği (USB ve hava boşluklu).



**Sınırlamalar**: Gelişmiş Bitcoin kavramlarında (UTXO'lar, tanımlayıcılar, türetme yolları) önemli öğrenme eğrisi.



## En iyi uygulamalar



Kötü amaçlı yazılımlara karşı kendinizi korumak için doğrulamadan önce her zaman donanım wallet ekranınızdaki adresleri ve miktarları kontrol edin.



PDF yedeklerini tohumlarınızdan ayrı tutun. Bu genel tanımlayıcılar bir banka kasasında veya şifrelenmiş bulutta saklanabilir ve özel anahtarlarınızı açığa çıkarmadan kurtarmayı kolaylaştırır.



Portföylerinizi büyük fonlarla kullanmadan önce token tutarları üzerinde kurtarma işlemini test edin. Prosedürlerinizi doğrulamak için oluşturun, test edin, silin ve geri yükleyin.



Spectre'yi ve ürün yazılımınızı güncel tutun. Yerel felaketlere dayanmak için çoklu imza ortak imzalayıcılarınızı coğrafi olarak (ev/ofis/yakın) dağıtın. Muhasebe ve vergi iadelerini kolaylaştırmak için açıklayıcı etiketler kullanın.



## Bonus: Bir Bitcoin sunucusuna kurulum (Umbrel, RaspiBlitz, Start9)



Umbrel, RaspiBlitz, MyNode veya Start9 gibi bir Bitcoin sunucusuna sahipseniz Spectre Desktop'ı doğrudan uygulama mağazalarından yükleyebilirsiniz. Bu yaklaşım birçok önemli avantaj sunar: uygulama kendini otomatik olarak yerel Bitcoin Core düğümünüzle yapılandırır, ağınızdaki herhangi bir cihazdan bir web arayüzü aracılığıyla 7/24 erişilebilir kalır ve hatta Tor aracılığıyla uzaktan güvenli bir şekilde erişebilirsiniz. Tüm Bitcoin altyapınız tek bir özel sunucu üzerinde merkezileştirilerek yönetimi basitleştirir ve egemenliğinizi güçlendirir.



### Umbrel App Store'dan yükleme



Umbrel arayüzünüzden App Store'a gidin ve Spectre Desktop'ı arayın. Yüklemeyi başlatmak için "Yükle "ye tıklayın.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Kurulum tamamlandığında, Umbrel'inizde Spectre Desktop'ı açın. Karşılama ekranı sizden bağlantı türünüzü seçmenizi isteyecektir. Umbrel'inizde Spectre kullanıyorsanız, bağlantıyı yapılandırmak için "Ayarları güncelle "ye tıklayın.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Uzak Umbrel sunucusunda Specter kullanırken yerel bilgisayarınıza bağlı USB donanım cüzdanlarının kullanımını etkinleştirmek için "Uzak Specter USB bağlantısı "nı seçin.



![Configuration Remote Specter USB](assets/fr/20.webp)



HWI Köprüsünü yapılandırmak için görüntülenen talimatları izleyin. Cihaz köprü ayarlarına erişmeniz ve `http://umbrel.local:25441` etki alanını beyaz listeye eklemeniz gerekir. Yapılandırmayı kaydetmek için "Güncelle" üzerine tıklayın.



![HWI Bridge Settings](assets/fr/21.webp)



USB donanım cüzdanlarınızı yerel bilgisayarınızdan da kullanmak istiyorsanız, Spectre Desktop uygulamasını makinenize indirin ve "Evet, Spectre'yi uzaktan çalıştırıyorum" olarak ayarlayın. Yapılandırmayı sonlandırmak için "Kaydet "e tıklayın.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Sonuç



Spectre Desktop, gelişmiş Bitcoin yapılandırmalarını demokratikleştirerek, egemenliğinizden veya gizliliğinizden ödün vermeden çoklu imzayı erişilebilir hale getirir. Önemli miktarda parayı yöneten kullanıcılar için, kurumsal uygulamaları özel kişiler tarafından kullanılabilecek çözümlere dönüştürür.



Uygulama, altyapı ve öğrenme için başlangıç yatırımı gerektirse de tam bir egemenlik sunar: doğrulama altyapısının kontrolü, anahtarların fiziksel sahipliği ve üçüncü taraf gözetiminden uzak işlemler. İster birikimlerini güvence altına alan bir birey, ister çok nesilli bir kasa oluşturan bir aile ya da nakit akışını yöneten bir şirket olun, Spectre Desktop maksimum güvenlik ve mutlak egemenliği uzlaştırmak için referans araçtır.



## Kaynaklar



### Resmi belgeler




- [Spectre Desktop resmi web sitesi](https://specter.solutions/desktop/)
- [GitHub kaynak kodu](https://github.com/cryptoadvance/specter-desktop)
- [Belgelerin tamamı](https://docs.specter.solutions/)



### Topluluk ve destek




- [Telegram Spectre Topluluk Grubu](https://t.me/spectersupport)
- [Reddit tartışma forumu](https://reddit.com/r/specterdesktop/)
- [GitHub hata raporları](https://github.com/cryptoadvance/specter-desktop/issues)