---
name: Wallet of Satoshi - Kendi Kendine Velayet
description: Bir Wallet of Satoshi portföyünün kendi kendine saklama modunun nasıl yapılandırılacağını öğrenin
---

![cover](assets/cover.webp)



***Anahtarlarınız yoksa, madeni paralarınız da yoktur* bir deyişten daha fazlasıdır, Bitcoin'nin temel bir ilkesidir, yani bitcoinlerinizin kilidini açan **özel anahtarları** kontrol etmiyorsanız, onlara gerçekten sahip değilsiniz demektir.



Birçok kullanıcı genellikle bir **custodial wallet** ile başlar, daha sonra özel anahtarlarını kendilerinin kontrol ettiği bir **self-custodial wallet**'e geçer.


Bu eğitimde, size yeni bir kendi kendine gözetimli wallet'i tanıtmayacağız. Bunun yerine, size ***Wallet of Satoshi*** wallet'lerin yeni bir özelliğini tanıtacağız: **kendi kendine gözetim modu**.



Bu yeni entegrasyonun amacı, kullanıcıların basitlik ve akıcı bir kullanıcı deneyiminden yararlanırken özel anahtarlarının kontrolünü ellerinde tutmalarını sağlamaktır.



Konunun özüne inmeden önce, Wallet of Satoshi (WoS) tarafından sunulan özel kendi kendine saklama modunu incelemek için bir dakikanızı ayıralım.



## Kendi kendine saklama modunun özelliği



WoS'un kendi kendini saklama modunun basitliği ve akışkanlığı, Lightning kanalları açma, düğümleri yönetme karmaşıklığını ortadan kaldırır... Ama bu nasıl mümkün olabilir?



Wallet of Satoshi'nin kendi kendini saklama modu **Spark** tarafından desteklenmektedir. Bu, Lightspark tarafından **statechains** teknolojisi kullanılarak oluşturulan Bitcoin için bir Layer 2 çözümüdür.



Sonuç olarak, işlemlerinizi doğrudan Lightning Network üzerinde gerçekleştirmezsiniz. LN** ağı ile **Spark** arasındaki etkileşimler **atomik takaslar** yoluyla gerçekleşir.



Örneğin, Bob WoS kullanarak bir Lightning faturası ödemek istiyor. satoshi'lerini transfer eder, ancak arka planda bunlar Spark üzerindeki bir **Spark Hizmet Sağlayıcısına (SSP)** yönlendirilir ve bu da Lightning ağında ödemeyi gerçekleştirir.



Tersine, Alice doğrudan WoS portföyünden fon almak ister. Bu durumda, **SSP** sats'i LN aracılığıyla alır ve hemen Alice'ün portföyünü kredilendirir.



Bu nedenle, WoS'un basitliğinden ve akışkanlığından yararlanmak için Spark'ın sunucularına bağlı olmanız gerektiğini belirtmek önemlidir. Bununla birlikte, güvenlik açısından, bir SSP kötü niyetli hale gelirse veya kullanılamaz hale gelirse, Bitcoin on-chain'deki fonlarınızı geri almanıza izin veren bir güvenlik önlemi olan **tek taraflı çıkış** mekanizmasına sahip olursunuz (bu yavaş ve maliyetli olsa bile) ve özel bir Lightning düğümününkiyle karşılaştırılabilir bir kendi kendine gözetim deneyimi garanti eder.



Tüm bu parametreleri göz önünde bulundurarak, WoS'unuzda ne kadar sats bulundurmak istediğinize karar verebilirsiniz.



Wallet of Satoshi'de yeniyseniz, doğal olarak mobil wallet uygulamasını indirmeniz gerekecektir. Ancak, zaten kullanıyorsanız ve **kendi kendine gözetim modunu** nasıl kullanacağınızı öğrenmek istiyorsanız, lütfen doğrudan bu eğitimin **Kendi kendine gözetim modu yapılandırması** bölümüne gidin.



## Wallet of Satoshi ile çalışmaya başlama



Uygulama mağazanıza gidin ve WoS'u indirin.



![screen](assets/fr/03.webp)



İndirme işlemi tamamlandıktan sonra uygulamayı açın ve **Başlat** düğmesine basın.



![screen](assets/fr/04.webp)



Uygulamanın ana arayüzüne yönlendirileceksiniz. Aslında, WoS'a ilk kez eriştiğinizde, portföy zaten işlevseldir ve varsayılan olarak sistematik olarak saklama modunda açılır.



![screen](assets/fr/05.webp)



WoS'u gözetim modunda kullanmak istemeseniz bile, önce yapılandırmanızı öneririz. Bunu yapmak için bu eğiticiye başvurun.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

WoS'umuzun kendi kendini muhafaza etme yapılandırmasına geçelim.



## Kendi kendine saklama modu yapılandırması



Ana arayüzün sağ üst köşesindeki hamburger menüsüne (3 çubuklu simge) tıklayın.



![screen](assets/fr/06.webp)



Ardından, görüntülenen menüde **Open Self Custody Wallet** alt menüsüne tıklayın.



![screen](assets/fr/07.webp)



WoS size hemen *kendi kendine saklama modunun bir kurtarma ifadesiyle birlikte geldiğini söyler. Ayrıca, paranızın güvenliğinden yalnızca siz sorumlusunuz*.



![screen](assets/fr/08.webp)



"**Anladım**" düğmesini (1) işaretleyin, ardından parlak sarı renkte görünen **Kendi Kendine Velayeti Aç Wallet** düğmesine (2) basın.



![screen](assets/fr/09.webp)



### Kendi kendine velayet portföyü oluşturma



Öz Gözetim Wallet** Aç düğmesine tıkladıktan sonra **Yeni Wallet Oluştur** düğmesine tıklayın.



![screen](assets/fr/10.webp)



WoS daha sonra yine aynı uygulama içinde sizin için bir kendi kendine velayet portföyü oluşturacaktır. İstediğiniz zaman **custodial** modu (belirli bölgelerde mevcuttur) ve **self-custodial** modu arasında geçiş yapabileceksiniz.



![screen](assets/fr/11.webp)



Oluşturulduktan sonra, ana WoS kendi kendine saklama arayüzüne yönlendirileceksiniz. Bir WoS saklama portföyünün genel görünümü ve arayüzleri ile bir WoS kendi kendine saklama portföyününkiler arasında hiçbir fark olmadığını fark edeceksiniz.



### Anımsatıcı ifadenizi kaydetme



Ekranın üst kısmında Wallet of Satoshi adı ile hamburger menü arasında bulunan **Anahtar Zinciri + Yedekleme Wallet** simgesine dokunun.



![screen](assets/fr/12.webp)



WoS, 12 kelimenizi (anımsatıcı cümle) kaydetmenin iki farklı yolunu sunar: **Google Drive üzerinden yedekleme** ve **manuel yedekleme**.



En güvenli olan manuel yedeklemeyi önermemize rağmen, Google Drive üzerinden nasıl yedekleme yapacağınızı da göstereceğiz.



#### Google Drive üzerinden yedekleme



Google Drive Yedekleme** düğmesine tıklayın.



![screen](assets/fr/13.webp)



Google Drive ile yedeklemeyi tercih ederseniz, Google hesabınızın ele geçirilme riski yüksektir. Kötü niyetli bir kişi 12 kelimenizi içeren dosyaya erişebilir ve böylece wallet'inize erişim sağlayabilir.



Ekstra bir güvenlik katmanı eklemek için 12 kelimenizi içeren dosyayı şifrelemek üzere bir parola eklemek kesinlikle iyi bir yoldur.



Bu yüzden gelişmiş seçeneklerdeki **Şifre ile şifrele** düğmesini etkinleştirin.



![screen](assets/fr/14.webp)



Görüntülenen yeni arayüzde güçlü bir parola belirleyin ve ardından tekrar onaylayın.



![screen](assets/fr/15.webp)



Bir şifre seçtikten sonra onu unutmamanız veya yazdığınız ortamı kaybetmemeniz gerektiğini unutmamanız önemlidir. Unutur veya kaybederseniz, 12 kelimenize ve dolayısıyla fonlarınıza bir daha asla erişemezsiniz.



Şifrenizi seçtikten sonra, yedekleme için bir Google hesabı seçin, ardından WoS tarafından istenen erişimleri verin.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Birkaç saniye bekle. Bingo! Yedeklemeniz başarıyla tamamlandı.



![screen](assets/fr/18.webp)



İkinci yedekleme yöntemini seçerek her zaman ek bir yedekleme yapma seçeneğiniz vardır: manuel yedekleme.


#### Manuel yedekleme



Manuel yedeklemeyi tercih ederseniz, anımsatıcı ifadenizi güvenli bir şekilde yedeklemek için en iyi uygulamaları araştıran bu eğiticiye başvurmanızı şiddetle tavsiye ederiz, böylece bitcoinlerinize erişiminizi kaybetmezsiniz.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Manuel Yedekleme** düğmesine basın.



![screen](assets/fr/19.webp)



Aşağıdaki arayüzde WoS, manuel yedeklemeye devam etmeden önce dikkate almanız gereken birkaç güvenlik önlemini hatırlatır.



Anladım** düğmesini etkinleştirin ve **Sonraki** düğmesine basın.



![screen](assets/fr/20.webp)



Daha sonra 12 kelimeniz size sunulacaktır. Bunları kaydedin ve ardından **Sonraki** düğmesine tıklayın.



![screen](assets/fr/21.webp)



Bu yeni arayüzde, kelimelere doğru sırayla basın.



![screen](assets/fr/22.webp)



Son olarak, **Sonraki** düğmesine tıklayın. Tebrikler! Yedeklemeniz artık tamamlandı.



![screen](assets/fr/23.webp)



## Öz saklama portföyü restorasyonu



Bir telefon değişikliğinin ardından veya başka bir nedenle WoS self-custody wallet'unuzu kurtarmak veya geri yüklemek istediğinizde izlemeniz gereken adımlar şunlardır.



WoS portföyünü açmak için ana arayüzün sağ üst köşesindeki hamburger menüsüne tıklayın.


Görüntülenen menüde **Open Self Custody Wallet** alt menüsüne tıklayın.


Görüntülenen yeni arayüzde **Mevcut Wallet'i Geri Yükle** düğmesine basın.



![screen](assets/fr/24.webp)



Bir geri yükleme yöntemi seçin ve bir sonraki adıma geçin.



![screen](assets/fr/25.webp)



### Google Drive üzerinden geri yükleme



1. Google Drive'dan Geri Yükle** düğmesine basın.


2. Bir Google hesabı seçin ve WoS'un Google Drive'ınıza kaydedilen kurtarma verilerini almasına izin verin.


3. Ardından 12 kelimenizi içeren dosyadan şifreleme parolanızı girin (tabii ki daha önce tanımladıysanız).


4. Geri yüklemenin etkili olması için birkaç dakika bekleyin ve portföyünüze tekrar erişebileceksiniz.



### Manuel restorasyon



1. Elle Geri Yükle** düğmesine basın.


2. Ardından, her kelimeyi başlangıç numarasının önüne yazarak anımsatıcı ifadenizin 12 kelimesini girin.


3. Geri yüklemenin etkili olması için birkaç dakika bekleyin ve portföyünüze tekrar erişebileceksiniz.




### WoS saklama ve WoS kendi kendine saklama arasında bitcoin transferi



WoS saklama sats'ünüzde bitcoinleriniz (wallet) olduğunda ve bir WoS öz saklama wallet oluşturduğunuzda, fonlarınızı kaybetmezsiniz. Daha da iyisi, bunları kendi saklama portföyünüze aktarabilir veya tam tersini yapabilirsiniz.



Bunu yapmak için :


Yıldırım WoS kendi kendine saklama adresinizi veya oluşturduğunuz bir faturayı kopyalayabilirsiniz.



![screen](assets/fr/26.webp)



Şimdi wallet velayetinizi açın ve **Envoyer** düğmesine basın.



Ardından adresi veya faturayı yapıştırın. İkinci kez **Envoyer** tuşuna basın.



Kendi saklama portföyünüze geri döndüğünüzde fonları gerçekten aldığınızı göreceksiniz.



![screen](assets/fr/27.webp)



## Bitcoin gönderme ve alma



Kendi kendine saklama modunda bitcoin gönderme ve almaya gelince, tıpkı genel bakış ve arayüzler gibi, bunlar da bir WoS saklama wallet aracılığıyla bitcoin gönderip almaktan farklı değildir.



Lütfen Plan₿ Ağında Wallet of Satoshi kullanımına ilişkin temel eğitime bakın.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Artık Wallet of Satoshi'u kendi kendine saklama modunda kendiniz yapılandırabilir ve çalıştırabilirsiniz.



Bu öğreticiyi faydalı bulduysanız, lütfen aşağıya yeşil bir başparmak bırakın. Çok teşekkür ederim!