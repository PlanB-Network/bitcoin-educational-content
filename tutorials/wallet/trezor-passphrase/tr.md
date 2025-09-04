---
name: passphrase BIP39 Trezor
description: Trezor Wallet cihazıma nasıl passphrase ekleyebilirim?
---
![cover](assets/cover.webp)



passphrase BIP39, Mnemonic ifadesi ile birlikte deterministik ve hiyerarşik Bitcoin cüzdanları için ek bir Layer güvenlik sağlayan isteğe bağlı bir paroladır. Bu eğitimde, bir Trezor (Safe 3, Safe 5 ve Model One) üzerinde güvenli Bitcoin Wallet'nızda bir passphrase'ün nasıl kurulacağını birlikte keşfedeceğiz.



![Image](assets/fr/01.webp)



Bu eğitime başlamadan önce, passphrase konseptine, nasıl çalıştığına ve Bitcoin Wallet'unuz üzerindeki etkilerine aşina değilseniz, her şeyi açıkladığım bu diğer teorik makaleye başvurmanızı şiddetle tavsiye ederim (bu çok önemlidir, çünkü nasıl çalıştığını tam olarak anlamadan bir passphrase kullanmak bitcoinlerinizi riske atabilir) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Trezor'da passphrase, yapılandırma sırasında BIP39 standardını seçtiyseniz klasik şekilde işlenir (*Çoklu paylaşım Yedeklemeye* ihtiyacınız yoksa bunu öneririm). Trezor'un özelliği, passphrase'yi doğrudan Hardware Wallet üzerinden ya da Trezor Suite yazılımını kullanarak bilgisayarınızın klavyesi üzerinden girebilmenizdir. Bu ikinci seçenek, bilgisayarın Hardware Wallet'den çok daha büyük bir saldırı yüzeyine sahip olması nedeniyle önemli ölçüde daha az güvenlidir. Bununla birlikte, karmaşık bir passphrase'yi yazmak geleneksel bir klavyede Hardware Wallet'den daha hızlı olabilir ve bu da güçlü parolaların kullanılmasını teşvik edebilir. Bu nedenle, yazılması gerekse bile bir passphrase kullanmak, hiç kullanmamaktan her zaman daha iyidir. Bununla birlikte, bunun ima ettiği artan sayısal saldırı riskinin farkında olmak önemlidir.



Bu seçenekler Trezor uyumlu tüm Wallet yönetim yazılımlarında mevcut değildir. Örneğin, Model One için passphrase, Sparrow wallet üzerindeki klavye aracılığıyla girilebilir. Model T, Safe 3 ve Safe 5 modelleri için, Sparrow üzerinden girme seçeneği birkaç yıl önce HWI tarafından devre dışı bırakıldığı için ya Trezor Suite kullanmalı ya da passphrase'i doğrudan Hardware Wallet üzerinden girmelisiniz.



![Image](assets/fr/02.webp)



Trezor Suite'te, passphrase talebini yönetmenin iki farklı yolu vardır. "*Cihaz*" sekmesinde "*passphrase*" seçeneğini etkinleştirebilirsiniz. Etkinleştirilirse, Trezor Suite ve diğer tüm Wallet yönetim yazılımları, her başlattığınızda sistematik olarak passphrase'unuzu girmenizi isteyecektir. passphrase'u kullanmak için daha gizli bir yaklaşım tercih ediyorsanız, ayarı "*Standart*" olarak tutabilirsiniz. Bu durumda, Hardware Wallet'inizin sol üst köşesindeki menüsüne manuel olarak erişmeniz ve her başlattığınızda "*+ passphrase*" düğmesine tıklamanız gerekecektir.



Bu eğitime başlamadan önce, lütfen Trezor'unuzu başlattığınızdan ve Mnemonic cümlenizi oluşturduğunuzdan emin olun. Eğer yapmadıysanız ve Trezor'unuz yeniyse, Plan ₿ Network'de bulunan modele özel öğreticiyi izleyin. Bu adımı tamamladıktan sonra, bu eğitime geri dönebilirsiniz.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Safe 3 veya Safe 5'e bir passphrase ekleme



Wallet'nızı oluşturduktan, Mnemonic'inizi kaydettikten ve bir PIN belirledikten sonra Trezor Suite ana menüsüne yönlendirileceksiniz. Sol üst köşede, sizi passphrase BIP39'u etkinleştirmeye davet eden bir pencere görünmelidir.



![Image](assets/fr/03.webp)



Bu pencere görünmezse, "*Aygıt*" ayarları sekmesinde "*passphrase*" seçeneğini manuel olarak etkinleştirmeniz gerekir.



![Image](assets/fr/04.webp)



Bu pencere sizden passphrase'inizi girmenizi ister. Güçlü bir passphrase seçin ve hemen kağıt veya metal gibi bir ortama fiziksel bir yedekleme yapın. Bu örnekte ben passphrase'i seçtim: `fH3&kL@9mP#2sD5qR!82`. Bu bir örnektir; ancak biraz daha uzun bir passphrase seçmenizi tavsiye ederim. 30 ila 40 karakter arası ideal olacaktır (iyi bir parola gibi).



elbette, bu eğitimde yaptığım gibi passphrase'unuzu asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**_



passphrase seçimine ilişkin daha spesifik öneriler için sizi bir kez daha bu diğer makaleye başvurmaya davet ediyorum:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase'ünüzü bilgisayar klavyeniz aracılığıyla girmek istiyorsanız, verilen alana girin ve ardından "*passphrase Wallet*'e Eriş" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



Hardware Wallet cihazınız daha sonra passphrase cihazınızı görüntüleyecektir. Devam etmek için ekrana tıklamadan önce fiziksel yedeğinizle (kağıt veya metal) eşleştiğinden emin olun.



![Image](assets/fr/06.webp)



Bu size passphrase korumalı Wallet'inize erişim sağlayacaktır.



![Image](assets/fr/07.webp)



passphrase'unuzu yalnızca Trezor'unuza girerek güvenliği artırmayı tercih ediyorsanız, istendiğinde "*passphrase'u Trezor'a Girin*" seçeneğine tıklayın.



![Image](assets/fr/08.webp)



Trezor'unuzda passphrase'ınızı girmenize olanak tanıyan bir T9 klavye belirecektir. Girişinizi tamamladıktan sonra, passphrase'ı Wallet'inize uygulamak için Green onay işaretine tıklayın.



![Image](assets/fr/09.webp)



Daha sonra passphrase güvenli Wallet'ünüze erişiminiz olacaktır.



![Image](assets/fr/10.webp)



Sparrow wallet'yı kullanmak için prosedür benzerdir, ancak T, Safe 3 ve Safe 5 modelleri için passphrase bilgisayar klavyesi üzerinden değil Hardware Wallet üzerinden girilmelidir.



Sparrow wallet Trezor'unuza erişim gerektirdiğinde ve passphrase son başlatmadan bu yana henüz uygulanmadığında, T9 klavyeyi kullanarak girmeniz gerekir.



![Image](assets/fr/11.webp)



## Model One'a bir passphrase ekleme



Model Bir'de passphrase BIP39 kullanımı neredeyse vazgeçilmezdir. Bu cihaz bir secure element içermediğinden, hassas bilgilerin çıkarılması nispeten kolaydır. Bu nedenle fiziksel saldırılara karşı dayanıklı değildir. Ancak, passphrase cihaz kapatıldıktan sonra cihazda tutulmadığından, güçlü (kırılamayan) bir passphrase kullanmak sizi bu modelde bilinen çoğu fiziksel saldırıya karşı koruyabilir.



Model One'da passphrase'ü doğrudan Hardware Wallet'e girmek mümkün değildir. Bilgisayarınızın klavyesi aracılığıyla girmeniz gerekir.



Wallet'nizi oluşturduktan, Mnemonic'nızı kaydettikten ve bir PIN belirledikten sonra Trezor Suite ana menüsüne yönlendirileceksiniz. Sol üst köşede, sizi passphrase BIP39'u etkinleştirmeye davet eden bir pencere görünmelidir.



![Image](assets/fr/12.webp)



Bu pencere görünmezse, ayarların "*Cihaz*" sekmesindeki "*passphrase*" seçeneğini etkinleştirmeniz gerekir.



![Image](assets/fr/13.webp)



Bu pencere sizden passphrase'unuzu girmenizi ister. Güçlü bir passphrase seçin ve hemen kağıt veya metal gibi bir ortama fiziksel bir yedekleme yapın. Bu örnekte ben passphrase'u seçtim: `fH3&kL@9mP#2sD5qR!82`. Bu sadece bir örnek; ancak biraz daha uzun bir passphrase seçmenizi tavsiye ederim. 30 ila 40 karakter arası ideal olacaktır (iyi bir parola gibi).



passphrase'ınızı seçme konusunda daha spesifik öneriler için sizi bir kez daha bu diğer makaleye başvurmaya davet ediyorum:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sağlanan alana passphrase'inizi girin, ardından "*passphrase Wallet*'ye Eriş" düğmesine tıklayın.



![Image](assets/fr/14.webp)



Hardware Wallet cihazınız passphrase cihazınızı görüntüleyecektir. Fiziksel yedeğinizle (kağıt veya metal) eşleştiğinden emin olun, ardından devam etmek için sağdaki düğmeye tıklayın.



![Image](assets/fr/15.webp)



Bu sizi passphrase korumalı Wallet'nıza götürecektir.



![Image](assets/fr/16.webp)



Bundan sonra Sparrow wallet'i kullanmak için prosedür aynı kalır. Sparrow, Hardware Wallet'nize her erişim istediğinde ve cihazın son çalıştırılmasından bu yana passphrase girilmemişse, girmeniz gerekecektir.



![Image](assets/fr/17.webp)



Tebrikler, artık Trezor donanım cüzdanlarında passphrase BIP39'u kullanmaya başladınız. Wallet güvenliğinizi bir adım öteye taşımak istiyorsanız, Trezor'un *Çoklu paylaşım* yedekleme sistemleri (*Şamir'in Gizli Paylaşım Şeması*) hakkındaki bu eğitime göz atın:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!