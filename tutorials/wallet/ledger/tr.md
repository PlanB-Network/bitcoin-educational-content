---
name: Ledger Nano S

description: Ledger Nano S cihazınızı nasıl kurarsınız?
---

![image](assets/cover.webp)


*Ledger, 25 Haziran 2025 itibariyle klasik Nano S için yazılım desteğinin sona erdiğini duyurdu: bu cihaz artık güvenlik güncellemeleri almayacak veya yeni özelliklerle uyumlu olmayacak ve kullanıcılarını potansiyel güvenlik açıklarına ve gelecekteki uyumsuzluğa maruz bırakacak. Bununla birlikte, kurtarma ifadesi aracılığıyla fonlara erişilebilir, ancak bitcoinlerinizin güvenliğini ve uzun vadeli erişilebilirliğini sağlamak için daha yeni bir modele geçmeniz şiddetle tavsiye edilir. Lütfen bunun **eski Nano S** ile ilgili olduğunu, desteklenmeye devam edecek olan **Nano S Plus** ile ilgili olmadığını unutmayın.*


___


Cold fiziksel Wallet - €60 - Başlangıç - €2,000 ila €50,000 arası güvence altına almak için


Ledger, bitcoinleri basit bir şekilde güvence altına almak için Fransız çözümüdür.


Bu eğitimde, büyük meblağları saklamak için gelişmiş bir güvenlik çözümü olan parolalar bölümünü de tartışıyoruz: 20,000€ - 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


# Ledger'i Sparrow'ye bağlayın Bitcoin Wallet (yazma kılavuzu)


Önce "Bitcoin Donanım Cüzdanlarını Kullanma" başlıklı diğer parçayı gözden geçirdiğinizden emin olun. Burada bazı adımları gözden geçireceğim ve çoğunlukla Ledger'e özgü olanlara odaklanacağım.


## Cihazın kurulumu


Ledger kendi USB kablosuyla birlikte gelir. Bunu kullandığınızdan emin olun ve herhangi bir eski kabloyu kullanmayın. Bazı USB kabloları sadece güç sağlar. Bu kablo hem veri hem de güç iletiyor. Cihazı etrafta duran bir telefon şarj USB kablosuyla kullandığımda, cihaz bağlanamadı.


Bilgisayarınıza bağlayın ve cihaz açılacaktır.


![image](assets/1.webp)


Seçenekler arasında dolaşın. Göreceksiniz


1. Yeni cihaz olarak ayarla

2. Kurtarma ifadesinden geri yükleme


Temel olarak, cihazın sizin için bir seed oluşturmasını isteyip istemediğinizi veya zaten kullanmak istediğiniz bir seed'ünüz olup olmadığını soruyor. Kendi seed'ünüzü yapmak en iyi uygulamadır, ancak bunu güvenli bir şekilde yapmak çok ileri düzeydedir ve bu makalenin kapsamı dışındadır. "Yeni cihaz olarak ayarla "yı seçin


Daha sonra bir PIN seçmeniz istenecektir. Bu Bitcoin seed cihazınızın bir parçası değildir ve sadece bu cihaza özeldir. Cihazı kilitler.


Daha sonra size üzerinden geçmeniz ve yazmanız gereken 24 kelime sunacaktır.


Garip bir şekilde, sonuna geldiğinizde "kelimelerinizi doğrulamak için sola basın" diyor. Bu, devam etmek için nasıl onaylayacağınızı açıklamıyor, sadece geri dönüp kelimelere tekrar bakabileceğiniz anlamına geliyor. Bunun yerine sağa basın ve sol ve sağa aynı anda basarak onaylayın.


Bir sonraki kısım çok can sıkıcı. 24 kelimeyi karıştırıyor ve 1'den 24'e kadar her seçim için tüm kelimeler arasında geçiş yaparak her birini onaylamanız gerekiyor. İşiniz bittiğinde, iki düğmeye basarak onaylamanıza ve devam etmenize izin verir.


![image](assets/2.webp)


Kontrol panelinizde bir ayarlar düğmesi ve uygulamaları yüklemenizi sağlayan bir artı işareti düğmesi olduğunu göreceksiniz. Ama önce Ledger Live'a bağlanmanız gerekiyor. Bunu daha sonra yapacağız..


## Ledger Canlı İndir


Ledger Live'ı web sayfasından indirebilirsiniz, ancak kaynak kodunun tutulduğu GitHub'dan edinmek daha iyidir.


Google "Ledger live GitHub" veya tıklayın ![this](link https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


"İndirilenler" başlığını görene kadar aşağı kaydırın..


![image](assets/4.webp)


En altta, bağlantıyı göreceksiniz: Kurulum paketlerinin Hash ve imzalarını doğrulamak için talimatlar bu sayfada mevcuttur. Bu bağlantıya tıklayın.(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


En üstte, işletim sisteminize bağlı olarak ihtiyacınız olan yazılım paketi için bağlantı seçenekleri vardır. İndirmek için uygun olana tıklayın.


Daha sonra, ekstra güvenlik için indirmenin Hash'ünü doğrulamak istiyoruz. Ledger, mevcut dosyaların her birinin Hash'ünü yayınlar. Şimdi indirmeyi Hash ile yapacağız ve çıktıyı karşılaştıracağız. Dosyanın kurcalanmadığından emin olmak için aynı olması gerekir.


Mac'te terminali veya Windows'ta CMD'yi açın; içine aşağıdaki komutları yazın ve enter tuşuna basın:


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


Umarım komutların oklardan sonra başladığı açıktır. Bu makale güncel değilse, komutlardaki dosya adını tam olarak indirdiğiniz dosya adıyla değiştirdiğinizden emin olun. Her komuttan sonra <Enter> tuşuna basmanız gerekir. Burada görülen komutlar web tarayıcınızda bir satıra sığmayabilir. Tümünün tek satırda yazıldığına dikkat edin.


Hash'ün çıktısına bakın ve GitHub'da yayınlananla aynı olduğundan emin olun.


İdeal olarak, ekstra süslü olmak ve yayınlanan hash'lerin sahte olmadığından emin olmak istersiniz. Bunu gpg imzaları ile yaparız, ancak bu makalenin kapsamı dışındadır. Eğer bu konuda bilgi edinmek istiyorsanız (ki eninde sonunda öğrenmenizi öneririm) bu makaleye göz atabilirsiniz.


## Ledger Live'a bağlanın


Ledger Live'ı çalıştırmadan önce, bir VPN açmak gizliliğe biraz yardımcı olur. Ledger yine de tüm adreslerinizi alacaktır, ancak evinizdeki Address'yı ele veren IP Address'nızı bilmeyeceklerdir. Mullvad VPN mükemmel bir VPN hizmetidir ve çok pahalı değildir (reklam yapmıyorum, sadece kullandığım şey bu).


Yazılımı bilgisayarınıza yükleyin ve çalıştırın.


![image](assets/6.webp)


Cihazınızı seçin ve "İlk kez kullanıyorum..." seçeneğini seçin


![image](assets/7.webp)


Daha sonra bir sihirbaz aracılığıyla yönlendirileceksiniz, ancak tüm bu adımları döngüye girebilmeniz için yaptık.


![image](assets/8.webp)


Birçok adımdan ve bir testten sonra, cihazın orijinal olup olmadığını kontrol edecektir. Bağlandığınızdan ve pini girdiğinizden emin olmanız gerekir ve ardından cihazda Ledger Live'ın bağlanmasına izin verip vermediğinizi soracaktır. Elbette bunu onaylamanız gerekiyor.


![image](assets/9.webp)


Bir sonraki açılır pencerede "sürüm notları" olarak gizlenmiş bazı boktan reklamlar vardı. Onu kapatın ve sonra bu ekrana gelmelisiniz.


![image](assets/10.webp)


Bir Bitcoin Wallet almak için "Hesap ekle "ye tıklamanız gerekir.


![image](assets/11.webp)


Bitcoin Cash veya başka bir shitcoin değil, Bitcoin seçtiğinizden emin olun. Cihazı kontrol edecek ve CİHAZ ÜZERİNDE devam etmek için onaylamanız gerekecek. Birkaç dakika boyunca adresleri hesaplayacaktır. Sonra BİTTİ'ye tıklayın.


![image](assets/12.webp)

![image](assets/13.webp)


Harika. Artık bilgisayarınızda bir Bitcoin Wallet içeren bir shitcoin Wallet yöneticiniz var. Aslında artık buna ihtiyacınız yok ve ondan kurtulabilirsiniz. Asıl amaç, Bitcoin Uygulamasını cihazın kendisine yerleştirmekti ve bazı aşırı yazılım mühendisliği teknikleri uygulamak dışında tek yol buydu.


Daha önce cihazda bir ayarlar düğmesi ve bir artı işareti düğmesi olduğunu hatırlayın. Şimdi fazladan bir düğmemiz daha var - Bitcoin App düğmesi.


Ledger Live'ı şimdi kapatabilirsiniz.


## Bir passphrase ekleyin


Artık Bitcoin Uygulamasına sahip olduğumuza göre, seed cümlemize bir passphrase ekleyebiliriz. seed ilk oluşturulduğunda bunu daha önce yapamıyorduk çünkü başlangıçta Bitcoin Uygulamamız yoktu ve onu almak için Ledger Live'a bağlanmamız gerekiyordu.


Cihazın içindeki "ayarlar" menüsüne ve ardından "güvenlik" alt menüsüne gidin. Ardından passphrase'i seçin. "Gelişmiş özellik" seçeneğini göreceksiniz. Sağ tuşa tıklayın, "kılavuzu oku..." yazısını göreceksiniz ve ardından sağ tuşa tıkladıktan sonra "geri" yazısını göreceksiniz. Ama bu son değil. Sezgisel olarak böyle düşünürsünüz ama sağ düğmeye tekrar tıklayın. "passphrase'i kur" seçeneğini göreceksiniz.


"PIN'e ekle" veya "Geçici olarak ayarla" seçeneklerinden birine karar verebilirsiniz. Ben "PIN'e ekle" seçeneğini öneriyorum. Bu şekilde, cihazı ilk açtığınızda girdiğiniz PIN'e bağlı olarak farklı cüzdanlara erişebilirsiniz. "Geçici olarak ayarlarsanız", passphrase'ye her erişmek istediğinizde Wallet'ü girmeniz gerekir, ancak bu her zaman varsayılan PIN'den olur.


passphrase'ü girin ve onaylayın.


Sizden "Mevcut PIN" kodunu isteyecektir. Bu, yeni passphrase ile ilişkilendirdiğiniz PIN değildir. Bu oturum için cihazı açtığınızda girdiğiniz PIN kodudur.


Şimdi geri seçeneğini birkaç kez seçerek ana menüye çıkabilirsiniz.


## Wallet izleniyor


Önceki makalelerde, Sparrow wallet'yi nasıl indireceğinizi ve doğrulayacağınızı ve kendi düğümünüze veya genel bir düğüme nasıl bağlayacağınızı açıkladım. Bu kılavuzları takip etmelisiniz:



- Bitcoin core'i kurun ( https://armantheparman.com/bitcoincore/)



- Sparrow Bitcoin Wallet'i kurun (https://armantheparman.com/download-Sparrow/)



- Sparrow Bitcoin Wallet'i Bitcoin core'ye bağlayın (https://armantheparman.com/sparrowcore/)


Sparrow Bitcoin Wallet kullanımına bir alternatif Electrum Desktop Wallet'dir, ancak çoğu insan için en iyisi olduğuna karar verdiğim için Sparrow Bitcoin Wallet'i açıklamaya devam edeceğim. İleri düzey kullanıcılar Electrum'u alternatif olarak kullanmak isteyebilirler.


Şimdi onu yükleyeceğiz ve Ledger'ı, passphrase'u içeren Wallet ile bağlayacağız. Bu Wallet hiçbir zaman Ledger Live'a maruz kalmadı çünkü cihazı Ledger Live'a bağladıktan SONRA oluşturuldu. Yeni özel Wallet'inizi ifşa etmemek için bir daha asla Ledger Live'a bağlamadığınızdan emin olun.


Yeni bir Wallet oluşturun:


![image](assets/14.webp)


Güzel bir isim ver


![image](assets/15.webp)


"Mevcut işlem var" onay kutusuna dikkat edin. Bu daha önce kullandığınız bir Wallet ise, bunu işaretleyin, aksi takdirde bakiyeniz yanlışlıkla sıfır olarak gösterilecektir. Bu kutunun işaretlenmesi Sparrow'in önceki işlemler için Bitcoin core'ün veritabanını (Blockchain) incelemesini ister. Bu kılavuz için yepyeni bir Wallet kullanıyoruz, bu nedenle kutuyu işaretlemeden bırakabilirsiniz.


![image](assets/16.webp)


"Bağlı Hardware Wallet" üzerine tıklayın ve cihazın gerçekten bağlı olduğundan, açık olduğundan, PIN girildiğinden ve Bitcoin Uygulamasına girdiğinizden emin olun.


![image](assets/17.webp)


Bir sonraki ekranda "Tara "ya ve ardından "Anahtar Deposunu İçe Aktar "a tıklayın.


![image](assets/18.webp)


Bir sonraki ekranda düzenleyecek bir şey yok, Ledger bunu sizin için doldurdu. "Uygula "ya tıklayın


![image](assets/19.webp)


Bir sonraki ekran bir şifre eklemenizi sağlar. Bunu "passphrase" ile karıştırmayın; birçok kişi karıştıracaktır. İsimlendirme talihsiz. Parola, bu Wallet'yi bilgisayarınızda kilitlemenizi sağlar. Bu bilgisayardaki bu yazılıma özeldir. Bitcoin özel anahtarınızın bir parçası değildir.


![image](assets/20.webp)


Bir duraklamadan sonra, bilgisayar düşünürken, soldaki düğmelerin griden maviye dönüştüğünü göreceksiniz. Tebrikler, Wallet'ünüz artık kullanıma hazır. Gönlünüzce işlem yapın ve gönderin.


![image](assets/21.webp)


## Teslim alma


Bazı Bitcoin'ları almak için soldaki Adresler sekmesine gidin ve alınacak adreslerden birini seçin. İstediğiniz Address'e sağ tıklayın ve "Address'i kopyala" seçeneğini seçin. Ardından paranın gönderildiği Exchange'ünüze gidin ve oraya yapıştırın. Ya da Address'i size ödeme yapmak için kullanabilecek bir müşteriye verebilirsiniz.


Wallet'u ilk kez kullandığınızda, çok küçük bir miktar almalısınız, Wallet'un beklendiği gibi çalıştığını kanıtlamak için Wallet içinde veya Exchange'ye geri dönerek başka bir Address'e harcama alıştırması yapın.


Bunu yaptıktan sonra, yazdığınız kelimeleri yedeklemelisiniz. Tek bir kopya yeterli değildir. En az iki kağıt kopyanız olsun (metal daha iyidir) ve bunları iki farklı, iyi korunmuş yerde saklayın. Bu, doğal bir felaketin HWW'nizi ve kağıt yedeklemenizi tek bir olayda yok etme riskini azaltır. Bu konuda tam bir tartışma için "Bitcoin Donanım Cüzdanlarının Kullanımı" bölümüne bakın.


## Gönderme


![image](assets/22.webp)


Bir ödeme yaparken, ödeme yaptığınız Address'i "Öde" alanına yapıştırmanız gerekir. Aslında Etiketi boş bırakamazsınız, bu sadece kendi cüzdanlarınızın kayıtları içindir, ancak Sparrow buna izin vermez - sadece bir şey girin (sadece siz göreceksiniz). Tutarı girin ve istediğiniz ücreti manuel olarak da ayarlayabilirsiniz.


HWW bağlı olmadığı sürece Wallet işlemi imzalayamaz. Bu HWW'nin görevidir - işlemi almak, imzalamak ve imzalanmış olarak geri vermek. Cihazı imzalarken, ödeme yaptığınız Address'ün cihazda ve bilgisayar ekranında aynı olduğunu ve aldığınız Invoice'ü görsel olarak incelediğinizden emin olun (örneğin, belirli bir Address'ü ödemeniz için bir e-posta almış olabilirsiniz).


Ayrıca, ödeme tutarından daha büyük bir Coin kullanmayı seçerseniz, kalanın cüzdanlarınızın değişim adreslerinden birine geri gönderileceğine dikkat edin. Bazı kişiler bunu bilmemektedir ve işlemlerini herkese açık bir Blockchain'da aramış ve bir miktar Bitcoin'in bir saldırganın Address'sine gönderildiğini düşünmüştür, ancak aslında bu kendi değişim Address'leridir.


## Ürün Yazılımı


Ürün yazılımını güncellemek için Ledger Live'a bağlanmanız gerekir. Bunu yapmak istiyorsanız, önce cihazı silmeli ve cihazı geri yüklemek için yedek kelimelerinizin ve passphrase'ın mevcut olduğundan emin olmalısınız. Önce cihazı silmeyi tercih etmemin nedeni, aygıt yazılımını güncellemek için cihazınızı Ledger Live'a bağlamanız gerekmesi ve yeni Wallet'nizi (passphrase'lı olan) asla Ledger Live'a maruz bırakmamayı tercih etmem. Ledger Live'a bağlandığımda Ledger'in cihazdan açık anahtar bilgilerimi almadığına güvenmiyorum. Yapmadıklarını iddia ediyorlar, ancak kodu okumadan ve dahili donanımı da anlamadan bunu kendim doğrulayamam.


## Sonuç


Bu makale size bir Ledger HWW'yi reklamı yapılandan daha güvenli ve daha özel bir şekilde nasıl kullanacağınızı gösterdi - ancak bu makale tek başına yeterli değil. Başta da söylediğim gibi, bunu "Bitcoin Donanım Cüzdanlarının Kullanımı" bölümünde verilen bilgilerle birleştirmelisiniz.

İpuçları:


Statik Yıldırım Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


Bu konuyu daha fazla keşfetmek ve BIP39 passphrase ile Ledger Nano üzerindeki Wallet'inizin güvenliğini güçlendirmek için sizi bu kapsamlı eğitime göz atmaya davet ediyorum:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49