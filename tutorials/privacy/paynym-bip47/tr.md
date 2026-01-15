---
name: BIP47 - PayNym
description: Ashigaru'da yeniden kullanılabilir bir ödeme kodu kullanın
---
![cover](assets/cover.webp)



Bitcoin'de yapabileceğiniz en kötü gizlilik hatası adresleri tekrar kullanmaktır. Aynı adres birden fazla ödeme aldığında, bu işlemler birbirine bağlanır ve dünyaya işlemlerinizin bir haritasını sunar. Bu nedenle, her makbuz için her zaman benzersiz bir generate adresi kullanmanız şiddetle tavsiye edilir. Ancak bazı Bitcoin uygulamaları için bu basit bir mesele değildir.



Justus Ranvier tarafından 2015 yılında önerilen BIP47, bu soruna zarif bir yanıt sunmaktadır. BIP, **yeniden kullanılabilir ödeme kodu** kavramını ortaya koymaktadır: bir adresi tekrar kullanmadan neredeyse sınırsız sayıda zincir içi bitcoin ödemesi alınmasını sağlayan benzersiz bir tanımlayıcı. ECDH (*Diffie-Hellman on elliptic curves*) değişimine dayanan bir kriptografik mekanizma sayesinde, aynı koda yapılan her ödeme, gönderen ve alıcı arasındaki ilişkiye özgü boş bir adresle sonuçlanır.



![Image](assets/fr/01.webp)



Bu BIP47 ilkesi, özellikle Samourai Wallet tarafından geliştirilen ve şimdi Ashigaru tarafından devralınan sistem olan **PayNym** tarafından uygulanmaktadır. Bu eğitimde, PayNym'inizi nasıl etkinleştireceğinizi, bir muhabirle ödeme kodlarını nasıl değiştireceğinizi ve bir adresi tekrar kullanmadan işlemleri nasıl gerçekleştireceğinizi inceleyeceğiz.



Burada BIP47'nin ayrıntılı işleyişine girmeyeceğim. Konuyu daha derinlemesine incelemek isterseniz, lütfen BTC 204 eğitim kursumun 6.6 bölümüne bakın.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ön Koşullar



Bu öğreticiyi takip etmek için tek ihtiyacınız olan Ashigaru uygulamasında bir wallet. Uygulamayı nasıl indireceğinizi, doğrulayacağınızı, yükleyeceğinizi veya bir wallet oluşturacağınızı bilmiyorsanız, önce bu eğitime başvurmanızı tavsiye ederim:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## PayNym Talep Edin



İlk adım PayNym'inizi talep etmektir. Bu işlemin wallet başına yalnızca bir kez gerçekleştirilmesi gerekir. seed'inizden (`PM...`) türetilen BIP47 ödeme kodunuzu PayNym uygulamasına özgü benzersiz bir tanımlayıcı ile ilişkilendirir. Bu daha kısa, daha okunaklı tanımlayıcı daha sonra uzun, tam BIP47 kodunu paylaşmak zorunda kalmadan alışverişleri kolaylaştırmak için muhabirlerinize iletilebilir.



Bunu yapmak için, arayüzün sol üst köşesindeki PayNym resminize ve ardından ödeme kodunuz `PM...`ye tıklayın.



![Image](assets/fr/02.webp)



Ardından sağ üst köşedeki üç küçük noktaya tıklayın ve `PayNym Talep Et` seçeneğini seçin.



![Image](assets/fr/03.webp)



PAYNYM'nızı ŞİKAYET EDİN düğmesine tıklayarak onaylayın.



![Image](assets/fr/04.webp)



Sayfayı yenileyin: PayNym ID'niz artık resminizin altında, BIP47 ödeme kodunuzun hemen üstünde görüntülenir.



![Image](assets/fr/05.webp)



PayNym'iniz artık aktiftir ve ilk BIP47 işlemleriniz için kullanılmaya hazırdır.



## Bir kişi ile bağlantı kurun



PayNym arasında iki tür bağlantı vardır: **takip et** ve **bağlan**. Takip etme işlemi tamamen ücretsizdir. Samourai ekibi tarafından geliştirilen ve Ashigaru tarafından benimsenen Tor tabanlı şifreli bir iletişim protokolü olan Soroban aracılığıyla iki PayNym arasında bir bağlantı kurar. Bu bağlantı, birbirini takip eden iki kullanıcının özel olarak bilgi alışverişinde bulunmasını, özellikle de başka bir eğitimde inceleyeceğimiz Stowaway veya StonewallX2 gibi ortak işlemleri koordine etmesini sağlar. Bu adım PayNym'e özgüdür ve BIP47 protokolünün bir parçası değildir.



![Image](assets/fr/06.webp)



Diğer yandan, bağlantı işlemi (`connect`) bir on-chain işlemi gerektirir. BIP47'de tanımlandığı gibi bir bildirim işleminin gerçekleştirilmesinden oluşur. Bu Bitcoin işlemi, ödeyen ve alıcı arasında şifreli bir iletişim kanalı kuran bir `OP_RETURN` çıktısında meta veriler içerir. Bu kanaldan, ödeyici her bir ödeme için generate benzersiz alıcı adresleri belirleyebilecek ve alıcı bu ödemelerden haberdar edilecek ve bu fonları daha sonra harcamak için adreslerle ilişkili özel anahtarları generate kullanabilecektir.



Bu bildirim işleminin bir maliyeti vardır: mining ücreti ve bağlantıyı işaret etmek için alıcının bildirim adresine gönderilen 546 sats. Bağlantı kurulduktan sonra, BIP47 aracılığıyla neredeyse sonsuz sayıda ödeme yapılabilir.



Özetle:




- follow": ücretsiz, Soroban üzerinden şifreli iletişim kurar, Ashigaru'nun işbirlikçi araçları için kullanışlıdır;
- `Connect`: ücretlidir, ödeyici ve alıcı arasındaki kanalı etkinleştirmek için BIP47 bildirim işlemini gerçekleştirir.



Bir PayNym ile etkileşime geçmek için önce onu *takip* etmelisiniz. Bu, bir BIP47 bağlantısı kurmadan önceki ilk adımdır. Diyelim ki `+instinctiveoffer10` PayNym'ine yinelenen ödemeler göndermek istiyorsunuz.



Ashigaru'daki PayNym sayfanıza gidin, ardından arayüzün sağ alt tarafındaki `+` düğmesine tıklayın.



![Image](assets/fr/07.webp)



Daha sonra alıcının tam ödeme kodunu yapıştırabilir veya QR kodunu tarayabilirsiniz.



![Image](assets/fr/08.webp)



Yalnızca PayNym ID'sine sahipseniz, ödeme koduyla ilişkili QR kodunu bulmak için [Paynym.rs](https://paynym.rs/) adresine gidin.



![Image](assets/fr/09.webp)



QR kodunu taradıktan sonra, PayNym'i takip etmek için `TAKİP ET` düğmesine tıklayın.



![Image](assets/fr/10.webp)



İşbirliği işlemleri (*cahoots*) için `FOLLOW` eylemi yeterlidir. Ancak, BIP47 ödemeleri göndermek için bir bağlantı kurmanız gerekir: bildirim işlemini gerçekleştirmek için `CONNECT` üzerine tıklayın.



![Image](assets/fr/11.webp)



Bildirim işlemi daha sonra ağda yayınlanır. İlk ödemenizi yapmadan önce en az bir onay alana kadar bekleyin.



![Image](assets/fr/12.webp)



## BIP47 ödemesi yapın



Artık alıcıya bağlısınız ve alıcı ile önceden herhangi bir alışveriş yapmadan BIP47 protokolü kullanılarak otomatik olarak oluşturulan benzersiz bir adrese ödeme gönderebilirsiniz.



PayNym ana sayfanızdan, ödeme göndermek istediğiniz kişiye tıklayın.



![Image](assets/fr/13.webp)



Arayüzün sağ üst köşesindeki ok simgesine tıklayın.



![Image](assets/fr/14.webp)



Gönderilecek tutarı girin. Bir alıcı adresi girmenize gerek yoktur: BIP47 protokolü kullanılarak otomatik olarak türetilecektir.



![Image](assets/fr/15.webp)



Ücretler de dahil olmak üzere işlem ayrıntılarını dikkatlice kontrol edin, ardından işlemi imzalamak ve yayınlamak için ekranın altındaki yeşil oku sürükleyin.



![Image](assets/fr/16.webp)



İşlem gönderildi.



![Image](assets/fr/17.webp)



Bu örnekte, ödeme başka bir PayNym cüzdanıma yapıldı. Bu nedenle, herhangi bir adres manuel olarak değiştirilmeden diğer Ashigaru wallet'üme ulaştığını görebiliyorum: yalnızca PayNym tanımlayıcısı kullanıldı.



![Image](assets/fr/18.webp)



Ashigaru uygulamasındaki PayNym uygulaması sayesinde artık BIP47 yeniden kullanılabilir ödeme kodlarını nasıl kullanacağınızı biliyorsunuz. Artık bu ödeme kodunu size ödeme göndermek isteyen herkesle paylaşabilirsiniz (özellikle yinelenen ödemeler). Ayrıca bağış almak için PayNym ID'nizi web sitenizde veya sosyal ağlarınızda yayınlayabilirsiniz.



Bu protokol hakkındaki bilgilerinizi derinleştirmek, nasıl çalıştığını ve gizlilik üzerindeki etkilerini ayrıntılı olarak anlamak için BTC 204 kursumu almanızı şiddetle tavsiye ederim:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c