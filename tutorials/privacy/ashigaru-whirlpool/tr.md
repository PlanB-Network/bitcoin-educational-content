---
name: Ashigaru - Whirlpool Coinjoin
description: Ashigaru uygulamasında nasıl coinjoins yapabilirim?
---

![cover](assets/cover.webp)



"*sokaklar için bir bitcoin wallet*"



Bu eğitimde, coinjoin'in ne olduğunu ve Ashigaru Terminal uygulaması ve Samourai Wallet'ten miras kalan bir coinjoin protokolü olan Whirlpool uygulaması ile nasıl yapılacağını öğreneceksiniz.



## Whirlpool koinjointler nasıl çalışır?



Bu eğitimde, coinjoin kavramının, kullanışlılığının veya Whirlpool'in teorik işleyişinin üzerinden geçmeyeceğim, çünkü bu konular Plan ₿ Academy'deki BTC 204 eğitim kursunun 5. Bölümünde zaten ayrıntılı olarak açıklanmıştır. Whirlpool'in işleyişi veya coinjoin prensibi konusunda henüz uzmanlaşmadıysanız, devam etmeden önce bu 5. bölüme başvurmanızı şiddetle tavsiye ederim:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ancak, burada işinize yarayabilecek birkaç hızlı bilgi ve rakam bulunmaktadır.



Whirlpool uyumlu portföyler, coinjoin sürecinin ihtiyaçlarını karşılamak için 4 ayrı hesap kullanır:




- 0'` indeksi ile tanımlanan **Depozito** hesabı;
- 2,147,483,644 endeksi ile tanımlanan **Kötü Banka** (veya *doxxic exchange*) hesabı;
- 2 147 483 645'` endeksi ile tanımlanan **Premix** hesabı;
- Postmix** hesabı, `2 147 483 646'` endeksi ile tanımlanmıştır.



Ashigaru'da, Kasım 2025'te iki havuz mezhebi mevcuttur (bu liste muhtemelen önümüzdeki aylarda değişecektir: bu nedenle okurken değerleri kontrol etmeyi unutmayın):




- 0.25 BTC`, giriş ücreti ise `0,0125 BTC`;
- 0.025 BTC, giriş ücreti 0,00125 BTC.



Her karıştırma döngüsü giriş ve çıkışta 5 ila 10 UTXO içerebilir.



![Image](assets/fr/01.webp)



## Yazılım gereksinimleri



Whirlpool ile coinjoins yapmak için üç ayrı programa ihtiyacınız olacaktır:





- Ashigaru Terminal**, coinjoins'lerinizi doğrudan bilgisayarınızdan yönetmenizi sağlar;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, akıllı telefonunuzdaki uygulama ile bitcoinlerinizi her yerden *postmix* içinde harcayabilirsiniz;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, üçüncü taraf bir sunucuya bağımlı olmadan ağa egemen bir bağlantıyı garanti eden bir Bitcoin düğüm uygulaması.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Bu araçların her birini ilgili eğitimlerini izleyerek yükleyin, ardından ilk coinjoins'lerinizi yapmaya başlayabilirsiniz.



## Bitcoin alma



Portföyünüzü oluşturduktan sonra, `0'` endeksi ile tanımlanan tek bir hesapla başlayacaksınız. Bu `Deposit` hesabıdır. Coinjoins için bitcoinleri bu hesaba göndereceksiniz. Bunları Ashigaru uygulaması (özel eğitimin 5. bölümüne bakın) veya Ashigaru Terminali (yine özel eğitimin 5. bölümünde ayrıntılı olarak açıklanmıştır) aracılığıyla alabilirsiniz.



Mevduat hesabınız en küçük havuza katılmak için gereken miktarı (artı hizmet ücretleri ve mining maliyetlerini karşılamak için gereken minimum tutar) içerdiğinde, ilk coinjoins'lerinizi başlatmaya hazır olacaksınız.



![Image](assets/fr/02.webp)



## Tx0'ı yapın



Para yatırma hesabınıza ulaştığında ve işlem onaylandığında, coinjoin işlemini başlatabilirsiniz. Bunu yapmak için, Ashigaru Terminalinde `Cüzdanlar` menüsünü açın, ardından wallet'nizi seçin. wallet'niz kilitliyse, yazılım sizden şifrenizi ve passphrase'inizi isteyecektir.



![Image](assets/fr/03.webp)



Ardından `Mevduat` hesabını seçin.



![Image](assets/fr/04.webp)



UTXOs menüsüne gidin.



![Image](assets/fr/05.webp)



Burada para yatırma hesabınızdaki tüm UTXO'ların bir listesini göreceksiniz. Coinjoin döngülerinde göndermek istediklerinizi seçin.



Daha fazla gizlilik için ve *Common Input Ownership Heuristic (CIOH)* önlemek için, Whirlpool'te girdi başına yalnızca bir UTXO kullanılması önerilir (bu ilkenin ayrıntılı bir açıklaması BTC 204'te bulunabilir).



Bir UTXO seçmek için klavyenizdeki `ENTER` tuşuna basın: seçildiğini belirtmek için yanında bir yıldız işareti `(*)` belirecektir.



![Image](assets/fr/06.webp)



Ardından `Seçilen Karışım` düğmesine tıklayın.



![Image](assets/fr/07.webp)



Mevcut iki havuzdan birine katılabilecek kadar büyük bir UTXO'niz varsa, okları kullanarak hedef havuzu seçebilirsiniz. Bu sayfada, Tx0'ınızın ayrıntılarını göreceksiniz:




- havuza girecek UTXO'ların sayısı;
- uygulanan çeşitli ücretler (hizmet ücretleri ve mining ücretleri) ;
- *doxxic değişim* miktarı.



Bilgileri dikkatlice kontrol edin, ardından Tx0'ı yayınlamak için `Broadcast` seçeneğine tıklayın.



![Image](assets/fr/08.webp)



Ashigaru daha sonra Tx0'ınızın TXID'sini görüntüleyerek işlemin ağ üzerinde yayınlandığını onaylayacaktır.



![Image](assets/fr/09.webp)



## Eş birleştirmeler yapma



Tx0 yayınlandıktan sonra, mevduat hesabınızın ana sayfasına dönün, ardından `Hesaplar` üzerine tıklayın ve `Premix` hesabını seçin.



![Image](assets/fr/10.webp)



UTXOs' menüsünde, çeşitli eşitlenmiş parçaları, eş birleştirme döngülerine girmeye hazır olarak göreceksiniz. Tx0 onaylanır onaylanmaz, Ashigaru Terminal otomatik olarak ilk karıştırma döngüsünü başlatacaktır.



![Image](assets/fr/11.webp)



Tx0 onaylandıktan sonra, ilk coinjoin işlemi Ashigaru Terminali tarafından otomatik olarak oluşturulacak ve yayınlanacaktır. Hesaplar > Postmix > UTXO'lar'a giderek, ilk döngülerinin onaylanmasını bekleyen eşitlenmiş UTXO'larınızı görüntüleyebilirsiniz.



![Image](assets/fr/12.webp)



Artık Ashigaru Terminal'i arka planda çalışır durumda bırakabilirsiniz: parçalarınızı otomatik olarak karıştırmaya ve remikslemeye devam edecektir.



## Eş birleşimlerin tamamlanması



Artık madeni paralarınızın kendilerini otomatik olarak yeniden karıştırmasına izin verebilirsiniz. Whirlpool modeli, yeniden karıştırma için ekstra ücret alınmadığı anlamına gelir: hizmet ücreti yok, mining ücreti yok. Dolayısıyla, coin'lerinizin daha fazla karıştırma döngüsüne katılmasına izin vermek yalnızca gizliliğinize fayda sağlayabilir.



Bu mekanizmayı ve kaç döngü beklemeye değer olduğunu daha iyi anlamak için bu makaleyi okumanızı tavsiye ederim:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Parçalarınızın her biri tarafından gerçekleştirilen remiks sayısını görüntülemek için, `Postmix` hesabındaki `UTXOs` menüsünü açın.



![Image](assets/fr/13.webp)



Karışık paralarınızı harcamak için, Ashigaru Terminal yazılımınızla aynı wallet'yi kullanan Ashigaru uygulamasına gidin. Açılışta görüntülenen wallet, `Deposit` hesabınıza karşılık gelir. Karma UTXO'larınızı içeren `Postmix` hesabına erişmek için, sağ üst köşedeki Whirlpool sembolüne tıklayın.



![Image](assets/fr/14.webp)



Bu hesapta, şu anda karıştırılmakta olan tüm paralarınızı göreceksiniz. Bunları harcamak için ekranın sağ altındaki `+` sembolüne basın ve ardından `Gönder`i seçin.



![Image](assets/fr/15.webp)



İşleminizin ayrıntılarını doldurun: alıcının adresi, gönderilecek tutar ve isterseniz gizliliğinizi daha da artırmak için belirli bir işlem yapısı seçin (ilgili eğitimlere bakın).



![Image](assets/fr/16.webp)



İşlem ayrıntılarını dikkatlice kontrol edin, ardından gönderiyi onaylamak için ekranın altındaki oku sürükleyin.



![Image](assets/fr/17.webp)



İşleminiz imzalanmış ve Bitcoin ağında yayınlanmıştır.



![Image](assets/fr/18.webp)



## Doxxic Değişim Harcayın



Unutmayın: Whirlpool'ün modeli, taşlarınızın havuzlara girmeden önce Tx0'da eşitlenmesine dayanır. UTXO'ların takibini bozan da bu mekanizmadır. Bence bu en verimli coinjoin modeli, ancak bir dezavantajı var: coinjoin sürecinden geçmeyen bir *değişim* üretiyor.



Bu değişiklik, her Tx0 için oluşturulan bir UTXO'e karşılık gelir. Diğer UTXO'larınızla birlikte kullanılmasını önlemek için yazılıma bağlı olarak `Doxxic Change` veya `Bad Bank` adlı belirli bir hesapta izole edilir. Bu çok önemlidir, çünkü bu UTXO'lar karıştırılmamıştır: izlenebilirlik bağlantıları bozulmadan kalır ve sizinle coinjoin etkinliğiniz arasında bir bağlantı kurarak gizliliğinizi tehlikeye atabilirler. Bu nedenle bunları dikkatli kullanın ve karıştırılmış olsun ya da olmasın **asla diğer UTXO'larla** birlikte kullanmayın. Toksik bir UTXO'i karışık bir UTXO ile birleştirmek, coinjoining'den elde ettiğiniz tüm gizlilik kazanımlarını silecektir.



Şu an için Ashigaru bu `Doxxic Change` hesabına doğrudan erişim sunmuyor (en azından ben bulamadım). Bu özellik muhtemelen gelecekteki bir güncellemede eklenecektir. Bu arada, bu fonları geri almanın tek yolu seed'unuzu Sparrow Wallet'e aktarmaktır. İkincisi normalde bunun wallet ile kullanılan bir Whirlpool olduğunu otomatik olarak algılayacak ve size `Doxxic Change` hesabı da dahil olmak üzere dört hesaba erişim verecektir. Daha sonra bu UTXO'ları Sparrow'den normal bitcoinler gibi harcayabilirsiniz.



İşte döviz UTXO'larınızı coinjoins'ten gizliliğinizden ödün vermeden yönetmek için birkaç olası strateji:





- Onları daha küçük havuzlara karıştırmak:** Eğer toksik UTXO'niz daha küçük bir havuza katılacak kadar büyükse, bu genellikle en iyi seçenektir. Ancak dikkatli olun, bunu başarmak için asla birkaç toksik UTXO'yu birleştirmeyin, çünkü bu Whirlpool'deki çeşitli girişleriniz arasında bir bağlantı oluşturacaktır.





- Harcanamaz olarak işaretleyin:** Bir başka ihtiyatlı yaklaşım da bunları ayrı hesaplarında olduğu gibi tutmak ve dokunmadan bırakmaktır. Bu, yanlışlıkla onları harcamanızı önleyecektir. Bitcoin'in değeri artarsa, boyutlarına göre uyarlanmış yeni havuzlar açılabilir.





- Bağış yapın:** Bu zehirli UTXO'ları Bitcoin geliştiricilerine, açık kaynaklı projelere veya BTC kabul eden derneklere bağışa dönüştürmeyi seçebilirsiniz. Bu, ekosistemi desteklerken bunları faydalı bir şekilde elden çıkarmanıza olanak tanır.





- Ön ödemeli hediye kartları veya Visa kartları satın alın:** [Bitrefill](https://www.bitrefill.com/) gibi platformlar, bitcoinlerinizi mağazalarda kullanılabilecek hediye kartları veya yeniden yüklenebilir Visa kartları ile değiştirmenize olanak tanır. Bu, toksik UTXO'larınızı harcamak için basit ve gizli bir yol olabilir.





- Bunları Monero ile takas edin:** Samourai Wallet artık kullanılmayan bir BTC/XMR atomik takas hizmeti sunuyordu. Benzer bir hizmet varsa (şahsen bilmiyorum), bu UTXO'ları izole etmek, Monero'ya dönüştürmek ve sonunda Bitcoin'e geri göndermek için mükemmel bir çözümdür. Ancak, bu yöntem pahalı ve mevcut likiditeye bağlıydı.





- Bunları Lightning Network'ya aktarın:** Düşük işlem ücretlerinden yararlanmak için bu UTXO'ları Lightning Network'ya aktarmak potansiyel olarak ilginç bir seçenektir. Ancak, bu yöntem Lightning kullanımınıza bağlı olarak belirli bilgileri açığa çıkarabilir ve bu nedenle dikkatli kullanılmalıdır.



## Coinjoin döngülerimizin kalitesi hakkında nasıl bilgi edinebilirim?



Bir coinjoin'in gerçekten etkili olabilmesi için, girdi ve çıktı miktarları arasında yüksek derecede tekdüzelik sunması gerekir. Bu tekdüzelik, dışarıdan bir gözlemci için olası yorumların sayısını artırır ve bu da işlem hakkındaki belirsizliği artırır. Bu belirsizliği ölçmek için işleme uygulanan entropi kavramını kullanırız. Whirlpool modeli, katılımcılar arasında mükemmel homojenliği garanti ettiği için bu açıdan en etkili modellerden biri olarak kabul edilmektedir. Bu ilkeye daha derinlemesine bir bakış için BTC 204 eğitim kursunun 5. Bölümünün son kısmına bakmanızı tavsiye ederim.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Birkaç coinjoin döngüsünün performansı, bir madeni paranın gizlendiği kümelerin büyüklüğü ile ölçülür. Bu kümeler *anonset* olarak bilinen kümeleri tanımlar. İki tür vardır: ilki geriye dönük analiz karşısında gizliliği ölçer (günümüzden geçmişe), ikincisi ise ileriye dönük analize direnci ölçer (geçmişten günümüze). Bu iki göstergenin tam açıklaması için lütfen aşağıdaki öğreticiyi (veya bir kez daha BTC 204 eğitim kursunu) okuyun:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Postmiks nasıl yönetilir?



Birkaç coinjoin döngüsü çalıştırdıktan sonra, en iyi strateji UTXO'larınızı `Postmix' hesabında tutmak ve gerçekten harcamanız gerekene kadar süresiz olarak remiks yapmalarına izin vermektir.



Bazı kullanıcılar karışık bitcoinlerini wallet donanımıyla güvence altına alınmış bir wallet'e aktarmayı tercih etmektedir. Bu seçenek mümkündür, ancak coinjoins ile elde edilen gizliliğin tehlikeye atılmamasını sağlamak için belirli bir titizlik gerektirir.



UTXO'ların birleştirilmesi en sık yapılan hatadır. Karışık UTXO'ları asla aynı işlemde karıştırılmamış UTXO'larla birleştirmemek önemlidir, aksi takdirde *Common Input Ownership Heuristic (CIOH)* tetikleme riskiyle karşı karşıya kalırsınız. Bu, özellikle açık ve kesin etiketleme yoluyla UTXO'larınızın titiz bir şekilde yönetilmesi anlamına gelir. Genel olarak konuşursak, UTXO'ların birleştirilmesi kötü bir uygulamadır ve kötü yönetildiğinde genellikle gizlilik kaybına yol açar.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Karma UTXO'ları konsolide etme konusunda da dikkatli olmalısınız. UTXO'ların önemli anonimleri varsa sınırlı konsolidasyonlar düşünülebilir, ancak bunlar kaçınılmaz olarak gizlilik düzeyinizi azaltır. Karışım öncesi ve sonrası parçalarınız arasında çıkarımsal bağlantılar kurabileceğinden, yeterli sayıda remiksten önce gerçekleştirilen büyük veya aceleye getirilmiş konsolidasyonlardan kaçının. Şüphe durumunda, en iyisi postmix UTXO'larınızı birleştirmemek ve her seferinde yeni bir boş alım adresi oluşturarak bunları tek tek wallet donanımınıza aktarmaktır. Aktarılan her UTXO'i etiketlemeyi unutmayın.



Postmix UTXO'larınızı azınlık betikleri kullanarak portföylere taşımamanızı şiddetle tavsiye ederiz. Örneğin, Whirlpool'ye `P2WSH'deki bir multi-sig portföyünden katıldıysanız, bu tür bir komut dosyasını paylaşan çok az kişi olacaktır. Postmix UTXO'larınızı bu aynı tip betiğe göndererek anonimliğinizi önemli ölçüde azaltmış olursunuz. Senaryo türünün ötesinde, diğer belirli wallet parmak izleri gizliliğinizi tehlikeye atabilir, bu nedenle yapılacak en iyi şey bunları Ashigaru uygulamasından harcamaktır.



Son olarak, tüm Bitcoin işlemlerinde olduğu gibi, bir alıcı adresini asla tekrar kullanmayın. Her ödeme yeni, benzersiz, boş bir adrese gönderilmelidir.



En basit ve güvenli yöntem, karışık UTXO'larınızı `Postmix' hesaplarında dinlendirmek, doğal olarak yeniden karışmalarına izin vermek ve yalnızca Ashigaru'dan ihtiyaç duyulduğunda harcamaktır.



Ashigaru ve Sparrow cüzdanları, blok zinciri analiziyle ilişkili en yaygın hatalara karşı ek korumalar içermekte ve işlemlerinizin gizliliğini korumanıza yardımcı olmaktadır.