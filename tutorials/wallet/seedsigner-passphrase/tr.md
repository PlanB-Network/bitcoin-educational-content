---
name: BIP-39 passphrase SeedSigner
description: SeedSigner portföyüme nasıl passphrase ekleyebilirim?
---

![cover](assets/cover.webp)



passphrase BIP39, Mnemonic ifadesiyle birlikte deterministik ve hiyerarşik Bitcoin cüzdanları için ek bir Layer güvenlik sağlayan isteğe bağlı bir paroladır. Bu eğitimde, bir SeedSigner ile kullanılan Bitcoin Wallet'nızda bir passphrase'ün nasıl kurulacağını birlikte keşfedeceğiz.



![Image](assets/fr/01.webp)



## Bir passphrase eklemeden önce ön koşullar



Bu eğitime başlamadan önce, passphrase konseptine, nasıl çalıştığına ve Bitcoin Wallet'iniz üzerindeki etkilerine aşina değilseniz, her şeyi açıkladığım bu diğer teorik makaleye başvurmanızı şiddetle tavsiye ederim (bu çok önemlidir, çünkü nasıl çalıştığını tam olarak anlamadan bir passphrase kullanmak bitcoinlerinizi riske atabilir) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Bu eğitime başlamadan önce lütfen SeedSigner'ınızı daha önce başlattığınızdan ve Mnemonic cümlenizi oluşturduğunuzdan emin olun. Eğer yapmadıysanız ve SeedSigner'ınız yeniyse, Plan ₿ Academy'deki öğreticiyi takip edin. Bu adımı tamamladıktan sonra bu eğitime geri dönebilirsiniz:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## SeedSigner'a nasıl passphrase ekleyebilirim?



SeedSigner aracılığıyla yönetilen portföyünüze bir passphrase eklemek tamamen yeni bir portföy oluşturur ve tamamen ayrı bir anahtar seti oluşturur. Sonuç olarak, zaten Satss içeren bir portföyünüz varsa, tamamen farklı bir portföy oluşturduğundan artık passphrase ile buna erişemezsiniz.



SeedSigner'ınıza bir passphrase uygulamak için cihazı açın ve SeedQR'nizi her zamanki gibi tarayın. SeedSigner daha sonra mevcut Wallet'nızın **passphrase'siz** olana karşılık gelen parmak izini görüntüleyecektir. passphrase'li Wallet farklı bir parmak izine sahip olacaktır.



BIP-39 passphrase` düğmesine tıklayın.



![Image](assets/fr/02.webp)



Ardından, ekran klavyesini kullanarak sağlanan alana seçtiğiniz passphrase'u girin. Bir veya daha fazla fiziksel yedekleme (kağıt veya metal) yaptığınızdan emin olun: bu passphrase'un kaybı, bitcoinlerinize erişimin kalıcı olarak kaybedilmesine neden olacaktır. **Bir Wallet'i geri yüklemek için hem Mnemonic hem de passphrase gereklidir ** İkisinden biri kaybolursa, bitcoinleriniz geri alınamaz şekilde bloke olur.



Girişinizi tamamladıktan sonra, SeedSigner'ın sağ alt tarafındaki `KEY3` düğmesine basarak doğrulayın.



![Image](assets/fr/03.webp)



*Bu örnekte passphrase `pba` kullandım. Ancak, sizin durumunuzda, sağlam bir passphrase seçtiğinizden emin olun. Optimum bir passphrase'nin nasıl tanımlanacağını öğrenmek için lütfen şu diğer makaleye bakın:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner daha sonra passphrase Wallet'ünüzün yeni parmak izini görüntüler. Bu parmak izinin birkaç kopyasını oluşturun: passphrase ile bir Wallet kullanırken önemlidir, çünkü passphrase'ü her girdiğinizde herhangi bir yazım hatası yapmadığınızı ve doğru Wallet'e eriştiğinizi kontrol etmenizi sağlar.



Örneğin, benim durumumda SeedSigner'ı başlatırken yanlışlıkla `pba` yerine passphrase `Pba` yazarsam, küçük harften büyük harfe yapılan bu basit değişiklik, erişmek istediğimden tamamen farklı bir portföyün oluşturulmasına neden olacaktır.



Bu parmak izi Wallet'inizin güvenliği veya gizliliği için hiçbir risk oluşturmaz. Anahtarlarınız hakkında kamuya açık veya özel herhangi bir bilgiyi ifşa etmez. Mnemonic ve passphrase'nın aksine, parmak izini dijital bir ortama kaydedebilirsiniz. Bir kopyasını birkaç yerde saklamanızı tavsiye ederim: kağıt üzerinde, bir şifre yöneticisinde vb.



Parmak izinizi kaydettikten sonra `Bitti` seçeneğine tıklayın.



![Image](assets/fr/04.webp)



Daha sonra klasik bir SeedSigner'da olduğu gibi portföyünüzün tüm işlevlerine erişebilirsiniz.



![Image](assets/fr/05.webp)



Artık anahtar deposunu Sparrow wallet'a aktarabilir ve Wallet'inizi normal şekilde kullanabilirsiniz. Her yeniden başlattığınızda, hem SeedQR'nizi taramanız hem de burada yaptığımız gibi klavyeyi kullanarak passphrase'unuzu yeniden girmeniz gerekecektir.



Wallet'ünüzü passphrase ile gerçekten kullanmadan önce, tam bir boş kurtarma testi yapmanızı şiddetle tavsiye ederim. Bu, Mnemonic ifadenizin ve passphrase yedeklerinizin geçerli olduğunu doğrulamanızı sağlayacaktır. Bu kontrolün nasıl yapılacağını öğrenmek için aşağıdaki eğitime bakın:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895