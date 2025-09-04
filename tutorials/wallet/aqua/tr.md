---
name: Aqua
description: Bitcoin, Lightning ve Liquid tek bir Wallet içinde
---
![cover](assets/cover.webp)


Aqua, Bitcoin ve Liquid için bir Hot Wallet oluşturmayı kolaylaştıran ve ayrıca entegre takaslar sayesinde bir düğümü yönetmenin karmaşıklığı olmadan Lightning kullanma imkanı sunan bir mobil uygulamadır. Ayrıca USDT sabit coinlerinin çeşitli ağlarda yönetilmesini sağlar.


Samson Mow yönetimindeki JAN3 şirketi tarafından geliştirilen Aqua uygulaması, dünya çapındaki tüm kullanıcılar için uygun olmasına rağmen, başlangıçta özellikle Latin Amerika'daki kullanıcıların ihtiyaçları için tasarlanmıştır. Özellikle yeni başlayanlar ve ödemeleri için günlük olarak Bitcoin kullananlar için ilgi çekicidir.


Bu eğitimde, Aqua'ün birçok özelliğini nasıl kullanacağımızı öğreneceğiz. Ancak bunu yapmadan önce, Sidechain'in Bitcoin'de ne olduğunu ve Liquid'ün nasıl çalıştığını anlamak için bir dakikanızı ayıralım, böylece Aqua'ün değerini tam olarak kavrayabiliriz.


![AQUA](assets/fr/01.webp)


## Sidechain nedir?


Bitcoin protokolü, ağın ademi merkeziyetçiliğini korumaya ve güvenliğin tüm kullanıcılar arasında dağıtılmasını sağlamaya yardımcı olan kasıtlı teknik sınırlamalara sahiptir. Ancak bu sınırlamalar, özellikle yüksek hacimli eşzamanlı işlemlerden kaynaklanan tıkanıklık sırasında bazen kullanıcıları hayal kırıklığına uğratabilir. Bitcoin'in ölçeklenebilirliği konusundaki tartışmalar, özellikle de Blocksize Savaşı sırasında topluluğu uzun süre bölmüştür. Bu olaydan bu yana, Bitcoin topluluğu içinde ölçeklenebilirliğin ikinci Layer sistemlerinde off-chain çözümleri ile sağlanması gerektiği yaygın olarak kabul görmektedir. Bu çözümler, Lightning Network gibi diğer sistemlere kıyasla hala nispeten bilinmeyen ve az kullanılan yan zincirleri içermektedir.


Bir Sidechain, ana Bitcoin Blockchain ile paralel olarak çalışan bağımsız bir Blockchain'dir. "*two-way peg*" adı verilen bir mekanizma sayesinde Bitcoin'yi hesap birimi olarak kullanır. Bu sistem, bitcoinleri ana zincirde kilitleyerek değerlerini Sidechain'de yeniden üretmeyi mümkün kılar ve burada orijinal bitcoinler tarafından desteklenen tokenlar şeklinde dolaşırlar. Bu tokenlar normalde ana zincirde kilitli bitcoinlerle değer eşitliğini korur ve Bitcoin'deki fonları kurtarmak için süreç tersine çevrilebilir.


Yan zincirlerin amacı, daha hızlı işlemler, daha düşük ücretler veya akıllı sözleşmeler için destek gibi ek işlevler veya teknik iyileştirmeler sunmaktır. Bu yenilikler, merkeziyetsizlik veya güvenlikten ödün vermeden her zaman doğrudan Bitcoin Blockchain üzerinde uygulanamaz. Bu nedenle yan zincirler, Bitcoin'ün bütünlüğünü korurken yeni çözümleri test etmeyi ve keşfetmeyi mümkün kılar. Ancak bu protokoller, seçilen yönetişim modeli ve mutabakat mekanizmasına bağlı olarak, özellikle ademi merkeziyetçilik ve güvenlik açısından sıklıkla taviz verilmesini gerektirmektedir.


## Liquid nedir?


Liquid, Blockstream tarafından işlem hızını, gizliliğini ve işlevselliğini artırmak için geliştirilen, Bitcoin için birleştirilmiş bir Sidechain kaplamasıdır. Bitcoinleri ana zincirde kilitlemek ve karşılığında Liquid-bitcoinleri (L-BTC) oluşturmak için bir federasyon üzerinde kurulan iki taraflı bir ankraj mekanizması kullanır, orijinal bitcoinler tarafından desteklenmeye devam ederken Liquid'de dolaşan tokenler.


![AQUA](assets/fr/02.webp)


Liquid Network, blokları doğrulayan ve iki taraflı sabitlemeyi yöneten Bitcoin ekosistemindeki tanınmış kuruluşlardan oluşan bir katılımcı federasyonuna dayanır. L-BTC'ye ek olarak Liquid, USDT stablecoin ve diğer kripto para birimleri gibi diğer dijital varlıkların da ihraç edilmesini sağlar.


![AQUA](assets/fr/03.webp)


## Aqua uygulamasını yükleyin


İlk adım elbette Aqua uygulamasını indirmektir. Uygulama mağazanıza gidin:



- [Android için](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Apple için](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Android kullanıcıları için, uygulamayı `.apk` dosyası [GitHub'da mevcuttur] (https://github.com/AquaWallet/Aqua-Wallet/releases) aracılığıyla yükleme seçeneğiniz de vardır.


![AQUA](assets/fr/05.webp)


Uygulamayı başlatın, ardından "*Hizmet Koşulları ve Gizlilik Politikasını* okudum ve kabul ediyorum" kutusunu işaretleyin.


![AQUA](assets/fr/06.webp)


## Wallet'inizi Aqua üzerinde oluşturun


"*Wallet* Oluştur" düğmesine tıklayın.


![AQUA](assets/fr/07.webp)


Ve işte, Wallet'iniz çoktan oluşturuldu!


![AQUA](assets/fr/08.webp)


Ancak her şeyden önce, bu bir kendi kendine saklama Wallet olduğundan, Mnemonic'nizin fiziksel bir yedeğini almanız zorunludur. **Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu Mnemonic'ye sahip olan herhangi biri, telefonunuza fiziksel erişimi olmasa bile paranızı çalabilir.


Telefonunuzun kaybolması, çalınması veya kırılması durumunda bitcoinlerinize yeniden erişmenizi sağlar. Bu nedenle, fiziksel bir ortama (dijital değil) dikkatlice kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir. Bunu bir kağıda yazabilir veya daha fazla güvenlik için, eğer bu büyük bir Wallet ise, yangın, sel veya çökme riskinden korumak için paslanmaz çelik bir destek üzerine kazımanızı tavsiye ederim (az miktarda bitcoini güvence altına almak için tasarlanmış bir Hot Wallet için, basit bir kağıt yedekleme muhtemelen yeterlidir).


Bunu yapmak için Ayarlar menüsüne tıklayın.


![AQUA](assets/fr/09.webp)


Ardından "*seed İfadesini Görüntüle*" seçeneğine tıklayın. Bu 12 kelimelik ifadenin fiziksel bir yedeğini alın.


![AQUA](assets/fr/10.webp)


Aynı ayarlar menüsünde, uygulama dilini ve kullanılan fiat para birimini de değiştirebilirsiniz.


![AQUA](assets/fr/11.webp)


Wallet'inize ilk bitcoinlerinizi almadan önce **boş kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ilk aldığınız Address gibi bazı referans bilgilerini not edin, ardından Wallet'inizi hala boşken Aqua uygulamasından silin. Ardından kağıt yedeklerinizi kullanarak Wallet'inizi Aqua'a geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan çerez bilgilerinin başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz. Test kurtarma işleminin nasıl gerçekleştirileceği hakkında daha fazla bilgi edinmek için lütfen bu diğer eğitime başvurun:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Bir emülatör kullandığım için ekranımda göremiyorsunuz ama ayarlarda uygulamayı biyometrik kimlik doğrulama sistemiyle kilitleme seçeneğini bulacaksınız. Bu güvenlik özelliğini etkinleştirmenizi şiddetle tavsiye ederim çünkü bu özellik olmadan, kilidi açık telefonunuza erişimi olan herhangi biri bitcoinlerinizi çalabilir. IOS'ta Face ID'yi ya da Android'de parmak izinizi kullanabilirsiniz. Kimlik doğrulama sırasında bu yöntemler başarısız olursa, telefonunuzun PIN kodunu kullanarak uygulamaya erişmeye devam edebilirsiniz.


## Aqua üzerinden bitcoin alın


Artık Wallet'iniz ayarlandığına göre, ilk Sats'nizi almaya hazırsınız! "*Wallet*" menüsündeki "*Receive*" düğmesine tıklamanız yeterlidir.


![AQUA](assets/fr/12.webp)


Bitcoinleri zincir üzerinde, Liquid üzerinde veya Lightning aracılığıyla almayı seçebilirsiniz.


![AQUA](assets/fr/13.webp)


Zincirleme işlemler için Aqua, generate'ünüzü alabileceğiniz belirli bir alıcı Address'i Sats yapacaktır.


![AQUA](assets/fr/14.webp)


Benzer şekilde, Liquid'u seçtiğinizde, Aqua size bir Liquid Address sağlayacaktır.


![AQUA](assets/fr/15.webp)


Lightning aracılığıyla para almayı tercih ederseniz, öncelikle istediğiniz tutarı belirtmeniz gerekecektir.


![AQUA](assets/fr/16.webp)


Ardından "*generate Invoice*" üzerine tıklayın.


![AQUA](assets/fr/17.webp)


Aqua, Lightning Wallet'ten fon almak için bir Invoice oluşturacaktır. Onchain ve Liquid seçeneklerinin aksine, Lightning aracılığıyla alınan fonların, Aqua bir Lightning düğümü olmadığından, Boltz aracı kullanılarak Liquid'te otomatik olarak L-BTC'ye dönüştürüleceğini lütfen unutmayın. Bu işlem, Bitcoin'lerinizi Lightning'de saklamadan Lightning aracılığıyla para almanıza ve göndermenize olanak tanır.


![AQUA](assets/fr/18.webp)


Şahsen ben Lightning aracılığıyla Aqua'e bitcoin göndererek başlayacağım. İşlem, sağlanan Invoice ile tamamlandıktan sonra bir onay alıyoruz.


![AQUA](assets/fr/19.webp)


Takasın ilerleyişini takip etmek için Wallet'inizin ana sayfasına dönün ve Lightning (takas yoluyla) ve Liquid işlemlerini listeleyen "*L2 Bitcoin*" hesabına tıklayın.


![AQUA](assets/fr/20.webp)


Burada işleminizi ve L-BTC bakiyenizi görüntüleyebilirsiniz.


![AQUA](assets/fr/21.webp)


## Bitcoin'nin Aqua ile değiştirilmesi


Artık Aqua Wallet'nizde varlıklarınız olduğuna göre, bunları ana Bitcoin Blockchain'e veya Liquid'ya aktarmak için doğrudan uygulamadan takas edebilirsiniz. Ayrıca bitcoinlerinizi USDT stablecoin'e (veya diğerlerine) dönüştürebilirsiniz. Bunu yapmak için "*Marketplace*" menüsüne gidin.


![AQUA](assets/fr/22.webp)


"*Swaps*" üzerine tıklayın.


![AQUA](assets/fr/23.webp)


"*Transfer from*" kutusunda, işlem yapmak istediğiniz varlığı seçin. Şu anda yalnızca L-BTC'ye sahibim, bu yüzden onu seçiyorum.


![AQUA](assets/fr/24.webp)


"*Transfer to*" kutusunda, takasınız için hedef varlığı seçin. Ben kendi adıma Liquid Network'da USDT'yi seçtim.


![AQUA](assets/fr/25.webp)


Dönüştürmek istediğiniz tutarı girin.


![AQUA](assets/fr/26.webp)


"*Devam*" üzerine tıklayarak onaylayın.


![AQUA](assets/fr/27.webp)


Takas ayarlarından memnun olduğunuzdan emin olun, ardından ekranın altındaki "*Swap*" düğmesini sürükleyerek onaylayın.


![AQUA](assets/fr/28.webp)


Takas işleminiz şimdi onaylandı.


![AQUA](assets/fr/29.webp)


Wallet'e dönüp baktığımızda, artık Liquid'de USDT'ye sahip olduğumuzu görebiliriz.


![AQUA](assets/fr/30.webp)


## Aqua ile bitcoin gönderin


Artık Aqua Wallet'ünüzde bitcoinler olduğuna göre, onları gönderebilirsiniz. "*Gönder*" düğmesine tıklayın.


![AQUA](assets/fr/31.webp)


Göndermek istediğiniz varlığı seçin veya işlemi gerçekleştirmek için ağı seçin. Ben kendi adıma Lightning üzerinden bitcoin göndereceğim.


![AQUA](assets/fr/32.webp)


Ardından, ödemeyi göndermek için gereken bilgileri girin: onchain veya Liquid bitcoinleri için bir alıcı Address girmeniz gerekir; Lightning için bir Invoice gereklidir. Bu bilgileri doğrudan verilen alana yapıştırabilir veya kameranızı açmak ve Address veya Invoice'yı taramak için QR kodu simgesini kullanabilirsiniz. Ardından "*Devam*" üzerine tıklayın.


![AQUA](assets/fr/33.webp)


Tüm bilgiler doğru görünüyorsa tekrar "*Devam*" düğmesine tıklayın.


![AQUA](assets/fr/34.webp)


Aqua daha sonra size işlemin bir özetini sunar. Hedef Address, ücretler ve tutar dahil olmak üzere tüm bilgilerin doğru olduğundan emin olun. İşlemi onaylamak için ekranın altındaki "*Göndermek için kaydır*" düğmesini kaydırın.


![AQUA](assets/fr/35.webp)


Daha sonra gönderinin onayını alacaksınız.


![AQUA](assets/fr/36.webp)


Artık tek bir Interface'dan Bitcoin, Lightning ve Liquid'de para almak ve harcamak için Aqua uygulamasını nasıl kullanacağınızı biliyorsunuz.


Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca, Liquid Wallet'nizi kurmak için bir başka ilginç çözüm olan Blockstream Green mobil uygulaması hakkındaki bu diğer kapsamlı eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a