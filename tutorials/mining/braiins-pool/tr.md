---
name: Braiins Havuz

description: Braiins Havuzuna Giriş
---

![signup](assets/cover.webp)


Eskiden Slush Pool olarak bilinen Braiins Pool, ilk Bitcoin Mining pool'dır. Kasım 2010'da kurulmuş ve ilk bloğunu 16 Aralık 2010'da 97834 numaralı blok olarak çıkarmıştır.


Mayıs 2024 itibariyle Braiins Havuzu, toplam Bitcoin Hashrate'nin yaklaşık %1,8'ini temsil eden 13 EH/s'lik bir hesaplama gücüne sahiptir. Toplam 1.307.188 bitcoin çıkarmıştır ki bu da var olabilecek maksimum 21 milyon bitcoinin yaklaşık %6'sına tekabül etmektedir.


### Tazminat Sistemi


Braiins Pool, 2023'ün sonundan bu yana tazminat sistemini FPPS (Hisse Başına Tam Ödeme) sistemini benimseyecek şekilde değiştirdi. Bu, madencilerin havuz bir blok bulmamış olsa bile, bir önceki gün yaptıkları tüm çalışmalar için her gün ödül aldıkları anlamına gelir. Bu, madencilerin yalnızca havuz bir blok bulduğunda ödül aldığı eski sistemden farklıdır.


**Bitcoin TimeChain'i analiz eden Mononaut'un bir tweetine göre] (https://x.com/mononautical/status/1777686545715089605), FPPS sistemini kullanan birçok Mining havuzunun çıkarılan bitcoinleri AntPool'un bir Address'ine göndereceğini belirtmek gerekir; bu da AntPool'un tüm bu havuzların Hashrate'ünü, yani küresel Bitcoin Hashrate'ün yaklaşık %47'sini kontrol ettiği anlamına gelir. Bu, ağın merkezsizleştirilmesi için çok kötü bir haberdir.**


### Havuz Ücretleri


Braiins Pool için ücretler %2,5'tir, ancak makinelerinizde BraiinsOS kullanırsanız ücretler %0 olacaktır


### Para Çekme


**Yıldırım Çekilmeleri**

Lightning para çekme işlemleri, ödüllerinizi günde bir kez Lightning Address aracılığıyla minimum tutar olmadan çekmenize olanak tanır.

Bu yöntemi kullanmak için Lightning adresleriyle uyumlu bir Wallet'a sahip olmanız gerekir.


**On-Chain Para Çekme**

On-Chain para çekme işlemleri asgari bir miktarla sınırlıdır ve ücrete tabi olabilir.

Minimum miktar: 20.000 Sats

Ücretler: 500.000 Sats'ün altındaki tutarlar için 10.000 Sats

500.000 Sats üzerindeki tutarlar için ücretsiz

Para çekme işlemleri zaman aralığına veya miktara göre tetiklenebilir.


## Hesap Oluşturma


Braiins Pool'u kullanmaya başlamak için [web sitelerine gidin] (https://braiins.com/pool) ve sağ üstteki "KAYIT OL" seçeneğine tıklayın



![signup](assets/3.webp)


Bilgilerinizi girin ve doğrulayın, ardından Address'inizi onaylamanızı isteyen bir e-posta alacaksınız. Aldığınız e-postadaki bağlantıyı kullanarak onaylayın ve ardından platforma giriş yapın


![signup](assets/4.webp)



## Bir "işçi" ekleme

Bir çalışan, havuza bağlayacağınız Miner'dır. Yeni bir Miner eklemek için sol kenar çubuğu menüsündeki "Çalışanlar "a tıklayın.

![signup](assets/7.webp)


Ardından mor renkli "Connect Workers +" düğmesine tıklayın.


Bu pencerede coğrafi bölgenizi seçin.


Bağlanmak istediğiniz Miner BraiinsOS kullanıyorsa, "Stratum V2" protokolünü seçin. Aksi takdirde, "Stratum V1 "i seçin.


![signup](assets/8.webp)


Miner'inizin web sayfasında girmeniz gereken bilgiler olacaktır (bu bilgileri nereye gireceğinizi öğrenmek için Miner'inizin belgelerine bakın).


Burada, **"stratum+tcp://eu.stratum.braiins.com:3333"** havuz URL'sidir.


**JimZap.workerName** sizin tanımlayıcınız ve Miner'unuzun adıdır; burada JimZap tanımlayıcı ve .workerName Miner'un adıdır. Birden fazla madenciniz varsa, onlara aynı adı verebilirsiniz, bu durumda bilgi işlem güçleri gösterge tablosunda toplanır veya ayrı ayrı izlemek için onlara farklı adlar verebilirsiniz.


Ve parola her zaman aynıdır **"anything123"**


Bu bilgileri Miner'inizin web sayfasına girdikten ve Mining'yi başlattıktan sonra, birkaç dakika sonra Braiins Pool Dashboard'da göründüğünü göreceksiniz.


## Gösterge Tablosuna Genel Bakış


![signup](assets/9.webp)


Üst başlıkta, tüm madencilerinizin 5 dakika, 1 saat ve 24 saat boyunca ortalama toplam Hashrate'sini görebilirsiniz. Ve çevrimiçi veya çevrimdışı madenci sayısının bir özeti.

Aşağıda, bilgi işlem gücünüzün gelişimini takip etmenizi sağlayan bir grafik yer almaktadır.


![signup](assets/10.webp)


Bu tablonun altında, Sats'teki ödülleriniz hakkında çeşitli bilgiler yer almaktadır.


**"Bugünün Mining Ödülleri "** Bugün çıkardığınız Sats sayısını gösterir. Günün sonunda bu değer 0'a sıfırlanacak ve Sats hesabınıza gönderilecektir.


**"Dünün Toplam Ödülü "** Bir gün önce çıkardığınız Sats sayısı


**"Est. Kârlılık (1 TH/s) "** 1 TH/s işlem gücü için bir günde kazandığınız Sats sayısının tahminidir. Örneğin, değer 77 Sats ise ve gün boyunca sürekli olarak 10 TH/s işlem gücüne sahipseniz, teorik olarak günde 77 x 10 = 770 Sats kazanırsınız.


**"Tüm Zamanların Ödülü "** Braiins Havuzu ile çıkardığınız toplam Sats


**"Ödül Programı "** Havuz tarafından uygulanan ücret oranı


**"Sonraki Ödeme ETA "** Sats'u platformdan çekebilmeniz için geçecek süre tahmini. Burada, Mining yalnızca birkaç dakikadır devam ettiği için tahmin hiçbir şey göstermiyor.


**"Hesap Bakiyesi "** Hesabınızda bulunan ve daha sonra çekebileceğiniz Sats sayısı.

## Para Çekme İşlemlerini Ayarlama

Ödüllerinizi On-Chain veya Address ile yıldırım yoluyla çekebilirsiniz.


En üstte, "Fonlar" üzerine tıklayın. Varsayılan olarak bir "Bitcoin Hesabınız" vardır. Ödülleri paylaşmak için başkalarını da oluşturabilirsiniz. Bu konuya bir sonraki bölümde döneceğiz.


Şimdilik "Kur" seçeneğine tıklayın.


![signup](assets/17.webp)


Bu yeni pencerede "Onchain ödeme" seçeneğini seçebilirsiniz.


Bu Wallet'yı adlandırın, bir BTC Address sağlayın ve istediğiniz tetikleyici türünü seçin. "Eşik", belirli bir miktarda BTC biriktirdiğinizde ödemenin tetikleneceği anlamına gelir ve "Zaman aralığı" ile ödeme düzenli aralıklarla (gün / hafta / ay) tetiklenir.


Minimum tutarın 0,0002 BTC olduğunu ve 0,005 BTC'nin altında 0,0001 BTC'lik bir ücret uygulanacağını unutmayın.


![signup](assets/18.webp)


Lightning para çekme işlemlerini kullanmak istiyorsanız, Lightning Address sağlayan bir Wallet'e ihtiyacınız olacaktır. Örneğin, getAlby kullanabilirsiniz.


Pencerenin üst kısmındaki "Yıldırım ödemesi" üzerine tıklayın.


Lightning Address'unuzu girin ve "Anlıyorum..." kutusunu işaretleyin, ardından doğrulayın.


Bu para çekme yöntemi ile ödülleriniz her gün Wallet'ınıza gönderilecektir.


![signup](assets/14.webp)


Ödeme ayarlarınızı doğruladıktan sonra bir onay e-postası alacaksınız.


![signup](assets/15.webp)


## Ödüllerin Paylaşımı


Braiins Pool ayrıca ödüllerinizi birden fazla cüzdan arasında paylaşmanıza da olanak tanır.


Bunu yapmak için, en üstte "Mining" ve ardından solda "Ayarlar" üzerine tıklayın.


![signup](assets/19.webp)


Bu sayfada, "Başka Bir Finansal Hesap Ekle" seçeneğine tıklayarak başka "Finansal Hesaplar" ekleyebilecek ve ödüllerinizi bir Wallet ile ilişkilendirmeniz gereken bu farklı hesaplar arasında % olarak dağıtabileceksiniz. Yeni bir Wallet'yi bir Finansal Hesapla ilişkilendirmek için önceki bölüme bakın.