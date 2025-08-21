---
name: Umbrel Nostr
description: Umbrel üzerinde Nostr uygulamalarını yapılandırma ve kullanma
---

![cover](assets/cover.webp)



## Önkoşullar: Umbrel kurulumu



Umbrel, Bitcoin uygulamalarını ve diğer hizmetleri kendi kişisel sunucunuzda kolayca barındırmanızı sağlayan açık kaynaklı bir platformdur. Bitcoin düğümlerinin ve merkezi olmayan uygulamaların kendi kendine barındırılmasını büyük ölçüde basitleştiren hepsi bir arada bir çözümdür.



Kurulum kılavuzumuzu takip ederek Umbrel'i yüklediğinizden emin olun:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Nostr'a Giriş



**Nostr** sosyal ağ için tasarlanmış açık, merkezi olmayan bir ağ protokolüdür. Adı _"Notlar ve Röleler Tarafından İletilen Diğer Şeyler"_ anlamına gelir. Herkesin JSON olayları olarak yönetilen mesajlar (notlar) yayınlamasına ve bunları merkezi bir platform yerine röle sunucuları aracılığıyla yaymasına olanak tanır. Her kullanıcı, bir tanımlayıcı görevi gören bir çift kriptografik anahtara (özel / genel) sahiptir: genel anahtar (npub) kullanıcıyı tanımlar ve özel anahtar (nsec) mesajların imzalanmasını sağlar. Bu dağıtık mimari sayesinde **Nostr sansüre karşı direnç** ve büyük esneklik sunar: tek bir sunucuya bağlı kalmadan birkaç istemci kullanabilir ve istediğiniz kadar röleye bağlanabilirsiniz.



Kısacası Nostr, **istemcilerin** (kullanıcı uygulamaları) **röleciler** (sunucular) aracılığıyla olay gönderip aldığı merkezi olmayan bir iletişim protokolüdür. Bu protokol, ademi merkeziyetçilik ve veri egemenliği değerleri nedeniyle 2023'ten beri Bitcoin topluluğu arasında özellikle popüler olmuştur.



**Not:** Nostr'u kullanmak için özel anahtarınıza (bir Nostr istemcisi tarafından veya özel bir uzantı aracılığıyla oluşturulmuş) ihtiyacınız olacaktır. **Herhangi birinin sizi taklit etmesine izin vereceğinden, özel anahtarınızı** asla paylaşmayın. Güvenli bir yerde saklayın ve güvenli anahtar yönetim araçları kullanın (aşağıdaki İpucuna bakın).



## Nostr için şemsiye uygulamaları



Umbrel, kişisel düğümünüzde Nostr'dan tam olarak yararlanmanız için entegre uygulamalardan oluşan bir ekosistem sunar. Nostr ile ilgili ana uygulamaların kullanımını detaylandıracağız: **Nostr Relay**, **noStrudel**, **Snort** ve **Nostr Wallet Connect**. Her biri belirli bir ihtiyacı karşılıyor: _Nostr Relay_ bir **özel röle sunucusu**, _noStrudel_ ve _Snort_ **Nostr istemcileri** (notları okumak/yayınlamak için arayüzler), _Nostr Wallet Connect_ ise **Lightning Wallet**'nizi Nostr'a bağlamak için bir araçtır.



### Nostr Relay - Umbrel'deki özel röleniz



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay**, düğümünüzde **kendi Nostr rölenizi** çalıştırmak için Umbrel'in resmi uygulamasıdır. Temel amaç, tüm Nostr** faaliyetlerinizi gerçek zamanlı olarak **yedeklemek için **özel** ve güvenilir bir röleye sahip olmaktır. Başka bir deyişle, genel rölelere ek olarak bu kişisel röleyi kullanarak, tüm notlarınızın, mesajlarınızın ve tepkilerinizin sansür veya veri kaybına karşı güvenli bir şekilde eve kopyalanmasını sağlarsınız.



**Kurulum:** Umbrel App Store'dan (_Social_ kategorisi) _Nostr Relay_ uygulamasını yükleyin. Uygulama başlatıldıktan sonra arka planda çalışır (docker servisi).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Umbrel aracılığıyla Interface web'ini göreceksiniz: temel bilgileri ve her şeyden önce, daha fazla kullanım için kopyalamanız gereken aktarıcınızın URL'sini (sağ üstte) sağlar. Bir senkronizasyon düğmesi (küre simgesi) de mevcuttur.



**Umbrel rölenizden yararlanmak için :



**Aktarıcıyı Nostr istemcinize ekleyin:** İstemci uygulamanızda (örneğin iOS'ta Damus, Android'de Amethyst, Umbrel'de Snort veya noStrudel vb.), daha önce kopyaladığınız özel aktarıcınızın URL'sini ekleyin. Varsayılan olarak, Umbrel aktarıcısı **4848** numaralı bağlantı noktasını dinler. Yerel ağ üzerinden erişirseniz, bu aşağıdaki gibi bir URL verir: `ws://umbrel.local:4848` (veya Umbrel'in yerel IP'sini kullanın).



Tailscale kullanıyorsanız (aşağıya bakın), MagicDNS DNS takma adını (genellikle `umbrel` veya otomatik oluşturulan bir ad) kullanarak her yerden, her zaman 4848 numaralı bağlantı noktasından erişebilirsiniz.



Tor'u tercih ediyorsanız, Umbrel'in .onion Address'ünü edinin ve Tor uyumlu bir tarayıcı veya istemci aracılığıyla 4848 numaralı bağlantı noktası ile kullanın (Tor bölümüne bakın)



URL, Nostr istemcinizin Aktarıcı yapılandırmasına eklendikten sonra, bu aktarıcıya bağlanın. İstemcinizde Umbrel aktarıcısının bağlı olduğunu görmelisiniz (genellikle bir Green noktası veya benzeri ile gösterilir).



**Geçmişi senkronize edin (isteğe bağlı)**: Umbrel'deki _Nostr Relay_'in Interface web'inde **globe** 🌐 simgesine tıklayın (sayfanın en üstünde). Bu eylem, Umbrel aktarıcınızı diğer aktarıcılarınıza (istemcinizde yapılandırılmış olanlar) bağlanmaya zorlayarak **eski genel** etkinliklerinizi içe aktaracaktır. Bu, genel aktarıcılar aracılığıyla yayınladığınız veya okuduğunuz geçmiş notların da indirileceği ve özel aktarıcınızda saklanacağı anlamına gelir. Lütfen senkronizasyonun gerçekleşmesini bekleyin.



**Nostr'u her zamanki gibi kullanın:** Şu andan itibaren, Nostr'da gerçekleştirdiğiniz tüm yeni etkinlikler (yayınlanan notlar, tepkiler, şifrelenmiş özel mesajlar, vb.) her zamanki gibi genel aktarıcılara **ve paralel olarak Umbrel aktarıcınıza** iletilecektir. Nostr istemciniz düzgün yapılandırılmışsa, her olayı tüm aktarıcılara (sizinki dahil) gönderecektir. Özel röleniz gerçek zamanlı bir yedekleme görevi görecektir. Geçici bir bağlantı kesilmesi durumunda bile, müşterileriniz bu röle sayesinde eksik verileri daha sonra yeniden senkronize edebilecektir. bu size Nostr verileriniz üzerinde tam kontrol sağlar



Arka planda, Umbrel'in _Nostr Relay_ açık kaynaklı **nostr-rs-relay** projesine (Rust protokol uygulaması) dayanmaktadır. Nostr protokolünün tamamını ve çok sayıda standart NIP'yi (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, vb.) destekleyerek müşterilerle maksimum uyumluluğu garanti eder.



### noStrudel - Kaşifler için Nostr istemcisi



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel**, Nostr ağını ayrıntılı olarak anlamak ve keşfetmek için ideal, güçlü kullanıcı odaklı bir Nostr web istemcisidir. Olayları ve röleleri incelemek ve protokolün gelişmiş özelliklerini denemek için bir tür sanal alan. Interface İngilizce ve nispeten tekniktir, bu da onu Nostr'un iç işleyişini merak eden deneyimli kullanıcılar için ideal kılar.



**Kurulum:** Umbrel Uygulama Mağazasından (_Sosyal_ kategorisi) _noStrudel_ uygulamasını yükleyin. Başlatıldıktan sonra, tarayıcınız aracılığıyla Umbrel'in Address adresinden erişilebilir (örneğin `http://umbrel.local` veya .onion/Tailscale aracılığıyla, harici erişim bölümüne bakın).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Röleleri yapılandırın:** noStrudel'i açtığınızda, sağ üst köşede bir "Röleleri Kur" düğmesi göreceksiniz. Rölelerinizi yapılandırmak için üzerine tıklayın.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Bu sayfada, daha önce kopyaladığınız Umbrel aktarıcınızın URL'sini yapıştırın. Uygulama tarafından varsayılan olarak önerilen diğer röleleri de ekleyebilirsiniz. Aktarıcılarınızı yapılandırdıktan sonra, devam etmek için sol alttaki "Oturum aç" seçeneğine tıklayın.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Bağlantı:** noStrudel size çeşitli bağlantı seçenekleri sunar. Bizim durumumuzda, "Özel Anahtar "ı seçeceğiz ve önceden oluşturulmuş Nostr özel anahtarınızı yapıştıracağız. Henüz bir anahtarınız yoksa, Nostr anahtarlarınızı oluşturmak ve/veya kaydetmek ve böylece çeşitli Nostr uygulamalarıyla daha güvenli bir şekilde iletişim kurmak için [Nostr Connect] uzantısını (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) yükleyebilirsiniz.



![Interface principale de noStrudel](assets/fr/07.webp)



Bağlandıktan sonra, notlarınızı Nostr aracılığıyla paylaşmak için noStrudel'i kullanabilirsiniz. Interface size erişim sağlar :





- Notlar zaman çizelgesi, bildirimler, mesajlaşma, profil arama ile eksiksiz Nostr kontrol paneli
- Röle yönetimi ve bağlantı durumu
- Olayları ve JSON içeriklerini incelemek için gelişmiş araçlar
- Zaman çizelgesi filtreleri ve PIN'ler için yapılandırma seçenekleri



**İpucu:** _noStrudel_ üzerinde _timeline filters_ ayarlayabilir veya farklı _NIP'leri (Nostr Implementation Possibilities)_ test edebilirsiniz. Örneğin, NIP-05 (merkezi olmayan tanımlayıcılar) veya daha yeni özellikler için desteği kontrol edin. Bu, _noStrudel_ 'i kontrollü bir ortamda deney yapmak için mükemmel bir araç haline getirir.



### Snort - Umbrel'de Modern Nostr müşterisi



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort**, Umbrel'de bulunan ve merkezi olmayan sosyal ağ ile etkileşim için modern, hızlı ve düzenli bir **Interface** sunan başka bir Nostr web istemcisidir. Güçlü kullanıcıları hedefleyen noStrudel'in aksine, _Snort_ işlevsellikten ödün vermeden kullanım kolaylığını amaçlamaktadır. React'te inşa edilmiştir ve klasik sosyal ağları anımsatan temiz bir kullanıcı deneyimi sunarak günlük kullanım için uygun hale getirir.



**Kurulum:** Umbrel App Store'dan (_Social_ kategorisi) _Snort_ uygulamasını yükleyin.



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Snort'u açtığınızda, sol alt köşede bir "Kayıt Ol" düğmesi göreceksiniz.



![Options de connexion dans Snort](assets/fr/10.webp)



Kayıt olmayı veya mevcut bir hesaba bağlanmayı seçebilirsiniz (bu eğitim için yapacağımız şey budur).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort çeşitli bağlantı yöntemleri sunar. Önceden yüklenmiş Nostr Connect uzantısını veya diğer mevcut yöntemleri kullanabilirsiniz. Bağlandıktan sonra, uygulamayı tam olarak kullanabileceksiniz.



_Snort_'tan Interface şunları sunar :





- Notlarınız, başlık altındaki tartışmalar veya genel akış arasında gezinmek için bir **Postalar/Görüşmeler/Global** ekranı
- Bildirimler**, **Mesajlar** (DM), **Arama**, **Profil**, vb. için sekmeler.
- Yeni bir not yayınlamak için bir **+** veya _Yaz_ düğmesi
- Aboneliklerin (takip eden)** ve **listelerin** yönetimi
- Röle eklemek/kaldırmak ve kullanılabilirliklerini takip etmek için röle yönetim menüsü



**Önerilen röle yapılandırması:** Umbrel rölenizi eklemek için Ayarlar - Röleler bölümüne gidin. Snort'un röleler listesine rölenizin URL'sini (`ws://umbrel:4848` veya yapılandırmanıza bağlı olarak başka bir URL) girin. Bu şekilde, Snort notlarınızı herkese açık olanlara ek olarak özel aktarıcınızda da yayınlayacaktır.



### Nostr Wallet Connect - Lightning Wallet'ünüzü Nostr'a bağlayın



**Nostr Wallet Connect (NWC)**, Lightning ödemeleri yapmak için (örneğin, içeriği "beğenmek" için mikro ödemeler olan _zaps_ göndermek) Umbrel (Lightning)** düğümünüzü uyumlu Nostr uygulamalarına bağlayan bir uygulamadır. Bu eğitimde, doğrudan Interface'ten ödeme yapmak için noStrudel'i Lightning düğümünüze nasıl bağlayacağınıza bakacağız.



**Kurulum ve yapılandırma:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Umbrel'deki Alby mağazasından _Nostr Wallet Connect_ yükleyin.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



NoStrudel'de sağ üst köşedeki profilinize ve ardından "yönet" düğmesine tıklayın.



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



"Yıldırım" ve ardından "Wallet'yi bağla" üzerine tıklayın.



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Mevcut bağlantı seçenekleri arasından "Umbrel "i seçin.



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Otomatik olarak Umbrel Nostr Wallet Connect oturumunuza yönlendirilmek için "Bağlan "a tıklayın.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Nostr Wallet Connect sayfasında şunları yapabilirsiniz:




   - Maksimum bütçenizi belirleyin
   - Yetkileri doğrulayın
   - Bağlantı için bir sona erme süresi ayarlayın


Sonlandırmak için "bağlan "a tıklayın.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Bir onay mesajı ile noStrudel'e yönlendirilirsiniz: artık Wallet/LND düğümünüzden tüm dünyayı zaplayabilirsiniz!



NWC sayesinde, Nostr** üzerinden **Lightning ödemeleriniz (ödül gönderilerine zaplar, _Değer için Değer_ ödemeleri vb.) **kendi düğümünüzden** başlar. Artık işlemlerinizi harici hizmetler üzerinden yönlendirmek veya her seferinde telefonunuzdan bir QR taramak zorunda değilsiniz. Kullanıcı deneyimi büyük ölçüde geliştirilirken, _gözetimsiz_ ve gizlilik dostu kalır.



Umbrel üzerinde kendi Lightning düğümünüzü nasıl kuracağınızı öğrenmek istiyorsanız, bu diğer kapsamlı eğitime göz atmanızı tavsiye ederim:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Gelişmiş yapılandırma ve güvenlik



Umbrel ve Nostr'u ileri düzeyde birlikte kullanmak **güvenlik** ve **bağlantı** konularına özel dikkat gerektirir. İşte yapılandırmanızı nasıl koruyacağınıza ve nerede olursanız olun en iyi şekilde nasıl erişeceğinize dair birkaç ipucu.



### Güvenli harici erişim: Tor ve Tailscale



Güvenlik nedeniyle, Umbrel'inize varsayılan olarak yalnızca yerel ağınızdan (ve Tor üzerinden) erişilebilir. Nostr ile evden uzakta etkileşim kurmak için tercih ettiğiniz iki çözüm vardır: **Tor** (onion ağı üzerinden anonim erişim) ve **Tailscale** (özel VPN ağı).





- Tor üzerinden erişim:** Umbrel, Interface web ve uygulamaları için otomatik olarak bir **Tor hizmeti (.onion)** yapılandırır. Bu, Interface Umbrel'e (_noStrudel_ veya _Snort_ dahil) Tor tarayıcısını kullanarak, genel IP'nizi açığa çıkarmadan her yerden erişebileceğiniz anlamına gelir. tor, Umbrel hizmetlerinize yerel ağınızın dışından, cihazınızı İnternet'e maruz bırakmadan erişmek için kullanılır ([Sisteminize Tor Kurun - Kılavuzlar - Umbrel Topluluğu](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Bu seçeneği kullanmak için Umbrel ayarlarına gidin ve Umbrel'inizin .onion URL'sini alın (veya sağlanan QR kodunu tarayın). Bir Tor tarayıcısında, bu .onion Address'e erişin: yerel olarak aynı Interface'yi alacaksınız. Daha sonra Nostr uygulamalarınızı tıpkı evinizdeki gibi kullanabilirsiniz.


**Tor üzerinden Nostr aktarıcısı:** Nostr aktarıcınızın müşterileriniz (veya yetkili arkadaşlarınız) tarafından Tor üzerinden erişilebilir olmasını istiyorsanız, bu mümkündür. Umbrel, aktarıcının .onion Address'ünü doğrudan sağlamaz, ancak 4848 numaralı bağlantı noktasında çalıştığından, ya :





    - UI Umbrel'in .onion Address'sını kullanın ve istemcinizi bu Interface üzerinden bağlanacak şekilde yapılandırın (WebSocket için pratik değildir),





    - Veya** 4848 numaralı bağlantı noktasını ayrı bir onion hizmeti olarak açığa çıkarın. Bu, Umbrel'deki Tor yapılandırmasıyla uğraşmayı gerektirir (SSH konusunda rahat olan ileri düzey kullanıcılar için ayrılmıştır). Alternatif olarak, Umbrel'e yönlendiren başka bir sunucuda bir **Tor tüneli** düşünebilirsiniz: ancak kişisel kullanım için Tailscale kullanmak en kolay yoldur.





- Tailscale üzerinden erişim:** [Tailscale](https://tailscale.com/), cihazlarınız ve Umbrel arasında sanal bir özel ağ oluşturan bir örgü VPN çözümüdür. Avantajı: sanki bir LAN'daymışsınız gibi çalışır, ancak İnternet üzerinden, şifreli ve karmaşık yapılandırma olmadan. **Tailscale, Umbrel'inize ağ konumundan bağımsız olarak sabit bir IP ve özel bir alan adı atar ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. Pratikte, Tailscale'i Umbrel'e (Umbrel App Store'dan, _Networking_ kategorisinden) **ve** cihazlarınıza (mobil, PC...) yükledikten sonra, Umbrel'e `100.x.y.z` (Tailscale IP) gibi bir Address veya `umbrel.tailnet123.ts.net` gibi bir ad aracılığıyla erişebileceksiniz.


nostr_ için Tailscale son derece kullanışlıdır: cep telefonunuz, eğer Tailscale aktifse, `ws://umbrel:4848` adresine (MagicDNS sayesinde) veya doğrudan Tailscale IP'sine ve 4848 numaralı bağlantı noktasına bağlanarak aktarıcıyı kullanabilecektir. Damus veya Amethyst gibi istemciler Umbrel'inizi aynı yerel ağdaymış gibi görecektir. **İpucu:** IP'yi ezberlemek yerine `umbrel` ana bilgisayar adını kullanmak için Tailscale'de **MagicDNS** seçeneğini etkinleştirin. Bu, hareket halindeyken bile aktarıcınıza sorunsuz bir bağlantı sağlar ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Dahası, Tailscale Interface Umbrel'e (ve dolayısıyla _noStrudel/Snort_ web istemcilerine) özel IP veya atanmış alan adını kullanarak basit bir tarayıcı aracılığıyla erişmenizi sağlar. Tor Tarayıcıya gerek yoktur ve veri aktarım hızları genellikle Tor ağı üzerinden olduğundan daha iyidir.




**Not: Tor ve Tailscale birbirini dışlamaz. Anonimleştirilmiş erişim veya belirli hizmetler için Tor'u etkin tutabilir ve basitliği için Tailscale'i günlük olarak kullanabilirsiniz. Her iki durumda da yönlendiricinizde bir bağlantı noktası açmanız gerekmez, bu da güvenliği güçlendirir.



### Nostr aktarıcınızın güvenliğini sağlama (önerilen uygulamalar)



Umbrel'de bir Nostr aktarıcısı barındırıyorsanız, özellikle de gelişmiş bir bağlamda, birkaç iyi uygulama uyguladığınızdan emin olun:





- Özel veya kısıtlı aktarıcı:** Varsayılan olarak, Umbrel aktarıcınız özeldir (herkese açık değildir) ve yalnızca Tailscale veya LAN'ınız üzerinden erişirseniz, yabancılar için erişilemez kalacaktır. **Bağlantıyı gizli tutun ** Diğer kullanıcıları gönüllü olarak barındırmak istemiyorsanız, bunu herkese açık Nostr ağlarında yayınlamayın, bu tamamen başka bir konudur (moderasyon, bant genişliği vb.). Kişisel kullanım için, erişimi kendinizle ve gerekirse birkaç güvenilir arkadaşınız ve ailenizle sınırlandırmanızı öneririz.





- Beyaz Liste / Auth**: Nostr-rs-relay uygulaması bir **NIP-42** kimlik doğrulama mekanizmasının yanı sıra açık anahtarların _beyaz listelerini_ destekler. Bu seçenekleri etkinleştirerek, aktarıcınızı **sadece belirli anahtarlar (sizinki)** tarafından imzalanmış olayları kabul edecek veya istemcilerin yayınlamak için kimlik doğrulaması yapması gerekecek şekilde kısıtlayabilirsiniz. bunu ayarlamak, Umbrel'deki aktarıcının `config.toml` yapılandırma dosyasını düzenlemeyi gerektirir (Docker konteynerinde SSH aracılığıyla)._ Bu gelişmiş bir manipülasyondur, ancak örneğin izin verilen reklamları listeleyebilirsiniz (`pubkey_whitelist`). Bu şekilde, birisi aktarıcınızı keşfetse bile, listede yer almıyorsa orada herhangi bir şey yayınlayamaz.





- Güncellemeler ve bakım:** Umbrel ve _Nostr Relay_ uygulamanızı güncel tutun. Güncellemeler performans iyileştirmeleri (örn. daha iyi spam işleme) ve güvenlik düzeltmeleri içerebilir. Umbrel'de, _Nostr Relay_ güncellemeleri için App Store'u düzenli olarak kontrol edin ve gerektiğinde bunları uygulayın.





- İzleme ve limitler:** Rölenizin nasıl kullanıldığına dikkat edin. Başkalarına açarsanız, bir röle hızla çok fazla veri biriktirebileceğinden, Umbrel'inizdeki yüke (CPU / RAM depolama) dikkat edin. nostr-rs-relay yapılandırılabilir **hız ve depolama limitleri** sunar (yapılandırmadaki `limits`, örneğin saniyedeki olay sayısı, maksimum olay boyutu, eski olayların temizlenmesi ...). Özel kullanım için muhtemelen bunlara dokunmanız gerekmeyecektir, ancak ihtiyacınız olursa bu parametrelerin var olduğunu unutmayın ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Nostr anahtarlarının güvenliğini sağlamak:** Bu noktadan daha önce bahsedilmişti, ancak çok önemlidir: Nostr özel anahtarlarınızı asla tam olarak güvenmediğiniz bir Interface'a girmeyin. Bunun yerine, hassas eylemleri imzalamak için tarayıcı uzantılarını veya harici cihazları (ayrı telefonlardaki Nostr _signers_ gibi) kullanın. Umbrel'de, _Snort_ ve _noStrudel_ gibi web istemcileriniz NIP-07 aracılığıyla gizli anahtarınızı bilmeden çalışabilir. Konfor ve güvenliği birleştirmek için bu fırsattan yararlanın.




Bu ipuçlarını takip ederek, bir Umbrel düğümünü Nostr ile entegrasyonunuz hem güçlü **hem de** güvenli olacaktır. Eksiksiz bir ortama sahip olacaksınız: Lightning ödemeleri için bir Bitcoin düğümü, veri egemenliği için özel bir Nostr aktarıcısı ve bu yeni merkezi olmayan sosyal ağda gezinmek için yüksek performanslı Nostr web istemcileri. Umbrel ile Nostr'u keşfetmenin tadını çıkarın!