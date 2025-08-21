---
name: Bitwarden
description: Parola yöneticisi nasıl kurulur?
---
![cover](assets/cover.webp)


Dijital çağda, bankacılık, finansal platformlar, e-postalar, dosya depolama, sağlık, yönetim, sosyal ağlar, video oyunları vb. dahil olmak üzere günlük hayatımızın çeşitli yönlerini kapsayan çok sayıda çevrimiçi hesabı yönetmemiz gerekiyor.


Bu hesapların her birinde kimliğimizi doğrulamak için, bir parola ile birlikte bir tanımlayıcı, genellikle bir e-posta Address kullanırız. Çok sayıda benzersiz parolayı ezberlemenin imkansızlığı karşısında, aynı parolayı tekrar kullanmak veya kolayca hatırlamak için ortak bir tabanı biraz değiştirmek cazip gelebilir. Ancak bu uygulamalar hesaplarınızın güvenliğini ciddi şekilde tehlikeye atar.


Parolalar için uyulması gereken ilk ilke, onları tekrar kullanmamaktır. Her bir çevrimiçi hesap diğerlerinden tamamen farklı benzersiz bir parola ile korunmalıdır. Bu önemlidir, çünkü bir saldırgan şifrelerinizden birini ele geçirmeyi başarırsa, tüm hesaplarınıza erişmesini istemezsiniz. Her hesap için benzersiz bir parolaya sahip olmak olası saldırıları izole eder ve kapsamlarını sınırlar. Örneğin, bir video oyun platformu ve e-postanız için aynı şifreyi kullanırsanız ve bu şifre oyun platformuyla ilgili bir kimlik avı sitesi aracılığıyla ele geçirilirse, saldırgan e-postanıza kolayca erişebilir ve diğer tüm çevrimiçi hesaplarınızın kontrolünü ele geçirebilir.


İkinci temel ilke ise parolanın gücüdür. Bir parolanın kaba kuvvetle, yani deneme yanılma yoluyla tahmin edilmesi zorsa güçlü olduğu kabul edilir. Bu, şifrelerinizin mümkün olduğunca rastgele, uzun ve çeşitli karakterler (küçük harf, büyük harf, sayılar ve semboller) içermesi gerektiği anlamına gelir.


Bu iki parola güvenliği ilkesini (benzersizlik ve sağlamlık) uygulamak günlük hayatta zor olabilir, çünkü tüm hesaplarımız için benzersiz, rastgele ve güçlü bir parola ezberlemek neredeyse imkansızdır. İşte bu noktada parola yöneticisi devreye giriyor.


Parola yöneticisi güçlü parolalar oluşturup bunları güvenli bir şekilde saklayarak tüm çevrimiçi hesaplarınıza tek tek ezberlemenize gerek kalmadan erişmenizi sağlar. Yalnızca tek bir parolayı, yöneticide kayıtlı tüm parolalarınıza erişmenizi sağlayan ana parolayı hatırlamanız gerekir. Bir parola yöneticisi kullanmak çevrimiçi güvenliğinizi artırır çünkü parolaların tekrar kullanılmasını önler ve sistematik olarak rastgele parolalar oluşturur. Aynı zamanda hassas bilgilerinize erişimi merkezileştirerek hesaplarınızın günlük kullanımını kolaylaştırır.

Bu eğitimde, çevrimiçi güvenliğinizi artırmak için bir parola yöneticisinin nasıl kurulacağını ve kullanılacağını keşfedeceğiz. Size Bitwarden'ı tanıtacağım ve başka bir derste KeePass adlı başka bir çözümü inceleyeceğiz.

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Uyarı: Bir parola yöneticisi parolaları saklamak için harikadır, ancak **Bitcoin Wallet'ünüzün Mnemonic cümlesini asla içinde saklamamalısınız!** Unutmayın, bir Mnemonic cümlesi yalnızca bir kağıt parçası veya metal gibi fiziksel bir biçimde kaydedilmelidir.


## Bitwarden'a Giriş


Bitwarden hem yeni başlayanlar hem de ileri düzey kullanıcılar için uygun bir şifre yöneticisidir. Çok sayıda avantaj sunar. Her şeyden önce, Bitwarden çok platformlu bir çözümdür, yani onu bir mobil uygulama, web uygulaması, tarayıcı uzantısı ve masaüstü yazılımı olarak kullanabilirsiniz.

![BITWARDEN](assets/notext/01.webp)

Bitwarden, ana parolanızla uçtan uca şifreleme sağlarken, parolalarınızı çevrimiçi olarak kaydetmenize ve tüm cihazlarınızda senkronize etmenize olanak tanır. Bu, örneğin, şifrelerinize hem bilgisayarınızdan hem de akıllı telefonunuzdan erişmenizi ve ikisi arasında senkronizasyon yapmanızı sağlar. Parolalarınız şifrelenmiş olduğundan, ana parolanız olan şifre çözme anahtarı olmadan Bitwarden dahil hiç kimse tarafından erişilemezler.


Dahası, Bitwarden açık kaynak kodludur, yani yazılım bağımsız uzmanlar tarafından denetlenebilir. Fiyatlandırmaya gelince, Bitwarden üç plan sunuyor:


- Bu eğitimde keşfedeceğimiz ücretsiz bir sürüm. Ücretsiz olmasına rağmen, ücretli sürümlere eşdeğer bir güvenlik seviyesi sağlar. Sınırsız sayıda parola saklayabilir ve istediğiniz kadar cihazı senkronize edebilirsiniz;
- Dosya depolama, banka kartı yedekleme, fiziksel bir güvenlik anahtarı ile 2FA kurma ve doğrudan Bitwarden ile TOTP 2FA kimlik doğrulamasına erişim gibi ek özellikler içeren yıllık 10 $ 'lık premium sürüm;
- Ve premium sürümün avantajlarını altı farklı kullanıcıya genişleten yıllık 40 $ 'lık bir aile planı.

![BITWARDEN](assets/notext/02.webp)

Bence bu fiyatlar makul. Ücretsiz sürüm yeni başlayanlar için mükemmel bir seçenektir ve premium sürüm daha fazla özellik sunarken piyasadaki diğer şifre yöneticilerine kıyasla paranızın karşılığını çok iyi bir şekilde verir. Ek olarak, Bitwarden'in açık kaynaklı olması büyük bir avantaj. Bu nedenle, özellikle yeni başlayanlar için ilginç bir uzlaşmadır.

Bitwarden'in bir başka özelliği de, örneğin evinizde bir NAS varsa, parola yöneticinizi kendiniz barındırabilmenizdir. Bu yapılandırmayı kurduğunuzda, şifreleriniz Bitwarden'ın sunucularında değil, kendi sunucularınızda saklanır. Bu size parolalarınızın kullanılabilirliği üzerinde tam kontrol sağlar. Ancak, bu seçenek herhangi bir erişim kaybını önlemek için titiz bir yedekleme yönetimi gerektirir. Bu nedenle, Bitwarden'in kendi kendine barındırma özelliği ileri düzey kullanıcılar için daha uygundur ve bunu başka bir derste tartışacağız.

## Bitwarden hesabı nasıl oluşturulur?


Bitwarden web sitesini] (https://bitwarden.com/) ziyaret edin ve "*Get Started*" seçeneğine tıklayın.

![BITWARDEN](assets/notext/03.webp)

Address e-postanızın yanı sıra adınızı veya takma adınızı girerek başlayın.

![BITWARDEN](assets/notext/04.webp)

Ardından, ana parolanızı ayarlamanız gerekecektir. Giriş bölümünde gördüğümüz gibi, bu parola çok önemlidir çünkü yöneticideki diğer tüm kayıtlı parolalarınıza erişmenizi sağlar. Bu durumda iki ana risk ortaya çıkar: kayıp ve ele geçirme. Bu parolaya erişiminizi kaybederseniz, artık tüm kimlik bilgilerinize erişemezsiniz. Parolanız çalınırsa, saldırgan tüm hesaplarınıza erişebilir.


Kayıp riskini en aza indirmek için, ana parolanızın fiziksel bir yedeğini kağıt üzerinde almanızı ve güvenli bir yerde saklamanızı öneririm. Mümkünse, bu yedeği güvenli bir zarf içinde Seal'e koyarak düzenli olarak başka kimsenin erişmediğinden emin olun.


Ana parolanızın ele geçirilmesini önlemek için son derece sağlam olması gerekir. Mümkün olduğunca uzun olmalı, çok çeşitli karakterler kullanmalı ve rastgele seçilmelidir. 2024 yılında, güvenli bir parola için minimum öneriler, parolanın gerçekten rastgele olması koşuluyla, rakamlar, küçük ve büyük harflerin yanı sıra sembolleri de içeren 13 karakterdir. Bununla birlikte, daha uzun süre güvenliğini sağlamak için olası tüm karakter türlerini içeren en az 20 karakterlik bir parola seçmenizi öneririm.


Ana parolanızı özel kutuya girin ve aşağıdaki kutuda onaylayın.

![BITWARDEN](assets/notext/05.webp)

İsterseniz ana parolanız için bir ipucu ekleyebilirsiniz. Ancak, ipucu parolanızı kaybetmeniz durumunda güvenilir bir kurtarma yöntemi sağlamayacağı ve hatta parolanızı tahmin etmeye veya kaba kuvvet uygulamaya çalışan saldırganlar için yararlı olabileceği için bunu yapmamanızı tavsiye ederim. Genel bir kural olarak, ana parolanızın güvenliğini tehlikeye atabilecek herkese açık ipuçları oluşturmaktan kaçının.

![BITWARDEN](assets/notext/06.webp)

Ardından "*Bir hesap oluştur*" düğmesine tıklayın.

![BITWARDEN](assets/notext/07.webp)

Artık yeni Bitwarden hesabınıza giriş yapabilirsiniz. E-posta adresinizi girin Address.

![BITWARDEN](assets/notext/08.webp)

Ardından ana parolanızı yazın.

![BITWARDEN](assets/notext/09.webp)

Şu anda parola yöneticinizin web Interface sayfasındasınız.

![BITWARDEN](assets/notext/10.webp)

## Bitwarden nasıl kurulur?


Başlamak için, Address e-postamızı onaylayacağız. "*E-posta Gönder*" üzerine tıklayın.

![BITWARDEN](assets/notext/11.webp)

Ardından e-posta ile gelen butona tıklayın.

![BITWARDEN](assets/notext/12.webp)

Son olarak, tekrar giriş yapın.

![BITWARDEN](assets/notext/13.webp)

Her şeyden önce, parola yöneticinizin güvenliğini sağlamak için iki faktörlü kimlik doğrulama (2FA) ayarlamanızı şiddetle tavsiye ederim. Bir TOTP uygulaması veya fiziksel bir güvenlik anahtarı kullanma seçeneğiniz vardır. 2FA'yı etkinleştirdiğinizde, Bitwarden hesabınıza her giriş yaptığınızda, sizden yalnızca ana parolanız değil, aynı zamanda ikinci kimlik doğrulama faktörünüzün kanıtı da istenecektir. Bu ek bir Layer güvenlik faktörüdür ve özellikle ana parolanın kağıt yedeğinin tehlikeye girmesi durumunda faydalıdır.


Bu 2FA cihazlarını nasıl kuracağınızdan ve kullanacağınızdan emin değilseniz, bu diğer 2 öğreticiyi takip etmenizi öneririm:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Bunu yapmak için, "*Ayarlar*" menüsündeki "*Güvenlik*" sekmesine gidin.

![BITWARDEN](assets/notext/14.webp)

Ardından "*İki adımlı giriş*" sekmesine tıklayın.

![BITWARDEN](assets/notext/15.webp)

Burada tercih ettiğiniz 2FA yöntemini seçebilirsiniz. Örneğin ben "*Yönet*" butonuna tıklayarak bir TOTP uygulaması ile 2FA'yı seçeceğim.

![BITWARDEN](assets/notext/16.webp)

Ana parolanızı onaylayın.

![BITWARDEN](assets/notext/17.webp)

Ardından 2FA uygulamanız ile QR kodunu tarayın.

![BITWARDEN](assets/notext/18.webp)

2FA uygulamanızda belirtilen 6 haneli kodu girin ve ardından "*Aç*" düğmesine tıklayın. ![BITWARDEN](assets/notext/19.webp)

Hesabınızda iki faktörlü kimlik doğrulama başarıyla ayarlandı.

![BITWARDEN](assets/notext/20.webp)

Şimdi, yöneticinizde tekrar oturum açmaya çalışırsanız, önce ana parolanızı, ardından 2FA uygulamanız tarafından oluşturulan 6 haneli dinamik kodu girmeniz gerekecektir. Bu dinamik koda her zaman erişiminiz olduğundan emin olun; bu kod olmadan şifrelerinizi kurtaramazsınız.

![BITWARDEN](assets/notext/21.webp)

Ayarlarda, "*Tercihler*" sekmesinde yöneticinizi özelleştirme seçeneğiniz de vardır. Burada, yöneticinizin otomatik olarak kilitlenmesinden önceki süreyi ve Interface'un dilini ve temasını değiştirebilirsiniz.

![BITWARDEN](assets/notext/22.webp)

Bitwarden tarafından oluşturulan parolaların uzunluğunu ayarlamanızı şiddetle tavsiye ederim. Varsayılan olarak, uzunluk 14 karakter olarak ayarlanmıştır, bu da optimum güvenlik için yetersiz olabilir. Artık tüm parolalarınızı hatırlamak için bir yöneticiniz olduğuna göre, çok güçlü parolalar kullanmak için bundan yararlanabilirsiniz.


Bunun için "*Generator*" menüsüne gidin.

![BITWARDEN](assets/notext/23.webp)

Burada, parolalarınızın uzunluğunu 40'a çıkarabilir ve sembolleri dahil etmek için kutuyu işaretleyebilirsiniz.

![BITWARDEN](assets/notext/24.webp)

## Bitwarden ile hesaplarınızı nasıl güvence altına alabilirsiniz?


Artık parola yöneticiniz yapılandırıldığına göre, çevrimiçi hesaplarınızın kimlik bilgilerini saklamaya başlayabilirsiniz. Yeni bir öğe eklemek için doğrudan "*Yeni öğe*" düğmesine veya ekranın sağ üst köşesinde bulunan "*Yeni*" düğmesine ve ardından "*öğe*" düğmesine tıklayın.

![BITWARDEN](assets/notext/25.webp)

Açılan formda, kaydedilecek öğenin niteliğini belirleyerek başlayın. Oturum açma kimlik bilgilerini saklamak için açılır menüden "*Login*" seçeneğini seçin.

![BITWARDEN](assets/notext/26.webp)

"*Adı*" alanına kimlik bilgileriniz için açıklayıcı bir ad girin. Bu, özellikle çok sayıda parolanız varsa, parolalarınızı aramanızı ve düzenlemenizi kolaylaştıracaktır. Örneğin, PlanB Network sitesi için kimlik bilgilerinizi kaydetmek istiyorsanız, bu öğeyi gelecekteki aramalarınız sırasında hemen tanınmasını sağlayacak şekilde adlandırabilirsiniz.

![BITWARDEN](assets/notext/27.webp)

"*Klasör*" seçeneği, kimlik bilgilerinizi klasörler halinde sınıflandırmanıza olanak tanır. Şimdilik herhangi bir klasör oluşturmadık, ancak bunu nasıl yapacağınızı daha sonra göstereceğim.

![BITWARDEN](assets/notext/28.webp)

"*Kullanıcı adı*" alanına, genellikle e-posta adresiniz olan kullanıcı adınızı girin Address. ![BITWARDEN](assets/notext/29.webp)

Ardından, "*Password*" alanına şifrenizi girebilirsiniz. Ancak, Bitwarden generate'nin sizin için uzun, rastgele ve benzersiz bir parola oluşturmasına izin vermenizi şiddetle tavsiye ederim. Bu, güçlü bir parolaya sahip olmanızı sağlar. Bu özelliği kullanmak için, doldurulacak alanın üzerindeki çift ok simgesine tıklayın.

![BITWARDEN](assets/notext/30.webp)

Parolanızın oluşturulduğunu görebilirsiniz.

![BITWARDEN](assets/notext/31.webp)

"*URI 1*" alanına web sitesinin alan adını girebilirsiniz.

![BITWARDEN](assets/notext/32.webp)

Ve son olarak, "*Notlar*" alanında, gerekirse ek ayrıntılar ekleyebilirsiniz.

![BITWARDEN](assets/notext/33.webp)

Tüm bu alanları doldurmayı bitirdiğinizde "*Kaydet*" düğmesine tıklayın.

![BITWARDEN](assets/notext/34.webp)

Tanımlayıcınız artık Bitwarden yöneticinizde görünür.

![BITWARDEN](assets/notext/35.webp)

Üzerine tıklayarak ayrıntılarına erişebilir ve bunları değiştirebilirsiniz.

![BITWARDEN](assets/notext/36.webp)

Sağ taraftaki üç küçük noktaya tıklayarak şifreyi veya tanımlayıcıyı kopyalamak için hızlı erişim sağlayabilirsiniz.

![BITWARDEN](assets/notext/37.webp)

Tebrikler, ilk parolanızı yöneticinize başarıyla kaydettiniz! Tanımlayıcılarınızı daha iyi organize etmek istiyorsanız, belirli klasörler oluşturabilirsiniz. Bunu yapmak için, ekranın sağ üst köşesinde bulunan "*Yeni*" düğmesine tıklayın ve ardından "*Klasör*"ü seçin.

![BITWARDEN](assets/notext/38.webp)

Klasörünüz için bir ad girin.

![BITWARDEN](assets/notext/39.webp)

Ardından "*Kaydet*" üzerine tıklayın.

![BITWARDEN](assets/notext/40.webp)

Klasörünüz artık yöneticinizde görünür.

![BITWARDEN](assets/notext/41.webp)

Daha önce yaptığımız gibi, bir tanımlayıcıyı oluştururken veya mevcut bir tanımlayıcıyı değiştirerek ona bir klasör atayabilirsiniz. Örneğin, PlanB Network için tanımlayıcıma tıklayarak, onu "*Bitcoin*" klasöründe sınıflandırmayı seçebilirim.

![BITWARDEN](assets/notext/42.webp)

Bu şekilde, tanımlayıcılarınızı bulmayı kolaylaştırmak için parola yöneticinizi yapılandırabilirsiniz. Bunları kişisel, profesyonel, bankalar, e-postalar, sosyal ağlar, abonelikler, alışveriş, yönetim, akış, depolama, seyahat, sağlık vb. gibi klasörlerle düzenleyebilirsiniz.

Bitwarden'in yalnızca web sürümünü kullanmayı tercih ediyorsanız, bununla devam etmeniz tamamen mümkündür. O zaman kolay erişim ve kimlik avı risklerinden kaçınmak için parola yöneticinizi tarayıcınızın sık kullanılanlarına eklemenizi öneririm. Bununla birlikte Bitwarden, yöneticinizi çeşitli cihazlarda kullanmanıza ve günlük kullanımını basitleştirmenize olanak tanıyan eksiksiz bir istemci yelpazesi de sunar. Özellikle bir mobil uygulama, bir tarayıcı uzantısı ve masaüstü yazılımı sunuyorlar. Şimdi bunları birlikte nasıl kuracağımızı görelim.


![BITWARDEN](assets/notext/43.webp)


## Bitwarden tarayıcı uzantısı nasıl kullanılır?


İlk olarak, dilerseniz tarayıcı uzantısını kurabilirsiniz. Bu uzantı, yöneticinizin küçültülmüş bir sürümü olarak çalışır ve size yeni parolaları otomatik olarak kaydetme, güvenli parolalar için generate önerileri ve web sitesi giriş sayfalarında kimlik bilgilerinizi otomatik olarak doldurma olanağı sunar.


Bu uzantının günlük kullanımı son derece kullanışlıdır, ancak aynı zamanda yeni saldırı vektörleri de açabilir. Bu nedenle bazı siber güvenlik uzmanları, parola yöneticileri için tarayıcı uzantılarının kullanılmamasını tavsiye ediyor. Bununla birlikte, Bitwarden uzantısını kullanmayı seçerseniz, işte nasıl ilerleyeceğiniz:


Resmi Bitwarden indirme sayfasına] (https://bitwarden.com/download/#downloads-web-browser) giderek başlayın.


![BITWARDEN](assets/notext/44.webp)


Sağlanan listeden tarayıcınızı seçin. Bu örnekte Firefox kullanıyorum, bu yüzden Firefox Eklenti Mağazası'ndaki resmi Bitwarden uzantısına yönlendirildim. Prosedür diğer tarayıcılar için de oldukça benzer.


![BITWARDEN](assets/notext/45.webp)


"*Firefox'a ekle*" düğmesine tıklayın.


![BITWARDEN](assets/notext/46.webp)


Daha sonra kolay erişim için Bitwarden'i uzantı çubuğunuza ekleyebilirsiniz. Giriş yapmak için uzantıya tıklayın.


![BITWARDEN](assets/notext/47.webp)


E-posta adresinizi girin Address.


![BITWARDEN](assets/notext/48.webp)


Sonra ana şifreniz.


![BITWARDEN](assets/notext/49.webp)


Ve son olarak, kimlik doğrulama uygulamanızdaki 6 haneli kodu girin.


![BITWARDEN](assets/notext/50.webp)


Artık tarayıcı uzantısı aracılığıyla Bitwarden yöneticinize bağlısınız.


![BITWARDEN](assets/notext/51.webp)


Örneğin, PlanB Network sitesine geri dönüp hesabıma giriş yapmaya çalışırsam, tarayıcıya entegre Bitwarden uzantısının giriş alanlarını tanıdığını ve daha önce kaydettiğim tanımlayıcıyı seçmemi otomatik olarak sunduğunu görebilirsiniz.


![BITWARDEN](assets/notext/52.webp)

Bu tanımlayıcıyı seçersem, Bitwarden giriş alanlarını benim için doldurur. Uzantının bu özelliği, Bitwarden web uygulamasından veya yazılımından kimlik bilgilerini kopyalayıp yapıştırmaya gerek kalmadan web sitelerine hızlı bağlantı sağlar.

![BITWARDEN](assets/notext/53.webp)

Uzantı ayrıca yeni hesapların oluşturulmasını tespit etmek için tasarlanmıştır. Örneğin, PlanB Network'te yeni bir hesap oluştururken, Bitwarden otomatik olarak yeni tanımlayıcıyı kaydetmeyi önerir.

![BITWARDEN](assets/notext/54.webp)

Görünen bu öneriye tıkladığımda uzantı açılıyor. Yeni tanımlayıcının ayrıntılarını girmeme ve generate'ya güçlü, benzersiz bir parola girmeme izin veriyor.

![BITWARDEN](assets/notext/55.webp)

Bilgileri tamamladıktan ve "*Kaydet*" düğmesine tıkladıktan sonra, uzantı kimlik bilgilerini kaydeder.

![BITWARDEN](assets/notext/56.webp)

Ardından, uzantı kimlik bilgilerimizi web sitesindeki uygun alanlara otomatik olarak doldurur.

![BITWARDEN](assets/notext/57.webp)

## Bitwarden yazılımı nasıl kullanılır?


Bitwarden masaüstü yazılımını yüklemek için [indirme sayfasına] (https://bitwarden.com/download/#downloads-desktop) giderek başlayın. İşletim sisteminize karşılık gelen sürümü seçin ve indirin.

![BITWARDEN](assets/notext/58.webp)

İndirme işlemi tamamlandıktan sonra, bilgisayarınıza yazılım yüklemeye devam edin. Bitwarden yazılımının ilk açılışında, parola yöneticinizin kilidini açmak için kimlik bilgilerinizi girmeniz gerekecektir.

![BITWARDEN](assets/notext/59.webp)

Ardından, yöneticinizin ana sayfasına ulaşacaksınız. Interface, web uygulamasındaki ile neredeyse aynıdır.

![BITWARDEN](assets/notext/60.webp)

## Bitwarden uygulaması nasıl kullanılır?


Şifrelerinize telefonunuzdan erişmek için Bitwarden mobil uygulamasını yükleyebilirsiniz. İndirme sayfasına] (https://bitwarden.com/download/#downloads-mobile) giderek başlayın ve işletim sisteminize karşılık gelen QR kodunu taramak için akıllı telefonunuzu kullanın.

![BITWARDEN](assets/notext/61.webp)

Resmi Bitwarden mobil uygulamasını indirin ve yükleyin. Uygulamanın ilk açılışında, şifre yöneticinize erişimin kilidini açmak için kimlik bilgilerinizi girin.

![BITWARDEN](assets/notext/62.webp)

Bağlandıktan sonra, tüm şifrelerinize doğrudan uygulama üzerinden danışabilecek ve yönetebileceksiniz.

![BITWARDEN](assets/notext/63.webp)

Uygulamanızın güvenliğini artırmak için, ayarlara girmenizi ve PIN korumasını etkinleştirmenizi tavsiye ederim. Bu, telefonunuzun kaybolması veya çalınması durumunda ekstra bir Layer güvenlik ekleyecektir.

![BITWARDEN](assets/notext/64.webp)

## Bitwarden nasıl yedeklenir?

Ana şifrenizi kaybetmeniz veya Bitwarden sunucularını etkileyen bir felaket durumunda bile şifrelerinize erişimi asla kaybetmemenizi sağlamak için, yöneticinizin harici bir ortamda düzenli olarak şifrelenmiş bir yedeğini almanızı tavsiye ederim.


Buradaki fikir, tüm Bitwarden kimlik bilgilerinizi ana parolanızdan farklı bir parola ile şifrelemek ve bu şifreli yedeği örneğin evinizde sakladığınız bir USB belleğe veya bir Hard sürücüsüne kaydetmektir. Daha sonra şifre çözme parolasının fiziksel bir kopyasını yedekleme ortamının depolandığı yerden ayrı bir yerde tutabilirsiniz. Örneğin, USB belleği evde tutabilir ve şifreleme parolasının fiziksel kopyasını güvendiğiniz bir arkadaşınıza emanet edebilirsiniz.


Bu yöntem, yedekleme ortamınız çalınsa bile, şifre çözme parolası olmadan verilerinize erişilememesini sağlar. Benzer şekilde, arkadaşınız da fiziksel ortama sahip olmadan verilerinize erişemeyecektir.


Ancak, bir sorun olması durumunda, Bitwarden'dan bağımsız olarak kimlik bilgilerinize yeniden erişmek için şifreyi ve harici ortamı kullanabilirsiniz. Böylece, Bitwarden'in sunucuları yok edilse bile, şifrelerinizi geri alma olanağına sahip olursunuz.


Bu nedenle, her zaman en son kimlik bilgilerinizi içerecek şekilde bu yedeklemeleri düzenli olarak yapmanızı tavsiye ederim. Şifreleme parolasının bir kopyasına sahip olan arkadaşınızı her yeni yedeklemede rahatsız etmemek için bu parolayı parola yöneticinize kaydedebilirsiniz. Arkadaşınız zaten fiziksel bir kopyaya sahip olduğundan, bu bir yedekleme olarak değil, daha ziyade gelecekteki dışa aktarma prosedürlerinizi basitleştirmek için tasarlanmıştır.


Dışa aktarma işlemine devam etmek için oldukça basit: Bitwarden yöneticinizin "*Araçlar*" bölümüne gidin, ardından "*Kasayı dışa aktar*" seçeneğini seçin.

![BITWARDEN](assets/notext/65.webp)

Biçim için "*.json (Şifreli)*" öğesini seçin.

![BITWARDEN](assets/notext/66.webp)

Ardından "*Şifre korumalı*" seçeneğini seçin.

![BITWARDEN](assets/notext/67.webp)

Burada, yedeği şifrelemek için güçlü, benzersiz ve rastgele oluşturulmuş bir parola seçmek önemlidir. Bu, şifrelenmiş yedeğinizin çalınması durumunda bile, bir saldırganın kaba kuvvetle şifresini çözmesinin imkansız olmasını sağlar.

![BITWARDEN](assets/notext/68.webp)

"*Biçimi onayla*" seçeneğine tıklayın ve dışa aktarma işlemine devam etmek için ana parolanızı girin.

![BITWARDEN](assets/notext/69.webp)

Dışa aktarma işlemi tamamlandığında, şifrelenmiş yedekleme dosyanızı indirilenler bölümünde bulabilirsiniz. USB bellek veya Hard sürücüsü gibi güvenli bir harici depolama aygıtına aktarın. Kullanımınıza bağlı olarak bu işlemi periyodik olarak tekrarlayın. Örneğin, ihtiyaçlarınıza göre yedeklemeyi her hafta veya her ay yenileyebilirsiniz.