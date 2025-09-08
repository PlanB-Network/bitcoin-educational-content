---
name: PayJoin - Samourai Wallet
description: Samourai Wallet üzerinde bir PayJoin işlemi nasıl gerçekleştirilir?
---
![samourai payjoin cover](assets/cover.webp)


***DİKKAT:** Samourai Wallet'in kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Samourai Wallet'teki Payjoins Stowaway, her iki kullanıcının da kendi Dojo'larına bağlı olması koşuluyla, yalnızca ilgili taraflar arasında manuel olarak PSBT alışverişi yaparak çalışır. Sparrow'e gelince, BIP78 üzerinden Payjoins hala çalışıyor. Ancak, bu araçların önümüzdeki haftalarda yeniden kullanıma sunulması mümkündür. Bu arada, Stowaway'in teorik işleyişini anlamak için bu makaleyi okuyabilirsiniz.*


_Eğer bir Kaçak Yolculuğu manuel olarak gerçekleştirmeyi planlıyorsanız, prosedür bu eğitimde anlatılana çok benzer. Temel fark Stowaway işleminin türünün seçiminde yatmaktadır: `Online` seçeneğini seçmek yerine `In Person / Manual` seçeneğine tıklayın. Ardından, Stowaway işlemini oluşturmak için PSBT'leri manuel olarak Exchange yapmanız gerekecektir. İşbirlikçinize fiziksel olarak yakınsanız, QR kodlarını art arda tarayabilirsiniz. Eğer uzaktaysanız, JSON dosyaları güvenli bir iletişim kanalı üzerinden değiş tokuş edilebilir. Eğitimin geri kalanı değişmeden kalır


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *Blockchain casuslarını bildiklerini sandıkları her şeyi yeniden düşünmeye zorlayın.*

PayJoin, ödeme alıcısı ile işbirliği yaparak harcama sırasında kullanıcı gizliliğini artıran özel bir Bitcoin işlem yapısıdır. PayJoin'un kurulumunu ve otomasyonunu kolaylaştıran birkaç uygulama vardır. Bu uygulamalar arasında en bilineni Samourai Wallet ekipleri tarafından geliştirilen Stowaway'dir. Bu eğitim, Samourai Wallet uygulamasını kullanarak bir Stowaway PayJoin işleminin nasıl gerçekleştirileceğini açıklamaktadır.


## Stowaway nasıl çalışır?


Daha önce de belirtildiği gibi, Samourai Wallet "Stowaway" adında bir PayJoin aracı sunmaktadır Bu araca PC'deki Sparrow wallet yazılımı veya Android'deki Samourai Wallet uygulaması aracılığıyla erişilebilir. Bir PayJoin gerçekleştirmek için, aynı zamanda bir işbirlikçi olarak hareket eden alıcının Stowaway ile uyumlu bir yazılım, yani Sparrow veya Samourai kullanması gerekir. Bu iki yazılım birlikte çalışabilir ve bir Sparrow wallet ile bir Samourai Wallet arasında Stowaway işlemine izin verir ve bunun tersi de geçerlidir.


Stowaway, Samourai'nin "Cahoots" olarak adlandırdığı bir işlem kategorisine dayanır Bir Cahoot, esasen birden fazla kullanıcı arasında off-chain bilgi Exchange gerektiren işbirlikçi bir işlemdir. Samourai bugüne kadar iki Cahoots aracı sunmaktadır: Stowaway (Payjoins) ve StonewallX2 (gelecekteki bir makalede inceleyeceğiz).


Cahoots işlemleri, kullanıcılar arasında kısmen imzalanmış işlemlerin değiş tokuşunu içerir. Bu işlem özellikle uzaktan yapıldığında uzun ve zahmetli olabilir. Ancak yine de başka bir kullanıcıyla manuel olarak gerçekleştirilebilir, bu da ortak çalışanlar fiziksel olarak yakınsa uygun olabilir. Pratikte bu, art arda taranacak beş QR kodunun manuel olarak değiştirilmesini içerir.


Uzaktan yapıldığında bu işlem çok karmaşık hale gelmektedir. Samourai, Address'un bu sorununu çözmek için Tor'a dayanan ve "Soroban" adı verilen şifreli bir iletişim protokolü geliştirdi Soroban ile, bir PayJoin için gerekli alışverişler kullanıcı dostu bir Interface'in arkasında otomatikleştirilir. Bu, bu makalede inceleyeceğimiz ikinci yöntemdir.


Bu şifreli alışverişler, Cahoots katılımcıları arasında bir bağlantı kurulmasını ve kimlik doğrulamasını gerektirir. Bu nedenle Soroban iletişimleri kullanıcıların Paynym'lerine dayanmaktadır. Paynym'lere aşina değilseniz, sizi daha fazla ayrıntı için bu makaleye başvurmaya davet ediyorum: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



Basitçe ifade etmek gerekirse, Paynym, şifreli mesajlaşma da dahil olmak üzere çeşitli işlevlere izin veren Wallet'ünüze bağlı benzersiz bir tanımlayıcıdır. Paynym bir tanımlayıcı ve bir robotu temsil eden bir illüstrasyon şeklinde sunulur. İşte benim Testnet'deki bir örneğim: ![paynym samourai Wallet](assets/en/1.webp)


**Özetle:**


- _Payjoin_ = İşbirliğine dayalı işlemlerin özel yapısı;
- _Stowaway_ = Samourai ve Sparrow wallet'te bulunan PayJoin uygulaması;
- _Cahoots_ = Samourai tarafından PayJoin Kaçak Yolcu da dahil olmak üzere tüm işbirlikçi işlem türlerine verilen ad;
- _Soroban_ = Tor üzerinde kurulan ve bir Cahoots işlemi bağlamında diğer kullanıcılarla işbirliğine olanak tanıyan şifreli iletişim protokolü;
- _Paynym_ = Bir Cahoots işlemi gerçekleştirmek için Soroban'da başka bir kullanıcıyla iletişime izin veren bir Wallet'nin benzersiz tanımlayıcısı.


[**-> PayJoin işlemleri ve faydaları hakkında daha fazla bilgi edinin**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Paynym'ler arasında nasıl bağlantı kurulur?


Samourai aracılığıyla uzaktan bir Cahoots işlemi, özellikle de bir PayJoin (Stowaway) gerçekleştirmek için, Paynym'lerini kullanarak işbirliği yapmak istediğiniz kullanıcıyı "Takip Etmek" gerekir. Kaçak yolcu söz konusu olduğunda bu, bitcoin göndermek istediğiniz kişiyi takip etmek anlamına gelir.


**İşte bu bağlantıyı kurmak için gereken prosedür:**


Başlamak için, PayJoin için alıcının Paynym'inin ödeme kodunu almanız gerekir. Samourai Wallet uygulamasında, alıcı ekranın sol üst köşesinde bulunan Paynym simgesine (küçük robot) dokunmalı ve ardından `+...` ile başlayan Paynym takma adına tıklamalıdır. Örneğin, benimki `+namelessmode0aF`. Eğer işbirlikçiniz Sparrow wallet kullanıyorsa, sizi buraya tıklayarak özel eğitimimize başvurmaya davet ediyorum.


![connexion paynym samourai](assets/notext/2.webp)


Ortak çalışanınız daha sonra Paynym sayfasına yönlendirilecektir. Buradan Paynym kimlik bilgilerini sizinle paylaşabilir veya taramanız için QR kodlarını paylaşabilirler. Bunu yapmak için, ekranlarının sağ üst köşesinde bulunan küçük "paylaş" simgesine tıklamaları gerekir.

![partager paynym samourai](assets/en/1.webp)


Kendi tarafınızda, Samourai Wallet uygulamanızı başlatın ve aynı şekilde "PayNyms" menüsüne erişin. Paynym'inizi ilk kez kullanıyorsanız, tanımlayıcıyı edinmeniz gerekecektir.


![demander un paynym](assets/notext/3.webp)


Ardından ekranın sağ alt köşesindeki mavi "+" işaretine tıklayın.

![ajouter paynym collaborateur](assets/notext/4.webp)

Daha sonra `COLLER LE CODE PAIEMENT` seçeneğini seçerek iş ortağınızın ödeme kodunu yapıştırabilir veya `SCANNEZ LE CODE QR` tuşuna basarak QR kodunu taramak için kamerayı açabilirsiniz.![paste paynym identifier](assets/notext/5.webp)


SUIVRE düğmesine tıklayın.

![follow paynym](assets/notext/6.webp)

EVET`e tıklayarak onaylayın.

![confirm follow paynym](assets/notext/7.webp)

Yazılım daha sonra size bir `SE CONNECTER` düğmesi sunacaktır. Eğitimimiz için bu düğmeye tıklamanız gerekli değildir. Bu adım yalnızca BIP47'nin bir parçası olarak diğer Paynym'e ödeme yapmayı planlıyorsanız gereklidir, ki bu bizim eğitimimizle ilgili değildir.

![connect paynym](assets/notext/8.webp)

Alıcının Paynym'i sizin Paynym'iniz tarafından takip edildiğinde, alıcının da sizi takip etmesi için bu işlemi ters yönde tekrarlayın. Daha sonra bir PayJoin gerçekleştirebilirsiniz.


## Samourai Wallet üzerinde bir PayJoin nasıl yapılır?


Bu ön adımları tamamladıysanız, artık PayJoin işlemini gerçekleştirmeye hazırsınız demektir! Bunu yapmak için eğitim videomuzu izleyin:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**Harici kaynaklar:**


- https://docs.samourai.io/en/spend-tools#stowaway.