---
name: Cashu.me
description: Cashu.me ecash kullanım kılavuzu
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*İşte BTC Sessions'tan, uygulama mağazasına ihtiyaç duymadan basit, ucuz ve özel Bitcoin işlemlerine erişmenizi sağlayan Cashu.me Bitcoin Wallet'in nasıl kurulacağı ve kullanılacağı konusunda size yol gösteren bir video rehberi!


Bu eğitimde Chaumian ecash kullanarak özel Wallet ödemeleri için tarayıcı tabanlı bir Bitcoin olan Cashu.me'yi keşfedeceğiz. Başlamadan önce, ecash ve nasıl çalıştığına dair kısa bir giriş yapalım.


## Ecash'e giriş


Cebinizde tıpkı fiziksel banknotlar gibi çalışan dijital paranız olduğunu hayal edin - özel, anında ve aracılar olmadan eşler arası kullanılabilir. İşte ecash bunu mümkün kılıyor: fiziksel paranın gizliliğini dijital dünyaya geri getiren bir dijital ödeme yaklaşımı. Her işlemi herkesin görebileceği halka açık bir Ledger'e kaydeden onchain-Bitcoin'ün aksine ecash, harcama alışkanlıklarınızı gizli tutarken gerçek Bitcoin değerini temsil eden özel tokenlar oluşturur.


Ecash'i cihazınızda depolanan dijital hamiline yazılı araçlar olarak düşünün - bunları tutarsanız, tıpkı fiziksel nakit gibi onlara sahip olursunuz. Bu tokenlar, temel Bitcoin rezervlerini tutan "Mints" adı verilen güvenilir hizmetler tarafından verilir. Ecash kullandığınızda, işlemlerinizi tüm ağa yayınlamazsınız. Bunun yerine, özel tokenları doğrudan başkalarıyla değiş tokuş ederek, geleneksel bir dijital ödeme yapmaktan çok birine nakit para vermek gibi hissettiren bir ödeme deneyimi yaratırsınız.


Cashu, Bitcoin için oluşturulmuş ücretsiz ve açık kaynaklı bir Chaumian ecash protokolüdür. Teknoloji, David Chaum'un 1980'lerdeki öncü kriptografik araştırmalarına dayanmakta ve gizliliği sağlamak için "kör imzalar" kullanmaktadır. Ecash token'ları aldığınızda, darphane bunları bir sonraki aşamada nereye harcanacaklarını bilmeden imzalar - işlem takibini önleyen çok önemli bir özellik. Daha da önemlisi, ecash Bitcoin'in yerini almaz; Bitcoin mimari gereksinimleriyle birlikte gelen bazı kritik sorunları ele alarak onu tamamlar. Fiziksel paranın sunduğu (Bitcoin'in şeffaf Ledger'unda bulunmayan) gizliliği sağlar ve Blockchain ücretleri veya onay gecikmeleri olmadan anında mikro işlemlere olanak tanır.


Ecash, Lightning Network ile sorunsuz bir şekilde entegre olur. Bitcoin'i bir darphaneye yatırmak (Bitcoin değerinizi ecash jetonlarına dönüştürmek) ve daha sonra çekmek (jetonları tekrar harcanabilir Lightning bakiyesine dönüştürmek) için Lightning'i kullanırsınız. Birlikte güçlü bir kombinasyon oluştururlar: Bitcoin güvenli yerleşim Layer'yi sağlar, Lightning hızlı işlemler ve ağ birlikte çalışabilirliği sağlar ve ecash dijital ödemeleri yeniden gerçekten özel hissettiren gizlilik Layer'yi ekler.


## Cashu.me


Cashu.me, Bitcoin için tasarlanmış Chaumian ecash'in özel bir uygulaması olan Cashu protokolünü uygulayan bir `Progressive Web App (PWA)`dır. Bir PWA olarak, uygulama mağazalarından kurulum gerektirmeden doğrudan tarayıcınızda çalışır, ancak daha kolay erişim için cihazınıza 'yükleyebilirsiniz'. Bu web tabanlı yaklaşım, platform kısıtlamaları yerine kriptografik protokoller aracılığıyla güvenliği korurken işletim sistemleri arasında geniş uyumluluk sağlar.


## 🎉 Temel Özellikler


Şimdi özellikleri inceleyelim ve Cashu.me'nin neler sunabileceğini keşfedelim:



- Lightning** üzerinde Chaumian ecash: Kör imzalar kullanır, böylece darphaneler kullanıcı bakiyelerini veya işlem geçmişlerini izleyemez
- Jetonların kendi kendine muhafazası**: seed ifadenizle ecash jetonlarını yerel olarak kontrol edersiniz
- seed ifade yedekleri**: gW-15 restorasyonu için 12 kelimelik kurtarma cümlesi
- Darphane bağımsızlığı**: Birden fazla bağımsız darphane ile çalışır - tek bir sağlayıcıya bağlı kalmazsınız
- Anında, ücretsiz işlemler**: Aynı darphane içinde, ödemeler sıfır ücretle saniyeler içinde sonuçlanır
- Gizliliği koruyan mimari**: Darphaneler kimin kiminle işlem yaptığını göremez
- Çevrimdışı ecash**: İnternet bağlantısı olmadan NFC, QR kodu, Bluetooth vb. gibi yerel bir iletim protokolü aracılığıyla jeton gönderin/alın
- Nostr** aracılığıyla ecash darphanelerini keşfedin: Nostr protokolü aracılığıyla güvenilir darphaneleri bulun ve doğrulayın
- Darphaneler arasında ecash takas edin**: Tüm darphaneler Lightning konuşur, bu da aralarında değer aktarabileceğiniz anlamına gelir.
- Nostr Wallet Connect (NWC)** ile Wallet'nizi uzaktan kontrol edin: Nostr Client gibi diğer uygulamalara bağlanın ve NWC aracılığıyla zaplamaya başlayın


Kritik değiş tokuş "güven "dir: tokenların kendilerini kontrol ederken, altta yatan Bitcoin rezervlerini saklamak için darphanelere güvenmelisiniz. Cashu'nun belgelerinde belirtildiği gibi:


> ...darphane Lightning altyapısını çalıştırıyor ve darphane ecash kullanıcıları için satoshileri saklıyor. Kullanıcılar Lightning'e geçmek istediklerinde ecash'lerini Redeem için darphaneye güvenmelidir.

- Cashu Dokümantasyonu, [Genel Güvenlik ve Gizlilik Soruları](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Bu, ecash'i Bitcoin'nin kendisi için bir saklama çözümü haline getirir, ancak tokenlerin tam kontrolünü elinizde tutarsınız.


## 1️⃣ İlk Kurulum


① Tarayıcınızda [Wallet.cashu.me](https://Wallet.cashu.me) adresini ziyaret ederek başlayın. Cashu.me bir `PWA` olduğundan, uygulama mağazalarından indirmenize gerek yoktur, siteyi doğrudan tarayıcınızda açmanız yeterlidir. Daha kolay erişim için, isteğe bağlı olarak cihazınızın ana ekranına yükleyebilirsiniz.


② PWA'yı yüklemek için tarayıcınızdaki ⋮ menü düğmesine dokunun ve `Ana Ekrana Ekle`yi seçin. Yüklendikten sonra tarayıcı sekmesini kapatın ve Cashu.me'yi cihazınızın ana ekranından başlatın. Karşılama ekranında, devam etmek için `Sonraki` seçeneğine dokunun.


③ Güvenlik çok önemlidir. seed ifadenizi bir şifre yöneticisinde güvenli bir şekilde saklayın veya daha da iyisi kağıda yazın. Bu 12 kelimelik kurtarma cümlesi, bu cihaza erişiminizi kaybetmeniz durumunda fonları kurtarmanın tek yoludur. seed ifadenizi ortaya çıkarmak için 👁️ simgesine dokunun, 12 kelimeyi dikkatlice sırayla yazın, ardından `Yazdım` işaretli kutuyu işaretleyin. Devam etmek için `Sonraki` seçeneğine dokunun ve aşağıdaki ekranda `şartları` kabul ettiğinizi onaylamak için kutuyu işaretleyin.


![image](assets/en/01.webp)


Kurulumu tamamladıktan sonra, bir `Mint`e bağlanmanız gerekecektir. Nostr topluluğu tarafından önerilen darphaneleri görüntülemek için `ADD MINT` ve ardından `DISCOVER MINTS` üzerine dokunun. Ek doğrulama için [bitcoinmints.com](bitcoinmints.com) adresinden darphane derecelendirmelerini inceleyebilirsiniz.


Daha sonra tam listeyi görmek için `Nane şekerlerine göz atmak için tıklayın` seçeneğine dokunun. URL'sini kopyalayıp URL alanına yapıştırarak ve tanınabilir bir ad vererek bir nane seçin. Bu örnek için şunu kullanacağız:


URL: `https://mint.minibits.cash/Bitcoin`

İsim: `Minibits`


![image](assets/en/02.webp)


İşlemi tamamlamak için `ADD MINT` üzerine dokunun. Onay ekranında, bu nanenin operatörüne güvendiğinizi doğrulayın ve ardından tekrar `ADD MINT` üzerine dokunun. Minibits nane şekeri artık Ana Ekranınızda görünecektir. Wallet'ünüz kurulduktan sonra, işlem yapmadan önce ona para yatırmanız gerekecektir.


![image](assets/en/03.webp)


## 2️⃣ Wallet'inizin Finansmanı


Cashu.me, Wallet'nıza para yatırmak için iki farklı yöntem sunar. Ana Ekranda "Al" seçeneğine dokunduğunuzda, "NAKİT" veya "AYDINLATMA" yoluyla para alma seçeneklerini göreceksiniz.


![image](assets/en/04.webp)


### LIGHTNING aracılığıyla finansman


İlk seçenek Wallet'i Lightning Invoice aracılığıyla finanse etmektir. farklı darphaneler eklediyseniz `Bir darphane seçin` ve almak istediğiniz `miktarı (Sats)` tanımlayın. Ardından `Invoice OLUŞTUR` seçeneğine dokunun. Şimdi başka bir yıldırım Wallet ile tarayabileceğiniz bir QR Kodu görüntülenir veya Invoice'yi basitçe `Kopyalayabilir` ve cashu.me Wallet'inizi ödemek ve finanse etmek için başka bir Wallet'e yapıştırabilirsiniz.


![image](assets/en/05.webp)


### Ecash alma


Ecash yöntemi, doğrudan başka bir ecash Wallet'dan token almanızı sağlar. Al` düğmesine dokunarak ve `ECASH` seçeneğini seçerek başlayın. Başka bir Wallet'dan Cashu token göndermek için `Yapıştır` veya `Tarama` yapabilir ya da `NFC` kullanabilirsiniz. Yapıştırmayı seçerseniz, başka bir Wallet'dan kopyaladığınız token dizesini girin, `Miktar` ve `Nane` otomatik olarak görüntülenecektir. İşlemi tamamlamak için `ALMA` düğmesine dokunun ve Sats, Wallet'unuzda görünecektir. Bakiyenizin artık birden fazla darphaneye dağıtıldığına dikkat edin. Örneğin, Minibits `Mint`inizde 1.000 Sats ve Coinos `Mint`inizde ek 1.000 Sats olabilir. Farklı darphaneler arasındaki bu ayrım Cashu'nun mimarisinin önemli bir yönüdür.


![image](assets/en/06.webp)


### Naneler Arasında Değişim


Eklediğiniz belirli bir darphaneye artık güvenmiyorsanız, cashu.me bir darphaneden diğerine `Fon Takası` yapma özelliği sunar. Darphaneler sekmesine gidin ve `Multimint Swaps` seçeneğini görene kadar aşağı kaydırın. Açılır menülerden `FROM` ve `TO` darphanelerini seçin ve aktarmak istediğiniz tutarı girin. Tokenları darphaneler arasında taşımak için `SWAP` seçeneğine dokunun. Bu işlem Lightning işlemi aracılığıyla gerçekleştirilecektir, bu nedenle olası Lightning ücretleri için yer bırakmanız gerekir. Benim örneğimde 1 sat yeterli oldu.


![image](assets/en/07.webp)


## 3️⃣ Fon gönderme


Sats göndermek için Cashu.me iki seçenek sunar. Nakit veya yıldırım yoluyla göndermek için. Her iki seçeneğe de bir göz atalım.


### Lightning ile Gönderme


Lightning ile göndermek için aşağıdaki adımları izleyin:


1. Ana Ekranda `GÖNDER` üzerine dokunun ve `Yıldırım` öğesini seçin

2. Uygulama sizden bir `Lightning Invoice` veya `-Address` girmenizi isteyecektir. Invoice/Address'ü doğrudan yapıştırabilir veya görsel olarak yakalamak için QR kodunu tara seçeneğini kullanabilir, ardından `ENTER` ile onaylayabilirsiniz

3. Açılır alanı kullanarak ödeme yapmak istediğiniz Darphaneyi seçin ve onaylamak için `ÖDEME` seçeneğine dokunun. **Not**: `Ayarlar` -> `Deneysel` altında aynı anda birden fazla darphaneden fatura ödemenize olanak tanıyan `Multinut` kullanma seçeneği de vardır.

4. Başarılı bir şekilde tamamlandıktan sonra, ödeme onayını ve bakiyenizden düşülen tutarı göreceksiniz.


![image](assets/en/08.webp)


### Ecash ile gönderme


Ecash göndermek de benzer şekilde basittir.


1. GÖNDER` seçeneğine dokunun ve bu kez `ECASH` seçeneğini seçin.

2. "Bir nane seçin" ve göndermek istediğiniz "Tutar "ı Sats olarak girin ve onaylamak için "GÖNDER "e dokunun

3. Bu, Hız ve Boyut parametrelerini ayarlayarak özelleştirebileceğiniz bir `Animasyonlu QR Kodu` oluşturur. Herkes bu QR Kodunu tarayarak Redeem'yi hemen Sats'a dönüştürebilir veya KOPYALA'ya dokunarak token dizesini Bluetooth, NFC veya standart mesajlaşma gibi alternatif kanallar aracılığıyla başka birine gönderebilirsiniz.

4. Başka bir Wallet açıyorum. Panodan yapıştırın ve diğer Wallet'ta `Ecash al` seçeneğini seçin.


![image](assets/en/09.webp)


## 4️⃣ Ek Özellikler


Cashu.me, temel gönderme ve alma işlevlerinin ötesinde, Nostr ekosistemi içinde Bitcoin deneyiminizi geliştiren güçlü ek özellikler sunar.


### Nostr Wallet Bağlantı


Nostr Wallet Connect (`NWC`), Wallet'ünüz ve sosyal uygulamalarınız arasında kesintisiz bir bağlantı oluşturarak Nostr uygulamalarıyla etkileşim şeklinizi dönüştürür. Bu protokol, [Damus](https://damus.io/) veya [Primal](https://primal.net/home) gibi uygulamaların, uygulamadan çıkmanıza gerek kalmadan doğrudan Nostr röleleri aracılığıyla ödeme talep etmesine olanak tanır.


Cashu.me'de `NWC` kurmak için:


1. Sol üstteki Hamburger menüsünden `Ayarlar` seçeneğine gidin

2. NOSTR Wallet CONNECT` Bölümüne ilerleyin ve `Etkinleştir` Düğmesine dokunun

3. Daha sonra, uygulamaların Wallet'inizden harcayabileceği maksimum miktarı belirlemek için bir ödenek belirleyeceksiniz.

4. Yapılandırıldıktan sonra, bağlantı dizesini kopyalayabilir ve `NWC`yi destekleyen herhangi bir Nostr istemcisine yapıştırarak anında zapping ve devrilme işlevselliğini etkinleştirebilirsiniz.


![image](assets/en/10.webp)


### Lightning Address npub.cash aracılığıyla


Cashu.me, Nostr protokolü ile sorunsuz çalışan bir Lightning Address sağlamak için [npub.cash](https://npub.cash/) ile entegre olur. Burada, 5.000 Sats'e mal olan ve npub.cash projesini destekleyen Nostr `nsec`inizi sağlayarak kaydolabilir ve kullanıcı adınızı talep edebilir veya kayıt olmadan herhangi bir Nostr genel anahtarını (`npub`) kullanabilirsiniz.


İlk olarak, `Ayarlar` bölümüne gidin ve npub.cash ile Yıldırım Address`yi Etkinleştir`e dokunun. Bu, varsayılan olarak Wallet seed ifadenizden türetilen bir `npub` dizesi kullanarak generate bir npub.cash Address oluşturacaktır.


Alternatif olarak, kendi Nostr `nsec`inizi kullanarak özel bir kullanıcı adı talep etmek için [bu web sayfasını](https://npub.cash/username) ziyaret edin ve size username@npub.cash gibi kişiselleştirilmiş bir Lightning Address verin.


![image](assets/en/11.webp)


## 🎯 Sonuç


Cashu.me, fiziksel nakit gibi işleyen özel Bitcoin ödemeleri sunar - işlem geçmişinizi ifşa etmeden anında ve eşler arası. Şahsen PWA mimarisini takdir ediyorum çünkü uygulama mağazası kısıtlamalarından bağımsız çalışıyor. Bitcoin'ün güvenliğini, Lightning'in hızını ve ecash'in gizliliğini bir araya getiren Wallet, günlük Bitcoin kullanımını artırabilecek kullanım örnekleri sunuyor.


Öz saklama yoluyla ecash tokenlarınız üzerinde tam kontrole sahip olsanız da, darphanelerin temel Bitcoin rezervlerini tutan güvenilir üçüncü taraflar olarak hareket ettiğini unutmayın. Birden fazla darphane kullanma ve bunlar arasında takas yapma olanağı, gizliliği korurken esneklik sağlar.


NWC ve npub.cash adresleri gibi özellikler sayesinde Cashu.me, büyük teknoloji politikası kısıtlamaları yerine gizliliğe ve egemenliğe değer veren sosyal müşteriler için cazip bir Wallet seçeneğidir.


## 📚 Kaynaklar


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)