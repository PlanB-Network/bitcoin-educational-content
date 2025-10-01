---
name: GitHub Desktop
description: Yerel çalışma ortamınızı nasıl kurarsınız?
---
![github](assets/cover.webp)


PlanB'nin misyonu, Bitcoin hakkında mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılmaktadır, bu da herkesin platformu zenginleştirmeye katılmasına olanak tanır. Katkılar çeşitli şekillerde olabilir: mevcut metinleri düzeltmek ve düzeltmek, diğer dillere çevirmek, bilgileri güncellemek veya sitemizde henüz bulunmayan yeni eğitimler oluşturmak.


PlanB Ağına katkıda bulunmak istiyorsanız, değişiklik önermek için GitHub'ı kullanmanız gerekecektir. Bunu yapmak için iki seçeneğiniz vardır:


- GitHub'ın **Interface** web sitesi üzerinden doğrudan katkıda bulunun: Bu en basit yöntemdir. Yeni başlayan biriyseniz veya yalnızca birkaç küçük katkı yapmayı planlıyorsanız, bu seçenek muhtemelen sizin için en iyisidir;
- **Git** kullanarak yerel olarak katkıda bulunun: PlanB Network'e düzenli veya önemli katkılarda bulunmayı planlıyorsanız bu yöntem daha uygundur. Bilgisayarınızda yerel Git ortamınızı kurmak ilk başta karmaşık görünse de, bu yaklaşım uzun vadede daha verimlidir. Değişikliklerin daha esnek bir şekilde yönetilmesini sağlar. Bu konuda yeniyseniz endişelenmeyin, **ortamınızı kurma sürecinin tamamını bu eğitimde açıklıyoruz** (söz veriyorum, herhangi bir komut satırı yazmanıza gerek kalmayacak ^^).


GitHub'ın ne olduğu hakkında hiçbir fikriniz yoksa veya Git ve GitHub ile ilgili teknik terimler hakkında daha fazla bilgi edinmek istiyorsanız, bu kavramlara aşina olmak için giriş makalemizi okumanızı tavsiye ederim.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- Başlamak için tabii ki bir GitHub hesabına ihtiyacınız olacak. Zaten bir hesabınız varsa giriş yapabilirsiniz, aksi takdirde yeni bir tane oluşturmak için eğitimimizi kullanabilirsiniz.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Adım 1: GitHub Desktop'ı yükleyin



- GitHub Desktop yazılımını indirmek için https://desktop.github.com/ adresine gidin. Bu yazılım, bir terminal kullanmak zorunda kalmadan GitHub ile kolayca etkileşim kurmanızı sağlar:

![github-desktop](assets/1.webp)


- Yazılımı ilk başlattığınızda, GitHub hesabınızı bağlamanız istenecektir. Bunu yapmak için `GitHub.com`da oturum aç` seçeneğine tıklayın:

![github-desktop](assets/2.webp)


- Tarayıcınızda bir kimlik doğrulama sayfası açılacaktır. Hesabınızı oluştururken seçtiğiniz Address e-posta adresinizi ve şifrenizi girin, ardından `Sign in` düğmesine tıklayın:

![github-desktop](assets/3.webp)


- Hesabınız ve yazılım arasındaki bağlantıyı onaylamak için `Masaüstünü yetkilendir` seçeneğine tıklayın:

![github-desktop](assets/4.webp)


- Otomatik olarak GitHub Masaüstü yazılımına yönlendirileceksiniz. Bitir`e tıklayın: ![github-desktop](assets/5.webp)
- GitHub hesabınızı yeni oluşturduysanız, henüz herhangi bir depo oluşturmadığınızı belirten bir sayfaya yönlendirileceksiniz. Bu noktada, GitHub Masaüstü yazılımını bir kenara koyun; daha sonra geri döneceğiz: ![github-desktop](assets/6.webp)


## Adım 2: Obsidian'ı Kurun


Yazma yazılımını yüklemeye geçelim. Burada birkaç seçeneğiniz var. PlanB Network, deposundaki metin dosyaları için bu biçimi kullandığından, Markdown dosyalarını düzenlemeyi destekleyen bir yazılıma ihtiyacınız olacak.


Markdown dosyalarını düzenlemek için özel olarak tasarlanmış Typora gibi çok sayıda yazılım vardır. İdeal olmasa da Visual Studio Code (VSC) veya Sublime Text gibi bir kod editörü seçmek de mümkün. Ancak ben bir yazar olarak Obsidian yazılımını kullanmayı tercih ediyorum. Nasıl kurulacağını ve başlayacağını birlikte görelim.



- Https://obsidian.md/download adresine gidin ve yazılımı indirin: ![github-desktop](assets/7.webp)
- Obsidian'ı yükleyin, yazılımı başlatın, dilinizi seçin ve ardından `Hızlı Başlangıç` seçeneğine tıklayın: ![github-desktop](assets/8.webp)
- Obsidian yazılımına ulaşacaksınız. Şimdilik açık dosyanız yok: ![github-desktop](assets/9.webp)


## Adım 3: Fork PlanB Ağ deposu



- Aşağıdaki Address adresinden PlanB Network veri havuzuna gidin: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Bu sayfadan, pencerenin sağ üst köşesindeki `Fork` düğmesine tıklayın: ![github-desktop](assets/11.webp)
- Oluşturma menüsünde varsayılan ayarları bırakabilirsiniz. Yalnızca geliştirme dalını kopyala` kutusunun işaretli olduğundan emin olun, ardından `Fork Oluştur` düğmesine tıklayın: ![github-desktop](assets/12.webp)
- Daha sonra PlanB Network deposunun kendi Fork'inize ulaşacaksınız: ![github-desktop](assets/13.webp)

Bu Fork, şu anda aynı verileri içermesine rağmen orijinalinden ayrı bir depo oluşturmaktadır. Şimdi bu yeni depo üzerinde çalışacaksınız.


Bir bakıma PlanB Network kaynak deposunun bir kopyasını oluşturduk. Fork'unuz (kopya) ve orijinal depo artık birbirlerinden bağımsız olarak gelişecek. Orijinal depoda, diğer katkıda bulunanlar yeni veriler ekleyebilirken, siz Fork'unuzda kendi değişikliklerinizi yapmaya devam edeceksiniz.

Bu iki depo arasındaki tutarlılığı korumak için, aynı bilgileri almaları amacıyla bunları periyodik olarak senkronize etmek gerekecektir. Değişikliklerinizi kaynak depoya göndermek için **Çekme İsteği** adı verilen bir yöntem kullanacaksınız. Ve kaynak depodaki değişiklikleri Fork'nize entegre etmek için GitHub web Interface'de bulunan **Sync Fork** komutunu kullanacaksınız.

![github-desktop](assets/14.webp)


## Adım 4: Fork'ü Klonlayın



- GitHub Masaüstü yazılımına geri dönün. Şimdiye kadar, Fork'ünüz `Repolarınız` bölümünde görünmelidir. Hemen göremezseniz, listeyi yenilemek için çift ok düğmesini kullanın. Fork'ünüz göründüğünde, seçmek için üzerine tıklayın:

![github-desktop](assets/15.webp)


- Ardından mavi düğmeye tıklayın: `Clone [username]/Bitcoin-educational-content`:

![github-desktop](assets/16.webp)


- Varsayılan yolu koruyun. Onaylamak için mavi `Clone` düğmesine tıklayın:

![github-desktop](assets/17.webp)


- GitHub Desktop Fork'nızı yerel olarak klonlarken bekleyin:

![github-desktop](assets/18.webp)


- Depoyu klonladıktan sonra, yazılım size iki seçenek sunar. İlkini seçmelisiniz: `Ana projeye katkıda bulunmak için`. Bu seçim, gelecekteki çalışmalarınızı yalnızca kişisel Fork'inizin (`[kullanıcı adı]/Bitcoin-educational-content`) bir modifikasyonu olarak değil, ana projeye (`PlanB-Network/Bitcoin-educational-content`) bir katkı olarak sunmanıza olanak tanıyacaktır. Seçenek belirlendikten sonra `Devam Et` seçeneğine tıklayın:

![github-desktop](assets/19.webp)


- GitHub Masaüstünüz artık doğru şekilde yapılandırıldı. Şimdi, yapacağımız değişiklikleri takip etmek için yazılımı arka planda açık bırakabilirsiniz.

![github-desktop](assets/20.webp)

Bu aşamada elde ettiğimiz şey, GitHub'da barındırılan deponuzun yerel bir kopyasının oluşturulmasıdır. Bir hatırlatma olarak, bu depo PlanB Network'ün kaynak deposunun bir Fork'udur. Bu yerel kopyada eğitimler, çeviriler veya düzeltmeler eklemek gibi değişiklikler yapabileceksiniz. Bu değişiklikler yapıldıktan sonra, yerel değişikliklerinizi GitHub'da barındırılan Fork'a göndermek için **Push origin** komutunu kullanacaksınız.


Ayrıca, örneğin PlanB Network deposu ile bir senkronizasyon sırasında Fork'den değişiklikleri alabilirsiniz. Bunun için, değişiklikleri yerel kopyanıza (klonunuza) indirmek için **Fetch origin** komutunu ve ardından bunları çalışmanızla birleştirmek için **Pull origin** komutunu kullanacaksınız. Bu, etkin bir şekilde katkıda bulunurken projenin en son gelişmelerinden haberdar olmanızı sağlar.


![github-desktop](assets/21.webp)

## Adım 5: Yeni bir Obsidian kasası oluşturun



- Obsidian yazılımını açın ve pencerenin sol altındaki küçük kasa simgesine tıklayın:

![github-desktop](assets/22.webp)


- Mevcut bir klasörü kasa olarak açmak için `Aç` düğmesine tıklayın: ![github-desktop](assets/23.webp)
- Dosya gezgininiz açılacaktır. Dosyalarınız arasında `Documents` dizininizde olması gereken `GitHub` başlıklı klasörü bulmanız ve seçmeniz gerekir. Bu yol, 4. adımda belirlediğiniz yola karşılık gelir. Klasörü seçtikten sonra, seçimini onaylayın. Obsidian'da kasanızın oluşturulması daha sonra yazılımın yeni bir sayfasında başlayacaktır:


![github-desktop](assets/24.webp)

-> **Dikkat**, Obsidian'da yeni bir kasa oluştururken `Bitcoin-educational-content` klasörünü seçmemeniz önemlidir. Bunun yerine, üst klasör olan `GitHub`ı seçin. Eğer `Bitcoin-educational-content` klasörünü seçerseniz, yerel Obsidian ayarlarınızı içeren `.obsidian` yapılandırma klasörü otomatik olarak depoya entegre edilecektir. Obsidian yapılandırmalarınızı PlanB Network deposuna aktarmanız gerekmediği için bundan kaçınmak istiyoruz. Bir alternatif `.gitignore` dosyasına `.obsidian` klasörünü eklemektir, ancak bu yöntem aynı zamanda kaynak deponun `.gitignore` dosyasını da değiştirecektir, ki bu arzu edilen bir durum değildir.



- Pencerenin sol tarafında, yerel olarak klonlanmış farklı GitHub depolarınızın bulunduğu dosya ağacını görebilirsiniz.
- Klasör adlarının yanındaki oklara tıklayarak, depoların alt klasörlerine ve belgelerine erişmek için bunları genişletebilirsiniz:

![github-desktop](assets/25.webp)


- Obsidian'ı karanlık moda ayarlamayı unutmayın: "Işık böcekleri çeker" ;)


## Adım 6: Bir Kod Düzenleyici Kurun


Yapacağınız değişikliklerin çoğu Markdown formatındaki (`.md`) dosyalar üzerinde olacaktır. Bu belgeleri düzenlemek için daha önce bahsettiğimiz Obsidian yazılımını kullanabilirsiniz. Ancak, PlanB Network diğer dosya biçimlerini kullanır ve bunlardan bazılarını değiştirmeniz gerekecektir.


Örneğin, yeni bir öğretici oluştururken, öğreticinizin etiketlerini, başlığını ve öğretmen kimliğinizi girmek için bir YAML (`.yml`) dosyası oluşturmanız gerekecektir. Obsidian bu tür dosyaları değiştirme imkanı sunmaz, bu nedenle bir kod düzenleyiciye ihtiyacınız olacaktır.


Bunun için çeşitli seçenekler mevcuttur. Bu değişiklikler için bilgisayarınızın standart not defteri kullanılabilse de, bu çözüm düzgün işler için ideal değildir. VS Code](https://code.visualstudio.com/download) veya [Sublime Text](https://www.sublimetext.com/download) gibi bu amaç için özel olarak tasarlanmış yazılımları seçmenizi tavsiye ederim. Özellikle hafif olan Sublime Text, ihtiyaçlarımız için fazlasıyla yeterli olacaktır.


- Bu yazılım programlarından birini yükleyin ve gelecekteki değişiklikleriniz için bir kenarda tutun. ![github-desktop](assets/26.webp)

Tebrikler! Çalışma ortamınız artık PlanB Network'e katkıda bulunmak için ayarlandı. Şimdi her bir katkı türü için diğer özel eğitimlerimizi keşfedebilirsiniz (çeviri, düzeltme, yazma.


https://planb.network/tutorials/others

..).