---
name: Windows 11
description: Yapılandırma dosyası aracılığıyla Microsoft Windows 11'in Otomatik Kurulumu
---
![cover](assets/cover.webp)


Bu eğitimde, standart Windows yükleme işlemi dışında bir yöntem kullanarak Windows 11'i otomatik olarak nasıl yükleyeceğimizi öğreneceğiz.


## İndirin!


İhtiyacınız olan ilk şey bir kurulum dosyasıdır. Bunu indirmek için en güvenli ve en güvenilir yer doğrudan Microsoft'un resmi web sitesidir.


Aşağıda verilen bağlantıyı ziyaret edin ve [Windows 11 ISO dosyasını] indirmek için talimatları izleyin (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


İndirme sayfasına geldiğinizde, ISO dosyasını indirme bölümüne ilerleyin.


![Image](assets/en/01.webp)


َVe uygun versiyonu seçin.


![Image](assets/en/03.webp)


Windows 11'i seçtikten sonra Onayla düğmesine tıklayın.


Bu adımda, talebin işlenmesi birkaç saniye sürebilir ve ardından aşağıdaki sayfayı göreceksiniz:


![Image](assets/en/04.webp)


Talebi onayladıktan sonra, tercih ettiğiniz dili seçmeniz gerekir.


![Image](assets/en/05.webp)


Dil seçildikten ve Onayla düğmesine tıklandıktan sonra talep işleme alınacaktır. Bu adım birkaç saniye sürebilir.


İstek başarıyla işlendikten sonra, .iso dosyasının indirme bağlantısını içeren bir sayfa göreceksiniz. İndirmeyi başlatmak için 64-bit İndir düğmesine tıklayın.


Dosya boyutu yaklaşık 5,5 GB'tır ve oluşturulan bağlantı 24 saat boyunca geçerli olacaktır.


## Otomasyon!


Bu aşamada, standart Windows kurulumunda değişiklikler yapmamız gerekiyor. Bu aşamada, Katılımsız yükleme kullanarak, daha sonra kullanıcının girdisi olmadan hangi öğelerin yükleneceğini belirleriz. Aslında bu yöntemde, kurulum adımlarını ve Windows'ta yüklü hizmetleri yapılandırmak için bir XML dosyası kullanılır. Başka bir deyişle, Unattended.xml dosyasının kullanımı kurulum sırasında bir otomasyon süreci yaratarak birden fazla seçenek seçme ihtiyacını önler ve kurulum sırasında genellikle gerekli olan sıkıcı adımlardan kaçınır. Bu yöntem, Microsoft tarafından sunulan alışılmadık ancak standart bir yöntemdir. Daha fazla bilgi [Microsoft'un resmi web sitesi] (https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11) adresinde mevcuttur.


Katılımsız dosyalar oluşturmak için internette çeşitli araçlar mevcuttur. Bunlardan bazıları çevrimiçi, bazıları ise çevrimdışıdır. Bu dosyayı oluşturmak için çevrimiçi araçlardan biri [bu web sitesi](https://schneegans.de/windows/unattend-generator). Açtıktan sonra, aşağıdaki sayfa ile karşılaşıyoruz:


![Image](assets/en/06.webp)


Sayfanın üst kısmında belirtildiği gibi, bu yöntem Windows 10 ve 11'i yüklemek için kullanılabilir. İlk adımda Windows dilini seçiyoruz. Eğer Windows ekran ve klavye dilleri listesine ikinci hatta üçüncü bir dil eklememiz gerekirse aşağıdaki kutucuğu kullanabiliriz:


![Image](assets/en/07.webp)


Bir sonraki adımda, istenen konumu seçiyoruz.


![Image](assets/en/08.webp)


Bu aşamada, bilgisayar için işlemci mimarisini de belirleyebiliriz. Bu adımda şunları yapabiliriz:

1. TPM ve Güvenli Önyükleme gibi Windows güvenlik özelliklerini yok sayıp saymayacağınıza karar verin. Güvenli Önyükleme özelliği, önyükleme işlemi sırasında herhangi bir temel Windows dosyasıyla oynanırsa, sorunun algılanmasını ve yürütülmesinin engellenmesini sağlar. Bu özellik ayrıca sistemin Windows'a kötü amaçlı güncellemeler yüklenmesine karşı korunmasına da yardımcı olur. Bu özellikleri atlama seçeneğini etkinleştirmek, özellikle eski modeller olmak üzere bazı bilgisayarlarda bazen kaçınılmazdır. Ancak genellikle Secure Boot gibi özelliklerin etkin tutulması önerilir.

2. İşlemi tamamlamak için internet bağlantısı gerekliliğini göz ardı edin. Bu, kablolu bir LAN bağlantısının mevcut olmadığı durumlarda kullanışlıdır, çünkü çoğu durumda kablosuz kart Windows kurulumu sırasında henüz tanınmaz ve kablo aracılığıyla internet erişimi gerekir. Bu seçeneğin etkinleştirilmesi, bu adımla ilgili sorunları çözer.


Bir sonraki adımda, bilgisayar için bir isim seçebiliriz.


![Image](assets/en/09.webp)


Windows'un sistem için bir ad seçmesine de izin verebiliriz. Bu adımda, sıkıştırılmış veya sıkıştırılmamış Windows türünü seçebilir veya Windows'un bilgisayarın özelliklerine göre uygun sürümü belirlemesine izin verebiliriz. Saat dilimi de bu aşamada ayarlanabilir.


Bir sonraki adım bölüm ayarlarını içerir:


![Image](assets/en/10.webp)


Bu aşamada, Windows'u yüklemek için bölüm türünü ve Windows Kurtarma Ortamını yüklemek için gerekli ayarları belirleyebiliriz. İlk seçenek seçildiğinde, bölüm seçimi ve bölümleme Windows kurulumu zamanına ertelenir ve kurulum sırasında bu sorular tıpkı normal kurulum yönteminde olduğu gibi sorulur.


Bu adımda, kurulacak Windows sürümünü seçiyoruz:


![Image](assets/en/11.webp)


Bir ürün anahtarı mevcutsa, bu aşamada da girilebilir.


Bir sonraki adım Windows oturum açma hesabının yapılandırılmasını içerir:


![Image](assets/en/12.webp)


## Hesap görüşmeleri


Bu aşamada:


1. Yönetici hesabı için bir ad ve parola tanımlayabiliriz. Birden fazla kullanıcı veya yönetici hesabı oluşturmak da mümkündür.

2. Burada, Windows kurulumundan sonra ilk kez hangi hesapta oturum açılacağını belirtiyoruz. Bu bölüm için farklı seçenekler resimde gösterilmiştir.

3. Herhangi bir hesap oluşturulmasını istemiyorsanız, tüm hesapları temizleyin ve bu seçeneği seçin. Bu durumda, Windows kurulumundan sonra otomatik olarak Windows Administrator hesabında oturum açacaksınız.


Bir sonraki adım şifre ve ana bilgisayar dosyası ayarlarının yapılandırılmasını içerir:


![Image](assets/en/13.webp)


Bu aşamada, parolaların bir son kullanma süresine sahip olup olmayacağını belirliyoruz. Ayrıca bu bölüm, ihtiyaçlarınıza göre etkinleştirilebilen veya devre dışı bırakılabilen başarısız giriş denemeleriyle ilgili güvenlik ayarlarını içerir.


Bu bölümün alt kısmında dosya görüntüleme ayarları bulunmaktadır. Bu seçeneklerin hiçbiri standart bir Windows kurulumu sırasında kullanılamaz ve kurulumdan sonra yapılandırılması gerekir. Buna karşın, Katılımsız kurulum yönteminde bu ayarlara kolayca erişilebilir.


Bir sonraki adım Windows güvenlik ayarlarının yapılandırılmasını içerir:


![Image](assets/en/14.webp)


## Güvenlik ayarları


Bu aşamada:


1. Windows Defender etkinleştirilebilir veya devre dışı bırakılabilir. Bu özellik Windows'taki güvenlik yazılımı gibi davranır ve kötü amaçlı dosyaların, belirli ağ saldırılarının ve daha fazlasının yürütülmesini önlemeye yardımcı olur.

2. Otomatik Windows güncellemeleri devre dışı bırakılabilir. Bu, Windows kullanıcılarının karşılaştığı yaygın zorluklardan biridir!

3. Bu bölüm UAC'nin (Kullanıcı Hesabı Denetimi) etkinleştirilmesini veya devre dışı bırakılmasını sağlar. Bu özellik, şüpheli uygulamaların okuma ve yazma için yükseltilmiş izinlerle çalışmasını önler.

4. Bu özellik Windows tarafından potansiyel olarak zararlı yazılımları tespit etmek için kullanılır.

5. PowerShell ve diğerleri gibi Windows uygulamalarında uzun yollar için desteği etkinleştirin veya devre dışı bırakın.

6. Sisteme uzaktan erişmek için Uzak Masaüstü'nü etkinleştirin veya devre dışı bırakın.


Kullanılan Windows sürümüne bağlı olarak, bu özelliklerden bazıları desteklenebilir veya desteklenmeyebilir.


Bir sonraki adım simgelerin yapılandırılmasını içerir:


![Image](assets/en/15.webp)


Bu bölümde:


1. Gerektiğinde eklenebilen veya kaldırılabilen masaüstü simgeleri listelenir.

2. Başlat menüsü simgeleri listelenir ve bunlar da gereksinimlere göre eklenebilir veya kaldırılabilir.

3. Bu bölüm sanallaştırmayla ilgili araçların yüklenip yüklenmeyeceğinin yapılandırılmasını sağlar. Bu seçenek Windows 11'e özgüdür ve Windows 10 için geçerli değildir.


Bir sonraki adım Wi-Fi ayarlarının yapılandırılmasını içerir:


![Image](assets/en/16.webp)


Bu bölümde Wi-Fi ağ ayarları yapılandırılabilir. Daha önce de belirtildiği gibi, çoğu durumda Wi-Fi kartı Windows kurulumu sırasında tanınmaz, bu nedenle kurulum sırasında bağlanmak genellikle mümkün değildir. Ancak bu bölüm yapılandırılarak, kablosuz kart algılanırsa sistem internete bağlanabilir.


Bir sonraki adım önemli bir ayarı içerir:


![Image](assets/en/17.webp)


Bu bölümde, sistem sorun bilgilerinin Microsoft'a gönderilip gönderilmeyeceğini belirtiyoruz.


Bir sonraki adım varsayılan uygulamaların yapılandırılmasını içerir:


![Image](assets/en/18.webp)


## Varsayılan yazılım etkinleştirme/devre dışı bırakma


Bu bölümde, varsayılan olarak yüklenmesini istemediğimiz uygulamaları seçebiliriz. Örneğin, Cortana veya Copilot'u yüklememeyi tercih edebiliriz.


Bir sonraki adım, uygulama yürütme ile ilgili güvenlik ayarlarını içerir:


![Image](assets/en/19.webp)


WDAC ayarları uygulanarak belirli uygulamaların yürütülmesi engellenebilir.


Son olarak, istenen ayarlar uygulandıktan sonra, oluşturulan XML dosyası indirilebilir:


![Image](assets/en/20.webp)


XML Dosyasını İndir seçeneğine tıklandığında autounattend.xml dosyası indirilir. Bu dosyayı kullanmak için, indirilen ISO'yu bir USB sürücüsüne takın, autounattend.xml dosyasını kök dizine yerleştirin ve ardından Windows kurulumuna devam edin.


Önyüklenebilir bir USB sürücü oluşturmak için kullanılabilecek araçlardan biri Rufus'tur. Rufus, belirli bir Windows kurulum ISO dosyası ile önyüklenebilir bir Windows kurulum flash sürücüsü oluşturabilir. Hızlı ve basittir, [buradan](https://rufus.ie/en/#download) indirebilirsiniz


![Image](assets/en/21.webp)


Bu yazılımda, istenen USB sürücüsünü ve uygun ISO dosyasını seçtikten sonra Başlat'a tıklıyoruz.


![Image](assets/en/22.webp)


Bu aşamada, tüm seçenekleri devre dışı bırakıyoruz, çünkü bunların etkin olması oluşturulan Unattend dosyasını kullanırken çakışmalara neden olabilir. Dosyalar USB sürücüsüne kopyalandıktan sonra autounattend.xml dosyasını kök dizine yerleştiriyoruz:


![Image](assets/en/23.webp)


Bu noktada, USB sürücü Windows'u otomatik olarak yüklemek için kullanıma hazırdır ve kurulum bu sürücü kullanılarak başlatılabilir.


## ISO düzenleme


Windows'u sanal bir makineye yüklemeniz gerekiyorsa, ISO dosyalarını oluşturmak ve düzenlemek için yazılım kullanabilirsiniz. Böyle bir yazılım AnyBurn'dür. Microsoft web sitesinden indirilen ISO dosyasının içeriğini çıkardıktan sonra, autounattend.xml dosyasını kök dizine yerleştirin. Ardından AnyBurn kullanarak güncellenmiş içeriklerle yeni bir ISO oluşturun.


AnyBurn ISO dosyaları ile çalışmak için çok işlevli bir yazılımdır. ISO dosyalarını işlemek için çeşitli özellikler sunar, bunlardan biri önyüklenebilir ISO görüntüleri oluşturmaktır; [burada](https://www.anyburn.com/download.php) orijinal web sitesidir.


Yazılımın ana sayfasında "Dosya/Klasörden Görüntü Oluştur" seçeneğini seçin:


![Image](assets/en/24.webp)


Bir sonraki sayfada, autounattend.xml dosyası ile birlikte ISO'dan çıkarılan tüm dosyaları seçin.


![Image](assets/en/25.webp)


Bu adımda, ISO dosyasını önyüklenebilir hale getirmek için ayarları yapılandırıyoruz:


![Image](assets/en/26.webp)


Bu aşamada, ISO'yu önyüklenebilir hale getirmek için bootfix.bin dosyasının yolu ayarlanmalıdır. Bu dosya ISO'nun kökünde, önyükleme klasörünün içinde bulunur. Ayrıca Özellikler bölümünde hem ISO9660 hem de UDF seçeneklerinin etkinleştirilmesi önerilir.


![Image](assets/en/27.webp)


Bu adımdan sonra İleri'ye tıkladığınızda ISO dosyası oluşturulacaktır. Bu dosya Oracle VirtualBox gibi sanallaştırma yazılımlarında kullanılabilir. aşağıda VirtualBox hakkında bir eğitim bulacaksınız:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65