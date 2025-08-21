---
name: VeraCrypt
description: Bir depolama aygıtı nasıl kolayca şifrelenir?
---
![cover](assets/cover.webp)


Günümüzde, kişisel belgeleriniz, fotoğraflarınız veya önemli projeleriniz gibi dosyalarınızın erişilebilirliğini, güvenliğini ve yedeklenmesini sağlamak için bir strateji uygulamak önemlidir. Bu verileri kaybetmek felakete yol açabilir.


Bu sorunları önlemek için, dosyalarınızın birden fazla yedeğini farklı ortamlarda tutmanızı tavsiye ederim. Bilgisayarda yaygın olarak kullanılan bir strateji, dosyalarınızın korunmasını sağlayan "3-2-1" yedekleme stratejisidir:


- dosyalarınızın 3** kopyası;
- En az **2** farklı medya türüne kaydedilmiştir;
- En az **1** kopyası şirket dışında tutulmalıdır.


Başka bir deyişle, dosyalarınızı bilgisayarınız, harici bir Hard sürücüsü, USB bellek veya çevrimiçi depolama hizmeti gibi farklı nitelikteki ortamları kullanarak 3 farklı yerde saklamanız tavsiye edilir. Ve son olarak, şirket dışı bir kopyaya sahip olmak, evinizin veya iş yerinizin dışında depolanan bir yedeğiniz olması gerektiği anlamına gelir. Bu son nokta, yangın veya sel gibi yerel felaketlerde dosyalarınızın tamamen kaybolmasını önlemeye yardımcı olur. Evinizden veya iş yerinizden uzakta bulunan harici bir kopya, verilerinizin yerel risklerden bağımsız olarak hayatta kalmasını sağlar.


Bu 3-2-1 yedekleme stratejisini kolayca uygulamak için, bilgisayarınızdaki dosyaları bulutunuzdakilerle otomatik olarak veya periyodik olarak senkronize eden bir çevrimiçi depolama çözümünü tercih edebilirsiniz. Bu çevrimiçi yedekleme çözümleri arasında bildiğiniz büyük dijital şirketlere ait olanlar da var: Google Drive, Microsoft OneDrive veya Apple iCloud. Ancak bunlar gizliliğinizi korumak için en iyi çözümler değildir. Daha önceki bir eğitimde, daha iyi gizlilik için belgelerinizi şifreleyen bir alternatifi tanıtmıştım: Proton Drive.


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Bu yerel ve bulut yedekleme stratejisini benimseyerek, verileriniz için biri tesis dışında olmak üzere iki farklı medya türünden zaten faydalanmış olursunuz. 3-2-1 stratejisini tamamlamak için ek bir kopya eklemeniz yeterlidir. Yapmanızı önerdiğim şey, yerel olarak ve bulutunuzda bulunan verilerinizi periyodik olarak USB bellek veya harici bir Hard sürücüsü gibi fiziksel bir ortama aktarmaktır. Bu şekilde, çevrimiçi depolama çözümünüzün sunucuları yok olsa ve bilgisayarınız aynı anda bozulsa bile, verilerinizi kaybetmemek için harici bir ortamda bu üçüncü kopyaya sahip olursunuz.

![VeraCrypt](assets/notext/01.webp)

Ancak, sizden veya sevdiklerinizden başka kimsenin erişememesini sağlamak için veri depolamanızın güvenliği hakkında düşünmek de önemlidir. Hem yerel hem de çevrimiçi veriler normalde güvenlidir. Bilgisayarınızda muhtemelen bir şifre belirlemişsinizdir ve modern bilgisayarların Hard sürücüleri genellikle varsayılan olarak şifrelenmiştir. Çevrimiçi depolama alanınızla (bulut) ilgili olarak, önceki eğitimde hesabınızı güçlü bir parola ve iki faktörlü kimlik doğrulama ile nasıl güvence altına alacağınızı gösterdim. Ancak, fiziksel bir ortamda saklanan üçüncü kopyanız için tek güvenlik, fiziksel olarak sahip olunmasıdır. Eğer bir hırsız USB belleğinizi ya da harici Hard sürücünüzü çalmayı başarırsa, tüm verilerinize kolayca erişebilir.

![VeraCrypt](assets/notext/02.webp)

Bu riski önlemek için fiziksel ortamınızı şifrelemeniz tavsiye edilir. Böylece, verilere herhangi bir erişim girişimi, içeriğin şifresini çözmek için bir parola girilmesini gerektirecektir. Bu parola olmadan, USB belleğinizin veya harici Hard sürücünüzün çalınması durumunda bile kişisel dosyalarınızı güvence altına alarak verilere erişmek imkansız olacaktır.

![VeraCrypt](assets/notext/03.webp)

Bu eğitimde, açık kaynaklı bir araç olan VeraCrypt'i kullanarak harici bir depolama ortamını nasıl kolayca şifreleyebileceğinizi göstereceğim.


## VeraCrypt'e Giriş


VeraCrypt, verilerinizi çeşitli şekillerde ve farklı ortamlarda şifrelemenize olanak tanıyan Windows, macOS ve Linux'ta kullanılabilen açık kaynaklı bir yazılımdır.

![VeraCrypt](assets/notext/04.webp)

Bu yazılım, şifrelenmiş birimlerin anında oluşturulmasını ve sürdürülmesini sağlar; yani verileriniz kaydedilmeden önce otomatik olarak şifrelenir ve okunmadan önce şifresi çözülür. Bu yöntem, depolama ortamınızın çalınması durumunda bile dosyalarınızın korunmasını sağlar. VeraCrypt sadece dosyaları değil, aynı zamanda dosya adlarını, meta verileri, klasörleri ve hatta depolama ortamınızdaki boş alanı da şifreler.


VeraCrypt dosyaları yerel olarak ya da sistem diski de dahil olmak üzere tüm bölümleri şifrelemek için kullanılabilir. Bu eğitimde göreceğimiz gibi USB bellek veya disk gibi harici bir ortamı tamamen şifrelemek için de kullanılabilir.


VeraCrypt'in tescilli çözümlere göre en büyük avantajı tamamen açık kaynak kodlu olmasıdır, yani kodu herkes tarafından doğrulanabilir.


## VeraCrypt nasıl kurulur?


"*Downloads*" sekmesindeki [resmi VeraCrypt web sitesine] (https://www.veracrypt.fr/en/Downloads.html) gidin.

![VeraCrypt](assets/notext/05.webp)

İşletim sisteminize uygun sürümü indirin. Windows kullanıyorsanız, "*EXE Installer*" seçeneğini seçin.

![VeraCrypt](assets/notext/06.webp)

Interface'ünüz için dil seçin.

![VeraCrypt](assets/notext/07.webp)

Lisans koşullarını kabul edin.

![VeraCrypt](assets/notext/08.webp)

"*Yükle*" öğesini seçin.

![VeraCrypt](assets/notext/09.webp)

Son olarak, yazılımın yükleneceği klasörü seçin ve ardından "*Yükle*" düğmesine tıklayın.

![VeraCrypt](assets/notext/10.webp)

Kurulumun tamamlanmasını bekleyin.

![VeraCrypt](assets/notext/11.webp)

Kurulum tamamlanmıştır.

![VeraCrypt](assets/notext/12.webp)

Dilerseniz, bu açık kaynaklı aracın geliştirilmesini desteklemek için bitcoin cinsinden bağışta bulunabilirsiniz.

![VeraCrypt](assets/notext/13.webp)

## VeraCrypt ile bir depolama aygıtı nasıl şifrelenir?


İlk fırlatışta bu Interface'e ulaşacaksınız:

![VeraCrypt](assets/notext/14.webp)

Seçtiğiniz depolama aygıtını şifrelemek için makinenize bağlayarak başlayın. Daha sonra göreceğiniz gibi, bir USB bellek veya Hard sürücüsünde yeni bir şifreli birim oluşturma işlemi, cihaz zaten silmek istemediğiniz verileri içeriyorsa çok daha uzun sürecektir. Bu nedenle, zamandan tasarruf etmek için şifreli birimi oluşturmak için boş bir USB bellek kullanmanızı veya cihazı önceden boşaltmanızı öneririm.


VeraCrypt'te "*Volumes*" sekmesine tıklayın.

![VeraCrypt](assets/notext/15.webp)

Ardından "*Yeni Birim Oluştur...*" menüsünde.

![VeraCrypt](assets/notext/16.webp)

Açılan yeni pencerede "*Sistem dışı bir bölümü/sürücüyü şifrele*" seçeneğini seçin ve "*Sonraki*" düğmesine tıklayın.

![VeraCrypt](assets/notext/17.webp)

Daha sonra "*Standart VeraCrypt birimi*" ve "*Gizli VeraCrypt Birimi*" arasında seçim yapmanız gerekecektir. İlk seçenek cihazınızda standart bir şifrelenmiş birim oluşturur. "*Gizli VeraCrypt Birimi*" seçeneği standart bir VeraCrypt birimi içinde gizli bir birim oluşturulmasını sağlar. Bu yöntem, zorlama durumunda bu gizli birimin varlığını inkar etmenizi sağlar. Örneğin, birisi sizi fiziksel olarak cihazınızın şifresini çözmeye zorlarsa, saldırganı tatmin etmek için yalnızca standart kısmın şifresini çözebilir, ancak gizli kısmı açıklamayabilirsiniz. Benim örneğimde, standart bir birim ile devam edeceğim.

![VeraCrypt](assets/notext/18.webp)

Takip eden sayfada "*Cihaz Seç...*" düğmesine tıklayın.

![VeraCrypt](assets/notext/19.webp)

Makinenizde bulunan diskler listesinden depolama aygıtınızın bölümünü seçebileceğiniz yeni bir pencere açılır. Normalde, şifrelemek istediğiniz bölüm "*Çıkarılabilir Disk N*" başlıklı bir satırın altında listelenecektir. Uygun bölümü seçtikten sonra "*Tamam*" düğmesine tıklayın.

![VeraCrypt](assets/notext/20.webp)

Seçilen destek kutuda görünür. Şimdi "*Sonraki*" düğmesine tıklayabilirsiniz. ![VeraCrypt](assets/notext/21.webp)

Ardından, "*Şifreli birim oluştur ve biçimlendir*" veya "*Bölümü yerinde şifrele*" seçenekleri arasından seçim yapmanız gerekecektir. Daha önce de belirtildiği gibi, ilk seçenek USB belleğinizdeki veya Hard sürücünüzdeki tüm verileri kalıcı olarak silecektir. Bu seçeneği yalnızca cihazınız boşsa seçin; aksi takdirde içerdiği tüm verileri kaybedersiniz. Mevcut verileri saklamak istiyorsanız, geçici olarak başka bir yere aktarabilir, her şeyi silen daha hızlı bir işlem için "*Şifreli birim oluştur ve biçimlendir*" seçeneğini seçebilir veya "*Bölümü yerinde şifrele*" seçeneğini tercih edebilirsiniz. Bu son seçenek, halihazırda mevcut olan verileri silmeden birimin şifrelenmesini sağlar, ancak işlem çok daha uzun sürecektir. Bu örnekte, USB belleğim boş olduğu için, her şeyi silen "*Şifreli birim oluştur ve biçimlendir*" seçeneğini seçiyorum.

![VeraCrypt](assets/notext/22.webp)

Ardından, şifreleme algoritmasını ve Hash işlevini seçme seçeneğiniz olacaktır. Özel ihtiyaçlarınız olmadığı sürece, varsayılan seçenekleri korumanızı tavsiye ederim. Devam etmek için "*Sonraki*" üzerine tıklayın.

![VeraCrypt](assets/notext/23.webp)

USB bellekteki kullanılabilir alanın sadece bir kısmını değil tamamını şifrelemek için biriminiz için belirtilen boyutun doğru olduğundan emin olun. Doğrulandıktan sonra, "*Sonraki*" üzerine tıklayın.

![VeraCrypt](assets/notext/24.webp)

Bu aşamada, cihazınızı şifrelemek ve şifresini çözmek için bir parola belirlemeniz gerekecektir. Bir saldırganın kaba kuvvet saldırılarıyla içeriğinizin şifresini çözmesini önlemek için güçlü bir parola seçmeniz önemlidir. Parola rastgele, mümkün olduğunca uzun olmalı ve çeşitli karakter türlerini içermelidir. Küçük harfler, büyük harfler, sayılar ve semboller içeren en az 20 karakterden oluşan rastgele bir parola seçmenizi tavsiye ederim.


Ayrıca şifrenizi bir şifre yöneticisine kaydetmenizi tavsiye ederim. Bu, erişimi kolaylaştırır ve unutma riskini ortadan kaldırır. Bizim özel durumumuz için, bir parola yöneticisi kağıt ortamına tercih edilir. Gerçekten de, bir hırsızlık durumunda, depolama cihazınız çalınsa bile, yöneticideki parola saldırgan tarafından bulunamaz ve bu da verilere erişimi engeller. Tersine, parola yöneticiniz ele geçirilirse, parolayı kullanmak ve verilere erişmek için cihaza fiziksel erişim hala gereklidir.


Parolaları yönetme hakkında daha fazla bilgi için, bu diğer eksiksiz öğreticiyi keşfetmenizi tavsiye ederim:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Belirlenen 2 alana şifrenizi girin, ardından "*Sonraki*" üzerine tıklayın. ![VeraCrypt](assets/notext/25.webp)

VeraCrypt daha sonra size şifrelenmiş birimde 4 GiB'den büyük dosyaları saklamayı planlayıp planlamadığınızı soracaktır. Bu soru yazılımın en uygun dosya sistemini seçmesini sağlar. Genel olarak, işletim sistemlerinin çoğuyla uyumlu olduğu için FAT sistemi kullanılır, ancak maksimum dosya boyutu sınırı 4 GiB'dir. Daha büyük dosyaları yönetmeniz gerekiyorsa, exFAT sistemini tercih edebilirsiniz.

![VeraCrypt](assets/notext/26.webp)

Ardından, rastgele bir anahtar generate girmenize olanak tanıyan bir sayfaya ulaşacaksınız. Bu anahtar, verilerinizi şifrelemek ve şifresini çözmek için kullanılacağından önemlidir. Medyanızın belirli bir bölümünde saklanacak ve daha önce belirlediğiniz parola ile güvence altına alınacaktır. generate güçlü bir şifreleme anahtarı için VeraCrypt entropiye ihtiyaç duyar. Bu nedenle yazılım sizden farenizi pencere üzerinde rastgele hareket ettirmenizi ister; bu hareketler daha sonra anahtarı generate yapmak için kullanılır. Entropi göstergesi tamamen dolana kadar fareyi hareket ettirmeye devam edin. Ardından, şifrelenmiş birimi oluşturmaya başlamak için "*Format*" üzerine tıklayın.

![VeraCrypt](assets/notext/27.webp)

Biçimlendirme işlemi tamamlanırken bekleyin. Bu işlem büyük hacimler için uzun sürebilir.

![VeraCrypt](assets/notext/28.webp)

Daha sonra bir onay alacaksınız.

![VeraCrypt](assets/notext/29.webp)

## VeraCrypt ile şifrelenmiş bir sürücü nasıl kullanılır?


Şimdilik, medyanız şifrelenmiştir ve bu nedenle onu açamazsınız. Şifresini çözmek için VeraCrypt'e gidin.

![VeraCrypt](assets/notext/30.webp)

Listeden bir sürücü harfi seçin. Örneğin, ben "*L:*" seçtim.

![VeraCrypt](assets/notext/31.webp)

"*Aygıt Seç...*" düğmesine tıklayın.

![VeraCrypt](assets/notext/32.webp)

Makinenizdeki tüm disklerin listesinden, ortamınızdaki şifrelenmiş birimi seçin ve ardından "*Tamam*" düğmesine tıklayın.

![VeraCrypt](assets/notext/33.webp)

Biriminizin iyi seçilmiş olduğunu görebilirsiniz.

![VeraCrypt](assets/notext/34.webp)

"*Mount*" düğmesine tıklayın.

![VeraCrypt](assets/notext/35.webp)

Birim oluşturma sırasında seçilen şifreyi girin ve ardından "*Tamam*" düğmesine tıklayın.

![VeraCrypt](assets/notext/36.webp)

Biriminizin artık şifresinin çözüldüğünü ve "*L:*" sürücü harfinden erişilebilir olduğunu görebilirsiniz.

![VeraCrypt](assets/notext/37.webp)

Erişmek için dosya gezgininizi açın ve "*L:*" sürücüsüne (veya önceki adımlarda seçtiğiniz harfe bağlı olarak başka bir harfe) gidin. ![VeraCrypt](assets/notext/38.webp)

Kişisel dosyalarınızı medyaya ekledikten sonra, birimi tekrar şifrelemek için "*Dismount*" düğmesine tıklamanız yeterlidir.

![VeraCrypt](assets/notext/39.webp)

Biriminiz artık "*L:*" harfinin altında görünmez. Böylece tekrar şifrelenir.

![VeraCrypt](assets/notext/40.webp)

Artık depolama ortamınızı kaldırabilirsiniz.


Tebrikler, artık kişisel verilerinizi güvenli bir şekilde saklamak için şifrelenmiş bir ortamınız var, böylece bilgisayarınızdaki kopyaya ve çevrimiçi depolama çözümünüze ek olarak eksiksiz bir 3-2-1 stratejisine sahipsiniz.


VeraCrypt'in gelişimini desteklemek isterseniz, [bu sayfada] (https://www.veracrypt.fr/en/Donation.html) bitcoin olarak bağışta bulunabilirsiniz.