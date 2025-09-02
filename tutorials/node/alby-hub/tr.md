---
name: Alby Hub
description: Kendi Lightning düğümünüzü nasıl kolayca başlatırsınız?
---
![cover](assets/cover.webp)


Alby Hub, popüler Lightning web uzantısının arkasındaki şirket olan Alby'nin en son açık kaynaklı yazılımıdır. Alby Hub, düzinelerce uygulamayla entegre olmak için her yerden erişilebilen, kullanımı en kolay Lightning düğümüne sahip, kendi kendine emanet edilebilen bir Wallet'dir. Alby Hub, Lightning düğümlerini yönetmek için kullanımı kolay bir Interface'dır.


Bu eğitimde, Alby Hub'ı kullanmanın farklı yollarını, Alby'nin mobil uygulaması Alby Go'ya veya Alby Tarayıcı Uzantısına nasıl bağlanacağını inceleyeceğiz. Bu, Sats'nizi hareket halindeyken düğümünüzün yönetiminde özerk olmanızı sağlayacaktır.


![ALBY HUB](assets/fr/01.webp)


## Alby Hub nedir?


Alby Hub, Alby ekosisteminin yeni amiral gemisi aracı olacak. Bu yazılım, kullanıcıların anahtarlarının Ownership'ünü korurken (self-custody), entegre bir Lightning düğümü ile kendi self-custodial Wallet'lerini kolayca yönetmelerini sağlar.


Alby Hub son derece uyarlanabilir bir araçtır. Hem yeni başlayanların hem de ileri düzey kullanıcıların ihtiyaçlarını karşılayabilir. Yeni başlayanlar, altta yatan karmaşıklıkla uğraşmak zorunda kalmadan gerçek bir Lightning düğümünü kendi başlarına kolayca çalıştırmak için kullanacaklardır. Daha deneyimli kullanıcılar için Alby Hub, mevcut bir Lightning düğümünün gelişmiş yönetimi için eksiksiz bir Interface olarak kullanılabilir.


İhtiyaçlarınıza bağlı olarak, Alby Hub 4 konfigürasyonda mevcuttur:




- Alby Hub Bulut :**


Acemiler için ideal olan bu ilk seçenek Alby bulut seçeneğidir. Alby Hub Interface üzerinden erişilebilen, Alby tarafından yönetilen bir sunucuya doğrudan bir Hub yerleştirmenize olanak tanır. Alby sunucuyu yönetmesine rağmen, anahtarlarınız yalnızca sizin bildiğiniz bir parola kullanılarak şifrelendiğinden, fonlarınız üzerindeki egemenliğinizi korursunuz. Bununla birlikte, düğümün çalışması için anahtarlarınızın RAM'de şifreli kalması gerekir, bu da teorik olarak birinin sunucuya fiziksel olarak erişmesi durumunda onları riske maruz bırakır. Yeni başlayanlar için ilginç bir uzlaşmadır, ancak risklerin farkında olmak önemlidir.


Bu seçeneğin en büyük avantajı, barındırmayı kendiniz yönetmek zorunda kalmadan 7/24 çalışan bir Lightning düğümüne sahip olmanızdır. Dahası, Lightning düğümünüzün yedeklemeleri, kanal yedeklemelerini kendiniz yönetmeniz gereken kendi kendine barındırılan seçeneklere kıyasla basitleştirilmiş ve otomatikleştirilmiştir.


Alby Cloud ücretli bir hizmettir [Daha fazla ayrıntı için fiyatlandırmalarını kontrol edin] (https://albyhub.com/#pricing). Ücret, Alby tarafından verilen bir Lightning Invoice aracılığıyla Wallet'inizden otomatik olarak düşülür. Bu, düğümünüzü aboneliğinizle ilgili Alby faturalarını otomatik olarak ödeyecek şekilde yapılandıran bir NWC bağlantısı aracılığıyla yapılır.





- Mevcut bir düğüm ile Alby Hub :**


Örneğin Umbrel veya Start9 üzerinde barındırılan bir düğümünüz varsa, Alby Hub, ThunderHub veya RTL ile aynı şekilde gelişmiş bir yönetim Interface olarak kullanılabilir.




- Alby Hub yerel :**


Alby Hub'ı doğrudan bilgisayarınıza kurmak da mümkündür, ancak Lightning düğümüne uzaktan erişmek için bilgisayarınızın her zaman etkin kalması gerektiğinden bu seçenek daha az pratiktir. Ancak, bu alternatif özel ihtiyaçlarınız için uygun olabilir.




- Alby Hub kişisel bir sunucuda :**


İleri düzey kullanıcılar için, Alby Hub basit bir komutla kişisel bir sunucuya dağıtılabilir. Bu seçenek bu eğitimde ele alınmamıştır, ancak [Alby'nin GitHub'ında] özel talimatlar bulabilirsiniz (https://github.com/getAlby/hub?tab=readme-ov-file#docker).


Bu eğitim, seçilen seçenekten bağımsız olarak aynı olacak olan Interface'a odaklanmaktadır. Ayrıca Alby Hub'ın ücretli bulut seçeneği ve ardından kutu içinde düğüm seçeneği (Umbrel veya Start9) ile nasıl dağıtılacağına da bakacağız.


![ALBY HUB](assets/fr/02.webp)


Bilgisayarınıza yerel kurulum için, [işletim sisteminize göre yazılımı indirin ve kurun] (https://github.com/getAlby/hub/releases), ardından Interface'deki aynı talimatları izleyin.


![ALBY HUB](assets/fr/03.webp)


## Bir Alby hesabı oluşturun


İlk adım bir Alby hesabı oluşturmaktır. Bu, Alby Hub'ı kullanmak için gerekli olmasa da, bir Lightning Address edinme olasılığı da dahil olmak üzere mevcut seçeneklerden tam olarak yararlanmanıza olanak tanır.


Resmi Alby web sitesine] (https://getalby.com/) gidin ve "*Hesap Oluştur*" düğmesine tıklayın.


![ALBY HUB](assets/fr/04.webp)


Bir takma ad ve Address e-posta adresi girin, ardından "*Kayıt ol*" düğmesine tıklayın. Bu Address e-postası daha sonra hesabınıza giriş yapmak için kullanılacaktır.


![ALBY HUB](assets/fr/05.webp)


E-posta ile aldığınız doğrulama kodunu girin.


![ALBY HUB](assets/fr/06.webp)


Çevrimiçi hesabınıza giriş yaptıktan sonra "*Devam*" düğmesine tıklayın.


![ALBY HUB](assets/fr/07.webp)


Tekrar "*Devam*" düğmesine tıklayın.


![ALBY HUB](assets/fr/08.webp)


## Bulut barındırma seçeneği


Daha sonra Alby Hub'ı kendi cihazınıza yüklediğiniz self-hosted seçeneği veya premium seçenekler arasında seçim yapmanız gerekecek. Pro Cloud seçeneği ile nasıl devam edeceğinizi açıklayarak başlayacağım (bunun ücretli bir seçenek olduğunu unutmayın, önceki bölümdeki ayrıntılara bakın).


"*Yükseltme*" üzerine tıklayın.


![ALBY HUB](assets/fr/09.webp)


"*Şimdi Abone Ol*" butonuna tıklayarak onaylayın.


![ALBY HUB](assets/fr/10.webp)


"*Alby Hub'ı Başlat*" üzerine tıklayın.


![ALBY HUB](assets/fr/11.webp)


Düğümünüz oluşturulurken birkaç dakika bekleyin.


![ALBY HUB](assets/fr/12.webp)


İşte bu kadar, Alby Hub'ınız artık yapılandırıldı. Bir sonraki bölümde, Alby Hub'ı mevcut bir node'a nasıl kuracağınızı göstereceğim. Halihazırda bir lightning node'unuz yoksa, Alby Hub'ı Alby Cloud üzerinde yapılandırmak için bir sonraki bölüme geçebilirsiniz.


![ALBY HUB](assets/fr/13.webp)


## Kendi kendine barındırma seçeneği


Alby Hub'ı mevcut Lightning düğümünüz için bir Interface olarak kullanmayı tercih ederseniz, birkaç seçeneğiniz vardır: bir sunucuya, yerel olarak bilgisayarınıza veya bir kutu içinde düğüm (Umbrel veya Start9) aracılığıyla yükleyin. Alby Hub'ı bu yapılandırmalarda kullanmak ücretsizdir. Fiziksel erişim olmadan sunucu seçeneğinin bulut sürümüne benzer riskler sunduğunu ve bir PC'ye yerel kurulumun genellikle uygun olmadığını düşündüğüm için kutu içinde düğüm seçeneğine odaklanacağız.


Bunu Umbrel'de kurmak için (Start9 için adımlar aynıdır), öncelikle yapılandırılmış bir LND düğümüne sahip olmanız gerekir.


Umbrel Interface cihazınızda oturum açın ve uygulama mağazasına gidin.


![ALBY HUB](assets/fr/14.webp)


"*Alby Hub*" uygulamasını arayın.


![ALBY HUB](assets/fr/15.webp)


Düğümünüze yükleyin.


![ALBY HUB](assets/fr/16.webp)


Alby Hub Interface'niz artık hazır. Eğitimin geri kalanını bulut Interface kullanıyormuş gibi takip edebilirsiniz, ancak ücretli sürümün seçenekleri olmadan. Dahası, bulut sürümünden farklı olarak, anahtarlarınız Alby'nin sunucularında değil, düğümünüzde yerel olarak saklanır.


![ALBY HUB](assets/fr/17.webp)


## Alby Hub'ı başlatın


"*Get Started*" düğmesine tıklayın.


![ALBY HUB](assets/fr/18.webp)


Alby Hub daha sonra sizden bir parola seçmenizi isteyecektir. Bu şifre Wallet'inizi şifrelemek için kullanılacağından çok önemlidir. Ücretli bulut sürümünde, anahtarlarınız Alby sunucusunda saklanır, yalnızca sizin bildiğiniz bu parola ile şifrelenir, daha sonra şifresi çözülür ve gerektiğinde işlemleri imzalamak için yalnızca RAM'de saklanır.


Bu nedenle güçlü bir parola seçmek çok önemlidir. Bu şifreye sahip olan herkes potansiyel olarak düğümünüze erişim sağlayabilir. Daha fazla güvenlik için bu parolanın bir veya daha fazla fiziksel yedeğini bir kağıda veya daha iyisi bir metal parçasına aldığınızdan emin olun.


Şifrenizi dikkatlice seçip kaydettikten sonra "*Şifre Oluştur*" seçeneğine tıklayın.


![ALBY HUB](assets/fr/19.webp)


Artık Lightning düğümünüze erişiminiz var.


![ALBY HUB](assets/fr/20.webp)


Yapılacak ilk işlem, anahtarlarınızın türetildiği kurtarma cümlenizi kaydetmektir. Bunu yapmak için "Ayarlar" üzerine tıklayın. Bu ifade, otomatik yedeklemeleri etkinleştirdiyseniz Wallet'unuza erişimi kurtarmanıza olanak tanır.


![ALBY HUB](assets/fr/21.webp)


Ardından "*Yedekleme*" sekmesine gidin. Erişmek için şifrenizi girin.


![ALBY HUB](assets/fr/22.webp)


Daha sonra 12 kelimelik kurtarma cümlenize erişebileceksiniz. Bu ifadenin bir veya daha fazla fiziksel yedeğini kağıt veya metal üzerine alın ve güvenli bir yerde saklayın.


![ALBY HUB](assets/fr/23.webp)


İfadeyi kaydettikten sonra, kaydettiğinizi onaylamak için kutuyu işaretleyin ve "*Devam*" düğmesine tıklayın.


![ALBY HUB](assets/fr/24.webp)


## Bitcoinlerime erişimi nasıl geri kazanabilirim?


Alby Hub'ınıza fon göndermeden önce, bir sorun olması durumunda bu fonların nasıl kurtarılacağını ve bu kurtarma işlemi için hangi bilgilerin gerekli olduğunu anlamak önemlidir. Süreç, kurtarılacak fonların niteliğine ve node'unuzun barındırma moduna göre değişir.


Ücretli bulut kullanıcıları için, bitcoinlerinizin tamamen kurtarılması üç temel Elements gerektirir:



- Kurtarma cümleniz;
- Otomatik yedeklemeleri almak için Alby hesabınıza erişim.


Bu 2 bilgiden herhangi birinin olmaması, bitcoinlerinizi tam olarak kurtarmanızı imkansız hale getirecektir.


Alby Hub'ı kendi cihazlarında çalıştıranlar için kurtarma süreci [burada] (https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account) belgelenmiştir.


Alby Hub'ı mevcut bir düğüme kurduysanız, söz konusu düğüm işletim sisteminin kurtarma sürecini izlemeniz gerekir. Örneğin: Umbrel, Lightning kanallarınızın en son durumunu şifrelemek ve Tor aracılığıyla dinamik ve anonim olarak kaydetmek için [bir seçenek] (https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) sunar. Yalnızca Alby'nin otomatik yedeklemelerinin herhangi bir kanalı kapatmadan Hub'ınızı tamamen kurtarmanıza izin verdiğini unutmayın.


## İlk Lightning kanalınızı satın alın


Artık Alby Hub tarafından sağlanan talimatları takip edebilirsiniz. Gelen nakit için ilk kanalınızı açmak için düğmeye tıklayın.


![ALBY HUB](assets/fr/25.webp)


"*Açık Kanal*" seçeneğini seçin. Yönlendirme düğümü olmayı düşünmüyorsanız ve özellikle buna ihtiyacınız yoksa, özel kanalları tercih etmenizi öneririm.


![ALBY HUB](assets/fr/26.webp)


Alby Hub ödemeniz için bir generate ve bir Invoice gönderecektir. Bu ödeme, kanalınızı açmak için gereken işlem ücretlerinin yanı sıra düğümünüze bir kanal açacak olan LSP'nin (*Lightning Service Provider*) hizmet ücretlerini de kapsar ve ödemeleri hemen almanızı sağlar.


![ALBY HUB](assets/fr/27.webp)


Invoice ödendikten ve işlem onaylandıktan sonra ilk Lightning kanalınız kurulmuş olur.


![ALBY HUB](assets/fr/28.webp)


"*Node*" sekmesinde, artık Lightning aracılığıyla ödeme almanıza olanak tanıyan gelen nakit paranız olduğunu görebilirsiniz.


![ALBY HUB](assets/fr/29.webp)


Ödeme almak için "*Wallet*" sekmesine ve ardından "*Al*" seçeneğine tıklayın.


![ALBY HUB](assets/fr/30.webp)


Bir tutar girin ve gerekiyorsa bir açıklama ekleyin, ardından "*Invoice Oluştur*" düğmesine tıklayın.


![ALBY HUB](assets/fr/31.webp)


İlk ödemem olan 120,000 Sats'yı aldım.


![ALBY HUB](assets/fr/32.webp)


"*Wallet*" sekmesine geri dönerek Wallet bakiyenizi kontrol edebilirsiniz. İlk ödemenizi yaptığınızda Alby Hub'ın otomatik olarak 354 Sats ayırdığını unutmayın. Bundan sonra açtığınız her Lightning kanalı için Alby Hub otomatik olarak kanalın kapasitesinin %1'ine eşdeğer bir rezerv ayıracaktır. Bu rezerv, eşiniz tarafından dolandırıcılık girişiminde bulunulması durumunda düğümünüzün kanalın fonlarını geri almasını sağlayan bir güvenlik önlemidir. Bu nedenle, 120.000 Sats göndermiş olmama rağmen, bakiyemde yalnızca 119.646 Sats görünüyor.


![ALBY HUB](assets/fr/33.webp)


## Zincir üzerinde bitcoin yatırma


Ödeme yapmak için giden nakit paraya sahip olmak istiyorsanız, kendiniz de bir kanal açabilirsiniz. Bunu yapmak için Wallet'unuzda zincir içi bitcoinlere ihtiyacınız olacak.


"*Node*" sekmesinden "*Deposit*" üzerine tıklayın.


![ALBY HUB](assets/fr/34.webp)


Görüntülenen Address'a bitcoin gönderin. Bu Address, önceden kaydedilmiş kurtarma cümlenizden türetilmiştir.


![ALBY HUB](assets/fr/35.webp)


72.000 Sats gönderdim. Artık Lightning'de değil, zincirde sahip olduğum tüm fonları içeren "*Tasarruf Bakiyesi*" bölümünde görülebiliyorlar.


![ALBY HUB](assets/fr/36.webp)


## Bir Lightning kanalı açın


Artık zincir içi fonlarınız olduğuna göre, yeni bir Lightning kanalı açabilirsiniz. Kısıtlama olmaksızın her zaman ödeme yapabilmenizi sağlamak için yeterli miktarda birkaç kanal açmanız önerilir. Çoğu LSP (*Lightning Hizmet Sağlayıcıları*) sizinle bir kanal açmak için en az 150.000 Sats gerektirir.


"*Node*" sekmesinde "*Open Channel*" seçeneğine tıklayın.


![ALBY HUB](assets/fr/37.webp)


Kanalınızın boyutunu seçin. Bunun bir Lightning düğümü olduğunu ve anahtarlarınızı barındıran makinenin bir Hardware Wallet ile aynı düzeyde güvenlik sunmadığını göz önünde bulundurarak çok küçük kanallar açmamanızı tavsiye ederim. Bu yüzden engellemeyi seçtiğiniz miktarlara dikkat edin.


![ALBY HUB](assets/fr/38.webp)


"*Gelişmiş Seçenekler*" menüsünde, kanalınızı hangi LSP ile açacağınızı seçebilir veya manuel olarak başka bir Lightning düğümü girebilirsiniz.


![ALBY HUB](assets/fr/39.webp)


Ardından "*Kanal Aç*" üzerine tıklayın.


![ALBY HUB](assets/fr/40.webp)


Kanalınız zincir üzerinde onaylanırken bekleyin.


![ALBY HUB](assets/fr/41.webp)


Yeni kanalınız şimdi "*Node*" sekmesinde görünecektir.


![ALBY HUB](assets/fr/42.webp)


## Düğüm yönetimi


Lightning kanallarınızı yönetmek düşündüğünüzden daha kolay. Alby Hub, Sats'i harcama bakiyeniz ile On-Chain bakiyeniz arasında aktarmanıza olanak tanır. Bu şekilde harcama veya alım kapasitenizi artırabilirsiniz.


![ALBY HUB](assets/fr/66.webp)


## Bir gider uygulamasını bağlayın


Artık çalışan bir Lightning düğümünüz olduğuna göre, bunu günlük olarak Sats almak ve harcamak için kullanabilirsiniz. Alby Hub'ın web Interface'sı düğümünüzü yönetmek için kullanışlı olsa da, hareket halindeyken hızlı işlemler yapmak için ideal değildir. Bunun için akıllı telefonumuzda yüklü bir Lightning Wallet uygulaması kullanacağız.


Bu eğitimde, kullanımı çok kolay olan Alby Go'yu tercih etmenizi öneririm, ancak Zeus gibi diğer uyumlu uygulamaları da kullanabilirsiniz.


![ALBY HUB](assets/fr/43.webp)


Alby Go'yu yüklemek için cihazınızın uygulama mağazasına gidin:




- [Android için](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple için](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Android kullanıcıları da uygulamayı `.apk' dosyası [Alby'nin GitHub'ında mevcut] (https://github.com/getAlby/go/releases) aracılığıyla yükleyebilirler.


![ALBY HUB](assets/fr/45.webp)


Uygulama başlatıldığında, "*Connect Wallet*" seçeneğine tıklayın.


![ALBY HUB](assets/fr/46.webp)


Alby Hub'ınızda, App Store'un altında "Alby Go "yu bulun ve "Bağlan "a tıklayın

![ALBY HUB](assets/fr/47.webp)

"Tek Sekmeli Bağlantılar ile Bağlan" seçeneğine tıklayın. Bu, Alby Hub'ınızı tek bir tıklamayla Alby Go kullanarak diğer uygulamalara bağlamanızı sağlayacaktır.


![ALBY HUB](assets/fr/48.webp)


Alby Hub daha sonra Alby Go ile bağlantı kurmak için generate sırrını verecektir.


![ALBY HUB](assets/fr/49.webp)


Alby Go uygulamasına geri dönün, QR kodunu tarayın veya sırrı yapıştırın.


![ALBY HUB](assets/fr/50.webp)


"Bitir*" üzerine tıklayın.


![ALBY HUB](assets/fr/51.webp)


Artık akıllı telefonunuzdan Lightning node destekli Alby Hub'ınıza uzaktan erişebilir, böylece her gün hareket halindeyken Sats'i harcamayı ve almayı kolaylaştırabilirsiniz.


![ALBY HUB](assets/fr/52.webp)


Gerekirse, bu bağlantı için izinleri doğrudan Alby Hub'da üzerine tıklayarak yönetebilirsiniz.


![ALBY HUB](assets/fr/53.webp)


Sats'yi almak için "*Al*" düğmesine tıklamanız yeterlidir.


![ALBY HUB](assets/fr/54.webp)


"*Invoice*" üzerine tıklayarak Invoice tutarını ve açıklamasını değiştirin.


![ALBY HUB](assets/fr/55.webp)


Sats'i almak için Invoice'ü şarj edin.


![ALBY HUB](assets/fr/56.webp)


Sats'yı göndermek için "*Gönder*" düğmesine tıklayın.


![ALBY HUB](assets/fr/57.webp)


Ödemek istediğiniz Invoice'yi tarayın.


![ALBY HUB](assets/fr/58.webp)


Ardından "*Ödeme*" üzerine tıklayın.


![ALBY HUB](assets/fr/59.webp)


İşleminiz onaylandı.


![ALBY HUB](assets/fr/60.webp)


Küçük oka tıklayarak işlem geçmişinize erişebilirsiniz.


![ALBY HUB](assets/fr/61.webp)


Bu işlemler Alby Hub'ınızda da görülebilir.


![ALBY HUB](assets/fr/62.webp)


## Lightning Address'inizi özelleştirin


Alby size Lightning Address seçeneği sunar. Bu, her seferinde manuel olarak generate bir Invoice yapmak zorunda kalmadan düğümünüzde ödeme almanıza olanak tanır. Varsayılan olarak, Alby size bir Lightning Address atar, ancak bunu özelleştirebilirsiniz. Alby çevrimiçi hesabınıza giriş yapın, sağ üst köşedeki adınıza tıklayın, ardından "*Ayarlar*" ı seçin.


![ALBY HUB](assets/fr/63.webp)


"*Lightning Address*" menüsüne gidin.


![ALBY HUB](assets/fr/64.webp)


Address'ünüzü değiştirin, ardından "*Yıldırım Address'ünüzü güncelleyin*" seçeneğine tıklayarak onaylayın.


![ALBY HUB](assets/fr/65.webp)


Lütfen Address'ünüz değiştirildikten sonra artık size ait olmadığını unutmayın. Bu yüzden bir daha asla Sats göndermediğinizden emin olun.


Ve işte bu kadar, artık Alby Hub aracını kullanarak Lightning'i kendi düğümünüzle nasıl kullanacağınızı biliyorsunuz. Bu öğreticiyi yararlı bulduysanız, aşağıya bir Green başparmak koyarsanız çok minnettar olurum. Lütfen bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Bu eğitimde manipüle ettiğimiz tüm Yıldırım mekanizmalarını ayrıntılı olarak anlamak için, konuyla ilgili ücretsiz eğitimimizi keşfetmenizi şiddetle tavsiye ederim:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb