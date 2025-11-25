---
name: Seedkeeper x SeedSigner
description: Seedkeeper'ı SeedSigner'ım ile nasıl kullanabilirim?
---

![cover](assets/cover.webp)



*Satochip](https://satochip.io/) ekibine bu eğitimde [videolarını](https://www.youtube.com/@satochip/videos) yeniden kullanmayı kabul ettikleri için teşekkür ederiz. Ayrıca [Crypto Guide]'a (https://www.youtube.com/@CryptoGuide/) SeedSigner ürün yazılımının fork'ı için teşekkürler, akıllı kartlar için destek sağlar



---

SeedSigner, genellikle bir Raspberry Pi Zero etrafında, standart donanımdan kendiniz monte ettiğiniz bir wallet donanımıdır. Bu wallet "*durumsuz*" olarak adlandırılır: piyasadaki diğer modellerin (Coldcard, Trezor, Ledger, vb.) aksine, kalıcı bellekte herhangi bir veri depolamaz ve yalnızca RAM'den canlı olarak çalışır. Sonuç olarak, portföyünüzün seed'ü hiçbir zaman SeedSigner'da saklanmaz. Her yeniden başlattığınızda, cihazın işlemlerinizi imzalamasını sağlamak için bunu doldurmanız gerekecektir. En yaygın yöntem, seed'ünüzü bir QR kodu olarak kaydetmek ve daha sonra her kullandığınızda bu kodu taramaktır (*SeedQR*).



Ancak bu yaklaşım önemli bir riski de beraberinde getirir: seed'ün taranabilmesi için açık metin olarak erişilebilir kalması gerekir. Hırsızlık veya izinsiz giriş durumunda, bir saldırgan bunu kolayca ele geçirebilir ve bitcoinlerinizi çalabilir.



Bu zayıflığın üstesinden gelmek için SeedSigner, Satochip tarafından geliştirilen bir akıllı kart olan [**Seedkeeper**](https://satochip.io/product/seedkeeper/) ile birleştirilebilir. Bu, anımsatıcı ifadelerin (veya diğer sırların) bir PIN kodu ile korunan bir secure element'te saklanmasını sağlar. Seedkeeper uygulaması açık kaynaklıdır ve secure element'i EAL6+ sertifikasına sahiptir. SeedSigner ile birlikte kullanıldığında çok ilginç bir güvenlik özelliği sunar: anahtarlarınız tamamen çevrimdışı olarak yönetilir, işlemlerinizi güvenilir bir ekranda imzalarsınız ve seed fiziksel saldırılara karşı dayanıklı bir akıllı kartta fiziksel olarak korunur.



Kurulumu tamamlamak için ihtiyacınız olan tek şey aşağıdaki öğelerdir:




- Klasik bir SeedSigner için gereken olağan ekipmanlar: bir Raspberry Pi Zero, bir Waveshare 1.3" ekran, uyumlu bir kamera ve bir microSD kart (aşağıdaki SeedSigner eğitiminde daha fazla ayrıntı bulacaksınız);
- SeedSigner uzatma kiti, [resmi Satochip mağazasında] (https://satochip.io/product/seedsigner-extension-kit/) mevcuttur, bu da akıllı kartı doğrudan SeedSigner'ınızdan okumanızı ve yazmanızı sağlar. Diğer bir seçenek ise Raspberry Pi üzerindeki Micro-USB portuna kablo ile bağlanabilen harici bir akıllı kart okuyucu kullanmaktır. Ancak, bu çözümü kendim test etmedim;
- Bir Seedkeeper veya alternatif olarak Seedkeeper uygulamasının yükleneceği boş bir akıllı kart (Satochip tarafından satılan eklenti kiti zaten boş bir akıllı kart içerir).



![Image](assets/fr/01.webp)



Bu eğitim iki senaryoyu kapsamaktadır:




- SeedSigner'ınız aracılığıyla yönetilen bir Bitcoin portföyünüz zaten varsa, yeni aygıt yazılımını yüklemeniz yeterlidir. Daha sonra mevcut wallet'inizi kullanmaya devam edebilir, bu kez daha fazla güvenlik için Seedkeeper'ı kullanabilirsiniz.
- Henüz SeedSigner'ınızla ilişkilendirilmiş bir Bitcoin wallet'ünüz yoksa, aşağıda belirtilen eğitimin **5** ve **6** adımlarını izlemeniz gerekecektir. Bu bölümler SeedSigner ile bir anımsatıcı ifadeyi nasıl generate yapacağınızı, bunu bir *SeedQR* aracılığıyla nasıl kaydedeceğinizi ve ardından bu wallet'ü yönetmek için Sparrow Wallet'ye nasıl bağlayacağınızı açıklamaktadır. Bu prosedürlere burada girmeyeceğim ve **Sparrow ve SeedSigner'ınızla yapılandırılmış, çalışan bir Bitcoin wallet'ünüz olduğunu varsayıyorum**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Ürün yazılımını yükleme



SeedSigner'ınızı bir Seedkeeper ile kullanmak için, akıllı kart okumayı desteklemek amacıyla orijinal SeedSigner'ınkinden farklı alternatif bir ürün yazılımı yüklemeniz gerekir. Bunun için "*3rdIteration*"](https://github.com/3rdIteration/seedsigner) adresindeki fork'ü kullanmanızı tavsiye ederim. Kullandığınız Raspberry Pi modeline karşılık gelen [görüntünün en son sürümünü](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) indirin.



![Image](assets/fr/02.webp)



Henüz sahip değilseniz, [Balena Etcher] yazılımını indirin (https://etcher.balena.io/), ardından aşağıdaki şekilde devam edin:




- MicroSD kartı bilgisayarınıza takın;
- Launch Etcher ;
- Yeni indirdiğiniz `.zip` dosyasını seçin;
- Hedef olarak microSD kartı seçin;
- "Flash!" üzerine tıklayın.



![Image](assets/fr/03.webp)



İşlem tamamlanana kadar bekleyin: microSD'niz artık kullanıma hazırdır. Artık cihazınızı monte etmeye geçebilirsiniz.



Aygıt yazılımı kurulumu ve yazılım doğrulaması (atmanızı şiddetle tavsiye ettiğim bir adım) hakkında daha fazla bilgi için aşağıdaki eğitime bakın:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Akıllı kart okuyucunun montajı



![video](https://youtu.be/jqE8HDMCImA)



Kamerayı Raspberry Pi Zero'ya takarak başlayın, dikkatlice kamera pimine yerleştirin ve siyah tırnakla kilitleyin. Ardından Pi'yi kasanın altına yerleştirin ve bağlantı noktalarını ilgili açıklıklarla hizaladığınızdan emin olun.



![Image](assets/fr/04.webp)



Ardından akıllı kart okuyucuyu Raspberry Pi Zero'nun GPIO pinlerine takın.



![Image](assets/fr/05.webp)



Plastik kapağı akıllı kart okuyucunun üzerine doğru konumlanana kadar kaydırın.



![Image](assets/fr/06.webp)



Ardından ekranı uzantının GPIO pinlerine ekleyin.



![Image](assets/fr/07.webp)



Son olarak, aygıt yazılımını içeren microSD kartı Raspberry Pi Zero'nun yan portuna takın.



![Image](assets/fr/08.webp)



Artık SeedSigner'ınızı Raspberry Pi Zero'nun Micro-USB portu veya uzantının USB-C portu üzerinden bağlayabilirsiniz. Her iki seçenek de çalışır. Başlangıç için birkaç saniye bekleyin, ardından karşılama ekranının göründüğünü göreceksiniz.



![Image](assets/fr/09.webp)



SeedSigner'ınızın ilk kurulumu hakkında daha fazla ayrıntı için aşağıdaki öğreticiyi tavsiye ederim:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Seedkeeper uygulaması ile bir akıllı kartı flaş edin (isteğe bağlı)



![video](https://youtu.be/NF4HemyEcOY)



Zaten bir Seedkeeper'ınız varsa, bu adımı atlayabilir ve doğrudan 4. adıma geçebilirsiniz. Bu bölümde, Seedkeeper uygulamasının boş bir akıllı karta nasıl kurulacağına bakacağız (DIY yöntemi).



Başlamak için SeedSigner'ınızda `Araçlar > Akıllı Kart Araçları` menüsünü açın.



![Image](assets/fr/10.webp)



Ardından `DIY Tools > Install Applet` öğesini seçin.



![Image](assets/fr/11.webp)



Akıllı kartınızı çipi aşağı bakacak şekilde SeedSigner okuyucusuna yerleştirin, ardından `SeedKeeper` uygulamasını seçin.



![Image](assets/fr/12.webp)



Lütfen kurulum sırasında sabırlı olun: işlem birkaç on saniye sürebilir.



![Image](assets/fr/13.webp)



Uygulama başarıyla yüklendikten sonra 4. adıma geçebilirsiniz.



![Image](assets/fr/14.webp)



## 4. Seedkeeper'da mevcut bir SeedQR'yi kaydetme



![video](https://youtu.be/X-vmFHU9Ec8)



Artık Seedkeeper'ınız çalışır durumda olduğuna göre, Bitcoin wallet anımsatıcınızı akıllı karta kaydedebilirsiniz. Başlamak için, SeedSigner'ınızı her zamanki gibi açın, ardından wallet'nızın *SeedQR*'sini cihaza yüklemek için tarayın. seed içe aktarıldıktan sonra, sadece `Bitti` seçeneğini seçin.



![Image](assets/fr/15.webp)



seed yüklendiğinde, `Yedek Tohum` menüsüne erişin.



![Image](assets/fr/16.webp)



Ardından Seedkeeper'ınızı SeedSigner sürücüsüne yerleştirin ve `To SeedKeeper` seçeneğini seçin.



![Image](assets/fr/17.webp)



SeedSigner daha sonra sizden Seedkeeper'ınız için bir PIN kodu girmenizi isteyecektir. Bu boş bir kart olduğu için henüz bir kod tanımlanmamıştır. Bu adımı atlamak için herhangi bir kod girin ve ardından doğrulayın.



![Image](assets/fr/18.webp)



SeedSigner, Seedkeeper'ın henüz başlatılmadığını algılar (yani şifre belirlenmemiştir). Devam etmek için `Anladım` seçeneğine tıklayın.



![Image](assets/fr/19.webp)



Şimdi Seedkeeper'ınızın yeni PIN kodunu 4 ila 16 karakter arasında seçin. Daha fazla güvenlik için uzun, rastgele bir kod seçin: bu, anımsatıcı ifadenize fiziksel erişimi koruyan tek engeldir.



Bu PIN'i oluşturulur oluşturulmaz güvenilir bir parola yöneticisine veya stratejinize bağlı olarak ayrı bir fiziksel ortama kaydetmeyi unutmayın. İkinci durumda, PIN'i içeren ortamı asla Seedkeeper'ınızla aynı yerde tutmadığınızdan emin olun, aksi takdirde koruma etkisiz hale gelecektir. Yedek bir kopyaya sahip olmak önemlidir: **Bu PIN olmadan seed'unuza erişemezsiniz ve bitcoinleriniz kaybolur**.



![Image](assets/fr/20.webp)



Daha sonra anımsatıcı ifadenizle ilişkili bir `Etiket` tanımlayabilirsiniz. Bu etiket, Seedkeeper'da birkaç gizli bilgi saklıyorsanız, bunları kolayca tanımlayabilmeniz için kullanışlıdır.



![Image](assets/fr/21.webp)



Anımsatıcı ifadeniz artık akıllı karta kaydedilmiştir.



![Image](assets/fr/22.webp)



Güvenlik stratejisi açısından, ihtiyaçlarınıza ve riske maruz kalma düzeyinize bağlı olarak çeşitli yaklaşımlar mümkündür. Şahsen, seed'nizin en az 2 kopyasını saklamanızı tavsiye ederim:




- Bu, adres doğrulama veya işlem imzalama gibi günlük işlemler için kolayca erişilebilir tutabileceğiniz akıllı kartlar için bir ilktir. Bu yöntem pratiktir (5. bölümde göreceğimiz gibi) ve PIN kodunun sunduğu koruma sayesinde güvenliğini korur, böylece büyük bir risk olmadan erişilebilir durumda tutabilirsiniz;
- Şifrelenmemiş anımsatıcı ifadenizin ikinci bir kopyası, yalnızca Seedkeeper'ın kaybolması veya çalınması durumunda kullanılmak üzere portföyünüzün nihai yedeği olarak hizmet eder. Bu versiyon şifrelenmemiş olduğundan, 2 yedeğin aynı anda tehlikeye girmesini önlemek için ayrı ve daha güvenli bir yerde tutulmalıdır.



Koruma stratejinize ve risk profilinize bağlı olarak, seed'i birkaç farklı Seedkeeper'da çoğaltabilir veya anımsatıcının birkaç fiziksel kopyasını oluşturabilirsiniz. Bu uygulamalar hakkında daha fazla bilgi edinmek için aşağıdaki eğitime göz atın:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Seedkeeper'dan bir seed yükleniyor



![video](https://youtu.be/ms0Iq_IyaoE)



Artık Seedkeeper'ınızı kullanarak başlangıçta anımsatıcı ifadenizi SeedSigner'a yükleyebilir ve böylece Bitcoin işlemlerinizi imzalayabilirsiniz. Başlamak için SeedSigner'ınızı fişe takarak açın, ardından `Seeds' menüsünü açın.



![Image](assets/fr/23.webp)



Ardından `From SeedKeeper` seçeneğini seçin.



![Image](assets/fr/24.webp)



Seedkeeper'ınızı akıllı kart okuyucusuna yerleştirin, ardından kilidi açmak için PIN kodunuzu girin. Sağ alttaki onay düğmesine, `KEY3`, basarak girişinizi onaylayın.



![Image](assets/fr/25.webp)



Seedkeeper birden fazla gizli bilgi içerebilir, bu nedenle SeedSigner sizden yüklemek istediğinizi seçmenizi ister. Görüntülenen etiket 4. adımda tanımladığınız isme karşılık gelir. Benim durumumda olduğu gibi, yalnızca bir seed kaydettiyseniz, yalnızca bir seçenek mevcut olacaktır.



![Image](assets/fr/26.webp)



seed'iniz şimdi yüklenmiştir. Ekranda görüntülenen parmak izini Sparrow Wallet ayarlarınızda belirtilenle karşılaştırarak bunun doğru wallet olup olmadığını kontrol edin. Bu parmak izi, wallet ilk oluşturulduğunda da sağlanmıştır.



Eğer bir passphrase kullanıyorsanız, bu aşamada uygulayabilirsiniz (bu eğitimin 6. bölümüne bakın). Aksi takdirde, sadece `Bitti` üzerine tıklayın.



![Image](assets/fr/27.webp)



Daha sonra wallet'unuzu her zamanki gibi kullanabilirsiniz: klasik bir SeedSigner'da olduğu gibi teslimat adreslerinizi kontrol edebilir ve işlemleri imzalayabilirsiniz. Nasıl kullanılacağı hakkında daha fazla bilgi edinmek için özel eğitime bakın :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Seedkeeper'ı bir passphrase BIP39 ile kullanma



Bitcoin portföyünüzü korumak için bir passphrase mi kullanıyorsunuz? seed'inizin yanı sıra Seedkeeper'ınıza da kaydedebilirsiniz. Bu çözüm, her kullandığınızda passphrase'yi küçük tuş takımına manuel olarak girmek zorunda kalmadan wallet'ünüzü SeedSigner'a hızlı bir şekilde yüklemenizi sağlayacaktır.



Bu yöntemi özellikle ilginç buluyorum, çünkü passphrase'nın güvenlik avantajlarından faydalanmanızı sağlarken, günlük kullanımıyla ilgili kısıtlamaları ortadan kaldırıyor. İşte size tavsiye edebileceğim bir yapılandırma örneği:




- seed ve passphrase'nizi güçlü bir PIN koduyla korunan bir Seedkeeper'da saklayın (bu önemlidir). Bu yedekleme wallet'inizi günlük olarak kolayca kullanmanızı sağlayacaktır. Dilerseniz bu bilgileri ikinci bir Seedkeeper'da çoğaltabilirsiniz;
- Ayrıca anımsatıcınızın ve passphrase'ın net bir kopyasını kağıt veya metal üzerinde saklayın. Bu, Seedkeeper'ınızı veya PIN kodunu kaybetmeniz durumunda son çare olarak başvuracağınız yedektir. Bu kopyaları ayrı yerlerde sakladığınızdan emin olun, böylece aynı anda ele geçirilemezler.



Bu yapılandırmada, birisi sadece düz metin anımsatıcınızı ele geçirirse, passphrase'i bilmeden hiçbir şey çalamaz (tabii ki kaba kuvvet saldırısına dayanacak kadar güçlü olması şartıyla). Tersine, birisi passphrase'inizi düz metin olarak keşfederse, ilgili anımsatıcı ifade olmadan kullanılamaz durumda kalacaktır.



Son olarak, eğer birisi seed ve passphrase'yi içeren Seedkeeper'ınıza fiziksel erişim sağlamayı başarırsa, PIN kodunu bilmeden hiçbir şey çıkaramayacaktır. passphrase'den farklı olarak, akıllı kart 5 geçersiz denemeden sonra kendini otomatik olarak kilitlediğinden, bu kod kaba kuvvetle zorlanamaz.



Bu nedenle bu konfigürasyonun güvenliği 2 temel noktaya dayanmaktadır:




- Bir **passphrase strong**: uzun, rastgele olmalı ve çok çeşitli karakterler içermelidir. Karmaşıklığı sizin için bir sorun değildir, çünkü başlatma sırasında klavyede yalnızca bir kez girmeniz gerekecektir; daha sonra Seedkeeper tarafından iletilecektir;
- Seedkeeper için bir **güçlü PIN kodu**: ayrıca rastgele ve 16 karakterden oluşur.



Bu kurulumu ayarlamak için, passphrase'inizi her zamanki gibi SeedSigner'a yükleyerek başlayın. Bu eğitimde ayrıntılı olarak açıklanan prosedürü takip edebilirsiniz:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

passphrase içeren portföyünüz SeedSigner'a doğru şekilde yüklendikten sonra, `Seeds' menüsünü açın ve bu portföye karşılık gelen ayak izini seçin. Bu ayak izinin passphrase içermeyen portföyün ayak izinden farklı olduğunu unutmayın.



![Image](assets/fr/28.webp)



Ardından `Yedek Tohum'a tıklayın, Seedkeeper'ı sürücüye yerleştirin ve `To SeedKeeper'ı seçin.



![Image](assets/fr/29.webp)



Seedkeeper'ın kilidini açmak için PIN kodunuzu girin, ardından bu sırra bir etiket atayın. Bir tür makul inkar edilebilirlik sağlamak için parmak izini etiket olarak bırakabilir veya örneğin `Passphrase Wallet` ifadesini açıkça belirtebilirsiniz.



![Image](assets/fr/30.webp)



passphrase portföyünüz artık Seedkeeper'da kayıtlıdır.



![Image](assets/fr/31.webp)



Bir dahaki sefere başlattığınızda, Seedkeeper'ınızı sürücüye takın ve ardından `Seeds > From SeedKeeper` seçeneğine gidin.



![Image](assets/fr/32.webp)



Akıllı kartın kilidini açmak için PIN kodunuzu girin, ardından passphrase'unuza karşılık gelen wallet'yi seçin.



![Image](assets/fr/33.webp)



passphrase ve wallet baskınızı kontrol edin, ardından onaylayın.



![Image](assets/fr/34.webp)



Artık portföyünüze passphrase ile erişebilir ve işlemlerinizi normalde bir SeedSigner'da yaptığınız gibi imzalayabilirsiniz.



## 7. Ek seçenekler



Araçlar > Akıllı Kart Araçları menüsünde, Seedkeeper'ınızı yönetmek için çeşitli seçenekler bulacaksınız:





- Ortak Araçlar` menüsünde şunları yapabilirsiniz:
 - Kartın gerçekliğini kontrol edin;
 - PIN kodunu değiştirin ;
 - Sırlarınızla ilişkili etiketleri değiştirin ;
 - NFC işlevini devre dışı bırakın (yalnızca çip okuyucu kullanıyorsanız önerilir) ;
 - Fabrika ayarlarına sıfırlama gerçekleştirin.





- SeedKeeper İşlevleri` menüsünde şunları yapabilirsiniz:
 - Kayıtlı sırların listesine bakın ;
 - Yeni bir sır kaydedin ;
 - Mevcut bir sırrı silme ;
 - Tanımlayıcılarınızı kaydedin veya yükleyin (multi-sig portföyleri için yararlı işlev).





- DIY Araçları` menüsünde şunları yapabilirsiniz:
 - Seedkeeper uygulamasının derlenmesi ;
 - Uygulamayı boş bir karta yükleyin ;
 - Bir Seedkeeper uygulamasını sıfırlamak ve tekrar boş hale getirmek için silin.



Artık SeedSigner ile birlikte portföyünüzü güvenli bir şekilde yedeklemek için Seedkeeper'ı nasıl kullanacağınızı biliyorsunuz.



Bu kurulum sizi ikna ettiyse, bunu mümkün kılan projeleri desteklemekten çekinmeyin:




- Ekipmanınızı doğrudan [Satochip web sitesinden] satın alarak (https://satochip.io/shop/);
- SeedSigner projesine bağışta bulunarak] (https://seedsigner.com/donate/);
- Crypto Guide'ın YouTube kanalına] (https://www.youtube.com/@CryptoGuide/) abone olarak, değiştirilmiş ürün yazılımını barındıran GitHub deposunu yöneten kişi tarafından yönetilir.