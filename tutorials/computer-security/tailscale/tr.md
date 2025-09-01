---
name: Kuyruk Ölçeği
description: Gelişmiş Tailscale eğitimi
---
![cover](assets/cover.webp)



## 1. Giriş



Tailscale, cihazlarınız arasında şifrelenmiş bir örgü ağ oluşturan yeni nesil bir VPN'dir. Karmaşık yapılandırma veya bağlantı noktası açma olmadan uzak makineleri aynı yerel ağdaymış gibi bağlamanızı sağlar.



Kendi kendine barındırma için Tailscale, her cihaza sanal bir ağda sabit bir özel IP atar ve genel IP'niz değişse bile hizmetlerinize istikrarlı erişim sağlar. Bu, hizmetlerinizi doğrudan internete maruz bırakmadan sunucularınızı uzaktan yönetebileceğiniz anlamına gelir.



**Ana uygulamalar:**




- Kişisel bir sunucuyu dışarıdan yönetme
- Umbrel/Lightning düğümlerini Tor'dan daha hızlı yönetin
- Raspberry Pi veya NAS'a güvenli erişim
- Karmaşık ağ yapılandırması olmadan SSH veya HTTP aracılığıyla hizmetlerinize bağlanın



Bu basitlik odaklı yaklaşım, kendi kendini barındıranların geleneksel VPN'lerin tuzaklarından kaçınarak hizmetlerine güvenli bir şekilde erişmelerini sağlar.



## 2. Tailscale nasıl çalışır?



Tüm trafiği merkezi bir sunucu üzerinden yönlendiren geleneksel VPN'lerin aksine Tailscale, cihazların birbirleriyle doğrudan iletişim kurduğu bir örgü ağ oluşturur. Merkezi sunucu, kullanıcı verilerini görmeden yalnızca kimlik doğrulama ve anahtar dağıtımını gerçekleştirir.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Şekil 1: Tüm trafiğin merkezi bir sunucudan geçtiği hub-and-spoke mimarisine sahip geleneksel VPN*



WireGuard temelinde, her cihaz kendi kriptografik anahtarlarını oluşturur. Koordinasyon sunucusu genel anahtarları düğümlere dağıtır ve düğümler de doğrudan kendi aralarında uçtan uca şifrelenmiş tüneller kurar. Tailscale, güvenlik duvarlarını aşmak için NAT geçişini ve son çare olarak şifrelemeyi sürdüren DERP aktarıcılarını kullanır.



![VPN maillé (mesh)](assets/fr/02.webp)


*Şekil 2: Cihazların birbirleriyle doğrudan iletişim kurduğu kuyruk ölçekli örgü ağ*



Tüm iletişimler WireGuard ile şifrelenir. Tailscale yalnızca meta verileri (bağlantıları) görür, ancak alışverişlerin içeriğini asla görmez. Daha fazla egemenlik için Headscale, koordinasyon sunucusunun kendi kendine barındırılmasını sağlar.



**Güvenlik ve gizlilik:** WireGuard sayesinde Tailscale'deki tüm iletişimler uçtan uca şifrelenir. Tailscale trafiğinizi okuyamaz - yalnızca cihazlarınız gerekli özel anahtarlara sahiptir. Hizmet yalnızca meta verileri görür: IP adresleri, cihaz adları, bağlantı zaman damgaları ve eşler arası bağlantı günlükleri (içeriksiz).



Ancak bu mimari, ağ koordinasyonu için Tailscale Inc. şirketine bağımlıdır. Bu bağımlılığı ortadan kaldırmak için Headscale, resmi Tailscale istemcilerini kullanırken kontrol sunucusunu kendi kendinize barındırmanıza olanak tanıyan açık kaynaklı bir alternatif sunar, böylece daha teknik bir yapılandırma pahasına ağ altyapınız üzerinde tam egemenlik sağlar.



**Kontrol düzlemi yönetimi, NAT geçişi ve DERP röleleri dahil olmak üzere Tailscale'in iç işleyişinin ayrıntılı bir açıklaması için resmi blogdaki mükemmel makaleyi [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) öneririz. Bu makale, Tailscale'i bu kadar güçlü kılan teknik kavramları derinlemesine açıklamaktadır.



## 3. Tailscale'in Kurulumu



Tailscale **en yaygın** işletim sistemlerinde (Windows, macOS, Linux, iOS, Android) çalışır. Kurulumun tüm platformlarda "hızlı ve kolay" olduğu söyleniyor. Interface'a ve nasıl hesap oluşturulacağına bir göz atarak başlayalım, ardından farklı ortamlar için kurulum prosedürlerine geçelim.



### 3.1 Tailscale hesap oluşturma



Https://tailscale.com/] (https://tailscale.com/) adresine gidin ve sayfanın sağ üst köşesindeki "Get Started" (Başlayın) düğmesine tıklayın.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscale ana sayfası konsepti açıklıyor ve ücretsiz bir başlangıç sunuyor*



Tailscale'i kullanmak için öncelikle bir kimlik sağlayıcı aracılığıyla bir hesap oluşturmanız gerekir:



![Page de connexion Tailscale](assets/fr/04.webp)


*Tailscale'e bağlanmak için kimlik sağlayıcı seçimi (Google, Microsoft, GitHub, Apple, vb.)*



Giriş yaptıktan sonra, Tailscale sizden kullanım amacınız hakkında bazı bilgiler isteyecektir:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Kullanım durumunuzu daha iyi anlamak için form (kişisel veya profesyonel)*



Hesabınızı oluşturduktan sonra, Tailscale'i cihazlarınıza yükleyebilirsiniz:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale, uygulamayı farklı sistemlere yüklemenizi sağlar*



### 3.2 Farklı platformlara kurulum





- Windows ve macOS'ta:** Grafik uygulamayı resmi Tailscale web sitesinden indirin ve kurun (.msi dosyası Windows'ta, .dmg dosyası Mac'te). Uygulama yüklendikten sonra, makinenin kimliğini doğrulamak için Tailscale hesabınıza bağlanmanızı (bir tarayıcı aracılığıyla) sağlayan grafiksel bir Interface başlatır.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*MacBook'u arka ağa bağlayın*



![Connexion réussie](assets/fr/09.webp)


*Cihazın Tailscale* ağına bağlı olduğunun onaylanması





- Linux'ta (Debian, Ubuntu, vb.):** Birkaç seçeneğiniz vardır. En basit yöntem resmi kurulum betiğini çalıştırmaktır: örneğin Debian/Ubuntu'da:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Bu betik resmi Tailscale deposunu ekleyecek ve paketi yükleyecektir. Ayrıca [APT deposunu manuel olarak ekleyebilir] (https://pkgs.tailscale.com) veya normal Snap veya apt paketlerini kullanabilirsiniz. Kurulduktan sonra, daemon `tailscaled` arka planda çalışacaktır. Daha sonra **düğümün kimliğini doğrulamanız** gerekecektir (aşağıdaki Interface CLI vs web bölümüne bakın). Diğer dağıtımlarda (Fedora, Arch...), paket standart depolar veya evrensel kurulum betiği aracılığıyla da kullanılabilir. Başsız bir sunucu için CLI kullanın: örneğin, önceden oluşturulmuş bir kimlik doğrulama anahtarı kullanıyorsanız `sudo tailscale up --auth-key <key>` veya etkileşimli bir oturum açma için sadece `tailscale up` (cihazın kimliğini doğrulamak için ziyaret edilecek bir URL sağlayacaktır).





- ARM tabanlı sistemlerde (Raspberry Pi, vb.):** Genellikle Linux kullanıyoruz, bu nedenle yukarıdaki ile aynı yaklaşım (komut dosyası veya paket). Tailscale'in ARM32/ARM64 mimarisini sorunsuz bir şekilde desteklediğini unutmayın. Birçok kullanıcı Tailscale'i apt aracılığıyla Raspberry Pi OS'ye veya Pi'lerine her yerden erişmek için hafif dağıtımlara (DietPi, vb.) yükler.





- IOS ve Android'de:** Tailscale **resmi** mobil uygulamalar sağlar. App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) veya [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android) üzerinden *Tailscale* yüklemeniz yeterlidir.



![Installation sur iPhone](assets/fr/11.webp)


*Tailscale'i iPhone'a yükleme adımları: karşılama, gizlilik, bildirimler, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Tailnet'e bağlanın, hesabı seçin ve iPhone'da doğrulayın*



Uygulama yüklendikten sonra, ilk açılışta sizden seçilen sağlayıcı (Tailscale için ne kullandığınıza bağlı olarak Google, Apple ID, Microsoft, vb.) aracılığıyla kimlik doğrulaması yapmanızı isteyecektir - bu diğer platformlarda olduğu gibi aynı prosedürdür, genellikle bir OAuth web sayfasına yönlendirir. Bundan sonra, mobil uygulama VPN'i oluşturur (iOS'ta VPN yapılandırma eklentisini kabul etmeniz gerekir). Uygulama daha sonra arka planda çalışarak tailnet'inize her yerden erişmenizi sağlar. *Lütfen unutmayın:* mobil cihazlarda, aynı anda yalnızca **bir aktif VPN'e sahip olabilirsiniz** - bu nedenle aynı anda başka bir VPN'in bağlı olmadığından emin olun, aksi takdirde Tailscale kendi VPN'ini kuramaz. Android'de, belirli kullanımları izole etmek istiyorsanız ayrı bir çalışma profili oluşturabilirsiniz (örneğin, belirli bir uygulama için Tailscale'in etkin olduğu bir profil).



### 3.3 Birden fazla cihaz ekleme ve doğrulama



İlk cihazınız bağlandıktan sonra, Tailscale ağınıza başka cihazlar eklemenizi ister:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface ilk cihazın bağlandığını ve diğer cihazları beklediğini gösteriyor*



Birkaç cihaz ekledikten sonra, birbirleriyle iletişim kurup kuramadıklarını kontrol edebilirsiniz:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Cihazların ping aracılığıyla birbirleriyle iletişim kurabildiğinin teyidi*



Tailscale daha sonra deneyiminizi geliştirmek için ek yapılandırmalar önerir:



![Suggestions de configuration](assets/fr/14.webp)


*DNS kurulumu, cihaz paylaşımı ve erişim yönetimi için öneriler*



### 3.4 Yönetim panosu



Web yönetim konsolu, bağlı tüm cihazlarınızı görüntülemenizi ve yönetmenizi sağlar:



![Tableau de bord des machines](assets/fr/15.webp)


*Özellikleri ve durumlarıyla birlikte bağlı cihazların listesi*



**Interface Web vs Interface CLI:** Tailscale ağ ile etkileşim için iki tamamlayıcı yol sunar: **Interface web yönetimi** ve **komut satırı istemcisi (CLI)**.





- Interface Web (Yönetici Konsolu)**: [https://login.tailscale.com](https://login.tailscale.com) adresinden erişilebilen bu web konsolu, Tailscale ağınız için merkezi kontrol panelidir. Tüm cihazları (*Makineler*), çevrimiçi/çevrimdışı durumlarını, Tailscale IP adreslerini ve daha fazlasını listeler. Burada **cihazları yönetebilir** (yeniden adlandırabilir, anahtarların süresini uzatabilir, rotaları yetkilendirebilir, bir düğümü devre dışı bırakabilir), **kullanıcıları yönetebilir** (organizasyonel bağlamda) ve güvenlik kurallarını (ACL'ler) tanımlayabilirsiniz. Burası aynı zamanda MagicDNS, etiketler veya auth anahtarları (otomatik cihaz ekleme için generate öncesi auth anahtarları) gibi global seçenekleri yapılandırdığınız yerdir. Interface web, genel bir bakış elde etmek ve koordinasyon sunucusu aracılığıyla tüm düğümlere yayılacak değişiklikleri uygulamak için çok kullanışlıdır. *Örnek:* Bir **alt ağ rotasını** veya bir **çıkış düğümünü** etkinleştirmek, söz konusu düğüm kendini bu şekilde duyurduktan sonra konsolda tek bir tıklama ile yapılır.





- Interface komut satırı (CLI):** `tailscale` komutu, Tailscale'in kurulu olduğu her cihazda CLI'de mevcuttur. Bu CLI, yerel olarak her şeyi yapmanıza olanak tanır: bağlanma (`tailscale up`), durumu inceleme (hangi eşlerin bağlı olduğunu görmek için `tailscale status`), hata ayıklama (`tailscale ping <ip>`) vb. Hatta bazı özellikler **CLI'e özeldir** veya daha ileri düzeydedir, örneğin:





  - bir alt ağ rotasının reklamını yapmak için `tailscale up --advertise-routes=192.168.0.0/24`,
  - makinenizi bir çıkış düğümü olarak önermek için `tailscale up --advertise-exit-node`,
  - bir rotayı tüketmek veya bir çıkış düğümü kullanmak için `tailscale set --accept-routes=true` (veya `--exit-node=<IP>`),
  - cihazın Tailscale IP'sini görüntülemek için `tailscale ip -4`,
  - "kuyruk ölçeği kilitleme/kilit açma" (*tailnet-lock*, gelişmiş güvenlik özelliği kullanılıyorsa),
  - veya **Taildrop** (cihazlar arasında dosya aktarımı) kullanmak için `tailcale file send <node>`.


CLI, Interface grafikleri olmayan sunucularda ve belirli eylemleri komut dosyası haline getirmek için çok kullanışlıdır. **Kullanımdaki farklılıklar:** Çoğu temel yapılandırma ya Web üzerinden ya da CLI üzerinden yapılabilir. Örneğin, bir cihaz ekleme işlemi ya konsol üzerinden komut verilerek ya da cihaz üzerinde `tailcale up' çalıştırılarak ve web üzerinden doğrulama yapılarak gerçekleştirilir. Benzer şekilde, bir cihazın yeniden adlandırılması konsol üzerinden veya `tailscale set --hostname` ile yapılabilir. **Özetle**, web konsolu küresel ağ yönetimi için idealdir (özellikle birden fazla makine / kullanıcı ile), CLI ise belirli bir makine üzerinde ince taneli kontrol, otomasyon komut dosyaları veya GUI olmayan bir sistemde kullanım için kullanışlıdır.



## 4. Umbrel'de Tailscale Kullanımı



Umbrel popüler bir kendi kendini barındırma platformudur (özellikle App Store aracılığıyla Bitcoin/Lightning düğümleri ve diğer kendi kendini barındıran hizmetler için kullanılır). Umbrel'i kurmak ve yapılandırmak için özel öğreticimizi takip etmenizi öneririz:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Umbrel ve Tailscale'i birlikte kullanmak, Umbrel'in dağıtımı kolay bir Tailscale modülünü yerel olarak entegre etmesi nedeniyle özellikle ilginç bir kullanım örneğidir. İşte Tailscale'in Umbrel ile nasıl entegre olduğu ve neler getirdiği:



### 4.1 Şemsiye kurulumu ve yapılandırması





- Tailscale'i Umbrel'e Yükleme:** Umbrel'in App Store'da resmi bir Tailscale uygulaması vardır. Kurulum daha basit olamazdı:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Umbrel App Store'da Tailscale uygulama sayfası*



Interface Web Umbrel'den App Store'u açın, **Tailscale** uygulamasını arayın ve *Yükle* düğmesine tıklayın. Birkaç saniye sonra uygulama Umbrel'e yüklenir. Uygulamayı açtığınızda, Umbrel düğümünüzü Tailscale'e bağlamanızı sağlayan bir sayfa görüntüler.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Umbrel'in Interface'sında kuyruk ölçeği bağlantı ekranı*



Sizi Tailscale kimlik doğrulama sayfasına yönlendirecek olan **"Oturum aç "** seçeneğine tıklamanız yeterlidir:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Bir kimlik sağlayıcı aracılığıyla Tailscale'e bağlanın*



Tailscale hesabınız (Google/GitHub/vb.) üzerinden kimlik doğrulaması yapabilir veya e-postanızı girebilirsiniz. Genellikle Umbrel'de Interface sizden [https://login.tailscale.com](https://login.tailscale.com) adresini ziyaret etmenizi ve oturum açmanızı ister - bu Umbrel Tailscale uygulamasının kimliğini doğrular.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Umbrel cihazının Tailscale ağına bağlı olduğunun teyidi*



Bu işlem tamamlandığında Umbrel'iniz Tailscale ağınızda "yer alır" ve konsolunuzda bir adla görünür (örneğin *umbrel*). Daha sonra kopyalamak için cihazlarınızın IP Address'ine tıklayabilir, IPv6 Address'i veya cihazınızla ilişkili MagicDNS'inizi alabilirsiniz.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Umbrel* dahil olmak üzere çeşitli bağlı cihazları gösteren Tailscale yönetim konsolu




### 4.2 Umbrel hizmetlerine uzaktan erişim



Umbrel Tailscale'e bağlandıktan sonra, **Interface Umbrel'e ve üzerinde çalışan uygulamalara, yerel ağdaymışsınız gibi her yerden erişebilirsiniz**. Bu, Tor'a göre ana avantajlardan biridir.



Erişim son derece basittir: `umbrel.local` (yalnızca yerel ağınızda çalışır) kullanmak yerine, Umbrel'in Tailscale IP Address'sini (`http://100.x.y.z`) doğrudan tailnet'inize bağlı herhangi bir cihazdan kullanırsınız. Bu, nerede olursanız olun veya hangi internet bağlantısını kullanıyor olursanız olun (4G, halka açık Wi-Fi, kurumsal ağ) çalışır.



**Tailscale aracılığıyla erişilebilen Umbrel tarafından barındırılan uygulama örnekleri:**





- Interface ana Umbrel**: Tarayıcınızda `http://100.x.y.z` yazarak Umbrel kontrol panelinize erişin
- Bitcoin düğümü**: Bitcoin düğümünüzü gecikme olmadan yönetin, senkronizasyonu ve istatistikleri görüntüleyin
- Lightning Node**: Anında yanıt veren ThunderHub, RTL veya diğer Lightning yönetim arayüzlerini kullanın
- Mempool**: Tor gecikmeleri olmadan Bitcoin işlemlerini ve Mempool'ü görüntüleyin
- noStrudel**: Umbrel üzerinde barındırılan Nostr hizmetlerinize erişin



**Harici cüzdanları Tailscale aracılığıyla Bitcoin veya lightning düğümlerinize bağlayın:**



Tailscale ayrıca diğer cihazlarda yüklü Bitcoin ve Lightning cüzdanlarınızın doğrudan Umbrel düğümünüze bağlanmasını sağlar:





- Sparrow wallet (Bitcoin)**: Bu harici Wallet Bitcoin, Tailscale IP Address'i kullanarak doğrudan Umbrel'in Electrum sunucusuna bağlanabilir:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Umbrel'in Tailscale IP Address*'sini kullanarak Sparrow wallet'de özel bir Electrum sunucusu yapılandırma



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Umbrel Tailscale IP Address* ile Sparrow'teki Electrum sunucu takma adlarının listesi



Sparrow wallet'i Bitcoin düğümünüzle yapılandırmaya yönelik eksiksiz kılavuzumuzu okuyun:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Yıldırım)**: Bu Wallet mobil Lightning, Umbrel üzerindeki Lightning düğümünüze bağlanabilir. Uç noktayı `.onion' olarak yapılandırmak yerine, Umbrel'inizin Tailscale IP'sini ve Lightning API bağlantı noktasını ayarlamanız yeterlidir. Bağlantı Tor'a kıyasla anlık olacaktır.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Zeus'un Lightning düğümüne Tailscale* IP Address üzerinden bağlanması için yapılandırılması



Zeus'u Lightning düğümünüzle yapılandırmak için ayrıntılı öğreticimize bakın:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Lightning Network ve Umbrel'de nasıl çalıştığı hakkında daha fazla bilgi edinmek için şu adresi ziyaret edin:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Tor'a göre avantajları



Umbrel yerel olarak Tor üzerinden uzaktan erişim sunar (web hizmetleri için `.onion` adresleri sağlayarak). Tor gizlilik (anonimlik) avantajına sahip olsa ve kayıt gerektirmese de, birçok kullanıcı günlük kullanım için **Tor'u yavaş ve kararsız** buluyor (sayfalar yavaş yükleniyor, zaman aşımları, vb.) - *"Tor üzerinden Umbrel çok yavaş "* bazıları şikayet ediyor.



Tailscale, trafik 3 Tor düğümünden geçmek yerine doğrudan (veya hızlı bir aktarıcı aracılığıyla) geçtiği için genellikle **daha hızlı, düşük gecikmeli** bir bağlantı sunar. Dahası, Tailscale bir "yerel ağ" deneyimi sağlar: özel IP'ler kullanılır ve uygulamalar doğrudan eşlenebilir (örneğin, \100.x.y.z üzerindeki SMB ağ sürücüsü).



Bununla birlikte, Tor, Umbrel'de merkezi olmayan ve "kutudan çıktığı gibi" olma avantajına sahipken, Tailscale üçüncü bir tarafa güvenmeyi (veya headcale'i barındırmayı) gerektirir. Tor ayrıca istemcisiz erişim için de kullanışlıdır (herhangi bir Tor tarayıcısından Umbrel kullanıcı arayüzüne başvurabilirsiniz, oysa Tailscale istemcinin erişim cihazında yüklü olmasını gerektirir).



**Özetle**, interaktif kullanım için (Lightning cüzdanları, sık kullanılan web arayüzleri) Tailscale, hafif bir dışa bağımlılık pahasına Tor ile karşılaştırıldığında kayda değer bir konfor ve hız sunar. Birçok kişi *her ikisini de* kullanmayı tercih ediyor: Günlük olarak Tailscale ve yedek olarak Tor ya da VPN'lerine davet etmeden biriyle erişimi paylaşmak için.



### 4.4 Güvenlik



Umbrel ile Tailscale kullanarak Umbrel'i internete maruz bırakmaktan kaçınırsınız. Umbrel düğümüne yalnızca tailnet'teki kimliği doğrulanmış diğer cihazlarınız erişebilir ve bu da saldırı yüzeyini önemli ölçüde azaltır (yabancılara açık bağlantı noktası yoktur, web hizmetine İnternet üzerinden saldırı riski yoktur).



İletişimler, hizmetlerinizin zaten yapmakta olduğu şifrelemeye ek olarak şifrelenir (WireGuard) (örneğin dahili HTTP bile tünelde). Ağı bölümlere ayırmak istiyorsanız, örneğin belirli bir tailnet cihazının Umbrel'e erişmesini engellemek için yine de Tailscale ACL'leri uygulayabilirsiniz. Umbrel'in kendisi farkı görmez - yerel hizmet verdiğini düşünür.



---

Bu bölümü sonlandırmak için, Tailscale'i Umbrel'e entegre etmek sadece birkaç tıklama alır ve kendi kendine barındırılan düğümünüzün erişilebilirliğini **büyük ölçüde geliştirir. Umbrel'i ve hizmetlerini her yerden, güvenli ve verimli bir şekilde, tıpkı evinizdeymiş gibi yönetebileceksiniz. Bu, Tor gecikmesinden muzdarip gerçek zamanlı uygulamalar (Lightning) için veya daha genel olarak basit bir özel bağlantı arayan herhangi bir kendi kendine ev sahibi için özellikle yararlı bir çözümdür. Tüm bunlar, kutunuzdaki tek bir bağlantı noktasını** açığa çıkarmadan ve karmaşık ağ yapılandırması olmadan gerçekleşir.



## 5. Gelişmiş yönetim ve kullanım durumları



### 5.1 Tailscale gelişmiş özellikleri



**Ağ yönetimi:** Yönetim konsolu (login.tailscale.com) cihazlarınızı yönetmenizi, bağlantıları görüntülemenizi ve erişim kurallarını yapılandırmanızı sağlar.



**MagicDNS:** IP adreslerini ezberlemekten kaçınmak için cihaz adlarını (örneğin `raspberrypi.tailnet.ts.net`) otomatik olarak çözer.



**ACL ve erişim kontrolü:** Belirli cihazları izole etmek veya belirli hizmetlere erişimi kısıtlamak için ideal olan JSON kuralları aracılığıyla ağınızda kimin neye erişebileceğini tam olarak tanımlayın.



**Aygıt Paylaşımı, birine tüm ağınıza erişim izni vermeden belirli bir makineye erişmesi için davet etmenize olanak tanır.



**Alt Ağ Yönlendiricisi:** Bir Tailscale makinesi, tüm bir alt ağ için ağ geçidi görevi görebilir ve yapılandırılmış tek bir makine aracılığıyla Tailscale dışı cihazlara (IoT, yazıcılar vb.) erişim sağlar.



**Çıkış Düğümü:** IP'si ile çıkmak için bir makineyi İnternet ağ geçidi olarak kullanın. Halka açık Wi-Fi için veya coğrafi kısıtlamaları atlamak için kullanışlıdır.



**Taildrop:** AirDrop'a güvenli bir alternatiftir ve platformları veya konumları ne olursa olsun Tailscale cihazlarınız arasında dosya aktarmanıza olanak tanır. Apple ekosistemi ve fiziksel yakınlıkla sınırlı olan AirDrop'un aksine Taildrop, farklı ülkelerde olsalar bile tüm cihazlarınız (Windows, Mac, Linux, Android, iOS) arasında çalışır. Dosyalar, merkezi bir sunucudan geçmeden, uçtan uca şifreleme ile doğrudan cihazlar arasında aktarılır. Sisteminize bağlı olarak komut satırı `tailcale file cp` veya grafiksel Interface uygulamasını kullanın.



### 5.2 Diğer çözümlerle karşılaştırma



**Vs OpenVPN:** Tailscale'in yapılandırılması çok daha basittir (açılacak port yok, sertifika yönetimi yok) ancak üçüncü taraf bir hizmete bağımlılık içerir. OpenVPN tamamen kontrol edilebilir, ancak daha fazla uzmanlık gerektirir.



**Doğrudan bir rakip olarak ZeroTier, Layer 2'de (Ethernet) çalışarak yayın/çok noktaya yayın sağlarken Tailscale, Layer 3'te (IP) çalışır. ZeroTier daha fazla ağ esnekliği sunarken, Tailscale kullanım kolaylığını tercih eder.



**Vs Tor:** Tor, Tailscale'in sunmadığı anonimliği sunar, ancak çok daha yavaştır. Tor merkezi değildir ve hesap gerektirmez, Tailscale ise daha hızlıdır ve LAN benzeri bir deneyim sunar.



**Vs WireGuard manuel:** Tailscale, WireGuard raw'ın manuel olarak işlemenizi gerektirdiği tüm anahtar ve bağlantı yönetimini otomatikleştirir. Esasen WireGuard + basitleştirilmiş bir yönetim Layer'dir.



Sonuç olarak, Tailscale kendisini kişisel kullanım ve küçük ekipler için ideal olan modern, basitlik odaklı bir çözüm olarak konumlandırıyor. Tam kontrol isteyenler için Headscale kendi kendini barındıran bir alternatif sunuyor.



## 6. Sonuç



**Tailscale avantajları:** Tailscale, kendi kendine barındırma için çeşitli avantajlar sunar:





- Basitlik ve performans** - Karmaşık ağ yapılandırması olmadan tüm platformlarda hızlı kurulum. Trafik, WireGuard protokolünün performansı ile makineleriniz arasındaki en doğrudan yolu (P2P mesh) izler ve verimi sınırlayacak merkezi bir sunucu yoktur.
- Güvenlik ve esneklik** - Uçtan uca şifreleme, azaltılmış saldırı yüzeyi ve gelişmiş özellikler (ACL, SSO/MFA kimlik doğrulama). Ağı ihtiyaçlarınıza göre uyarlamak için alt ağ yönlendiricileri ve çıkış düğümleri ile NAT'ların arkasında veya hareket halindeyken bile çalışır.



**Sınırlar:** Ayrıca aklınızda bulundurun:





- Dış bağımlılık** - Standart sürümünde, hizmet Tailscale Inc. altyapısına dayanır. Bu bağımlılık Headscale (kendi kendine barındırma alternatifi) aracılığıyla atlanabilir.
- Diğer kısıtlamalar** - Kısmen kapalı kaynak kodu, belirli gelişmiş kullanımlar için ücretsiz sürümün sınırlamaları, Layer 2 (yayın/multicast) için destek olmaması ve bağlantı kurmak için İnternet erişimine ihtiyaç duyulması.



**Tailscale, bireysel kendi kendini barındıranlar ve küçük ekipler, dağınık kaynaklara erişime ihtiyaç duyan geliştiriciler, VPN'e yeni başlayanlar ve mobil kullanıcılar için idealdir. Tam kontrol gerektiren şirketler için doğrudan Headscale veya WireGuard gibi diğer çözümler tercih edilebilir.



**Tam kendi kendine barındırma, API ve DevOps entegrasyonları (Terraform) için Headscale'i veya Innernet (benzer ancak tamamen kendi kendine barındırılan) ve Netmaker gibi alternatifleri keşfedin.



Tailscale, basitliği ve verimliliği sayesinde kendi kendini barındırma için önemli bir araçtır ve kontrolü evde tutarken özel altyapınızı buluttaymış gibi erişilebilir hale getirir.



## 7. Yararlı kaynaklar



### Resmi belgeler





- Tailscale Dokümantasyon Merkezi**: [docs.tailscale.com](https://docs.tailscale.com) - Tam İngilizce belgeler, kurulum kılavuzları, öğreticiler ve teknik referanslar.
- Tailscale nasıl çalışır**: [Tailscale Nasıl Çalışır](https://tailscale.com/blog/how-tailscale-works) - Tailscale'in iç işleyişini açıklayan ayrıntılı makale.
- Değişiklik Günlüğü**: [tailscale.com/changelog](https://tailscale.com/changelog) - Güncellemeleri ve yeni özellikleri takip etme.



### Pratik kılavuzlar





- Homelab** eğitimleri: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Kendi kendine barındırma için özel kılavuzlar.
- Bir Çıkış Düğümünü Yapılandırma**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Çıkış Düğümlerini yapılandırmak için ayrıntılı kılavuz.
- Taildrop** kullanın: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Tailscale cihazları arasında dosya aktarın.



### Karşılaştırmalar





- Tailscale diğer çözümlere karşı**: [tailscale.com/compare](https://tailscale.com/compare) - Diğer VPN ve ağ çözümleriyle (ZeroTier, OpenVPN, vb.) ayrıntılı karşılaştırmalar.



### Topluluk





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Tartışmalar, sorular ve geri bildirimler.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Müşteri kaynak kodu, geliştirmenin takip edileceği ve sorunların bildirileceği yer.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Kullanıcı ve geliştirici topluluğu.



Tailscale düzenli olarak yeni içerik ve özellikler sunar. En son haberler ve vaka çalışmaları için [resmi bloglarına] (https://tailscale.com/blog/) göz atın.