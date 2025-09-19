---
name: Tor Browser
description: Tor Browser nasıl kullanılır?
---
![cover](assets/cover.webp)


Adından da anlaşılacağı gibi tarayıcı, internette gezinmek için kullanılan bir yazılımdır. Kullanıcının makinesi ile web arasında bir geçit görevi görür ve web sitelerinin kodlarını etkileşimli ve okunabilir sayfalara çevirir. Tarayıcınızın seçimi çok önemlidir, çünkü yalnızca tarama deneyiminizi değil, aynı zamanda çevrimiçi güvenliğinizi ve gizliliğinizi de etkiler.


Tarayıcı ile arama motorunu karıştırmamaya dikkat edin. Tarayıcı, İnternet'e erişmek için kullandığınız yazılımdır (Chrome veya Firefox gibi), arama motoru ise örneğin Google veya Bing gibi çevrimiçi bilgi bulmanıza yardımcı olan bir hizmettir.


Günümüzde Google Chrome açık ara en çok kullanılan tarayıcıdır. 2024'te küresel pazarın yaklaşık %65'ini oluşturuyor. Chrome hızı ve performansıyla beğeni toplasa da, özellikle gizlilik sizin için bir öncelikse, herkes için en iyi seçenek olmayabilir. Chrome, kullanıcıları hakkında büyük miktarda veri toplaması ve analiz etmesiyle bilinen bir şirket olan Google'a aittir. Ve gerçekten de, şirket içi tarayıcıları gözetim stratejilerinin merkezinde yer alıyor. Bu yazılım, çevrimiçi etkileşimlerinizin çoğunda merkezi bir bileşendir. Tarayıcınızda veri toplama konusunda uzmanlaşmak Google için önemli bir konudur.

![TOR BROWSER](assets/notext/01.webp)

*Kaynak: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


Her biri belirli bir işleme motoruna dayanan birkaç büyük tarayıcı ailesi vardır. Google Chrome, Microsoft Edge, Brave, Opera veya Vivaldi gibi tarayıcıların tümü, Google tarafından geliştirilen Chrome'un hafif ve açık kaynaklı bir sürümü olan Chromium tarayıcısı üzerine kurulmuştur. Tüm bu tarayıcılar, kendisi de KHTML'den türetilmiş olan WebKit'in bir Fork'ı olan Blink işleme motorunu kullanmaktadır. Chromium'un piyasadaki baskınlığı, web geliştiricileri sitelerini öncelikle Blink için optimize etme eğiliminde olduklarından, ondan türetilen tarayıcıları özellikle verimli kılmaktadır.


Apple'ın tarayıcısı Safari, yine KHTML'den gelen WebKit'i kullanıyor.


Öte yandan, Mozilla Firefox, LibreWolf ve Tor Browser gibi tarayıcılar, aslen Netscape tarayıcısından farklı bir işleme motoru olan Gecko'yu kullanır.


Doğru tarayıcıyı seçmek ihtiyaçlarınıza bağlıdır. Ancak en azından gizliliğiniz ve dolayısıyla güvenliğiniz konusunda endişeleriniz varsa, genel kullanım için Firefox'u ve daha fazla gizlilik için Tor Browser'ı tercih etmenizi öneririm. Bu eğitimde size Tor Browser'ı nasıl kolayca kullanmaya başlayacağınızı göstereceğim.

![TOR BROWSER](assets/notext/02.webp)


## Tor Browser'a Giriş


Tor Browser, güvenli ve mümkün olduğunca gizli İnternet navigasyonu için özel olarak tasarlanmış bir tarayıcıdır. Tarayıcı Firefox'a ve dolayısıyla Gecko işleme motoruna dayanmaktadır.

Tor Browser, trafiğinizi şifrelemek ve hedefe iletmeden önce birden fazla aktarıcı sunucu üzerinden yönlendirmek için Tor ağını kullanır. "*onion routing*" olarak bilinen bu çok katmanlı yönlendirme işlemi, gerçek IP Address'inizin gizlenmesine yardımcı olarak konumunuzun ve çevrimiçi faaliyetlerinizin belirlenmesini zorlaştırır. Ancak, dolaylı olduğu için Tor ağını kullanmayan standart bir tarayıcıya göre internette gezinmek daha yavaş olacaktır.

Diğer tarayıcılardan farklı olarak Tor Browser, ziyaret edilen her web sitesini izole etmek ve kapanışta çerezleri ve geçmişi otomatik olarak silmek gibi çevrimiçi faaliyetlerinizin izlenmesini önlemek için belirli özellikleri entegre eder. Ayrıca, tüm kullanıcıların ziyaret edilen sitelere mümkün olduğunca benzer görünmesini sağlayarak parmak izi risklerini en aza indirecek şekilde tasarlanmıştır.


Tor Browser'ı standart bir web sitesine (`.com`, `.org`, vb.) erişmek için pekala kullanabilirsiniz. Bu durumda, trafiğiniz, clearnet üzerindeki son siteyle iletişim kuran bir çıkış düğümüne ulaşmadan önce birkaç Tor düğümünden geçerek anonimleştirilir.

![TOR BROWSER](assets/notext/03.webp)

Tor Browser'ı gizli hizmetlere (`.onion` ile biten adresler) erişmek için de kullanabilirsiniz. Bu senaryoda, tüm trafik bir çıkış düğümü olmadan Tor ağı içinde kalır ve hem kullanıcı hem de hedef sunucu için tam gizlilik sağlar. Bu çalışma şekli özellikle "*dark web*" olarak adlandırılan, İnternet'in geleneksel arama motorları tarafından indekslenmeyen bir bölümüne erişmek için kullanılır.

![TOR BROWSER](assets/notext/04.webp)


## Tor ağı ile Tor tarayıcısı arasındaki fark nedir?


Tor ağı ve Tor tarayıcısı birbirine karıştırılmaması gereken iki farklı şeydir, ancak birbirlerini tamamlarlar. Tor ağı, kullanıcılar tarafından işletilen ve İnternet trafiğini nihai hedefine yönlendirmeden önce birkaç düğümden geçirerek anonimleştiren küresel bir aktarıcı sunucu altyapısıdır. Bu ünlü soğan yönlendirmesidir.


Tor tarayıcısı ise bu ağa erişimi basit bir şekilde kolaylaştırmak için tasarlanmış özel bir tarayıcıdır. Tor ağına bağlanmak için gerekli tüm ayarları varsayılan olarak entegre eder ve gizlilik ve güvenliği en üst düzeye çıkarırken tanıdık bir tarama deneyimi sağlamak için Firefox'un değiştirilmiş bir sürümünü kullanır.


Tor ağı sadece Tor tarayıcısı tarafından kullanılmaz. İletişimlerini güvence altına almak için çeşitli yazılım ve uygulamalar tarafından kullanılabilir. Örneğin, Address IP'nizi diğer kullanıcılardan gizlemek ve Bitcoin ile ilgili trafiğinizin internet servis sağlayıcınız tarafından izlenmesini önlemek için Bitcoin düğümünüzde Tor ağı üzerinden iletişimi etkinleştirmek mümkündür.

Özetlemek gerekirse, Tor ağı internet gezintilerimizde gizliliği sağlayan altyapı, Tor Browser ise bu ağı web gezintilerimizin bir parçası olarak kullanmamızı sağlayan yazılımdır.


## Tor Browser nasıl kurulur?


Tor Browser bilgisayarlarda Windows, Linux ve macOS için, akıllı telefonlarda ise Android için kullanılabilir. Tor Browser'ı bilgisayarınıza yüklemek için [resmi Tor Projesi web sitesini] (https://www.torproject.org/) ziyaret edin.

![TOR BROWSER](assets/notext/05.webp)

"*Tor Browser'ı İndir*" düğmesine tıklayın.

![TOR BROWSER](assets/notext/06.webp)

İşletim sisteminize uygun sürümü seçin.

![TOR BROWSER](assets/notext/07.webp)

Kurulumu başlatmak için yürütülebilir dosyaya tıklayın, ardından dilinizi seçin.

![TOR BROWSER](assets/notext/08.webp)

Yazılımın yükleneceği klasörü seçin ve ardından "*Yükle*" düğmesine tıklayın.

![TOR BROWSER](assets/notext/09.webp)

Kurulumun tamamlanmasını bekleyin.

![TOR BROWSER](assets/notext/10.webp)

Son olarak, "*Bitir*" düğmesine tıklayın.

![TOR BROWSER](assets/notext/11.webp)


## Tor Browser nasıl kullanılır?


Tor Browser standart bir tarayıcı gibi kullanılır.

![TOR BROWSER](assets/notext/12.webp)

İlk açılışta, tarayıcı sizi Tor ağına bağlanmaya davet eden bir sayfa sunar. Bağlantı kurmak için "*Bağlan*" düğmesine tıklamanız yeterlidir.

![TOR BROWSER](assets/notext/13.webp)

Yazılımın gelecekteki kullanımlarınızda Tor ağına otomatik olarak bağlanmasını istiyorsanız, "*Her zaman otomatik bağlan*" seçeneğini işaretleyin.

![TOR BROWSER](assets/notext/14.webp)

Tor ağına bağlandıktan sonra ana sayfaya ulaşacaksınız.

![TOR BROWSER](assets/notext/15.webp)

İnternette bir arama yapmak için, sorgunuzu arama çubuğuna girmeniz ve "*enter*" tuşuna basmanız yeterlidir.

![TOR BROWSER](assets/notext/16.webp)

Ardından, arama motorunuzdan sonuçları diğer tarayıcılarla aynı şekilde alırsınız.

![TOR BROWSER](assets/notext/17.webp)

DuckDuckGo'daki "*Onionize*" seçeneği, arama motorunu Tor ağındaki gizli hizmeti aracılığıyla, `.onion` Address'e erişerek kullanmanıza olanak tanır.

![TOR BROWSER](assets/notext/18.webp)


## Tor Browser nasıl yapılandırılır?


Tarayıcı ekranınızın üst kısmında sık kullanılanlarınızı içe aktarma seçeneği bulacaksınız. Bu, eski tarayıcınızdaki yer imlerini otomatik olarak Tor Browser'a entegre etmenizi sağlar.

![TOR BROWSER](assets/notext/19.webp)

Ziyaret ettiğiniz web sayfasının sağ üst köşesinde bulunan yıldız simgesine tıklayarak yeni yer imleri ekleme seçeneğiniz de vardır.

![TOR BROWSER](assets/notext/20.webp)

Sağdaki menüden çeşitli seçeneklere erişebilirsiniz.

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

"*Bookmarks*" menüsü yer imlerinizi yönetmenizi sağlar.

![TOR BROWSER](assets/notext/23.webp)

"*History*", ayarlarda etkinleştirdiyseniz tarama geçmişinize erişmenizi sağlar.

![TOR BROWSER](assets/notext/24.webp)

"*Eklentiler ve temalar*" menüsü, tarayıcınızın görünümünü özelleştirmenize veya uzantılar eklemenize olanak tanır. Tor Browser Mozilla Firefox tabanlı olduğundan, Firefox için mevcut olan temaları ve uzantıları kullanabilirsiniz.

![TOR BROWSER](assets/notext/25.webp)

Son olarak, "*Ayarlar*" düğmesi tarayıcınızın ayarlarına erişmenizi sağlar.

![TOR BROWSER](assets/notext/26.webp)

Ayarların "*Genel*" sekmesinde, Tor Browser kullanıcısı Interface'i özelleştirmenize olanak tanıyan çeşitli seçenekler vardır.

![TOR BROWSER](assets/notext/27.webp)

"*Ana Sayfa*" sekmesinde, Tor Browser açılırken ve yeni sekmeler açılırken görüntülenen varsayılan sayfayı değiştirmeyi seçebilirsiniz.

![TOR BROWSER](assets/notext/28.webp)

"*Arama*" sekmesinde arama motorunu seçebilirsiniz. Tor Browser varsayılan olarak kullanıcıların gizliliğini korumaya odaklanmış bir arama motoru olan DuckDuckGo'yu kullanır, ancak örneğin Google veya Startpage'i de tercih edebilirsiniz.

![TOR BROWSER](assets/notext/29.webp)

Arama motorunuzda kısayollar da ayarlayabilirsiniz.

![TOR BROWSER](assets/notext/30.webp)

Örneğin, tarayıcının arama çubuğuna "*@wikipedia*" ve ardından "*Bitcoin*" gibi arama teriminizi yazabilirsiniz.

![TOR BROWSER](assets/notext/31.webp)

Bu özellik daha sonra teriminiz için doğrudan Wikipedia sitesinde bir arama gerçekleştirir.

![TOR BROWSER](assets/notext/32.webp)

Böylece farklı siteler için başka özel kısayollar ayarlayabilirsiniz.


Ardından, "*Gizlilik ve Güvenlik*" sekmesinde, gizlilik ve güvenlikle ilgili tüm ayarları bulacaksınız.

![TOR BROWSER](assets/notext/33.webp)

Tarama geçmişinizi saklama veya silme seçeneğiniz vardır.

![TOR BROWSER](assets/notext/34.webp)

Farklı web sitelerine verdiğiniz erişim izinlerini de yönetebilirsiniz.

![TOR BROWSER](assets/notext/35.webp)

Tarayıcınızın genel güvenliği için "*Safer*" ve "*Safest*" modları, ziyaret ettiğiniz siteler tarafından yürütülen web işlevlerini ve komut dosyalarını ayarlamanıza olanak tanır. Bu, güvenlik açıklarından yararlanma risklerini en aza indirir, ancak karşılığında sitelerin görüntüsünü ve etkileşimini de etkileyecektir. ![TOR BROWSER](assets/notext/36.webp) Tehlikeli içerik engelleyici ve sitelerle bağlantıların sürekli olarak bu protokole uymasını sağlayan yalnızca HTTPS modu dahil olmak üzere diğer güvenlik seçeneklerini bulacaksınız. ![TOR BROWSER](assets/notext/37.webp) Son olarak, "*Connection*" sekmesinde Tor ağına bağlanmakla ilgili tüm ayarları bulacaksınız. Burası, Tor'a erişimin sansürlenebileceği bölgelerden erişmek için bir köprü yapılandırabileceğiniz yerdir. ![TOR BROWSER](assets/notext/38.webp) Ve işte, artık internette daha güvenli ve daha gizli bir şekilde gezinmeye hazırsınız! Çevrimiçi gizlilik ilginizi çeken bir konuysa, Mullvad VPN hakkındaki bu diğer öğreticiyi de keşfetmenizi tavsiye ederim:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8