---
name: Bitfinex - Şirket
description: Bitfinex'te bir şirket hesabı oluşturma ve yönetme
---
![cover](assets/cover.webp)


2012 yılında kurulan Bitfinex, ilk Bitcoin ve Altcoin Exchange platformlarından biridir. Başlangıçta P2P Bitcoin borsalarına odaklanan platform, hizmetlerini hızla marj ticareti, P2P finansmanı, türev ticareti ve yüksek hacimli işlemler için bir OTC ("* tezgah üstü*") piyasasını içerecek şekilde genişletti.


Bugün Bitfinex, hem basit bitcoin alımlarına hem de risk yönetimi araçlarıyla gelişmiş ticaret işlevlerinin (geleneksel ticaret, türevler, OTC, borç verme vb.) kullanılmasına olanak tanıyan eksiksiz bir platformdur. Bir web sürümü mevcuttur ve basit işlemler için kullanımı kolay bir mobil uygulama da mevcuttur.


Bu eğitimde, Bitfinex'te bir işletme hesabı oluşturma, bitcoin satın alma ve satma, muhasebe amaçlı işlemleri yönetme ve euro ve bitcoin yatırma ve çekme sürecini ele alacağız. Amaç, ister Bitcoin'ü nakit akışınıza entegre etmeyi ister Bitcoin'ü bir ödeme aracı olarak kabul etmeyi planlıyor olun, size temel bilgileri sağlamaktır.


Bitcoin'i işletmenize entegre etme konusuyla ilgileniyorsanız, konuyla ilgili eksiksiz teorik eğitim kursumuzu keşfetmenizi de tavsiye ederim:


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a

## 1 - Bitfinex hesabı oluşturma


Bitfinex'in resmi web sitesine] (https://www.bitfinex.com/) gidin. Ana sayfada, hesabınızı oluşturmaya başlamak için "*Kayıt Ol*" seçeneğini bulun ve tıklayın. İlk başta, bireyler için standart bir hesap oluşturacaksınız, "*Kurumsal*" seçeneği daha sonra doğrulama işlemi sırasında seçilecektir.


![BITFINEX](assets/fr/01.webp)


Gerekli bilgileri tamamlayın: ticari e-posta adresinizi Address ve şirketinizin ikamet ettiği ülkeyi girin. Güvenli bir kullanıcı adı ve şifre seçin, ardından kaydı onaylamak için "*Kaydol*" seçeneğine tıklayın.


![BITFINEX](assets/fr/02.webp)


Güçlü, benzersiz parolaların kullanımı ve korunmasına ilişkin ipuçları için bu eğitime de bakın:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Şimdi hesabı güvence altına almak için 2FA'yı yapılandıracağız. Akıllı telefonunuzda Google Authenticator veya Authy gibi bir kimlik doğrulama uygulaması kullanın. Bu araçla ilgili bir öğreticiyi burada bulabilirsiniz:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

QR kodunu uygulamanızla tarayın ve verilen 6 haneyi girin.


![BITFINEX](assets/fr/03.webp)


Kayıt işlemleri tamamlanmıştır.


![BITFINEX](assets/fr/04.webp)


Posta kutunuzu kontrol edin ve kaydınızı onaylamak için Bitfinex tarafından gönderilen bağlantıya tıklayın.


![BITFINEX](assets/fr/05.webp)


Hesabınız şimdi oluşturuldu. Platforma erişmek için "*Giriş yap*" seçeneğine tıklayın.


![BITFINEX](assets/fr/06.webp)


## 2 - Şirket hesabı doğrulaması


Bitfinex, mevcut düzenlemelere uygun bir doğrulama süreci (KYC) uygulamaktadır. "Temel" modda para yatırmak mümkün değildir, bu da en azından "Orta" doğrulama seviyesini, hatta gerekirse "Tam" doğrulama seviyesini elde etmeyi gerekli kılar.


Hesabınız oluşturulduktan sonra, bir açılır pencere hesabınızı doğrulamanızı önerecektir. "*Doğrula*" üzerine tıklayın.


![BITFINEX](assets/fr/07.webp)


Bu pencere görünmezse, Interface'nin sağ üst köşesindeki profilinize gidin ve ardından "*Doğrulama*" seçeneğine tıklayın.


![BITFINEX](assets/fr/08.webp)


"*Hesap Türü*" altında "*Kurumsal*" seçeneğini seçin. Benim durumumda, "*Orta Düzeye*" yükseltme yapıyorum, bu yüzden "*Orta Düzeye Yükselt*" seçeneğini seçiyorum.


![BITFINEX](assets/fr/09.webp)


Sağlayarak adımları tamamlayın:




- Şirket bilgileri (şirket adı, iletişim bilgileri, iş sektörü vb;
- Yasal belgeler (ana sözleşme, Kbis özeti, yönetici ve hissedar listesi);
- Her bir intifa hakkı sahibi veya yönetici için KYC bilgileri (kimlik belgeleri, Address kanıtı vb.).


Başvurunuz tamamlandıktan ve gönderildikten sonra, platformun iş doğrulaması için doğrulaması birkaç gün sürebilir. Bu süre zarfında, para yatırma işlemleri geçici olarak engellenecektir.


![BITFINEX](assets/fr/10.webp)


## 3 - Bitfinex Interface'a hızlı giriş


Giriş yaptıktan sonra, Interface'un üst kısmında bir gezinme çubuğu göreceksiniz: "*Trading*", "*Derivatives*", "*Funding*", "*OTC*", "*P2P*", "*Wallet*", vb. Bitfinex, aşağıdakiler de dahil olmak üzere çok çeşitli işlevler sunar:




- Ticaret**: kripto para birimleri (Bitcoin dahil) almak ve satmak için emir verebileceğiniz "*klasik*" piyasa;
- OTC**: Halka açık emir defterlerinin dışında, doğrudan başka bir oyuncuyla büyük hacimli alım satım yapmak için Tezgah Üstü hizmet;
- Fonlama**: Borç verme ve marj fonlamasına ayrılmış alan;
- Türevler**: Türev ürünler (vadeli işlemler vb.) bölümü, deneyimli tüccarlara yöneliktir;
- P2P**: Eşler arası temelde diğer kullanıcılardan kripto almanıza veya satmanıza olanak tanır.


Standart kullanım için (bitcoin satın alma/satma, para yatırma/çekme ve nakit yönetimi), esas olarak "*Trading*" sekmesinin yanı sıra "*Wallet*", "*Deposit*" ve "*Withdraw*" bölümlerini kullanacaksınız.


![BITFINEX](assets/fr/11.webp)


Kurumsal formülün bir diğer avantajı da alt hesaplar oluşturabilmesidir. Bu, her biri belirli haklara sahip (salt okunur, alım satım, yalnızca para yatırma vb.) birkaç kullanıcıya bu alt hesaplara erişim verebileceğiniz anlamına gelir.


## 4 - Euro (fiat) yatırma ve çekme


Bitfinex Kurumsal hesabınıza avro yatırmak için, Interface'nın üst kısmındaki "*Wallet*" menüsünde bulunan "*Deposit*" alt menüsüne erişin.


![BITFINEX](assets/fr/12.webp)


Euro (veya başka bir fiat para birimi) cinsinden para yatırmak için "*Banka havalesi*" veya "*Kredi/Banka Kartı*" seçeneğini seçin.


![BITFINEX](assets/fr/13.webp)


Gönderilecek fiat para birimini seçin, örneğin euro. Yalnızca temel "*Ticaret*" işlevlerini kullanıyorsanız, "*Exchange*" üzerine tıklayın. Ayrıca yatırmak istediğiniz tutarı ve ticari hesap bankanızın ülkesini de belirtin.


![BITFINEX](assets/fr/14.webp)


Ticari banka hesabınızdan Bitfinex tarafından belirtilen banka hesabına bir transfer yapın.


Para çekmek için prosedür benzerdir: "*Çek*" alt menüsüne gidin.


![BITFINEX](assets/fr/15.webp)


"*Banka havalesi*" üzerine tıklayın.


![BITFINEX](assets/fr/16.webp)


Çekmek istediğiniz fiat para birimini, Bitfinex'te borçlandırılacak hesabı (yalnızca temel özellikleri kullanıyorsanız "*Exchange*") ve çekilecek tutarı seçin.


![BITFINEX](assets/fr/17.webp)


Bitfinex, uyumluluk nedenleriyle transferi kabul etmeden önce banka hesabınızın doğrulanmasını isteyebilir.


![BITFINEX](assets/fr/18.webp)


Prosedür başlatıldıktan sonra, Bitfinex parayı banka hesabınıza aktaracaktır.


## 5 - Bitcoin yatırma ve çekme


Bitfinex'e Bitcoin yatırmak için "*Deposit*" alt menüsüne erişin.


![BITFINEX](assets/fr/19.webp)


"*Cryptocurrency*" üzerine tıklayın.


![BITFINEX](assets/fr/13.webp)


"*BTC*" öğesini seçin. Bir alıcı Address görünecektir. Bu Address'i kopyalayın ve BTC'nizi göndermek için kendi sakladığınız Wallet'den veya başka bir platformdan kullanın.


![BITFINEX](assets/fr/20.webp)


Bitcoin'ü geri çekmek için "*Geri Çek*" alt menüsüne gidin.


![BITFINEX](assets/fr/21.webp)


"*Cryptocurrency*" üzerine tıklayın.


![BITFINEX](assets/fr/22.webp)


"*BTC*" seçeneğini seçin. Para çekme işleminiz için borçlandırılacak Bitfinex hesabını seçin (temel özellikler için "*Exchange*"). Bitcoinlerin miktarını ve hedef Address'i girin. Herhangi bir hatayı önlemek için para çekme Address'i kontrol ettiğinizden emin olun.


![BITFINEX](assets/fr/23.webp)


Onayınızı takiben bitcoinleriniz transfer edilecektir. Ücretlerin ve gecikmelerin Mempool yoğunluğuna bağlı olarak değişebileceğini lütfen unutmayın.


Bitfinex ayrıca Lightning Network üzerinden para yatırma ve çekme seçenekleri sunarak daha hızlı ve daha ucuz işlemlere olanak sağlamaktadır.


![BITFINEX](assets/fr/24.webp)


Lightning Network ile ilgileniyorsanız, nasıl çalıştığını anlamanıza yardımcı olacak eksiksiz bir eğitim kursumuz da var:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

## 6 - Bitfinex'te bitcoin alım satımı


Bitfinex çeşitli işlem modları sunmaktadır. Kullanım kolaylığı için, "*Trading*" veya "*Exchange*" olarak da bilinen klasik spot piyasayı tercih edin. Burada, piyasa fiyatından alım veya satım emirleri verebilir veya bir limit fiyat belirleyebilirsiniz.


Üst menüde "*Ticaret*" üzerine tıklayın.


![BITFINEX](assets/fr/25.webp)


Örneğin, Exchange cinsinden Euro karşılığında BTC almak veya satmak istiyorsanız "*BTC/EUR*" çiftini seçin.


![BITFINEX](assets/fr/26.webp)


Interface, ortada bir fiyat grafiği, altta emir defteri ve solda emir giriş modülünü görüntüler. Emir girişi bölümünde, "*Piyasa*" emri (mevcut en iyi fiyattan hemen gerçekleştirilir) veya "*Limit*" emri (fiyatı siz belirlersiniz) arasında seçim yapabilirsiniz. Alacağınız veya satacağınız BTC miktarını belirtin veya bakiyenizin bir yüzdesini seçin. Ardından satın almak için "*Buy*" veya satmak için "*Sell*" seçeneğine tıklayın.


![BITFINEX](assets/fr/27.webp)


Gerçekleşen emirlerinizin geçmişini Interface'nin alt kısmında görüntüleyebilirsiniz.


![BITFINEX](assets/fr/28.webp)


## 7 - İşlem geçmişi dışa aktarımı ve muhasebe


Muhasebe amaçları için, işlemlerinizin ayrıntılarını (alımlar, satışlar, para yatırma, çekme) dışa aktarmanız gerekir. Bitfinex kapsamlı bir raporlama aracı sunar. Interface'ün sağ üst köşesindeki profil simgenize ve ardından "*Raporlar*" menüsüne tıklayın.


![BITFINEX](assets/fr/29.webp)


Sol tarafta, dışa aktarılacak veri türünü seçebilirsiniz. Örneğin, "*İşlemler*" seçildiğinde tüm işlemlerinize erişebilirsiniz.


![BITFINEX](assets/fr/30.webp)


"*Tarih*" kutusunda istediğiniz dönemi tanımlayın ve gerekirse "*Sembol*" alanını kullanarak aramanızı bir veya daha fazla belirli çift ile sınırlandırın.


![BITFINEX](assets/fr/31.webp)


Bu verileri dışa aktarmak için "*Dışa Aktar*" düğmesine tıklayın.


![BITFINEX](assets/fr/32.webp)


Parametreleri kontrol edin, ardından dışa aktarımı onaylayın.


![BITFINEX](assets/fr/33.webp)


Rapor, Bitfinex hesabınızla ilişkili Address'e bir CSV dosyası olarak e-posta ile gönderilecektir.


![BITFINEX](assets/fr/34.webp)


Dosya dışa aktarıldıktan sonra, muhasebe yazılımınıza entegre edebilir veya yeminli mali müşavirinize gönderebilirsiniz.


## 9 - Şirket için kullanım senaryoları


Şirketinizin hedeflerine ve yapısına bağlı olarak Bitfinex'in kullanımı değişiklik gösterebilir.


### Nakit karşılığında bitcoin satın alma


**Amaç:** Bitcoin'e yatırım yaparak şirketin nakit akışını çeşitlendirmek.


**İzlenecek adımlar:**




- Şirketin banka hesabından Bitfinex'e avro yatırın;
- Bitcoin satın almak için bu avroları kullanın;
- Bitcoin'leri platformda tutun veya kendi gözetiminizde saklamak için çekin;
- İşlem geçmişlerini gerektiği gibi dışa aktarın.


### Bitcoin'nin ödeme aracı olarak kabul edilmesi


**Amaç:** Şirketinize, ürün veya hizmetleriniz için bir ödeme aracı olarak Bitcoin'i kabul etme imkanı sunmak.


**İzlenecek adımlar:**




- Bir Bitcoin ödeme sistemi entegre edin. Küçük işletmeler için basit Wallet yazılımı yeterli olabilir veya Bitcoin'u web sitenize veya satış noktasına bir ödeme seçeneği olarak entegre etmek için Swiss Bitcoin Pay veya BTCPay Server gibi özel çözümleri tercih edebilirsiniz;
- Bitcoin olarak alınan ödemeleri Bitfinex hesabınıza aktarın;
- Finansal stratejinize bağlı olarak, aldığınız bitcoinleri avro karşılığında satabilir, gelecekte değer kazanma potansiyeli için saklayabilir veya her ikisinin bir kombinasyonunu tercih edebilirsiniz;
- Bitcoinleri platformda tutun veya kendi kendinize saklamak için çekin. Ayrıca banka hesabınıza avro da çekebilirsiniz;
- İşlem geçmişlerini gerektiği gibi dışa aktarın.


Bu konuya daha derinlemesine bir bakış için, nakit akışına ekleme, Bitcoin ödemelerini kabul etme ve muhasebe konularını ayrıntılı olarak ele alan Bitcoin'i işletmelere entegre etmeye yönelik bu kapsamlı eğitim kursunu tavsiye ederim:


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a