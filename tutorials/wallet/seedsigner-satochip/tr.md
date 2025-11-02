---
name: Satochip x SeedSigner
description: SeedSigner'ınızla bir Satochip nasıl kullanılır?
---

![cover](assets/cover.webp)



*Bu eğitimde kullanacağımız akıllı kart desteği için SeedSigner ürün yazılımının Fork'ı için [Crypto Guide]'a (https://www.youtube.com/@CryptoGuide/) teşekkürler



---

Satochip, en yüksek güvenlik standartlarından biri olan EAL6+ sertifikalı güvenlik unsuruna sahip, akıllı kart formatında bir Hardware Wallet'dir. Aynı adı taşıyan Belçikalı şirket tarafından tasarlanmış ve üretilmiştir: Satochip.



Fiyatı yaklaşık 25 € olan Satochip, parasının karşılığını mükemmel bir şekilde vermesiyle rakiplerinden ayrılıyor. Güvenli çipi sayesinde fiziksel saldırılara karşı dayanıklılık sunuyor. Dahası, uygulamasının kaynak kodu tamamen açık kaynaklıdır ve *AGPLv3* altında lisanslanmıştır.



Öte yandan, formatı bazı işlevsel sınırlamalar getirmektedir. Satochip'in en büyük dezavantajı entegre bir ekrana sahip olmamasıdır: kullanıcılar bu nedenle işlemleri yalnızca bilgisayarlarının ekranına güvenerek kör bir şekilde imzalamak zorundadır.



Bu zayıflığın üstesinden gelmek için, özellikle ilginç bir yapılandırma, bir SeedSigner ile birlikte kullanmaktır. Bu kurulumda iletişim artık doğrudan bilgisayar ve Satochip arasında değil, bilgisayar ve SeedSigner arasında QR kodu alışverişi yoluyla gerçekleşir. SeedSigner daha sonra bir güven ekranı görevi görür: imzalanacak bilgileri gösterirken, imzanın kendisi Satochip tarafından gerçekleştirilir. Geleneksel SeedSigner kullanımının (hatta Seedkeeper ile birlikte kullanımının) aksine, seed hiçbir zaman SeedSigner'a yüklenmez. Böylece SeedSigner, Satochip'in ekranı haline gelir ve kör imzalama ile ilişkili riskleri ortadan kaldırır.



Soruna başka bir açıdan bakacak olursak, SeedSigner'ı bir Satochip ile kullanmak SeedSigner'daki büyük bir boşluğu doldurur: seed'ü bir secure element içinde saklama ve kullanma yeteneği.



Bence bu yapılandırma, geleneksel donanım cüzdanlarına göre çeşitli avantajlar sunuyor:




- Satochip'in maliyeti yaklaşık 25 €'dur ve uygulama açık kaynaklı olduğu için boş bir akıllı karta kendiniz yükleyebilirsiniz. Daha sonra SeedSigner bileşenlerinin maliyetini ve akıllı kartları okumak için uzantıyı eklemeniz gerekir: bu donanımı nereden satın aldığınıza bağlı olarak, toplam 70 ila 100 € arasında olmalıdır.
- Kurulumda yer alan tüm yazılımlar açık kaynaklıdır: SeedSigner aygıt yazılımı ve Satochip uygulaması.
- Sertifikalı bir güvenlik unsurundan faydalanırsınız.
- Yapılandırma, açıkça Bitcoin kullanımı için tasarlanmış donanıma başvurmadan, tamamen kendin yap şeklinde gerçekleştirilebilir; bu da bir tür makul inkar edilebilirlik ve belirli dış tehditlere (ülkeye bağlı olarak devlet baskısı dahil) karşı direnç sağlayabilir. Bölgenizde ticari donanım cüzdanlarına erişim kısıtlıysa ya da imkansızsa bu da ilginç bir çözümdür.




## 1. Gerekli malzemeler



Bu kurulumu gerçekleştirmek için aşağıdaki öğelere ihtiyacınız olacaktır:




- Klasik bir SeedSigner tarafından ihtiyaç duyulan olağan ekipman :
 - gPIO pinleri olan bir Raspberry Pi Zero,
 - 1.3" Waveshare ekran,
 - uyumlu bir kamera,
 - bir microSD kart.



![Image](assets/fr/01.webp)





- SeedSigner uzatma kiti, [resmi Satochip mağazasından](https://satochip.io/product/seedsigner-extension-kit/) temin edilebilir, bu kit doğrudan SeedSigner'ınızdan bir akıllı kartı okumanızı ve yazmanızı sağlar. Diğer bir seçenek ise Raspberry Pi üzerindeki Micro-USB portuna kablo ile bağlanabilen [harici bir akıllı kart okuyucu](https://satochip.io/product/chip-card-reader/) kullanmaktır. Ancak, bu çözümü kendim test etmedim;
- [Bir Satochip](https://satochip.io/product/satochip/) veya alternatif olarak Satochip uygulamasının yükleneceği bir [boş akıllı kart](https://satochip.io/product/card-for-diy-project/) (Satochip tarafından satılan uzatma kiti zaten boş bir akıllı kart içerir). Satochip'in uzantı kiti [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/) formatını da desteklemektedir. Bu yüzden tercih ederseniz bu formatı seçebilirsiniz.



![Image](assets/fr/02.webp)



SeedSigner'ı monte etmek için gereken ekipman hakkında daha fazla bilgi için lütfen bu diğer eğitimin 1. Bölümüne bakın:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Ürün yazılımını yükleme



SeedSigner'ınızı bir Satochip ile kullanmak için, akıllı kart okumayı desteklemek amacıyla orijinal SeedSigner'ınkinden farklı alternatif bir ürün yazılımı yüklemeniz gerekir. Bunun için "**3rdIteration**"](https://github.com/3rdIteration/seedsigner) adresindeki Fork'yı kullanmanızı tavsiye ederim. Kullandığınız Raspberry Pi modeline karşılık gelen [görüntünün en son sürümünü](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) indirin.



![Image](assets/fr/03.webp)



Henüz sahip değilseniz, [Balena Etcher] yazılımını indirin (https://etcher.balena.io/), ardından aşağıdaki şekilde devam edin:




- MicroSD kartı bilgisayarınıza takın;
- Launch Etcher ;
- Yeni indirdiğiniz `.zip` dosyasını seçin;
- Hedef olarak microSD kartı seçin;
- "Flash!" üzerine tıklayın.



![Image](assets/fr/04.webp)



İşlem tamamlanana kadar bekleyin: microSD'niz artık kullanıma hazırdır. Artık cihazınızı monte etmeye geçebilirsiniz.



Aygıt yazılımı kurulumu ve yazılım doğrulaması (atmanızı şiddetle tavsiye ettiğim bir adım) hakkında daha fazla bilgi için aşağıdaki eğitime bakın:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Akıllı kart okuyucunun montajı



Kamerayı Raspberry Pi Zero'ya takarak başlayın, dikkatlice kamera pimine yerleştirin ve siyah tırnakla kilitleyin. Ardından Pi'yi kasanın altına yerleştirin ve bağlantı noktalarını ilgili açıklıklarla hizaladığınızdan emin olun.



![Image](assets/fr/05.webp)



Ardından akıllı kart okuyucuyu Raspberry Pi Zero'nun GPIO pinlerine takın.



![Image](assets/fr/06.webp)



Plastik kapağı akıllı kart okuyucunun üzerine doğru konumlanana kadar kaydırın.



![Image](assets/fr/07.webp)



Ardından ekranı uzantının GPIO pinlerine ekleyin.



![Image](assets/fr/08.webp)



Son olarak, aygıt yazılımını içeren microSD kartı Raspberry Pi Zero'nun yan portuna takın.



![Image](assets/fr/09.webp)



Artık SeedSigner'ınızı Raspberry Pi Zero'nun Micro-USB portu veya uzantının USB-C portu üzerinden bağlayabilirsiniz. Her iki seçenek de çalışır. Başlangıç için birkaç saniye bekleyin, ardından karşılama ekranının göründüğünü göreceksiniz.



![Image](assets/fr/10.webp)



SeedSigner'ınızın ilk kurulumu hakkında daha fazla ayrıntı için aşağıdaki eğitimin 4. bölümüne bakmanızı tavsiye ederim:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Satochip uygulaması ile bir akıllı kartı flaş edin (isteğe bağlı)



Zaten bir Satochip'iniz varsa, bu adımı atlayabilir ve doğrudan 4. adıma geçebilirsiniz. Bu bölümde, Satochip uygulamasını boş bir akıllı karta nasıl yükleyeceğimize bakacağız (DIY yöntemi). Uygulama, akıllı kart üzerinde çalışan ve belirli işlevleri yönetmemizi sağlayan küçük bir programdır.



Başlamak için SeedSigner'ınızda `Araçlar > Akıllı Kart Araçları` menüsünü açın.



![Image](assets/fr/11.webp)



Ardından `DIY Tools > Install Applet` öğesini seçin.



![Image](assets/fr/12.webp)



Akıllı kartınızı SeedSigner okuyucusuna çip aşağı bakacak şekilde yerleştirin ve `Satochip` uygulamasını seçin.



![Image](assets/fr/13.webp)



Lütfen kurulum sırasında sabırlı olun: işlem birkaç on saniye sürebilir.



![Image](assets/fr/14.webp)



Uygulama başarıyla yüklendikten sonra 4. adıma geçebilirsiniz.



![Image](assets/fr/15.webp)




## 5. seed oluşturma ve kaydetme



### 5.1. generate seed



Artık tüm donanım ve yazılımınız düzgün çalıştığına göre, Bitcoin portföyünüzü oluşturmaya devam edebilirsiniz. Bunu yapmak için SeedSigner'ınızı takın, ardından geleneksel bir SeedSigner'da olduğu gibi zar atarak veya fotoğraf çekerek seed'nizi generate yapın:




- Araçlar > Kamera / Zar Ruloları menüsüne gidin;
- Ardından seçilen yönteme göre entropi oluşturma sürecini takip edin;
- Son olarak, seed'ü fiziksel ortama yedekleyin ve yedeği dikkatlice kontrol edin.



![Image](assets/fr/16.webp)



Bu prosedürün ayrıntılarını görmek isterseniz, lütfen bu eğitimin 5. bölümünü izleyin:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. seed'ün bir Seedkeeper'a kaydedilmesi



seed oluşturulduktan sonra, SeedSigner'ın RAM'inde bulunduğu tek zaman budur. Benim durumumda, sırları saklamak için tasarlanmış bir başka Satochip ürünü olan [Seedkeeper] (https://satochip.io/product/seedkeeper/) üzerine kaydetmek istiyorum. Bu cihazı, Satochip'imin kaybolması durumunda son çare olarak kullanacağım.



Burada seçilen yedekleme stratejisi tercihlerinize bağlıdır, ancak Mnemonic ifadenizin fiziksel ortamda (kağıt veya metal) veya burada olduğu gibi bir Seedkeeper'da en az bir kopyasının olması zorunludur. Ayrıca yedekleme sayısını gerektiği kadar çoğaltabilirsiniz. Portföy yedekleme stratejileri hakkında daha fazla bilgi için bu eğitimi okumanızı öneririm:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

seed'nizi bir Seedkeeper'da yedeklemek için doğrudan `seed'yi Yedekle` menüsüne gidin.



![Image](assets/fr/17.webp)



Ardından Seedkeeper'ınızı akıllı kart okuyucusuna takın ve `To SeedKeeper` seçeneğini seçin.



![Image](assets/fr/18.webp)



Kilidi açmak için PIN kodunuzu girin.



![Image](assets/fr/19.webp)



Seedkeeper'da saklanan farklı gizli dizilerinizi kolayca tanımlamak için bir `Etiket` seçin. Örneğin, sadece Wallet'in parmak izini saklayabilir veya açıkça `seed'u belirtebilirsiniz. Seçim sizin tercihinize ve riskinize bağlıdır.



![Image](assets/fr/20.webp)



Yedekleme stratejiniz yalnızca bu Seedkeeper'a dayanıyorsa, şimdi boş bir kurtarma testi yapmanızı ve ardından yedeklemenin çalışıp çalışmadığını kontrol etmek için parmak izlerini karşılaştırmanızı şiddetle tavsiye ederim.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper PIN kodu, kartın fiziksel olarak ele geçirilmesi durumunda kaba kuvvet girişimlerini önlemek için mümkün olduğunca uzun ve rastgele olmalıdır. Ayrıca bu PIN kodunun yedek bir kopyasını Seedkeeper'dan ayrı bir yerde saklamalısınız. Bu PIN kodu olmadan Seedkeeper'da saklanan Mnemonic'ye erişemezsiniz ve bitcoinleriniz sonsuza kadar kaybolur.



### 5.3. seed'i Satochip'e kaydedin



Portföyünüz oluşturulduğuna, kaydedildiğine ve kontrol edildiğine göre şimdi onu Satochip'e aktaracağız. Bunu yapmak için, seed'nin SeedSigner'ın RAM'ine yüklendiğinden emin olun. Ardından `Araçlar > Akıllı Kart Araçları > Satochip İşlevleri` bölümüne gidin.



![Image](assets/fr/21.webp)



Satochip'inizi akıllı kart okuyucusuna takın, ardından `seed ile Başlat` seçeneğini seçin.



![Image](assets/fr/22.webp)



Cihaz sizden Satochip PIN kodunu girmenizi ister; kart yeni ve başlatılmamış olduğu için henüz PIN kodu yoktur. Bu adımı atlamak için herhangi bir kod girin (engelleyici bir kod değildir).



![Image](assets/fr/23.webp)



SeedSigner, Satochip'inizin başlatılmadığını tespit eder. Onaylamak için `Anladım` seçeneğine tıklayın.



![Image](assets/fr/24.webp)



Daha sonra Satochip PIN kodunu 4 ila 16 karakter arasında ayarlayabilirsiniz. Wallet'inizin güvenliğini güçlendirmek için uzun, rastgele bir kod seçin: bu, Mnemonic ifadenize fiziksel erişime karşı tek korumadır.



Kişisel stratejinize bağlı olarak, bu PIN'i oluşturulur oluşturulmaz güvenli bir şifre yöneticisine veya fiziksel bir ortama kaydetmeyi unutmayın. İkinci durumda, PIN'i içeren ortamı asla Satochip'inizle aynı yerde saklamadığınızdan emin olun, aksi takdirde koruma işe yaramaz hale gelecektir. Yedek bir kopyaya sahip olmak önemlidir: **Bu PIN olmadan, artık seed'nıza erişemezsiniz ve bitcoinleriniz kalıcı olarak kaybolur**.



![Image](assets/fr/25.webp)



SeedSigner daha sonra Satochip'e hangi seed'yi aktaracağınızı sorar. Parmak izi yeni oluşturduğunuz portföy ile eşleşeni seçin.



![Image](assets/fr/26.webp)



seed'iniz şimdi Satochip'e aktarıldı.



![Image](assets/fr/27.webp)



Artık SeedSigner'ınızı kapatabilirsiniz.



Wallet'unuzun güvenliğini artırmak için bir passphrase BIP39 kullanmak isterseniz, lütfen bu eğitimin 6. bölümüne bakın:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Wallet'yi Sparrow'e aktarın



Artık portföyünüz hazır ve çalışır durumda olduğuna göre, genel bilgilerini ("*keystore*") Sparrow wallet veya başka bir portföy yönetim yazılımına aktaracağız. Bu yazılım işlemlerinizi oluşturmak, dağıtmak ve takip etmek için kullanılacaktır. Ancak, bu işlem için gereken özel anahtarlar yalnızca Satochip'te (ve herhangi bir yedekte) bulunduğundan, bunları imzalayamayacaktır.



### 6.1 SeedSigner ve Satochip'in Hazırlanması



İşletim sistemini içeren microSD kartı takın, ardından SeedSigner'ınızı açın. Henüz seed'ünüzü tanımadığı için şu an için hiçbir şey yapamaz. Satochip'i akıllı kart okuyucuya takarak başlamanız gerekecek, çünkü seed'ünüzü tutan kart bu.



Ana ekrandan `Araçlar > Akıllı Kart Araçları > Satochip İşlevleri` menüsüne erişin.



![Image](assets/fr/28.webp)



Ardından `Export Xpub` seçeneğine tıklayın.



![Image](assets/fr/29.webp)



Portföy türünü seçin. Bizim durumumuzda, bu tek bir portföydür: `Single Sig` seçeneğini seçin.



![Image](assets/fr/30.webp)



Ardından komut dosyası standardı seçimi gelir. En yenisini seçin: `Native SegWit`.



![Image](assets/fr/31.webp)



Son olarak, `Koordinatör`ü, yani kullanmak istediğiniz portföy yönetim yazılımını seçin. Biz burada Sparrow wallet'yı kullanacağız.



![Image](assets/fr/32.webp)



Bir uyarı mesajı görüntülenir: bu tamamen normaldir. Genişletilmiş açık anahtar (`xpub`), seed'nizden (ilk hesapta) türetilen tüm adresleri görüntülemenizi sağlar. Bununla birlikte, fonlarınıza erişim sağlamaz: ifşa edilmesi gizliliğinizi tehlikeye atar, ancak bitcoinlerinizin güvenliğini tehlikeye atmaz. Başka bir deyişle, bakiyelerinizi gözlemlemenize izin verir, ancak onları harcamanıza izin vermez.



Anlıyorum'a tıklayın.



![Image](assets/fr/33.webp)



Ardından kilidi açmak için Satochip'inizin PIN kodunu girin. Bu, 5. adımda tanımladığınız ve kaydettiğiniz koddur.



![Image](assets/fr/34.webp)



Son olarak, görüntülenen bilgilerden memnunsanız `Export Xpub` seçeneğine tıklayın.



![Image](assets/fr/35.webp)



SeedSigner daha sonra portföyünüzü Sparrow wallet'de yönetmek için ihtiyaç duyduğunuz tüm verileri içeren dinamik bir QR kodu şeklinde xpub'ınızı oluşturur. QR kodunun taranmasını kolaylaştırmak için joystick'i kullanarak ekranın parlaklığını ayarlayabilirsiniz.



### 6.2 Yeni bir portföyü Sparrow wallet'a aktarma



Sparrow wallet yazılımının bilgisayarınızda yüklü olduğundan emin olun. Nasıl indireceğinizi, orijinalliğini nasıl kontrol edeceğinizi ve doğru şekilde nasıl yükleyeceğinizi bilmiyorsanız, konuyla ilgili eksiksiz eğitimimize bakın:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Bilgisayarınızda Sparrow wallet'i açın, ardından menü çubuğunda `Dosya → Wallet'yi İçe Aktar'a tıklayın.



![Image](assets/fr/36.webp)



SeedSigner'a kaydırın ve ardından `Tara...` öğesini seçin. Web kameranız etkinleştirilecektir: SeedSigner ekranınızda görüntülenen dinamik QR kodunu tarayın.



![Image](assets/fr/37.webp)



Portföyünüze bir isim verin, ardından `Wallet Oluştur`a tıklayın. Sparrow daha sonra sizden bu Wallet'ya yerel erişimi kilitlemek için bir parola belirlemenizi isteyecektir. Güçlü bir parola seçin: Sparrow'teki verilerinizi korur (genel anahtarlar, adresler, etiketler ve işlem geçmişi). Ancak, bu parola gelecekte Wallet'yı geri yüklemek için gerekli değildir: yalnızca Mnemonic ifadeniz (ve muhtemelen passphrase'ünüz) gerekli olacaktır.



Kaybetmemek için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.



![Image](assets/fr/38.webp)



Anahtar deponuz başarıyla içe aktarıldı.



![Image](assets/fr/39.webp)



Şimdi Sparrow wallet'de görüntülenen `Ana parmak izi`nin daha önce SeedSigner'ınızda bulunanla eşleşip eşleşmediğini kontrol edin.



SeedSigner daha sonra içe aktarımın geçerliliğini onaylamak için Sparrow wallet'inizden rastgele bir alıcı Address'u taramanızı isteyecektir.



![Image](assets/fr/40.webp)



Satochip'iniz (SeedSigner aracılığıyla) ve Sparrow wallet artık güvenli bir şekilde bağlı. Satochip, işlemlerinizi imzalayabilen tek cihaz olarak kalırken Sparrow, Interface'in tam bir yönetimi olarak hizmet eder. Artık tamamen hava boşluklu bir konfigürasyonda bitcoin almaya ve göndermeye hazırsınız.



![Image](assets/fr/41.webp)



## 7. Bitcoin alma ve gönderme



Satochip ve Sparrow wallet'ünüz artık birlikte çalışacak şekilde yapılandırılmıştır. Bu bölümde, bu modda nasıl bitcoin alacağınızı ve göndereceğinizi adım adım açıklayacağız.



### 7.1 Bitcoin alma



#### 7.1.1 Bir alım Address oluşturulması



Bilgisayarınızda Sparrow wallet'i açın ve şifrenizi kullanarak `Satochip-SeedSigner` Wallet'nın kilidini açın. Yazılımın bir sunucuya bağlı olduğunu kontrol edin (sağ alttaki gösterge). Ardından, kenar çubuğunda `Al` seçeneğine tıklayın.



![Image](assets/fr/42.webp)



Yeni bir Bitcoin Address görünür. Bulacaksın :




- Metin biçiminde Address (bu örnekte olduğu gibi P2WPKH kullanıyorsanız `bc1q...` ile başlar) ;
- İlgili QR kodu ;
- İşlemlerinizi izlemek için yararlı bir `Etiket` alanı.



Wallet'nizdeki her bir Bitcoin makbuzuna bir etiket eklemenizi şiddetle tavsiye ederim. Bu, her bir UTXO'ün kaynağını kolayca belirlemenize ve gizliliğinizi daha iyi yönetmenize yardımcı olacaktır. Bu önemli konu hakkında daha fazla bilgi edinmek için Plan ₿ Academy'deki özel eğitime göz atın:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Etiket eklemek için `Etiket` alanına bir isim girmeniz ve ardından onaylamanız yeterlidir.



Örneğin:



```txt
Label : Sale of the Raspberry Pi Zero
```



Address'ünüz artık tüm Sparrow bölümlerinde bu etiketle ilişkilendirilmiştir.



![Image](assets/fr/43.webp)



#### 7.1.2 SeedSigner üzerinde Address doğrulaması



Alıcı Address'inizi ödeyene iletmeden önce, bunun seed'inize ait olduğunu kontrol etmek önemlidir. Bu adım, Satochip'inizin daha sonra bu Address ile ilişkili işlemleri imzalayabilmesini sağlar. Ayrıca Sparrow'un sahte bir Address göstereceği olası saldırıları da önler. Sparrow'un, saldırı yüzeyi tamamen izole edilmiş olan Satochip'inizinkinden çok daha büyük olan güvensiz bir ortamda (bilgisayarınız) çalıştığını unutmayın. Bu nedenle Hardware Wallet'nizde kontrol etmeden önce Sparrow'da görüntülenen adreslere asla körü körüne güvenmemelisiniz.



Sparrow'de, büyütmek için Address'in QR koduna tıklayın: daha sonra tam ekran görüntülenecektir.



![Image](assets/fr/44.webp)



SeedSigner'ınızda Satochip'i okuyucuya yerleştirin, ardından ana menüden `Tara` seçeneğini seçin. Bilgisayarınızda görüntülenen QR kodunu tarayın ve ardından `Satochip kartını kullan` seçeneğini seçin.



![Image](assets/fr/45.webp)



Ardından kullanılan komut dosyasını onaylayın (bu durumda, `Native SegWit`), kilidi açmak için Satochip PIN kodunu girin ve `xpub` bilgilerini doğrulayın.



![Image](assets/fr/46.webp)



Taranan Address, seed'inizden elde edilenle eşleşirse, SeedSigner mesajı görüntüleyecektir: `Address Doğrulandı`.



![Image](assets/fr/47.webp)



Böylece Address'nın portföyünüze ait olduğundan emin olabilirsiniz.



#### 7.1.3 Fonların teslim alınması



Artık bu Address'i metin biçiminde veya QR kodu aracılığıyla size Satss göndermesi gereken kişiye veya hizmete iletebilirsiniz. İşlem ağ üzerinde yayınlandıktan sonra, Sparrow wallet'nin `İşlemler` sekmesinde görünecektir.



![Image](assets/fr/48.webp)



### 7.2 Bitcoin gönderin



Satochip-SeedSigner yapılandırması ile bitcoin göndermek 3 adımdan oluşur:




- Sparrow'da işlem oluşturma ;
- Bu işlemin Satochip üzerinde SeedSigner aracılığıyla imzalanması;
- Son olarak, işlem Sparrow'den ağ üzerinden yayınlanır.



İki cihaz arasındaki tüm alışverişler yalnızca QR kodları aracılığıyla gerçekleşir.



#### 7.2.1 Sparrow'de işlem oluşturma



Sparrow wallet'de, sol taraftaki kenar çubuğunda bulunan `Gönder` sekmesine tıklayarak bir işlem oluşturabilirsiniz. Ancak ben *Coin Kontrolü* uygulamanıza olanak tanıyan `UTXOs` sekmesini kullanmayı tercih ediyorum. Bu yöntem, işlemleriniz sırasında ortaya çıkan bilgileri sınırlamak için harcanan UTXO'lar üzerinde hassas kontrol sunar.



UTXOs sekmesinde, harcamak istediğiniz madeni paraları seçin ve ardından `Seçilenleri Gönder` seçeneğine tıklayın.



![Image](assets/fr/49.webp)



Ardından işlem alanlarını doldurun:




- 'Ödeme yapılacak' kısmına alıcının Address'ünü yapıştırın veya kamera simgesini kullanarak QR kodunu tarayın;
- Etiket` alanına, bu gideri izlemek için bir etiket ekleyin;
- Tutar` alanına gönderilecek tutarı girin;
- Son olarak, mevcut şebeke koşullarına göre şarj oranını seçin (tahminler [Mempool.space](https://Mempool.space/) adresinde mevcuttur).



Tüm alanları doldurduktan sonra bilgileri dikkatlice gözden geçirin ve ardından `İşlem Oluştur >>` seçeneğine tıklayın.



![Image](assets/fr/50.webp)



İşlem ayrıntılarını doğruluk açısından son bir kez kontrol edin ve ardından `İmzalama için İşlemi Sonlandır` seçeneğine tıklayın.



![Image](assets/fr/51.webp)



İşlem artık hazırdır, ancak henüz imzalanmamıştır. PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) QR kodu olarak görüntülemek için `Kareyi Göster` seçeneğine tıklayın.



![Image](assets/fr/52.webp)



#### 7.2.2 Satochip ile işlemin imzalanması



SeedSigner'ınızı açın ve Satochip'inizi her zamanki gibi takın. Ana ekrandan `Tarama` yı seçin, ardından Sparrow üzerinde görüntülenen QR kodunu tarayın.



![Image](assets/fr/53.webp)



Satochip kartı kullan` seçeneğini seçin.



![Image](assets/fr/54.webp)



Akıllı kartın kilidini açmak için PIN kodunuzu girin.



![Image](assets/fr/55.webp)



SeedSigner bunun bir PSBT olduğunu algılar ve işlemin bir özetini görüntüler:




   - Gönderilen miktar,
   - Hedef adresler,
   - İlişkili işlem maliyetleri.



Ayrıntıları İncele'ye tıklayın ve tüm bilgileri doğrudan SeedSigner ekranında inceleyin. Kontrol edilmesi gereken en önemli noktalar gönderilen tutarlar, varış adresleri ve işlem ücretleridir.



![Image](assets/fr/56.webp)



Her şey yolundaysa, Satochip'i kullanarak işlemi imzalamak için `PSBT'ı Onayla'yı seçin.



![Image](assets/fr/57.webp)



İmza tamamlandığında, SeedSigner imzalanan işlemi içeren ve Sparrow tarafından taranmaya hazır yeni bir QR kodu oluşturur.



#### 7.2.3 İşlemin Sparrow'den yayınlanması



İşlem imzalandığına ve doğrulandığına göre, geriye kalan tek şey Bitcoin ağında yayınlamaktır, böylece bir Miner bunu bir BLOCK'e dahil edebilir. Sparrow'te `Karekodu Tara'ya tıklayın.



![Image](assets/fr/58.webp)



SeedSigner'ınızda görüntülenen QR kodunu (imzalanmış işlemi içeren) web kamerasına gösterin. Sparrow daha sonra tüm işlem detaylarını görüntüleyecektir. Tüm bilgilerin doğru olup olmadığını son bir kez kontrol edin ve ardından Bitcoin ağında yayınlamak için "İşlemi Yayınla" seçeneğine tıklayın.



![Image](assets/fr/59.webp)



İşleminiz artık ağa iletilmiştir. Onayını Sparrow wallet'un `İşlemler` sekmesinden takip edebilirsiniz.



![Image](assets/fr/60.webp)



## 8. Wallet'ünüzü geri alın



Önceki bölümlerde gördüğümüz gibi, güvenlik stratejinize bağlı olarak, Satochip'inize ek olarak kurtarma ifadenizi yedeklemenin birkaç yolu vardır:




- SeedSigner ile klasik bir *SeedQR* kullanmak;
- Mnemonic ifadesini fiziksel bir ortama kaydederek;
- Ya da bölüm 5.2'de açıklandığı gibi bir Seedkeeper'da depolayarak.



Her durumda, müdahale etmeniz gereken 2 ana durum vardır: Satochip'in kaybı veya SeedSigner'ın kaybı. Şimdi bu senaryoların her birinde nasıl tepki vereceğinize bir göz atalım.



### 8.1. Satochip ile Wallet'nizi geri alın



Satochip'iniz hala sizdeyse ancak SeedSigner'ınız bozulmuş veya kaybolmuşsa, Wallet'ünüz hala Satochip'in içinde olduğu için durumu yönetmek oldukça basittir.



En iyi seçenek, gerekli bileşenleri tavsiye etmek ve sıfırdan yeni bir SeedSigner inşa etmektir. Bu "durumsuz" bir cihaz olduğundan, aynı veya başka bir SeedSigner kullanmanız fark etmez: Satochip'inizi yerleştirebildiğiniz sürece her şey normal şekilde çalışacaktır.



Yeniden oluşturmak istemiyorsanız, Satochip'inizi klasik şekilde, yani SeedSigner'dan geçmeden doğrudan bilgisayarınızdan da kullanabilirsiniz. Bu yöntem mükemmel çalışır, ancak Bitcoin Wallet'inizin güvenliğini önemli ölçüde azaltır: "*hava boşluklu*" izolasyonu kaybedersiniz ve SeedSigner güvenilir bir ekran görevi gördüğü için artık kör olarak imzalamanız gerekir. Ancak bu, acil bir durumda veya bir SeedSigner'ı yeniden oluşturamadığınız durumlarda geçici bir çözüm olabilir.



Bunu yapmak için bir USB akıllı karta veya NFC okuyucuya ihtiyacınız olacaktır. Geri yüklemek istediğiniz Wallet'yi Sparrow'da açın, ardından `Ayarlar` sekmesine gidin ve `Değiştir` seçeneğine tıklayın.



![Image](assets/fr/61.webp)



Satochip'inizi bilgisayara bağlı akıllı kart okuyucusuna takın, ardından `Satochip'in yanındaki `İçe Aktar'a tıklayın.



![Image](assets/fr/62.webp)



Son olarak, kilidi açmak için akıllı kart PIN kodunuzu girin. Ardından Wallet'inize erişebilecek, işlemler oluşturabilecek ve bağlı Satochip'i kullanarak bunları doğrudan imzalayabileceksiniz.



### 8.2. SeedSigner ile portföyünüzü geri alın



Diğer, daha hassas senaryo ise seed içeren Satochip'inize erişiminizi kaybetmenizdir: kırılmış, kaybolmuş, çalınmış veya PIN kodunu unutmuş olabilirsiniz. Satochip'iniz çalındıysa veya kaybolduysa, fonlarınıza erişiminiz yeniden sağlandıktan sonra bitcoinlerinizi derhal farklı bir seed ile oluşturulan yepyeni bir Wallet'a aktarmanızı şiddetle tavsiye ederiz. Bu, potansiyel bir saldırganın Sat'lerinize asla erişememesini sağlar.



Portföyünüze yeniden erişim kazanmak ve fonlarınızı taşımak için seed'inizi SeedSigner'a yüklemeniz yeterlidir. Kullandığınız yedekleme ortamına bağlı olarak, birkaç seçeneğiniz vardır:





- Mnemonic cümlenizi `Seeds > Enter 12-word seed` menüsüne manuel olarak girin.



![Image](assets/fr/63.webp)





- Ana sayfadaki `Tara` düğmesine tıklayarak *SeedQR*'nizi tarayın.



![Image](assets/fr/64.webp)





- Ya da seed'ünüzü bir Seedkeeper'dan `Seeds > From SeedKeeper` menüsü aracılığıyla yükleyebilirsiniz (bu eğitimde kullandığım yöntem budur). Basitçe Seedkeeper PIN kodunu girmeniz ve SeedSigner'da seed olarak kullanılacak sırrı seçmeniz gerekecektir.



![Image](assets/fr/65.webp)



seed SeedSigner'a yüklendikten sonra, hangi yöntemi kullanırsanız kullanın, bitcoinlerinizi yeni, tehlikesiz bir Wallet'e taşımak için bir veya daha fazla tarama işlemi imzalayabileceksiniz. Bunu nasıl yapacağınızı öğrenmek için aşağıdaki eğitimin 7.2 bölümüne bakın:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Artık SeedSigner ile birlikte Bitcoin portföyünüzü güvenli bir şekilde yönetmek için Satochip'i nasıl kullanacağınızı biliyorsunuz.



Bu kurulum sizi ikna ettiyse, bunu mümkün kılan projeleri desteklemekten çekinmeyin:




- Ekipmanınızı doğrudan [Satochip web sitesinden] satın alarak (https://satochip.io/shop/);
- SeedSigner projesine bağışta bulunarak] (https://seedsigner.com/donate/);
- Crypto Guide'ın YouTube kanalına] (https://www.youtube.com/@CryptoGuide/) abone olarak, bu eğitimde kullandığımız değiştirilmiş ürün yazılımını barındıran GitHub deposunu yöneten kişi tarafından yönetilir.