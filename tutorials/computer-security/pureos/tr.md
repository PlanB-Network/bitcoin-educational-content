---
name: PureOS
description: Dijital yaşamınız üzerinde kontrol sahibi olmanızı sağlayan Linux dağıtımı.
---

![cover](assets/cover.webp)



Dijital çağda kişisel bilgilerin korunması her İnternet kullanıcısı için en önemli önceliktir. Şirketler, kuruluşlar ve hatta işletim sistemleri, profilinizi ve yaşam tarzınızı tanımlamak için yararlı bilgi kaynaklarıdır. Doğru işletim sistemini seçmek, çevrimiçi gizliliğinizi güçlendirmenin ilk adımıdır. Bu eğitimde, gizlilik odaklı bir Linux dağıtımı olan PureOS'a göz atacağız.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## PureOS ile çalışmaya başlama



PureOS, Purism tarafından geliştirilen Debian tabanlı bir işletim sistemidir. PureOS hem BT profesyonelleri hem de basit, kullanımı kolay bir dağıtım arayan kullanıcılar için uygundur. Özgür Yazılım* olmasıyla benzersizdir ve Debian tarafından sunulan gizlilik, özgürlük, güvenlik ve istikrara dayalı bir çerçeve oluşturarak kullanıcılarının kişisel verilerinin korunmasına odaklanır.



### Neden PureOS'u seçmelisiniz?





- Basit, sezgisel Interface**: GNOME, komut satırında rahat olmayan kişiler için bile kullanımı kolay olacak şekilde tasarlanmış net bir Interface masaüstü sunar.





- Ücretsiz**: Çoğu Linux dağıtımı gibi PureOS'un kullanımı da tamamen ücretsizdir. Ancak, geliştiricileri desteklemek için aylık bir abonelik mevcuttur.





- Güvenlik ve kararlılık**: PureOS'un mimarisi ve işletim modu, onu son derece güvenli bir dağıtım haline getirerek veri koruması ve sistem kararlılığını garanti eder.





- Dokümantasyon ve aktif topluluk**: PureOS, sorunları çözmeyi ve sistemi adım adım öğrenmeyi kolaylaştıran açık, erişilebilir belgelere ve kararlı, duyarlı bir topluluğa sahiptir.



## Kurulum ve yapılandırma



PureOS'u bilgisayarınıza kurmak ve yapılandırmak için aşağıdaki minimalist özelliklere sahip olmanız gerekir:




- Sistemi flaşlamak için en az 8 GB'lık bir USB anahtarı.
- 4 GB RAM.
- gW-1 diskinizde 30 GB boş alan.



PureOS resmi web sitesine] (https://pureos.net/) gidin ve ardından makinenizin mimarisine göre işletim sisteminin ISO görüntüsünü indirin.



PureOS kurulumunu başlatmak için, [Balena Etcher] (https://www.balena.io/etcher) gibi bir flash yazılımı kullanarak önyüklenebilir bir USB anahtarı oluşturmanız gerekir.



Üç kolay adımda, PureOS işletim sistemi ile önyüklenmiş bir USB bellek elde edeceksiniz.





- USB anahtarını takın ve indirilen Balena yazılımını çalıştırın.
- Ardından PureOS ISO görüntüsünü seçin
- USB anahtarını çıkış aygıtı olarak seçin, ardından **Flash** düğmesine tıklayın ve işlemin bitmesini bekleyin.



![0_01](assets/fr/01.webp)



USB anahtarı önyüklendikten sonra, PureOS'u yüklemek istediğiniz bilgisayarı yeniden başlatın.



Önyükleme sırasında, makinenize bağlı olarak `ESC`, `F9` veya `F11` tuşuna basarak BIOS'a erişin. Önyükleme aygıtı olarak USB anahtarını seçin, ardından onaylamak için `ENTER` tuşuna basın.



### Başlangıç ekranı



PureOS, işletim sistemini başlatmak için çeşitli seçenekler sunar. İşletim sistemi kurulumunu başlatmak için **Test or Install PureOS** seçeneğini seçin.



![0_02](assets/fr/02.webp)



Bilgisayarınızda kullanmak istediğiniz dili ve klavye düzenini ayarlayın.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Bölgenize göre kişiselleştirilmiş öneriler için uygulamalara **coğrafi konumunuza** erişime izin verin veya erişimi reddedin.



![0_05](assets/fr/05.webp)



Başka bir sistemde kullandığınız ofis paketine bağlı verileri almak için mevcut **NextCloud** hesabınıza bağlanabilirsiniz.



![0_06](assets/fr/06.webp)



Bir eğitim verilmektedir, ancak bu adımı atlamak isterseniz pencereyi kapatabilirsiniz.



![0_08](assets/fr/08.webp)



### Kurulumun başlatılması



Aktiviteler** menüsüne tıklayın ve sisteme önceden yüklenmiş uygulamaları ve araçları keşfedin. Kurulumu başlatmak için **Install PureOS** üzerine tıklayın



![0_09](assets/fr/09.webp)



Sistem dilini ve klavye düzenini gerektiği gibi ayarlayın, ardından Hard disk bölümleme modunu yapılandırın.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Hard diskinizi bölümlemek için iki seçeneğiniz vardır:




- Diski sil**: PureOS'un tam kurulumu için, Hard diskinizdeki önceden var olan tüm verileri siler.



![0_14](assets/fr/14.webp)





- Kendi skorlarınızı oluşturmak için Manuel Bölümleme**



⚠️ İşletim sisteminiz için manuel olarak bölümler oluşturduğunuzda, PureOS işlemi için en az 2 GB'lık bir bölüm ve ardından veriler için başka bir bölüm ayırdığınızdan emin olun.



![0_15](assets/fr/15.webp)



Verilerinizi güvence altına almak istiyorsanız **disk şifrelemeyi** etkinleştirin. Güçlü, karmaşık bir parola girin.



Verilerinizin güvenliğini güçlendirmek için bir kullanıcı adı ve en az 20 karakterden oluşan alfanümerik bir parola tanımlayarak işletim sisteminizle bir kullanıcıyı ilişkilendirin.



![0_16](assets/fr/16.webp)



Yaptığınız ayarları gözden geçirin ve gerekirse değiştirin.



![0_17](assets/fr/17.webp)



PureOS'un bilgisayarınıza yüklendiğini onaylamak için **Yükle** ve ardından **Şimdi Yükle** üzerine tıklayın.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Yükleme tamamlandığında, bilgisayarınızı yeniden başlatmak için **Şimdi yeniden başlat** kutusunu işaretleyin ve ardından onaylayın:




- Dil.
- Klavye düzeni.
- NextCloud hesabınız (isteğe bağlı).



![0_25](assets/fr/25.webp)



## Güncellemeler



PureOS'u kullanmaya başlamadan önce sisteminizi güncellemeniz çok önemlidir. Bu, en son özelliklerden ve güvenlik yamalarından yararlanmanızı ve daha fazla kararlılık sağlamanızı mümkün kılacaktır.





- Interface grafiği aracılığıyla güncelleme**:


Yazılım** uygulamasını açın, ardından **Güncellemeler** sekmesine gidin. Mevcut güncellemeler otomatik olarak görüntülenir. İndirme işlemi tamamlandıktan sonra **İndir** ve ardından **Yükle** seçeneğine tıklayın.





- Terminal üzerinden güncelleyin**:


Terminali açın, ardından mevcut paketlerin listesini güncellemek için aşağıdaki komutu girin:



```shell
sudo apt update
```



Şifrenizi girin ve onaylayın. Ardından güncellemeleri ile yükleyin:



```shell
sudo apt full-upgrade
```



## Geliştirme için PureOS



PureOS varsayılan olarak geliştirme için gereken tüm araçları içermez.


Bunları aşağıdaki komutla hızlı bir şekilde yükleyebilirsiniz:



```shell
sudo apt install build-essential git curl
```



Bu, çoğu geliştirme ortamında yararlı olan **Git** ve **Curl** derleme araçlarını yükleyecektir.



## PureOS ortamı



PureOS, gerçek yakınsamaya yönelik yenilikçi yaklaşımıyla öne çıkıyor: tek bir işletim sistemi, dizüstü bilgisayarlar, tabletler, mini PC'ler ve akıllı telefonlar dahil olmak üzere çeşitli cihazlarda sorunsuz ve kesintisiz çalışma sağlıyor.



PureOS uygulamaları uyarlanabilir olacak şekilde tasarlanmıştır: ekran boyutuna ve giriş moduna (dokunmatik veya klavye/fare) otomatik olarak uyum sağlarlar. Örneğin, GNOME Web tarayıcısı hem mobil hem de masaüstü cihazlarda en iyi deneyimi sağlamak için Interface'yı dinamik olarak uyarlar.



PureOS ayrıca **LibreOffice** ofis paketini de içerir:





- Writer**: belge oluşturmak ve düzenlemek için eksiksiz bir kelime işlemci.
- Calc**: verilerinizi ve hesaplamalarınızı yönetmek için güçlü bir elektronik tablo programı.
- Impress**: profesyonel sunumlar oluşturmak için bir araç.



Bu ücretsiz paket, tescilli yazılımlara bağımlı kalmadan verimli bir şekilde çalışmanızı sağlar.



PureOS, tam kontrolü ve gizliliğe sıkı bir şekilde saygı gösterilmesini garanti eden %100 açık kaynak dağıtımına dayalı birleşik, güvenli ve esnek bir ortam sunar. Gerçek yakınsaması, karmaşık uyarlamalara gerek kalmadan bilgisayarlar, tabletler ve akıllı telefonlar gibi farklı cihaz türleriyle uyumlu uygulamaların oluşturulmasını kolaylaştırır.



Temel araçlara yerel erişim, sağlam paket yöneticileri ve zengin bir açık kaynak ekosistemi ile PureOS, güvenli bir ortamda uygulama geliştirme, test etme ve dağıtmayı basitleştirir. İstikrarlı mimarisi ve Commitment'den gizliliğe, Blockchain geliştirme, hızlı prototipleme veya üretim ortamları dahil olmak üzere çeşitli kullanımlar için güvenilir bir platform haline getirir.



Güvenliğinizi güçlendirmeye ve dijital gizliliğinizi korumaya yönelik kursumuzu keşfedin.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1