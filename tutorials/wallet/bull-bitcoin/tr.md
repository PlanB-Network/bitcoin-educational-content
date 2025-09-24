---
name: Bull Bitcoin Wallet
description: Wallet Bull Bitcoin'nin nasıl kullanılacağını öğrenin
---

![cover](assets/cover.webp)



Bu kılavuz sizi Bull Bitcoin Mobile'ın kurulumu, yapılandırılması ve kullanımına götürür. Üç ağda nasıl para alacağınızı ve göndereceğinizi öğreneceksiniz: onchain, Liquid ve Lightning ve Bitcoin'ünüzü bir ağdan diğerine nasıl aktaracağınızı. Eklerde kaynaklar ve iletişim bilgileri, arka plan bilgileri ve teknik kavramların kısa açıklamaları yer almaktadır.



## Giriş



**Bull Bitcoin** ([hesap oluştur](https://app.bullbitcoin.com/registration/orangepeel)) tarafından geliştirilen **Bull Bitcoin Mobile**, bir **kendi kendine emanet** Bitcoin Wallet'dur, yani üçüncü bir tarafa bağlı olmadan özel anahtarlarınız ve dolayısıyla fonlarınız üzerinde tam kontrole sahipsiniz. Açık kaynaklı ve Cypherpunk felsefesine dayanan bu Wallet, basitlik, gizlilik ve ağlar arası takas ve PayJoin desteği gibi gelişmiş özellikleri bir araya getirir. Bitcoinlerinizi üç ağ üzerinde yönetmenizi sağlar: **Bitcoin onchain**, **Liquid** ve **Lightning**, her biri belirli kullanımlara göre uyarlanmıştır.



### Kalkınma bağlamı



Wallet büyük bir zorluğa yanıt vermektedir: Bitcoin ağ ücretleri küçük ödemeler için veya kendi kendine barındırılan küçük Lightning kanalları açmak için uygun değildir. Wallet Bull Bitcoin Mobile, 3 büyük Bitcoin ağına güvenirken kendi kendine emanet bir çözüm sunar:





- **Bitcoin ağı (onchain)**: Ücretlerin oransal olarak ihmal edilebilir olduğu UTXO'ların ve büyük değerli işlemlerin orta ila uzun vadeli depolanması için idealdir.
- **Liquid Network**: Hızlı (~2 dakika), daha gizli (gizli miktarlar), düşük maliyetli işlemler için tasarlanmıştır, küçük miktarlar biriktirmek veya gizliliğinizi korumak için mükemmeldir.
- **Lightning** ağı: Anında, düşük maliyetli ödemeler için optimize edilmiş, küçük ve orta değerli günlük işlemler için uygundur.



Örneğin Bull Bitcoin Mobile ile **Liquid** veya **Lightning** portföylerinde küçük miktarlarda birikim yapabilir ve ardından önemli bir miktara ulaştığınızda :





- Liquid ve/veya Lightning upstream ile geliştirilmiş gizlilik ve tek bir işlem için onchain ücretleri ile güvenli orta veya uzun vadeli depolama için onchain ağına aktarım



### Sürekli evrim



Wallet sürekli olarak gelişmektedir, bu nedenle bu eğitim ile güncel uygulamanız arasında tutarsızlıklar bulursanız şaşırmayın.




- Örneğin, 19/07/2025 tarihinden itibaren, Exchange'de [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel) mevcut olan bu seçenekler yakında birleşik bir deneyim için entegre edileceğinden, **"Al / Sat / Öde "** düğmeleri uygulamada görünür ancak gri renktedir. Kullanımları tamamen isteğe bağlı kalacaktır. Diğer birçok gelişme devam etmekte veya planlanmaktadır: çoklu Wallet yönetimi, passphrase, donanım cüzdanlarıyla uyumluluk ...
- BullBitcoin GitHub]'da (https://github.com/orgs/SatoshiPortal/projects/49) güncel konulara ve gelecek gelişmelere göz atabilirsiniz. Proje %100 açık kaynaklı ve "halka açık" olduğundan, önerilerinizi ve karşılaştığınız hataları da bize gönderebilirsiniz.




## 1. Ön Koşullar



**Bull Bitcoin Mobile** cihazını kullanmaya başlamadan önce, aşağıdaki öğelere sahip olduğunuzdan emin olun:





- **Uyumlu Akıllı Telefon**: Bir **iOS** (iPhone veya iPad) veya **Android** cihazı
- İnternet bağlantısı
- Güvenli yedekleme medyası**: Kurtarma cümlenizi** (12 kelime) kağıt veya metal üzerine yazın ve güvenli bir yerde saklayın.
- **Temel bilgi**: Bitcoin kavramlarının (adresler, işlemler, ücretler) asgari düzeyde anlaşılması yararlıdır, ancak bu eğitim yeni başlayanlar için her adımı açıklamaktadır.



## 2. Kurulum





- **Başvuruyu indirin** :
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Android cihazlar için uygulama mağazasından indirin**
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Android cihazlar için APK'yı doğrudan indirin**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **Apple cihazları için TestFlight aracılığıyla indirin**
 - Sahte uygulamalardan kaçınmak için geliştiricinin adını (Bull Bitcoin) kontrol edin.
 - İndirilen sürümün GitHub'da belirtilen en son kararlı sürüme karşılık geldiğinden emin olun.
 - Bull Bitcoin Mobile **açık kaynaklıdır**. Kodu görüntülemek için: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Uygulamayı yükleyin




## 3. İlk yapılandırma



### 3.1 Uygulamayı başlatın :



Uygulama, her iki portföy için de 12 kelimelik benzersiz bir kurtarma ifadesi kullanır:




- **güvenli Bitcoin Wallet**: Bitcoin ağındaki işlemler için (onchain)
- **Anında Ödemeler Wallet**: Liquid ve Lightning ağlarında anlık işlemler için



Açılışta, mevcut bir kurtarma ifadesini içe aktarmanız veya yeni bir Wallet oluşturmanız istenir:



![image](assets/fr/02.webp)



### 3.2 Kurtarma ifadesi :



Mevcut bir Wallet'i yeniden kullanmak istiyorsanız, "**Wallet'i Kurtar**" seçeneğine tıklayın ve kurtarma ifadenizin 12 kelimesini doldurun.



Aksi takdirde, "**Yeni Wallet** Oluştur" üzerine tıklayın:




- Kurtarma ifadenizi son derece dikkatli bir şekilde yazın. Kağıt veya metal üzerine yazın ve güvenli bir yerde saklayın (kiralık kasa, çevrimdışı konum). Bu ifade, cihazınızın kaybolması veya uygulamanın silinmesi durumunda bitcoinlerinize erişmek için tek yolunuzdur.
- Bu ifadeye sahip herhangi birinin tüm bitcoinlerinizi çalabileceğini de unutmamak gerekir. Asla dijital olarak saklamayın:
 - Ekran görüntüsü yok
 - Bulut, e-posta veya mesajlaşma yedeklemesi yok
 - Kopyala/yapıştır yok (panoya kaydetme riski)



**! Bu nokta kritiktir**. Daha fazla yardım için :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Erişimin güvence altına alınması :





- Ayarlara gidin ve ardından **PIN Kodu** üzerine tıklayın.
- Uygulamaya erişimi korumak için sağlam bir **PIN kodu** oluşturun.
- Bu adım isteğe bağlıdır, ancak telefonunuza erişimi olan herhangi birinin Wallet'ünüze erişmesini önlemek için şiddetle tavsiye edilir.



![image](assets/fr/03.webp)



### 3.4 Kişisel bir düğüme bağlantı (isteğe bağlı):



Wallet BullBitcoin varsayılan olarak Electrum sunucularına bağlanır: Bull Bitcoin tarafından yönetilen ilk sunucu ve Blockstream'den ikincil bir sunucu, her ikisinin de günlük tutmadığı ve izleme riskini azalttığı düşünülmektedir.



Daha fazla gizlilik için, uygulamayı bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayabilirsiniz ([BullBitcoin'in GitHub](https://github.com/orgs/SatoshiPortal/projects/49) adresinde talimatlar mevcuttur).




## 4. Fonların alınması



İster **Bull Bitcoin Mobile** kullanın, **Bull Bitcoin Mobile** ile para almak basittir ve ihtiyaçlarınıza göre uyarlanmıştır:




  - uzun vadeli koruma için **Bitcoin (onchain)** ağı,
  - hızlı, daha fazla Confidential Transactions için **Liquid** ağı,
  - anında, düşük değerli ödemeler için **Lightning** ağı.



Uygulama, seçilen ağa bağlı olarak otomatik olarak Lightning alımı veya Invoice adreslerini oluşturur. Her ağ için nasıl ilerleyeceğiniz aşağıda açıklanmıştır.



### 4.1. onchain (Bitcoin ağı)



Ana ekranda şunları yapabilirsiniz:




- veya **Secure Bitcoin Wallet** öğesini seçin ve ardından "**Al "** öğesine tıklayın:



![image](assets/fr/04.webp)





- veya "**Alıcı "** üzerine tıklayın ve ardından **Bitcoin** ağını seçin:



![image](assets/fr/05.webp)



#### 4.1.1. Yalnızca Address'yı kopyala veya tara" seçeneği devre dışı (varsayılan)



![image](assets/fr/06.webp)





- Bu, isteğe bağlı gelişmiş parametrelere erişim sağlar. Belirtebilirsiniz :
 - BTC, Sats veya fiat cinsinden bir **miktar**.
 - URI / QR Kodunun kopyasına dahil edilecek bir **kişisel not**.
 - Gönderici ve alıcı girişlerini birleştirerek gizliliği artıran **PayJoin**'in etkinleştirilmesi (ayrıntılar için Ek 3'e bakın).





- **Otomatik olarak oluşturulan bir URI örneği**:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Kullanım**: Gönderenle paylaşmak için URI'yi kopyalayın veya QR kodunu taramasına izin verin.



#### 4.1.2. Yalnızca Address'u kopyala veya tara" seçeneği etkin



![image](assets/fr/07.webp)





- "Yalnızca Address'yi kopyala veya tara" **seçeneği etkinleştirildiğinde, uygulama SegWit (bech32) formatında basit bir Bitcoin Address oluşturur.**





- Örnek:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Bir tutar veya not girseniz bile, bunlar QR koduna veya Address kopyasına dahil edilmeyecektir





- **Kullanım**: Gönderenle paylaşmak için Address'ü kopyalayın veya QR kodunu taramasına izin verin.



#### 4.1.3. Yeni bir Address oluşturma





- Neden her işlem için yeni bir Address kullanıyorsunuz? Bu, birden fazla ödemenin aynı Address'ye bağlanmasını önleyerek **gizliliğinizi korur** ve Blockchain'da izleme olasılıklarını sınırlar.
- Varsayılan olarak, Bull Bitcoin otomatik olarak kullanılmayan bir **Address** oluşturur.
 - Ekranın altındaki **"Yeni Address"** seçeneğine tıklayarak yeni bir Address oluşturulmasını zorlayabilirsiniz.
 - Tüm adresleriniz seed ifadenize bağlıdır: kaç adres kullanırsanız kullanın, portföyünüz tek bir bakiye gösterecek ve bir gönderi yapıldığında fonları otomatik olarak birleştirebilecektir.





- İpucu: Özel bir ihtiyacınız olmadıkça (örneğin bağış almak için halka açık bir Address) her zaman Bull Bitcoin tarafından sağlanan yeni **Address**'yi kullanın.



### 4.2. Liquid



Ana ekranda şunları yapabilirsiniz:




- veya **Anında ödemeler Wallet** öğesini seçin, ardından **"Al "** öğesine ve ardından **"Liquid"** öğesine tıklayın:



![image](assets/fr/08.webp)





- veya "**Alıcı "** üzerine tıklayın ve ardından **Liquid** ağını seçin:



![image](assets/fr/09.webp)



"Al "** ekranına geldiğinizde, bir Liquid Address kopyalayın:





- Miktar veya not yok. Örnek:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Veya URI / QR Kodunun kopyasına dahil edilecek bir **miktar** (BTC, Sats veya fiat cinsinden) ve/veya bir **kişisel not** belirterek. Örnek:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Kullanın**: Gönderenle paylaşmak için Address/URI'yi kopyalayın veya QR kodunu taramasına izin verin.



### 4.3. Yıldırım



Ana ekranda şunları yapabilirsiniz:




- veya **Anında ödemeler Wallet**'yi seçin ve ardından **Al** düğmesine tıklayın:



![image](assets/fr/10.webp)





- veya "**Alıcı "** üzerine tıklayın ve ardından **Yıldırım** ağını seçin:



![image](assets/fr/11.webp)



#### 4.3.1. Çalışma, sınırlar ve faydalar





- **Mekanizma**: Bull Bitcoin Wallet, ödemelerin Lightning aracılığıyla yapılmasını ve alınmasını sağlayan bir Wallet'tir. Lightning aracılığıyla alınan fonlar, **Boltz** aracılığıyla otomatik bir takas sayesinde **Liquid** ağında (Wallet Anında Ödemelerde) saklanır. Bu, size likidite kanallarını yönetmek zorunda kalmadan Lightning ile etkileşim kurma olanağı sağlarken, kendi kendini saklama özelliğini de korur.





- **Sınırlar:**
- generate'yı Invoice yaptığınızda minimum 100 satoshi tutarında (19/07/2025 itibariyle).
- Wallet Lightning native ile almanın aksine, yalnızca gönderenin gönderilen tutara ek olarak transfer masraflarını ödediği durumlarda, gönderen tarafından gönderilen tutardan düşülecek olan masrafları **siz** ödersiniz. 19/07/2025 tarihi itibarıyla 47 Sats gönderilen tutardan düşülmektedir.





- **Avantajlar**:
- **Kendi kendine emanet**: Fonlarınız sizin kontrolünüz altında kalır ve Liquid Network'de saklanır.
- **Yüksek zincir içi ücretler yok**: Liquid üzerinde depolama, Lightning kanalınızı açmak veya likidite eklemek için maliyetli zincir içi para yatırma işlemlerini önler. Bu işlemler, Liquid'de biriken miktar ücretleri haklı çıkardığında daha sonra gerçekleştirilebilir.





- **İpucu:** Göndericide Wallet Bull Bitcoin varsa, takas ücretlerinden kaçınmak için doğrudan Liquid Network kullanın



#### 4.3.2. generate Invoice





- Bir **miktar** girin (BTC, Sats veya fiat olarak)





- Invoice'e entegre edilecek bir **kişisel not** ekleyin. Gönderen Invoice'i öderse, Wallet'unuz da bunu işlem ayrıntılarına dahil edecektir.





- **Invoice geçerliliği:** Yıldırım Invoice **12 saat** için geçerlidir. Bu sürenin sonunda geçerliliğini yitirir ve artık ödeme yapılamaz. Yeni bir Invoice oluşturulmalıdır.





- **Kullanım**: Gönderenle paylaşmak için Invoice'i kopyalayın veya QR kodunu taramasına izin verin.




## 5. Fon gönderme



### 5.1. Temel prensip



Ya ana sayfadan ya da cüzdanlardan :



![image](assets/fr/12.webp)



gönderme ekranına erişmek için:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile**, girilen Address veya Invoice'e (kopyalanan veya QR kodu ile taranan) göre ağı (Bitcoin, Liquid veya Lightning) otomatik olarak algılayarak para göndermeyi kolaylaştırır.



### 5.2. zincirleme iletim (Bitcoin ağı)



#### 5.2.1. Gönderme ekranı



**Eylem**: Address zincirine bir Bitcoin girin veya tarayın





- Miktar tanımlanmamışsa, örneğin :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Ardından gönderme ekranında seçim yapabilirsiniz:
 - BTC, sat veya fiat cinsinden tutar. Minimum miktar: 22/07/2025 tarihinde 546 satoshis.
 - İşlemi tanımlamak için isteğe bağlı bir not. İşlem ayrıntılarında yalnızca sizin tarafınızdan görülebilir.



![image](assets/fr/14.webp)





- Miktar zaten tanımlanmışsa, örneğin :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Daha sonra doğrudan aşağıdaki onay ekranına yönlendirileceksiniz.



#### 5.2.2 Onay ekranı



Özellikle miktar, varış noktası Address ve ücretler olmak üzere tüm parametreleri kontrol etmek için zaman ayırın.


Ardından parametreleri ayarlayabilirsiniz:



![image](assets/fr/15.webp)




- **Ücretler**: Seçebilirsiniz :
- İşleminizin gerçekleştirilme **hızı** ve ilgili ücretler tahmin edilecektir
- Mutlak ücretler (satoshi cinsinden toplam ücretler) veya Göreceli ücretler (bayt başına ücretler) modunda **ücretler** ve işleminizin hızı tahmin edilecektir





- **Gelişmiş ayarlar**:





- **Replace-by-fee (RBF)**: Varsayılan olarak etkinleştirilen bu işlev, daha yüksek bir ücret ödeyerek işlemi hızlandırır (ayrıntılar için Ek 4'e bakın).





- **UTXO'in manuel seçimi**: Fonlarınız birkaç farklı Wallet adresinde saklanıyorsa, fonların gönderileceği adresleri seçebilirsiniz. Bunu neden yapmalısınız? Bitcoin'ün giderek daha fazla benimsenmesiyle birlikte transfer ücretleri artmaktadır. Küçük miktarlarda birkaç adresten göndermek, tek bir Address'den göndermekten daha pahalıdır, ancak bunu şimdi yapmak, ücretlerin daha da yüksek olacağı daha sonra yapmak zorunda kalmayı önler. Buna **UTXO'in konsolidasyonu** denir



![image](assets/fr/16.webp)





- **PayJoin** ile gönderme: İşlev, URI'yi sağlayan alıcı tarafından etkinleştirildiyse, örn:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Ardından Bull Bitcoin Mobile, UTXO'larınızı alıcının UTXO'ları ile girdi olarak birleştirerek gönderimi yapılandıracak ve gizliliği artıracaktır (ayrıntılar için Ek 3'e bakın).



### 5.3. Liquid'e gönder



#### 5.3.1 Gönderme ekranı



**Liquid** ağı, hızlı işlemlere (dakikada bir blok sayesinde ~ 2 dakika), onchain ağından daha gizli (maskelenmiş tutarlar) ve çok düşük ücretlerle olanak tanır. Fonlar **Instant Payments Wallet**'dan çekilir.



**Eylem**: Bir Liquid Address girin veya tarayın





- Miktar tanımlanmamışsa, örneğin :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Ardından gönderme ekranında seçim yapabilirsiniz:




- BTC, sat veya fiat cinsinden miktar. Minimum yok, 1 Satoshi mümkün;
- İşlemi tanımlamak için isteğe bağlı bir not. İşlem ayrıntılarında yalnızca sizin tarafınızdan görülebilir.



![image](assets/fr/17.webp)





- Miktar zaten tanımlanmışsa, örneğin :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Daha sonra doğrudan aşağıdaki onay ekranına yönlendirileceksiniz.



#### 5.3.2 Onay ekranı



Tüm parametreleri, özellikle de Address miktarını ve hedefini kontrol etmek için zaman ayırın.



![image](assets/fr/18.webp)





- **Ücretler**: İşlemin karmaşıklığıyla orantılı olarak, genellikle 0,1 sat/vB bazında, yani basit bir işlem için 20-40 satoshis (22/07/2025 tarihinde 33 Sats).



### 5.4. Yıldırım'a gönder



#### 5.4.1 Gönderme ekranı



**Lightning** ağı, küçük tutarlar için anında, düşük maliyetli ödemeler sağlar ve küçük günlük işlemler için idealdir.



**Eylem**: Bir Lightning Invoice girin veya tarayın





- Miktarı ayarlamanıza izin veren bir LN-URL Address tararsanız


Örnek: `orangepeel@walletofsatoshi.com`.


ardından gönderme ekranında seçim yapabilirsiniz:




 - BTC, sat veya fiat cinsinden tutar. 23/07/2025 tarihinde minimum 1000 satoshis tutarı
 - İşlemi tanımlamak için isteğe bağlı bir not. Alıcıya gönderilecektir.



![image](assets/fr/19.webp)





- Belirli bir miktar içeren bir Lightning Invoice tararsanız


Örnek:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Daha sonra doğrudan aşağıdaki onay ekranına yönlendirileceksiniz.



Not: miktar 23/07/2025 tarihinde 21 Sats'den büyük olmalıdır



#### 5.4.2 Operasyon, sınırlar ve faydalar





- **Mekanizma**: Fonlar **Anlık Ödemeler Wallet** (Liquid)'den çekilir ve **Boltz** ile bir **Liquid → Lightning** takası yoluyla dönüştürülür.





- **Sınırlar:**
- Wallet Lightning native'den daha yüksek bir **minimum miktar** (yukarıya bakın)
- **Giderler** artı Liquid → Boltz aracılığıyla Yıldırım takası





- **Avantajlar**:
- **Kendi kendine emanet**: Fonlarınız kontrolünüz altında kalır, Liquid Network'te saklanır ve gerektiğinde Lightning aracılığıyla transfer edilebilir
- **Yüksek zincir içi ücretler yok**: Liquid'da depolamak, Lightning kanalınızı açmak veya likidite eklemek için maliyetli zincir içi para yatırma işlemlerinden sizi kurtardı. Bu işlemler, Liquid'da biriken miktar ücretleri haklı çıkardığında daha sonra gerçekleştirilebilir.





- **İpucu:** Alıcıda Wallet Bull Bitcoin varsa, takas maliyetlerinden kaçınmak için doğrudan Liquid Network kullanın



#### 5.3.3 Onay ekranı



Özellikle miktar ve hedef Address olmak üzere tüm parametreleri kontrol etmek için zaman ayırın.



![image](assets/fr/20.webp)




## 6. Geçmişi görüntüle



**Bull Bitcoin Mobile**, **Bitcoin (onchain)**, **Liquid** ve **Lightning** ağlarındaki işlemlerinizi takip etmenizi kolaylaştırır. Geçmişe iki şekilde erişilebilir ve her işlem türü için ayrıntılı bilgi görüntülenir. İşlemlerinizi harici blok tarayıcıları kullanarak da kontrol edebilirsiniz.



### 6.1. Erişim geçmişi





- Ana ekran üzerinden:
- Zincir içi işlemleri görüntülemek için **Secure Bitcoin Wallet** üzerine veya **Liquid** ve **Lightning** işlemleri için **Instant Payments Wallet** üzerine tıklayın.
 - Geçmiş, seçilen Wallet türüne göre filtrelenmiş olarak portföy toplamının hemen altında görüntülenir.



![image](assets/fr/21.webp)





- **Özel sayfa aracılığıyla** :
 - Ana ekranda **tarih simgesine** (saat simgesi veya benzeri) tıklayın.
 - İşlem türüne göre filtrelerle tüm işlemlerin listelendiği bir sayfaya erişin: **Gönder**, **Al**, **Takas**, **PayJoin**, **Sat**, **Al** (not: Sat ve Al geliştirme aşamasındadır ve şu anda mevcut değildir, 20 Temmuz 2025).



![image](assets/fr/22.webp)



### 6.2. İşlem detayları



Her işlem, ağa ve eylem türüne (gönderme veya alma) bağlı olarak belirli bilgileri görüntüler. İşte bir **transaction onchain** için mevcut ayrıntılar:



![image](assets/fr/23.webp)



### 6.3. Block explorer üzerinden kontrol



Bitcoin onchain, **Liquid** ve **Lightning** ağları için kaşiflerin listesi Ek 4'te yer almaktadır.



**Lightning** için işlemler genel tarayıcılarda görünmez. Uygulamadaki ayrıntıları (Boltz için Swap ID dahil) kontrol edin.




## 7. Ayarlar



"Ayarlar" sayfasına doğrudan Bull Bitcoin uygulamasının ana sayfasından erişilebilir ve portföyün ve kullanıcı deneyiminin çeşitli yönlerini yapılandırmak ve yönetmek için kullanılır.



![image](assets/fr/24.webp)





- **Wallet Yedekleme**: Güvenli yedekleme için portföyün kurtarma ifadesini görüntüler. Kurtarma ifadesinin yönetilmesi ve saklanmasına ilişkin en iyi uygulamalar için portföy oluşturma hakkındaki 3. bölüme bakın.





- **Wallet Detayları**:
- **Pubkey**: generate Bitcoin alım adresleri için kullanılan, Wallet ile ilişkili genel anahtar.
- **Türetme Yolu**: generate Wallet adreslerini özel anahtardan türetmek için kullanılan türetme yolu.





- **Electrum Sunucusu (Bitcoin Düğümü)**: Zincir üzerindeki işlemler için özelleştirilmiş bir Bitcoin düğümüne bağlantı kurun.





- **PIN Kodu**: Uygulamaya ve Wallet işlevlerine erişimi korumak için güvenlik kodunu etkinleştirin ve/veya değiştirin.





- **Para Birimi**: Tutarların BTC veya Sats cinsinden görüntülenip görüntülenmeyeceğini ve varsayılan fiat para birimini (dolar, euro, vb.) seçin.





- **Otomatik Takas Ayarları**: Otomatik Takas işlevi, BTC'nizin **Anında Ödemeler Wallet'ten (Liquid)** **Bitcoin On-Chain** Wallet'inize aktarımını, miktar işlem ücretini haklı çıkarmak için yeterince yüksek olduğunu düşündüğünüz bir eşiğe ulaşır ulaşmaz otomatikleştirmenize olanak tanır.





- **Günlükler**: Sorun gidermeyi kolaylaştırmak için teknik destekle paylaşılabilen görüntülenebilir etkinlik günlükleri.





- **Destek için Telegram erişimi**: Kullanıcı yardımı için resmi Telegram kanalına doğrudan bağlantı.





- **Github erişimi**: Açık kaynak kodunu görüntülemek veya sorunları bildirmek için [Bull Bitcoin Github deposu](https://github.com/SatoshiPortal) bağlantısı.




## EKLER



### A1. PayJoin (P2EP) Açıklaması



![image](assets/fr/25.webp)



**Tanım** :




- PayJoin veya **Pay-to-EndPoint (P2EP)**, **onchain** ağında gizliliği artıran bir Bitcoin işlem tekniğidir. Gönderici ve alıcı girişlerini tek bir işlemde birleştirerek tutarların ve adreslerin izlenmesini daha zor hale getirir.



**Operasyon:**




- Bir PayJoin işleminde, gönderici ve alıcı uyumlu bir PayJoin sunucusu aracılığıyla generate ortak bir işlem için birlikte çalışır.
- Sadece göndericinin girdi sağlaması yerine (UTXO), alıcı da kendi UTXO'larından biriyle katkıda bulunur. Bu, Blockchain'de görünen bilgileri bulanıklaştırır: gerçek miktara karşılık gelen tek bir giriş yerine artık iki giriş vardır ve çıkışlar doğrudan değiş tokuş edilen miktarı yansıtmaz.
- Nihai işlem standart bir Bitcoin işlemine (çoklu giriş/çoklu çıkış) benzer, ancak steganografik bir yapı sayesinde gönderilen gerçek miktarı ve adresler arasındaki bağlantıları gizler.



**Bull Bitcoin Mobile'da kullanım için**




- **Alma** (Address Supply): PayJoin varsayılan olarak etkindir.
- **Gönder**: Wallet otomatik olarak bir PayJoin URI algılar ve işlemi buna göre yapılandırır, örneğin:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Faydalar**




- **Geliştirilmiş gizlilik**: PayJoin, bir işlemdeki tüm girdilerin tek bir varlığa ait olduğu varsayımını geçersiz kılar. PayJoin ile girdiler hem göndericiden hem de alıcıdan gelir ve bu varsayımı bozar.
- **Miktar maskeleme**: Değiş tokuş edilen gerçek miktar doğrudan çıktılarda görünmez. Alıcının UTXO gelen ve giden miktarı arasındaki fark olarak hesaplanır ve bu da analizi yanıltıcı hale getirir.



**Limits**




- PayJoin, gönderici ve alıcının uyumlu cüzdanlar kullanmasını gerektirir, aksi takdirde standart bir zincir içi işlem kullanılır.
- İşlem biraz daha karmaşıktır (daha fazla girdi ve çıktı), bu da biraz daha yüksek maliyetlere neden olur.
- Standart bir işleme benzeyecek şekilde tasarlanmış olsa da, gelişmiş sezgisel yöntemler (örneğin belirsiz çıktılar, bilinen PayJoin sunucuları), kesin olmamakla birlikte, kullanımından şüphelenilmesine neden olabilir.



**Daha fazla bilgi:**




- [Sözlük](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Replace-by-fee'nin Açıklaması (RBF)



**Tanım**: Replace-by-fee (RBF), göndericinin daha yüksek bir ücret ödemeyi kabul ederek bir **zincir üzerinde** işlemin onaylanmasını hızlandırmasına olanak tanıyan Bitcoin ağının bir özelliğidir.



**Limits** :




- RBF, Liquid veya Lightning işlemleri için kullanılamaz.
- İlk işlem oluşturulduğunda RBF uyumlu olarak işaretlenmelidir, Bull Bitcoin Mobile bunu devre dışı bırakılmadığı sürece otomatik olarak yapar.



**Daha fazla bilgi:**




- [Sözlük](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. En iyi uygulamalar



**Bull Bitcoin Mobile'ı** güvenli ve verimli bir şekilde kullanmak için bu tavsiyelere uyun. Bunlar, **Bitcoin (onchain)**, **Liquid** ve **Lightning** ağlarında paranızı korumanıza, işlemlerinizi optimize etmenize ve gizliliğinizi korumanıza yardımcı olacaktır.





- **Kurtarma cümlenizi güvence altına alın** :
 - Öğretici: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- **Güvenli kimlik doğrulama kullanın**:
 - Uygulamaya erişimi korumak için bir **güçlü PIN** veya **biyometrik kimlik doğrulama** (parmak izi veya yüz tanıma) etkinleştirin.
 - PIN kodunuzu veya biyometrik verilerinizi asla paylaşmayın.





- **Gizliliğinizi koruyun**:
 - generate Blockchain üzerindeki izlemeyi sınırlandırmak için her zincir üstü veya Liquid alımı için yeni bir Address.
 - Zincir üzerinde gönderilen miktarla ilgili gizliliği artırmak için mevcut olduğunda PayJoin kullanın
 - Maksimum gizlilik için, Wallet'nizi genel düğümü kullanmak yerine bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayın





- **İhtiyaçlarınıza en uygun ağı seçin**:
- **Onchain**: Uzun vadeli saklama veya büyük değerli işlemler için tercih edilir (ücretler tutara göre ihmal edilebilir).
- **Liquid**: Gelişmiş gizlilik ile hızlı, düşük maliyetli transferler için kullanın.
- **Lightning**: Küçük miktarlar için anında, düşük maliyetli transferleri tercih edin. İki Wallet Bull Bitcoin kullanıcısıysanız, Boltz aracılığıyla Lightning <> Liquid takas ücretlerinden kaçınmak için Liquid'ü seçin.





- Her zaman gönderim adreslerini kontrol edin:
 - Para göndermeden önce Address'yi dikkatlice kontrol edin. Yanlış Address'ye gönderilen fonlar sonsuza kadar kaybolur. Kopyala/yapıştır veya QR kod taraması kullanın, asla bir Address'yi elle kopyalamayın/değiştirmeyin.





- **Maliyetleri optimize edin**:
 - Zincir üzerindeki işlemler için, aciliyet ve ağ tıkanıklığına göre uygun ücretleri (yavaş, orta, hızlı) seçin.
 - Küçük miktarlar için Liquid veya Lightning kullanın.
 - Onayı hızlandırmanız gerektiğini düşünüyorsanız zincirleme gönderiler için Replace-by-fee'ü (RBF) etkinleştirin (bkz. Ek 4).





- Uygulamayı güncel tutun




### A4. Ek kaynaklar





- **Resmi bağlantılar ve destek:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : destek e-postası
- [Bull Bitcoin resmi web sitesi](https://bullbitcoin.com/): **Bull Bitcoin hizmetleri hakkında bilgi, hesap oluşturma, uygulamaya erişim**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Kodu, evrimi ve yol haritasını görüntüleyin, geliştirmeye katkıda bulunun...**
- [X Hesabı - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- Wallet mobil için **Telegram** grubu: destek ile grup sohbeti, "Ayarlar" sayfasına bakın.





- Blok Kaşifleri :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blok Akış Bilgisi](https://blockstream.info/Liquid)**
 - Yıldırım: **[1ML (Lightning Network)](https://1ml.com/)**





- Öğrenme ve dersler:** [Plan ₿ Network](https://planb.network/)** :
 - Kurtarma ifadenizi güvence altına alma



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Sözlük](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Sözlük](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Boğa Bitcoin



#### Şirkete genel bakış



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, 2013 yılında Montreal, Kanada'daki Bitcoin Büyükelçiliğinde kurulan, yalnızca Bitcoin'ye adanmış en eski depo dışı Exchange platformudur. Bitcoin ekosisteminde tanınmış bir öncü olan Francis Pouliot tarafından yönetilen şirket, kendisini finansal egemenliği ve kullanıcı özerkliğini teşvik etmede kilit bir oyuncu olarak konumlandırmaktadır. Misyonu, Bitcoin dışındaki fiat para birimlerini ve kripto para birimlerini reddederken, Bitcoin'yi bir özgürlük ve ödeme aracı olarak kullanarak bireylerin paralarının kontrolünü yeniden kazanmalarını sağlamaktır.



![image](assets/fr/26.webp)



gW-221 alım ve satımlarında %0,25 indirim ile [Hesabınızı oluşturun] (https://app.bullbitcoin.com/registration/orangepeel).



#### Değerler ve felsefe



Bull Bitcoin, Commitment ila Cypherpunk ilkeleri ve Bitcoin etiği ile öne çıkmaktadır:





- **Bitcoin'e özel odaklanma**: Platform, merkezi olmayan, sansüre dirençli bir para birimi vizyonuna sadıktır.





- **Saklama kuruluşu olmayan**: Kullanıcılar kendi portföylerine fon göndererek Bitcoin'lerinin tam kontrolünü ellerinde tutarlar.





- **Gizlilik**: Kişisel verilerin toplanması en aza indirilmiş, 999 USD altındaki işlemler için KYC'siz satın alma seçenekleri. Veriler yönetmeliklere uygun olarak korunmaktadır (Kanada'da FINTRAC, Fransa'da AMF).





- **Şeffaflık**: Gizli ücret yoktur, maliyetler spread'e (alış ve satış fiyatları arasındaki fark) dahildir.





- **Finansal egemenlik**: Bull Bitcoin geleneksel bankacılık sistemlerinden ve merkezi kurumlardan bağımsızlığı teşvik eder.



#### Ana hizmetler





- **Fiat para yatırma**: Kullanıcılar Bull Bitcoin hesaplarına fiat para birimi (CAD, EUR, vb.) ile banka havalesi veya belirli Kanada postanelerinde nakit/banka kartı yoluyla para yatırabilirler.





- **Bitcoin Satın Alma**: Kullanıcılar, fonlarının tam kontrolünü garanti ederek doğrudan depozitosuz portföylerine gönderilen Bitcoin'i satın alabilirler.





- **Planlanmış Bitcoin satın alma**: Bull Bitcoin, Bitcoin'lerin kullanıcı kontrolündeki Wallet'a doğrudan aktarılmasıyla, mevcut bakiyenizden yararlanarak düzenli aralıklarla otomatik olarak yinelenen bir satın alma hizmeti (DCA - Dolar Maliyet Ortalaması) sunar ve fiyat dalgalanmalarının etkisini azaltır.



"AutoBuy" adı verilen bir seçeneğin, fiatlarınızı Bull Bitcoin bakiyenize dokunur dokunmaz dönüştürmenize ve Bitcoinlerinizi kendi Wallet'nize göndermenize olanak tanıdığını unutmayın. Bu seçenek, DCA yapmak için bankanızla planlanan yinelenen bir banka havalesi ile de birleştirilebilir. Bu seçenek, uygulamayı hiç açmak zorunda kalmadan Bitcoin birikiminizi otomatikleştirir.






- Bitcoin'ü sabit bir fiyattan **'Limit Emri'** ile satın alın: Kullanıcı tarafından önceden belirlenen bir fiyattan Bitcoin satın almanıza olanak tanır ve Bull Bitcoin endeks fiyatı belirlenen limite ulaştığında veya altına düştüğünde otomatik olarak gerçekleştirilir.





- **Bitcoin satışı**: Kullanıcılar Bitcoin'lerini satabilir ve fiat para birimi cinsinden parayı banka veya SEPA havalesi yoluyla doğrudan banka hesaplarına alabilirler.





- **Üçüncü taraf ödemeleri**: Bull Bitcoin, kullanıcıların Bitcoin'lerinden banka hesaplarına alıcıya tamamen şeffaf bir şekilde fiat para göndermelerini sağlar.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime, yüksek gelirli ve kurumsal müşteriler için özelleştirilmiş çözümler ve premium destek sunan premium bir hizmettir. Buna indirimli ücretlere erişim, özel bir hesap yöneticisi ve özel kurumsal hizmetler dahildir. Bu hizmet, derinlemesine uzmanlık ve öncelikli muamele isteyen kurumlar, profesyonel tüccarlar ve kurumsal müşterilere yöneliktir.





- **Mobil Wallet**: Bull Bitcoin, onchain, Liquid ve Lightning Network işlemlerini destekleyen, Android ve iOS'ta kullanılabilen, açık kaynaklı, kendi kendine emanet edilebilen bir mobil Wallet sunmaktadır.





- **Eğitim desteği**: Kullanıcıların Bitcoin portföylerini oluşturmalarına, güvence altına almalarına ve yönetmelerine yardımcı olmak için ücretsiz kılavuzlar ve kişiselleştirilmiş koçluk, finansal özerkliği güçlendirir.



#### Uyum ve güvenlik





- **Düzenleyici**: FINTRAC (Kanada) ve AMF'ye (Fransa) kayıtlı Bull Bitcoin, KYC/AML gerekliliklerine uygundur.





- **Güvenlik**: Güvenli portföylerin kullanımı ve çevrimdışı depolama önerileri. Kişisel veriler, Bull'un %100 kendi kendine barındırılan ve herhangi bir üçüncü tarafa güvenmeyen Bitcoin altyapısında barındırılır.