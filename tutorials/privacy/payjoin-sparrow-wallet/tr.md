---
name: PayJoin - Sparrow wallet
description: Sparrow wallet üzerinde PayJoin işlemi nasıl yapılır?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


_**UYARI:** Samourai Wallet'in kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Samourai Wallet'teki Payjoins Stowaway artık yalnızca her iki kullanıcının da kendi Dojo'larına bağlı olması koşuluyla, ilgili taraflar arasında manuel olarak PSBT alışverişi yaparak çalışmaktadır. Sparrow'e gelince, BIP78 üzerinden Payjoins hala çalışıyor. Ancak, bu araçlar önümüzdeki haftalarda yeniden başlatılabilir. Bu arada, payjoins'in teorik işleyişini anlamak için her zaman bu makaleyi okuyabilirsiniz._


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *Blockchain casuslarını bildiklerini sandıkları her şeyi yeniden düşünmeye zorlayın.*

PayJoin, ödeme alıcısı ile işbirliği yaparak harcama sırasında kullanıcı gizliliğini artıran özel bir Bitcoin işlem yapısıdır. PayJoin'un kurulumunu ve otomasyonunu kolaylaştıran birkaç uygulama vardır. Bu uygulamalar arasında en bilineni Samourai Wallet ekibi tarafından geliştirilen Stowaway'dir. Bu eğitim, Sparrow wallet yazılımını kullanarak bir Stowaway PayJoin işlemi yapma sürecinde size rehberlik etmeyi amaçlamaktadır.


## Stowaway nasıl çalışır?


Daha önce de belirtildiği gibi, Samourai Wallet "Stowaway" adında bir PayJoin aracı sunmaktadır Bu araca PC'deki Sparrow wallet yazılımı veya Android'deki Samourai Wallet uygulaması aracılığıyla erişilebilir. Bir PayJoin gerçekleştirmek için, aynı zamanda bir işbirlikçi olarak hareket eden alıcının Stowaway ile uyumlu bir yazılım, yani Sparrow veya Samourai Wallet kullanması gerekir. Bu iki yazılım birlikte çalışabilir ve bir Sparrow wallet ile bir Samourai Wallet arasında Stowaway işlemlerine izin verir ve bunun tersi de geçerlidir.


Stowaway, Samourai'nin "Cahoots" olarak adlandırdığı bir işlem kategorisine dayanır Bir Cahoot, esasen birden fazla kullanıcı arasında off-chain bilgisi Exchange gerektiren işbirliğine dayalı bir işlemdir. Şu anda Samourai iki Cahoots aracı sunmaktadır: Stowaway (Payjoins) ve StonewallX2 (gelecekteki bir makalede inceleyeceğiz).


Cahoots işlemleri, kullanıcılar arasında kısmen imzalanmış işlemlerin değiş tokuşunu içerir. Bu işlem özellikle uzaktan yapıldığında uzun ve zahmetli olabilir. Bununla birlikte, başka bir kullanıcıyla manuel olarak da yapılabilir, bu da ortak çalışanlar fiziksel olarak yakınsa uygun olabilir. Pratikte bu, art arda taranacak beş QR kodunun manuel olarak değiştirilmesini içerir.


Uzaktan yapıldığında bu işlem çok karmaşık hale gelmektedir. Samourai, Address'un bu sorununu çözmek için Tor'a dayanan ve "Soroban" adı verilen şifreli bir iletişim protokolü geliştirdi Soroban ile bir PayJoin için gerekli alışverişler kullanıcı dostu bir Interface'in arkasında otomatikleştirilir. Bu, bu makalede inceleyeceğimiz ikinci yöntemdir.


Bu şifreli alışverişler, Cahoots katılımcıları arasında bir bağlantı kurulmasını ve kimlik doğrulamasını gerektirir. Soroban iletişimleri kullanıcıların Paynym'lerine dayanır. Paynym'lere aşina değilseniz, sizi daha fazla ayrıntı için bu makaleye başvurmaya davet ediyorum: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

Basitçe ifade etmek gerekirse, Paynym, şifreli mesajlaşma da dahil olmak üzere çeşitli işlevlere izin veren Wallet'ünüze bağlı benzersiz bir tanımlayıcıdır. Paynym bir tanımlayıcı ve bir robotu temsil eden bir illüstrasyon şeklinde sunulur. İşte benim Testnet'teki bir örneğim: ![Paynym Sparrow](assets/en/1.webp)


**Özetle:**



- _Payjoin_ = İşbirliğine dayalı işlemin spesifik yapısı;
- _Stowaway_ = Samourai ve Sparrow wallet'te bulunan PayJoin uygulaması;
- _Cahoots_ = Samourai tarafından PayJoin Kaçak Yolcu da dahil olmak üzere tüm işbirlikçi işlem türlerine verilen ad;
- _Soroban_ = Tor üzerinde kurulan ve bir Cahoots işlemi bağlamında diğer kullanıcılarla işbirliğine olanak tanıyan şifreli iletişim protokolü.
- _Paynym_ = Soroban'da başka bir kullanıcıyla iletişime izin veren bir Wallet'in benzersiz tanımlayıcısı

bir Cahoots işlemi gerçekleştirmek.


[**-> PayJoin işlemleri ve faydaları hakkında daha fazla bilgi edinin**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Paynym'ler arasında nasıl bağlantı kurulur?


Samourai veya Sparrow aracılığıyla uzaktan bir Cahoots işlemi, özellikle de bir PayJoin (Kaçak Yolcu) gerçekleştirmek için, işbirliği yapmayı düşündüğünüz kullanıcıyı Paynym'lerini kullanarak "Takip Etmek" gerekir. Kaçak yolcu söz konusu olduğunda bu, bitcoin göndermek istediğiniz kişiyi takip etmek anlamına gelir.


**İşte bu bağlantıyı kurmak için gereken prosedür:**


İlk olarak, alıcının Paynym tanımlayıcısını edinmeniz gerekir. Bu, takma adları veya ödeme kodları kullanılarak yapılabilir. Bunu yapmak için, alıcının Sparrow wallet'ünden `Araçlar` sekmesini seçin ve ardından `PayNym Göster` seçeneğine tıklayın.

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

Kendi tarafınızda, Sparrow wallet'ünüzü açın ve aynı `Show PayNym` menüsüne erişin. Paynym'inizi ilk kez kullanıyorsanız, `Retrieve PayNym` seçeneğine tıklayarak bir tanımlayıcı edinmeniz gerekecektir.

![Retrieve paynym](assets/notext/3.webp)

Ardından, işbirlikçinizin Paynym tanımlayıcısını (takma adı `+...` veya ödeme kodu `PM...`) `Kişi Bul` kutusuna girin ve ardından `Kişi Ekle` düğmesine tıklayın.

![add contact](assets/notext/4.webp)

Yazılım daha sonra size bir `İletişime Bağlan` düğmesi sunacaktır. Eğitimimiz için bu düğmeye tıklamanız gerekli değildir. Bu adım yalnızca BIP47 bağlamında belirtilen Paynym'e ödeme yapmayı planlıyorsanız gereklidir, bu da eğitimimizle ilgili değildir.


Alıcının Paynym'i sizin Paynym'iniz tarafından takip edildiğinde, bu işlemi ters yönde tekrarlayın, böylece alıcınız da sizi takip eder. Daha sonra bir PayJoin gerçekleştirebilirsiniz.


## Sparrow wallet üzerinde bir PayJoin nasıl gerçekleştirilir?


Bu birkaç ön adımı tamamladıysanız, nihayet PayJoin işlemini gerçekleştirmeye hazırsınız demektir! Bunu yapmak için eğitim videomuzu izleyin:

![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)


**Harici kaynaklar:**



- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.