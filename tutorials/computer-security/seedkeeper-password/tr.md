---
name: Seedkeeper - Parola Yöneticisi
description: Seedkeeper akıllı kart ile şifrelerinizi nasıl kaydedersiniz?
---

![cover](assets/cover.webp)



Seedkeeper, dijital sırları yönetmek ve korumak için donanım çözümleri konusunda uzmanlaşmış Belçikalı bir şirket olan Satochip tarafından geliştirilen bir akıllı karttır. Bitcoin ekosistemine yönelik akıllı kart yelpazesiyle tanınan Satochip, Seedkeeper'ı anımsatıcı ifadelerin ve diğer dijital sırların saklanmasına yönelik geleneksel yöntemlere bir alternatif olarak tasarlamıştır.



Somut olarak Seedkeeper, güvenli bir işlemciye ve kurcalamaya dayanıklı belleğe ("Güvenli Öğe" olarak adlandırılır) sahip çok işlevli, EAL6 sertifikalı bir akıllı kart şeklini alır. Adından da anlaşılacağı gibi, rolü Bitcoin portföy anımsatıcılarını ve şifrelerini şifreli ve korumalı bir şekilde saklamaktır. Seedkeeper ile generate, sırlarınızı doğrudan kartın güvenli bileşenine aktarabilir, düzenleyebilir ve kaydedebilirsiniz.



Bana göre Seedkeeper'ın iki ana kullanım alanı var ve bunları 2 ayrı eğitimde inceleyeceğiz:




- Bitcoin** anımsatıcı ifade depolama: 12 veya 24 kelimenizi kağıda yazmak yerine, bunları akıllı karta aktarabilir ve bir PIN kodu ile koruyabilirsiniz.
- Şifre yönetimi**: Seedkeeper uygulaması aracılığıyla generate güçlü şifreler oluşturabilir ve bunları doğrudan akıllı kartta saklayarak size kullanışlı, kullanımı kolay bir çevrimdışı şifre yöneticisi sağlayabilirsiniz.



Teknik olarak Seedkeeper 8192 baytlık bir kapasiteye sahiptir ve bu da en az 50 ayrı sırrı saklamasına olanak tanır (kesin sayı, boyutlarına ve her biriyle ilişkili meta verilere bağlı olacaktır). Seedkeeper'a bir bilgisayara [bağlı bir akıllı kart okuyucu aracılığıyla](https://satochip.io/accessories/) ya da NFC bağlantılı mobil uygulama aracılığıyla erişilebilir. Tüm sistem internet bağlantısı olmadan çevrimdışı modda çalışarak sınırlı bir saldırı yüzeyini garanti eder.



![Image](assets/fr/001.webp)



Özellikle ilginç bir özellik, bir yedekleme oluşturmak için bir Seedkeeper'ın içeriğini diğerine kopyalama yeteneğidir. Bu eğitimde size tam da bunu nasıl yapacağınızı göstereceğiz.



Bu eğitimde, SeedKeeper'ın yalnızca geleneksel parolalar için, bir parola yöneticisi tarzında kullanımını ele alacağız. SeedKeeper'ı Bitcoin wallet anımsatıcı cümlelerini kaydetmek için kullanmak isterseniz, lütfen bu diğer eğitime bakın:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Nasıl bir Seedkeeper alabilirim?



Seedkeeper'ınızı almanın iki ana yolu vardır. Doğrudan Satochip'in resmi mağazasından](https://satochip.io/product/seedkeeper/) veya yetkili bir satıcıdan satın alabilirsiniz. Ancak [Seedkeeper uygulaması açık kaynaklı](https://github.com/Toporin/Seedkeeper-Applet) olduğundan, [boş bir akıllı karta](https://satochip.io/product/blank-javacard-for-diy-project/) kendiniz yükleme seçeneğiniz de vardır.



Seedkeeper'ın yedekleme işlevini kullanmak istiyorsanız, iki akıllı kart satın almanız gerekecektir.



## 2. Seedkeeper istemcisini yükleme



İlk adım, yazılımı bilgisayarınıza veya akıllı telefonunuza yüklemektir. Bir bilgisayarda, [Satochip-Utils'in en son sürümünü indirmeniz](https://github.com/Toporin/Satochip-Utils/releases) gerekir. Cep telefonlarında, Seedkeeper uygulaması [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ve [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060)'da mevcuttur.



![Image](assets/fr/002.webp)



## 3. Seedkeeper başlatma



Uygulamayı başlatın ve "*Tıkla ve Tara*" düğmesine tıklayın.



![Image](assets/fr/003.webp)



Seedkeeper'ınız için sizden bir PIN kodu istenecektir. Bu yeni bir kart olduğu için henüz bir PIN kodu tanımlanmamıştır. Bu adımı atlamak için herhangi bir kod girin ve ardından "*Sonraki*" düğmesine tıklayın.



![Image](assets/fr/004.webp)



Ardından kartı akıllı telefonunuzun arkasına yerleştirin. Uygulama Seedkeeper'ın henüz başlatılmadığını tespit edecek ve sizden akıllı kartınızın PIN kodunu 4 ila 16 karakter uzunluğunda ayarlamanızı isteyecektir. Optimum güvenlik için, mümkün olduğunca uzun, rastgele ve çok çeşitli karakterlerden oluşan sağlam bir PIN kodu seçin. Bu PIN kodu, şifrelerinize fiziksel erişime karşı tek engeldir.



**Bu PIN kodunu şimdi kaydetmeyi de unutmayın**, örneğin bir şifre yöneticisinde veya ayrı bir fiziksel ortamda. İkinci durumda, PIN'i içeren ortamı asla Seedkeeper'ınızla aynı yerde tutmayın, aksi takdirde bu güvenlik işe yaramaz hale gelecektir. Güvenilir bir yedeğe sahip olmak önemlidir: PIN olmadan Seedkeeper'ınızda saklanan sırları kurtaramazsınız.



![Image](assets/fr/005.webp)



PIN kodunuzu ikinci kez onaylayın.



![Image](assets/fr/006.webp)



Seedkeeper'ınız şimdi başlatıldı. Yeni ayarladığınız PIN kodunu girerek kilidini açabilirsiniz.



![Image](assets/fr/007.webp)



Şimdi akıllı kart yönetimi sayfanıza yönlendirileceksiniz.



![Image](assets/fr/008.webp)



## 4. Şifreleri Seedkeeper'a kaydedin



Seedkeeper'ınızın kilidi açıldıktan sonra "*+*" düğmesine tıklayın.



![Image](assets/fr/009.webp)



"Generate secret*" seçeneğini seçin. "*Bir sırrı içe aktar*" seçeneği mevcut bir sırrı (örneğin, geçmişte oluşturduğunuz bir parolayı) kaydetmenize olanak tanır.



![Image](assets/fr/010.webp)



Bizim durumumuzda, bir şifre kaydetmek istiyoruz. "*Parola*" üzerine tıklayın.



![Image](assets/fr/011.webp)



Bu sırra bir "*Etiket*" atayın, böylece Seedkeeper'ınızda birkaç bilgi parçası saklıyorsanız kolayca tanımlanabilir. Ayrıca parola ve sitenin URL'si ile ilişkili bir tanımlayıcı da ekleyebilirsiniz.



![Image](assets/fr/012.webp)



Parolanızın uzunluğunu ve parametrelerini seçin, ardından "*Generate*", ardından "*Import*" seçeneğine tıklayın.



![Image](assets/fr/013.webp)



Seedkeeper'ınızı akıllı telefonunuzun arkasına yerleştirin.



![Image](assets/fr/014.webp)



Şifreniz kaydedildi.



![Image](assets/fr/015.webp)



## 5. Seedkeeper şifrenize erişin



Şifrenizi kontrol etmek istiyorsanız, Seedkeeper'ınızı alın ve "*Tıkla ve Tara*" düğmesine tıklayın.



![Image](assets/fr/016.webp)



PIN kodunuzu girin, ardından "*Sonraki*" düğmesine basın.



![Image](assets/fr/017.webp)



Seedkeeper'ınızı akıllı telefonunuzun arkasına yerleştirin.



![Image](assets/fr/018.webp)



Bu sizi tüm kayıtlı gizli parolalarınızın bir listesine götürür. Bu örnekte, Plan ₿ Academy hesabımın şifresini görüntülemek istiyorum, bu yüzden üzerine tıklıyorum.



![Image](assets/fr/019.webp)



"*Reveal*" düğmesine basın.



![Image](assets/fr/020.webp)



Seedkeeper'ınızı tekrar tarayın.



![Image](assets/fr/021.webp)



Önceden kaydettiğiniz parolanız şimdi ekranda görünür. Bunu kopyalayabilir ve ilgili web sitesinde kullanabilirsiniz.



![Image](assets/fr/022.webp)



## 6. Seedkeeper'ı yedekleme



Şimdi Seedkeeper'ımın yedeğini ikinci bir Seedkeeper'a alacağız, böylece iki kopyamız olacak. Bu yedekleme, en önemli parolalarınızı güvence altına alma stratejisinin bir parçası olabilir: örneğin, fiziksel riskleri sınırlamak için Seedkeeper'larınızı 2 ayrı yerde saklamak veya bir kopyasını güvendiğiniz bir akrabanıza emanet etmek.



Bunu yapmak için, ikinci Seedkeeper'ınızı yanınıza alın (herhangi bir karışıklığı önlemek için ikisinden birini üzerinde bir işaretle tanımlamayı unutmayın). Bu eğitimin 3. adımında açıklandığı gibi onu başlatarak başlayın. Bir kez daha güçlü bir PIN kodu seçin. Stratejinize bağlı olarak farklı bir PIN kodu seçebilir ya da aynı PIN kodunu kullanabilirsiniz.



![Image](assets/fr/023.webp)



Uygulamayı açın, "*Tıkla ve Tara*" seçeneğine tıklayın, Seedkeeper n°1'inizin (kaynak) PIN kodunu girin ve ardından tarayın.



![Image](assets/fr/024.webp)



Bu sizi sırlarınızın bir listesini içeren ana sayfaya götürür. Arayüzün sağ üst köşesindeki üç küçük noktaya tıklayın.



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



Hepsi bu kadar! Artık Seedkeeper'ı şifrelerinizi saklamak için nasıl kullanacağınızı biliyorsunuz. Gelecekteki bir eğitimde, Seedkeeper'ı bir Bitcoin wallet'i yedeklemek için nasıl kullanacağımıza bakacağız. Ayrıca sizi SeedSigner ile birlikte kullanımını keşfetmeye davet ediyorum:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356