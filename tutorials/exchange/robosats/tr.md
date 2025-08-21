---
name: Robosatlar

description: Robosatlar nasıl kullanılır?
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/), ulusal para birimleri için özel olarak Exchange Bitcoin yapmanın kolay bir yoludur Eşler arası deneyimi basitleştirir ve saklama ve güven gereksinimlerini en aza indirmek için yıldırım tutma faturalarını kullanır.


![video](https://youtu.be/XW_wzRz_BDI)


## Kılavuz


**Not:** Bu kılavuz Bitocin Q&A'dan (https://bitcoiner.guide/robosats/) alınmıştır. Tüm krediler ona aittir, onu [burada] (https://bitcoiner.guide/contribute) destekleyebilirsiniz; BitcoinQ&A aynı zamanda bir Bitcoin mentorudur. Mentorluk için onunla iletişime geçin!


![image](assets/0.webp)


RoboSats - Basit ve özel bir Yıldırım tabanlı P2P Exchange


## Başlamadan Önce


### Bilmeniz gerekenler


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## Sahip olmanız gereken şeyler


### Bir Yıldırım Wallet


RoboSats Lightning'e özgüdür, bu nedenle tahvili finanse etmek ve satın alınan Sats'yi alıcı olarak almak için bir Lightning Wallet'ya ihtiyacınız olacak. Wallet'nızı seçerken dikkatli olmalısınız, RoboSats'ın çalışmasını sağlamak için kullanılan teknoloji nedeniyle hepsi uyumlu değildir.


Eğer bir düğüm koşucusuysanız, Zeus açık ara en iyi seçenektir. Kendi node'unuz yoksa, basit kurulumu ve Lightning'e erişimi olan çapraz platformlu bir mobil Wallet olan Phoenix'i şiddetle tavsiye ederim. Bu kılavuzun hazırlanmasında Phoenix kullanılmıştır.


### Bazı Bitcoin


Alıcı ve satıcıların, herhangi bir işlem gerçekleşmeden önce bir tahvili finanse etmeleri gerekir. Bu genellikle çok küçük bir miktardır (işlem tutarının ~%3'ü), ancak yine de bir ön koşuldur.


RoboSats'ı ilk Sats'unuzu satın almak için mi kullanıyorsunuz? Neden bir arkadaşınız size başlangıç için gereken küçük miktarı ödünç vermiyor? Eğer tek başınıza uçuyorsanız, işte başlamanız için bazı noKYC Sats elde etmek için diğer bazı harika seçenekler.


### RoboSat'lara Erişim


Açıkçası RoboSats'a erişmeniz gerekecek! Bunu yapabilmeniz için dört ana yol vardır:


1. Tor Tarayıcı ile (Önerilen!)

2. Normal bir web tarayıcısı aracılığıyla (Önerilmez!)

3. Android APK'sı aracılığıyla

4. Kendi müşteriniz


Tor tarayıcısında yeniyseniz, daha fazla bilgi edinin ve [buradan] indirin (https://www.torproject.org/download/).


Telefonlarından Tor aracılığıyla RoboSats'a erişmek isteyen iOS kullanıcıları için kısa bir not. 'Onion Browser' Tor Browser değildir. Bunun yerine Orbot + Safari ve Orbot + DuckDuckGo kullanın.


## Bitcoin Satın Alma


Aşağıdaki adımlar Mayıs 2023'te Tor tarayıcısı üzerinden erişilen 0.5.0 sürümü kullanılarak gerçekleştirilmiştir. RoboSats'a Android APK üzerinden erişen kullanıcılar için adımlar aynı olmalıdır.


Bu yazının yazıldığı sırada RoboSats hala aktif olarak geliştirilme aşamasındaydı, bu nedenle Interface gelecekte biraz değişebilir, ancak ticareti tamamlamak için gereken temel adımlar büyük ölçüde değişmeden kalmalıdır.


**Not:** RoboSats'ı ilk yüklediğinizde bu açılış sayfası ile karşılaşacaksınız. Başlat'a tıklayın.


![image](assets/2.webp)


generate token'ünüzü şifreli bir not uygulaması veya şifre yöneticisi gibi güvenli bir yerde saklayın. Bu token, tarayıcınızın veya uygulamanızın bir işlemin ortasında kapanması durumunda geçici Robot Kimliğinizi kurtarmak için kullanılabilir.


![image](assets/3.webp)


Yeni Robot kimliğinizle tanışın, ardından Devam'a tıklayın.


![image](assets/4.webp)


Sipariş defterine göz atmak için Teklifler'e tıklayın. Sayfanın üst kısmında tercihlerinize göre filtreleme yapabilirsiniz. Tahvil yüzdelerine ve ortalama Exchange oranı üzerindeki prime dikkat ettiğinizden emin olun.



- 'Satın Al' etiketini seçin
- Para biriminizi seçin
- Ödeme yöntem(ler)inizi seçin


![image](assets/5.webp)


**Not:** almak istediğiniz teklifin üzerine tıklayın. Satıcıdan satın almak istediğiniz tutarı (seçtiğiniz fiat para biriminde) girin, ardından ayrıntıları son bir kez kontrol edin ve 'Siparişi Al'a tıklayın.


Satıcı çevrimiçi değilse (profil resminde kırmızı bir nokta ile gösterilir), işlemin normalden daha uzun sürebileceğine dair bir uyarı görürsünüz. Devam ederseniz ve satıcı zamanında işlem yapmazsa, boşa harcadığınız zaman için teminat tutarının %50'si size tazmin edilecektir.


![image](assets/6.webp)


Ardından, ekrandaki Invoice'yı ödeyerek ticari senedinizi kilitlemeniz gerekir. Bu, Wallet'nizde donan bir Invoice tutmadır. Yalnızca işlemin kendi tarafınızı tamamlayamazsanız tahsil edilecektir.


![image](assets/7.webp)


Lightning Wallet'unuzda QR kodunu tarayın ve Invoice'i ödeyin.


![image](assets/8.webp)


Ardından, Yıldırım Wallet generate ve Invoice ile gösterilen tutarı girin ve verilen alana yapıştırın.


![image](assets/9.webp)


Satıcının işlem tutarını kilitlemesini bekleyin. Bu gerçekleştiğinde, RoboSats otomatik olarak sohbet penceresinin açılacağı bir sonraki adıma geçecektir. Merhaba deyin ve satıcıdan fiat ödeme bilgilerini isteyin. Verildikten sonra, ödemeyi seçilen yöntemle gönderin ve ardından bunu RoboSats'ta onaylayın. RoboSats'taki tüm sohbetler PGP şifrelidir, yani mesajları yalnızca siz ve işlem eşiniz okuyabilirsiniz.


![image](assets/10.webp)


Satıcı ödemenin alındığını onayladığında, RoboSats daha önce sağlanan Invoice'ü kullanarak ödemeyi otomatik olarak serbest bırakır.


![image](assets/11.webp)


Invoice ödendiğinde işlem tamamlanır ve bononuzun kilidi açılır. Daha sonra bir işlem özeti göreceksiniz.


![image](assets/12.webp)


Sats'nın geldiğini teyit etmek için Lightning Wallet'inizi kontrol edin.


![image](assets/13.webp)


## Ek Özellikler


Bitcoin'nin bariz alım satımının yanı sıra RoboSats'ın bilmeniz gereken birkaç özelliği daha var.

Robot Garajı


Aynı anda birden fazla işlem yapmak istiyor, ancak hepsinde aynı kimliği paylaşmak istemiyor musunuz? Sorun değil! Robot sekmesine tıklayın, generate ek bir Robot oluşturun ve bir sonraki siparişinizi oluşturun veya alın.


![image](assets/14.webp)


### Sipariş Oluşturma


Başkasının teklifini kabul etmenin yanı sıra, kendi teklifinizi oluşturabilir ve başka bir Robotun size gelmesini bekleyebilirsiniz.



- Oluştur sayfasını açın.
- Emrinizin Bitcoin almak mı yoksa satmak mı olduğunu tanımlayın.
- Alım/Satım yapmak istediğiniz tutarı ve para birimini girin.
- Kullanmak istediğiniz ödeme yöntem(ler)ini girin.
- Kabul etmek istediğiniz 'Piyasa Üzeri Prim' yüzdesini girin. Mevcut piyasa fiyatına kıyasla indirimli teklif vermek için bunun negatif bir rakam olabileceğini unutmayın.
- Sipariş Oluştur'a tıklayın.
- Maker Bond'unuzu kilitlemek için Yıldırım Invoice'u ödeyin.
- Siparişiniz şimdi yayında. Arkanıza yaslanın ve birinin kabul etmesini bekleyin.


![image](assets/15.webp)


### On-Chain Ödemeleri


RoboSats Lightning odaklıdır, ancak alıcılar Sats'lerini bir On-Chain Bitcoin Address'e alma seçeneğine sahiptir. Alıcılar bu seçeneği tahvillerini kilitledikten sonra seçebilirler. On-Chain'yi seçtikten sonra, alıcı ücretlere genel bir bakış görecektir. Bu hizmet için ek ücretler şunları içerir:



- RoboSats tarafından toplanan bir takas ücreti - Bu ücret dinamiktir ve Bitcoin ağının ne kadar meşgul olduğuna bağlı olarak hareket eder.
- Ödeme işlemi için bir Mining ücreti - Bu alıcı tarafından yapılandırılabilir.


![image](assets/16.webp)


### P2P Takasları


RoboSats, kullanıcıların Sats'ı Lightning Wallet ile takas etmelerine veya çıkarmalarına olanak tanır. Mevcut takas tekliflerini görüntülemek için teklifler sayfasının üst kısmındaki takas düğmesine tıklamanız yeterlidir.


Bir 'Takas' teklifinin alıcısı olarak, On-Chain Bitcoin'ü eşe gönderir ve Sats'yı, ilan edilen ücretler ve/veya primler düşüldükten sonra Lightning Wallet'inize geri alırsınız. Bir 'Takas' teklifinin alıcısı olarak, Lightning aracılığıyla Sats gönderirsiniz ve On-Chain Address'ünüze herhangi bir ücret ve/veya prim düşülmüş olarak Bitcoin alırsınız. Samourai veya Sparrow wallet kullanıcıları da bir takası tamamlamak için Kaçak Yolcu özelliğinden yararlanabilir.


RoboSats takas teklifleri, RBTC, LBTC ve WBTC gibi Bitcoin'ye sabitlenmiş alternatifleri de içerebilir. Bu tokenlarla etkileşime girerken son derece dikkatli olmalısınız çünkü hepsi çeşitli ödünleşimlerle birlikte gelir. Sabitlenmiş Bitcoin, Bitcoin değildir!


![image](assets/17.webp)


### Kendi RoboSats İstemcinizi çalıştırın


Umbrel, Citadel ve Start9 düğüm koşucuları kendi RoboSats istemcilerini doğrudan düğümlerine yükleyebilirler. Bunu yapmanın faydaları şu şekilde sıralanmaktadır:



- Önemli ölçüde daha hızlı yükleme süreleri.
- Daha güvenli: Hangi RoboSats istemci uygulamasını çalıştıracağınızı siz kontrol edersiniz.
- RoboSats'a herhangi bir tarayıcıdan / cihazdan güvenle erişin. Yerel ağınızdaysanız veya VPN kullanıyorsanız TOR kullanmanıza gerek yok: düğüm arka ucunuz anonimleştirme için gereken torifikasyonu gerçekleştirir.
- Hangi P2P piyasa koordinatörüne bağlanacağınız üzerinde kontrol sağlar (varsayılan olarak robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## SSS


### Dolandırılabilir miyim?


Bir alıcı olarak, işlemin sizin tarafınız için gerekli olan fiatı gönderdiyseniz, ancak satıcı Sats'u size serbest bırakmazsa, bir anlaşmazlık açabilirsiniz. Bu anlaşmazlık sürecinde RoboSats hakemlerine fiatı gönderdiğinizi kanıtlayabilirseniz, satıcının emanet fonları ve takas teminatı size serbest bırakılacaktır.

Bir işlemi nasıl iptal edebilirim?


Tahvilinizi gönderdikten sonra işlem menüsündeki İşbirlikçi İptal düğmesine tıklayarak bir işlemi iptal edebilirsiniz. İşlem eşiniz iptal etmekten memnunsa, herhangi bir ücret ödemezsiniz. Ancak işlem ortağınız işlemi tamamlamak isterse ve siz yine de devam edip iptal ederseniz, işlem teminatınızı kaybedersiniz.


### RoboSats 'X' ödeme yöntemi ile çalışıyor mu?


RoboSats'ta ödeme yöntemleri konusunda herhangi bir kısıtlama yoktur. İstediğiniz yöntemde herhangi bir teklif görmüyorsanız, bunu kullanarak kendi teklifinizi oluşturun!


![image](assets/19.webp)


### RoboSats, onu kullandığımda benim hakkımda ne öğreniyor?


RoboSats'ı Tor veya Android uygulaması üzerinden kullanmanız koşuluyla, hiçbir şey! Daha fazlasını buradan öğrenin.



- Tor ağ gizliliğinizi korur.
- PGP şifrelemesi ticari sohbetinizi gizli tutar.
- Hesap olmaması, işlem başına bir Robot anlamına gelir. Bu, RoboSat'ların birden fazla işlemi tek bir varlıkla ilişkilendiremeyeceği anlamına gelir.


Ancak, bazı uyarılar var! Lightning gönderici olarak oldukça gizlidir, ancak alıcı olarak değildir. Kendi Lightning düğümünüze alım yaparsanız, düğüm kimliğiniz faturalarınızda paylaşılır. Bu düğüm kimliği, bu konuda bilgisi olan herkese On-Chain etkinliğinizi ilişkilendirmek için bir başlangıç noktası sağlar. Bu durum, bir kullanıcının işlemlerini On-Chain ödemesi yoluyla almayı tercih etmesi halinde de geçerlidir.


Bunu azaltmak için kullanıcılar Lightning için Proxy Wallet veya On-Chain için CoinJoin gibi bir çözüm kullanmayı tercih edebilir.


### Federasyon


Şu anda RoboSats geliştirici ekibi tarafından işletilen tek bir RoboSats koordinatörü var. Bitcoin'te her türlü merkezileşme, belirli bir hizmete sıcak bakmayabilecek hükümetler ya da düzenleyiciler için daha kolay bir hedef haline gelmektedir.


RoboSats bir Açık Kaynak projesi olduğundan, herkes kodu alabilir ve kendi koordinatörünü çalıştırmaya başlayabilir. Bu durum riski tek bir hedeften uzaklaştırarak bir nebze merkezsizleştirse de, zaten zayıf olan likidite piyasasını da parçalamaktadır.


RoboSats ekibi bunun farkına varmış ve federasyon modeli üzerinde çalışmaya başlamıştır. Son kullanıcı olarak bu, yukarıda gösterilen ticaret akışını çok fazla değiştirmemelidir, ancak ortaya çıkan farklı koordinatörleri eklemeniz veya kaldırmanız için ekstra görünümler veya ekranlar olacaktır.


Kılavuzun sonu

https://bitcoiner.guide/robosats/