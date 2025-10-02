---
name: Trezor Model One
description: Hardware Wallet Model One'ın kurulumu ve kullanımı
---
![cover](assets/cover.webp)



*Resim kredisi: [Trezor.io](https://trezor.io/)*



Trezor Model One, 2014 yılında SatoshiLabs tarafından piyasaya sürülen ilk Hardware Wallet'dir. On yıldan uzun bir süre sonra, özellikle hem teknik hem de bütçe açısından erişilebilir bir Hardware Wallet arayan kullanıcılar için ilginç bir seçim olmaya devam ediyor. Aslında, resmi Trezor web sitesinde 49 € olarak fiyatlandırılmıştır. Bu fiyat aralığındaki tek donanım cüzdanlarından biri. Genellikle ekranı olmayan Tapsigner gibi 20 € civarındaki giriş seviyesi cihazlar ile Ledger Nano S Plus veya Trezor Safe 3 gibi 80 € civarındaki orta sınıf cihazlar arasında yer alıyor.



Model One 0,96 inç monokrom OLED ekrana ve iki fiziksel düğmeye sahiptir. Pil olmadan çalışır, güç ve veri Exchange için yalnızca mikro USB bağlantısı kullanır.



![Image](assets/fr/01.webp)



Model One'ın en büyük dezavantajı secure element'e sahip olmamasıdır, bu da onu çeşitli fiziksel saldırılara karşı savunmasız hale getirmektedir ve bu saldırılardan bazılarının gerçekleştirilmesi nispeten kolaydır. Bu saldırılar, cihaz PIN'ini belirlemek için yardımcı kanalların analizini veya daha sonra kaba kuvvet uygulamak için şifrelenmiş seed'yi çıkarmak için daha gelişmiş teknikleri içerebilir. Bu saldırıların cihaza fiziksel erişim gerektirdiğini unutmayın. Ancak bu güvenlik açığı sağlam bir passphrase BIP39 kullanılarak önemli ölçüde azaltılabilir. Bu Hardware Wallet'ü tercih ederseniz, bir passphrase yapılandırmanızı şiddetle tavsiye ederim.



Model One iki önemli avantaj sunmaktadır:




- Tamamen açık kaynaklı bir mimariye dayanmaktadır. secure element'li daha yeni modellerin aksine, tüm Model One donanım ve yazılım bileşenleri denetlenebilir;
- Bir ekran ile donatılmıştır. Bildiğim kadarıyla bu fiyat aralığında piyasada ekranı olan tek Hardware Wallet bu. Bu çok önemli bir özellik, çünkü imzalı bilgilerin ve alım adreslerinin doğrulanmasını sağlıyor, böylece birçok dijital saldırıyı önlüyor.



Bu nedenle Trezor Model One, sınırlı bir bütçeye sahip yeni başlayanlar ve orta düzey kullanıcılar için akıllıca bir seçim olabilir. Bununla birlikte, secure element'un olmaması nedeniyle fiziksel koruma açısından sınırlamalarının farkında olmak önemlidir. Bütçeniz sınırlıysa, bu iyi bir seçenektir, ancak 79 € 'luk Trezor Safe 3 gibi daha üstün bir modeli seçmeyi göze alabiliyorsanız, secure element içerdiğinden tercih edilebilir.



## Trezor Model One'ın Kutudan Çıkarılması



Model One cihazınızı teslim aldığınızda, paketin açılmadığını teyit etmek için kutunun ve Seal'in sağlam olduğundan emin olun. Cihazın orijinalliği ve bütünlüğüne ilişkin bir yazılım doğrulaması da daha sonra kurulduğunda gerçekleştirilecektir.



Kutu içeriği şunları içerir :




- Trezor Model Bir;
- Mnemonic ifadenizi, çıkartmalarınızı ve talimatlarınızı kaydetmek için kart stoğu;
- USB-A - mikro-USB kablosu.



![Image](assets/fr/02.webp)



Cihazda gezinmek çok basittir:




- Onaylamak ve sonraki adımlara geçmek için sağ tıklayın;
- Geri dönmek için sol düğmeyi kullanın.



## Ön Koşullar



Bu eğitimde, Trezor Model One'ı [Sparrow wallet Wallet yönetim yazılımı] (https://sparrowwallet.com/download/) ile nasıl kullanacağınızı göstereceğim. Bu yazılımı henüz yüklemediyseniz, lütfen şimdi yükleyin. Yardıma ihtiyacınız olursa, Sparrow wallet'ün yapılandırılması hakkında ayrıntılı bir eğitimimiz de var:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Model One'ı yapılandırmak, orijinalliğini kontrol etmek ve aygıt yazılımını yüklemek için Trezor Suite yazılımına da ihtiyacınız olacak. Bu yazılımı yalnızca bunun için kullanacağız ve daha sonra yalnızca aygıt yazılımı güncellemeleri için gerekli olacak. Wallet'in günlük yönetimi için yalnızca Sparrow wallet'i kullanacağız, çünkü Bitcoin için optimize edilmiştir ve yeni başlayanlar için bile kullanımı kolaydır (Sparrow yalnızca Bitcoin'yı destekler, altcoinleri desteklemez).



[Trezor Suite'i resmi web sitesinden indirin](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Bu iki program için de, makinenize yüklemeden önce hem orijinalliklerini (GnuPG ile) hem de bütünlüklerini (Hash ile) kontrol etmenizi şiddetle tavsiye ederim. Bunu nasıl yapacağınızı bilmiyorsanız, bu diğer öğreticiyi takip edebilirsiniz:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Model One'ı Çalıştırma



Model One'ınızı Trezor Suite ve Sparrow wallet'nin zaten yüklü olduğu bilgisayarınıza bağlayın.



![Image](assets/fr/04.webp)



Trezor Suite'i açın, ardından "*Trezor'umu kur*" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



"*Bitcoin-only firmware*" öğesini seçin, ardından "*Install Bitcoin-only*" öğesine tıklayın.



![Image](assets/fr/06.webp)



Trezor Suite daha sonra aygıt yazılımını Model One'ınıza yükleyecektir. Lütfen kurulum sırasında bekleyin.



![Image](assets/fr/07.webp)



"*Devam*" üzerine tıklayın.



![Image](assets/fr/08.webp)



## Bitcoin Wallet Oluşturma



Trezor Suite'te "*Yeni Wallet* oluştur" düğmesine tıklayın.



![Image](assets/fr/09.webp)



Hardware Wallet'in kullanım koşullarını kabul edin.



![Image](assets/fr/10.webp)



Trezor Suite'te "*Yedeklemeye devam et*" seçeneğine tıklayın.



![Image](assets/fr/11.webp)



Yazılım, Mnemonic ifadenizi nasıl yöneteceğinize ilişkin talimatlar sağlar.



Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herhangi biri, Trezor Model One'ınıza fiziksel erişimi olmasa bile paranızı çalabilir.



24 kelimelik ifade, Hardware Wallet'inizin kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde saklamanız ve güvenli bir yerde muhafaza etmeniz çok önemlidir.



Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.



Talimatları onaylayın, ardından "*Wallet yedeği oluştur*" düğmesine tıklayın.



![Image](assets/fr/12.webp)



Model One, rastgele sayı üretecini kullanarak Mnemonic cümlenizi oluşturacaktır. Bu işlem sırasında izlenmediğinizden emin olun. Ekranda verilen kelimeleri seçtiğiniz fiziksel ortama yazın. Güvenlik stratejinize bağlı olarak, ifadenin birkaç tam fiziksel kopyasını çıkarmayı düşünebilirsiniz (ancak her şeyden önce, bölmeyin). Kelimelerin numaralandırılmış ve sıralı olması önemlidir.



**Açıkçası, bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**



Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sonraki kelimelere geçmek için sağ tıklayın. Tüm kelimeleri yazdıktan sonra, bir sonraki adıma geçmek için sağ düğmeye tekrar tıklayın.



![Image](assets/fr/13.webp)



Hardware Wallet'ünüz yine size tüm kelimelerinizi gösterir. Hepsini yazıp yazmadığınızı kontrol edin.



![Image](assets/fr/14.webp)



## PIN kodunun ayarlanması



Ardından PIN kodu adımı gelir. PIN kodu Trezor'unuzun kilidini açar. Bu nedenle yetkisiz fiziksel erişime karşı koruma sağlar. Bu PIN kodu, Wallet'nızın kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, PIN koduna erişiminiz olmasa bile, 12 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.



Trezor Suite'te "*PIN'e Devam Et*" ve ardından "*PIN Ayarla*" düğmesine tıklayın.



![Image](assets/fr/15.webp)



Model 1'i onaylayın.



![Image](assets/fr/16.webp)



Mümkün olduğunca rastgele bir PIN kodu seçmenizi öneririz. Bu kodu Trezor'unuzun kayıtlı olduğu yerden ayrı bir yere kaydettiğinizden emin olun (örneğin bir parola yöneticisine). PIN kodunu 8 ila 50 basamak arasında tanımlayabilirsiniz. Güvenliği artırmak için mümkün olduğunca uzun bir PIN kodu seçmenizi öneririm.



PIN kodu, Trezor Model One'da görüntülenen klavye yapılandırmasına göre rakamlara karşılık gelen noktalara tıklanarak bilgisayarınızdaki Trezor Suite'e girilmelidir.



Bu özel PIN giriş yöntemi, Trezor Suite veya Sparrow wallet aracılığıyla Trezor Model One'ınızın kilidini her açtığınızda gereklidir.



![Image](assets/fr/17.webp)



Bitirdiğinizde, "*PIN Gir*" düğmesine tıklayın.



![Image](assets/fr/18.webp)



Onaylamak için PIN kodunuzu tekrar yazın.



![Image](assets/fr/19.webp)



Trezor Suite'te "*Kurulumu tamamla*" düğmesine tıklayın.



![Image](assets/fr/20.webp)



Model One'ınızın yapılandırması artık tamamlanmıştır. Dilerseniz Hardware Wallet'inizin adını ve ana sayfasını değiştirebilirsiniz.



![Image](assets/fr/21.webp)



Hardware Wallet'unuzda düzenli ürün yazılımı güncellemeleri yapmak veya bir kurtarma testi gerçekleştirmek dışında Trezor Suite yazılımına artık ihtiyacımız olmayacak. Artık Wallet'yi yönetmek için Sparrow'i kullanacağız, çünkü bu yazılım yalnızca Bitcoin kullanımı için mükemmel bir şekilde uygundur.



## Wallet'ün Sparrow wallet üzerinde kurulması



Henüz yapmadıysanız, Sparrow wallet'i [resmi web sitesinden] (https://sparrowwallet.com/) bilgisayarınıza indirip yükleyerek başlayın.



Sparrow wallet'yı açtıktan sonra, yazılımın Interface'nin sağ alt köşesindeki tik işaretiyle gösterilen bir Bitcoin düğümüne bağlı olduğundan emin olun. Sparrow'u bağlamakta sorun yaşıyorsanız, bu eğitimin başına bakmanızı tavsiye ederim:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

"*Dosya*" sekmesine ve ardından "*Yeni Wallet*" seçeneğine tıklayın.



![Image](assets/fr/22.webp)



Wallet'inize bir isim verin ve ardından "*Wallet* Oluştur "a tıklayın.



![Image](assets/fr/23.webp)



"*Script Type*" açılır menüsünde, bitcoinlerinizi güvence altına almak için kullanılacak script türünü seçin. Ben "*Taproot*" ya da bu mümkün değilse "*Native SegWit*" seçeneğini öneririm.



![Image](assets/fr/24.webp)



"*Bağlı Hardware Wallet*" düğmesine tıklayın. Model One'ınız elbette bilgisayara bağlı olmalıdır.



![Image](assets/fr/25.webp)



"*Tarama*" düğmesine tıklayın. Model One'ınız görünmelidir.



Model One'ınızı Sparrow wallet açıkken bir bilgisayara bağladığınızda, Sparrow'de bir passphrase BIP39 girmeniz istenecektir. Bu gelişmiş seçenek gelecekteki bir eğitimde ele alınacaktır. Şimdilik, Trezor'unuzu her başlattığınızda bir passphrase girmenizi istemesini önlemek için "*passphrase'yı Kapat*" seçeneğini seçebilirsiniz.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



"*Anahtar Deposunu Aktar*" üzerine tıklayın.



![Image](assets/fr/27.webp)



Artık ilk hesabınızın genişletilmiş genel anahtarı da dahil olmak üzere Wallet'inizin ayrıntılarını görebilirsiniz. Wallet oluşturma işlemini tamamlamak için "*Uygula*" düğmesine tıklayın.



![Image](assets/fr/28.webp)



Sparrow wallet'a güvenli erişim için güçlü bir parola seçin. Bu parola, Sparrow wallet verilerinize güvenli erişim sağlayarak genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı koruyacaktır.



Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.



![Image](assets/fr/29.webp)



Ve şimdi Wallet'iniz Sparrow wallet'a aktarıldı!



![Image](assets/fr/30.webp)



Wallet'nizdeki ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız gibi bazı referans bilgilerini yazın, ardından Wallet hala boşken Trezor Model One'ınızı sıfırlayın. Ardından kağıt yedeklerinizi kullanarak Wallet'nizi Trezor'a geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan xpub'ın başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.



Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime başvurmanızı öneririm:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Trezor Model One ile bitcoin nasıl alınır?



Sparrow üzerinde, "*Alma*" sekmesine tıklayın.



![Image](assets/fr/31.webp)



Sparrow wallet tarafından önerilen Address'yı kullanmadan önce Trezor'unuzun ekranında kontrol edin. Bu uygulama, Sparrow'de görüntülenen Address'nın sahte olmadığını ve Hardware Wallet'ün daha sonra bu Address ile güvence altına alınan bitcoinleri harcamak için gereken özel anahtarı gerçekten tuttuğunu doğrulamanızı sağlar. Bu, çeşitli saldırı türlerinden kaçınmanıza yardımcı olur.



Bu kontrolü gerçekleştirmek için "*Address'i Göster*" düğmesine tıklayın.



![Image](assets/fr/32.webp)



Trezor'unuzda görüntülenen Address'in Sparrow wallet'daki ile eşleşip eşleşmediğini kontrol edin. Geçerliliğinden emin olmak için Address'inizi göndericiye iletmeden hemen önce bu kontrolü yapmanız da tavsiye edilir. Onaylamak için sağ düğmeye basabilirsiniz.



![Image](assets/fr/33.webp)



Bu Address ile güvence altına alınacak bitcoinlerin kaynağını açıklamak için bir "*Etiket*" de ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenizi sağlayan iyi bir uygulamadır.



![Image](assets/fr/34.webp)



Daha sonra bu Address'yi bitcoin almak için kullanabilirsiniz.



![Image](assets/fr/35.webp)



## Trezor Model One ile bitcoin nasıl gönderilir?



Artık Model One güvenceli Wallet'ünüzdeki ilk Sat'larınızı aldığınıza göre, onları da harcayabilirsiniz! Trezor'unuzu bilgisayarınıza bağlayın, Sparrow wallet'ü başlatın ve ardından yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.



![Image](assets/fr/36.webp)



Eğer *Coin Kontrolü* yapmak istiyorsanız, yani işlemde hangi UTXO'ların kullanılacağını özellikle seçmek istiyorsanız, "*UTXO'lar*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesindeki aynı ekrana yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçilmiş olacak.



![Image](assets/fr/37.webp)



Hedef Address'yı girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.



![Image](assets/fr/38.webp)



Bu masrafın amacını hatırlamak için bir "*Etiket*" yazın.



![Image](assets/fr/39.webp)



Bu Address'ye gönderilecek tutarı seçin.



![Image](assets/fr/40.webp)



İşleminizin ücret oranını mevcut piyasaya göre ayarlayın. Örneğin, uygun bir ücret oranı seçmek için [Mempool.space](https://Mempool.space/) kullanabilirsiniz.



Tüm işlem parametrelerinizin doğru olduğundan emin olun ve ardından "*İşlem Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/41.webp)



Her şey sizi tatmin ediyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.



![Image](assets/fr/42.webp)



"*İmzala*" üzerine tıklayın.



![Image](assets/fr/43.webp)



Trezor Model One'ınızın yanındaki "*İmzala*" düğmesine tıklayın.



![Image](assets/fr/44.webp)



Alıcının alıcı Address'i, gönderilen miktar ve ücret dahil olmak üzere Hardware Wallet ekranınızdaki işlem parametrelerini kontrol edin. İşlem Trezor'da doğrulandıktan sonra imzalamak için sağ tıklayın.



![Image](assets/fr/45.webp)



İşleminiz artık imzalanmıştır. Her şeyin yolunda olup olmadığını son bir kez kontrol edin, ardından Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" düğmesine tıklayın.



![Image](assets/fr/46.webp)



Bunu Sparrow wallet'nin "*İşlemler*" sekmesinde bulabilirsiniz.



![Image](assets/fr/47.webp)



Tebrikler, artık Trezor Model One'ın Sparrow wallet ile temel kullanımını öğrenmiş bulunuyorsunuz! İşleri bir adım öteye taşımak için, güvenliğinizi pekiştirmek amacıyla Hardware Wallet Trezor'u passphrase BIP39 ile kullanma hakkındaki bu kapsamlı öğreticiyi tavsiye ederim:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!