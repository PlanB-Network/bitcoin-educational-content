---
name: COLDCARD Mk

description: Coldcard cihazı ve Bitcoin core ile bir Bitcoin özel anahtarı oluşturma, yedekleme ve kullanma
---

![cover](assets/cover.webp)


_Coldcard cihazı ve Bitcoin Core ile bir Bitcoin özel anahtarı oluşturma, yedekleme ve kullanma_


## Coldcard kullanarak özel bir anahtar oluşturmak ve bunu Bitcoin core düğümünüzün Interface'i aracılığıyla kullanmak için eksiksiz kılavuz!


Bitcoin'nın ağ kullanımının özünde asimetrik kriptografi kavramı yatmaktadır: verileri şifreleyen ve şifresini çözen bir çift anahtar - biri özel diğeri genel - iletişimin gizliliğini sağlayan bir kavram.


Bitcoin durumunda, böyle bir özel ve açık anahtar çifti oluşturarak bitcoinleri (UTXO veya Harcanmamış İşlem Çıktısı) depolayabilir ve bunları harcamak için işlemleri imzalayabiliriz.


Günümüzde, cüzdanların bir Mnemonic cümlesini (seed cümlesi) şifreleme anahtarlarıyla nasıl ilişkilendireceğini belirleyen bir standart olan BIP 39'u kullanarak özel bir anahtarın rastgele oluşturulmasını ve metinsel biçimde yedeklenmesini kolaylaştıran birden fazla araç mevcuttur. Çoğu zaman, Mnemonic cümlesi 12 veya 24 kelimeden oluşur ve bir Wallet'u ve bitcoinlerini kurtarabilmek için güvenli bir şekilde yedeklenmesi gerekir.


Bu yazıda, Bitcoin dünyasında en yaygın kullanılan ve güvenli cihazlardan biri olan Coldcard Mk4 kullanarak, maksimum entropi sağlamak için zar atma yöntemini kullanarak bir özel anahtarın nasıl generate yapılacağını ve Bitcoin core ile hava boşluklu bir şekilde nasıl kullanılacağını öğreneceğiz!


**Not:🧰** Kılavuzu kullanmak için aşağıdaki araçları edinin:



- Soğuk kart cihazı (Mk3 veya Mk4)
- MicroSD kart (4GB yeterlidir)
- Yalnızca güç sağlayan manyetik USB kablosu (Mk3 için mini-usb, Mk4 için usb-c)
- Bir veya daha fazla kalite zarı


## Coldcard ile yeni bir Mnemonic cümlesi oluşturma


Sıfırdan bir özel anahtar oluşturma sürecine, PIN'in önceden ayarlanmış olduğu yeni açılmış bir Coldcard varsayarak başlayacağız (cihazın başlatılması sırasında Coldcard'daki adımları izleyin).


**Not🚨:** Önceden yapılandırılmış bir Coldcard'ın özel anahtarını sıfırlamak için aşağıdaki adımları izleyin:

_Gelişmiş/Araçlar > Tehlike Bölgesi > seed İşlevleri > seed'yı Yok Et > ✓_


**Dikkat:** Coldcard'ınız bu adımları izleyerek özel anahtarı unutacaktır. Daha sonra kurtarabilmek istiyorsanız Mnemonic ifadenizi düzgün bir şekilde yedeklediğinizden emin olun.


## İzlenecek adımlar:


PIN ile Coldcard'a bağlanın > Yeni seed Kelimeler > 24 Kelime Zar Atma


Her zar atışından sonra 1'den 6'ya kadar elde edilen sonucu Soğuk Karta yazarak 100 zar atışı gerçekleştirin. Bu yöntemi uygulayarak 256 bayt entropi yaratırsınız, böylece tamamen rastgele bir özel anahtar oluşturulmasını desteklersiniz. Coinkite ayrıca entropi oluşturma sistemlerinin bağımsız olarak doğrulanması için gerekli belgeleri de sağlamaktadır.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


100 zar atımı tamamlandıktan sonra ✓ tuşuna basın ve ardından elde edilen 24 kelimeyi sırayla yazın. İki kez doğrulayın ve ✓ tuşuna basın. Son olarak, geriye kalan tek şey Soğuk Kart üzerindeki 24 kelimenin doğrulama testini tamamlamak ve işte, yeni özel anahtarınız oluşturuldu!


Ardından, gösterilen adımları izleyerek NFC (Mk4) ve USB işlevlerini etkinleştirip etkinleştirmeyeceğinizi seçin. Ana menüye girdikten sonra, artık cihazın aygıt yazılımını güncelleme zamanı gelmiştir. Gelişmiş/Araçlar > Aygıt Yazılımını Yükselt > Sürümü Göster seçeneğine gidin ve mevcut en son sürümü doğrulamak ve indirmek için resmi web sitesini kontrol edin. Maksimum güvenlikten faydalanmak için Coldcard'ı güncellemeniz tavsiye edilir.


Devam etmeden önce, özel anahtarla ilişkili Ana Anahtar Parmak İzini (XFP) not etmeniz önerilir. Bu veriler, örneğin kurtarma durumunda doğru Wallet'de olup olmadığınızın hızlı bir şekilde doğrulanmasını sağlar. Gelişmiş/Araçlar > Kimliği Görüntüle > Ana Anahtar Parmak İzi (XFP) seçeneğine gidin ve elde edilen sekiz alfanümerik karakter dizisini not edin. XFP, Mnemonic ifadesiyle aynı yere not edilebilir, hassas veri değildir.


**Not:💡** Mnemonic cümle yedeklemenizi farklı bir yazılımda test etmeniz önerilir. Bunu güvenli bir şekilde yapmak için Bitcoin Wallet yedeğini Tails ile 5 dakikadan kısa sürede doğrulama makalemize bakın.


## Güvenlik Bonusu: "Gizli İfade" (isteğe bağlı)


Bir passphrase (gizli ifade), bitcoinlerinizi korumak için bir Layer güvenlik eklemek amacıyla bir Wallet yapılandırmasına eklemek için harika bir unsurdur. passphrase, Mnemonic ifadesine bir tür 25. kelime olarak işlev görür. Eklendiğinde, özel bir anahtar ve ilişkili Mnemonic ifadesiyle birlikte tamamen yeni bir Wallet oluşturulur. Yeni Mnemonic ifadesini yazmak gerekli değildir, çünkü bu Wallet'ya ilk Mnemonic ifadesini seçilen passphrase ile birleştirerek erişilebilir.


Amaç passphrase'i Mnemonic ifadesinden ayrı olarak not etmektir çünkü her iki öğeye de erişimi olan bir saldırganın fonlara erişimi olacaktır. Öte yandan, bu öğelerden yalnızca birine erişimi olan bir saldırganın fonlara erişimi olmayacaktır ve Wallet yapılandırmasının güvenlik düzeyini optimize eden de bu özel avantajdır.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Coldcard ile passphrase ekleme adımları:


passphrase > Sözcük Ekle (önerilir) > Uygula. Cihaz, yeni oluşturulan Wallet'ün XFP'sini passphrase ile birlikte görüntüleyecektir; daha önce belirtilen aynı nedenlerden dolayı passphrase ile birlikte not edilmelidir.


**İpucu💡** Burada passphrase ile ilgili ek kaynaklar bulunmaktadır:



- [Burada] (https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) _Trezor_ tarafından yazılan ilk kitap var;
- [Burada] (https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) ikincisini _Coinkite_ tarafından bulabilirsiniz;
- Ve [burada] (https://armantheparman.com/passphrase/) sonuncusunu _armantheparman_ tarafından bulacaksınız.


## Wallet'in Bitcoin core'ye aktarılması


Wallet artık Bitcoin ağıyla etkileşim kurmak için yazılıma aktarılmaya hazırdır. Bu kılavuzda Bitcoin core (v24.1) kullanacağız.


Bitcoin core için kurulum ve yapılandırma kılavuzlarımıza bakın:



- **Bitcoin core ile kendi düğümünüzü çalıştırma:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- **Bir Bitcoin core düğümü için Tor yapılandırma:** https://agora256.com/configuration-tor-Bitcoin-core/


İlk olarak, Coldcard'a bir mikro SD kart takın, ardından aşağıdaki adımları izleyerek Wallet'u Bitcoin core için dışa aktarın: Gelişmiş/Araçlar > Wallet'u Dışa Aktar > Bitcoin core. Mikro SD karta iki dosya yazılacaktır: Bitcoin-core.sig & Bitcoin-core.txt. Mikro SD kartı Bitcoin core'nin kurulu olduğu bilgisayara takın ve .txt dosyasını açın. "Ana anahtar parmak izine sahip Wallet için" satırını göreceksiniz Sekiz karakterli XFP'nin özel anahtarınızı oluştururken not ettiğinizle eşleştiğini doğrulayın

Dosyadaki talimatları izlemeden önce, aşağıdaki adımları izleyerek Bitcoin core Interface'deki Wallet'yi hazırlayarak başlayalım: Dosya sekmesine gidin > Bir Wallet oluşturun. Wallet'niz için bir isim seçin (Core'da "porte-monnaie" ile değiştirilebilir terim) ve aşağıdaki resimde gösterildiği gibi Özel anahtarları devre dışı bırak, Boş bir Wallet oluştur ve Wallet tanımlayıcıları seçeneklerini işaretleyin. Ardından, Oluştur düğmesine basın.


![create a wallet](assets/guide-agora/3.webp)


Wallet, Bitcoin core'te oluşturulduktan sonra Pencere sekmesi > Konsol'a gidin ve sayfanın üst kısmında seçilen Wallet'ün oluşturduğunuz Wallet'ün adını gösterdiğinden emin olun.


Şimdi, daha önce Coldcard tarafından oluşturulan .txt dosyasında importdescriptors ile başlayan satırı kopyalayın ve ardından Bitcoin core konsoluna yapıştırın. "success": true satırını içeren bir yanıt döndürülmelidir.


![nodes window](assets/guide-agora/4.webp)


Yanıt "mesaj" içeriyorsa: "Menzilli tanımlayıcıların bir etiketi olmamalıdır" içeriyorsa, .txt dosyasından kopyalanan satırdaki "label": .txt dosyasından kopyalanan satırdaki "Coldcard xxxx0000" yazısını silin, ardından tüm satırı Bitcoin core konsoluna geri yapıştırın.


Gerekirse, Coldcard Github'da [burada] (https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) biraz yardım bulabilirsiniz.


## Bitcoin core'de Wallet ithalatının doğrulanması


İşlemin başarılı olduğundan emin olmak için, istenen Wallet'in Bitcoin core'a aktarıldığını doğrulamak gerekir. Bunu doğrulamak için basit bir yöntem, Soğuk Kartta oluşturulan adreslerin Bitcoin core'ta oluşturulan adreslere karşılık geldiğini doğrulamaktır.


Bitcoin core: Al > Yeni bir alıcı oluştur Address

Soğuk kart: Address Explorer > bc1q ile başlayan Address'i seçin. Soğuk Kart Address 'bc1q', Bitcoin core'te görüntülenen Address ile eşleşmelidir.

'Air-gapped' modunda işlem alma ve gönderme


Bir işlemi almak son derece basittir; sadece Al düğmesine basın, işlemi etiketleyin (isteğe bağlı ancak önerilir) ve yeni bir alıcı Address oluşturun. Daha sonra geriye kalan tek şey Address'yı gönderici ile paylaşmaktır.


Şimdi, bu Coldcard + Bitcoin core kurulumunun kilit unsuru, Bitcoin'in TBSP (PSBT - Kısmen İmzalanmış Bitcoin İşlemleri) işlevini kullanan ve air-gapped adı verilen bir yöntemle, Coldcard ve özel anahtarı internete bağlı olmadan işlem göndermektir.

Esasen, Bitcoin core Interface'i bir işlem oluşturmak için kullanırız, daha sonra bu işlemi mikro SD kart aracılığıyla Coldcard'a aktararak imzalarız ve ardından imzalı işlem dosyasını Bitcoin core'e geri göndererek işlemi ağa yayınlarız. Bunu bu şekilde yapmak zorundayız çünkü Bitcoin core'e aktarılan Wallet'ün özel anahtarı yoktur, yalnızca açık anahtarı vardır (bu da alıcı adreslerimizi generate yapmamızı sağlar), bu nedenle bitcoinlerimizi harcamak için doğrudan yazılımda bir işlem imzalamamız imkansızdır.


Devam etmeden önce, Ayarlar > Wallet bölümünde aşağıdaki seçeneklerin etkin olduğundan emin olun:



- Coin kontrol özelliklerini etkinleştirin
- Onaylanmamış paraları harcayın (İsteğe bağlı)
- TBPS kontrollerini etkinleştirin


![option ](assets/guide-agora/5.webp)


### Hava boşluklu modda gönderme adımları:


Gönder > Girişler > istediğiniz UTXO'i seçin, ardından Ödeme yapılacak yere alıcının Address'sini girin. İşlem ücreti: Seçin... > Özel > İşlem ücretini girin (Bitcoin core, çoğu alternatif Wallet çözümü gibi sat/byte yerine Sats/kilobyte olarak hesaplar. Yani 4000 Sats/kilobyte = 4 Sats/byte). İmzasız bir işlem oluşturun > dosyayı mikro SD kartınıza kaydedin ve Coldcard'a takın.


Coldcard'da İmzalamaya Hazır düğmesine basın, işlem ayrıntılarını doğrulayın, ardından ✓ düğmesine basın ve imzalı dosyalar oluşturulduktan sonra mikro SD kartı bilgisayara geri takın.


Bitcoin core'e geri dönün, Dosya sekmesine gidin > TBSP'yi dosyadan yükleyin ve imzalı işlem dosyasını girin .PSBT. PSBT İşlemleri kutusu ekranda belirecek ve işlemin tamamen imzalandığını ve yayınlanmaya hazır olduğunu onaylayacaktır. Geriye kalan tek şey İşlemi yayınla düğmesine basmaktır.


![PSBT operations](assets/guide-agora/6.webp)


### Sonuç


Coldcard cihazının kendi düğümünüzü çalıştırdığınız Bitcoin core ile kombinasyonu güçlüdür. Buna 100 zar atılarak oluşturulan özel bir anahtar ve gizli bir ifade eklendiğinde Wallet yapılandırmanız sofistike ve sağlam bir kaleye dönüşür.


Yorumlarınızı ve sorularınızı paylaşmak için bizimle iletişime geçmekten çekinmeyin! Amacımız bilgiyi paylaşmak ve anlayışımızı her geçen gün artırmaktır.