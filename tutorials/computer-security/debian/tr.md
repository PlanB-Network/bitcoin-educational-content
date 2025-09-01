---
name: Debian
description: Kararlılığı, sağlamlığı ve uyumluluğu ile tanınan bir Linux dağıtımı.
---

![cover](assets/cover.webp)



Debian, sağlamlığı ve güvenilirliği ile tanınan ücretsiz bir GNU/Linux dağıtımıdır. Linux çekirdeği ve tüm paketleri, kaya gibi sağlam bir kararlılık ve yüksek düzeyde güvenlik sağlamak için titizlikle test edilmiştir. Hem sunucular hem de iş istasyonları için uygun olan Debian, kullanımı kolay bir deneyim ve geniş bir yazılım kataloğu sunar. İster günlük kullanım ister üretim ortamı için güvenli bir sistem arıyor olun, Debian doğru seçimdir.



## Neden Debian'ı seçmelisiniz?





- Ücretsiz ve açık**: Debian tamamen açık kaynaklıdır, şeffaflığı garanti eder ve lisans ücreti yoktur.
- Kararlılık ve güvenlik**: Her sürüm kapsamlı bir test sürecinden geçerek Debian'ı piyasadaki en güvenilir ve güvenli dağıtımlardan biri haline getirir.
- Aktif topluluk**: geniş bir topluluk ve kapsamlı dokümantasyon, ihtiyacınız olduğunda sizi desteklemek için hazırdır.
- Hafif ve ölçeklenebilir**: Debian'ı mütevazı kaynaklara sahip makinelere kurarken iyi bir performans elde edebilirsiniz.
- Kapsamlı yazılım kataloğu**: 50.000'den fazla resmi paket, depolar aracılığıyla kullanılabilir.



## Bir Interface grafiği seçin



Debian, ihtiyaçlarınıza uygun çeşitli masaüstü ortamları sunar:





- GNOME**: modern, sezgisel Interface, yeni başlayanlar için ideal. Uygulamalara erişim için akıcı, kullanımı kolay bir grafik menü sunar.
- XFCE**: hafif ve hızlı, daha az güçlü makineler için mükemmel.
- KDE Plasma**: Windows benzeri bir görünüme sahip, son derece özelleştirilebilir.
- Cinnamon**: Windows'tan esinlenen basit, zarif Interface.
- LXDE / LXQt**: ultra hafif, eski bilgisayarlar için uygun.
- MATE**: basit ve klasik, eski GNOME'a yakın.



💡 Rahat, kolay kavranan bir deneyim için **GNOME şiddetle tavsiye edilir**.



## Debian'ı kurma ve yapılandırma


### Donanım gereksinimleri



Kuruluma başlamadan önce lütfen aşağıdaki ekipmana sahip olduğunuzdan emin olun:





- USB anahtarı**: önyüklenebilir ISO görüntüsünü tutmak için minimum 8 GB.
- Rastgele Erişim Belleği (RAM)**: sorunsuz kurulum ve çalışma için 4 GB.
- Disk alanı**: sistem ve güncellemeler için en az 15 GB boş alan.



### İndir



Debian görüntüsünün seçimi işlemci mimarinize bağlıdır:





- AMD64**: [download] listesinden "live hybrid" sürümünü indirin (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: DVD görüntüsünü resmi [Debian] web sitesinden (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/) edinin.
- Diğer mimariler**: mimarinize karşılık gelen ISO'yu bulun [burada](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Önyüklenebilir bir USB anahtarı oluşturma



Uygun ISO görüntüsünü indirdikten sonra, kurulum medyanızı oluşturmaya devam edin:




- Balena Etcher'ı** [resmi web sitesinden] (https://etcher.balena.io/) indirin, ardından sisteminiz için ikili dosyayı alın ve kurun.



![etcher](assets/fr/02.webp)





- Etcher'ı** başlatın: yazılımı açın ve önceden indirilmiş Debian ISO görüntüsünü seçin.
- USB anahtarını seçin**: hedef olarak anahtarınızı (8 GB+) belirtin.
- Flash'ı başlat**: **Flash!** üzerine tıklayın ve işlem tamamlanana kadar bekleyin.



![flash](assets/fr/03.webp)



USB anahtarınız artık Debian'ı yüklemeye başlamak için hazırdır.



## Debian'ı sisteminize yükleme



### USB anahtarından önyükleme



Yüklemeyi USB anahtarınızdan başlatmak için:




- Bilgisayarı tamamen kapatın**.
- Yeniden başlatın** ardından hemen `ESC`, `F2`, `F11` (veya markanıza bağlı olarak özel tuş) tuşlarına basarak BIOS/UEFI'ye erişin.
- Önyükleme menüsünde, önyükleme aygıtı olarak **USB anahtarınızı** seçin.
- Debian imajını başlatmak için Enter tuşu ile onaylayın**: bu sizi yükleyicinin karşılama ekranına götürecektir.



### Kurulumun başlatılması



Başlangıç ekranı:



![starting](assets/fr/04.webp)



USB bellekten önyükleme yaparken, Debian karşılama ekranı çeşitli seçenekler sunar:




- Canlı Sistem**: Debian'ı kurmadan başlatır, ortamı test etmek için idealdir.
- Yükleyiciyi Başlat**: yüklemeyi doğrudan Hard diskinde başlatır.
- Gelişmiş Kurulum Seçenekleri**: özelleştirilmiş kurulum modlarına erişmenizi sağlar.



Debian'ı canlı modda keşfetmek için **Canlı Sistem** seçeneğini seçin ve **Enter** ile onaylayın. Daha sonra canlı ortamda **Install Debian** seçeneğine tıklayarak kurulumu başlatabilirsiniz.



![system](assets/fr/05.webp)





- Dil seçimi** (isteğe bağlı)



Listeden Debian sisteminizin ana dilini seçin ve ardından Tamam'a tıklayın.



![language](assets/fr/06.webp)





- Saat dilimi** (GMT)



Tarih ve saati otomatik olarak ayarlamak için coğrafi bölgenizi seçin.



![timezone](assets/fr/07.webp)





- Klavye düzeni



Klavye dilinizi ve düzeninizi seçin. Her tuşun beklenen karakteri üretip üretmediğini kontrol etmek için yerleşik test alanını kullanın.



![keyboard](assets/fr/08.webp)



### Disk bölümleme





- Diski sil**: özel bir bölümünüz varsa, bu seçenek tüm içeriğini silecektir.
- Manuel bölümleme**: bölümleri gerektiği gibi oluşturmak, yeniden boyutlandırmak veya silmek için bu seçeneği seçin.



![disk](assets/fr/09.webp)





- Kullanıcı hesabı oluşturma



Oturumunuzun güvenli olduğundan emin olmak için tam adınızı, hesap adınızı ve güçlü bir parola girin.



![user](assets/fr/10.webp)





- Parametre özeti**



Seçimlerinizin bir özeti görüntülenir: her bir öğeyi kontrol edin ve gerekirse değiştirmek için geri dönün.



![settings](assets/fr/11.webp)





- Kurulumun başlatılması



Dosyaları kopyalamaya ve sistemi yapılandırmaya başlamak için **Yükle** seçeneğine tıklayın, ardından işlem tamamlanana kadar bekleyin.



![install](assets/fr/12.webp)





- Yeniden başlat**



Kurulum tamamlandığında, tüm yapılandırmaları uygulamak ve yeni Debian sisteminize erişmek için bilgisayarı yeniden başlatın.



![restart](assets/fr/13.webp)



Başlangıçta, sisteme erişmek için kullanıcı adını ve parolayı girin.



![login](assets/fr/14.webp)



## Sistem güncellemesi



Sisteminizi kullanmaya başlamadan önce onu güncellemeniz çok önemlidir. Bu, en son yazılım yamalarından, güncel depolardan ve bazı durumlarda işletim sisteminin kendisi için güvenlik yamalarından yararlanmanızı sağlar.



### Seçenek 1: Grafiksel Interface (GNOME) aracılığıyla güncelleme



Debian'ı GNOME masaüstü ortamı ile kurduysanız, güncellemeleri grafiksel olarak gerçekleştirebilirsiniz. Bunu yapmak için **Yazılım** uygulamasını açın, ardından **Güncellemeler** sekmesine gidin. Ardından işlemi başlatmak için **Yeniden başlat ve güncelle** seçeneğine tıklayın.



### Seçenek 2: Terminal üzerinden güncelleme (önerilir)



Bu yöntem daha eksiksiz bir kontrol sunar. Depoları, yazılım paketlerini ve gerekirse çekirdeği güncellemenize olanak tanır.




- Ctrl + Alt + T` kısayolunu kullanarak terminali açın.
- Mevcut paketlerin listesini aşağıdaki komutla güncelleyin:



```shell
sudo apt update
```



Sorulduğunda şifrenizi girin (yazarken hiçbir karakterin görüntülenmeyeceğini unutmayın - bu normaldir).





- Mevcut güncellemeleri yüklemek için:



```shell
sudo apt full-upgrade
```



## Temel görevleri keşfedin



### İnternette gezinme



Debian'da varsayılan web tarayıcısı **Firefox**'tur. Başka bir tarayıcı tercih ederseniz, Debian depolarında mevcut olması koşuluyla başka bir tarayıcı yükleyebilirsiniz (Chromium, Brave... gibi).



### Kelime işlemci



LibreOffice** paketi Debian'da varsayılan olarak yüklüdür.





- Belge yazmak için Microsoft Word'ün eşdeğeri olan **LibreOffice Writer** programını kullanın.
- Elektronik tablolar için **LibreOffice Calc** Excel'e alternatif olarak işlev görür.
- Son olarak, **LibreOffice Impress** tıpkı PowerPoint gibi sunumlar oluşturmanızı sağlar.



## Uygulamaları yükleme



Debian'a uygulama yüklemenin iki yolu vardır:



### Grafiksel yöntem:



Uygulamaları kolayca aramak ve yüklemek için **yazılım yöneticisini** (grafik Interface üzerinden erişilebilir) kullanabilirsiniz.



### Komut satırı yöntemi:



Aradığınız uygulama grafiksel Interface'da görünmüyorsa veya terminali tercih ediyorsanız, aşağıdaki komutu kullanın:



```shell
sudo apt install <name>
```



<name>` yerine paket adını yazın. Örneğin, `curl` yüklemek için:



```shell
sudo apt install curl
```



### Manuel olarak indirilen bir paketi yükleme:



Eğer bir `.deb` dosyası (Debian paketi) indirdiyseniz, aşağıdaki komutla kurabilirsiniz:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Debian sisteminiz artık kurulu ve günlük işleriniz için kullanıma hazır.


GNOME** masaüstü ortamı sayesinde, hem yeni başlayanlar hem de ileri düzey kullanıcılar için ideal olan kullanıcı dostu bir grafik Interface aracılığıyla çok çeşitli uygulamalara erişebilirsiniz.



Debian'ı yeniden yüklemenize gerek kalmadan masaüstü ortamınızı (örneğin XFCE, KDE, vb.) değiştirmeniz de mümkündür. Bunu yapmak için terminali kullanmanız ve seçtiğiniz yeni ortamı yüklemeniz yeterlidir.



Debian ve daha genel olarak GNU/Linux dağıtımları hakkında daha fazla bilgi edinmek için bu kursa başvurmanızı tavsiye ederim:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1