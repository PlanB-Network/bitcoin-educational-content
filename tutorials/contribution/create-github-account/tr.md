---
name: GitHub Hesabı
description: GitHub'da kendi hesabınızı nasıl oluşturabilirsiniz?
---

![cover](assets/cover.webp)


Plan ₿'ın misyonu, Bitcoin hakkında mümkün olduğunca çok dilde mevcut olan üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılmaktadır, bu da herkese platformun zenginleştirilmesine katkıda bulunma fırsatı sunmaktadır. Katkılar çeşitli şekillerde olabilir: mevcut metinlerin düzeltilmesi ve redaksiyonu, diğer dillere çeviriler, bilgilerin güncellenmesi veya sitemizde henüz bulunmayan yeni eğitimlerin oluşturulması.


Plan ₿ Network'e katkıda bulunmak istiyorsanız, Git ve GitHub kullanmanız gerekecek, bu nedenle, bu araçlar size yabancı geliyorsa veya işleyişleri belirsiz görünüyorsa panik yapmayın, bu makale tam size göre! Git ve GitHub'ın temellerini ve ilgili teknik jargonu birlikte gözden geçirerek daha sonra bunları etkili bir şekilde kullanmanızı sağlayacağız.


## Git nedir?


Git, özellikle yazılım projelerini yönetmek için tasarlanmış bir sürüm kontrol sistemidir. Linus Torvalds tarafından 2005 yılında oluşturulan Git, yazılım geliştirme endüstrisinde sürüm kontrolü için hızla standart haline gelmiştir. Peki bu tam olarak ne anlama geliyor?

![git](assets/11.webp)

Özünde Git, geliştiricilerin bir projenin kaynak kodunda zaman içinde yapılan değişiklikleri izlemelerine olanak tanır. Bu, koddaki her değişiklikle birlikte Git'in projenin yeni bir sürümünü kaydettiği anlamına gelir. Bir hata oluşursa veya deneysel bir özellik beklendiği gibi çalışmazsa, bir tür zaman makinesi gibi kodun önceki bir durumuna geri dönmek mümkündür, ancak dosyalar için.


Git'in temel özelliklerinden biri dal yönetimidir. Dal, geliştiricilerin projenin geri kalanından bağımsız olarak çalışabilecekleri bir tür paralel hattır. Bu, ana kodu bozmadan yeni özelliklerin eklenmesini veya hataların düzeltilmesini büyük ölçüde kolaylaştırır. Değişiklikler test edilip onaylandıktan sonra ana dal ile birleştirilebilir.


Git'in özelliklerinden biri de dağıtılmış bir şekilde çalışabilmesidir. Her geliştiricinin kendi bilgisayarının Hard sürücüsünde projenin tam bir kopyası vardır, bu da çevrimdışı çalışmalarına ve daha sonra bir İnternet bağlantısı mevcut olduğunda değişiklikleri birleştirmelerine olanak tanır. Bu, çakışma riskini azaltır ve birden fazla geliştiricinin aynı proje üzerinde birbirlerinin ayak parmaklarına basmadan aynı anda çalışmasına olanak tanır.

Başlangıçta Git öncelikle yazılım geliştirme projeleri için tasarlanmıştır. Ancak, içerik yazma projelerini yönetmek için de kullanılabilir. Kod üzerinde işbirliği yapmak yerine metin üzerinde işbirliği yapıyoruz. İşte Plan ₿ Network'ün içeriğini yönetmek için benimsediği yöntem de tam olarak bu! Git, değişikliklerin hassas bir şekilde izlenmesine, verimli sürüm yönetimine ve ayrıca içeriğin diğer katılımcılar tarafından gözden geçirilmesine ve geliştirilmesine olanak tanıdığı için kurslar ve eğitimler yazarken işbirliğini kolaylaştırır.


## GitHub nedir?


GitHub, daha önce bahsettiğimiz Git sürüm kontrol sistemine dayanan bir kaynak kodu yönetimi ve barındırma platformudur. 2008 yılında faaliyete geçen GitHub, kısa sürede popülerlik kazanmış ve dünya çapındaki geliştiriciler için vazgeçilmez bir referans haline gelmiştir. Peki GitHub'ın Git'ten farkı nedir ve içerik üretim yöntemimizde neden bu kadar önemlidir?

![github](assets/12.webp)

Öncelikle, GitHub'ın Git üzerine kurulu olduğunu anlamak önemlidir (önceki bölümde tartışmıştık). Git kod değişikliklerini takip eden bir araçken, GitHub bu kodu barındıran, paylaşan ve yöneten çevrimiçi bir hizmettir.


Git'i, her geliştiricinin projesindeki tüm değişiklikleri kaydetmek için kendi bilgisayarında kullandığı bir tür seyir defteri olarak düşünün. GitHub ise tüm bu kayıt defterlerinin paylaşılabildiği, karşılaştırılabildiği ve birleştirilebildiği halka açık bir kütüphane gibidir.


Git ve GitHub arasındaki temel fark işlevlerinde yatmaktadır: Git, kod sürümlerini yönetmek için her geliştirici tarafından yerel olarak kullanılan bir araçtır; GitHub ise bu sürümleri barındıran ve işbirliğini kolaylaştıran çevrimiçi bir platformdur.


GitHub bir kod barındırma hizmetinden çok daha fazlasıdır. Geliştiricilerin birlikte verimli bir şekilde çalışmasını sağlayan bir işbirliği platformudur. Ve gerçekten de Plan ₿ Network bu platformu sadece web sitesine güç veren tüm kodları değil, aynı zamanda bizi ilgilendiren tüm içeriği (öğreticiler, eğitimler, kaynaklar...) barındırmak için kullanıyor.


## Bazı Teknik Terimler


Git ve GitHub'da, isimleri karmaşık görünebilecek komutlar ve özelliklerle karşılaşacaksınız. Bu son bölümde, Git ve GitHub'ı kullanırken karşılaşabileceğiniz teknik terimleri anlamanız için bazı basit tanımlar sunacağım:



- Fetch origin:** Uzak bir depodaki son bilgileri ve değişiklikleri yerel çalışmanızla birleştirmeden alan komut. Yerel deponuzu, uzak depoda bulunan yeni dallar ve taahhütlerle günceller.



- Pull origin:** Uzak bir depodan güncellemeleri alan ve senkronize etmek için bunları hemen yerel dalınıza entegre eden komut. Bu, getirme ve birleştirme adımlarını tek bir komutta birleştirir.
- Sync Fork:** GitHub'da bir projenin Fork'ini kaynak depodaki en son değişikliklerle güncellemenizi sağlayan bir özellik. Bu, proje kopyanızın ana geliştirme ile güncel kalmasını sağlar.
- Push origin:** Yerel değişikliklerinizi uzaktaki bir depoya göndermek için kullanılan komut.



- Çekme İsteği:** Bir katılımcı tarafından uzak bir depodaki bir dala değişiklik gönderdiğini ve bu değişikliklerin gözden geçirilmesini ve potansiyel olarak deponun ana dalıyla birleştirilmesini istediğini belirtmek için gönderilen bir istek.



- Commit:** Değişikliklerinizi kaydetme. Bir commit, belirli bir andaki çalışmanızın anlık görüntüsü gibidir ve değişikliklerin geçmişini tutmaya olanak tanır. Her commit, neyin değiştirildiğini açıklayan açıklayıcı bir mesaj içerir.



- Dal:** Deponun paralel bir sürümüdür ve ana dalı (genellikle "ana" veya "master" olarak adlandırılır) etkilemeden değişiklikler üzerinde çalışmanıza olanak tanır. Dallar, kararlı kodu bozma riski olmadan yeni özelliklerin geliştirilmesini ve hataların düzeltilmesini kolaylaştırır.



- Birleştirme:** Birleştirme, bir daldaki değişiklikleri diğerine entegre etmekten oluşur. Örneğin, bir çalışma dalındaki değişiklikleri ana dala eklemek için kullanılır, bu da çeşitli katkıların eklenmesine izin verir.



- Fork:** Bir depoyu çatallamak, kendi GitHub hesabınızda bu deponun bir kopyasını oluşturmak anlamına gelir; bu, orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork kendi yoluna gidebilir ve orijinalinden farklı bir proje haline gelebilir veya ona katkıda bulunmak için orijinal projeyle düzenli olarak senkronize olabilir.



- Klonlama:** Bir depoyu klonlamak, bilgisayarınızda tüm dosyalara ve geçmişe erişmenizi sağlayan yerel bir kopya oluşturmak anlamına gelir. Bu, proje üzerinde doğrudan yerel olarak çalışmanıza olanak tanır.



- Depo:** GitHub'da bir proje için depolama alanı. Bir depo, tüm proje dosyalarının yanı sıra üzerinde yapılan tüm değişikliklerin geçmişini içerir. GitHub'da depolama ve işbirliğinin temelidir.



- Issue:** GitHub'da görevleri ve hataları izlemek için bir araç. Sorunlar, sorunların bildirilmesine, iyileştirmelerin önerilmesine veya yeni özelliklerin tartışılmasına olanak tanır. Her sorun atanabilir, etiketlenebilir ve hakkında yorum yapılabilir.


Bu liste kesinlikle kapsamlı değildir. Git ve GitHub'a özgü başka birçok teknik terim vardır. Ancak, burada bahsedilenler sıklıkla karşılaşacağınız ana terimlerdir.


Bu makaleyi okuduktan sonra, Git ve GitHub'ın bazı yönleri sizin için hala belirsiz olabilir, bu nedenle bu araçları kendiniz kullanmaya başlamanızı tavsiye ederim. Pratik yapmak genellikle makinenin nasıl çalıştığını anlamanın en iyi yoludur! Ve başlamak için, bu diğer 2 öğreticiyi keşfedebilirsiniz:


## GitHub hesabı nasıl oluşturulur


PlanB Network'e katkıda bulunmak istiyorsanız, bir GitHub hesabına ihtiyacınız olacak. Bu eğitimde, kendi hesabınızı nasıl oluşturacağınız, kuracağınız ve düzgün bir şekilde güvence altına alacağınız konusunda size adım adım rehberlik edeceğiz.



- Https://github.com/signup](https://github.com/signup) adresine gidin.
- E-posta adresinizi girin Address, ardından Green `Devam Et` düğmesine tıklayın:

![github](assets/1.webp)


- Güçlü bir parola seçin ve ardından Green `Devam Et` düğmesine tıklayın:

![github](assets/12.webp)


- Ardından, kullanıcı adınızı seçin. Gerçek kimliğinizi açıklayabilir veya bir takma ad kullanabilirsiniz. Ardından, Green `Devam Et` düğmesine tıklayın:

![github](assets/3.webp)


- Captcha'yı tamamlayın:

![github](assets/4.webp)


- Size bir onay kodu içeren bir e-posta gönderilecektir; hesabınızın oluşturulmasını tamamlamak için bu kodu girmeniz gerekecektir:

![github](assets/5.webp)


- GitHub'ın sizi belirli araçlara yönlendirmesini istiyorsanız soruları doldurun veya atlamak için `kişiselleştirmeyi atla` seçeneğine tıklayın:

![github](assets/6.webp)


- Ücretsiz devam et` butonuna tıklayarak ücretsiz planı seçin:

![github](assets/7.webp)


- Daha sonra kontrol panelinize yönlendirileceksiniz.
- Dilerseniz, ekranın sağ üst köşesinde bulunan profil resminize tıklayarak ve ardından `Ayarlar` menüsüne erişerek hesabınızı özelleştirebilirsiniz:

![github](assets/8.webp)


- Bu bölümde yeni bir profil resmi ekleme, bir ad seçme, biyografinizi özelleştirme veya kişisel web sitenize bir bağlantı ekleme seçeneğiniz vardır:

![github](assets/9.webp)


- Ayrıca en azından iki faktörlü kimlik doğrulamayı ayarlamak için `Şifre ve kimlik doğrulama` menüsünü ziyaret etmenizi öneririm:

![github](assets/10.webp)