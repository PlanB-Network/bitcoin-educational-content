---
name: BIP-39 Passphrase Ledger
description: Ledger Wallet'ünüze bir passphrase nasıl eklenir?
---
![cover](assets/cover.webp)


BIP39 passphrase, Mnemonic ifadenizle birleştirildiğinde deterministik ve hiyerarşik Bitcoin cüzdanları için ek bir Layer güvenlik sağlayan isteğe bağlı bir paroladır. Bu eğitimde, bir Ledger'de (modelden bağımsız olarak) güvenli Bitcoin Wallet'unuzda bir passphrase'in nasıl kurulacağını birlikte inceleyeceğiz.


Bu eğitime başlamadan önce, passphrase kavramına, nasıl çalıştığına ve Bitcoin Wallet'ünüz üzerindeki etkilerine aşina değilseniz, her şeyi açıkladığım bu diğer teorik makaleye başvurmanızı şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## passphrase bir Ledger üzerinde nasıl çalışır?


Ledger cihazlarıyla, Wallet'inizde bir passphrase yapılandırmak için iki farklı seçeneğiniz vardır: "*PIN-tied*" seçeneği ve "*temporary*" seçeneği.


"*PIN-tied*" seçeneği ile bir passphrase'u Ledger'nizdeki ikinci bir PIN ile ilişkilendirirsiniz. Bu, 2 PIN'iniz olacağı anlamına gelir: biri passphrase olmadan normal Wallet'inize erişmek için, diğeri ise passphrase tarafından korunan ikinci Wallet'inize erişmek için.


![PASSPHRASE BIP39](assets/notext/03.webp)


Temel olarak, bu passphrase seçeneği ikinci PIN'e bağlı olsa bile, passphrase'niz passphrase'niz olarak kalır. Bu, Ledger'ünüzü kaybederseniz ve bitcoinlerinizi başka bir cihaz veya yazılımda kurtarmak isterseniz, 24 kelimelik ifadenize ve **tam passphrase'nize** kesinlikle ihtiyacınız olacağı anlamına gelir. passphrase ile ilişkili PIN yalnızca mevcut Ledger'ünüze erişmek için kullanılır, ancak diğer Defterlerde veya diğer yazılımlarda çalışmaz. Bu nedenle passphrase'nizi fiziksel bir ortamda tamamen yedeklemeniz önemlidir. **İkincil PIN kodunu bilmek Wallet'ünüze** yeniden erişim sağlamak için tek başına yeterli değildir; bu sadece Ledger'ünüzdeki bir kolaylık özelliğidir.


Bu ikinci PIN seçeneği özellikle fiziksel saldırılarla başa çıkmak için ilginçtir. Örneğin, bir saldırgan paranızı çalmak için sizi cihazınızın kilidini açmaya zorlarsa, ana paranızı ikinci PIN'in arkasında güvende tutarken, az miktarda bitcoin içeren sahte bir Wallet'e erişmek için ilk PIN'i kullanabilirsiniz.


Ayrıca bu seçenek, imzalama cihazınızı her kullandığınızda manuel olarak girmek zorunda kalmadan BIP39 passphrase'nın tüm güvenlik avantajlarını sunar. Bu, uzun ve rastgele bir passphrase kullanmanıza olanak tanır, böylece kaba kuvvet saldırılarına karşı korumayı güçlendirirken, cihazın küçük düğmelerine her seferinde manuel olarak yazmak zorunda kalmanın zorluğundan kaçınır.

"Geçici passphrase" seçeneği passphrase'yi cihazda saklamaz. Korumalı Wallet'unuza her erişmek istediğinizde, passphrase'yi Ledger'e manuel olarak girmeniz gerekecektir. Bu, kullanımı daha zahmetli hale getirir ancak aynı zamanda cihazda passphrase'nin izini bırakmayarak güvenliği biraz artırır. Cihazı kapattığınız anda, cihaz varsayılan durumuna geri döner ve gizli hesaplara erişmek için passphrase'nin tamamının yeniden girilmesini gerektirir. Bu "geçici passphrase" seçeneği bu nedenle diğer donanım cüzdanlarının çalışmasına benzer.

Bu eğitimde örnek olarak Ledger Flex'i kullanacağım. Ancak, başka bir Ledger modeli kullanıyorsanız, işlem aynı kalır. Ledger Stax için Interface, Ledger Flex ile aynıdır. Nano S, Nano S Plus ve Nano X modellerinde ise Interface farklı olsa da işlem ve menülerin isimleri aynı kalır.


**Dikkat:** passphrase'yi etkinleştirmeden önce Ledger'ünüzde zaten bitcoin aldıysanız, bunları bir Bitcoin işlemi yoluyla aktarmanız gerekecektir. passphrase bir dizi yeni anahtar üretir, böylece ilk Wallet'inizden tamamen bağımsız bir Wallet oluşturur. passphrase'yi eklediğinizde, boş olacak yeni bir Wallet'e sahip olacaksınız. Ancak bu, passphrase'si olmayan ilk Wallet'inizi silmez. passphrase'yi girmeden doğrudan Ledger'ünüz aracılığıyla veya 24 kelimelik ifadenizi kullanarak başka bir yazılım aracılığıyla hala erişebilirsiniz.


Bu eğitime başlamadan önce, Ledger'nizi zaten başlattığınızdan ve Mnemonic ifadenizi oluşturduğunuzdan emin olun. Durum böyle değilse ve Ledger'niz yeniyse, PlanB Network'te bulunan modelinize özel öğreticiyi izleyin. Bu adım tamamlandığında, bu eğitime geri dönebilirsiniz.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Bir Ledger ile geçici bir passphrase nasıl kurulur?


Ledger'ınızın ana sayfasında ayarlar dişli çarkına tıklayın.


![PASSPHRASE BIP39](assets/notext/04.webp)


"Gelişmiş" menüsünü ve ardından "passphrase'i Ayarla "yı seçin.


![PASSPHRASE BIP39](assets/notext/05.webp)


Bu, önceki bölümde bahsettiğimiz "PIN'e bağlı" seçeneği veya "geçici" seçeneği arasında seçim yapabileceğiniz adımdır. Burada, geçici bir passphrase'nin nasıl kurulacağını açıklayacağım, bu nedenle "Geçici passphrase'yi ayarla" seçeneğine tıklayın.


![PASSPHRASE BIP39](assets/notext/06.webp)

Daha sonra sizden passphrase'ünüzü girmeniz istenir. Güçlü bir passphrase seçin ve hemen kağıt veya metal gibi bir ortam üzerinde fiziksel bir yedeklemeye geçin. Bu örnekte ben passphrase'ü seçtim: `fH3&kL@9mP#2sD5qR!82`. passphrase'ünüzü girdikten sonra "*Devam*" düğmesine tıklayın.

![PASSPHRASE BIP39](assets/notext/07.webp)


passphrase'ünüzün fiziksel yedeklemenizde not ettiklerinizle eşleştiğini doğrulayın, ardından onaylamak için "*Evet, doğru*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/08.webp)


passphrase'inizin oluşturulmasını tamamlamak için Ledger'nızın PIN kodunu girin. Şu andan itibaren, Wallet'nize passphrase ile Ledger üzerinden erişmek istediğinizde, burada açıklanan adımların aynısını izlemeniz gerekecektir.


![PASSPHRASE BIP39](assets/notext/09.webp)


Artık Wallet'inizi yönetmek için Sparrow wallet'deki açık anahtar setinizi içe aktarabilirsiniz. Sparrow'de bu, passphrase olmadan ilk Wallet'inizden farklı bir Wallet'e karşılık gelecektir.


Sparrow wallet'yi açın. Yazılımın bir düğüme bağlı olduğundan emin olun, ardından "*Dosya*" sekmesine tıklayın ve "*Yeni Wallet*"ü seçin.


![PASSPHRASE BIP39](assets/notext/10.webp)


Bir passphrase tarafından korunan Wallet'iniz için bir isim seçin. Bu örnek için, açıkça "*passphrase*" terimini içeren bir isim seçtim. Ancak, bu Wallet'in gizliliğini bilgisayarınızda tutmayı tercih ediyorsanız, daha az çağrıştırıcı bir isim seçebilirsiniz.


![PASSPHRASE BIP39](assets/notext/11.webp)


Wallet'iniz için komut dosyası türünü seçin. "*Taproot*" veya alternatif olarak "*Native SegWit*" seçmenizi tavsiye ederim.


![PASSPHRASE BIP39](assets/notext/12.webp)


Ledger'nizi bilgisayarınıza bağlayın, ardından "*Bağlı Hardware Wallet*" üzerine tıklayın. passphrase'ınızı Ledger'nize zaten girmiş olduğunuzdan emin olun. Değilse, lütfen passphrase'ınızı girmek için önceki adımlara geri dönün. Taramaya geçmeden önce, Ledger'nizde "*Bitcoin*" uygulamasını açmayı da unutmayın.


![PASSPHRASE BIP39](assets/notext/13.webp)


"*Tarama...*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/14.webp)


Ledger'ünüzün yanındaki "*Anahtar Deposunu Aktar*" seçeneğine tıklayın.


![PASSPHRASE BIP39](assets/notext/15.webp)


passphrase tarafından korunan Wallet'nız artık Sparrow üzerinde oluşturulmuştur. Onaylamak için "*Uygula*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/16.webp)

Sparrow wallet'ye erişimi güvence altına almak için güçlü bir parola seçin. Bu parola, Sparrow üzerindeki Wallet verilerinize erişimin güvenliğini sağlayarak genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi herhangi bir yetkisiz erişime karşı korumaya yardımcı olur.

Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.


![PASSPHRASE BIP39](assets/notext/17.webp)


Ve işte, Wallet'iniz artık oluşturuldu! "*Ayarlar*" menüsünde, Sparrow size "*Ana parmak izinizi*" sağlayacaktır. Bu, Wallet'inizi türetmek için temel olarak kullanılan ana anahtarınızın parmak izini temsil eder. Bu parmak izinin bir kopyasını saklamanızı şiddetle tavsiye ederim. Benim örneğimde buna karşılık geliyor: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/18.webp)


Önceki bölümlerde bahsettiklerimizi hatırlayın: passphrase'nizi girerken yapacağınız küçük bir hata bile generate'ün farklı anahtarlara sahip tamamen yeni bir Wallet olmasını sağlayacaktır. Doğru passphrase ile doğru Wallet'e eriştiğinizden emin olmanız gereken her seferde, ana anahtarınızın parmak izinin not ettiğinizle eşleşip eşleşmediğini kontrol edin. Bu bilgi, tek başına, fonlarınızın güvenliği veya gizliliğiniz için hiçbir risk oluşturmaz.


Wallet'nizi bir passphrase ile kullanmadan önce, bir kuru çalıştırma kurtarma testi yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ana anahtarınızın parmak izi gibi referans bir bilgiyi not edin, ardından Wallet hala boşken Ledger'nızı sıfırlayın. Ardından, 24 kelimelik cümlenin ve passphrase'in kağıt yedeklerini kullanarak Wallet'nizi Ledger'ya geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan bilgilerin başlangıçta not ettiklerinizle eşleşip eşleşmediğini kontrol edin. Eğer durum buysa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


## Ledger ile bir PIN'e bağlı bir passphrase nasıl kurulur?


Ledger'inizin ana sayfasında ayarlar dişli çarkına tıklayın.


![PASSPHRASE BIP39](assets/notext/19.webp)


"*Gelişmiş*" menüsünü ve ardından "*passphrase*'i Ayarla "yı seçin.


![PASSPHRASE BIP39](assets/notext/20.webp)


Bu, önceki bölümde bahsettiğimiz "*PIN'e bağlı*" veya "*geçici*" seçeneği arasında seçim yapabileceğiniz adımdır. Burada, bir PIN'e bağlı bir passphrase'nin nasıl kurulacağını açıklayacağım, bu nedenle "*passphrase'yi ayarlayın ve yeni bir PIN'e ekleyin*" seçeneğine tıklayın.


![PASSPHRASE BIP39](assets/notext/21.webp)

Daha sonra passphrase'ünüzle ilişkilendirilecek PIN kodunu seçmelisiniz. Tıpkı ana PIN kodunda olduğu gibi, mümkün olduğunca rastgele 8 haneli bir PIN kodu seçmeniz önerilir. Ayrıca, bu kodu Ledger Flex'inizin depolandığı yerden farklı bir yere kaydettiğinizden emin olun.

Benim durumumda, ana PIN kodu `58293647` ve passphrase ile ilişkili ikincil PIN kodu olarak `71425839` seçtim.


![PASSPHRASE BIP39](assets/notext/22.webp)


Daha sonra sizden passphrase'nızı girmeniz istenir. Güçlü bir passphrase seçin ve hemen kağıt veya metal gibi bir ortam üzerinde fiziksel bir yedeklemeye geçin. Bu örnekte ben passphrase'yı seçtim: `fH3&kL@9mP#2sD5qR!82`. passphrase'nızı girdikten sonra "*Devam*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/23.webp)


passphrase'nizin fiziksel yedeklemenizde not ettiklerinizle eşleştiğini doğrulayın, ardından onaylamak için "*Evet, doğru*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/24.webp)


passphrase'inizin oluşturulmasını tamamlamak için, Ledger'unuzun ana PIN kodunu girin (passphrase ile ilişkili olanı değil).


![PASSPHRASE BIP39](assets/notext/25.webp)


Şu andan itibaren, Wallet'nize passphrase ile Ledger üzerinden erişmek istediğinizde, ana PIN kodunu değil, ikincil PIN kodunu girmeniz gerekecektir:


- Ana PIN kodu (`58293647`) > passphrase olmadan Wallet.
- İkincil PIN kodu (`71425839`) > passphrase ile Wallet.


Artık Wallet'ünüzü yönetmek için Sparrow wallet'deki açık anahtar setinizi içe aktarabilirsiniz. Sparrow'da bu, passphrase olmadan ilk Wallet'ünüzden farklı bir Wallet'e karşılık gelecektir.


Sparrow wallet'i açın. Yazılımın bir düğüme bağlı olduğundan emin olun, ardından "*Dosya*" sekmesine tıklayın ve "*Yeni Wallet*"yi seçin.


![PASSPHRASE BIP39](assets/notext/26.webp)


passphrase tarafından korunan Wallet'ünüz için bir isim seçin. Bu örnek için, açıkça "*passphrase*" terimini içeren bir isim seçtim. Ancak, bu Wallet'ün gizliliğini bilgisayarınızda tutmayı tercih ediyorsanız, daha az çağrıştırıcı bir isim seçebilirsiniz.


![PASSPHRASE BIP39](assets/notext/27.webp)


Wallet'niz için komut dosyası türünü seçin. "*Taproot*" veya bu mümkün değilse "*Native SegWit*" seçmenizi tavsiye ederim.


![PASSPHRASE BIP39](assets/notext/28.webp)

Ledger'inizi bilgisayarınıza bağlayın, ardından "*Bağlı Hardware Wallet*" üzerine tıklayın. İkincil PIN koduyla kilidini açarak Ledger'inizde passphrase'unuzun zaten bulunduğundan emin olun. Değilse, Ledger'inizi yeniden başlatın ve passphrase ile ilişkili PIN kodunu girin. Taramaya geçmeden önce, Ledger cihazınızda "*Bitcoin*" uygulamasını açmayı da unutmayın.


![PASSPHRASE BIP39](assets/notext/29.webp)


"*Tarama...*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/30.webp)


"*Anahtar Deposunu Aktar*" üzerine tıklayın.


![PASSPHRASE BIP39](assets/notext/31.webp)


passphrase tarafından korunan Wallet'ünüz artık Sparrow üzerinde oluşturulmuştur. Onaylamak için "*Uygula*" düğmesine tıklayın.


![PASSPHRASE BIP39](assets/notext/32.webp)


Sparrow wallet'e erişimi güvence altına almak için güçlü bir parola seçin. Bu parola, Sparrow üzerindeki Wallet verilerinize erişimin güvenliğini sağlayacak ve genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi herhangi bir yetkisiz erişime karşı korumaya yardımcı olacaktır.


Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.


![PASSPHRASE BIP39](assets/notext/33.webp)


Ve işte, Wallet'unuz artık oluşturuldu! "*Ayarlar*" menüsünde, Sparrow size "*Ana parmak izinizi*" sağlayacaktır. Bu, Wallet'unuzun türetilmesinde temel olarak kullanılan ana anahtarınızın parmak izini temsil eder. Bu parmak izinin bir kopyasını saklamanızı şiddetle tavsiye ederim. Benim örneğimde buna karşılık geliyor: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/34.webp)


Önceki bölümlerde bahsettiklerimizi hatırlayın: passphrase'nizi girerken yapacağınız küçük bir hata bile generate'in farklı anahtarlarla tamamen yeni bir Wallet olmasını sağlayacaktır. Doğru passphrase ile doğru Wallet'ye erişim sağlamanız gerektiğinde, ana anahtarınızın parmak izinin not ettiğinizle eşleştiğini doğrulayın. Bu bilgi, tek başına, fonlarınızın güvenliği veya gizliliğiniz için hiçbir risk oluşturmaz.

Wallet'inizi bir passphrase ile kullanmadan önce, bir kuru çalıştırma kurtarma testi yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ana anahtarınızın parmak izi gibi referans bir bilgiyi not edin, ardından Wallet hala boşken Ledger'ünüzü sıfırlayın. Ardından, 24 kelimelik cümlenin ve passphrase'ün kağıt yedeklerini kullanarak Wallet'inizi Ledger'e geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan bilgilerin başlangıçta not ettiklerinizle eşleşip eşleşmediğini kontrol edin. Eğer durum buysa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


Tebrikler, Bitcoin Wallet'iniz artık bir passphrase ile sabitlendi! Bu eğitimi faydalı bulduysanız, aşağıya bir beğeni bırakırsanız çok memnun olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca Ledger Flex'inizi nasıl kullanacağınıza dair bu diğer eksiksiz eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a