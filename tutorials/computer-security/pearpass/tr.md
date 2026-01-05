---
name: PearPass
description: Yerel, eşler arası, bulut içermeyen bir parola yöneticisi ile parolalarınızın kontrolünü yeniden ele geçirin
---

![cover](assets/cover.webp)



Her bireyin düzinelerce, hatta yüzlerce çevrimiçi hesabı yönettiği bir zamanda, oturum açma bilgilerinin güvenliği BT güvenliğinde merkezi bir konu haline gelmiştir. Sosyal ağlar, mesajlaşma sistemleri, profesyonel hizmetler, finansal platformlar: bu erişimlerin her biri, ele geçirilmesi hayatınız için ciddi sonuçlar doğurabilecek bir sırra dayanır.



Buna rağmen, saldırıların artmasına karşın kötü uygulamalar toplum genelinde hâlâ yaygındır: zayıf parolalar, yeniden kullanılan parolalar, düz metin olarak saklanan veya yaklaşık şekilde hatırlanan parolalar. Günlük yaşamı karmaşıklaştırmadan bu sorunları çözmek için çözüm, bir parola yöneticisi kullanmaktır.



Düzinelerce parola yöneticisi zaten mevcut ve Plan ₿ Academy bunların çoğu için bir eğitim sunuyor. Ancak bu eğitimde, çalışma şekli açısından diğerlerinden açıkça ayrılan bir tanesini tanıtmak istiyorum: **PearPass**.



**PearPass, kullanıcıya verileri üzerinde tam kontrolü yeniden kazandırmak için tasarlanmış, eşler arası, local-first ve açık kaynaklı bir parola yöneticisidir.**



![Image](assets/fr/01.webp)



## Neden PearPass'ı seçmelisiniz?



Parola yöneticisi, tüm parolalarınızı güvenli bir şekilde oluşturan, saklayan ve düzenleyen bir yazılım programıdır. Parolaları ezberlemek veya yeniden kullanmak yerine, korumanız gereken tek bir sır vardır: tüm kasanızı şifreleyen ana parola. Bu yaklaşım, her hizmet için benzersiz, uzun, rastgele parolalar kullanmayı mümkün kılarak hem unutma ve ele geçirme riskini azaltır hem de olası bir sızıntının etkisini sınırlandırır. Günümüzde herkesin kullanması gereken temel bir BT aracıdır.



İki ana şifre yöneticisi kategorisi vardır. Bir yanda, veriler asla merkezi bir sunucuda saklanmadığı için çok güvenli olan, ancak kimlik bilgilerinizi birkaç cihaz (bilgisayar, akıllı telefon, tablet...) arasında kolayca senkronize etmenize izin vermediği için çok pratik olmayan yalnızca yerel yazılımlar vardır. Öte yandan, bulut tabanlı parola yöneticileri kimlik bilgilerinizi sunucularında depolar ve tüm cihazlarınız arasında senkronize eder. Ana avantajları kolaylıktır, ancak şifreleriniz üzerinde kontrolünüz olmayan altyapılarda saklandığından güvenlikten ödün verirler.



PearPass kasıtlı olarak her iki modelden de ayrılır. Kendisini yerel yöneticiler ve bulut çözümleri arasında konumlandırır: parolalarınızın senkronizasyonunu sağlarken, asla uzak sunucularda saklanmadıklarını garanti eder. Sonuç olarak, tüm kimlik bilgileriniz cihazlarınızda yerel olarak saklanır ve birden fazla makine arasındaki senkronizasyon yalnızca eşler arasıdır. Bu mimari, merkezi veritabanlarıyla ilişkili tek hata noktalarını ortadan kaldırır: tehlikeye atılacak sunucu ve kimlik bilgilerinize erişecek üçüncü taraf altyapısı yoktur. Cihazlarınız arasındaki iletişim uçtan uca şifrelenir ve yalnızca sizin sahip olduğunuz anahtarların verilere erişmesini sağlar.



![Image](assets/fr/02.webp)



PearPass, adından da anlaşılacağı üzere bunu mümkün kılmak için sunucusuz uygulamaların oluşturulması ve yürütülmesine adanmış bir eşler arası teknoloji ekosistemi olan **Pears**'e dayanmaktadır. Pears, herhangi bir merkezi altyapı olmadan doğrudan eşler arasında senkronize olabilen, tamamen merkezi olmayan uygulamaları çalıştırmak için gereken yürütme ortamını, dağıtım mekanizmalarını ve ağ katmanlarını sağlar. PearPass durumunda, Pears cihaz keşfi, şifreli bağlantı kurma ve makineleriniz arasında şifre kasası senkronizasyonu sağlar. Bu yaklaşım, PearPass'ın işlevsel, esnek ve herhangi bir dış otoriteden bağımsız kalmasını sağlar.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Bu yenilikçi mimarinin ötesinde, PearPass tamamen açık kaynaklıdır ve tüm işlevleri ücretsizdir. Yazılım ayrıca Secfault Security tarafından bağımsız olarak denetlenmiştir. Özel mimarisine ek olarak, PearPass elbette bu eğitim boyunca keşfedeceğimiz iyi bir parola yöneticisinden beklenen tüm klasik özellikleri sunar.



Kısacası, geleneksel parola yöneticileri sizden bir şirkete ve onun sunucularına güvenmenizi isterken, PearPass egemenlik mantığını benimser: bulut yok, merkezi hesaplar yok, aracılar yok. Cihazlarınız arasında senkronizasyondan yararlanırken kimlik bilgileriniz üzerinde özel kontrole sahip olursunuz.



## PearPass'ı nasıl yüklerim?



PearPass tüm platformlarda kullanılabilir: Windows, Linux, macOS, Android, iOS ve tarayıcı uzantıları. Makinenize Pears yüklemenize gerek yoktur: PearPass kendi başına çalışır.



### Windows üzerinde kurulum



Windows üzerinde, PearPass klasik bir yükleyici olarak sağlanır. Resmi indirme sayfasına] (https://pass.pears.com/download) gidin, ardından `Windows yükleyicisini indir` düğmesine tıklayın.



Dosya indirildikten sonra, yükleyiciyi açın ve sihirbaz tarafından belirtilen adımları izleyin. Uygulamaya daha sonra `Başlat Menüsü`nden veya bir masaüstü kısayolu aracılığıyla erişilebilir.



![Image](assets/fr/03.webp)



### MacOS üzerinde kurulum



MacOS üzerinde, PearPass bir disk imajı (`.dmg`) olarak dağıtılır. Resmi indirme sayfasına] (https://pass.pears.com/download) gidin ve Mac'inizin mimarisine (Intel veya Apple Silicon) karşılık gelen sürümü seçin. İndirdikten sonra, `.dmg` dosyasını açın ve uygulamayı `Applications` klasöründen başlatın.



İlk açılışta macOS, uygulamanın İnternet'ten geldiğini belirten bir güvenlik mesajı gösterecektir: devam etmek için onaylamanız yeterlidir.



### Linux üzerinde kurulum



Linux'ta PearPass, herhangi bir özel bağımlılık olmadan çoğu dağıtımla geniş uyumluluğu garanti eden `.AppImage` formatında mevcuttur. .AppImage` dosyasını [resmi indirme sayfası](https://pass.pears.com/download) adresinden indirin, ardından çift tıklayarak doğrudan başlatın.



Ortamınıza bağlı olarak, dosyayı dosya özellikleri (sağ tıklama) veya `chmod +x` komutu ile çalıştırılabilir hale getirmeniz gerekebilir. Yetkilendirildikten sonra, PearPass tek başına bir uygulama olarak başlatılır.



### Tarayıcı uzantısı kurulumu



PearPass, web'de gezinirken otomatik oturum açma ve kasanıza hızlı erişim için bir tarayıcı uzantısı sunar. Uzantı şu anda Google Chrome ve uyumlu tarayıcılar için kullanılabilir. Yüklemek için [resmi indirme sayfası](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh) adresine gidin.



![Image](assets/fr/04.webp)



Eklendikten sonra, hızlı erişim için araç çubuğuna sabitleyebilirsiniz. Uzantıyı etkinleştirmek için PearPass uygulamasının bilgisayarınızda yerel olarak yüklü olması gerekir (bu konuya eğitimin ilerleyen bölümlerinde tekrar döneceğiz).



### IOS ve Android'de kurulum



IPhone ve Android'de, uygulamayı uygulama mağazanızdan indirmeniz yeterlidir:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Bu klasik kurulum yöntemlerine ek olarak, yazılımı doğrudan GitHub depolarından indirmek de mümkündür, her :




- [Masaüstü](https://github.com/tetherto/pearpass-app-desktop);
- [Mobil](https://github.com/tetherto/pearpass-app-mobile);
- [Tarayıcı uzantısı](https://github.com/tetherto/pearpass-app-browser-extension).



PearPass bir veya daha fazla platforma kurulduktan sonra, ilk yapılandırmaya geçebilirsiniz. Bu eğitimde, yazılımı masaüstünde yapılandırarak başlayacağız, ardından tarayıcı uzantısı ve mobil uygulama ile senkronize edeceğiz.



## PearPass kasasını nasıl oluşturabilirim?



PearPass'ı bilgisayarınızda ilk kez başlattığınızda, uygulama sizi iki adımda yönlendirir: ana parolanızı ayarlamak ve ardından ilk kasanızı oluşturmak.



### Ana parolayı ayarla



Uygulama masaüstünde ilk başlatıldığında, giriş ekranından geçmek ve ana şifre yapılandırma aşamasına ulaşmak için `Skip` düğmesine ve ardından `Continue` düğmesine tıklayın.



![Image](assets/fr/06.webp)



Sırada ana parolanızı seçmek gibi önemli bir adım var. Giriş bölümünde gördüğümüz gibi, bu parola çok önemlidir, çünkü yöneticide kayıtlı diğer tüm parolalarınıza erişmenizi sağlar. Teknik olarak, verilerinizi şifrelemek için kullanılan kriptografik anahtarları türetmek için kullanılır.



Ana parola iki temel risk içerir: kayıp ve ele geçirilme. Bu parolaya erişimi kaybederseniz, kimlik bilgilerinize artık erişemezsiniz. Nitekim PearPass ana parolanızı asla saklamaz: **kaybolursa, kimlik bilgileriniz kalıcı olarak kaybolur**. Herhangi bir kurtarma mekanizması yoktur. Buna karşılık, bu parola ele geçirilir ve bir saldırgan cihazlarınızdan birine erişim sağlarsa, tüm hesaplarınıza erişebilir.



Kayıp riskini sınırlandırmak için, ana parolanızın fiziksel bir yedeğini, örneğin kağıt üzerine alabilir ve güvenli bir yerde saklayabilirsiniz. İdeal olarak, bu yedeği bir zarfın içine koyarak mühürleyin, böylece düzenli aralıklarla erişilip erişilmediğini kontrol edebilirsiniz. Öte yandan, bu parolanın asla dijital bir yedeğini almayın.



Ele geçirilme riskini azaltmak için ana parolanızın güçlü olması gerekir. Mümkün olduğunca uzun olmalı, çok çeşitli karakterler içermeli ve gerçekten rastgele bir şekilde seçilmelidir. 2025'te minimum öneriler, parolanın rastgele olması koşuluyla büyük ve küçük harfler, sayılar ve semboller dahil olmak üzere en az 13 karakter gerektirmektedir. Bununla birlikte, daha kalıcı bir güvenlik düzeyi sağlamak için her türlü karakteri içeren en az 20 karakterlik bir parola öneriyorum.



Sağlanan alana ana parolanızı girin, ikinci kez onaylayın ve ardından `Devam Et` düğmesine tıklayın.



![Image](assets/fr/07.webp)



Daha sonra giriş ekranına yönlendirileceksiniz: her şeyin doğru çalışıp çalışmadığını kontrol etmek için ana şifrenizi girin.



![Image](assets/fr/08.webp)



### İlk kasanızı oluşturun



Giriş yaptıktan sonra, PearPass sizden ilk kasanızı oluşturmanızı isteyecektir. Kasa, parolalarınızın, kimlik bilgilerinizin, güvenli notlarınızın ve diğer bilgilerinizin saklandığı şifrelenmiş bir kaptır. Her kasa izole edilmiştir ve verilerinizi kullanımlarınıza göre (kişisel, profesyonel, belirli projeler...) düzenlemenize olanak tanıyan farklı bir adla tanımlanabilir.



Yeni bir kasa oluştur düğmesine tıklayın.



![Image](assets/fr/09.webp)



Bu kasa için bir ad seçin, ardından oluşturma işlemini tamamlamak için tekrar `Yeni bir kasa oluştur` seçeneğine tıklayın.



![Image](assets/fr/10.webp)



Kasanız hemen kullanıma hazırdır. Parolaları, oturum açma bilgilerini veya güvenli notları hemen eklemeye başlayabilirsiniz.



![Image](assets/fr/11.webp)



## PearPass'a nasıl giriş ekleyebilirim?



Kasanızı oluşturduktan sonra, öğelerinizi içine kaydetmeye başlayabilirsiniz. PearPass birçok öğe türünün kaydedilmesini destekler:




- bir siteye veya hizmete giriş yapın ;
- kimlik: formları hızlı bir şekilde doldurmak için kişisel bilgileriniz, aynı zamanda kimlik belgelerini doğrudan PearPass'ta saklamak için;
- kredi kartı: çevrimiçi alışveriş yaparken daha hızlı ödeme için kredi kartı numaralarınız;
- Wi-Fi: Wi-Fi ağlarınız için şifreler ;
- PassPhrase: birkaç kelimeden oluşan gizli ifade (uyarı: wallet Bitcoin anımsatıcı ifadeler için kullanılmamasını şiddetle tavsiye ederim);
- not: güvenli̇ notlar oluşturma ;
- özel: bu özellik, özel ihtiyaçlarınıza göre uyarlanmış özel bir öğe türü oluşturmanıza olanak tanır.



PearPass'ı açarak ve ana parolanızla giriş yaparak başlayın.



![Image](assets/fr/12.webp)



Bu tanımlayıcıyı kaydetmek istediğiniz kasayı seçin.



![Image](assets/fr/13.webp)



Ana sayfada, kaydetmek istediğiniz bilgi türüne bağlı olarak yeni bir öğe eklemek için düğmeye tıklayın. Benim durumumda, Plan ₿ Academy web sitesindeki hesabım için bir giriş eklemek istiyorum: bu yüzden `Giriş Oluştur` düğmesine tıklıyorum.



![Image](assets/fr/14.webp)



Eklemek istediğiniz öğe türünü seçtikten sonra, söz konusu hizmetle ilişkili bilgileri girmenize olanak tanıyan bir form görünür. İhtiyaçlarınıza bağlı olarak, hizmet adını, kullanıcı adını, şifreyi ve gerekirse web sitesi adresini ve ek notları girebilirsiniz.



PearPass ayrıca doğrudan formdan güçlü bir parola oluşturmanıza olanak tanıyan bir parola oluşturucuya sahiptir. Bunu kullanmak için, `Parola` alanında üç küçük noktayı temsil eden simgeye tıklayın, istediğiniz uzunluğu seçin ve ardından `Parola gir` seçeneğine tıklayın.



Tüm alanlar doldurulduktan sonra, tanımlayıcıyı kasaya kaydetmek için `Kaydet` düğmesine tıklayın.



![Image](assets/fr/15.webp)



Tanımlayıcı artık kaydedilmiştir. Seçilen kasadaki öğeler listesinde görünür ve üzerine tıklanarak görüntülenebilir.



![Image](assets/fr/16.webp)



Bir öğenin üzerine tıklayıp ardından `Düzenle` düğmesine tıklayarak kolayca değiştirebilirsiniz. Ayrıca arayüzün sağ üst köşesindeki üç küçük noktaya ve ardından `Elemanı sil` düğmesine tıklayarak da silebilirsiniz.



![Image](assets/fr/22.webp)



Mobil cihazlarda, arayüz uyarlanmış olsa da mantık aynı kalmaktadır. Giriş yaptıktan sonra, istediğiniz kasayı seçin, `+` düğmesine dokunun, oluşturulacak öğenin türünü seçin ve ardından gerekli bilgileri doldurun.



![Image](assets/fr/17.webp)



## PearPass nasıl organize edilir?



Önceki bölümlerde gördüğümüz gibi, PearPass birkaç farklı kasa oluşturmanıza izin verir. Bu, farklı kullanımları ayırmayı mümkün kılar ve parola yöneticiniz için ilk organizasyon seviyesini oluşturur. Ana sayfadan, arayüzün sol üst köşesindeki oka tıklayarak bir kasadan diğerine kolayca geçebilirsiniz.



![Image](assets/fr/18.webp)



Bir kasa içinde bile şifrelerinizi düzenlemenin bir başka yolu da klasörler oluşturmaktır. Bunu yapmak için, arayüzün sol sütununda `Tüm Klasörler`in yanındaki `+` sembolüne tıklayın, ardından oluşturmak istediğiniz klasörün adını girin.



![Image](assets/fr/19.webp)



Daha sonra seçtiğiniz tanımlayıcıları ya doğrudan bir öğe oluştururken ya da daha sonra `Düzenle` seçeneğine tıklayarak saklayabilirsiniz. Tek yapmanız gereken formun sol üst köşesinden istediğiniz klasörü seçmektir.



![Image](assets/fr/20.webp)



Giriş gibi bir öğeyi açtıktan sonra, favorilerinize eklemek için arayüzün sağ üst köşesindeki yıldız simgesine tıklayabilirsiniz. Sık kullanılanlar, temel klasörlerine ek olarak özel bir klasörde hızlı bir şekilde bulunabilir.



![Image](assets/fr/21.webp)



Son olarak, arayüzün üst kısmında bir arama çubuğu vardır, böylece kasanız çok sayıda tanımlayıcı içerse bile aradığınız öğeyi hızlı bir şekilde bulabilirsiniz.



## Cep telefonumda PearPass'ı nasıl senkronize edebilirim?



Artık bilgisayarınızda depolanan öğelerle çalışan bir kasanız olduğuna göre, muhtemelen akıllı telefonunuzdan veya başka bir cihazdan şifrelerinize erişmek isteyeceksiniz. PearPass, Pears kullanarak yöneticinizi birden fazla makinede güvenli bir şekilde senkronize etmenize olanak tanır. Nasıl olduğunu öğrenelim.



Başlamak için, kaynak makinede (örneğin bilgisayarınızda), ana parolanızı kullanarak kasanıza giriş yapın. Ana sayfaya girdikten sonra, arayüzün sağ alt kısmında bulunan `Cihaz Ekle` düğmesine tıklayın.



![Image](assets/fr/23.webp)



PearPass daha sonra seçtiğiniz cihazda seçilen kasayı senkronize etmek için QR kodu olarak da mevcut olan bir davet bağlantısı oluşturur.



![Image](assets/fr/24.webp)



Mobil cihazınızda senkronize etmek istiyorsanız, önce uygulamayı yükleyin, ardından başlatın. Mobil yöneticiniz için bir ana parola oluşturmanız istenecektir. Bilgisayarınızdakiyle aynı parolayı ya da farklı bir parola kullanmayı seçebilirsiniz. Her durumda aynı tavsiyelere uyun: fiziksel bir ortama kaydedilmiş güçlü, rastgele bir parola.



![Image](assets/fr/25.webp)



Daha sonra isterseniz, cep telefonunuzun kilidini her açtığınızda ana parolanızı manuel olarak girmek zorunda kalmamak için biyometrik kimlik doğrulamayı etkinleştirebilirsiniz.



![Image](assets/fr/26.webp)



Ana parolanızı tekrar girin ve ardından `Devam Et` düğmesine tıklayın.



![Image](assets/fr/27.webp)



Bir kasa yükle` seçeneğini seçin, ardından `Karekod Tara` seçeneğine tıklayın ve kaynak makinenizde (bilgisayar) PearPass tarafından görüntülenen davet QR kodunu tarayın.



![Image](assets/fr/28.webp)



Bilgisayarınızdaki ve cep telefonunuzdaki kasalarınız artık senkronize. Bir cihaza eklenen her kimlik diğer cihazda güvenli bir şekilde saklanacak ve çoğaltılacaktır.



![Image](assets/fr/29.webp)



Mobilde, dilerseniz alanların otomatik doldurulmasını da etkinleştirebilirsiniz. Bunun için `Settings > Advanced` bölümüne gidin, ardından `Autofill` kısmındaki `Set as Default` düğmesine tıklayın.



![Image](assets/fr/30.webp)



## PearPass'ı tarayıcı uzantısı ile nasıl senkronize edebilirim?



Bilgisayarınız ve akıllı telefonunuz arasında senkronize bir şifre yöneticisine sahip olmak zaten çok pratik, ancak bunu doğrudan tarayıcınıza entegre etmek daha da pratik. Bunu yapmak için [resmi PearPass uzantısını tarayıcınıza ekleyerek] başlayın (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Yerel makinenizde kurulu PearPass yazılımından `Ayarlar > Gelişmiş` seçeneğine gidin, ardından `Tarayıcı uzantısını etkinleştir` seçeneğini etkinleştirin.



![Image](assets/fr/32.webp)



PearPass bir token eşleştirme dosyası oluşturur. Kopyalayın.



![Image](assets/fr/33.webp)



Ardından tarayıcınızda PearPass uzantısını açın, token eşleştirmesini yapıştırın ve `Doğrula` düğmesine ve ardından `Tamamla` düğmesine tıklayın.



![Image](assets/fr/34.webp)



Parola yöneticiniz artık tarayıcı uzantısı ile senkronize edilmiştir.



![Image](assets/fr/35.webp)



Artık çeşitli web hesaplarınıza kolayca bağlanmak için kullanabilirsiniz.



![Image](assets/fr/36.webp)



Artık PearPass şifre yöneticisini nasıl kullanacağınızı biliyorsunuz. Bu aracın ötesinde, günlük dijital güvenlik uygun çözümlerin doğru kullanımına bağlıdır. Güvenli, istikrarlı ve verimli bir kişisel dijital ortamın nasıl kurulacağını öğrenmek istiyorsanız, sizi bu konuya adanmış eğitim kursumuzu keşfetmeye davet ediyorum:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1