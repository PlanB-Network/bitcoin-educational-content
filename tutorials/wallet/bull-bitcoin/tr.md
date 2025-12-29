---
name: Bull Bitcoin Wallet
description: Wallet Bull Bitcoin'in nasıl kullanılacağını öğrenin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*BTC Sessions'ın bu eğitim videosu, Bull Bitcoin Wallet'ü kurma ve kullanma sürecinde size yol gösteriyor!


Bu kılavuz sizi Bull Bitcoin Wallet'ün kurulumu, yapılandırılması ve kullanımına götürür. Bitcoin On-Chain, Liquid ve Lightning ağlarında para gönderip almayı ve Bitcoin'yı bunlar arasında nasıl taşıyacağınızı öğreneceksiniz. wallet'in kapsamlı özellikleri, onu Bitcoin'nızı yönetmek için güçlü, hepsi bir arada bir araç haline getirir. Hadi başlayalım.


## Giriş


Bull Bitcoin](https://www.bullbitcoin.com/) tarafından geliştirilen Bull Bitcoin Wallet, **kendini emanet eden** bir Bitcoin wallet'tir; bu da üçüncü bir tarafa bağlı olmadan özel anahtarlarınız ve dolayısıyla fonlarınız üzerinde tam kontrole sahip olduğunuz anlamına gelir. Açık kaynaklı ve Cypherpunk felsefesine dayanan bu Wallet, basitlik, gizlilik ve ağlar arası takas ve PayJoin desteği gibi gelişmiş özellikleri bir araya getirir. Bitcoinlerinizi üç ağ üzerinde yönetmenizi sağlar: **Bitcoin onchain**, **Liquid** ve **Lightning**, her biri belirli kullanımlara göre uyarlanmıştır. BullBitcoin GitHub]'da (https://github.com/orgs/SatoshiPortal/projects/49) güncel konulara ve gelecek gelişmelere göz atabilirsiniz. Proje %100 açık kaynaklı ve "halka açık" olduğundan, önerilerinizi ve karşılaştığınız hataları da gönderebilirsiniz. Bazı cüzdanlar artık birden fazla ağı desteklerken, Bull Bitcoin Wallet gizlilik özelliklerini hepsine derinlemesine entegre ederek öne çıkıyor ve Bitcoin'nizi tüm büyük ağlarda yönetmek için güçlü bir araç haline getiriyor


## 1️⃣ Ön Koşullar


Bull Bitcoin Wallet**'yı kullanmaya başlamadan önce, aşağıdaki öğelere sahip olduğunuzdan emin olun:



- Uyumlu Akıllı Telefon**: Bir **iOS** (iPhone veya iPad) veya **Android** cihazı
- İnternet bağlantısı
- Güvenli yedekleme medyası**: Kurtarma cümlenizi** (12 kelime) kağıt veya metal üzerine yazın ve güvenli bir yerde saklayın.
- Temel bilgi**: Bitcoin kavramlarının (adresler, işlemler, ücretler) asgari düzeyde anlaşılması yararlıdır, ancak bu eğitim yeni başlayanlar için her adımı açıklamaktadır.


## 2️⃣ Kurulum


Uygulamayı şu yolla yükleyebilirsiniz:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(iOS cihazları için)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (Android cihazlar için)


Android kullanıcılarının da alternatif seçenekleri var:



- APK'yı doğrudan [GitHub Releases] (https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) sayfasından indirin veya
- Nostr uyumlu [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap) aracılığıyla yükleyin


Uygulamayı yükledikten sonra, hesabınızı yapılandırmak için karşılama ekranını takip edin.


## 3️⃣ İlk yapılandırma


Açılışta, aşağıdaki seçenekler sorulur:



- `Yeni Wallet Oluştur`
- `Recover Wallet` ve
- `Gelişmiş Seçenekler`


Gelişmiş Seçenekler'e dokunarak başlayalım.


Burada, bir wallet oluşturmadan veya kurtarmadan önce gelişmiş ayarları yapılandırabiliriz:


1. Trafiği Tor ağı üzerinden yönlendirmek için `Tor proxy`yi etkinleştirin.

1. etkinleştirmeden önce [Orbot uygulaması](https://orbot.app/en/) kurulmalı ve çalıştırılmalıdır

2. Tor Proxy yalnızca Bitcoin (Liquid değil) için geçerlidir ve daha yavaş bir bağlantıya neden olabilir.

2. Bir `Özel Electrum Server` kurun veya

3. Boğayı Kurtar` ayarlarını yapın. Daha sonra [Boğayı Kurtar] (https://recoverbull.com/) hakkında daha fazla bilgi edineceğiz.


Tüm isteğe bağlı ayarlamaları yaptıktan sonra `Bitti` seçeneğine dokunun. Mevcut bir Wallet'i yeniden kullanmak isterseniz, `Wallet'i Kurtar` seçeneğine tıklayın ve kurtarma ifadenizin 12 kelimesini doldurun.


Aksi takdirde, `Yeni Bir Wallet Oluştur` seçeneğine tıklayın.


![image](assets/en/01.webp)


## 4️⃣ Ana Ekran


Daha derine inmeden önce, yönümüzü bulmak için `Ana Ekran`a bir göz atalım:



- işlemlere genel bakış` ve `ayarlar menüsü` en üstte yer almaktadır.
- Mevcut Bakiye`de `açılabilen veya kapatılabilen` bir gizlilik seçeneği vardır.
- "Satın Almak, Satmak veya Ödemek" için "Bitcoin Bull Exchange "ye erişin (bu, yargı yetkisine bağlıdır ve KYC gerektirebilir).
- cüzdanlar arasında fonların `Transferi`
- `Secure Bitcoin` eşittir Onchain Bitcoin Wallet
- lightning- / Liquid Network üzerinden `Anında ödemeler` *(Not: Bull Bitcoin Wallet, ödemelerin Lightning üzerinden yapılmasını ve alınmasını sağlar. Lightning aracılığıyla alınan fonlar, [*Boltz exchange](https://boltz.exchange/) üzerinden otomatik takas sayesinde [*Liquid network](https://liquid.net/) (Wallet Anında Ödemeler'de) saklanır. Bu, size likidite kanallarını yönetmek zorunda kalmadan Lightning ile etkileşim kurma olanağı sağlarken, kendi kendini saklama özelliğini de korur.)
- fonların `Gönderilmesi` ve `Alınması`


![image](assets/en/02.webp)


İlk olarak, bazı önemli yapılandırmaları yapalım ve `Yedekleme` ile başlayalım.


## 5️⃣ Yedekleme


Yedekleme işlemine başlamak için uygulamanın sağ üst köşesindeki `dişli simgesine (⚙)` dokunun ve `Wallet Yedekleme`yi seçin. wallet'nizi güvence altına almak için size iki yöntem sunulacaktır: `Şifreli Kasa` ve `Fiziksel Yedekleme`. Şimdi her birini inceleyelim.


![image](assets/en/03.webp)


### Fiziksel Yedekleme


Kurtarma veya seed ifadenizi temsil eden 12 kelimelik bir liste görmek için `Fiziksel Yedekleme` üzerine dokunun. Lütfen aşağıdakileri göz önünde bulundurun:



- Kurtarma cümlenizi büyük bir dikkatle yazın. Kağıda veya metal üzerine yazın ve güvenli bir yerde (kiralık kasa, çevrimdışı konum) saklayın. Bu ifade, cihazınızın kaybolması veya uygulamanın silinmesi durumunda bitcoinlerinize erişmenin tek yoludur.
- Bu ifadeye sahip herhangi birinin tüm bitcoinlerinizi çalabileceğini de unutmamak gerekir. Asla dijital olarak saklamayın:
- Ekran görüntüsü yok
- Bulut, e-posta veya mesajlaşma yedeklemesi yok
- Kopyala/yapıştır yok (panoya kaydetme riski)


![image](assets/en/25.webp)


Bir sonraki ekranda seed ifadesini doğru yaptığınızdan emin olmak için kelimeleri doğru sıraya koymanız istenecektir. Test tamamlandığında ve başarılı olduğunda bir onay alacaksınız.


! **Bu nokta kritiktir**. Daha fazla yardım için :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Şifreli kasa


Ayrıca bulutta şifrelenmiş, anonim bir yedekleme seçeneği de vardır. Ancak son paragrafta bulut yedeklemelerinin riskli olduğundan ve kaçınılması gerektiğinden bahsetmemiş miydik? Bununla birlikte, Bull Bitcoin ekibi süreci güvenli hale getirmek için akıllıca bir yol geliştirdi. İşte nasıl çalıştığı:


"Recoverbull", yedeklemeyi iki parçaya bölerek Bitcoin wallet'nizin güvenliğini basitleştiren bir yedekleme protokolüdür. İlk olarak, wallet'nizin yedekleme dosyası güçlü bir şifreleme anahtarı kullanılarak cihazınızda şifrelenir. Bu şifrelenmiş dosyayı Google Drive veya cihazınız gibi istediğiniz yere kaydedebilirsiniz. İkinci olarak, dosyanın kilidini açmak için gereken şifreleme anahtarı Recoverbull Anahtar Sunucusu tarafından saklanır. wallet'nizi kurtarmak için hem şifrelenmiş yedekleme dosyasına hem de PIN veya şifrenizle eriştiğiniz anahtara ihtiyacınız vardır. Bu tasarım, bulut yedeklemenizin tek başına işe yaramamasını ve anahtar sunucusunun da sizin özel yedekleme dosyanız olmadan işe yaramamasını sağlar. Bu, bir parça tehlikeye girse bile fonlarınızı güvende tutar.


Bunu bir kiralık kasa gibi düşünün. Şifrelenmiş yedekleme dosyası, herhangi bir yerde (Google Drive gibi) saklayabileceğiniz *kutudur*. Kurtarma PIN'iniz ise Recoverbull Anahtar Sunucusu tarafından ayrı olarak saklanan *anahtar*. Bir hırsızın kutuyu açmak için hem sizin özel kutunuzu hem de sizin özel anahtarınızı ele geçirmesi gerekir. Bu tasarım, birisi yedekleme dosyanızı ele geçirse bile, sunucudan gelen anahtar olmadan işe yaramamasını ve sunucunun anahtarının benzersiz yedekleme dosyanız olmadan işe yaramamasını sağlar.


Recoverbull` wallet yedekleme protokolü hakkında daha fazla bilgi edinin [burada](https://recoverbull.com/).


Varsayılan Sunucuyu kullanmayı onaylamak için `Şifreli kasa` ve ardından `Devam et` üzerine dokunun. Bağlantı, gizlilik ve anonimlik sağlamak için `Tor` Ağı üzerinden yönlendirilecektir.


**Şifrelerinizi Anlamak**



- uygulama Kilidi Açma PIN`i**:** Telefonunuzdaki uygulamayı kilitlemek için `Ayarlar > Güvenlik PIN`inde ayarlanan isteğe bağlı PIN.
- kurtarma PIN`i**:** `Şifreli Kasa` yedekleme işlemi sırasında oluşturulan ve kurtarma sırasında yedekleme dosyanızın şifresini çözmek için kullanılan zorunlu PIN.


Bunlar iki ayrı PIN kodudur. wallet'ünüzü geri yüklemek için gerekli olduğundan Kurtarma PIN kodunuzu unutmayın."


**Kurtarma PIN Kurulumu:**



- wallet'inize erişimi kurtarmak için bir PIN veya Parola oluşturmanız gerekir.
- PIN / Parola en az 6 basamak uzunluğunda olmalıdır (örneğin, kabul edilmeyen 123456 gibi basit dizilerden kaçının).
- Bu PIN olmadan wallet'nın kurtarılması mümkün değildir.


Ardından, bir kasa sağlayıcısı seçin:



- `Google Drive` veya
- bir `özel konum` (örneğin cihazınız)


![image](assets/en/04.webp)


Şimdi, `yedekleme dosyasını` kaydedin. Ardından, `Kurtarmayı Test Et` seçeneğine dokunun, kayıtlı yedekleme dosyanızı veya kasanızı seçin ve ardından `Kasanın Şifresini Çöz` seçeneğine dokunun. PIN veya Parola`nızı girin. Her şey çalıştıysa, `Test başarıyla tamamlandı` ekranı görünecektir.


### İthalat / İhracat Etiketleri


Şimdi Yedeklememizi oluşturduğumuza göre `Etiketlere' bir göz atalım.  Bull Bitcoin wallet, kullanıcıların alıcı adresleri ve işlemleri için özel etiketler oluşturmalarına olanak tanıyarak gizliliği ve organizasyonu geliştirir. Bu etiketler, etiketli bir adrese gönderilen işlemler bu etiketi devralacağı için fonlarınızı kategorize etmenize yardımcı olur ve değişimlerini izlemek için giden işlemleri de etiketleyebilirsiniz. wallet [BIP-329] (https://bip329.org/) standardını tam olarak destekler, yani tüm etiketlerinizi bir dosyaya aktarabilir ve başka bir wallet'e aktarabilirsiniz. Bu özellik, kişiselleştirilmiş organizasyonunuzu kaybetmeden işlem geçmişinizi ve kategorizasyonlarınızı sorunsuz bir şekilde yedekleyebilmenizi veya bunları farklı wallet örnekleri arasında taşıyabilmenizi sağlar.


![image](assets/en/05.webp)


## 6️⃣ Ayarlar


Birincil yedeklemeniz güvence altına alındıktan sonra, ayarlarda bulunan diğer özellikleri keşfedelim.


### A - Erişimin güvence altına alınması


Uygulamayı güvenli hale getirmek için `Ayarlar` bölümüne gidin ve PIN Kodunu seçmek için `Güvenlik PIN`ini seçin. wallet'nize erişimi kilitlemek için güçlü bir PIN oluşturun. Bu adım isteğe bağlı olmakla birlikte, telefonunuzu başka birinin kullanması durumunda yetkisiz erişimi önlemek için şiddetle tavsiye edilir.


![image](assets/en/06.webp)


### B - Kişisel bir düğüme bağlantı (isteğe bağlı)


Wallet BullBitcoin varsayılan olarak Electrum sunucularına bağlanır: Bull Bitcoin tarafından yönetilen ilk sunucu ve Blockstream'den ikincil bir sunucu, her ikisinin de günlük tutmadığı ve izleme riskini azalttığı düşünülmektedir.


Daha fazla gizlilik için, uygulamayı bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayabilirsiniz. Bunu yapmak için, `Ayarlar` > `Bitcoin Ayarları` > `Electrum Server Ayarları` üzerine dokunun, ardından sunucunuzun adresini ve kimlik bilgilerini girmek için `+ Özel Sunucu Ekle` üzerine dokunun.


![image](assets/en/07.webp)


### C - Para Birimi


Mevcut bakiye ana ekranda hem `sats` hem de `USD` cinsinden görüntülenir. Bunu değiştirmek için `Ayarlar` > `Para Birimi` bölümüne gidin. Burada, `sats/BTC` arasında geçiş yapabilir ve `varsayılan fiat para biriminizi` seçebilirsiniz.


![image](assets/en/08.webp)


### D - Bitcoin Ayarları


Bitcoin Ayarları menüsü, wallet'ınızın temel yapılandırmalarına ve verilerine derinlemesine erişim sunar. Burada, `Secure Bitcoin` ve `Anında ödemeler cüzdanlarınızın` temel ayrıntılarını inceleyebilir, size tam şeffaflık ve kontrol sağlayabilirsiniz. Bu menüdeki temel özellikler şunlardır:



- Wallet Detayları:** Belirli bilgileri görüntülemek için Güvenli Bitcoin veya Anında ödemeler wallet'ünüze gidin.
- Wallet Parmak İzi:** wallet'iniz için benzersiz bir tanımlayıcı.
- Açık Anahtar (Pubkey):** generate alıcı adreslerinizi Bitcoin yapmak için kullanılan anahtar.
- Descriptor:** wallet'unuzun yapısının teknik bir özeti.
- Türetme Yolu:** Ana özel anahtarınızdan tüm adresleri generate yapmak için kullanılan belirli yol.
- Address Görünümü:** Kullanılmayan alıcı adreslerinizin listesine erişin ve adresleri değiştirin (yakında)


Ayrıca, şu seçeneklere de sahipsiniz:



- maksimum anlık wallet bakiyesini ayarlamak için `Otomatik Transferi Etkinleştir` ayarları, daha sonra otomatik olarak güvenli bitcoin wallet'ye aktarılacaktır.
- Genel cüzdanları `Mnemonic` İfadesi aracılığıyla içe aktarın veya `sadece izle`yi içe aktarın
- Donanım cüzdanlarını bağlayın: şu anda desteklenen cihazlar ColdcardQ, SeedSigner, Spectre, Krux, Blockstream Jade ve Foundation Passport'tur


## 7️⃣ Bull Bitcoin Exchange


Doğrudan wallet'den [Bull Bitcoin borsasına] (https://www.bullbitcoin.com/) erişerek uygulamadan çıkmadan Bitcoin satın alabilir, satabilir ve ödeme yapabilirsiniz. Bu entegrasyon, Bitcoin ihtiyaçlarınızı yönetmek için uygun bir çözüm sağlar. Lütfen borsaya ve hizmetlerine erişimin yetki alanınıza bağlı olarak kısıtlanabileceğini ve düzenleyici standartlara uymak ve platformun tüm özelliklerini kullanmak için Müşterinizi Tanıyın (KYC) doğrulamasının tamamlanması gerekebileceğini unutmayın.


Başlamak için, sağ alt köşedeki `Exchange` üzerine dokunun, ardından `Kayıt ol` veya hesabınıza `Giriş yap`.


Borsa aşağıdaki [özellikleri] sunmaktadır (https://www.bullbitcoin.com/):



- Banka hesabınızdan kendi gözetiminizle Bitcoin satın alın
- Gözetim altında olmayan
- Bireyler veya şirketler
- Anında para çekme
- Gizli ücret yok
- Lightning Network mevcut
- İşlem limiti yok
- Yinelenen satın alma seçenekleri


![image](assets/en/09.webp)


Daha fazla bilgi edinmek için lütfen bu eğitimi ziyaret edin:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Fonların alınması


Bull Bitcoin Wallet** ile fon almak basit ve esnektir, farklı kullanım durumları için uyarlanmış üç farklı ağı destekler:



- Güvenli, uzun süreli depolama için `Bitcoin (onchain)` ağı.
- Hızlı ve daha gizli işlemler için `Liquid` ağı.
- Anında, düşük maliyetli ödemeler için `Lightning` ağı.


Uygulama, seçtiğiniz ağa göre uygun adresi veya faturayı otomatik olarak oluşturur. Her bir ağ için nasıl ilerleyeceğiniz aşağıda açıklanmıştır.


### Onchain (Bitcoin ağı) üzerinden alma


on-chain fonlarını almak için Ana ekrandan `Güvenli Bitcoin Wallet`i seçip `Al`a dokunabilir veya ana `Al` düğmesine dokunup ardından `Bitcoin ağı`nı seçebilirsiniz.


Bir alma adresi oluşturmak için iki temel modunuz vardır:


**Varsayılan Mod (ek giriş parametreleri ile URI)


Varsayılan olarak, wallet bir [BIP21 URI] (https://bips.dev/21/) oluşturur. Bu, gizliliği artırmak için bir miktar, kişisel bir not ve PayJoin parametreleri dahil olmak üzere basit bir adresten daha fazla bilgiyi paketleyen standartlaştırılmış bir formattır. Bu kapsamlı URI bir QR koduna kodlanır ve kopyalanabilir hale getirilir. Format şu şekildedir: `bitcoin:<adres>?<parametre1>=<değer1>&<parametre2>=<değer2>`.



- Ek Girdi Parametreleri:**
    - Tutar:** BTC, sats veya fiat para birimi cinsinden istenen tutarı belirtin.
    - Mesaj:** Gönderen tarafından görülebilecek kişisel bir not ekleyin.
    - PayJoin:** İşlemde hem göndericiden hem de alıcıdan gelen girdileri birleştirerek gizliliği artırmak için bu seçeneği etkinleştirin.


Örnek URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Önemli Not: Lütfen bu eğitimdeki adreslere herhangi bir para göndermeyin, wallet silinecektir.*


![image](assets/en/10.webp)


**Sadece Address'i kopyala veya tara seçeneği etkin


Yalnızca Address'yı kopyala veya tara seçeneği etkinleştirildiğinde, uygulama SegWit (bech32) formatında basit bir Bitcoin adresi oluşturur.


Örnek:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Bir tutar veya not girseniz bile, bunlar QR koduna veya kopyalanan adrese dahil edilmeyecektir.


![image](assets/en/11.webp)


### Liquid Network üzerinden alım


Liquid Network üzerinden bir ödeme alabilirsiniz. Al ekranına geldiğinizde, bir ödeme talebi oluşturmak için aynı iki seçeneğe sahip olursunuz:


**1. Basit Address:** Standart `Liquid adresini` kopyalayın. Bu, wallet ağındaki Liquid'ünüz için benzersiz bir tanımlayıcıdır ve herhangi bir özel miktar veya mesaj içermez.


Örnek Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Detaylı Ödeme Talebi (URI):** Daha yapılandırılmış bir talep için bir miktar ve kişisel bir not belirtebilirsiniz. Bu bilgiler otomatik olarak paylaşılabilir bir URI'ye ve ilgili QR koduna kodlanır.



- Tutar:** Tutarı Bitcoin (BTC), Satoshis (Sats) veya fiat para birimi olarak ayarlayabilirsiniz.
- Not:** İşlemi tanımlamak için kişisel bir mesaj ekleyin.


**Örnek URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


İşlemi tamamlamak için göndericiye `adres` veya `URI` verin. Bunu panonuza kopyalayarak veya QR kodunu doğrudan ekranınızdan taratarak yapabilirsiniz.


![image](assets/en/12.webp)


### Lightning aracılığıyla alma



Bull Bitcoin Wallet ayrıca Lightning Network aracılığıyla ödeme göndermenize ve almanıza olanak tanır. Önemli bir özellik, Lightning aracılığıyla alınan fonların otomatik olarak takas edilmesi ve `Anında Ödemeler Wallet` içinde `Liquid Network` üzerinde saklanmasıdır. Bu hizmet `Boltz` tarafından desteklenmektedir. Bu tasarım, likidite kanallarını yönetmenin karmaşıklığı olmadan Lightning'in hızından ve düşük maliyetinden yararlanmanızı sağlarken, fonlarınızın tam öz muhafazasını da korur. Bu hibrit yaklaşım kendi kendini saklar ve kanalları yönetmenin karmaşıklığından kaçınırken, üçüncü taraf bir hizmet (Boltz), küçük bir takas ücreti ve anahtar sahipleri olarak Liquid Network'un görevli federasyonuna güvenir; bu da kendi kanallarınızı yönettiğiniz geleneksel, saklama gerektirmeyen Lightning wallet'den farklıdır. Liquid ve yönetim modeli hakkında daha fazla bilgiyi buradan edinebilirsiniz:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Sınırlar:**
    - Minimum Tutar:** Minimum fatura tutarı gereklidir. Geçerli limit için lütfen uygulamayı kontrol edin
    - Ücretler:** Alıcı olarak siz, küçük bir takas ücretinden sorumlusunuz. Bu ücret, göndericinin transfer ettiği miktardan düşülür ve değişikliğe tabidir
- Avantajlar:**
    - Kendi Kendine Emanet:** Paranız her zaman kontrolünüz altında, Liquid ağında güvence altındadır.
    - Yüksek On-Chain Ücretlerinden Kaçının:** Lightning'i kullanarak ve Liquid'de depolayarak, geleneksel bir Lightning kanalı açmayla ilişkili on-chain ücretlerini atlarsınız. Biriken miktar masrafı haklı çıkardığında, fonları daha sonra bir on-chain kanalına taşımayı seçebilirsiniz.
    - İpucu:** İki Bull Bitcoin kullanıcısı arasında en uygun maliyetli işlem için, Lightning takas ücretlerinden tamamen kaçınmak üzere doğrudan **Liquid ağını** kullanın.


Ödeme alabilmek için generate `Lightning faturası` almanız gerekmektedir:


1. `Tutar Girin`**:** Almak istediğiniz tutarı Bitcoin (BTC), Satoshis (Sats) veya fiat para birimi cinsinden belirtin.

2. `Not Ekle` **(İsteğe bağlı):** Bir not veya not ekleyin. Bu, faturaya gömülecek ve ödeme tamamlandığında işlem geçmişinizde görüntülenerek tanımlanmasını kolaylaştıracaktır.

3. `Invoice Geçerlilik`**:** Lightning faturası zamana duyarlıdır ve **12 saat** sonra sona erer. Bu süre içinde ödenmezse, geçersiz hale gelir ve generate yeni bir tane almanız gerekir.


Faturayı panonuza kopyalayarak veya ekranınızda görüntülenen QR kodunu taramalarını sağlayarak gönderene verin.


![image](assets/en/13.webp)


## 9️⃣ Fon gönderme


Gönderme ekranına doğrudan ana sayfadan veya cüzdanlarınızdan herhangi birinden erişebilirsiniz. Bull Bitcoin Wallet, ister yapıştırılmış ister QR kodu ile taranmış olsun, girdiğiniz adres veya faturaya göre hedef ağı (Bitcoin, Liquid veya Lightning) otomatik olarak tespit ederek süreci basitleştirir.


### On-Chain Bitcoin Ağı üzerinden İletim


on-chain ile para göndermek, işleminizin doğrudan Bitcoin blok zincirine kaydedilmesi anlamına gelir. Bu yöntem, daha büyük transferler veya zamana duyarlı olmayan transferler için en iyisidir. Başlamak için sağ alttaki "Gönder Düğmesi "ne dokunabilir ve bir "standart Bitcoin adresi" tarayabilir veya girebilirsiniz.


Sağladığınız adres belirli bir tutar içermiyorsa, gönderme ekranında ayrıntıları doldurmanız istenecektir. Tutarı BTC, satoshis veya fiat eşdeğeri gibi tercih ettiğiniz birimde belirtebilirsiniz. Ayrıca, işlemi daha sonra tanımlamanıza yardımcı olmak için kendi referansınız için özel bir not olan kişisel bir not ekleme seçeneğiniz de vardır. Bu not alıcı ile paylaşılmaz.


Tersine, taradığınız veya yapıştırdığınız ödeme talebi, önceden tanımlanmış bir tutara sahip bir BIP21 URI gibi gerekli tüm ayrıntıları zaten içeriyorsa, wallet veri giriş ekranını atlayacak ve ödemeyi yetkilendirmek için sizi doğrudan onay ekranına götürecektir.


![image](assets/en/14.webp)


İşleminiz yayınlanmadan önce, size bir onay ekranı sunulacaktır. Alıcı adresi, gönderilen miktar ve ağ ücretlerine çok dikkat ederek her parametreyi dikkatlice gözden geçirmeniz çok önemlidir. Bu ekran aynı zamanda işleminizi özelleştirmek için güçlü araçlar sunar.


Ücretleri iki temel yolla kontrol edebilirsiniz. İlk yöntem, düşük, orta veya yüksek gibi istediğiniz bir işlem hızını seçmektir ve wallet sizin için uygun ücreti otomatik olarak hesaplayacaktır. İkinci yöntem, satoshi cinsinden mutlak bir toplam veya bayt başına göreceli bir oran olarak belirli bir ücret belirlemenize izin vererek daha hassas bir kontrol sağlar ve ardından tahmini bir onay süresi sağlar.


İleri düzey kullanıcılar için wallet, işleme ince ayar yapmak için çeşitli ayarlar sunar. `Ücrete Göre Değiştir` (RBF) varsayılan olarak etkindir; bu, bir işlemin mempool'da sıkışması durumunda daha yüksek bir ücretle yeniden yayınlayarak hızlandırmanıza olanak tanıyan değerli bir özelliktir. Ayrıca hangi `Harcama Yapılmayan İşlem Çıkışları`ndan (UTXOs) harcama yapılacağını manuel olarak seçebilirsiniz. Bu, birden fazla küçük girdiyi tek bir büyük girdide birleştirdiğiniz bir strateji olan UTXO konsolidasyonu için güçlü bir araçtır. Bu, mevcut işlem için daha fazla ücrete mal olsa da, özellikle ağ ücretlerinin artması bekleniyorsa, gelecekteki işlemlerin ücretlerini önemli ölçüde azaltabilir.


![image](assets/en/15.webp)


Bir alıcının `pj=` parametresi içeren ödeme talebini (bir BIP21 URI) taradığınızda PayJoin otomatik olarak denenir. Ekstra parametre içermeyen düz bir adres yapıştırırsanız, bu özellik etkinleştirilmez. Bu işbirlikçi yöntem, hem göndericiden hem de alıcıdan gelen girdileri birleştirerek gizliliği artırır, ortak girdi sahipliği sezgiselliğini kırar ve bazı durumlarda daha iyi ölçeklendirme ve ücret tasarrufu sağlar.


### Liquid Network'ye gönderme


Liquid Network`, minimum ücretle hızlı, gizli işlemler için tasarlanmıştır. Liquid aracılığıyla para gönderdiğinizde, bu para `Anında Ödemeler Wallet` hesabınızdan çekilir. İşlem basittir: alıcının `Liquid adresini girmeniz veya taramanız yeterlidir.


Adreste bir miktar belirtilmemişse, gönderme ekranında bir miktar belirtmeniz istenecektir. Tutarı BTC, satoshis veya fiat olarak girebilirsiniz. Liquid'nin önemli bir avantajı düşük minimum eşiğidir. on-chain işlemlerinde olduğu gibi, kendi kayıtlarınız için isteğe bağlı bir kişisel not ekleyebilirsiniz. Ödeme talebi zaten bir tutar içeriyorsa, wallet doğrudan onay ekranına ilerleyecektir.


Bir Liquid işlemi için onay ekranında ayrıntıları gözden geçireceksiniz. Ücretler oldukça düşüktür ve işlemin karmaşıklığına göre hesaplanır. Genellikle 0,1 sat/vB civarındadır ve basit bir işlem için sadece 20-40 satoshis tutarındadır (örneğin, 21 Aralık 2025 itibariyle 26 satoshis).


![image](assets/en/16.webp)


### Lightning Network'e gönderme


Alıcı için tutarı ve isteğe bağlı bir notu ayarlamanıza olanak tanıyan bir Yıldırım Address (örneğin `runningbitcoin@rizful.com`) tarayabilir veya sizi doğrudan onay ekranına götüren önceden tanımlanmış bir tutara sahip bir fatura tarayabilirsiniz.


*Minimum tutarların ve ücretlerin geçerli olduğunu unutmayın.*


Bull Bitcoin Wallet, Lightning ödemelerini `Anında Ödemeler Wallet` (Liquid üzerinde) kanalınızdan para çekerek ve bunları `Boltz` üzerinden takas ederek gönderir. Bu hibrit yaklaşım tamamen kendi kendini yönetir ve özel bir Lightning kanalını yönetmenin yüksek on-chain ücretlerinden kaçınır, ancak bir `takas ücreti` ödemeyi gerektirir. En düşük maliyet için, Bull Bitcoin wallet de kullanıyorlarsa doğrudan alıcının Liquid adresine gönderin.


## 🔟 Cüzdanlarınız Arasında Para Aktarma


Bull Bitcoin, Bitcoin`nızı `Secure Bitcoin` wallet ve `Instant Payments Wallet` arasında Liquid Network üzerinde veya `harici bir Wallet`ye taşımanıza olanak tanır. Bir transfer gerçekleştirmek için, `Transfer` bölümüne gitmeniz, kaynak ve hedef cüzdanları seçmeniz, taşımak istediğiniz tutarı girmeniz ve işlemi onaylamanız yeterlidir.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Bull Bitcoin Wallet'unuzu Kurtarma


Bu bölümde, cihazınızı kaybetmeniz, uygulamayı kaldırmanız ya da yeni bir cihaza geçmeniz durumunda Bull Bitcoin Wallet fonlarınıza yeniden nasıl erişim sağlayacağınız açıklanmaktadır. Daha önce açıklandığı gibi, kurtarma için iki temel yöntem vardır: benzersiz `Recoverbull` yöntemini kullanmak ve standart bir `BIP39 seed cümlesi` kullanmak.


### Yöntem 1: Recoverbull


Özet: Wallet yedekleri yerel olarak şifrelenir. Şifrelenmiş dosya bulut depolama alanında veya başka bir cihazda depolanabilir. Şifreleme anahtarı Recoverbull Anahtar Sunucusu tarafından saklanır. Her ikisi de ayrı tutulur ve bir wallet'ü kurtarmak için birleştirilmelidir.


Başlamak için Wallet'ü üzerindeki tüm fonlarla birlikte sileceğim ve wallet'i yeniden yükleyeceğim. Tekrar `Hoş geldiniz ekranına' geleceğiz. Bu kez, `Wallet`ü Kurtar` seçeneğini seçin. Ardından, `Şifreli Kasa` yöntemine gidin, `Varsayılan Anahtar sunucusunu` kullanmayı onaylayın ve yedekleme dosyasını sakladığınız konumu veya `Kasa sağlayıcısını` seçin.


![image](assets/en/18.webp)


Kasanın başarıyla içe aktarıldığını belirtir. Kasanın Şifresini Çöz` düğmesine dokunun ve `PIN`i girin. Bir sonraki ekran `bakiyelerinizi` ve kurtarılan `işlem sayısını` gösterecektir.


![image](assets/en/19.webp)


### Yöntem 2: Tohum İfadesi


Bu yöntem, wallet'inizin ana kurtarma ifadesini kullanır; bu, fonlarınız için nihai yedekleme görevi gören standart 12 kelimelik bir listedir. Belirli bir hizmete veya sunucuya bağlı olmadığı için Bitcoin wallet'i kurtarmanın en evrensel yoludur. Bu ifadeye sahip olduğunuz sürece, Bull Bitcoin Anahtar Sunucusuna erişiminiz olmasa bile wallet'inizi uyumlu herhangi bir cihazda geri yükleyebilirsiniz.


Hoş Geldiniz ekranından `Wallet`u Kurtar`ı seçin. Bu kez, `Fiziksel yedekleme` yöntemini seçin. Uygulama bir kelime tablosu sunacaktır. Dikkatlice 12 kelimelik seed cümlenizin her bir kelimesini doğru sırada seçin. Tek bir hata yanlış bir wallet ile sonuçlanacağından titiz olun.


## 1️⃣2️⃣ Bir Hardware Wallet'nin Bağlanması


En üst düzeyde güvenlik için, birçok Bitcoin kullanıcısı fonlarını `soğuk depoda` saklamayı tercih etmektedir. Bu, Bitcoin'ünüzü kontrol eden `özel anahtarları` asla internete bağlı olmayan bir cihazda tutmak anlamına gelir. Donanımsal wallet (veya İmzalama cihazı) tam da bu amaç için tasarlanmış özel bir fiziksel cihazdır. Anahtarlarınız için dijital bir kasa görevi görür ve hiçbir zaman çevrimiçi bir bilgisayarın veya akıllı telefonun potansiyel tehditlerine maruz kalmamalarını sağlar.


Bir donanım wallet'yı Bull Bitcoin uygulamasına bağlayarak, her iki dünyanın en iyisini elde edersiniz: özel anahtarlarınız için soğuk depolamanın ödün vermeyen güvenliği, bakiyeleri görüntülemek ve işlemleri yönetmek için Bull Bitcoin wallet'nın güçlü özellikleri ve kullanıcı dostu arayüzü ile birlikte. Bu son bölümde, [Coldcard Q] (https://coldcard.com/q) gibi bir donanım wallet'yı Bull Bitcoin wallet'nıza nasıl bağlayacağınızı göstereceğiz. Bu eğitimde Coldcard Q kurulumu derinlemesine ele alınmayacaktır; bu konuda buradan bilgi edinebilirsiniz:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Bir Wallet'nin içe aktarılması


![image](assets/en/26.webp)


İlk olarak, Coldcard Q'nuzun ana menüsünden `Export Wallet` öğesini seçin, ardından `Bull Wallet` öğesini seçin. Coldcard'ınız generate bir QR kodu oluşturacaktır.


![image](assets/en/20.webp)


Bull Bitcoin Wallet'i açın ve `Ayarlar` > `Bitcoin Ayarları` > `wallet'yi içe aktar` seçeneğine gidin ve telefonunuzda `Kart Q` seçeneğini seçin ve donanımınız wallet'nin genel anahtarlarını içe aktarmak üzere bu QR kodunu taramak için `Kamerayı aç` seçeneğine dokunun.


![image](assets/en/21.webp)


### Coldcard Q ile Alma


Bağlı Coldcard Q cihazınızı kullanarak Bitcoin almak için cihazın fiziksel olarak telefonunuza bağlı olmasına gerek yoktur. Bull Bitcoin Wallet, gerekli genel anahtarları zaten içe aktarmıştır ve generate adreslerini kendi başına almasına izin verir.


1. İçe aktarılan Coldcard Q imzalama cihazınızın üzerine dokunun ve `Al` seçeneğini seçin.

2. Uygulama, Coldcard'ınızın wallet'sinden otomatik olarak yeni bir Bitcoin adresi görüntüleyecektir.

3. Para almak için bu adresi kullanın. Bitcoin, işlem sırasında cihaz çevrimdışı olsa bile doğrudan donanım wallet'un anahtarlarına sabitlenecektir.


![image](assets/en/22.webp)


### Coldcard Q ile Gönderme


Coldcard Q ile Bitcoin göndermek, herhangi bir işlemi yetkilendirmek için fiziksel onayınızı gerektirir. Bull Wallet uygulaması işlemi oluşturmak için kullanılsa da, nihai imza yalnızca wallet donanımının kendisinde oluşturulabilir.


Başlamak için, `Coldcard Q` wallet'ünüzü açın ve `Gönder` üzerine dokunun. Ardından, alıcı adresin QR kodunu taramak için `kamerayı açın`. Taradıktan sonra, göndermek istediğiniz "tutarı" girin ve "ücret önceliğini" gerektiği gibi ayarlayın.


Daha fazla seçenek için Gelişmiş Ayarlar bölümüne bakabilirsiniz. Burada, varsayılan olarak etkinleştirilen ve takılan bir işlemi daha sonra hızlandırmanıza olanak tanıyan `Ücretle Değiştir` (RBF) seçeneğini bulacaksınız. Ayrıca, harcamak istediğiniz belirli UTXO'ları manuel olarak seçmenize olanak tanıyan `Coin Control` seçeneğine de sahipsiniz.


Tüm ayrıntıları inceledikten sonra, işlemi hazırlamak için `PSBT`yı Göster`e dokunun.


![image](assets/en/23.webp)


Coldcard Q'nuzdaki `Tara` düğmesine dokunun ve telefonunuzda görüntülenen QR kodunu taramak için kamerasını kullanın. Coldcard ekranı daha sonra size tüm işlem ayrıntılarını gösterecektir. Tutarı, alıcı adresini ve değişiklik adresinizi dikkatlice doğrulayın. Her şey doğruysa, işlemi imzalamak için Coldcard Q üzerindeki `Enter` düğmesine basın. Ardından, imzalanan işlemin QR kodu ekranda görünecektir.


![image](assets/en/24.webp)


Bull wallet'da `Bitirdim` seçeneğine dokunun, ardından `Kamera` düğmesine dokunarak Coldcard Q'nuzdan `imzalı işlem`in QR kodunu tarayın. Bull Wallet şimdi imzalı işlemin bir özet ekranını görüntüleyecektir. Son bir kez gözden geçirin, ardından `İşlemi Yayınla` düğmesine dokunun. Bu, işlemi Bitcoin ağına göndererek işlemi tamamlar ve paranız yola çıkar.


## 🎯 Sonuç


Artık Bull Bitcoin Wallet'deki yolculuğunuzu tamamladınız. Uygulama, güçlü gizlilik ve güvenlik araçlarını parmaklarınızın ucuna getirerek gelişmiş özelliklerin kullanımını kolaylaştırır. Blok zincirindeki işlemlerinizi gizleyen `PayJoin` ve ağ etkinliğinizi meraklı gözlerden gizleyen `Tor entegrasyonu` gibi özelliklerle gizli kalmanıza yardımcı olur. Nihai kontrol isteyenler için, üçüncü taraf sunuculara güvenmeyi bırakmak için `kendi kişisel Bitcoin düğümünüze` bağlanabilir ve özel anahtarlarınızı tamamen çevrimdışı ve güvende tutmak için bir `Donanım wallet` kullanabilirsiniz. Akıllı yedekleme seçenekleri ve Bitcoin, Liquid ve Lightning için kesintisiz destek ile Bull Bitcoin Wallet, fonlarını gizli, güvenli ve tamamen kendi kontrolleri altında tutma konusunda ciddi olan herkes için güçlü, hepsi bir arada bir seçimdir.


## 📚 Bull Wallet Kaynaklar


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Web Sitesi ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)