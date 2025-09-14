---
name: BitcoinVoucherBot
description: Bitcoin'ı gizlilik içinde satın almak için bir Telegram botu
---
![image](assets/cover.webp)


_Bu öğretici yazı yazılmıştır_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_) tarafından


## Giriş


BitcoinVoucherBot, Bitcoinlerin Exchange'de Euro karşılığında satın alınabileceği bir araçtır.


### KYC Işık


Bitcoin için avro değiştirme eylemi, bu konuyu çalışmaya başlamak için ilk ve en temel adımdır, ancak görünüşe göre aynı zamanda en zor ve karmaşık olanıdır. Birçok seçenek olabilir: merkezi Borsalar aracılığıyla Bitcoin sunmak, Bitcoin temalı buluşmalar, arkadaşlar, tanıdıklar ve daha fazlası. Bitcoiner topluluğuna katılıyoruz ve **kişinin gizliliğine daha fazla dikkat etmek için kesinlikle merkezi Borsaların** kullanılmasını öneriyoruz.


Bu seçim daha az kullanışlı olsa da, Borsaların Müşterini Tanı (KYC) yönetmeliğini uyguladığını ve böylece kendilerinden satın alınan her Satoshi'e fiziksel bir konumun yanı sıra bir kimlik atadığını anlamak önemlidir. "Kolaylığın" bazı çarpıcı yan etkileri vardır.


### Nasıl yapmalı?


İşte SEPA transferlerimiz ve Sats satın alımlarımız arasında bir kanal görevi gören bir Telegram botu olan [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) hizmeti geliyor.


### Ön Koşullar


BitcoinVoucherBot'u kullanmaya başlamak için Bot personeline hassas kişisel bilgilerinizi vermenize gerek yoktur. **Yetkilendirme gerekmez**.


Gerekli olan tek şey zaten aktif bir Telegram hesabı ve bir banka hesabıdır. **Not**: Poste Italiane (İtalyan müşteriler için) ile açılan bir hesap veya daha genel olarak şarj edilebilir bir karta atıfta bulunmak uygun değildir.


Telegram sohbetinde bir sipariş hazırlıyoruz, banka havalesi ile ödeme yapıyoruz ve son olarak bot aracılığıyla satın alma nesnesini bilmeyen üçüncü taraf bir şirket tarafından verilen bir kupon alıyoruz.


### Bot aktivasyonu ve menü


Aktivasyon tek seferlik basit bir işlemdir. Telegram'dan _@BitcoinVoucherBot_'u arayın ve Bot'un sohbetine girer girmez, altta büyük bir _Start/Start_ düğmesi göze çarpıyor. Bu işlem Bot'un yanıt vermesine neden olur ve Bot'un kullanabileceği ana komutları içeren bir menü sunar. Dikkatle okumanızı tavsiye ettiğimiz ilk karşılama mesajları da görünür.


**Dikkat**: Orijinal VoucherBot gibi görünen birkaç dolandırıcı var. Telegram üzerinden aramadan emin değilseniz, [resmi siteden](https://www.bitcoinvoucherbot.com/) BitcoinVoucherBot bağlantısına erişin


![image](assets/it/01.webp)


Sol alt köşedeki _Menü_ düğmesine tıklayarak seçenekler görüntülenir: komuta karşılık gelen kelimeye tıklayabilir veya mesaj kutusuna `/` eğik çizgisini ve ardından yazılan komutu yazabilirsiniz.


![image](assets/it/02.webp)


Başlıca operasyonlar şunlardır:




- _/purchase_: gerçek satın alma prosedürüdür. İşlem tamamlandığında, QR Kodu bot tarafından otomatik olarak oluşturulur ve kullanıma hazır hale gelir.
- _/refill_: Bu eğitimin yazıldığı sırada mevcuttu, ancak teknik nedenlerden dolayı bu seçenek daha sonra kaldırılabileceği için bu konuyu ele almayacağız.
- _/swap_: uygun bir Telegram botu veya web üzerinden kullanılabilen takas prosedürünü açar.
- _/ap_: **Sabit Birikim Planı (CAP)** oluşturmanıza olanak tanıyan birikim planı.
- _/lnaddress_: daha sonra göreceğimiz belirli bir prosedür için kendi LN Address'yı bağlamamız isteniyor.
- _/credits_: generate kuponlarına ne kadar kredi kaldığını kontrol etmek için.
- _/myorders_: bot ile verilen siparişleri gösterir (**Uyarı** sistem sadece verilen son 10 siparişi takip eder, tüm geçmişi değil).
- _/fees_: ağ ücretlerini kontrol etmek için bir komut. Bunları değerlendirmek için her zaman en iyisi Mempool.space'e güvenmektir.
- _/support_: ihtiyaç halinde, sorunları destek ekibine bildirmek için kişileri açar.


## Bitcoin Satın Alma Prosedürü


### Siparişin Hazırlanması


Komut menüsünde _/purchase_ öğesine tıklayın


![image](assets/it/03.webp)


Bir dizi fırsat ortaya çıkıyor, ancak biz _BTC Vouchers_'ı seçiyoruz


![image](assets/it/04.webp)


BitcoinVoucherBot, Bitcoin onchain, Lightning ve Liquid satın almanızı sağlar.


Bu aşamada _Onchain & Lightning'i seçin 🔗⚡️_


![image](assets/it/05.webp)


Ekran hızlı bir şekilde değişir ve VoucherBot satın alma değerlerini önerir. Minimum 100,00 €'dan başlayıp 900,00 €'ya kadar çıkmaktadır.


İlk satın alma durumunda, yalnızca 100,00 €, Onchain ve Lightning kupürleri sunulmaktadır. Gizliliği artırmak için _Lightning'i seçmenizi öneririz ⚡️_


![image](assets/it/06.webp)


VoucherBot bize bir ilk seçim yapıldığını ve bunu onaylamak için _Proceed_ seçeneğini seçmemiz gerektiğini bildirir


![image](assets/it/07.webp)


Şimdi ödeme yöntemini seçme meselesi. Transfer banka havalesi ile yapılır **(sadece SEPA kabul edilir)**. VoucherBot alıcı olarak biri İngiltere'de diğeri İsviçre'de olmak üzere iki banka hesabı sağlayan bir şirket önermektedir. Bu eğitimi gerçekleştirmek için İsviçre bankası seçilmiştir


![image](assets/it/08.webp)


Bu noktada, seçilen bankaya transferin başlayacağı IBAN'ımızı girmemiz istenir. Bu bilgiler, botun, yani bir makinenin, insan müdahalesine gerek kalmadan satın alma sürecinin akışını sağlamak için bazı bilgileri bir araya getirmesine izin verecek bir bulmaca oluşturmaya gider.


IBAN mesaj çubuğuna yazılmalı, kontrol edilmeli ve bota gönderilmelidir.


![image](assets/it/09.webp)


VoucherBot ile sohbette artık bir kontrol mesajı görünür.


Her şey doğruysa, _Proceed_ (Devam Et) düğmesine tıklayarak devam edin.


![image](assets/it/10.webp)


### Ödeme


Verileri işlemek için gerekli olan birkaç dakikadan sonra VoucherBot, siparişi tamamlamak için gerekli tüm ayrıntıları içeren bir mesajla yanıt verir. Bankanızın ne istediğine bağlı olarak, ilgili bilgiler şunlardır:




- depozito için gerekli olan `IBAN` ve alıcının Address'ü;
- voucherBot'un ödeme alındığında siparişi tanımasına izin vermek için karşılanması gereken "seçilen tutar" daha önce cutoff aracılığıyla;
- ödemenin nedeni olan `Ödeme nedeni`. **Transferinizin uygun alanına hiçbir şey çıkarmadan veya eklemeden kopyalanmalı ve yapıştırılmalıdır. Ödeme nedeninde bulunan herhangi bir "." veya "-", `beyaz boşluk'** ile değiştirilebilir.
- herhangi bir yardım talebinde bulunurken başvurulacak benzersiz bir `OrderID`.


Daha sonra uygulamanız veya bankanız aracılığıyla ödemeye devam edebilirsiniz. Ödeme banka tarafından kabul edildiğinde, VoucherBot ile sohbette _Ödemeyi bildir_ tuşuna basmayı unutmamak önemlidir. Bu basit işlem, bir ödemenin yolda olduğu konusunda sizi uyarır.


![image](assets/it/11.webp)


VoucherBot çok önemli bir uyarı içeren bir mesajla yanıt verir: *en azından kupon alınana kadar *sohbeti silmeyin**, çünkü siparişi yeniden oluşturmanın ve devam ettirmenin tek yolu budur.


![image](assets/it/12.webp)


---
Lütfen unutmayın:




- sadece SEPA banka havaleleri kabul edilmektedir;
- bekleme süreleri yalnızca bankaların (Bitcoin gibi 7/24/365 çalışmayan) makbuzu nasıl işlediğiyle ilgilidir. Makbuzun alınması birkaç saatten 3 iş gününe kadar sürebilir;
- herhangi bir ihtiyaç için, Bitcoin VoucherBot'un Telegram'da mükemmel bir [destek] (https://t.me/BitcoinVoucherGroup) hizmeti vardır.


---
### İtfa


Ödeme başarılı olur olmaz, Bitcoin VoucherBot kuponu doğrudan sohbete gönderir. Yıldırım kuponu, turuncu bir arka plan üzerine basılmış bir QR kodu şeklindedir.


![image](assets/it/31.webp)


Paraya çevirmek için gereken tüm veriler var:




- gW-17 cinsinden, hizmet ücretleri ve ağ ücretleri hariç olmak üzere banka havalesi ile gönderilene eşdeğer tutar;
- kuponun referans kimliği;
- kuponun kullanılması gereken tarih, aksi takdirde fonların kaybedileceği tarih, yani verildikten 25 gün sonra.


QR kodunu uyumlu bir Wallet Lightning Network'in tarama işleviyle çerçeveleyerek veya QR kodunun altında da gösterilen LNURL aracılığıyla kuponu nakde çevirebilirsiniz.


Bu eğitim için Wallet Of Satoshi kullandık ve _Send_ düğmesiyle etkinleştirilen tarama işlevini kullandık.


![image](assets/it/32.webp)


Cep telefonu kamerası etkinleştirildiğinde, PC'den Telegram'ı açarak sohbetteki QR kodunu çerçeveleyin


![image](assets/it/34.webp)


Devam etmeden önce Wallet Of Satoshi, tutarı içeren ve kupon üzerinde belirtilenle tam olarak eşleşen doğrulama ekranını ve açıklama olarak BitcoinVoucherBot’u gösterir. Kuponu tahsil etmek için _Receive_’a tıklamanız yeterlidir.


![image](assets/it/35.webp)


Wallet Of Satoshi birkaç an boyunca işlem yapar.


![image](assets/it/36.webp)


ve son olarak tahsilat raporlanır ve hemen Wallet bakiyesinde kullanılabilir.


**Wallet of Satoshi saklama cüzdanıdır: kuponu nakde çevirdikten hemen sonra sat'lerin non-custodial bir cüzdana aktarılması tavsiye edilir.**


![image](assets/it/37.webp)


### Onchain kuponu nasıl nakde çevrilir


Sipariş hazırlığında gördüğümüz gibi VoucherBot, Sats'un kendi adını taşıyan kupon seçimiyle doğrudan zincir üzerinde satın alınmasına olanak tanıyor.


**Not**: Sipariş hazırlama ve ödeme değişmez, her zaman aynıdır. Değişen şey, bir zincirleme kuponun nasıl nakde çevrileceğidir.


Siparişi tamamladıktan, ödemeyi yaptıktan, _Ödemeyi bildir_ tuşuna bastıktan ve bankaların transferi aktarmak için teknik süresini bekledikten sonra, VoucherBot kuponu doğrudan sohbete göndererek yanıt verecektir.


Bu kupon da bir QR kodu şeklindedir, ancak ana renk kanarya sarısıdır ve - en önemlisi - açıklamada bunun doğrudan Wallet onchain'inizde nakde çevirdiğiniz bir onchain kuponu olduğu ve para çekme prosedürünü başlatmak için _Redeem on Telegram_ seçeneğine tıklamanız gerektiği iyi bir şekilde açıklanmıştır. Onchain kuponu ayrıca yıldırım kuponu için daha önce görülen bilgileri de içerir:




- gW-32 cinsinden, hizmet ücretleri ve ağ ücretleri hariç olmak üzere banka havalesi ile gönderilene eşdeğer tutar;
- bir kupon kodu;
- kuponun referans kimliği;
- kuponun kullanılması gereken tarih, aksi takdirde fonların kaybedileceği tarih, yani verildikten 25 gün sonra.


![image](assets/it/22.webp)


**UYARI ⚠️:** açıklandığı gibi tıklandığında, başka bir botun açılır penceresi açılır: **Voucher RedeemBot.**


Voucher RedeemBot bu amaçla kullanıma sunulan bir araçtır. İster ilk kullanım olsun, ister önceki siparişler olsun, her yeni kullanımda her zaman _START_ düğmesine tıklamak gerekir.


![image](assets/it/23.webp)


Bu noktada RedeemBot, Voucher Code ve referans ID ile kolayca tanınan zincir üzerindeki kuponu yükler. Ayrıca mesaj yazmak ve botla sohbet etmeye başlamak için çubuğun kilidini açar, bu da aslında bizi Address'ümüzün Wallet'ünü söylemeye davet eder.


**Not**: Bu Address, SegWit tipinde olmalıdır.


![image](assets/it/24.webp)


Bu noktada Wallet'ımızı açıyoruz ve generate bir SegWit Address


![image](assets/it/25.webp)


kopyalıyoruz


![image](assets/it/26.webp)


ve RedeemBot ile sohbete yapıştırın


![image](assets/it/27.webp)


Şimdi kupon kodunun ve RedeemBot'a ilettiğimiz Address'in doğru olduğunu doğrulamak için bir kontrol ekranımız var. Bunu iyi kontrol edelim çünkü _Proceed_ butonuna tıkladığımızda işlem başlar ve örneğin yanlış Address'i iletmişsek bunu tekrar bulmanın bir yolu olmayacaktır.


![image](assets/it/28.webp)


İşlem başlamıştır ve böylece onchain kuponunun Redeem prosedürü sona erer.


![image](assets/it/29.webp)


miktarı ise Wallet'ün tarihinde görülebilir.


![image](assets/it/30.webp)