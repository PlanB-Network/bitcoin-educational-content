---
name: Ocean Mining

description: Okyanus Mining'e Giriş
---

![signup](assets/cover.webp)


**Mayıs 2024**


Okyanus Mining biraz benzersiz bir Mining pool'dir. Burada hesap, e-posta adresi ya da şifre gerekmiyor. Tıpkı Bitcoin'te olduğu gibi, her şey şeffaf, takma adlıdır ve katkıda bulunanlar dört farklı blok şablonundan birini seçebilir.


### Tazminat Sistemi


Ocean'ın ücretlendirme sistemi TIDES, "Transparent Index of Distinct Extended Shares" olarak adlandırılmaktadır. Bu sistem madenciler tarafından sağlanan ve "hisse" olarak bilinen çalışmaları kaydeder. Havuz, her bir katılımcı için "hisse" yüzdesini hesaplar, ardından Bitcoin Address'larını Block reward'in bu yüzdesinin yararlanıcısı olarak havuzun blok şablonuna ekler.


Blok şablonu, en kazançlı yeni işlemleri hesaba katmak ve gerekirse Block reward'in dağılımını değiştirmek için yaklaşık her 10 saniyede bir güncellenir.


![signup](assets/rem.webp)


Havuzun yeni bir blok çıkardığı sırada makinelerinizin bağlı olup olmaması önemli değildir. Halihazırda gönderilen iş, havuz tarafından bulunan sonraki sekiz blok için saklanır.


Çıkarılan her yeni blokta sayaçları sıfırlamak yerine sekiz blok için çalışmayı sürdürmek, siz katkıda bulunmaya başladıktan sonra havuz sekiz blok bulduğunda tazminatınızın yalnızca %100 olacağı anlamına gelir. Bu aynı zamanda, havuza katkıda bulunmayı bırakırsanız sekiz blok için tazminat almaya devam edeceğiniz anlamına gelir.


Bu mekanizma telafiyi yumuşatır ve bir sonraki bloğu bulma olasılığı en yüksek olan havuza bağlı olarak havuzların düzenli olarak değiştirilmesini içeren "havuz atlamayı" engeller.


### Para Çekme


Ocean Mining'un çalışması, katkıda bulunanların "temiz" bitcoinleri, yani doğrudan Block reward tarafından verilen bitcoinleri kurtarmasına olanak tanır.


Diğer havuzların çoğundan farklı olarak Ocean yeni çıkarılan bitcoinleri almaz; katkıda bulunanların adresleri doğrudan blok şablonuna entegre edilir.


Şimdilik, temiz bitcoinlerden gerçekten faydalanmak için minimum miktar 1,048,576 Sats'dir. Havuz tarafından çıkarılan her blokta, Block reward tarafından size doğrudan ödeme yapılabilmesi için "hisse" payınızın size 1.048.576 Sats'den daha fazla hak kazandırması gerekir.

Aksi takdirde, toplam ödülleriniz bu miktarı aşana kadar Sats'ünüz Ocean tarafından saklanacaktır.


Ocean tarafından geçici olarak tutulan tüm bitcoinler bu Address üzerindedir: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, her şey TimeChain üzerinde doğrulanabilir](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Sats'nızı BOLT12 kullanarak Lightning üzerinden çekmeniz de mümkündür. Bunu nasıl ayarlayacağımızı göreceğiz.


### Havuz Ücretleri


Ücretler, seçilen blok şablonuna bağlı olarak %0 ile %2 arasında değişmektedir.


## Okyanusun Şeffaflığı


### Katılımcı Verileri


![signup](assets/1.webp)


Tüm kullanıcı verileri de dahil olmak üzere havuzla ilgili tüm bilgiler şeffaftır. Bu noktayı anlamak için bir örnek verelim:


[Ocean kontrol panelinde] (https://ocean.xyz/dashboard), son altı aydaki Hashrate, havuzdaki katılımcı sayısı, çıkarılan toplam bitcoin sayısı vb. gibi çok sayıda bilgiye sahipsiniz.


Biz "Katkıda Bulunanlar" bölümüne odaklanacağız. Son üç saatteki ortalama Hashrate'leriyle birlikte tüm katkıda bulunanların listesini ve havuzun geri kalanına göre **"paylaşım "** ve **"Hash"** yüzdesini görebilirsiniz.


**"Paylar %"**, havuzun geri kalanına kıyasla son sekiz blokluk pencerede katkıda bulunan tarafından sağlanan işin yüzdesidir.


**"Hash %"**, havuzun geri kalanına kıyasla son üç saat içinde katkıda bulunan tarafından sağlanan ortalama Hashrate'nin yüzdesidir.


![signup](assets/2.webp)


"Katkıda Bulunanların" Bitcoin Address ile tanımlandığını fark edeceksiniz. Daha fazla ayrıntı için bu adreslerden herhangi birine tıklayabilirsiniz.


İlkini, en yüksek Hashrate'e sahip olanı [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ] (https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ) alırsak, bu kullanıcıyla ilgili tüm ayrıntıları görebilirsiniz: Hashrate, kazılan bitcoin sayısı, hangi blokla kazıldığı ve hatta makinelerinin (ASIC'ler) her birinin ayrıntıları. Ancak, Bitcoin'te olduğu gibi anonim kalırlar.


### Blok Şablonu


Kontrol panelinde sol üstte "Sonraki blok" var. Bu sayfada dört farklı blok şablonu bulunmaktadır. Ocean, her katılımcının desteklemek istediği blok şablonunu seçmesine olanak tanır. Bunun sizin ücretiniz üzerinde doğrudan bir etkisi yoktur. Havuz bir blok çıkardığında, tüm katılımcılar seçtikleri şablondan bağımsız olarak tazmin edilir. Bu sadece herkesin kendisine uygun blok şablonu için "oy kullanmasına" olanak tanır.


![signup](assets/3.webp)


**ÇEKİRDEK:** Ücret %2, bu filtresiz klasik Bitcoin core şablonu, sayfalarında yazdığı gibi "İşlemleri ve spam'lerin çoğunu içerir"


**CORE+ANTISPAM:** Ücret %0, Ordinals gibi belirli işlemlere karşı bir filtre ile Bitcoin core "İşlemleri içerir ve spam'i sınırlar"


**OCEAN:** Ücret %0, Bitcoin Knot "Yalnızca işlemleri ve makul ölçüde küçük verileri içerir"


**VERİ İÇERMEZ:** Ücret %0, Bitcoin Düğümü "Yalnızca rastgele veri içermeyen işlemleri içerir"


### Bitcoin core ve Bitcoin Düğümü arasındaki ayrım

Bitcoin core, dünya genelindeki Bitcoin düğümlerinin yaklaşık %99'unun çalışmasını sağlayan yazılımdır. Bitcoin bir protokoldür, yani tıpkı birden fazla tarayıcının bulunduğu İnternet gibi, aynı TimeChain üzerinde birkaç farklı yazılım programı bir arada bulunabilir. Ancak, uyumluluk endişesi ve TimeChain üzerinde silinmez izler bırakacak hata riskini sınırlamak için, neredeyse tüm Bitcoin geliştiricileri Bitcoin core üzerinde çalışmaktadır. Bitcoin Knots, Bitcoin core'nin bir Fork'idir, yani kodlarının çoğunu paylaşır ve hata riskini büyük ölçüde sınırlar. Bu Fork, bir Hard Fork oluşturmadan Bitcoin core'den daha kısıtlayıcı kurallar uygulamak isteyen Luke Dashjr tarafından oluşturulmuştur. Şimdi, Nakamoto fikir birliği sayesinde Bitcoin core ve Bitcoin düğümleri bir arada var olmaktadır.


## İşçi Ekleme


Bir çalışan eklemek için blok şablonunuzu seçerek başlayın. Bu seçim, Miner'nıza (ASIC'ler) girilecek havuz URL'sini belirleyecektir.



- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`


Ardından, kullanıcı alanı için sahip olduğunuz bir Bitcoin Address girin. İşte uyumlu Address tiplerinin listesi:


- **P2PKH** (Orijinal Address tipi. "1" ile başlar)
- **P2SH** (Çoklu imza veya P2SH-SegWit. "3" ile başlar)
- **Bech32** (SegWit. "bc" ile başlar.)
- **Bech32m** (Taproot. "bc" ile başlar. Bech32'den daha uzun.)


Birden fazla madenciniz varsa, hepsi için aynı Address'ü girebilirsiniz, böylece Hash oranları birleştirilir ve tek bir Miner olarak görünür. Ayrıca her birine ayrı bir isim ekleyerek onları ayırt edebilirsiniz. Bunu yapmak için Bitcoin Address'ten sonra ".workername" eklemeniz yeterlidir.


Son olarak, şifre alanı için `x` kullanın.


**Örnek:**

Eğer **OCEAN** şablonunu seçerseniz, Bitcoin Address'unuz `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` ise ve Miner'inize "Brrrr" adını vermek istiyorsanız, Miner'inizin Interface'ine aşağıdaki bilgileri girmeniz gerekecektir:



- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **KULLANICI**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **ŞİFRE**: `x`


Mining'ü başlattıktan birkaç dakika sonra, Address'nizi arayarak verilerinizi Ocean sitesinde görebileceksiniz.


### Gösterge Tablosuna Genel Bakış


- **Ödül Penceresindeki Paylar**: Bu veri, havuz tarafından çıkarılan son 8 bloğun penceresinde havuza gönderdiğiniz iş olan hisse sayısını gösterir.
- **Pencerelerdeki Tahmini Ödüller**: Halihazırda yapılan iş ile kazanacağınız Sats sayısının tahmini. Bu, işlem ücretlerini hesaba katmaz, yalnızca ağ tarafından çıkarılan yeni bitcoinler olan coinbase'i hesaba katar.
- **Tahmini Kazanç Sonraki Blok**: Şimdi bir blok çıkarılırsa kazanılacak Sats sayısının tahmini. Unutmayın, bu değer 1.048.576 Sats'dan azsa, Sats'yı doğrudan Address'inize almayacaksınız. Kazançlarınız bu eşiği aşana kadar Ocean'ın Address'ine gönderilecekler.


Aşağıda, 6 aya kadar olan Hashrate geçmişinizi gösteren bir grafik bulunmaktadır.


![signup](assets/4.webp)


Burada, 60'lardan 24 saate kadar farklı zaman ölçeklerinde ortalama Hashrate'inizin yanı sıra katkıda bulunduğunuz ve ödüllendirildiğiniz havuz tarafından çıkarılan blokların geçmişine sahipsiniz.


![signup](assets/5.webp)


Bu geçmişin bir CSV dosyasını **CSV İndir** düğmesi ile dışa aktarma seçeneğiniz vardır.


![signup](assets/6.webp)


Aşağıdaki bölümde, bu Address ile havuza bağladığınız tüm madencilerin bir listesi bulunmaktadır. Elbette, bireysel Hashrate'larının yanı sıra, çalışmaları için bireysel olarak aldıkları Sats sayısı da var.


![signup](assets/7.webp)


Herhangi bir Miner'nin **Nickname**'ine tıklayabilirsiniz. Daha sonra az önce gördüğümüz tüm bilgilere sahip olacaksınız, ancak özellikle o Miner için.


Ve sayfanın altında, Address'ünüzün ödeme geçmişini, çıkardığınız ancak henüz ödenmemiş Sats'ü ve çıkardığınız toplam Sats'ü görebileceğiniz bazı ek bilgiler.


![signup](assets/8.webp)


Burada, **En Az Ödemeye Kadar Tahmini Süre** kutusunda Yıldırım yazdığını görebilirsiniz çünkü bir BOLT12 teklifi oluşturduk.


### Lightning Para Çekme İşlemlerini Ayarlama


Sizin de anladığınız gibi Ocean şeffaflığı en üst düzeye çıkarmayı ve gözetimi en aza indirmeyi (Sats'inizi sizin adınıza tutmayı) amaçlamaktadır.


Bu nedenle, Lightning para çekme işlemleri için **BOLT12 tekliflerini** kullanmak gerekir. Bu, 2024'te ortaya çıkmaya başlayan ve birkaç şeye izin veren Lightning Network'da ödeme yapmanın yeni bir yoludur:


- Yeniden kullanılabilir bir ödeme bağlantısıdır, otomatik ödemelere izin verir ve Lightning Address'den farklı olarak BOLT12 gözetim altında değildir.
- Ayrıca, ödemenin yapıldığına dair kanıt sağlayan bir ödeme yöntemidir, LNURL'lerde durum böyle değildir.
- Çok önemli, hem BTC Address hem de BOLT12 teklifinin sahibi olduğunuzu kanıtlamak için bir Bitcoin imzası ile birlikte kullanılabilir.

Bugün itibariyle (Mayıs 2024), bu yöntemi kullanmak için çok az çözüm mevcuttur. Bu örnekte Core Lightning ile bir Start9 sunucusu kullanacağız. Örneğin Phoenix Wallet gibi diğer araçlar entegre BOLT12 tekliflerine sahip olduğunda, bu eğitim geçerli kalacaktır. Gelen likidite ile açık kanallarınız olduğundan emin olun, aksi takdirde ödemeler çalışmayacaktır.


Ocean sitesindeki kontrol panelinize giderek BTC Address'inizi girerek başlayın, ardından **Yapılandırma** sekmesine tıklayın.


![signup](assets/9.webp)


**Açıklama** metnini buraya kopyalayacağız:

bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` için `OCEAN Ödemeleri


Şimdi Start9 sunucunuzdaki Core Lightning Interface'nize (veya BOLT12 teklifi sağlayabilen herhangi bir Wallet'e) gidin.


![signup](assets/10.webp)


**Al** üzerine tıklayın.


**Teklif** seçeneğini işaretleyin, ardından önceden kopyaladığınız metni **Açıklama** alanına yapıştırın ve **Miktar** alanını boş bırakın.


![signup](assets/11.webp)


**generate Teklifi** üzerine tıklayın.


![signup](assets/12.webp)


Lightning adreslerinde olduğu gibi merkezi bir sunucu gerektirmeyen, yeniden kullanılabilir ve kalıcı bir ödeme bağlantısı oluşturdunuz. Bağlantıyı kopyalayın ve ardından Ocean sayfasına geri dönün.


Lightning BOLT12 Offer** alanına ödeme bağlantısını yapıştırın ve **Block Height** alanını varsayılan değerinde bırakın. generate** üzerine tıklayın.


![signup](assets/13.webp)


Ocean'ın bir hesap sistemi kullanmadan bu ödeme bağlantısının gerçekten size ait olduğundan emin olması için, kullandığınız Bitcoin Address'ya karşılık gelen özel anahtarınızla yeni oluşturulan mesajı imzalamanız gerekecektir. Bir mesajı özel anahtarınızla imzalamak için birçok çözüm mevcuttur. Bu eğitimde BlueWallet örneğini ele alacağız, ancak yöntem tüm cüzdanlar için aynıdır.


![signup](assets/14.webp)


Özel anahtarınızın BlueWallet'ta olduğunu varsayarak (aynısını bir Hardware Wallet ile de yapabilirsiniz), ilgili Wallet'a tıklayın.


![signup](assets/15.webp)


Sonra sağ üstteki **...** düğmesine basın.


![signup](assets/15bis.webp)


Ve **İmzala/Doğrulama Mesajı**.


![signup](assets/16.webp)


Bu pencerede üç alan bulunmaktadır: **Address**, **İmza** ve **Mesaj**.


Address** alanına Bitcoin Address'inizi girin. Örneğimize geri dönersek, bu Address'dir: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.


**İmza** alanını boş bırakın.

Ve oluşturulan mesajı Ocean'ın sayfasındaki **Message** alanına yapıştırın: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

**İmzala** üzerine tıklayın.


Bu, generate Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`nin sahibi olduğunuzu kanıtlayan kriptografik bir imza olacaktır ve bu imza, Ocean tarafından sağlanan ve BOLT12 ödeme bağlantısından oluşturulan mesaj sayesinde benzersizdir.


![signup](assets/17.webp)


İmzayı kopyalayın ve Ocean'ın sayfasına yapıştırın, ardından **ONAYLA** düğmesine tıklayın.


![signup](assets/18.webp)


Bir onay mesajı görmeniz gerekir.


![signup](assets/19.webp)


Şimdi **İstatistiklerim** sekmesine gidin. Daha önce Start9'da Core Lightning ile oluşturduğunuz BOLT12 ödeme bağlantısıyla birlikte en üstte ek bilgiler görüntülenir.


![signup](assets/20.webp)