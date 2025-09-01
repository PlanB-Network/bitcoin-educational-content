---
name: Fedora
description: Size ücretsiz, eksiksiz ve güvenli bir çalışma alanı sağlayan Linux dağıtımı.
---


![cover](assets/cover.webp)





Fedora, 2003 yılında başlatılan, **Fedora Project** topluluğu tarafından geliştirilen ve **Red Hat Linux** tarafından desteklenen ücretsiz, açık kaynaklı Linux tabanlı bir işletim sistemidir. Kararlılığı, iyi performansı ve kullanım kolaylığı ile ünlüdür, bu da onu hem yeni başlayanlar hem de ileri düzey kullanıcılar için mükemmel bir seçim haline getirir. Sistem çoğu modern işlemci mimarisinde çalışır, bu da neredeyse her bilgisayara kurulmasını kolaylaştırır. Fedora ayrıca "Fedora Spins" veya "Fedora Editions" olarak adlandırılan ve özel ihtiyaçlar (video oyunları, astronomi, geliştirme...) için tasarlanmış önceden yapılandırılmış çeşitli sürümlerde mevcuttur.



## Fedora Linux mimarisi



Daha önce de okuduğunuz gibi Fedora, Linux çekirdeğini temel alan ücretsiz bir işletim sistemidir. Linux çekirdeği, işletim sisteminin bilgisayar donanımı ile iletişim kuran ve bellek ve işlem gücü gibi sistem kaynaklarını yöneten kısmıdır.



Fedora Linux, işletim sistemini Linux çekirdeği üzerinde çalıştırmak için gerekli olan çeşitli yazılım araçları ve uygulamaları içerir. Fedora'nın modüler mimarisi, gerektiğinde kolayca eklenebilen, çıkarılabilen veya değiştirilebilen bireysel bileşenlerin bir koleksiyonundan oluştuğu anlamına gelir. Bu, işletim sistemini yalnızca ihtiyacınız olan kaynakları kullanarak şekillendirmenize olanak tanır.



Fedora ayrıca kullanıcıların görevleri yerine getirdiği ve uygulamalara eriştiği Interface olan bir masaüstü ortamı da içerir. Fedora'nın varsayılan masaüstü ortamı, kullanıcı dostu, kullanımı kolay ve son derece özelleştirilebilir bir masaüstü ortamı olan GNOME'dur.



## Neden Fedora'yı seçmelisiniz?



Mevcut çok sayıda Linux dağıtımı arasında Fedora, özellikle:





- Modülerlik**: Farklı işlemci mimarileriyle uyumlu olan Fedora, düşük güçlü olanlar da dahil olmak üzere çoğu bilgisayara kurulabilir ve ihtiyaçlarınıza mükemmel şekilde uyum sağlar.





- Basit, sezgisel bir Interface**: Fedora, modern bir grafik Interface ile güçlü bir komut satırı Interface'i birleştirerek tüm profiller için kullanımı kolaylaştırır.





- Çekirdek kararlılığı**: Red Hat tabanlı Fedora, geniş bir topluluğun ücretsiz katkıları sayesinde büyük hatalar olmadan gerçekleştirilen güncellemelerinin, özellikle de çekirdek güncellemelerinin güvenilirliği ile ünlüdür.





- Hızlı, kolay kurulum**: Sadece 3 GB'lık görüntü boyutuyla, sınırlı kaynaklara sahip makinelerde bile kurulum hızlı ve kolaydır.



## Fedora sürümleri



Profilinize ve kullanımınıza bağlı olarak, Fedora ihtiyaçlarınıza uygun sürümler sunar. Esas olarak şunları bulacaksınız:





- Fedora İş İstasyonu**: Bilgisayarlarınızda kişisel ve/veya profesyonel kullanım için ideal olan bu sürüm, tarayıcılar, ofis paketi (metin düzenleyiciler) ve medya oynatma yazılımı gibi genel yardımcı programlarla birlikte yüklenir.





- Fedora Sunucusu**: Bu sürüm sunucu yönetimine adanmıştır. Fedora Server, sunucuları kendi ölçeğinize göre dağıtmanıza ve yönetmenize yardımcı olacak çeşitli araçlar içerir.





- Fedora CoreOS**: Bulut uygulamalarını kolayca çalıştırmak ve dağıtmak mı istiyorsunuz? Fedora CoreOS, örneğin Docker ve Kubernets ile imajlar oluşturmak ve yönetmek için size araçlar sağlayan sürümdür.



Bu eğitimde, Fedora Workstation sürümünün sorumluluğunu alacağız. Ancak, aşağıda ayrıntıları verilen işlemler diğer sürümler için de benzerdir.



## Fedora Workstation'ı yükleme ve yapılandırma



Fedora Workstation'ı yüklemek için aşağıdaki donanım yapılandırması gerekir:




- İşletim sistemini başlatmak için en az **8 GB** büyüklüğünde bir USB anahtarı.
- Bilgisayarınızın Hard diskinde en az **40 GB boş alan**.
- sorunsuz bir deneyim için 4 GB RAM**.



### Fedora İş İstasyonunu İndirin



Fedora Workstation] sürümünü (https://fedoraproject.org/fr/workstation/download) resmi Fedora projesi web sitesinden indirebilirsiniz. Ardından işlemci mimarinize (32-bit - 64-bit) karşılık gelen sürümü seçin ve **İndir** simgesine tıklayın.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Önyüklenebilir bir USB anahtarı oluşturma



Fedora'yı yüklemek için [Balena Etcher] (https://etcher.balena.io/) gibi bir yazılım kullanarak önyüklenebilir bir USB anahtarı oluşturmanız gerekir.



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Balena Etcher'ı yüklemeyi tamamladıktan sonra uygulamayı açın ve indirilen Fedora Workspace ISO görüntüsünü seçin. Hedef medya olarak USB anahtarınızı seçin ve önyüklenebilir anahtarı oluşturmaya başlamak için **Flash** düğmesine tıklayın.



![boot](assets/fr/05.webp)


### Fedora Kurulumu



USB anahtarınızı önyüklemeyi bitirdiğinizde bilgisayarınızı kapatın.


Bilgisayarınızı açın, ardından başlangıç sırasında bilgisayarınıza bağlı olarak `F2`, `F12` veya `ESC` tuşuna basarak BIOS'a erişin.



Önyükleme seçeneklerinde, birincil önyükleme aygıtı olarak USB anahtarınızı seçin. Bu seçimi onayladığınızda, bilgisayarınız yeniden başlatılacak ve USB anahtarında bulunan Fedora yükleyicisini** otomatik olarak başlatacaktır.



Bilgisayarınız USB bellekten önyükleme yaptıktan sonra **GRUB ekranı** görünür.



Bu aşamada aşağıdaki seçeneklere sahipsiniz:




- Ortamı test edin**: Bu seçenek USB belleğin bütünlüğünü kontrol etmenizi ve doğru bir kurulum için gereken tüm bağımlılıkların mevcut olduğundan emin olmanızı sağlar. Bu isteğe bağlı bir adımdır, ancak USB bellek hakkında herhangi bir şüpheniz varsa önerilir.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Fedora'yı Başlat**: Bu, Fedora'yı kurulum yapmadan "canlı" modda başlatır.



Fedora masaüstünde (canlı mod), yükleme işlemini başlatmak için **Install Fedora** (veya Install on Hard disk) seçeneğine tıklayın. Daha sonra yüklemeyi seçebilir ve Fedora'yı yüklemek zorunda kalmadan test edebilirsiniz.



![install-live](assets/fr/08.webp)



İlk adım Fedora'nın **kurulum dilini** ve **klavye düzenini** seçmektir



![language](assets/fr/10.webp)





- Kurulum diskinin seçilmesi:



Fedora'yı yüklemek istediğiniz Hard diskini seçin.



Eğer disk boşsa, Fedora otomatik olarak tüm kullanılabilir alanı kullanacaktır. Aksi takdirde, bölümlemeyi özelleştirebilirsiniz (manuel veya otomatik).



![disk](assets/fr/11.webp)





- Şifreleme:



Bu aşamada Fedora, ekstra bir Layer güvenlik eklemek için diskinizi şifrelemenizi önerir. Bu, verilerinizin yalnızca Fedora sisteminiz tarafından okunabilmesini sağlar.



![chiffrement](assets/fr/12.webp)



Kurulumu başlatmadan önce, Fedora seçimlerinizin bir özetini görüntüler. Fedora kurulumunu başlatmak için onaylayın ve yükle düğmesine tıklayın.



![resume](assets/fr/13.webp)



Kurulum sırasında Fedora dosyaları kopyalar ve sistemi yapılandırır. Bittiğinde, bilgisayar otomatik olarak yeniden başlatılır.



![installation](assets/fr/14.webp)



### Temel yapılandırma


İlk kullanımda, birkaç ayarı tamamlamanız gerekecektir:




- Gerekirse sistem dilini değiştirin.



![language](assets/fr/15.webp)





- Tercihlerinize uygun bir klavye düzeni seçin.



![keyboard](assets/fr/16.webp)





- Arama çubuğuna şehrinizin adını yazarak saat diliminizi seçin ve ardından ilgili öneriye tıklayın.



![timezone](assets/fr/17.webp)





 - İhtiyaç duyan uygulamalar için konumunuza erişimi ve hata raporlarının otomatik olarak gönderilmesini etkinleştirin veya devre dışı bırakın.



![location](assets/fr/18.webp)





- Üçüncü taraf yazılım depolarını etkinleştirmek isteyip istemediğinize karar verin.



![logs](assets/fr/19.webp)





- Tam adınızı girin ve hesabınız için bir kullanıcı adı tanımlayın.



![name](assets/fr/20.webp)





- Oturumunuz için güvenli bir parola oluşturun: olabildiğince uzun (en az 20 karakter), olabildiğince rastgele ve çeşitli karakterler (küçük harf, büyük harf, sayılar ve semboller). Şifrenizi kaydetmeyi unutmayın.



![mdp](assets/fr/21.webp)



Tüm bu adımlar tamamlandıktan sonra, Fedora'yı başlatın ve başka bir yeniden başlatmaya gerek kalmadan hemen kullanmaya başlayın.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Kurulumunuz tamamlandıktan sonra, önceden yüklenmiş birkaç yardımcı programla Interface evinize danışabilirsiniz.



![install-now](assets/fr/09.webp)



## Temel görevleri keşfedin



### İnternette gezinme


Fedora'nın varsayılan tarayıcısı **Firefox**. Kullanımı kolaydır ve çoğu ihtiyaç için uygundur.


Başka bir tarayıcıyı tercih ederseniz, **yazılım yöneticisinden** veya **terminal** üzerinden yükleyebilirsiniz.


### Kelime işlemci


Fedora, varsayılan olarak çeşitli yararlı araçlar sunan **LibreOffice** ofis paketini içerir:




- Kelime işlem için Writer**.
- Elektronik tablolar için Calc**.
- Sunumlar oluşturmak için Impress**.


## Uygulamaları yükleme


Yeni uygulamalar yüklemek için, Fedora'nın **yazılım yöneticisini** (_Software_ olarak adlandırılır) kullanabilirsiniz, bu da kurulumu kolay ve görsel hale getirir.  Ancak, **terminali** kullanmak genellikle daha hızlı ve daha doğrudur.



Herhangi bir yazılımı yüklemeden önce, mevcut en son sürümlere erişiminiz olduğundan emin olmak için **repositories**'i güncellemeyi unutmayın.



Ardından, istenen uygulamanın kurulumunu başlatmak için aşağıdaki komutu kullanın:


sudo dnf install yazılım_adı`


## İşletim sisteminizi güncelleme


Kurulumdan sonra, en son güvenlik yamaları ve yazılım güncellemelerinden yararlanmak için Fedora'yı güncellemek önemlidir.


### Seçenek 1: Interface grafiği aracılığıyla




- Fedora **Ayarlar**'ı açın, ardından **Sistem** bölümüne gidin.
- **Yazılım güncelleme** üzerine tıklayın.
- Güncellemeleri indirmeye başlayın ve işlem tamamlanana kadar bekleyin.



Güncellemeler yüklendikten sonra bir **yeniden başlatma** gerekebilir.


### Seçenek 2: Terminal üzerinden




- Bir terminal açın ve en son sürümlere sahip olduğunuzdan emin olmak için **repositories**'i güncelleyerek başlayın:



```shell
sudo dnf check-update
```





- Ardından, aşağıdaki komutla tüm yüklü yazılımları güncelleyin:



```shell
sudo dnf upgrade
```



Artık Fedora sisteminiz güncel ve tüm günlük işleriniz için kullanıma hazır. Başka bir Linux dağıtımı olan Linux Mint hakkındaki eğitimimizi ve Bitcoin işlemleriniz için nasıl sağlıklı ve güvenli bir ortam kuracağınızı keşfedin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5