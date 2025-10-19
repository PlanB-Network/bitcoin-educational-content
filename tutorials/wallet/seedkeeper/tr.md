---
name: Seedkeeper
description: Wallet Bitcoin cihazımı Seedkeeper akıllı kart ile nasıl yedekleyebilirim?
---

![cover](assets/cover.webp)



Seedkeeper, dijital sırları yönetmek ve korumak için donanım çözümleri konusunda uzmanlaşmış Belçikalı bir şirket olan Satochip tarafından geliştirilen bir akıllı karttır. Bitcoin ekosistemine yönelik akıllı kart yelpazesiyle tanınan Satochip, Seedkeeper'ı Mnemonic ifadelerinin saklanmasına yönelik geleneksel yöntemlere bir alternatif olarak tasarlamıştır.



Somut olarak Seedkeeper, güvenli bir işlemciye ve kurcalamaya dayanıklı belleğe (yani bir "secure element*") sahip çok işlevli, EAL6 sertifikalı bir akıllı kart şeklini alır. Adından da anlaşılacağı gibi, rolü Bitcoin Mnemonic cümlelerini ve şifrelerini şifreli ve korumalı bir şekilde saklamaktır. Seedkeeper ile generate, sırlarınızı doğrudan kartın güvenli bileşenine aktarabilir, düzenleyebilir ve kaydedebilirsiniz.



Bana göre Seedkeeper'ın iki ana kullanım alanı var ve bunları 2 ayrı eğitimde inceleyeceğiz:




- Bitcoin** Mnemonic ifade saklama: 12 veya 24 kelimenizi kağıda yazmak yerine, bunları akıllı karta aktarabilir ve bir PIN kodu ile koruyabilirsiniz.
- Şifre yönetimi**: Seedkeeper uygulaması aracılığıyla generate güçlü şifreler oluşturabilir ve bunları doğrudan akıllı kartta saklayarak size kullanışlı, kullanımı kolay bir çevrimdışı şifre yöneticisi sağlayabilirsiniz.



Teknik olarak Seedkeeper 8192 baytlık bir kapasiteye sahiptir ve bu da en az 50 ayrı sırrı saklamasına olanak tanır (kesin sayı, boyutlarına ve her biriyle ilişkili meta verilere bağlı olacaktır). Seedkeeper'a bir bilgisayara [bağlı bir akıllı kart okuyucu aracılığıyla] (https://satochip.io/accessories/) ya da NFC bağlantılı mobil uygulama aracılığıyla erişilebilir. Tüm sistem internet bağlantısı olmadan çevrimdışı modda çalışarak sınırlı bir saldırı yüzeyini garanti eder.



![Image](assets/fr/001.webp)



Özellikle ilginç bir özellik, bir yedekleme oluşturmak için bir Seedkeeper'ın içeriğini diğerine kopyalama yeteneğidir. Bu eğitimde size tam da bunu nasıl yapacağınızı göstereceğiz.



Seedkeeper, SeedSigner veya Specter DIY gibi durum bilgisi olmayan bir Hardware Wallet ile birleştirildiğinde de çok ilginçtir. Bu durumda, Satochip'in bilgisayarını veya mobil istemcisini kullanmaya gerek yoktur. Seedkeeper seed'ü secure element'de tutuyor ve kağıt QR kodu ihtiyacını ortadan kaldırarak doğrudan imzalama cihazı ile kullanılabiliyor. Bu özel kullanım durumunu bu eğitimde geliştirmeyeceğim, çünkü başka bir özel eğitimin konusu :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Seedkeeper için hangi kullanım durumu?



Bu eğitimde, sadece Bitcoin ile ilgili kullanım durumlarını ele alacağım, çünkü bu eğitimin konusu bu. Başka bir eğitimin konusu olacak olan parola yönetimi işlevselliğine girmeyeceğiz.



Mnemonic cümlesinin basit bir kağıt yedeği ile karşılaştırıldığında, Seedkeeper kullanmanın çeşitli avantajları vardır:





- Hırsızlığa dayanıklı:** Wallet'nızdaki seed'ye açık metin olarak erişilemez. Onu çıkarmak için Seedkeeper PIN kodunu bilmeniz gerekir. Cihazı ele geçiren bir hırsız, bu kod olmadan cihazla hiçbir şey yapamaz.





- Riski iki faktöre yaymak:** güvenliği dijital ve fiziksel faktörler arasında bölebilirsiniz. Örneğin, Seedkeeper PIN'ini parola yöneticinizde saklarsanız, seed'i elde etmek için hem bu yöneticiye erişmeniz hem de akıllı karta fiziksel olarak sahip olmanız gerekir (önemli ölçüde azaltılmış bir saldırı olasılığı).





- Merkezi yönetim:** Seedkeeper, farklı portföylerden birden fazla tohumun yönetimini kolaylaştırır.





- Kolay yedekleme:** şifrelenmiş yedekleri diğer SeedKeeper'lara kopyalamanız yeterlidir.



Bununla birlikte, seed'unuzun basit bir kağıt yedeği ile karşılaştırıldığında bir takım dezavantajları vardır:





- Fiyat:** mütevazı olmasına rağmen (yaklaşık 25 €), yine de bir kağıt yaprağından daha yüksektir.





- Genel amaçlı bir bilgi işlem cihazına bağımlılık:** seed'e girmek ve yönetmek için bir bilgisayar veya akıllı telefon gerekir, bu da Mnemonic'inizin Hardware Wallet'ye göre çok daha geniş bir saldırı yüzeyine sahip bir makineden geçtiği anlamına gelir. İş istasyonu tehlikeye girerse bu bir risk oluşturabilir. Bu nedenle Hardware Wallet'nin seed'ünü saklamak için Seedkeeper kullanılmasını önermiyorum (SeedSigner'da olduğu gibi bilgisayarsız durumsuz kullanım hariç). Hardware Wallet'nin rolü tam olarak seed'ü minimalist, yüksek güvenlikli bir ortamda saklamaktır. seed'ünüzü her zamanki bilgisayarınıza manuel olarak girdiğinizde, artık Hardware Wallet ile sınırlı kalmaz: aynı zamanda birden fazla saldırı vektörüne maruz kalan genel amaçlı bir makinede de son bulur. Bu nedenle Seedkeeper'ı Hot yerine Wallet için kullanmak daha iyidir (SeedSigner / durumsuz Hardware Wallet hariç).





- PIN ile bağlantılı kayıp riski:** seed'nin doğrudan erişilemez olması, kağıt yedeklemenin aksine, gerçekten de fiziksel hırsızlığa karşı koruma sağlar. Ancak her zaman olduğu gibi güvenlik, hırsızlık riski ile kayıp riski arasında bir denge kurmaktır. Yedeklemeniz bir PIN gerektiriyorsa, bu kodun kaybı Mnemonic ifadenizi kurtarmayı ve dolayısıyla bitcoinlerinize erişmeyi imkansız hale getirecektir.



Bu avantajlar ve dezavantajlar ışığında, Seedkeeper'ın en iyi kullanım alanlarının (şifre yöneticisi işlevi dışında), bir yandan telefonunuzda veya bilgisayarınızda zaten bulundukları için **yazılım portföylerinizden** veya Satochip gibi ekransız Donanım Cüzdanlarınızdan tohumları depolamak ve diğer yandan SeedSigner gibi durumsuz bir Hardware Wallet ile birlikte kullanmak olduğunu düşünüyorum.



Seedkeeper için özellikle ilginç bir kullanım alanı da portföylerinizin *Tanımlayıcılarını* güvenli ve güvenilir bir şekilde yedekleme imkanıdır.



## 2. Nasıl bir Seedkeeper alabilirim?



Seedkeeper'ınızı almanın iki ana yolu vardır. Doğrudan Satochip'in resmi mağazasından](https://satochip.io/product/seedkeeper/) veya yetkili bir satıcıdan satın alabilirsiniz. Ancak [Seedkeeper uygulaması açık kaynaklı](https://github.com/Toporin/Seedkeeper-Applet) olduğundan, [boş bir akıllı karta](https://satochip.io/product/blank-javacard-for-diy-project/) kendiniz yükleme seçeneğiniz de vardır.



Seedkeeper'ın yedekleme işlevini kullanmak istiyorsanız, iki akıllı kart satın almanız gerekecektir.



## 3. Seedkeeper istemcisini yükleme



Bu eğitimde, seed portföyümüzü Seedkeeper'ımızda yedekleyeceğiz. İlk adım, yazılımı bilgisayarınıza veya akıllı telefonunuza yüklemektir. Bilgisayarda, [Satochip-Utils'in en son sürümünü indirmeniz] (https://github.com/Toporin/Satochip-Utils/releases) gerekecektir. Seedkeeper uygulaması mobil cihazlarda [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ve [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060)'da mevcuttur.



![Image](assets/fr/002.webp)



## 4. Seedkeeper başlatma



Uygulamayı başlatın ve "*Tıkla ve Tara*" düğmesine tıklayın.



![Image](assets/fr/003.webp)



Seedkeeper'ınız için sizden bir PIN kodu istenecektir. Bu yeni bir kart olduğu için henüz bir PIN kodu tanımlanmamıştır. Bu adımı atlamak için herhangi bir kod girin ve ardından "*Sonraki*" düğmesine tıklayın.



![Image](assets/fr/004.webp)



Ardından kartı akıllı telefonunuzun arkasına yerleştirin. Uygulama Seedkeeper'ın henüz başlatılmadığını tespit edecek ve sizden akıllı kartınızın PIN kodunu 4 ila 16 karakter uzunluğunda ayarlamanızı isteyecektir. Optimum güvenlik için, mümkün olduğunca uzun, rastgele ve çok çeşitli karakterlerden oluşan güçlü bir şifre seçin. Bu PIN kodu, kurtarma ifadenize fiziksel erişime karşı tek engeldir.



**Bu PIN kodunu şimdi kaydetmeyi de unutmayın**, örneğin bir şifre yöneticisinde veya ayrı bir fiziksel ortamda. İkinci durumda, PIN'i içeren ortamı asla Seedkeeper'ınızla aynı yerde tutmayın, aksi takdirde bu güvenlik işe yaramaz hale gelecektir. Güvenilir bir yedeğe sahip olmak önemlidir: PIN olmadan Seedkeeper'ınızda saklanan sırları kurtaramazsınız.



![Image](assets/fr/005.webp)



PIN kodunuzu ikinci kez onaylayın.



![Image](assets/fr/006.webp)



Seedkeeper'ınız şimdi başlatıldı. Yeni ayarladığınız PIN kodunu girerek kilidini açabilirsiniz.



![Image](assets/fr/007.webp)



Şimdi akıllı kart yönetimi sayfanıza yönlendirileceksiniz.



![Image](assets/fr/008.webp)



## 5. Seedkeeper'da bir seed kaydettirin



Seedkeeper'ınızın kilidi açıldıktan sonra "*+*" düğmesine tıklayın.



![Image](assets/fr/009.webp)



"Sırrı içe aktar*" seçeneğini seçin. "*generate secret*" seçeneği, doğrudan uygulama içinden yeni bir Mnemonic ifadesi oluşturmanızı sağlar.



![Image](assets/fr/010.webp)



Bizim durumumuzda, seed'ü portföyümüze kaydetmek istiyoruz. "*Mnemonic*" üzerine tıklayın.



![Image](assets/fr/011.webp)



Bu sırra bir "*Etiket*" atayın, böylece Seedkeeper'ınızda birkaç bilgi parçası depoladığınızda kolayca tanımlanabilir.



![Image](assets/fr/012.webp)



Ardından sağlanan alana kurtarma cümlenizi girin. Dilerseniz bir passphrase BIP39 veya *Tanımlayıcılarınızı* da ekleyebilirsiniz. Ardından "İçe Aktar*" seçeneğine tıklayın.



![Image](assets/fr/013.webp)



*Bu görselde yer alan Mnemonic hayal ürünüdür ve kimseye ait değildir. Bu sadece bir örnektir. Kendi Mnemonic'nızı asla kimseye göstermeyin, aksi takdirde bitcoinleriniz çalınır



Seedkeeper'ınızı akıllı telefonunuzun arkasına yerleştirin.



![Image](assets/fr/014.webp)



seed'niz kaydedildi.



![Image](assets/fr/015.webp)



## 6. Seedkeeper üzerinden seed'inize erişin



Mnemonic ifadenizi kontrol etmek isterseniz, Seedkeeper'ınızı alın ve "*Tıkla ve Tara*" düğmesine tıklayın.



![Image](assets/fr/016.webp)



PIN kodunuzu girin, ardından "*Sonraki*" düğmesine basın.



![Image](assets/fr/017.webp)



Seedkeeper'ınızı akıllı telefonunuzun arkasına yerleştirin.



![Image](assets/fr/018.webp)



Bu sizi tüm kayıtlı gizli dizilerinizin bir listesine götürür. Bu örnekte, portföyümdeki seed'i görüntülemek istiyorum "*BLOCKSTREAM Uygulaması*", bu yüzden üzerine tıklıyorum.



![Image](assets/fr/019.webp)



"*Reveal*" düğmesine basın.



![Image](assets/fr/020.webp)



Seedkeeper'ınızı tekrar tarayın.



![Image](assets/fr/021.webp)



Önceden kaydettiğiniz Mnemonic cümlesi şimdi ekranda görüntülenir.



![Image](assets/fr/022.webp)



## 7. Seedkeeper'ı yedekleme



Şimdi iki kopyaya sahip olmak için Seedkeeper'ımın yedeğini ikinci bir Seedkeeper'da alacağız. Bu yedekleme, bitcoinlerinizi güvence altına alma stratejisinin bir parçası olabilir: örneğin, fiziksel riskleri sınırlamak için ifadenizi iki ayrı yerde saklamak veya miras planının bir parçası olarak bir kopyayı güvenilir bir akrabaya emanet etmek.



Bunu yapmak için, ikinci Seedkeeper'ınızı yanınıza alın (herhangi bir karışıklığı önlemek için ikisinden birini üzerinde bir işaretle tanımlamayı unutmayın). Bu eğitimin 4. adımında açıklandığı gibi onu başlatarak başlayın. Bir kez daha güçlü bir parola seçin. Stratejinize bağlı olarak farklı bir parola seçebilir ya da aynı parolayı kullanabilirsiniz.



![Image](assets/fr/023.webp)



Uygulamayı açın, "*Tıkla ve Tara*" seçeneğine tıklayın, Seedkeeper n°1'inizin (kaynak) şifresini girin ve ardından tarayın.



![Image](assets/fr/024.webp)



Bu sizi sırlarınızın bir listesini içeren ana sayfaya götürür. Interface'ün sağ üst köşesindeki üç küçük noktaya tıklayın.



![Image](assets/fr/025.webp)



"*Yedekleme yap*" öğesini seçin, ardından "*Başlat*" düğmesine basın.



![Image](assets/fr/026.webp)



Yedek kartınızın PIN kodunu girin (Seedkeeper n°2).



![Image](assets/fr/027.webp)



Ardından kartı tarayın.



![Image](assets/fr/028.webp)



Aynı işlemi ana kart (Seedkeeper n°1) için de yapın ve ardından "*Yedek al*" seçeneğine tıklayın.



![Image](assets/fr/029.webp)



Seedkeeper n°2'niz artık Seedkeeper n°1'de saklanan tüm sırları içerir.



![Image](assets/fr/030.webp)



Sırların kopyalanıp kopyalanmadığını kontrol etmek için Seedkeeper n°2'nizi tarayabilirsiniz.



![Image](assets/fr/031.webp)



Hepsi bu kadar! Artık Seedkeeper'ı bir Bitcoin Wallet'nın Mnemonic ifadesini saklamak için nasıl kullanacağınızı biliyorsunuz. Gelecekteki bir eğitimde, Seedkeeper'ı şifrelerinizi saklamak için nasıl kullanacağınıza bakacağız. Ayrıca sizi SeedSigner ile birlikte kullanımını keşfetmeye davet ediyorum:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Bu eğitimde, Bitcoin portföyünüzdeki ***Belirteçler***den birkaç kez bahsettik. Ne olduklarını bilmiyor musunuz? Bu durumda, HD portföylerinin işletilmesinde yer alan tüm mekanizmaları derinlemesine inceleyen ücretsiz CYP 201 eğitim kursumuzu almanızı tavsiye ederim!



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f