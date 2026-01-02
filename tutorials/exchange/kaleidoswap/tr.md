---
name: KaleidoSwap
description: KaleidoSwap ile Lightning Network'da RGB varlık ticareti için gelişmiş kılavuz
---

![cover](assets/cover.webp)


KaleidoSwap, RGB Protokolü ile Lightning Network arasındaki boşluğu dolduran sofistike bir açık kaynak masaüstü uygulamasıdır. RGB Lightning Düğümlerini yönetmek, LSPS1 spesifikasyonu aracılığıyla RGB Lightning Hizmet Sağlayıcıları (LSP'ler) ile etkileşim kurmak ve RGB varlıklarının atomik takaslarını gerçekleştirmek için kapsamlı bir arayüz görevi görür.


Gözetim altında olmayan bir çözüm olarak KaleidoSwap, kullanıcıların anahtarları ve verileri üzerinde tam kontrol sahibi olmalarını sağlar. RGB'nın istemci tarafı doğrulama paradigmasından yararlanarak, Bitcoin'ün üzerinde özel ve ölçeklenebilir akıllı sözleşmeler sağlar. Bu eğitim, KaleidoSwap'in gelişmiş özelliklerine dalarak "Renkli" UTXO yönetiminin incelikleri, belirli varlıklar için kanal likiditesi ve alıcı-yapıcı ticaret modeli konusunda size rehberlik ederek bu güçlü merkezi olmayan borsa protokolünü tam olarak kullanabilmenizi sağlar.


## Kurulum


KaleidoSwap, büyük işletim sistemleri için önceden oluşturulmuş ikili dosyalar sağlar, ancak ileri düzey kullanıcılar için kaynaktan derleme, özel yapılandırmalarınızla en son kodu çalıştırmanızı sağlar.


### İkilileri İndir


İşletim sisteminiz için en son sürümü [resmi web sitesi](https://kaleidoswap.com/) veya [GitHub sürümleri sayfası](https://github.com/kaleidoswap/desktop-app/releases) adresinden indirebilirsiniz.


### Kurulum Yöntemleri


1.  **Windows**: .exe` yükleyicisini indirin ve çalıştırın.

2.  **macOS**: .dmg` dosyasını indirin, açın ve KaleidoSwap'i Uygulamalar klasörünüze sürükleyin.

3.  **Linux**: .AppImage` veya `.deb` dosyasını indirin ve kurun/çalıştırın.



## Düğüm Kurulum Seçenekleri


KaleidoSwap'i ilk başlattığınızda, **Bağlantı Ekranı** ile karşılaşacaksınız. Bu, ortamınızı yapılandırmanın ilk adımıdır.


![Node Selection Screen](assets/en/01.webp)


RGB Lightning Network'ye nasıl bağlanacağınızı seçmelisiniz. Bu seçim kontrol ve gizlilik seviyenizi etkiler.


### Seçenek 1: Yerel Düğüm (Kendi Kendine Saklama için Önerilen)


**Tam kontrol ve gizlilik** için, doğrudan makinenizde bir düğüm çalıştırın, aşağıdaki avantajlara bakın:


- Kendi Kendine Velayet**: Anahtarlar sizde. Hiçbir üçüncü taraf fonlarınızı donduramaz veya işlemlerinizi sansürleyemez.
- Gizlilik**: Verileriniz cihazınızda kalır.
- Bağımsızlık**: Harici hizmet sağlayıcılara bağımlılık yok.


Yerel Düğüm** öğesini seçerseniz, yeni bir wallet oluşturabileceğiniz veya mevcut olanı geri yükleyebileceğiniz kurulum ekranına yönlendirilirsiniz.


![Local Node Setup Screen](assets/en/02.webp)


### Seçenek 2: Uzak Düğüm


Uzak bir RGB Lightning Node'a bağlanın (bir VPS'de veya barındırılan bir sağlayıcıda kendi kendine barındırılan).


- Avantajlar**: Yerel kaynak kullanımı yok, 7/24 kullanılabilirlik.
- Değiş tokuş**: Ana bilgisayara güvenmeyi veya uzak bir sunucuyu yönetmeyi gerektirir.


![Remote Node Setup Screen](assets/en/03.webp)


**Bitcoin ve RGB'nin sansüre dirençli özelliklerinden tam olarak faydalanmak için kendi düğümünüzü (yerel olarak (Seçenek 1) ya da uzak bir düğümü kendiniz barındırarak) çalıştırmanızı şiddetle tavsiye ederiz.


## Wallet Oluşturma


KaleidoSwap hem Bitcoin hem de RGB varlıklarını yönetir. wallet oluşturma işlemi, on-chain fonlarınızı ve Lightning kanal durumlarınızı güvence altına alan bir anahtar deposu başlatır.


İşte ayrıntılı süreç:

1. KaleidoSwap'i açın ve **Local Node** öğesini seçin.

2. Yeni Wallet Oluştur** üzerine tıklayın.

3. **Hesap Kurulumu**: Bir **Hesap Adı** girin ve **Ağ** seçin (örneğin, Bitcoin Mainnet, Testnet, Signet).

4. **Gelişmiş Yapılandırma** (İsteğe Bağlı): Uzman bir kullanıcıysanız, "Gelişmiş Ayarlar" altında özel RPC uç noktalarını, Dizin Oluşturucu URL'lerini veya Proxy ayarlarını yapılandırabilirsiniz.

5. Devam** düğmesine tıklayın.

6. **Parola**: wallet dosyanızı yerel olarak şifrelemek için güçlü bir parola belirleyin.

7. **Kurtarma İfadesi**: seed cümlenizi yazın ve güvenli bir şekilde saklayın.


    - Kritik**: Bu ifade on-chain fonlarınızı ve düğüm kimliğinizi kurtarmak için gereklidir.
    - Uyarı**: **Yıldırım kanalı durumları yalnızca seed'dan tam olarak kurtarılamaz**. Kanallarda kilitli fonları kurtarmak için Statik Kanal Yedekleri (SCB) de bulundurmalısınız.


![Wallet Creation Screen](assets/en/04.webp)



## Gösterge Tablosuna Genel Bakış


wallet'niz oluşturulduktan sonra, ana **Gösterge Panosuna** yönlendirileceksiniz.


![KaleidoSwap Dashboard](assets/en/05.webp)


not: Yukarıdaki ekran görüntüsü halihazırda fonlanmış ve aktif kanalları olan bir wallet'i göstermektedir. Yeni bir wallet, siz ona para yatırana kadar sıfır bakiye gösterecek ve aktif kanalları olmayacaktır._


## Wallet'unuzun Finansmanı


RGB varlıkları ile işlem yapmak için wallet'ünüzü fonlamanız gerekir. KaleidoSwap, on-chain işlemleri veya Lightning Network aracılığıyla hem Bitcoin hem de RGB varlıklarının yatırılmasını destekler.


### Bitcoin'in Yatırılması


1. Hızlı Eylemler menüsünde **Yatır** öğesine tıklayın.

2. Varlık listesinden **BTC** öğesini seçin.


![Select BTC Asset](assets/en/06.webp)


3. Para yatırma yönteminizi seçin: **Zincirleme** veya **Yıldırım**.


![BTC Deposit Options](assets/en/07.webp)



- Zincir üzerinde**: Bitcoin'yı başka bir wallet'den göndermek için QR kodunu tarayın veya adresi kopyalayın.
- Yıldırım**: İstediğiniz tutar için bir fatura oluşturun.


![BTC On-chain Deposit](assets/en/08.webp)


### RGB Varlıklarının ve Renkli UTXO'ların Yatırılması


RGB varlıklarını (USDT gibi) almak için, "renklendirilecek" (bir varlık atanacak) belirli UTXO'lara ihtiyacınız vardır.


1. Para Yatır** seçeneğine tıklayın ve RGB varlığını seçin (örneğin USDT). **Önemli**: Düğümünüz bu varlığı **ilk kez** alıyorsa, **Varlık Kimliği alanını boş bırakın**. Bilinmeyen bir varlık için bir kimlik girmek, düğümün varlığı henüz tanımadığı için hata vermesine neden olacaktır.

2. Zincirleme** veya **Yıldırım** seçeneklerinden birini seçin.


![USDT Deposit Options](assets/en/09.webp)


#### Zincirleme Alım Modları: Tanık vs Kör


RGB varlıklarını on-chain alırken, iki gizlilik moduna sahip olursunuz:



- Kör Alım (Gizlilik için önerilir)**: Gönderene bir "blinded" UTXO sağlarsınız. Göndericiden varlıkları sahip olduğunuz mevcut bir UTXO'e göndermesini istiyorsunuz, ancak gerçek UTXO tanımlayıcısını gizliyorsunuz. Bu daha iyi gizlilik sunar.
- Tanık Alımı**: Standart bir Bitcoin adresi veriyorsunuz. Göndericiden varlıkları bu adrese göndererek sizin için *yeni* bir UTXO oluşturmasını istiyorsunuz. Bu, RGB varlıklarının doğrudan işlem tarafından oluşturulan yeni UTXO'ya eklenmesini sağlar.


#### Yıldırım Depozitosu


Lightning depozitoları için generate bir fatura göndermeniz yeterlidir. RGB varlığı açık kanallarınız üzerinden size yönlendirilecektir.


![USDT Lightning Invoice](assets/en/10.webp)



## RGB Varlıkları ile Kanal Açma


RGB varlıklarını Lightning Network üzerinden yönlendirmek için yeterli likiditeye ve varlık tahsisine sahip bir kanala ihtiyacınız vardır. Başlamanın en kolay yolu bir LSP'den (Lightning Service Provider) **Kanal** satın almaktır.


### Kaleido LSP'den Kanal Satın Alma


1. Kanallar** sekmesine gidin. "Kanal Aç" (manuel) veya "Kanal Satın Al" (LSP) seçeneklerini göreceksiniz.

2. Satın Alma Kanalı'na** tıklayın.


![Channels Dashboard](assets/en/11.webp)


3. **LSP'ye bağlan**: Uygulama varsayılan Kaleido LSP'ye bağlanacaktır. Bu sağlayıcı gelen likidite sunar ve RGB varlık yönlendirmesini destekler.


![Connect to LSP](assets/en/12.webp)


4. **Kanalı Yapılandır**:


    - Kapasite**: Kanal için toplam Bitcoin kapasitesini seçin.
    - RGB Tahsisi**: Alabilmek veya gönderebilmek istediğiniz RGB varlığını (örn. USDT) seçin. LSP, kanalın bu varlığı destekleyecek şekilde yapılandırılmasını sağlayacaktır.


![Configure Channel](assets/en/13.webp)



    - RGB Tahsisi**: Alabilmek veya gönderebilmek istediğiniz RGB varlığını (örn. USDT) seçin. LSP, kanalın bu varlığı destekleyecek şekilde yapılandırılmasını sağlayacaktır.


![RGB Allocation](assets/en/14.webp)


5.  **Ödeme**: Kanalı açmak ve likidite sağlamak için LSP'ye bir ücret ödemeniz gerekir. Ödemeyi **Lightning** veya **On-chain** Bitcoin kullanarak yapabilirsiniz. Ödeme dahili KaleidoSwap wallet'inizden veya harici bir wallet'den yapılabilir.


![Complete Payment](assets/en/15.webp)


6. Ödeme onaylandıktan sonra LSP kanal açma işlemini başlatacaktır. Bir **Sipariş Tamamlandı** ekranı göreceksiniz.


![Order Completed](assets/en/16.webp)


7. Blok zincirinde onaylandıktan sonra, kanalınız aktif olacak ve RGB transferleri için hazır olacaktır.



## Ticaret: Alıcı-Alıcı Modeli


KaleidoSwap'in alım satım motoru bir **Piyasa Yapıcı modeli** üzerinde çalışır. Varlıkları bir eş ile manuel olarak takas edebilir veya bir Piyasa Yapıcı (LSP) kullanabilirsiniz.


### Bir Piyasa Yapıcı (LSP) ile Takas


Bu, işlem yapmanın en yaygın yoludur. LSP (**Maker**) tarafından sağlanan mevcut likiditeye karşı emirleri yerine getirerek **Taker** olarak hareket edersiniz.


1. Ticaret** sekmesine gidin ve **Piyasa Yapıcı** öğesini seçin.

2. **Tutar Girin**: Göndermek istediğiniz Bitcoin miktarını (veya almak istediğiniz varlığı) girin. Arayüz tahmini döviz kurunu ve ücretleri gösterecektir.


![Market Maker Swap](assets/en/17.webp)


3. **Takası Onaylayın**: Döviz kuru ve alacağınız tam miktar da dahil olmak üzere ayrıntıları gözden geçirin. Takası Onayla** seçeneğine tıklayın.


![Confirm Swap](assets/en/18.webp)


4. **İşlem**: Takas işlemi Lightning Network üzerinde atomik olarak gerçekleştirilir. Takasın beklemede olduğunu gösteren bir durum ekranı göreceksiniz.


![Swap Pending](assets/en/19.webp)


5. **Başarılı**: HTLC'ler kapatıldıktan sonra takas tamamlanır ve varlıklar sizin kanalınızda olur.


![Swap Success](assets/en/20.webp)



## Geliştirici API


KaleidoSwap'in üzerine inşa eden geliştiriciler için uygulama, destekleyen bir API sunar:



- RGB LSPS1**: Otomatik likidite hizmetleri için.
- Swap API**: Programatik ticaret ve piyasa yapıcılığı için.
- WebSocket**: Gerçek zamanlı piyasa veri abonelikleri için.


Tüm uç noktalar ve teknik özellikler için [API Dokümantasyonu]'na (https://docs.kaleidoswap.com/api/introduction) bakın.


## Sonuç


KaleidoSwap, Lightning Network üzerinde RGB varlıklarının gizliliğinden ve ölçeklenebilirliğinden yararlanmanızı sağlar. Renkli UTXO'ları ve kanal varlık tahsisini anlayarak, bu güçlü merkezi olmayan değişim protokolünden tam olarak yararlanabilirsiniz.