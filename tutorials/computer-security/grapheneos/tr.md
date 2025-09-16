---
name: GrapheneOS

description: Android tabanlı güvenlik ve gizliliğe odaklanan bir mobil işletim sistemi
---

![cover](assets/cover.webp)
> [GrapheneOS](https://grapheneos.org/) kâr amacı gütmeyen, açık kaynaklı bir mobil işletim sistemidir; yüksek düzeyde gizlilik ve güvenlik sağlamak üzere tasarlanmış olup Android uygulamalarıyla tamamen uyumlu kalır.

İlk olarak 2014 yılında 'CopperheadOS' olarak kurulan GrapheneOS, geleneksel Android Koduna (AOSP) dayanmaktadır, ancak kullanıcı gizliliğini ve güvenliğini artırmayı amaçlayan birçok değişiklik ve iyileştirme içermektedir. GrapheneOS, telefonlarının kontrolünü büyük teknoloji şirketlerine değil kullanıcıya verir.


![video](https://youtu.be/VnumtalYLFI)

### Sommaire:



- Giriş
- Hazırlık
- Kurulum
- Uygulama Alternatifleri
- Dezavantajları
- Faydalı Bilgiler


*Bu eğitim, [BitcoinQnA tarafından Bitcoiner.Guide üzerinde MIT lisansı altında yayınlanan](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md) orijinal içeriğin bir uyarlamasıdır ve ilk yazım çalışmasının tüm kredisi ona aittir.*


## Neden GrapheneOS kullanılmalı?


Modern telefonlar 500-1000 dolarlık takip ve veri toplama cihazlarıdır. Hayatımızın her bir yönü bu cihazlar aracılığıyla gerçekleşiyor ve ne yazık ki bu verilerin çoğu şu ya da bu şekilde üçüncü taraflarla paylaşılıyor.

GrapheneOS, bu veri paylaşımını azaltmak ve cihazınızın potansiyel saldırı vektörlerine karşı güvenliğini artırmak için özel olarak üretilmiştir. GrapheneOS hesabı diye bir şey yoktur. Uygulamaları indirmek veya işletim sistemiyle etkileşime geçmek için bir hesaba ihtiyacınız yoktur. Basitçe söylemek gerekirse, ürün siz değilsiniz.


GrapheneOS, bazı basit temel ilkeler aracılığıyla Android deneyiminize ek güvenlik sağlar.


1. **Saldırı yüzeyini azaltma** - Gereksiz kodu (veya bloatware'i) kaldırın.

2. **Zafiyete maruz kalmayı önleme** - Kullanıcıya rahat edeceği tehlikeleri seçmesi için yeterli ayrıntı düzeyi sağlayın.

3. **Kum havuzu koruması** - GrapheneOS, mevcut Android kum havuzlarını güçlendirerek her uygulamanın telefonunuzun geri kalanıyla iletişim kurma yeteneğini daha da kilitliyor.


GrapheneOS özellik setinin teknik detayları hakkında daha fazla bilgi edinin [burada](https://grapheneos.org/features).


### Geçişi Kolaylaştırmak


Yıllardır Google veya Apple ekosistemine bağlıysanız, tüm bu kolaylığı bir gecede kaybetme düşüncesi korkutucu olabilir. Ancak dikkatlice düşünülmüş bazı uygulama yükleme kararlarıyla (daha sonra ele alınacaktır), beklenen bu zorluğun çoğu azaltılabilir veya ortadan kaldırılabilir.


Alternatifler ne kadar iyi olursa olsun, böyle bir değişiklik düşüncesi hala itici olabilir. Kendinizi bu durumda bulursanız, en iyi tavsiyem yeni GrapheneOS cihazınızı bir süre mevcut telefonunuzla birlikte çalıştırmanızdır. Bu aşamadan sonra kendinizi sadece GrapheneOS cihazınıza uzanırken bulana kadar haftada 2-3 uygulamadan yavaş yavaş vazgeçebilirsiniz.


Bu yaklaşımı benimserseniz, kendinize karşı katı olun ve gözetlenen alternatiflere olan bağımlılığınızı mümkün olduğunca çabuk kesin. Biz insanlar tembelizdir ve genellikle en az direnç gösteren yolu seçeriz. İlk etapta neden geçiş yaptığınızı hatırlayın.


**Kişisel verilerinizle ödeme yapmak yerine, zamanınızla ve bazen de Hard kazandığınız paranızla (yüklediğiniz alternatif uygulamalara bağlı olarak) ödeme yapmayı seçtiniz.**


## Başlarken


GrapheneOS şu anda yalnızca [Google Pixel](https://grapheneos.org/faq#supported-devices) serisi telefonlar için _(oldukça ironik bir şekilde)_ üretiliyor. Yine de bu iyi bir neden olmadan gelmiyor. Pixel'ler, işletim sistemini sertleştirmek için yapılan çalışmaları tamamlamak üzere en iyi donanım tabanlı güvenliği sunuyor. Bu, belirli bileşen izolasyonları ve doğrulanmış önyükleme gibi şeyleri içerir.


### Bir cihaz seçme


GrapheneOS'u yüklemek istediğiniz Pixel'i seçerken, cihazın varsayılan [güvenlik güncellemelerini] (https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g) ne kadar süreyle almaya devam edeceğini kontrol ettiğinizden emin olun.


Bu yazının yazıldığı sırada Pixel 6a, Temmuz 2027'ye kadar garantili, iyi bir uzun vadeli desteğe sahip en ucuz modeldir. Bu modeli seçerseniz, OEM kilit açma işlemi fabrikadan çıkan stok işletim sistemi sürümüyle çalışmayacaktır. Havadan güncelleme yoluyla Haziran 2022 veya daha sonraki bir sürüme güncellemeniz gerekir. Güncellemeyi yaptıktan sonra OEM kilidi açmayı düzeltmek için cihazı fabrika ayarlarına sıfırlamanız da gerekecektir. Operatör kilidi açık olan diğer tüm modeller kutudan çıkar çıkmaz GrapheneOS için hazır olacaktır.


Bir cihaz seçerken kilitsiz bir versiyon satın aldığınızdan da emin olmak isteyeceksiniz. Verizon gibi bazı operatörler cihazlarını bootloader kilitli olarak gönderirler ve bu da aşağıdaki süreci tamamen engeller.


### GrapheneOS'u Yükleme


GrapheneOS [web yükleyici] (https://grapheneos.org/install/web) tüm süreci çocuk oyuncağı haline getirir ve herkes tarafından 10 dakikadan kısa bir sürede tamamlanabilir.

Aşağıdaki talimatlar, yukarıdaki bağlantıdan alınan kısaltılmış bir versiyondur.


Tek yapmanız gereken:



- Piksel
- Telefondan bilgisayarınıza gitmek için bir USB kablosu
- Bir web tarayıcısını çalıştıracak bir bilgisayar (Chromium tabanlı herhangi bir tarayıcı: Chrome, Edge, Brave, vb.)


Hadi içine dalalım:


1. İlk adım **Ayarlar** > **Telefon hakkında** bölümüne gitmek ve **'Geliştirici Modu'nun** etkinleştirildiğini görene kadar yapı numarasına tekrar tekrar dokunmaktır.

2. Ardından **Ayarlar** > **Sistem** > **Geliştirici Seçenekleri** bölümüne gidin ve **'OEM Kilit Açma'** özelliğini etkinleştirin.

3. Şimdi cihazı yeniden başlatın ve telefon tekrar açılırken ses kısma düğmesini basılı tutun.

4. Telefonu dizüstü bilgisayarınıza bağlayın ve yetkilendirme istenirse bağlantıya izin verin.

5. Web yükleyici sayfasında, 'Önyükleyicinin kilidini aç' seçeneğine tıklayın.

6. Ardından telefon seçeneklerinin değiştiğini göreceksiniz. Seçimi `kilidi aç` olarak değiştirmek için ses düğmesini kullanın ve kabul etmek için güç düğmesini kullanın.

7. Ardından web yükleyici sayfasındaki sürümü indir seçeneğine tıklayın.

8. Tamamen indirildikten sonra, bir sonraki adıma geçin ve 'Flash release'e tıklayın. Bu bir veya iki dakika sürecektir ve telefona hiç dokunmanıza gerek yoktur.

9. Son olarak, web yükleyicisinin bir sonraki adımına geçin ve **Önyükleyiciyi Kilitle** seçeneğine tıklayın. Seçimi değiştirmeniz ve işlemin başlarında yaptığınız gibi güç düğmesiyle onaylamanız gerekecektir.

10. Başlat kelimesini gördüğünüzde, güç düğmesiyle bunu onaylayın ve cihaz yeni Google'sız işletim sisteminize önyükleme yapacaktır.


![image](assets/fr/2.webp)

GrapheneOS başlangıç ekranı



i̇lk önyükleme ve kurulumdan sonra, Ayarlar > Sistem > Geliştirici Seçenekleri'nden OEM kilidini devre dışı bırakmak iyi bir uygulamadır._


_Ayrıca Auditor uygulaması aracılığıyla yüklemeyi doğrulamak için ekstra, isteğe bağlı ancak önerilen adımı atmak isteyebilirsiniz. Bu adımı tamamlamak için uygulamanın yüklü olduğu ayrı bir Android telefona ihtiyacınız olacaktır. Bununla ilgili talimatları [burada] (https://attestation.app/tutorial) bulabilirsiniz._



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Yukarıda özetlenen basit adımları detaylandıran video



Bu basit adımlar çok uzak bir adım gibi görünüyorsa, GrapheneOS yazılımı [önceden yüklenmiş] bir Pixel satın almayı düşünebilirsiniz (https://ronindojo.io/en/roninmobile). Sadece sağlayıcıya küçük bir miktar güven duyduğunuzu unutmayın.


### Önceden Yüklenmiş Uygulamalar


Artık hazır olduğunuza göre, GrapheneOS'un ilk kurulumda ne kadar çıplak göründüğünü fark edebilirsiniz. Varsayılan olarak bu uygulamalar yüklü olacaktır:


![image](assets/fr/3.webp)


Varsayılan uygulamalar


Aşina olmayabileceğiniz sadece iki tanesi 'Denetçi' ve 'Vanadyum'dur.



- Denetçi uygulaması] (https://play.google.com/store/apps/details?id=app.attestation.auditor), işletim sisteminin orijinalliği ve bütünlüğü ile birlikte bir cihazın kimliğini doğrulamak için donanım tabanlı güvenlik özelliklerini kullanır. Cihazın önyükleyici kilitli olarak stok işletim sistemini çalıştırdığını ve işletim sisteminde herhangi bir kurcalama olmadığını doğrulayacaktır.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) Chromium web tarayıcısının gizlilik ve güvenlik açısından güçlendirilmiş bir çeşididir.


## Özelleştirme


Telefon ayarları kişisel bir konudur, ancak GrapheneOS'u yüklerken kendimi daha rahat hissetmek için değiştirdiğim ilk öğelerden bazıları şunlardır.


### Duvar kağıdı ayarlama ve temayı güncelleme


Ayarlar > Duvar Kağıdı ve Stil bölümüne gidin. Buradan:



- Web'den indirilen görüntüler için ana ekran ve kilit ekranı arka planlarını güncelleyin.
- Kullanıcı arayüzü boyunca kullanılan vurgu renklerinin seçilmesi.
- Koyu temayı etkinleştirin.


### Pil yüzdesini göster


Ayarlar** > **Pil** bölümüne gidin, ardından durum çubuğunda **Pil yüzdesini göster** seçeneğini etkinleştirin.


### Kişileri içe aktarma


**Başka bir Android telefondan** - Kişiler uygulamasına gidin ve VCF'ye Aktar seçeneğini arayın.


**iOS'tan** - Export Contact gibi bir uygulama kullanın ve bir VCF dosyasını dışa aktarmak için 'vCard' dışa aktarma seçeneğini kullanın.

VCF dosyasını aldıktan sonra, microSD kart veya USB sürücü gibi harici bir depolama seçeneği ile GrapheneOS cihazınıza aktarabilirsiniz. Elinizde bunlardan herhangi biri yoksa, aşağıda listelenen birçok uygulamadan biri aracılığıyla paylaşmayı tercih edebilirsiniz.


![image](assets/fr/4.webp)


Kişiselleştirilmiş ana ekran



## Alternatif Uygulamalar


Telefonunuzu kullanışlı hale getirmek için bazı uygulamalar yüklemek isteyeceksiniz! Aşağıdaki seçenekler, hepsini kişisel olarak kullandığım veya daha geniş gizlilik topluluğundan güçlü öneriler aldıkları için dahil edilmiştir. Bahsetmediğim daha birçok harika alternatif mevcut ve [Awesome Privacy] (https://awesome-privacy.xyz) her tür cihaz için gizliliği koruyan uygulamaların inanılmaz kapsamlı bir listesini sunuyor.


Bir uygulamanın Özgür ve Açık Kaynak Kodlu Yazılım (FOSS) olması, potansiyel gizlilik sızıntılarından muaf olduğu anlamına gelmez. Tercih ettiğiniz uygulamaların gizlilik denetimlerine karşı nasıl performans gösterdiğini görmek için [Exodus](https://reports.exodus-privacy.eu.org/en/) adresini kullanın.


### F-Droid


[F-Droid](https://f-droid.org/) Android için FOSS uygulamalarının yüklenebilir bir kataloğudur. İstemci, cihazınızdaki uygulamalara göz atmayı, yüklemeyi ve güncellemeyi kolaylaştırır. F-Droid üzerinden yapılan güncellemelerin bazen diğer uygulama mağazalarına göre daha yavaş olabileceğini belirtmek gerekir. Bu, esas olarak uygulamanın ana F-Droid deposu veya özel bir depo aracılığıyla bulunup bulunmadığına bağlıdır.


F-Droid'i yüklemek için GrapheneOS telefonunuzdaki bir tarayıcı aracılığıyla web sitelerine gidin ve indir'e dokunun. Bu bir `.apk` dosyası indirecektir. Daha sonra uygulamayı yüklemek isteyip istemediğiniz sorulacaktır.


F-Droid'deki varsayılan depoda bulunan uygulamaların yanı sıra, birçok Açık Kaynak projesi de F-Droid uygulama ayarlarına eklenebilen kendi depolarını barındıracaktır. Böyle bir durumda, söz konusu proje web sitesinde bunu başarmak için gereken çok basit adımlarda size yol gösterecektir.


![image](assets/fr/5.webp)


F-Droid ana ekranı


https://planb.network/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

### Aurora Mağazası


[Aurora Store](https://auroraoss.com/) Google Play mağazasının bir FOSS sürümüdür. Aurora, geleneksel Play Store'a çok benziyor ve normalde Google seçeneği ile bulabileceğiniz herhangi bir uygulamayı indirmenize ve güncellemenize olanak tanıyor.


Aurora'nın en önemli özelliği anonim oturum açma özelliğidir. Bu, F-Droid veya doğrudan APK aracılığıyla kullanılamayan favori uygulamalarınızdan herhangi birini Google hesabınıza giriş yapmak zorunda kalmadan indirebileceğiniz anlamına gelir.


Bunu varsayılan yükleme seçeneğiniz haline getirmek için acele etmeden önce, uzak durmaya çalıştığımız uygulamaların çoğunun Play Store'dan yüklendiğini unutmayın. Aurora'dan erişilebilir olmaları, bazılarının gömülü izleme özelliklerine sahip olabileceği gerçeğini değiştirmez. Bu her zaman mümkün olmayabilir, ancak mümkün olduğunda Aurora üzerinden indirmeden önce bir F-Droid alternatifi arayın.


Aurora'yı yüklemek için F-Droid'de 'Aurora Store' araması yapmanız yeterlidir.


Aurora'nın bazı potansiyel saldırı vektörleri de var, çünkü "anonim hesaplar" gerçekten Aurora tarafından oluşturuluyor ve kontrol ediliyor. Teorik olarak, kötü amaçlı güncellemeler sunabilir veya uygulamaları telefonunuza gönderebilirler, ancak yine de cihazdaki yükleme istemini kabul etmeniz gerekir. Aurora bazen bölge ve cihaz yanlış okumaları nedeniyle uygulamaların görünmemesiyle ilgili bazı sorunlar da yaşayabiliyor. Bu genellikle aşağıdaki adımlarla aşılabilir.


**En iyi ipucu** - Bazen Aurora Store, uygulama arama ve yükleme yeteneğinizi sınırlayan hız sınırlaması yaşayabilir. Bunu aşmak için **Ayarlar** > **Uygulamalar** > **Aurora** > **Varsayılan olarak aç** bölümüne gidin, ardından `play.google.com` alan adını ekleyin. Şimdi, 'Play Store üzerinden indir' bağlantısına sahip bir ürün veya hizmetin web sitesine gittiğinizde, üzerine dokunduğunuzda, indirmeniz için Aurora içinde o uygulama açılacaktır.



![image](assets/fr/6.webp)


Aurora Store ana ekranı


https://planb.network/tutorials/computer-security/data/aurora-store-b3345da7-1ed1-407e-a9ae-a1c7f0ba9967

### APK İndir


Android'deki uygulamalar bir `.apk' dosyası aracılığıyla da indirilebilir ve yüklenebilir. Bu, sıfır üçüncü taraf uygulama mağazası gerektiren harika bir alternatiftir, dosyayı doğrudan projenin veya hizmetlerin web sitesinden veya GitHub deposundan indirmeniz yeterlidir.


Bu yaklaşımın dezavantajı, otomatik güncelleme alamamanızdır, bu nedenle yeni sürümleri öğrenmek için bu hizmetin iletişim kanallarını izlemeniz gerekir. Ancak bunu düzeltmeyi amaçlayan Obtanium adında harika bir proje var. [Obtainium] (https://github.com/ImranR98/Obtainium), Açık Kaynak uygulamalarını doğrudan sürüm sayfalarından yüklemenize ve güncellemenize ve yeni sürümler kullanıma sunulduğunda bildirim almanıza olanak tanır.


![image](assets/fr/7.webp)


Obtanium önizleme


### Web Uygulamaları


Bir hizmeti nadiren kullanmak isteyebileceğiniz ve yerel bir uygulama indirmek istemediğiniz zamanlar için, web sürümüne kolayca erişebilirsiniz. Günümüzde birçok web sitesi Progressive Web App (PWA) desteği de sunmaktadır. Bu, belirli bir web sitesini (örneğin Twitter.com) telefonunuzun ana ekranına işaretleyebileceğiniz yerdir. Ardından simgeye dokunduğunuzda, tipik tarayıcı deneyimiyle gelen olağan dikkat dağıtıcı unsurlar olmadan tam ekran bir uygulama olarak açılır. Bunun nasıl göründüğüne dair bir örneği aşağıda görebilirsiniz.


Bunu GrapheneOS'un yerel tarayıcısı Vanadium'da gerçekleştirmek için, istediğiniz web sitesine gidin, ekranın sağ üst köşesindeki üç dikey noktaya dokunun ve ardından **'Ana Ekrana Ekle'** seçeneğine dokunun.


Bu yaklaşımın tek dezavantajı, bu sadece yer imlerine eklenmiş bir web sayfası olduğu için herhangi bir bildirim almayacak olmanızdır. Yine de bazıları bunu olumlu olarak görebilir!


![image](assets/fr/8.webp)


Twitter PWA


### Web Tarayıcıları


Önceden paketlenmiş seçenek olan Vanadium ile gerçekten yanlış gidemezsiniz. Uygulama, denediğim diğer tüm mobil tarayıcılarla aynı şekilde davranıyor ve bir kez bile uyumluluk sorunu yaşamadım.


Tor yerel `.onion` sitelerine erişmeniz gereken zamanlar için Tor Browser APK'sını doğrudan [web sitesinden] (https://www.torproject.org/download/#android) veya F-Droid üzerinden indirebilirsiniz.


### VPN'ler


Çevrimiçi faaliyetlerinizi meraklı internet servis sağlayıcınızdan (İSS) korumak için Sanal Özel Ağ (VPN) uygulaması iyi bir seçenektir. VPN, internet trafiğinizi şifrelenmiş bir tünelde VPN hizmet sağlayıcısı tarafından kontrol edilen paylaşılan bir IP Address'e göndererek cihaz etkinliğinizin sizinle ilişkilendirilememesini sağlar.


İşte, herhangi bir kişisel bilgi vermeden hizmeti Bitcoin ile ödemenizi sağlayan iki tanınmış seçenek. Her ikisi de F-Droid'de mevcuttur.





https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mesajlaşma


Son yıllarda şifreli mesajlaşma çözümleri bol miktarda bulunur hale geldi. Ancak sorun şu ki, telefonunuza en iyi ve en özel seçeneği yükleyebilirsiniz, ancak bunu kullanan hiçbir kişiniz yoksa, ne anlamı var?


Gizlilik alanına ilgi duymayan çoğu kişi muhtemelen WhatsApp veya iMessage kullanıyordur. İlki Aurora Store üzerinden indirilebilir ancak ikincisi GrapheneOS üzerinde çalışmayacaktır (tabii ki!).



- [Signal](https://signal.org/), güçlü bir geçmişe ve zengin özellik setine sahip en popüler uçtan uca şifrelenmiş (E2EE) mesajlaşma programlarından biridir. Signal kaydolmak için bir telefon numarası gerektirir, bu nedenle telefon numaranızı bilmemeyi tercih ettiğiniz kişilerle sohbet etmeyi planlıyorsanız, belki de bazı alternatiflere bakın. Signal, Aurora Store üzerinden indirilmelidir.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) oldukça yeni bir E2EE mesajlaşma aracıdır. Kullanıcı kimliği yoktur, telefon numarası veya kişisel bilgi gerektirmez. İnsanlar sizi kişisel QR kodunuzu tarayarak veya benzersiz bağlantınızı ziyaret ederek bulur. Simplex ayrıca ileri düzey kullanıcıların herhangi bir merkezi varlığa bağımlılığı daha da azaltmak için kendi sunucularını çalıştırmalarına izin verir. Simplex'in bir masaüstü istemcisi yoktur, bu nedenle çoklu cihaz öncelik listenizdeyse uygun olmayabilir. Android için Simplex F-Droid üzerinden kullanılabilir.
- [Threema](https://threema.ch/en/faq/libre_installation) Simplex'e benzer bir deneyim sunuyor, ancak daha uzun süredir var ve sonuç olarak biraz daha cilalı hissediyor. Threema ücretsiz değildir, ömür boyu lisans ücreti 4,99 dolardır ve Bitcoin ile satın alınabilir. Threema bir web istemcisi ve yerel masaüstü uygulamaları sunuyor. Android uygulaması F-Droid üzerinden kullanılabilir.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/), Android için resmi Telegram uygulamasının resmi olmayan bir FOSS Fork'üdür. Telegram'da E2EE 'gizli sohbetler' vardır, ancak varsayılan seçenek özel değildir. Telegram FOSS F-Droid'den indirilebilir.


![image](assets/fr/9.webp)

Sol: Threema, Sağ: Simpleks


https://planb.network/tutorials/computer-security/communication/signal-8dfb5572-6962-4f1c-bfa5-3192da4e9a4e

https://planb.network/tutorials/computer-security/communication/telegram-09ab3cf3-7625-4267-97a1-24e59a9e5943

https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

https://planb.network/tutorials/computer-security/communication/simplex-chat-7a1efa11-4d0a-49c4-92aa-e18bf22c22b9

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

### Medya



- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/), Premium hesap gerektirmeyen platformlar arası bir Spotify istemcisidir. Spotube, F-Droid üzerinden kullanılabilir.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/), YouTube müziklerinden herhangi bir müziği ücretsiz olarak buharlaştırmak için harika bir uygulamadır. ViMusic F-Droid'den temin edilebilir.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) can sıkıcı reklamlar ve şüpheli izinler olmadan bir YouTube deneyimi sunar. NewPipe ile kanallara abone olabilir, arka planda dinleyebilir ve hatta çevrimdışı görüntüleme için indirebilirsiniz. NewPipe'a F-Droid üzerinden erişilebilir.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/), tüm favori şovlarınıza abone olmanızı ve yönetmenizi sağlayan bir podcast oynatıcıdır. AntennaPod F-Droid üzerinden kullanılabilir.


![image](assets/fr/11.webp)

Sol: Spotube, Sağ: ViMusic


### Haritalar


GrapheneOS'ta sürüş sırasında ve bir harita uygulaması kullanırken sesli yardım istiyorsanız, [RHVoice](https://rhvoice.org/installation/) yüklemeniz ve [configure](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) yapmanız gerekir.



- [Magic Earth](https://www.magicearth.com/), adım adım navigasyon, 3D ve çevrimdışı haritaları destekleyen bir harita alternatifidir. Magic Earth Aurora Store'dan indirilebilir.
- [Organic Maps] (https://f-droid.org/en/packages/app.organicmaps/) gezginler, turistler, yürüyüşçüler ve bisikletçiler için kitle kaynaklı OpenStreetMap verilerine dayalı bir harita alternatifidir. Maps.me uygulamasının (daha önce MapsWithMe olarak biliniyordu) gizlilik odaklı, açık kaynaklı bir Fork'idir. Aktif bir İnternet bağlantısı olmadan özelliklerin %100'ünü destekler ve F-Droid'den indirilebilir.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) yukarıda belirtilen tüm özellikleri destekleyen bir başka harika harita alternatifidir.


![image](assets/fr/13.webp)

Sol: Sihirli Dünya, Sağ: Organik Haritalar


### E-posta



- [Proton Mail](https://proton.me/mail) denetlenmiş E2EE'yi destekleyen ücretsiz bir özel e-posta hizmeti sunmaktadır. Proton ayrıca özel etki alanlarını ve [aliasing](https://proton.me/support/creating-aliases) destekleyen ücretli bir sürüm sunar. Proton Mail doğrudan APK olarak veya Aurora üzerinden indirilebilir.
- [Tutanota](https://tutanota.com/), isteğe bağlı ücretli hizmetler de dahil olmak üzere Proton Mail ile aynı özellikleri sunar ve doğrudan APK olarak veya F-Droid aracılığıyla indirilebilir.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/), temelde her e-posta sağlayıcısıyla çalışan açık kaynaklı bir e-posta istemcisidir. Birden fazla hesabı, birleşik gelen kutusunu ve OpenPGP şifreleme standardını destekler.


![image](assets/fr/15.webp)

Sol: Proton Mail, Sağ: Tutanota


### Üretkenlik



- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) bir dosya senkronizasyon programıdır. Dosyaları iki veya daha fazla cihaz arasında gerçek zamanlı olarak senkronize eder ve meraklı gözlerden güvenli bir şekilde korunur. Verileriniz yalnızca size aittir ve nerede saklanacağını, üçüncü bir tarafla paylaşılıp paylaşılmayacağını ve internet üzerinden nasıl iletileceğini seçme hakkına sahipsiniz. Syncthing F-Droid üzerinden kullanılabilir.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) ev ağınıza bağlıyken tüm cihazlarınızın birbiriyle kolayca konuşmasını sağlar. Tüm cihazlarınız arasında (iOS'ta bile!) Dosyaları, fotoğrafları, pano verilerini kolayca gönderin. KDE connect F-Droid'den indirilebilir.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/), düşüncelerinizi ve yapılacaklar listelerinizi tüm cihazlarınız arasında senkronize etmek için bir E2EE not uygulamasıdır. Ücretsiz planları çoğu kişisel kullanım durumunu kapsamalıdır. Notesnook F-Droid'de mevcuttur.
- [Standart Notlar] (https://f-droid.org/en/packages/com.standardnotes/) Notesnook'a çok benzer, ancak özellik setine uyması için ücretli bir plan gerektirir. Standart Notlar F-Droid aracılığıyla kullanılabilir.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/), telefon yazma deneyiminiz söz konusu olduğunda aklınıza gelebilecek hemen hemen her şeyi özelleştirmenize olanak tanıyan bir klavye uygulamasıdır. F-Droid üzerinden indirilebilir.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) varsayılan Google klavye uygulamasıdır. Benim deneyimlerime göre açık ara en iyi yazma ve kaydırma deneyimini sunuyor. Bu uygulamayı indirirseniz, ağ ile ilgili tüm izinleri tamamen devre dışı bıraktığınızdan emin olun. Aurora üzerinden indirilebilir.


![image](assets/fr/17.webp)

Sol: Notesnook, Sağ: KDE Connect


### Yaşam Tarzı



- [Geometric Weather] (https://f-droid.org/en/packages/wangdaye.com.geometricweather/), F-Droid aracılığıyla kullanılabilen güzel tasarlanmış bir Açık Kaynak hava durumu uygulamasıdır. Ayrıca farklı boyutlarda widget'ları da destekler, böylece seçtiğiniz konumdaki hava durumunu doğrudan ana ekranınızdan görebilirsiniz.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) 200'den fazla dili destekleyen bir Açık Kaynak ve gizliliği koruyan çeviri uygulamasıdır. Translate You, F-Droid üzerinden kullanılabilir.
- [Proton Calendar](https://proton.me/calendar/download), Proton e-posta hesaplarınızla sorunsuz bir şekilde etkileşime giren, kullanımı kolay bir E2EE'dir. Proton Calendar bir APK olarak veya Aurora mağazası aracılığıyla indirilebilir.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) biniş kartlarını, kuponları, sinema biletlerini ve üyelik kartlarını vb. görüntülemek ve saklamak için bir uygulamadır. Sadece ilgili `pkpass` veya `espass` dosyasını indirin ve uygulama ile açın. PassAndroid F-Droid üzerinden kullanılabilir.


![image](assets/fr/19.webp)

Sol: Geometrik Hava Durumu, Sağ: Proton Takvimi


### Güvenlik/Gizlilik



- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) tüm cihazlarınız için ücretsiz ve E2EE çapraz platform şifre yöneticisi çözümü sunar. Ücretli hizmetleri, 2FA kodlarını uygulamaya entegre etmenize olanak tanır. Bitwarden'in sunucu tarafı kendi kendine barındırılabilir ve Android uygulaması F-Droid aracılığıyla kullanılabilir.
- [Proton Pass](https://proton.me/pass/download) Bitwarden'a benzer bir ücretsiz hizmet sunuyor, ancak [Proton Unlimited](https://proton.me/pricing) müşterileri ek gelişmiş özelliklere erişebiliyor. Proton Pass APK veya Aurora üzerinden kullanılabilir.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/), tek seferlik şifre protokollerini kullanan sistemler için iki faktörlü bir kimlik doğrulama uygulamasıdır. Belirteçler bir QR kodu taranarak kolayca eklenebilir. FreeOTP, F-Droid üzerinden kullanılabilir.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/), çevrimiçi hizmetleriniz için 2 adımlı doğrulama belirteçlerinizi yönetmek için Android için ücretsiz, güvenli ve Açık Kaynaklı bir uygulamadır. Aegis, F-Droid üzerinden kullanılabilir.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/), verilerinizi yerel olarak şifreleyen ücretli, çapraz platformlu bir hizmettir, böylece verilerinizi en sevdiğiniz bulut hizmetine güvenle yükleyebilirsiniz. Cryptomator F-Droid üzerinden indirilebilir.


![image](assets/fr/21.webp)

Sol: Proton Geçidi,
Sağ: Bitwarden


https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

https://planb.network/tutorials/computer-security/data/cryptomator-84e52c76-2253-49fe-81da-e05e90c28d0d

### Bulut Çözümleri



- [Proton Drive](https://proton.me/drive/download) tüm dosyalarınızı yedeklemek ve saklamak için ücretli bir E2EE bulut çözümüdür. Yazım sırasında, bir Windows masaüstü istemcisi duyurdular, ancak Mac ve Linux kullanıcıları bilgisayarlarından senkronize etmek için web sürümünü kullanmaya devam etmelidir (şimdilik). Android istemcisi APK olarak ya da Aurora üzerinden kullanılabilir.
- [Skiff](https://skiff.com/download) ayrıca ücretli E2EE bulut depolama ve dosya işbirliği araçları da sunmaktadır. Bir Mac ve Windows masaüstü istemcisi (bir web uygulamasının yanı sıra) sunarlar ve Android istemcileri Aurora'dan indirilmelidir.
- [Nextcloud] (https://f-droid.org/en/packages/com.nextcloud.client/) işbirliği, cihazlar arası senkronizasyon ve dosya depolama için tam özellikli bulut tabanlı bir çözüm sunuyor. Daha ileri düzey kullanıcılar, Özgür ve Açık Kaynak yazılımlarını istedikleri donanım üzerinde kendi kendilerine barındırmayı seçebilirler. Android istemcileri F-Droid üzerinden indirilebilir.
- [Cryptpad](https://cryptpad.fr/) Google Docs'a ücretsiz, web tabanlı, E2EE bir alternatif sunuyor.


![image](assets/fr/23.webp)

Proton Sürücü


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

## Dezavantajları


Kullanmaya alıştığınız teknoloji holdingi uygulamalarının açık kaynak kodlu ve gizliliği koruyan alternatifleri çoktur ve bunlardan bazıları genellikle kapalı kaynak kodlu, casus yazılımlarla dolu alternatiflerden daha iyidir.


Ancak GrapheneOS'a geçerken, alternatif olmadığı için vazgeçmeniz gereken bazı yaratık konforları vardır. Bunlar şunları içerir:



- Apple CarPlay/Android Auto** - Eski moda Bluetooth, USB veya Aux'a bağlı kalmanız gerekecek.
- Apple/Google Pay** - Hemen hemen herkes Wallet'sını yanında taşıyor zaten!
- Bankacılık uygulamaları** - Bunlar hiç çalışmıyor değil. Aslında bazıları mükemmel çalışıyor. Diğerleri yalnızca Google Play Hizmetleri etkinleştirildiğinde çalışıyor (aşağıda daha fazlasını okuyun) ve diğerleri hiç çalışmıyor. Mevcut durumu görmek için bankanızla ilgili raporu [burada] (https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) okuyun. Sizinki çalışmayanlar listesindeyse korkmayın, URL'yi ana ekranınıza bir web uygulaması olarak kaydedebileceğinizi unutmayın.
- Anında Bildirimler** - Belirli bir uygulamayı kullanmadığınızda size güncellemeler gönderen çoğu uygulama bunu Google Play Hizmetleri aracılığıyla yapacaktır. Bunlar GrapheneOS ile varsayılan olarak yüklenmez, bu nedenle arkadaşınız size bir e-posta gönderdiğinde hemen bildirim almadığınızı fark ederseniz, muhtemelen nedeni budur. İyi haber şu ki, yukarıda bahsedilen bazı uygulamalar, güncellemeleri periyodik olarak kontrol etmek ve gerektiğinde size bir bildirim vermek için kendi arka plan bağlantılarını uyguladılar


### Sandbox'lı Google Play


**Lütfen unutmayın:** GrapheneOS, Google Play'in resmi sürümlerini standart uygulama sanal alanına yükleme ve kullanma seçeneği sunan bir Layer uyumluluğuna sahiptir. Google Play, uygulama sanal alanını atlamak ve büyük miktarda yüksek ayrıcalıklı erişim almak yerine GrapheneOS üzerinde kesinlikle hiçbir özel erişim veya ayrıcalık almaz.


En sevdiğiniz uygulama için anlık bildirimler olmadan yaşayamayacağınızı veya belirli bir 'olmazsa olmaz' uygulamanın Play Hizmetleri olmadan işe yaramayacağını düşünüyorsanız, GrapheneOS bu hizmetleri tamamen korumalı bir ortamda [yüklemenize] (https://grapheneos.org/usage#sandboxed-google-play-installation) olanak tanır. Yüklendikten sonra, bu hizmetlerin çalışması için Google hesabı gerekmez ve her birinin izinleri sıkı bir şekilde kontrol edilebilir.


Bunları ilk günden yüklemek için acele etmeden önce, onlar olmadan ne kadar ilerleyebileceğinizi görmenizi tavsiye ederim. Bunlar olmadan ne kadar çok uygulamanın gayet normal çalıştığını görünce muhtemelen şaşıracaksınız.


Bunları yüklemek istiyorsanız, önceden yüklenmiş 'Uygulamalar' uygulamasına ve ardından 'Google Play Hizmetleri'ne dokunmanız yeterlidir. Bunları, onsuz yaşayamayacağınız daha az özel uygulamaların yanına, telefonunuzun geri kalanından ekstra Layer ayrımı sağlamak için tamamen ayrı bir kullanıcı profilinin içine yüklemeyi düşünün.


![image](assets/fr/24.webp)

Play Hizmetleri yükleme ekranı


### Profiller


GrapheneOS, telefonunuzun içinde ayrı bir telefon deneyimine sahip olmanızı sağlar. Ek profiller kendi uygulamalarını ve hizmetlerini yükleyebilir ve sahip hesabından herhangi bir dosya veya veriye erişemez.

Play Hizmetleri gerektiren ancak çok seyrek kullanılan uygulamalardan yalnızca bir veya iki tanesine sahipseniz, bunları Play Hizmetleri ile birlikte ayrı bir profile yüklemek, sahip profilinde çalıştırılmalarından kaynaklanan küçük gizlilik etkilerini daha da güçlendirmek için harika bir fikir olabilir.


Bu kullanım örneği hakkında daha fazla bilgi edinebilirsiniz [burada](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).


Kullanım durumunuza uygun ayrı bir profil eklemeye karar verirseniz, [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) uygulaması sizin için yararlı olabilir. Insular, bu kılavuzda daha önce ele alınan geleneksel yükleme yollarından herhangi birini kullanmanıza gerek kalmadan mevcut uygulamalarınızdan herhangi birini yeni profile kolayca klonlamanıza olanak tanır. Insular ayrıca bu uygulamalardan herhangi birini hızlı bir şekilde 'dondurarak' o uygulamanın tüm arka plan hizmetlerinin çalışmasını tamamen devre dışı bırakmanıza olanak tanır.


![image](assets/fr/24.webp)

Kullanıcı profili yönetim ekranı


### e-Sims


Telefon gizliliğinizi bir üst seviyeye taşımak ve gerçek dünya kimliğinizden ayrı bir cep telefonu hizmetine sahip olmak istiyorsanız, bir eSIM sizin için uygun olabilir. Bir eSIM, çevrimiçi olarak satın alabileceğiniz ve bir QR kodu aracılığıyla telefonunuza ekleyebileceğiniz sanal bir SIM'dir. Bitcoin ile anonim olarak ödenebilen bu tür hizmetler sunan şirketler arasında [Silent.Link](https://silent.link/) ve [Bitrefill](https://www.bitrefill.com/gb/en/esims/) bulunmaktadır.


eSIM'lere telefon gizliliği için her derde deva bir çözüm olarak bakılmamalıdır. Doğru ellerde olduklarında faydalı bir araç olabilirler, ancak niyetiniz tamamen 'şebekeden uzaklaşmak' ise lütfen her türlü hücre hizmetini kullanmanın [ödünleri] (https://grapheneos.org/faq#cellular-tracking) hakkında araştırma yapın.


GrapheneOS'ta eSIM provizyonu için Sandboxed Play Services kurulmalıdır.


## Yedeklemeler


Yeni de-Google'd Pixel telefonunuzun kurulumunu yaptıktan sonra, kendinize bir yedek oluşturmanız iyi bir fikirdir. Bu yedekleme, telefonunuzu kaybetmeniz veya kaybolması/çalınması durumunda telefonu aynı duruma geri yüklemenizi sağlayacaktır.


Yedekleme dosyasını herhangi bir harici depolama ortamına veya Nextcloud gibi kendi kendine barındırılan bir bulut çözümüne depolamayı seçebilirsiniz, ancak bazı kullanıcılar ikinci seçenekle farklı başarı düzeyleri bildirmektedir.


İlk yedeğinizi oluşturmak için:


1. Ayarlar** > **Sistem** > **Yedekleme** bölümüne gidin, ardından 12 kelimelik kurtarma kodunuzu yazın. Bu kod, daha sonraki bir tarihte yedekleme dosyasının şifresini çözmek için gereklidir. Kodu kaybederseniz, telefon yedeklemenize erişiminizi kaybedersiniz.

2. Ardından depolama konumunuzu seçin. Harici bir USB sürücü veya endüstriyel sınıf microSD kart tavsiye ederim.

3. Yedeklenecek verileri seçin. Belirttiğiniz depolama ortamında yeriniz varsa, her şeyi seçmenizi tavsiye ederim.

4. Sağ üstteki üç noktaya dokunun ve **Şimdi yedekle** öğesini seçin.


![image](assets/fr/26.webp)


Yedekleme ekranı


Harici depolama ortamına çevrimdışı yedekleme yapıyorsanız, en kötü durumda telefonunuzdaki son önemli güncellemelerin kaybolmamasını sağlamak için bu adımı düzenli olarak tamamlamanın mantıklı olduğunu unutmayın.


![video](https://www.youtube.com/embed/eyWmcItzisk)


Yedekleme sürecini detaylandıran video


## Sonuç


Son yıllarda GrapheneOS yazılımı önemli ölçüde olgunlaşmıştır. Her zamankinden daha kararlı ve uyumludur. Bunu gelişen Açık Kaynak ve gizliliği koruyan uygulama ekosistemi ile birleştirmek, GrapheneOS'u sizin gibi 'normal' insanlar için bile stok Android veya iOS'a gerçekten uygun bir alternatif haline getiriyor!


Veri ihlalleri ve izlemeler günümüz dünyasında o kadar yaygın ki artık manşetlerde bile yer almıyor. Kendinizi korumak sizin elinizde. Yol boyunca yapılması gereken ayarlamalar ve fedakarlıklar olacaktır, ancak bu tür ihlallere maruz kalmanızı azaltmak düşündüğünüz kadar zor değildir.


Umarım bu rehber yolculuğunuz boyunca size yardımcı olur. Bu rehberi faydalı bulduysanız ve çalışmalarımı desteklemek istiyorsanız, lütfen bir [bağış](/ipuçları) göndermeyi düşünün.


Mevcut bir GrapheneOS kullanıcısıysanız veya bu kılavuzun bir sonucu olarak bir GrapheneOS kullanıcısı olduysanız, önemli çalışmalarını desteklemek için [bağış yapmayı] (https://grapheneos.org/donate) düşünün.


### Daha fazla bilgi edinin


GrapheneOS, herkesin kolayca haftalarını harcayabileceği bir tavşan deliğidir. Deneyimi gereksinimlerinize ve tehdit modellerinize göre uyarlamak için öğrenebileceğiniz ve kurcalayabileceğiniz çok şey var. Aşağıda yolculuğunuza devam edebileceğiniz bazı bağlantılar yer almaktadır:



- [GrapheneOS Resmi Kullanım Kılavuzu](https://grapheneos.org/usage) - Resmi Web Sitesi
- [GrapheneOS Forum](https://discuss.grapheneos.org/) - Resmi Web Sitesi
- [GrapheneOS Ayarları Masterclass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - 'The Privacy Wayfinder' tarafından hazırlanan video
- [GrapheneOS Genel Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - 'Watchman Privacy' tarafından hazırlanan Podcast


*Bu eğitim, [BitcoinQnA tarafından Bitcoiner.Guide üzerinde MIT lisansı altında yayınlanan](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md) orijinal içeriğin bir uyarlamasıdır ve ilk yazım çalışmasının tüm kredisi ona aittir.*

