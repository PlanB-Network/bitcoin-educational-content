---
name: Blitz Wallet
description: En basit Bitcoin cüzdanı.
---

![cover](assets/cover.webp)

Bir Bitcoin cüzdanı seçerken kullanıcı deneyimi belirleyici faktörlerden biridir. Bu rehberde, sadeliği yaklaşımının merkezine koyan bir cüzdan olan Blitz Wallet'ı tanıtıyoruz: **Spark** protokolünün entegrasyonu sayesinde Blitz, anlık ödemeler ve teknik yönetim gerektirmeden piyasadaki en basit ve en kapsamlı Bitcoin cüzdanlarından birini sunuyor.

## Blitz Wallet Nedir?

Blitz Wallet, egemenliğinize ve akıcı, sezgisel bir kullanıcı deneyimine odaklanan **self-custodial** ve **open source** bir Bitcoin cüzdanıdır.

[Blitz Wallet](https://blitz-wallet.com/), Android (Play Store) ve iOS (App Store) üzerinde kullanılabilen bir mobil uygulamadır.

Ödeme kanalları ve gelen likidite yönetimi gerektiren geleneksel Lightning cüzdanlarının aksine, Blitz Wallet bu teknik karmaşıklıkları ortadan kaldırmak için **Spark protokolüne** dayanır. Sonuç: herhangi bir ön yapılandırma olmadan, ilk satoshi alındığı andan itibaren anlık ödemeler. Blitz'in amacı, fonlarınızın self-custody'sinden asla ödün vermeden, bitcoin ödemelerini klasik bir ödeme uygulaması kadar basit hale getirmektir.

Blitz Wallet ayrıca `kullanici@alan.com` formatında **okunabilir adresleri** de destekler (LNURL aracılığıyla), bu sayede her işlemde uzun invoice'larla veya QR code'larla uğraşmadan, e-posta gönderir gibi kolayca bitcoin gönderebilirsiniz.

## Spark Protokolünü Anlamak

Uygulamaya geçmeden önce, Blitz Wallet'ın arka planında çalışan teknolojiyi anlamak faydalı olacaktır: **Spark protokolü**.

### Spark Nedir?

Spark, Lightspark ekibi tarafından geliştirilen, Bitcoin üzerine inşa edilmiş open source bir üst katman protokolüdür. Bitcoinlerinizin self-custody'sini koruyarak anlık ve düşük maliyetli işlemler yapmanızı sağlar.

İki taraf arasındaki **ödeme kanallarına** dayanan Lightning Network'ün aksine, Spark **statechain** (durum zinciri) adlı bir teknoloji kullanır. Temel ilke şudur: her işlemde bitcoinleri blockchain üzerinde taşımak yerine, Spark **harcama hakkını** bir kullanıcıdan diğerine on-chain hareketi olmadan aktarır.

### Nasıl Çalışır?

Spark'ı sezgisel olarak anlamak için, Spark üzerinde bir bitcoin harcamanın iki parçalı bir bulmacayı tamamlamayı gerektirdiğini hayal edelim:
- Bir parça kullanıcıya aittir (örneğin, Alice).
- Diğer parça **Spark Entity (SE)** adı verilen bir operatör grubuna aittir.

Bitcoinleri yalnızca birbiriyle eşleşen iki parçanın birleşimi harcayabilir.

Alice bitcoinlerini Bob'a göndermek istediğinde şunlar olur: Bob ile SE arasında ortaklaşa yeni bir bulmaca oluşturulur. Bulmaca aynı şeklini korur, ancak onu oluşturan parçalar değişir. Artık SE'nin parçasıyla eşleşen Bob'un parçasıdır. Alice'in eski parçası kullanılamaz hale gelir, çünkü SE kendi eşleşen parçasını yok etmiştir. Bitcoinlerin mülkiyeti el değiştirmiştir, **blockchain üzerinde herhangi bir işlem yapılmadan**.

Bob daha sonra aynı işlemi tekrarlayarak bu bitcoinleri Carol'a gönderebilir ve bu böyle devam eder. Her transfer, on-chain fon hareketi yerine bulmaca parçalarının değiştirilmesiyle çalışır.

### Neden Güvenli?

Haklı bir soru ortaya çıkıyor: SE eski parçasını gerçekten yok etmezse ne olur?

Spark Entity tek bir varlık değildir: bağımsız operatörlerden oluşan bir gruptur. SE'nin parçası asla tek bir operatör tarafından tutulmaz. Bulmacanın değiştirilmesi birden fazla operatörün işbirliğini gerektirir. Eski bir bulmacanın yeniden etkinleştirilmesini önlemek için bir transfer sırasında **tek bir dürüst operatörün olması yeterlidir**. Hiçbir tek operatör gizlice eski bir aktif bulmacayı saklayamaz veya daha sonra yeniden oluşturamaz.

Ayrıca Spark, tek taraflı çıkış mekanizması içerir: bitcoinlerinizi SE'nin işbirliği olmadan her zaman on-chain olarak geri alabilirsiniz. Bu yedek mekanizma Spark mimarisinin ayrılmaz bir parçasıdır ve fonlarınıza erişmek için asla ağa bağımlı olmadığınızı garanti eder.

### Spark ve Lightning Network Karşılaştırması

Spark ve Lightning rakip değildir: **birbirini tamamlayıcıdır**. Blitz Wallet her ikisini de entegre eder, böylece her birinin avantajlarından yararlanabilirsiniz.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Teknoloji**                 | Statechains (durum zincirleri) | Ödeme kanalları     |
| **Kanal yönetimi**            | Gerekli değil                | Gerekli               |
| **Gelen likidite**            | Gerekli değil                | Gerekli               |
| **Anlık işlemler**            | Evet                         | Evet                  |
| **Self-custody**              | Evet                         | Evet                  |
| **Lightning uyumluluğu**      | Evet (atomic swaps ile)      | Doğal                 |

Lightning Network, anlık ödemeler için mükemmel bir protokol olmaya devam etmektedir, ancak yeni başlayanları caydırabilecek teknik kısıtlamalar (kanal yönetimi, gelen likidite, çevrimiçi düğüm...) getirir. Spark, Lightning ile uyumlu kalarak bu kısıtlamaları ortadan kaldırır.

## Kurulum ve Yapılandırma

Bu rehberde Blitz Wallet'ın Android sürümünü temel alıyoruz, ancak aşağıda sunulan tüm işlemler iOS için de geçerlidir.

![installation](assets/fr/01.webp)

Blitz Wallet self-custody bir cüzdan olduğundan, **yeni bir cüzdan oluşturma** veya mevcut bir cüzdanın **kurtarma ifadesini içe aktarma** (12 veya 24 kelime) seçenekleriniz vardır.

Burada yeni bir cüzdan oluşturmayı tercih ediyoruz. Kurtarma ifadenizin yedeklenmesine ilişkin önerilerimizi aşağıda bulabilirsiniz:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **ONEMLI** : Bu 12 veya 24 kurtarma kelimesi **bitcoinlerinize erişmenin tek anahtarıdır**. Blitz self-custodial bir cüzdandır: ne Blitz ne de Spark kurtarma ifadenize veya fonlarınıza erişemez. Bu kelimeleri kaybederseniz, bitcoinlerinize erişimi kalıcı olarak kaybedersiniz. Bunları kimseyle paylaşmayın: bu kelimelere sahip olan herkes bitcoinlerinizi harcayabilir.

Ardından cüzdanınıza erişimi güvence altına almak için bir **PIN kodu** oluşturun.

![setup-wallet](assets/fr/02.webp)

## Blitz ile Başlangıç

Blitz ile işlem yapmak, diğer Bitcoin cüzdanlarının çoğundan daha sezgiseldir. Arayüz minimalisttir ve üç ana eyleme odaklanır: gönder, tara ve al.

### Bitcoin Alma

Blitz cüzdanınıza bitcoin almak için **"Aşağı ok"** (↓) simgesine tıklayın, almak istediğiniz satoshi miktarını girin, isteğe bağlı bir açıklama ekleyin; ardından cüzdan göndericinizle paylaşabileceğiniz bir fatura (invoice) oluşturacaktır.

⚠️ **NOT** : Satoshi (veya "sat"), bitcoinin en küçük birimidir: **1 bitcoin = 100.000.000 satoshi**.

Blitz Wallet'ın özelliklerinden biri, Bitcoin ekosistemindeki birden fazla ağ ve protokolü desteklemesidir:

- **Lightning Network** : Çok düşük ücretlerle anlık mikro ödemeler yapmayı sağlayan Bitcoin üst katmanlarından biri. Günlük küçük tutarlar için idealdir.

- **Bitcoin (on-chain)** : Maksimum güvenlik ve kesinliğin öncelikli olduğu daha büyük tutarlardaki işlemler için uygun olan Bitcoin protokolünün ana blockchaini.

- **Liquid Network** : Blockstream tarafından geliştirilen ve Liquid Bitcoin (L-BTC) kullanarak hızlı ve gizli işlemler yapmayı sağlayan bir Bitcoin sidechain'i (yan zincir).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Varsayılan olarak Blitz bir Lightning faturası oluşturur, ancak **"Choose format"** (Format seç) düğmesine tıklayarak satoshilerinizi almak istediğiniz ağı seçebilirsiniz.

![receive-sats](assets/fr/03.webp)

### Kişi Oluşturma

Blitz Wallet, kişi sistemi sayesinde tekrarlayan bitcoin gönderimlerini kolaylaştırır.

**Contacts** menüsünde, sık etkileşimde bulunduğunuz Blitz kullanıcı adlarını veya Lightning adreslerini (LNURL) kaydedebilirsiniz.

Böylece her seferinde QR code taramak veya manuel olarak adres girmek zorunda kalmadan, bu adreslere birkaç tıklamayla satoshi gönderebilirsiniz.

### Bitcoin Gönderme

Klasik bitcoin gönderme yöntemlerinin (QR code tarama, manuel adres girişi) yanı sıra Blitz birkaç pratik seçenek sunar:

- **Görüntüden** (*From Image*) : Fotoğraf galerinizden bir QR code içe aktarın.
- **Panodan** (*From Clipboard*) : Daha önce kopyalanmış bir adresi veya faturayı yapıştırın.
- **Manuel giriş** (*Manual Input*) : Doğrudan bir Bitcoin adresi, Lightning faturası veya okunabilir adres girin (örneğin `kullanici@walletofsatoshi.com`).
- **Kişilerinizden** : Birkaç tıklamayla göndermek için önceden kaydedilmiş bir alıcı seçin.

**Wallet** menüsünde **"Yukarı ok"** (↑) düğmesine tıklayın, gönderme yönteminizi seçin, gönderilecek tutarı girin, bir açıklama ekleyin ve işlemi onaylayın.

Gönderim yapmak için gereken minimum tutar şu anda **1.000 satoshi**'dir.

![send-bitcoin](assets/fr/05.webp)

## Blitz Mağazası

Bitcoin transfer işlemlerinin ötesinde, Blitz Wallet doğrudan uygulama içinden bitcoinlerinizi harcayarak dijital hizmetler satın alabileceğiniz bir mağaza içerir.

Ana menüden mağazaya erişmek için **Store** sekmesine tıklayın. Ayrıca burada, doğrudan bitcoin ile dünya genelinde binlerce perakendeciden hediye kartı satın almanızı sağlayan **Bitrefill** platformuna da erişim bulacaksınız.

- **Yapay zeka** : En son üretken yapay zeka modellerine (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) erişin ve kredilerinizi doğrudan satoshi ile ödeyin. İhtiyaçlarınıza göre çeşitli paketler mevcuttur (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonim SMS** : Kişisel telefon numaranızı ifşa etmeden dünyanın her yerine SMS gönderin ve alın. Hizmet, gönderilen her mesaj için satoshi olarak faturalandırılır.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard** : Blitz mağazasından doğrudan bitcoin ile ödeyerek bir WireGuard VPN aboneliğine (haftalık, aylık veya üç aylık) abone olarak çevrimiçi gizliliğinizi koruyun. Yararlanmak için cihazınıza WireGuard istemci uygulamasını indirmeniz yeterlidir.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet Perde Arkasında: Daha Derine İnmek

Blitz Wallet'ın kullanım kolaylığının arkasında, Bitcoin ekosisteminin birden fazla katmanını birleştiren iyi düşünülmüş bir teknik mimari bulunmaktadır.

### Bakiyenizin Dağılımı

Blitz Wallet, ihtiyaçlara göre fonlarınızı farklı protokoller arasında dağıtarak bakiyenizi şeffaf bir şekilde yönetir. Bakiyeniz 500.000 satoshinin altında olduğunda, Blitz size akıcı bir deneyim sunmak ve küçük tutarlarla bile Lightning Network üzerinde işlem yapmanızı sağlamak için **Liquid Network** ve atomik takaslar (*atomic swaps*) kullanır.

Bu yaklaşım, altta yatan mekanizmaları anlamalarına gerek kalmadan yeni kullanıcılar için basit bir başlangıç sağlar. Bakiyenizin farklı katmanlar arasındaki dağılımını **Ayarlar > Balance Info** menüsünden görüntüleyebilirsiniz.

![balance](assets/fr/09.webp)

### Lightning Modu (isteğe bağlı)

Varsayılan olarak, Blitz Wallet teknik yapılandırma gerektirmeden akıcı bir deneyim sunmak için Liquid Network ve Spark protokolünü kullanır. Ancak Blitz, bakiyeniz **500.000 satoshi** (0,005 BTC) seviyesine ulaştığında otomatik olarak bir ödeme kanalı açacak olan **Lightning modunu** etkinleştirmenize olanak tanır.

Lightning modunu etkinleştirmek için **Ayarlar** bölümüne gidin, ardından **Teknik Ayarlar** kısmında **Node Info** seçeneğine tıklayın.

![enable-lightning](assets/fr/10.webp)

Spark protokolü sayesinde bu etkinleştirme **isteğe bağlıdır**: Spark, kanal açmaya veya gelen likidite yönetmeye gerek kalmadan zaten Lightning uyumlu ödemeler yapmanızı sağlar. Doğal Lightning modu, uygulama içinde kendi Lightning düğümüne sahip olmak isteyen ileri düzey kullanıcılar için faydalı olmaya devam etmektedir.

### Satış Noktası (PoS)

Blitz Wallet, tüccarların doğrudan uygulama üzerinden bitcoin ödemelerini kabul etmesini sağlayan bir **satış noktası** özelliği içerir.

**Ayarlar > Point-of-sale** menüsünde şunları yapılandırabilirsiniz:

- Mağazanızın benzersiz tanımlayıcısı
- Fiyatların gösterileceği yerel itibari para birimi
- Çalışanlarınız için talimatlar
- Müşterileriniz için bahşiş seçeneği

Müşterilerinizin oluşturulan QR code'u tarayarak anında bitcoin ödemelerini gerçekleştirmeleri yeterlidir.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Bu rehberin hazırlanmasında kullanılan kaynaklar:
- [Breez](https://breez.technology/) Technology blogu: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
