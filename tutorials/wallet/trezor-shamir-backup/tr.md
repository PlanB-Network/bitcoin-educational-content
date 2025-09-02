---
name: Trezor Shamir Yedekleme
description: Trezor'da tek paylaşımlı ve çok paylaşımlı Mnemonic ifadeleri
---
![cover](assets/cover.webp)



*Resim kredisi: [Trezor.io](https://trezor.io/)*



## Trezor'da yeni yedekleme seçenekleri



Trezor, 2023'ten bu yana ***Tek Paylaşımlı Yedekleme*** adı verilen yeni bir yedekleme formatı sunarak çoğu cüzdanda bulunan klasik BIP39 tabanlı yaklaşımı kademeli olarak değiştiriyor. Geleneksel 12 veya 24 kelimelik Mnemonic cümlelerinin aksine, bu yeni format SatoshiLabs tarafından geliştirilen bir standarttan türetilen 20 kelimelik tek bir cümleye dayanmaktadır: **SLIP39**. Amaç, dağıtılmış bir yedekleme modeline sorunsuz geçişi sağlarken yedekleme sağlamlığını ve okunabilirliğini artırmaktır.



Bu dağıtılmış modele ***Çoklu Paylaşımlı Yedekleme*** denir. Aynı prensibe dayanır, ancak tek bir Mnemonic cümlesi oluşturmak yerine, her biri kendi başına bir Mnemonic cümlesi olan ***shares*** adı verilen birkaç parçaya böler. Wallet'i geri yüklemek için, bu *paylaşımların* belirli bir sayısının (bir *eşik* ile tanımlanır) yeniden birleştirilmesi gerekir. Örneğin, 5'te 3 şemasında, 5'ten herhangi 3 *hisse* Wallet'i geri yükleyecektir. Trezor'un dağıtılmış yedekleme sisteminin Multisig cüzdanlarından farklı olduğunu lütfen unutmayın. Bitcoinlerinizi harcamak için yalnızca Hardware Wallet Trezor'unuz gereklidir. Yalnızca bir imza gereklidir. Dağıtım yalnızca Mnemonic ifadesi, yani yedekleme düzeyinde geçerlidir.



![Image](assets/fr/01.webp)



Bu sistem, bir Multisig veya passphrase BIP39 yönetimiyle ilişkili dezavantajlar olmaksızın Mnemonic ifadesinin tek arıza noktası sorununu çözer. Kurtarma süreci artık tek bir bilgi parçasına değil, eşik sayesinde kayıp toleransının ek faydasıyla birlikte birkaç bilgiye dayanmaktadır.



Tek paylaşımlı Yedekleme* ile bir Wallet oluşturmuş olan kullanıcılar, Wallet'larını taşımak zorunda kalmadan istedikleri zaman *Çok paylaşımlı Yedekleme*'ye geçebilirler. Alıcı adresleri ve hesapları aynı kalacaktır. Çoklu paylaşım* sistemi yalnızca yedeklemeyi etkiler, Wallet'un geri kalanı değişmeden kalır.



Çok Paylaşımlı Yedekleme* Trezor Model T, Safe 3 ve Safe 5'te mevcuttur. Bu özellik Trezor Model One tarafından desteklenmez.



**Önemli not:** Trezor'un *Çoklu paylaşım* sistemi, dağıtım için *Shamir'in Gizli Paylaşım* şemasını kullandığından kriptografik olarak güvenlidir. Klasik bir Mnemonic cümlesini kendiniz bölerek benzer bir sistemi manuel olarak uygulamamanızı şiddetle tavsiye ederiz. Bu, bitcoinlerinizin çalınma ve kaybolma riskini önemli ölçüde artıran kötü bir uygulamadır, bu nedenle bunu yapmayın. Klasik bir Mnemonic cümlesi bütün olarak saklanır.



## Shamir'in SLIP39'daki Gizli Paylaşımı



Trezor'daki *Çoklu paylaşım* yedeklemelerinin altında yatan kriptografik mekanizma *Shamir'in Gizli Paylaşım Şeması* (SSSS)'dır. Prensibi şöyledir: gizli bilgi (bu durumda Wallet'in seed'si) matematiksel bir polinoma dönüştürülür. Daha sonra bu polinomun birkaç noktası hesaplanır ve bunların her biri bir paylaşım haline gelir. Orijinal sır, minimum sayıda nokta (eşik) toplanarak polinom interpolasyonu ile yeniden oluşturulur.



Eşiğin altındaki bir paylaşım sayısından hiçbir gizli bilgi çıkarılamaz, bu da gizli bilginin mükemmel teorik güvenliğini garanti eder. Başka bir deyişle, sınırsız hesaplama gücüne sahip bir saldırgan bile eşiğe ulaşılmadığı takdirde seed'ü tahmin edemez.



SLIP39, seed Wallet'ü dağıtmak için bu şemayı kullanır. Her paylaşım, 1024 kelimelik bir listeden (BIP39 listesinden farklı) oluşturulmuş 20 kelimelik bir cümledir.



## Trezor'da Çok Paylaşımlı Yedekleme Kurulumu



Trezor'da Wallet'nızı oluştururken üç farklı seçeneğiniz vardır:




- 12 veya 24 kelimelik klasik bir BIP39 Mnemonic cümlesi kullanın;
- Tek paylaşımlı bir Mnemonic ifadesi kullanın (SLIP39);
- Çoklu paylaşımda (SLIP39) birden fazla Mnemonic cümlesi yapılandırın.



Tek paylaşımlı bir SLIP39 Mnemonic cümlesini tercih ederseniz, Wallet'ü sıfırlamak zorunda kalmadan daha sonraki bir tarihte Çoklu paylaşıma yükseltebilirsiniz. Öte yandan, klasik bir BIP39 Wallet (12 veya 24 kelimelik ifade) ile başlarsanız, bunu doğrudan bir Çoklu paylaşıma dönüştüremezsiniz. Sıfırdan yeni bir Multi-share Wallet oluşturmanız ve fonlarınızı eski Wallet'ten bir veya daha fazla Bitcoin işlemi yoluyla yenisine aktarmanız gerekecektir. Bu daha karmaşık ve maliyetli bir işlemdir. Bu geçişi yapmak istiyorsanız, seed'ünüzü bir Wallet yazılımına girmek zorunda kalmamak için yeni bir Hardware Wallet Trezor satın almanızı tavsiye ederim.



Bu eğitimde, ilk olarak bir Wallet oluştururken bir Çoklu paylaşımın nasıl kurulacağına bakacağız, daha sonraki bir bölümde ise mevcut bir Wallet'te Tekli paylaşımın bir Çoklu paylaşıma nasıl dönüştürüleceğini göreceğiz.



Cihazınızın ilk kurulumu ile ilgili yardıma ihtiyacınız varsa, her Trezor modeli için ayrıntılı bir eğitimimiz de bulunmaktadır:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Yeni bir Wallet üzerinde



Artık Trezor'unuzun ilk yapılandırmasını tamamladınız ve Wallet'yi oluşturmaya hazırsınız. Trezor Suite'te "*Yeni Wallet* oluştur" düğmesine tıklayın.



![Image](assets/fr/02.webp)



"*Çok Paylaşımlı Yedekleme*" seçeneğini seçin ve ardından "*Wallet Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/03.webp)



Trezor'unuzdaki kullanım koşullarını kabul edin ve Wallet'un oluşturulmasını onaylayın.



![Image](assets/fr/04.webp)



Trezor Suite'te "*Yedeklemeye devam et*" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



Talimatları dikkatlice okuyun, onaylayın ve ardından "*Wallet yedeği oluştur*" seçeneğine tıklayın.



![Image](assets/fr/06.webp)



Mnemonic ifadelerinizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trezor'da, yapılandırmak istediğiniz toplam paylaşım sayısını seçin. En yaygın yapılandırmalar 2-de-3 ve 3-de-5'tir. Bu örnek için, 2-de-3 oluşturacağım, bu yüzden 3 paylaşım seçeceğim. Her paylaşım 20 kelimelik bir Mnemonic ifadesini temsil edecektir.



*Safe 5 kullanıcıları için, ekranda "*Devam etmek için dokunun*" yazsa da, aslında onaylamak için yukarı kaydırmanız gerekecektir



![Image](assets/fr/07.webp)



Ardından eşiği, yani Wallet'e ve içerdiği bitcoinlere yeniden erişim kazanmak için gereken hisse sayısını onaylayın.



![Image](assets/fr/08.webp)



Trezor, rastgele sayı üretecini kullanarak çeşitli paylaşımlarınızı (Mnemonic cümleleri) oluşturacaktır. Bu işlem sırasında izlenmediğinizden emin olun. Ekranda verilen kelimeleri seçtiğiniz fiziksel ortama yazın. Kelimelerin numaralandırılmış ve sıralı olması önemlidir.



Her bir paylaşımı ayrı bir ortama not etmenizi ve birkaçının aynı yerde erişilebilir olmasını önlemek için depolamalarını dikkatlice yönetmenizi öneririm. Örneğin, benimki gibi 3'te 2'lik bir yapılandırma için bir seçenek, bir paylaşımı evimde, diğerini güvendiğim bir arkadaşımda ve sonuncusunu da bir banka kasasında tutmak olabilir. Depolama yerlerinin seçimi kişisel güvenlik stratejinize bağlı olacaktır.



Şu anda hangi paylaşımı görüntülediğinizi ekranın üst kısmında görebilirsiniz.



tabii ki, benim bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**_



![Image](assets/fr/09.webp)



Bir sonraki kelimeye geçmek için ekranın alt kısmına tıklayın. Aşağı kaydırarak geriye doğru gidebilirsiniz. Tüm kelimeleri yazdıktan sonra, bir sonraki paylaşıma geçmek için parmağınızı ekranda tutun ve işlemi tekrarlayın.



![Image](assets/fr/10.webp)



Her paylaşım kaydının sonunda, doğru yazdığınızı teyit etmek için Mnemonic cümlenizdeki kelimeleri seçmeniz istenecektir.



![Image](assets/fr/11.webp)



İşte bu kadar, Çoklu paylaşım seçeneğini kullanarak Wallet'inizi başarıyla yedeklediniz. Şimdi yapılandırma talimatlarının geri kalanıyla devam edebilirsiniz.



### Mevcut tek paylı bir Wallet üzerinde



Halihazırda tek paylaşımlı yedeğe sahip bir Trezor Wallet'iniz varsa (klasik BIP39 ifadesi değil, SLIP39 Mnemonic ifadesi) ve Wallet yedeğinizin kullanılabilirliğini ve güvenliğini artırmak istiyorsanız, bitcoinlerinizi transfer etmek zorunda kalmadan çok paylaşımlı bir sistem kurabilirsiniz.



Bunu yapmak için Hardware Wallet'nizi bağlayın ve kilidini açın. Trezor Suite'te Ayarlar'a gidin.



![Image](assets/fr/12.webp)



"*Cihaz*" sekmesine gidin.



![Image](assets/fr/13.webp)



Ardından "*Çok Paylaşımlı Yedek Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/14.webp)



Talimatları okuyun ve ardından "*Çok Paylaşımlı Yedek Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/15.webp)



Daha sonra Trezor ekranınıza mevcut Mnemonic cümlenizi (tek paylaşımlı) girmeniz gerekir. Sözcük sayısını seçin (varsayılan 20'dir).



![Image](assets/fr/16.webp)



Ardından Trezor'un ekran klavyesini kullanarak mevcut Mnemonic ifadenizin her bir kelimesini girin.



![Image](assets/fr/17.webp)



Daha sonra, önceki bölümde verilen talimatları izleyerek Çok Paylaşımlı Yedeklemenizin yapılandırmasını seçebilirsiniz.



![Image](assets/fr/18.webp)



Çoklu paylaşım Yedeklemenizi oluşturduktan sonra, orijinal Tek paylaşımlı Mnemonic ifadenizle ne yapacağınıza karar vermeniz gerekecektir. Bitcoin Wallet aynı kaldığından, bu tek ifade her zaman ona erişime izin verecektir. Bu, güvenlik stratejinize bağlı olacaktır, ancak genel olarak, Çoklu Paylaşımlı Yedekleme'nin amacı olan bu tek hata noktasını ortadan kaldırmak için bu ifadeyi yok etmeniz önerilir. Yok etmeye karar verirseniz, bunu güvenli bir şekilde yaptığınızdan emin olun, çünkü **bitcoinlerinize hala erişim sağlar**.



Tebrikler, artık Trezor donanım cüzdanlarında Tek paylaşımlı ve Çok paylaşımlı Yedeklemelerin kullanımı konusunda bilgi sahibisiniz. Wallet güvenliğinizi bir adım öteye taşımak istiyorsanız, BIP39 parolaları hakkındaki bu eğitime bir göz atın:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



## Ek kaynaklar





- [SLIP-0039: Mnemonic Kodları için Shamir'in Gizli Paylaşımı](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Trezor'da Çok Paylaşımlı Yedekleme](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir'in gizli paylaşımı] (https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).