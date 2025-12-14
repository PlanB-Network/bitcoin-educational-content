---
name: BIP-39 Passphrase SeedSigner
description: SeedSigner portföyüme nasıl passphrase ekleyebilirim?
---

![cover](assets/cover.webp)



passphrase BIP39, anımsatıcı ifade ile birlikte deterministik ve hiyerarşik Bitcoin cüzdanları için ek bir güvenlik katmanı sağlayan isteğe bağlı bir paroladır. Bu eğitimde, bir SeedSigner ile kullanılan Bitcoin wallet'ünüzde bir passphrase'nin nasıl kurulacağını birlikte keşfedeceğiz.



![Image](assets/fr/01.webp)



## Parola eklemeden önce ön koşullar



Bu eğitime başlamadan önce, passphrase konseptine, nasıl çalıştığına ve Bitcoin wallet'niz üzerindeki etkilerine aşina değilseniz, her şeyi açıkladığım bu diğer teorik makaleye başvurmanızı şiddetle tavsiye ederim (bu çok önemlidir, çünkü nasıl çalıştığını tam olarak anlamadan bir passphrase kullanmak bitcoinlerinizi riske atabilir) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Bu eğitime başlamadan önce lütfen SeedSigner'ınızı daha önce başlattığınızdan ve anımsatıcı ifadenizi oluşturduğunuzdan emin olun. Eğer yapmadıysanız ve SeedSigner'ınız yeniyse, Plan ₿ Academy'deki öğreticiyi takip edin. Bu adımı tamamladıktan sonra bu eğitime geri dönebilirsiniz:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## SeedSigner'a nasıl bir passphrase ekleyebilirim?



SeedSigner aracılığıyla yönetilen portföyünüze bir passphrase eklemek tamamen yeni bir portföy oluşturur ve tamamen ayrı bir anahtar seti oluşturur. Sonuç olarak, zaten sats içeren bir portföyünüz varsa, tamamen farklı bir portföy oluşturduğundan, artık passphrase ile buna erişemezsiniz.



SeedSigner'ınıza bir passphrase uygulamak için cihazı açın ve SeedQR'nizi her zamanki gibi tarayın. SeedSigner daha sonra **passphrase'suz** olana karşılık gelen mevcut wallet'inizin parmak izini görüntüleyecektir. passphrase'lu wallet farklı bir parmak izine sahip olacaktır.



BIP-39 Passphrase` düğmesine tıklayın.



![Image](assets/fr/02.webp)



Ardından, ekran klavyesini kullanarak sağlanan alana seçtiğiniz passphrase'ü girin. Bir veya daha fazla fiziksel yedekleme (kağıt veya metal) yaptığınızdan emin olun: bu passphrase'ün kaybı, bitcoinlerinize erişimin kalıcı olarak kaybedilmesine neden olacaktır. **Bir wallet'ü geri yüklemek için hem anımsatıcı hem de passphrase gereklidir ** İkisinden biri kaybolursa, bitcoinleriniz geri alınamaz şekilde bloke olur.



Girişinizi tamamladıktan sonra, SeedSigner'ın sağ alt tarafındaki `KEY3` düğmesine basarak doğrulayın.



![Image](assets/fr/03.webp)



*Bu örnekte passphrase `pba` kullandım. Ancak, sizin durumunuzda, sağlam bir passphrase seçtiğinizden emin olun. Optimum bir passphrase'in nasıl tanımlanacağını öğrenmek için lütfen şu diğer makaleye bakın:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner daha sonra passphrase wallet'nizin yeni parmak izini görüntüler. Bu parmak izinin birkaç kopyasını oluşturun: passphrase ile bir wallet kullanırken önemlidir, çünkü passphrase'yı her girdiğinizde herhangi bir yazım hatası yapmadığınızı ve doğru wallet'ye eriştiğinizi kontrol etmenizi sağlar.



Örneğin, benim durumumda SeedSigner'ı başlatırken yanlışlıkla `pba` yerine passphrase `Pba` yazarsam, küçük harften büyük harfe yapılan bu basit değişiklik, erişmek istediğimden tamamen farklı bir portföyün oluşturulmasına neden olacaktır.



Bu parmak izi wallet'nizin güvenliği veya gizliliği için hiçbir risk oluşturmaz. Anahtarlarınız hakkında kamuya açık veya özel herhangi bir bilgiyi ifşa etmez. Dolayısıyla, anımsatıcı ve passphrase'un aksine, parmak izini dijital bir ortama kaydedebilirsiniz. Bir kopyasını birkaç yerde saklamanızı tavsiye ederim: bir kağıt parçasında, bir şifre yöneticisinde vb.



Parmak izinizi kaydettikten sonra `Bitti` seçeneğine tıklayın.



![Image](assets/fr/04.webp)



Daha sonra klasik bir SeedSigner'da olduğu gibi portföyünüzün tüm işlevlerine erişebilirsiniz.



![Image](assets/fr/05.webp)



Artık anahtar deposunu Sparrow Wallet'e aktarabilir ve wallet'ünüzü normal şekilde kullanabilirsiniz. Her yeniden başlattığınızda, hem SeedQR'nizi taramanız hem de burada yaptığımız gibi klavyeyi kullanarak passphrase'inizi yeniden girmeniz gerekecektir.



wallet'nızı passphrase ile gerçekten kullanmadan önce, tam bir boş kurtarma testi yapmanızı şiddetle tavsiye ederim. Bu, anımsatıcı ifade ve passphrase yedeklerinizin geçerli olduğunu doğrulamanızı sağlayacaktır. Bu kontrolün nasıl yapılacağını öğrenmek için aşağıdaki eğitime bakın:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895