---
name: Tails

description: Tails'i bir USB anahtarına yükleme
---

![image](assets/cover.webp)


Sizi gözetim ve sansüre karşı koruyan taşınabilir ve amnezik bir işletim sistemi.


## Neden Tails yüklü bir USB anahtarınız var?


Tails (https://tails.boum.org/), birlikte kullandığınız bilgisayarda hiçbir iz bırakmayan güvenli bir bilgisayarı her zaman elinizin altında bulundurmanın en kolay yoludur.


Tails'i kullanmak için, erişiminiz olan bilgisayarı kapatın (ailenizde, arkadaşlarınızda, bir İnternet kafede...) ve Windows, macOS veya Linux yerine Tails USB anahtarınızla başlatın.


Bundan sonra, normal işletim sisteminden bağımsız olan ve asla Hard sürücüsünü kullanmayan bir çalışma alanına ve iletişim ortamına sahip olacaksınız.


Tails asla Hard sürücüsüne yazmaz ve çalışmak için yalnızca bilgisayarın RAM'ini kullanır. Tails kapatıldığında bu bellek tamamen silinir, böylece olası tüm izler ortadan kalkar.


## Bazı somut kullanım örnekleri


Tails ile her zaman bir USB anahtarı bulundurmanın faydaları hakkında size somut fikirler vermek için, işte Agora256 ekibi tarafından derlenen kapsamlı olmayan küçük bir liste:



- İz bırakmadan web sitelerinde gezinmek için sansürsüz ve anonim bir şekilde İnternet'e ve Tor'a bağlanın;
- Şüpheli bir web sitesinden PDF açın;
- Bitcoin özel anahtar yedeklemenizi Electrum Wallet ile test edin;
- Bir ofis paketi (LibreOffice) kullanın ve size ait olmayan bir bilgisayarda çalışın;
- Microsoft ve Apple dünyasından nasıl ayrılacağınızı öğrenmek için Linux ortamında ilk adımlarınızı atın.


## Tails'e nasıl güvenebilirim?


Yazılım kullanımında her zaman bir güven unsuru vardır, ancak bunun kör olması gerekmez. Tails gibi bir araç, kullanıcılarına güvenilir olmak için gerekli araçları sağlamaya çalışmalıdır. Tails için bu şu anlama gelir:



- Genel kaynak kodu: https://gitlab.tails.boum.org/;
- Saygın projelere dayanan bir proje: Tor ve Debian;
- Doğrulanabilir ve tekrarlanabilir indirmeler;
- Farklı kişi ve kuruluşlar tarafından yapılan tavsiyeler.


## Kurulum ve kullanım kılavuzu


Bu kurulum kılavuzunun amacı, kurulumun her adımında size rehberlik etmektir. Yapılması gereken işlemleri resmi kılavuzdan daha fazla açıklamayacağız, ancak size ipuçları ve püf noktaları verirken sizi doğru yöne yönlendireceğiz.


Pratik deneyim nedeniyle, bu ipuçları macOS ve Linux platformlarına odaklanacaktır.

🛠️

Bu prosedüre başlamadan önce, lütfen minimum 150 MB/s okuma hızına ve en az 8 GB kapasiteye sahip, ideal olarak USB 3.0 olan bir USB anahtarınız olduğundan emin olun.


Önkoşullar:



- 1 USB anahtarı, yalnızca Tails için, en az 8 GB kapasiteli
- Linux, macOS (veya Windows) ile internete bağlı bir bilgisayar
- İnternet bağlantı hızınıza bağlı olarak, kurulum için ½ saat dahil olmak üzere yaklaşık bir saat boş zaman (1,3 GB dosya indirilecek)


## Adım 1: Tails'i bilgisayarınızdan indirin


![image](assets/1.webp)


🔗 **Resmi Kuyruklar bölümü:** https://tails.boum.org/install/linux/index.fr.html#download


.img uzantılı kurulum dosyasını indirmek İnternet indirme hızınıza bağlı olarak biraz zaman alabilir, bu nedenle önceden plan yapın. Modern ve verimli bir bağlantı ile 5 dakikadan az sürecektir.


Bir sonraki adım için gerekli olacağından, dosyayı İndirilenler gibi bilinen bir klasöre kaydedin.


## Adım 2: İndirme işleminizi doğrulayın


![image](assets/2.webp)


🔗 **Resmi Kuyruklar bölümü:** https://tails.boum.org/install/linux/index.fr.html#verify


İndirmenin doğrulanması, indirmenin Tails geliştiricileri tarafından yapıldığını ve indirme sırasında bozulmadığını veya ele geçirilmediğini garanti eder.


İndirdiğiniz dosyanın beklenen dosya olduğunu PGP kullanarak manuel olarak doğrulamak mümkündür, ancak ileri düzey bilgi olmadan bu doğrulama, indirme sayfasındaki JavaScript doğrulamasıyla aynı güvenlik düzeyini sunarken, çok daha karmaşık ve hatalara açıktır.


Dosyayı doğrulamak için resmi bölümde verilen "İndirme işleminizi seçin..." düğmesini kullanın!


## Adım 3: Tails'i USB anahtarınıza yükleyin


![image](assets/3.webp)


🔗 **Resmi Kuyruklar bölümü:**



- **Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- **macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher ve https://tails.boum.org/install/mac/index.fr.html#install


Tails'i USB anahtarınıza yüklemenin bu adımı, özellikle daha önce hiç yapmadıysanız, tüm kılavuzdaki en zor adımdır. En önemli nokta, işletim sisteminiz için resmi bölümdeki doğru prosedürü seçmektir: Linux ya da macOS.


Araçlar tavsiye edildiği şekilde kurulup hazırlandıktan sonra, .img uzantılı dosya anahtarınıza kopyalanarak (mevcut tüm veriler silinerek) bağımsız olarak "önyüklenebilir" hale getirilebilir.


İyi şanslar! 4. adımda görüşmek üzere.


## Adım 4: Tails USB anahtarınızı yeniden başlatın


![image](assets/4.webp)


🔗 **Resmi Kuyruklar bölümü:** https://tails.boum.org/install/linux/index.en.html#restart


Yeni USB belleğinizi kullanarak bilgisayarlarınızdan birini başlatmanın zamanı geldi. USB bağlantı noktalarından birine takın ve yeniden başlatın!


**Not💡: Çoğu bilgisayar Tails USB çubuğundan otomatik olarak önyükleme yapmaz, ancak önyükleme menüsü tuşuna basarak önyükleme yapılabilecek olası aygıtların listesini görüntüleyebilirsiniz.**


Her zamanki Hard sürücünüz yerine USB belleği seçmenize izin veren önyükleme menüsüne sahip olmanızı sağlamak için hangi tuşa basmanız gerektiğini belirlemek için, burada üreticiye göre kapsamlı olmayan bir liste bulunmaktadır:


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

USB bellek seçildikten sonra, bu yeni önyükleme ekranını görmelisiniz, bu çok iyi bir işarettir, bu yüzden bilgisayarın önyüklemeye devam etmesine izin verin...


![image](assets/5.webp)


## Adım 5: Tails'e Hoş Geldiniz!


![image](assets/6.webp)


🔗 **Resmi Kuyruklar bölümü:** https://tails.boum.org/install/linux/index.en.html#tails


Önyükleme yükleyicisi ve yükleme ekranından bir veya iki dakika sonra Hoş Geldiniz Ekranı görüntülenir.


![image](assets/7.webp)


Karşılama Ekranında, Dil ve Bölge bölümünde dilinizi ve klavye düzeninizi seçin. Start Tails'e tıklayın.


![image](assets/8.webp)


Bilgisayarınız ağınıza bağlı değilse, Wi-Fi olmadan ağınıza bağlanmanıza yardımcı olması için lütfen resmi Tails talimatlarına bakın ("Wi-Fi'nizi test edin" bölümü).


Yerel ağa bağlandıktan sonra, Tor ağına bağlanmanıza yardımcı olmak için Tor Bağlantı sihirbazı görünür.


![image](assets/9.webp)


Anonim olarak gezinmeye başlayabilir, Tails'de bulunan seçenekleri ve yazılımı keşfedebilirsiniz. Keyfinize bakın, USB bellekte hiçbir şey değiştirilmediği için hata yapmak için bolca alanınız var... Bir sonraki yeniden başlatmanızda tüm deneyimlerinizi unutmuş olacaksınız!


## Gelecekteki bir rehberde...


Kendi Tails USB belleğinizle biraz daha deney yaptıktan sonra, başka bir makalede daha gelişmiş konuları inceleyeceğiz, örneğin:



- Bir anahtarı **en son Tails** sürümü ile güncelleyin;
- **Kalıcı depolamayı** yapılandırın ve kullanın;
- **Ek yazılım** yükleyin.


O zamana kadar, her zaman olduğu gibi, herhangi bir sorunuz varsa, bunları Agora256 topluluğu ile paylaşmaktan çekinmeyin. Yarın bugün olduğumuzdan daha iyi olmak için birlikte öğreniyoruz!