---
name: Qubes
description: Oldukça güvenli bir işletim sistemi.
---

![cover](assets/cover.webp)



Qubes OS, güvenliği önceliklerinin en üstüne koyan kullanıcılar için tasarlanmış ücretsiz, açık kaynaklı bir işletim sistemidir. Özelliği basit ama radikal bir fikre dayanmaktadır: bilgisayarı bir bütün olarak düşünmek yerine, kullanımını **_qubes_** adı verilen bağımsız bölmelere ayırır.



Her qube, belirli bir güven seviyesi ve işlevi olan **izole edilmiş bir sanal ortam** olarak işlev görür. Dolayısıyla, bir uygulama tehlikeye girse bile, saldırı sistemin geri kalanını etkilemeden kendi küpüyle sınırlı kalır.



> Güvenlik konusunda ciddiyseniz, Qubes OS bugün mevcut olan en iyi işletim sistemidir. - **Edward Snowden**.

Ancak Qubes OS'yi kurmak, geleneksel bir işletim sistemini kurmaktan daha fazla hazırlık gerektirir. Belirli donanım ön koşullarını kontrol etmeyi, sanallaştırmanın temellerini anlamayı ve her günlük görevin ayrıştırma açısından düşünüldüğü farklı bir deneyimi kabul etmeyi içerir. Ancak Qubes OS bir kez kurulduğunda, bilgisayarınızla günlük olarak etkileşim kurma şeklinizi yeniden tanımlayan sağlam bir çerçeve sunar. Bu eğitimde, Qubes OS'nin nasıl çalıştığını ve sisteminize nasıl kolayca kurulacağını açıklayacağız.



## Qubes OS nasıl çalışır?



Qubes OS, bölümlere ayırma ilkesine dayanmaktadır. Tek bir sistem kullanmak yerine, qubes adı verilen yalıtılmış sanal makineler oluşturmak için **Xen** hipervizörüne güvenir. Her qube belirli bir göreve veya güven düzeyine (iş, kişisel tarama, bankacılık vb.) adanmıştır. Bu ayrım, bir qube'deki herhangi bir tehlikenin diğerlerine yayılmamasını sağlar ve tek bir makine içinde birkaç bağımsız bilgisayar gibi davranır.



Kullanıcı Interface, **dom0** adı verilen merkezi, güvenli bir etki alanı tarafından yönetilir. Bu etki alanı İnternet'ten tamamen yalıtılmıştır ve sistemin kalbidir. Pencereler ve menüler dom0 tarafından görüntülenmesine rağmen, uygulamaların asıl yürütülmesi kendi küplerinde gerçekleşir.



## Farklı küp türleri



Dom0'ın etrafında, her biri çok özel bir rol oynayan farklı küp türleri döner.





- AppVM** günlük uygulamaları çalıştırmak için kullanılır: böylece kullanıcı profesyonel e-postalarını web'de gezinme veya bankacılık faaliyetlerinden ayırabilir ve her ortam diğerlerinden tamamen bağımsız kalır.





- Bu AppVM'ler, yazılım yüklemek ve güncellemek için merkezi şablonlar olarak hizmet veren ve her bir küpü ayrı ayrı yönetme ihtiyacını ortadan kaldıran **TemplateVM'lere** dayanmaktadır.



Qubes OS ayrıca **sistem hizmetleri** konusunda uzmanlaşmış sanal makineleri de entegre eder.





- NetVM** doğrudan **ağ cihazlarını** yönetir ve İnternet bağlantısını sağlar. Genellikle **trafiği** filtrelemek ve diğer küplerin maruziyetini sınırlamak için müdahale eden **FirewallVM'lerle** ilişkilendirilirler.





- ServiceVM'ler, örneğin USB cihaz yönetiminde, her zaman aynı mantıkla benzer bir rol oynar: saldırı yüzeyini azaltmak için en riskli bileşenleri izole edin.



Son olarak, ara sıra veya riskli görevler için Qubes OS **DisposableVM** sunar. Bu geçici küpler, **şüpheli bir belgeyi açmak** veya **şüpheli bir siteyi ziyaret etmek** için anında oluşturulur, ardından kapatıldığında tamamen kaybolur, tüm izleri siler ve herhangi bir kalıcı saldırıyı önler.



### Güvenli kopyalama mekanizması (qrexec)



Qubes arasındaki alışverişler, güvenlik için tasarlanmış bir VM'ler arası iletişim sistemi olan **qrexec** tabanlıdır. Qubes'in serbestçe iletişim kurmasına izin vermek yerine, qrexec **belirli politikalar** uygular: bir AppVM'den diğerine kopyalanan bir dosya veya pano aracılığıyla aktarılan bir metin, her zaman sistem tarafından izlenen ve doğrulanan bir kanaldan geçer. Bu şekilde, basit bir kopyalama ve yapıştırma eylemi bile kötü amaçlı yazılımların yayılmasını önlemek için kontrol edilir.



### Disk yönetimi



Qubes OS, depolama yönetimi için ustaca bir sistem kullanır. TemplateVM'ler ortak yazılım tabanını içerirken, AppVM'ler yalnızca kendi kişisel verilerini ve belirli dosyaları ekler. Bu, disk alanı kullanımını azaltır ve global güncellemeleri kolaylaştırır. Öte yandan DisposableVM'ler, kapatıldıklarında tamamen yok olan geçici birimler kullanır. Bu model yalnızca daha fazla güvenlik sağlamakla kalmaz, aynı zamanda verimli kaynak yönetimini de garanti eder.



## Neden Qubes OS'yi seçmelisiniz?



Qubes OS'nin avantajları her şeyden önce benzersiz güvenlik modelinde yatmaktadır. Bu yaklaşımın merkezinde, her görevi ayrı sanal makinelerde izole ederek kullanıcıyı koruyan bölümlere ayırma yer alır. Pratik anlamda, virüslü bir e-posta veya kötü amaçlı bir web sitesi yalnızca tek bir qube'u tehlikeye atabilir ve sistemin geri kalanını ve kişisel verilerinizi tamamen korumalı bırakır. Bu mimari, geleneksel bir sistemde serbestçe yayılabilecek karmaşık saldırıları önemli ölçüde sınırlar.



Qubes OS ayrıca dijital ortamınız üzerinde tam şeffaflık ve kontrol sunar. Ağ, USB aygıtı veya diğer hassas bileşenler olsun, hangi yazılımın hangi kaynağa erişimi olduğunu tam olarak bilirsiniz. Sistem, tam disk şifreleme gibi gelişmiş güvenlik özelliklerini varsayılan olarak entegre eder ve Whonix işletim sistemi gibi anonimleştirme hizmetlerinin kullanımını kolaylaştırır.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Qubes OS, aşılmaz bir sistem yaratmaya çalışmak yerine, esnekliğe odaklanır: tehlikeye girme durumunda hasarı kapsülleyerek sistemin geri kalanı için riski azaltır. Bu pragmatik yaklaşım, Qubes OS'yi yüksek güvenlik ihtiyaçları olan veya dijital yaşamları üzerinde maksimum kontrolü elinde tutmak isteyen kullanıcılar için tercih edilen bir seçenek haline getirmektedir.



## Qubes İşletim Sistemini Kurma



Qubes OS'yi kurmadan önce, sistem qubes'i izole etmek için sanallaştırmaya dayandığından, donanımınızın minimum gereksinimleri karşıladığından emin olmanız çok önemlidir. Kontrol edilmesi gereken ana bileşenler şunlardır:




- İşlemci**: Donanım sanallaştırma (Intel VT-x veya AMD-V) ile uyumlu 64 bit işlemci.
- RAM: en az 8 GB gereklidir, ancak aynı anda birkaç qubes çalıştırmak için 16 GB veya daha fazla RAM öneririz.
- Depolama alanı**: en az 36 GB, optimum performans için ideal olarak bir SSD üzerinde 128 GB.



Qubes OS'yi kurmak için, Qubes OS [resmi sitesi] (https://www.qubes-os.org/downloads/) adresinden resmi ISO görüntüsünü indirin. Dosyanın tahrif edilmediğinden ve indirme işleminin güvenli olduğundan emin olmak için sağlanan GPG imzalarını kullanarak ISO'nun bütünlüğünü kontrol etmek önemlidir.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



ISO doğrulandıktan sonra, genellikle bir USB bellek olmak üzere önyüklenebilir bir kurulum ortamı oluşturmanız gerekir. Bunu yapmak için, Windows'ta **Rufus** veya Windows, Linux veya macOS'ta **Etcher** gibi bir yazılım indirip yükleyin. Bu araçlar ISO'yu USB belleğe kopyalamanızı ve böylece önyüklenebilir olmasını sağlar.



Kuruluma başlamadan önce, bilgisayarınızın **BIOS veya UEFI**'sini **sanallaştırmayı etkinleştirecek** ve USB'den önyüklemeye izin verecek şekilde yapılandırmanız gerekir. Makinenizin modeline bağlı olarak, Qubes OS bu seçenek etkinleştirildiğinde önyükleme yapamayabileceğinden **Güvenli Önyüklemeyi** devre dışı bırakmak gerekebilir.



![0_02](assets/fr/02.webp)



Bu koşullar yerine getirildikten sonra, bilgisayarınızı yeniden başlatın ve hemen **Esc**, **Del**, **F9**, **F10**, **F11** veya **F12** tuşlarına basarak BIOS/UEFI'ye erişin (üreticiye bağlı olarak). Önyükleme menüsünde, Qubes OS kurulumunu başlatmak için USB anahtarını önyükleme aygıtı olarak seçin.



**Başlangıç ekranı**


USB bellekten önyükleme yaparken, doğrudan gerçekleştirilecek eylemi seçebileceğiniz **GRUB** menüsüne yönlendirileceksiniz. Klavyenizdeki ok tuşlarını kullanarak "Install Qubes OS" seçeneğini seçin ve "Enter" tuşuna basın.



![0_03](assets/fr/03.webp)



**Dil seçimi** :



Kurulum başladığında, ilk adım yapılandırmanıza uygun **dili** ve **bölgesel varyantı** seçmektir. Bu, sistem ve kurulum seçeneklerinin tercih ettiğiniz dilde doğru şekilde görüntülenmesini sağlar.



![0_04](assets/fr/04.webp)



**Parametre yapılandırması** :



Bu aşamada, makinenizde kurulumu başlatmadan önce bir dizi Elements yapılandırmanız gerekecektir.



![0_05](assets/fr/05.webp)



**Klavye düzeni** :



Klavye** seçeneğine tıklayın, ardından bilgisayarınız için **uygun düzeni** seçin. Seçiminizi yaptıktan sonra, bir sonraki adıma geçmek için **Sonlandırıldı** seçeneğine tıklayın.



**Varış yeri seçimi** :



Qubes OS'yi kurmak istediğiniz diski seçmek için "Kurulum hedefi" seçeneğini seçin. Varsayılan olarak, bölümleme otomatik olarak gerçekleşir ve diskteki tüm verileri kaldırmanıza ve sistemi üzerine kurmanıza olanak tanır. Bununla birlikte, özelleştirilmiş bir bölümleme gerçekleştirmek için **Özelleştirilmiş** veya **Gelişmiş Özelleştirme** seçeneğini seçebilirsiniz. Ardından "Bitti" üzerine tıklayın. Sistem sizden verilerinizi şifrelemek için bir güvenlik Layer görevi gören bir **parola** belirlemenizi isteyecektir. Karmaşık ve benzersiz bir parola seçtiğinizden emin olun.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Tarih ve saat formatını seçin** :


Saat ve tarih seçeneğine tıklayın, ardından coğrafi bölgenizi seçin. Tercih ettiğiniz saat biçimini de seçebilirsiniz: 24 saat veya 12 saat.



![0_08](assets/fr/08.webp)



**Kullanıcı hesabı oluşturma** :


Qubes OS'de oturum açmanızı sağlayacak **ilk hesabınızı** oluşturmak için **Kullanıcı oluştur** seçeneğine tıklayın.



![0_09](assets/fr/09.webp)



**Kök hesabı etkinleştir** :


Yönetim için ayrı bir parola belirleyerek **kök hesabı** da etkinleştirebilirsiniz.



![0_10](assets/fr/10.webp)



Bu ayarlar yapıldıktan sonra, işlemi başlatmak için **Kurulumu başlat** seçeneğine tıklayın.



![0_11](assets/fr/11.webp)



Kurulumun bitmesini** bekleyin, ardından kurulumu tamamlamak ve Qubes OS'yi başlatmak için **sistemi yeniden başlat** seçeneğine tıklayın.



![0_12](assets/fr/12.webp)



**Ek yapılandırma** :


Yeniden başlatmanın ardından Qubes OS sizden **varsayılan şablonları ve qubes yapılandırmasını** sonlandırmanızı ister. Diski şifrelemek için tanımlanan şifreyi girin.



![0_13](assets/fr/13.webp)



Ardından, yüklemek istediğiniz **TemplateVM**'i seçerek başlayın. Yaygın seçenekler arasında **Debian 12 Xfce**, **Fedora 41 Xfce** ve **Whonix 17** bulunur; ikincisi **anonimlik ve ağ güvenliği** gerektiren kullanımlar için önerilir. Ayrıca yeni **AppVM'lerin** oluşturulması için temel teşkil edecek **varsayılan şablonu** da tanımlayabilirsiniz.



![0_14](assets/fr/14.webp)



Ana yapılandırma** bölümünde, **sys-net**, **sys-firewall** ve **default DisposableVM** gibi temel sistem küplerini otomatik olarak oluşturmayı seçebilirsiniz. Tehlike durumunda cihaz ve ağ maruziyetini sınırlamak için **sys-firewall ve sys-usb disposable** yapma seçeneğini etkinleştirmeniz önerilir. Ayrıca, faaliyetlerinizi güven düzeylerine göre düzenlemek için **personal**, **work**, **untrusted** ve **vault** gibi varsayılan **AppVM'ler** oluşturabilirsiniz.



![0_15](assets/fr/15.webp)



Qubes OS ayrıca USB cihazlarına** (sys-usb) ayrılmış bir **qube oluşturmanıza ve Tor ağı üzerinden iletişiminizi güvence altına almak için **Whonix Gateway ve Workstation qubes** yapılandırmanıza olanak tanır. İleri düzey kullanıcılar için **Gelişmiş yapılandırma** bölümü, qubes arasındaki disk alanını verimli bir şekilde yönetmek için bir **LVM ince havuzu** oluşturmanıza olanak tanır.



Tüm bu seçenekler yapılandırıldıktan sonra **Tamamla** ve ardından **Yapılandırmayı bitir** seçeneğine tıklayın. Sistem bu ayarları uygularken bekleyin. Daha sonra **kullanıcı hesabınıza** giriş yapmanız istenecek ve Qubes OS ortamınız kullanıma hazır, güvenli ve çeşitli faaliyetleriniz için uygun şekilde izole edilmiş olacaktır.



![0_17](assets/fr/17.webp)



İşletim sisteminiz artık yüklü ve kullanıma hazırdır.



![0_18](assets/fr/18.webp)



## Sisteminizde bir qube oluşturun



Bir qube oluşturmak için, süreç Başlat menüsünden erişilebilen **Qube Manager** aracı tarafından yönetilir. Araç penceresinde, yeni bir yapılandırma penceresi açmak için **Create qube** simgesine tıklamanız yeterlidir. İlk olarak, qube'unuzun kullanımını tanımlamak için "perso-web" veya "work" gibi bir isim girin.



Ardından, **Türünü** seçeceksiniz, genellikle rutin görevler için **AppVM** veya geçici kullanım için **DisposableVM**. İşletim sistemi ve yazılımı sağlayacağı için qube'unuzun temel alacağı **Template**'i seçmek çok önemlidir, örneğin "fedora-39" veya "debian-12" gibi. Ayrıca, İnternet erişiminden sorumlu küp olan **NetVM**'yi varsayılan olarak **sys-firewall** olarak belirleyeceksiniz.



Son olarak, gerekirse depolama boyutunu ve RAM'i ayarladıktan sonra, **Tamam** üzerine basit bir tıklama oluşturma işlemini başlatacaktır. İşlem tamamlandığında, yeni qube'unuz listede görünür ve kullanıma hazır olacaktır.



Sonuç olarak, Qubes OS sıradan bir işletim sistemi değil, kişisel bilgisayar mimarisini yeniden düşünen son teknoloji bir güvenlik çözümüdür. Sanallaştırma yoluyla bölümlere ayırma ve izolasyona dayanan yaklaşımı, en sofistike tehditlere karşı rakipsiz koruma sağlar. Çalışma ortamını her görev için özel küplere bölerek, kötü amaçlı yazılımların yayılmamasını ve tüm sistemi tehlikeye atmamasını sağlar.



İster internette güvenli bir şekilde gezinmeniz, ister hassas bilgileri korumanız veya farklı güven seviyeleriyle çalışmanız gereksin, Qubes OS esnek, şeffaf bir çerçeve sağlar. İyi uygulamaları benimseyerek ve özelliklerinden tam olarak yararlanarak, modern tehditlere uyarlanmış bir **dijital kaleye** sahip olacaksınız. Verilerinizi ve gizliliğinizi koruma hakkında daha fazla bilgi edinin.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1