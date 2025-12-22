---
name: Alias Vault
description: Parolaları, iki faktörlü kimlik doğrulamayı ve takma adları yönetmek için güçlü bir araç (yerleşik e-posta sunucusu ile) - Ayrıca kendi kendine barındırılır!
---

![cover](assets/cover.webp)



Çevrimiçi gizlilik ve güvenlik, işi ne olursa olsun herkesin çok dikkat etmesi gereken bir konudur.



Üstelik bu sorunlar, sürekli çalkantı içinde olan bir dünyanın parçasıdır: giderek daha fazla geliştirici konuya katılmakta, yerleşik çözümlere ve yeni ürünlere uygulamalar getirmektedir.



Bu, **Leendert de Borst** ve onun parolaları yönetmenize ve saklamanıza, web hizmetlerine kimlik doğrulaması yapmak için parola kayıtlarını kullanmanıza, iki faktörlü kimlik doğrulamayı yönetmenize ve en önemlisi generate gerçek _alias_'ları tek bir Interface'da yönetmenize olanak tanıyan devrim niteliğinde bir araç (türünün ilk örneği) olan `Alias Vault` için geçerlidir.



**Ama Alias Vault burada bitmiyor**.



## Temel Özellikler



Alias Vault, geliştiricinin sunucularında bulutta veya Docker dosyalarının ve görüntüsünün bir scipt ile kurulabileceği bir seçenek olan kendi altyapısında kendi kendine barındırılmış olarak çalışır. Web Interface'ye ek olarak, tüm popüler tarayıcılar için uzantıların yanı sıra iOS ve Android için mobil uygulamalar da mevcuttur; ikincisi, resmi Google mağazasını atlayarak F-Droid'den de indirilebilir.



Bir Interface Alias Vault'ta:




- Ücretsiz ve açık kaynak**
- Password Manager**, tüm karmaşık şifreleri saklamak için. Tarayıcı uzantısını kullanarak, parola yöneticisi web sitelerine girişleri tamamlar
- 2FA**, iki faktörlü kimlik doğrulamayı desteklemek için
- Yerleşik e-posta sunucusuna sahip takma ad yöneticisi**: Alias Vault, e-postayı kullanıcının posta kutusuna ileten takma adlar oluşturmaz; bunun yerine, ad, soyad, cinsiyet, kullanıcı adı, şifre ve doğum günü (bu bilgiler gerekliyse) ile tamamlanan gerçek alter-egolar oluşturur.



Bu güçlü aracın keşfinde yeni gelenlere eşlik edecek kapsamlı ve eksiksiz bir dokümantasyon paketin bir parçasıdır.



## Kişisel veri yok!



Her zaman olduğu gibi [aliasvault.net](aliasvault.net) web sitesinden başlar. Belirtildiği gibi, Alias Vault kişinin kendi sunucusunda veya kendi kendine barındırılan çözüme geçmeden önce onu tanımak için geliştiricinin bulutundan kullanılabilir.



Sitenin gerçekten göz alıcı ve bakımlı grafikleri var, ancak iyi şeyler ellerinizi kullanmaya başlarsanız gelir: **hesabınızı oluşturun**.



![img](assets/en/01.webp)



Büyük bir sürpriz olarak, Alias Vault'un kişisel bilgi istemediğini göreceksiniz: hesabı oluşturmak için ihtiyacınız olan tek şey, mevcut olduğu sürece size tanıdık gelen bir kelime olan herhangi bir takma addır. Hizmet Şartlarını kabul edin, kelimeyi seçin ve devam edin.



![img](assets/en/02.webp)



Tüm yeni sisteminizdeki en önemli bilgi olan **`ana şifre`yi`** şimdi belirleyin. Bu tek şifre ile, aslında, bilgilerinizi barındıracak sunucuda `vault`unuzu şifreli tutacağından, hesaba erişebilen / kurtarabilen tek kişi siz olacaksınız.



![img](assets/en/03.webp)



Gerçek: Kendi şifre yöneticinizi ve takma ad yöneticinizi oluşturdunuz, ancak kendi çalışan, özel e-posta Address'ünüzü vermediniz.



![img](assets/en/04.webp)



Alias Vault sizi güvenli, yeni, kişisel ama aynı zamanda boş bir alana davet ediyor. Ve şimdi onu biraz doldurmaya başlıyoruz.



Zaten bir parola yöneticiniz varsa, diğer sağlayıcılarla farklılıkları değerlendirmek için dosyayı kullandığınız sağlayıcıdan içe aktarabilir veya belki de her şeyi tek bir uygulamada yönetebilmek için takma ad yöneticisini ortadan kaldırabilirsiniz.



![img](assets/en/05.webp)



Alias Vault son derece basittir: iki menüye sahip `Home` olan bir ana sayfanız vardır:




- `Credentials`: kimlikler ve takma adlar oluşturmanıza ve yönetmenize olanak tanır
- `E-posta`: oluşturduğunuz takma adlar için gelen mesajları kontrol edebileceğiniz bir gelen kutusu.



![img](assets/en/06.webp)



Bizim ilgilendiğimiz ilk `takma ad`ın oluşturulmasıdır, bu nedenle sayfanın sağ üst köşesine gidin ve _+Yeni Takma Ad_ seçeneğine tıklayın.



![img](assets/en/07.webp)



Başlangıçta menü, Alias Vault'un felsefesine uygun olarak minimal görünüyor. Bu işlevin özelliklerini keşfetmek için _Create via advanced mode_ seçeneğine tıklayın.



![img](assets/en/08.webp)



İlk ekranın üst kısmı, aboneliğiniz olan hizmetler için zaten kullandığınız veya çevrimiçi olarak en sık kullandığınız parola kimlik bilgilerini içe aktarmak için kullanabilirsiniz.



Yukarıdaki hizmetlerden herhangi birinde (veya tümünde) iki faktörlü kimlik doğrulamayı etkinleştirdiyseniz, Alias Vault ile `secret key`i içe aktararak bu ek Layer güvenliğini de yönetebilirsiniz. Alias Vault erişim için gerekli `TOTP`yi oluşturacaktır.



![img](assets/en/09.webp)



**Dikkat**: E-posta Address için ayrılan alanda, Alias Vault varsayılan olarak kendi alan adını önerir; daha önce hesap oluşturduğunuz doğru Address'yı kullanmak için, _Özel alan adı girin_ seçeneğine tıklayın, böylece `@' dan sonra doğru alan adını ayarlayabilirsiniz.



![img](assets/en/14.webp)



Bu ekranın alt kısmı en eğlenceli kısmıdır. Rastgele Takma Ad Oluştur'a tıkladığınızda Alias Vault farklı ihtiyaçlarınız için her biri kendi posta kutusuna, çok sağlam düzey şifrelere sahip, cinsiyet, doğum tarihi ve uygun bir takma ad gibi diğer ayrıntılarla desteklenmiş ayrı kimlikler oluşturacaktır.



![img](assets/en/10.webp)



Uygun bir menüden, yalnızca küçük harfleri seçmek ve belirsiz olabilecek karakterleri ortadan kaldırmak gibi parola oluşturmayı etkileyen ayarları değiştirebilirsiniz.



![img](assets/en/11.webp)



Alias Vault tarafından önerilen takma e-postayı kullanabilir veya ilgili açılır menüye tıklarsanız alan adlarını değiştirebilirsiniz.



![img](assets/en/12.webp)



Bu e-postayı bir oturum açma hizmeti için kullanmadan önce, kendi Address'nizden yeni oluşturulan posta kutusuna bir mesaj göndererek işlevselliğini test edebilirsiniz.



![img](assets/en/13.webp)



**⚠️ UYARI**: Alias Vault'un yerleşik sunucusu sayesinde e-postaların alınması mümkündür, ancak bu yalnızca e-postaları almanıza ve yanıtlamanıza veya e-posta kutusunu bir `alias` hizmetinin "geleneksel" işlevleriyle kullanmanıza izin vermez. Bu nedenle Simple Login, Addy ve yalnızca bu tür hizmetlere adanmış diğer platformlardan büyük ölçüde farklıdır. Simple Login örneği için özel öğreticiyi görüntüleyebilirsiniz:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Test olarak oluşturduğunuz bir takma adı silmek için tek yapmanız gereken `Ev`, ardından `Kimlik Bilgileri` bölümüne giriş yapmak ve silmek istediğiniz kimliğe tıklamaktır. Devam edebilmeniz için sağ üst köşede _Delete_ komutu görünecektir.



![img](assets/en/16.webp)



## Tarayıcı uzantısı



İhtiyaçlarınızın ne olduğuna bağlı olarak, en yaygın kullanılan tarayıcılarda bulunabilen tarayıcı uzantısına başvurabilirsiniz.



![img](assets/en/15.webp)



Diğer tüm uzantılarda yaptığınız gibi yüklenir, bu yüzden bu ayrıntı üzerinde durmayacağım.



Tarayıcı uzantısı, çevrimiçi hizmetlerde oturum açmayı veya gerektiğinde yeni takma adlar oluşturmayı kolaylaştırmak için vardır: hizmet Takma Ad Kasası kayıtlarınız arasında saklanıyorsa, otomatik doldurma gerekeni yapar.



![img](assets/en/17.webp)



Dikkat edilmesi gereken tek nokta Alias Vault'un aktif olduğunu doğrulamaktır. Aslında, uygulamanın varsayılan bir ayarı vardır, bu sayede belirli bir süre kullanılmadığında duraklar. Bu, **örneğin bilgisayarınızdan uzaklaşmanız ve başka birinin hesaplarınıza erişmesini engellemeniz gerektiğinde** çok kullanışlı bir özelliktir. Kolaylaştırılmış bir prosedür, önceki oturum hala önbellekte ise, `ana şifre`yi girerek tekrar oturum açmanıza izin verecektir. Oturumu kapatma süresi, tercihlerinize göre kısaltarak veya uzatarak özelleştirebileceğiniz parametrelerden biridir.



## Mobil Uygulama



Bu türden kendine saygısı olan tüm uygulamalar gibi, Alias Vault'un da hem Android hem de iOS ortamlarında mobil cihazlar için bir sürümü vardır. Android için uygulamayı [F-Droid](https://f-droid.org/packages/net.aliasvault.app/) adresinden indirebilirsiniz.



Bu yazının yazıldığı sırada (Ağustos 2025 sonu), mobil uygulama `otomatik doldurma` özelliğini deneysel bir özellik olarak görüyor ve çok az sayıda site dışında çalışmıyor. Tam olarak uygulanana kadar, mobil cihazlarda Alias Vault kullanmak için verilerin kopyalanması/yapıştırılması gerekmektedir.



Uygulamayı mağazadan indirdikten sonra, giriş yapmak için web uygulamasında oluşturulan kullanıcı ve `ana şifre`yi girmeniz yeterlidir.



![img](assets/en/18.webp)



Kasanızı açarken, başka birinin telefonunuzu tutması durumunda şifrelerinize erişmesini önlemek için ek bir Layer güvenliği olan biyometrik olarak kontrol edilen erişimi etkinleştirmek isteyip istemediğiniz sorulacaktır.



![img](assets/en/19.webp)



Biyometrik kontrolü ayarlamaya karar verirseniz, devam edin. Bu adımı atlar ve fikrinizi değiştirirseniz, daha sonra _Ayarlar_ menüsünden de yapılandırabilirsiniz.



Oturum açmayı tamamladığınızda, önceden oluşturduğunuz verilerin yeniden senkronize edildiğini göreceksiniz.



![img](assets/en/20.webp)



Mobil uygulama, kendi sunucusunda barındırılan `vault` bağlantısına yönlendirilebilir.



![img](assets/en/22.webp)



Bir sonraki bölümde kısaca Address'u anlatacağımız da tam olarak bu kendi kendine barındırılan versiyon.



## Self-Hosting: verileriniz üzerinde tam kontrol



Alias Vault, adil olmak gerekirse, hizmeti altyapınıza dağıtmanıza izin veren ilk `parola yöneticisi` değildir. Başkaları da var, ancak bazılarının ya sınırlamaları var ya da kısmen kapalı kaynak.



Bu fırsat benzersizdir: **Harici hizmet sağlayıcılara veya bulutlara bağımlılığa son verin, ancak parolaları, takma adları ve tüm bunlarla ilişkili son derece hassas bilgileri korumak ve yönetmek için kendi yerel sunucunuzu kullanın**. Alias Vault ile daha fazla gizlilik için e-posta hizmetinin kendi e-posta sunucunuza yönlendirilmesini de sağlayabilirsiniz.



Alias Vault'u kendi kendinize barındırmaya nasıl devam edeceğinizi öğrenmek için [documentation](https://docs.aliasvault.net/installation/) adresine dönmenin zamanı geldi.



![img](assets/en/23.webp)



Alias Vault Docker Compose üzerinde çalışır, bu nedenle Linux ve Docker ile minimum deneyim gereklidir. Temel kurulumla başlayabilir ve daha sonra daha gelişmiş çözümlerle tamamlayabilirsiniz.



Sunucunuz bir Linux dağıtımı, 1 GB RAM ve en az 16 GB depolama alanına sahip 64 bit bir makinede çalışıyor olmalıdır; Docker (CE) sürümü en az 20.10 veya daha yüksek olmalıdır, Docker Compose ise 2.0 ve üzeri bir sürüm gerektirir.



Alias Vault'u, DietPi'nin bir dağıtım olarak kurulduğu, Debian Bookworm tabanlı, temel özelliklere göre optimize edilmiş ve zaten `Docker` ve `Docker Compose` çalıştıran ince bir istemci ile denemeye karar verdim.



Öncelikle, biraz düzen sağlamak için, evinizde bir dizin oluşturun, `terminal`i açın ve kurulum betiğini çalıştırmak için komutu yapıştırın.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Kurulum tamamlandığında, erişim için kimlik bilgilerinizi bulacaksınız:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Kurulumdan sonra dizinin içeriğini kontrol edin.



![img](assets/en/29.webp)



Alias Vault'u başlatmak için şu komutu kullanın:



``` Launch-Alias-Vault


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/kullanıcı/başlat


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Şifreleme ve güvenlikle ilgili hususlar



![img](assets/en/32.webp)



Lanedirt'in sitede, belgelerde ve Github'da belirttiğine göre, Alias Vault ile **Alias Vault'a yerleştirdiğiniz tüm bilgiler (bileşenler) cihaza sıkıca bağlı kalır, şifrelenir ve `ana şifreyi` bilmeyen herkes tarafından erişilemez**.



Bu nedenle `ana şifre` tüm `vault`un temel unsurudur. Girildikten sonra, sırrın cihazdan çıkmasını önlemek için bir Hard-bellek anahtarı türetme işlevi olan `Argon2id` algoritması ile işlenir.



Bulut veya barındırma hizmeti yöneticisinden bile her şey gizli kalır. Aslında, yönetici panelinden kullanıcı ayrıntılarına erişemezsiniz, yalnızca takma ad oluşturup oluşturmadıklarını, e-posta alıp almadıklarını ve başka çok az şeyi öğrenebilirsiniz.



Depolanan tüm içerikler `ana şifre`den türetilen kriptografik anahtarlarla şifrelenir ve şifreleri çözülür. **Sunucuda yalnızca şifrelenmiş veriler saklanır, hiçbir şey düz metin olarak görünmez**. Bir kullanıcı `ana parolasını` unutur veya kaybederse, sunucu düz metin içeriğine erişemeyeceğinden, buna bağlı hesap geri döndürülemez şekilde kaybolur.



Kendi kendine barındırılan sürüm için `ana parolayı` sıfırlamak için bir komut dosyası vardır, ancak bu veri kaybını önlemez.



![img](assets/en/33.webp)



Alias Vault _Beta_ aşamasında olduğundan, ana şifreyi değiştirirseniz/güncellerseniz erişmekte zorluk çekebilirsiniz. Baştan sağlam ve karmaşık bir şifre seçmenizi öneririm, böylece hizmeti deneyebilir ve sonunda kullanıp kullanmayacağınıza karar verebilirsiniz. Parola güncellemesinin ardından buluta erişmekte zorluk yaşarsanız, lütfen Alias Vault destek birimiyle iletişime geçin.



Alias Vault tarafından benimsenen mimari ve güvenliği tam olarak anlamak için, işleyişinin altında yatan kriptografinin ayrıntılarını içeren [bu sayfaya](https://docs.aliasvault.net/architecture/) başvurmanızı şiddetle tavsiye ederim.



## Yol Haritası


Geliştiricilerin niyeti, Alias Vault'un gelecekteki kullanım özelliklerini tanımlamak için 2025'in sonuna kadar olgun ve kararlı hale getirmektir.



Alias Vault her zaman açık kaynak kodlu ve ücretsiz olacaktır, ancak muhtemelen beta sürümündeki gibi sınırsız olmayacaktır. Daha önce duyurulduğu gibi bazı ücretli özellikler uygulanma sürecindedir.



Ekip/aile planları ve FIDO2 veya WebAuth ile kimlik doğrulama için donanım anahtarları desteği vardır.



## Kimin Alias Vault'a ihtiyacı var?



**Bunun gibi bir araç, çevrimiçi gizliliğe önem veren herkes için idealdir**.



Kimliğiniz, büyük olasılıkla, çevrimiçi yürüttüğünüz işlerin merkezinde yer almaktadır ve **bu** verileri çevrimiçi davranışlarınıza el koymak için her şeyi yapmaya istekli hizmetlerden, şirketlerden ve aracılardan uzak tutmak için her şekilde korunmalıdır.



Alias Vault, kimlik bilgileriniz üzerinde tam kontrol sahibi olmanızı sağlayarak en hassas verilerinizi korumak ve şifrelemek için üçüncü taraflara güvenme ihtiyacını azaltır veya tamamen ortadan kaldırır.



Alias Vault'un mimarisi ve kriptografik tesisi, egemen bireyler, küçük ve orta ölçekli işletmeler, geliştirme ekipleri ve tüm **açık kaynak** uygulama meraklıları için idealdir. Bu kategorilerden herhangi birine giriyorsanız: Alias Vault'u keşfederken iyi eğlenceler.