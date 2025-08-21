---
name: IVPN
description: Bitcoins ile ödenen bir VPN kurma
---
![cover](assets/cover.webp)


VPN ("*Sanal Özel Ağ*"), telefonunuz veya bilgisayarınız ile VPN sağlayıcısı tarafından yönetilen uzak bir sunucu arasında güvenli ve şifreli bir bağlantı kuran bir hizmettir.


Teknik olarak, bir VPN'e bağlanırken internet trafiğiniz şifrelenmiş bir tünel üzerinden VPN sunucusuna yönlendirilir. Bu işlem, İnternet Servis Sağlayıcıları (İSS'ler) veya kötü niyetli kişiler gibi üçüncü tarafların verilerinizi ele geçirmesini veya okumasını zorlaştırır. VPN sunucusu daha sonra sizin adınıza kullanmak istediğiniz hizmete bağlanan bir aracı görevi görür. Bağlantınıza yeni bir IP Address atar, bu da gerçek IP Address'ınızı ziyaret ettiğiniz sitelerden gizlemeye yardımcı olur. Bununla birlikte, bazı çevrimiçi reklamların önerebileceğinin aksine, VPN kullanmak internette anonim olarak gezinmenize izin vermez, çünkü tüm trafiğinizi görebilen VPN sağlayıcısına bir tür güven gerektirir.

![IVPN](assets/fr/01.webp)

VPN kullanmanın çok sayıda faydası vardır. İlk olarak, VPN sağlayıcısının bilgilerinizi paylaşmaması koşuluyla, çevrimiçi etkinliğinizin gizliliğini İSS'lerden veya hükümetlerden korur. İkinci olarak, özellikle MITM (man-in-the-middle) saldırılarına karşı savunmasız olan halka açık Wi-Fi ağlarına bağlandığınızda verilerinizi güvence altına alır. Üçüncü olarak, IP Address'inizi gizleyerek, bir VPN coğrafi kısıtlamaları ve sansürü atlamanıza, aksi takdirde bölgenizde kullanılamayacak veya engellenecek içeriğe erişmenize olanak tanır.


Gördüğünüz gibi VPN, trafik gözlemleme riskini VPN sağlayıcısına kaydırır. Bu nedenle, VPN sağlayıcınızı seçerken, kayıt için gereken kişisel verileri dikkate almak önemlidir. Sağlayıcı telefon numaranız, e-posta Address, banka kartı bilgileriniz veya daha kötüsü posta Address'niz gibi bilgiler isterse, kimliğinizin trafiğinizle ilişkilendirilme riski artar. Sağlayıcının tehlikeye girmesi veya yasal bir el koyma durumunda, trafiğinizi kişisel verilerinizle ilişkilendirmek kolay olacaktır. Bu nedenle, herhangi bir kişisel veri gerektirmeyen ve bitcoin gibi anonim ödemeleri kabul eden bir sağlayıcı seçmeniz önerilir.


Bu eğitimde, kullanımı için hiçbir kişisel bilgi gerektirmeyen basit, etkili, makul fiyatlı bir VPN çözümü sunuyorum.


## IVPN'e Giriş


IVPN, özellikle bir tür gizlilik arayan kullanıcılar için tasarlanmış bir VPN hizmetidir. YouTube'da sıklıkla tanıtılan popüler VPN sağlayıcılarının aksine, IVPN şeffaflığı, güvenliği ve gizliliğe saygısı ile öne çıkar.

IVPN'in gizlilik politikası katıdır: kayıt sırasında hiçbir kişisel bilgi gerekmez. E-posta Address, isim veya telefon numarası vermeden bir hesap açabilirsiniz. IVPN ödemeleri bitcoin (onchain ve Lightning) olarak kabul ettiğinden, ödeme için kredi kartı bilgilerinizi girmeniz gerekmez. Dahası, IVPN hiçbir aktivite kaydı tutmadığını iddia ediyor, bu da teorik olarak internet trafiğinizin şirket tarafından kaydedilmediği anlamına geliyor.

IVPN ayrıca yazılımları, uygulamaları ve hatta web siteleriyle ilgili olarak [tamamen açık kaynaklıdır] (https://github.com/ivpn), herkesin kodlarını doğrulamasına ve incelemesine izin verir. Ayrıca her yıl, sonuçları web sitelerinde yayınlanan bağımsız güvenlik denetimlerinden geçmektedirler.


IVPN yalnızca kendi barındırdığı sunucuları kullanır, böylece AWS, Google Cloud veya Microsoft Azure gibi üçüncü taraf bulut hizmetlerinin kullanımıyla ilişkili riskleri ortadan kaldırır.


Hizmet, anonimliği artırmak için trafiği farklı yargı bölgelerinde bulunan birden fazla sunucu üzerinden yönlendiren çoklu atlama gibi çok sayıda gelişmiş özellik sunar. IVPN ayrıca bir izleyici ve reklam engelleyici entegre eder ve farklı VPN protokolleri arasından seçim yapma seçeneği sunar.


Doğal olarak, bu hizmet kalitesinin bir bedeli vardır, ancak uygun bir fiyat genellikle kalite ve dürüstlüğün bir göstergesidir. Şirketin kişisel verileri satmaya ihtiyaç duymayan bir iş modeline sahip olduğuna işaret edebilir. IVPN daha sonra 2 tür plan sunar: 2 cihaza kadar bağlanmaya izin veren Standart plan ve 7 bağlantıya kadar izin veren ve trafiğinizi birden fazla sunucu üzerinden yönlendiren "*Multi-hop*" protokolünü içeren Pro plan.


Ana akım VPN sağlayıcılarının aksine IVPN, yinelenen bir abonelik yerine hizmete erişim süresi satın alma modeliyle çalışır. Seçilen süre için bir kez bitcoin olarak ödeme yaparsınız. Örneğin, bir yıllık erişim satın alırsanız, hizmeti o süre boyunca kullanabilirsiniz, ardından daha fazla erişim süresi satın almak için IVPN web sitesine geri dönmeniz gerekir.


IVPN ücretleri] (https://www.ivpn.net/en/pricing/) satın alınan erişim süresine bağlı olarak kademelidir. İşte Standart plan için fiyatlar:


- 1 hafta: $2
- 1 aylık: $6
- 1 yıl: $60
- 2 yıl: $100
- 3 yıl: $140


Ve Pro plan için:


- 1 hafta: $4
- 1 aylık: $10
- 1 yıl: $100
- 2 yıl: $160
- 3 yıl: $220


## IVPN bir bilgisayara nasıl kurulur?

İşletim sisteminiz için [yazılımın en son sürümünü] (https://www.ivpn.net/en/apps-windows/) indirin, ardından kurulum sihirbazındaki adımları izleyerek kuruluma devam edin. ![IVPN](assets/notext/02.webp)

Linux kullanıcıları için, [bu sayfa] (https://www.ivpn.net/en/apps-linux/) adresinde bulunan dağıtımınıza özgü talimatlara bakın.

![IVPN](assets/notext/03.webp)

Kurulum tamamlandığında, hesap kimliğinizi girmeniz gerekecektir. Bunu nasıl elde edeceğinizi bu eğitimin ilerleyen bölümlerinde göreceğiz.

![IVPN](assets/notext/04.webp)

## IVPN bir akıllı telefona nasıl kurulur?


IVPN'i, iOS kullanıcıları için [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683), Android için [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) veya [F-Droid](https://f-droid.org/en/packages/net.ivpn.client) uygulama mağazanızdan indirin. Android kullanıyorsanız, `.apk` dosyasını doğrudan [IVPN sitesinden] (https://www.ivpn.net/en/apps-android/) indirme seçeneğiniz de vardır.

![IVPN](assets/notext/05.webp)

Uygulamayı ilk kez kullandığınızda oturumunuz kapatılacaktır. Hizmeti etkinleştirmek için hesap kimliğinizi girmeniz gerekecektir.

![IVPN](assets/notext/06.webp)

Şimdi cihazlarınızda IVPN'i etkinleştirmeye geçelim.


## IVPN için ödeme nasıl yapılır ve etkinleştirilir?


Resmi IVPN web sitesine [ödeme sayfasında] (https://www.ivpn.net/en/pricing/) gidin.

![IVPN](assets/notext/07.webp)

İhtiyaçlarınıza en uygun planı seçin. Bu eğitim için, örneğin VPN'i bilgisayarımızda ve akıllı telefonumuzda etkinleştirmemize olanak tanıyan Standart planı seçeceğiz.

![IVPN](assets/notext/08.webp)

IVPN daha sonra hesabınızı oluşturacaktır. Herhangi bir kişisel bilgi vermenize gerek yoktur. Giriş yapmanızı sağlayacak olan yalnızca hesap kimliğinizdir. Bir nevi erişim anahtarı gibi davranır. Örneğin şifre yöneticiniz gibi güvenli bir yere kaydedin. Ayrıca basılı bir kopyasını da alabilirsiniz.

![IVPN](assets/notext/09.webp)

Aynı sayfada, hizmet aboneliğinizin süresini seçin.

![IVPN](assets/notext/10.webp)

Ardından ödeme yönteminizi seçin. Ben ödemeyi Lightning Network ile yapacağım için "*Bitcoin*" butonuna tıklıyorum.

![IVPN](assets/notext/11.webp)

Her şeyin istediğiniz gibi olup olmadığını kontrol edin ve ardından "*Yıldırım ile Öde*" düğmesine tıklayın.

![IVPN](assets/notext/12.webp)

BTCPay Sunucularında size bir Lightning Invoice sunulacaktır. QR kodunu Lightning Wallet'nizle tarayın ve ödemeye devam edin.

![IVPN](assets/notext/13.webp) Once the invoice is paid, click on the "*Return to IVPN*" button.

![IVPN](assets/notext/14.webp)

Hesabınız artık "*Aktif*" olarak görünür ve VPN'e erişiminizin geçerli olduğu tarihi görebilirsiniz. Bu tarihten sonra ödemenizi yenilemeniz gerekecektir.

![IVPN](assets/notext/15.webp)

IVPN üzerinden bağlantınızı bilgisayarınızda etkinleştirmek için hesap kimliğinizi kopyalamanız yeterlidir.

![IVPN](assets/notext/16.webp)

Ve daha önce indirdiğiniz yazılıma yapıştırın.

![IVPN](assets/notext/17.webp)

Ardından "*Login*" düğmesine tıklayın.

![IVPN](assets/notext/18.webp)

VPN bağlantısını etkinleştirmek için onay işaretine tıklayın ve işte bilgisayarınızın İnternet trafiği artık şifrelenmiş ve bir IVPN sunucusu üzerinden yönlendirilmiştir.

![IVPN](assets/notext/19.webp)

Akıllı telefonunuz için prosedür aynıdır. Hesap kimliğinizi yapıştırın veya web sitesinden erişilebilen IVPN hesabınızla ilişkili QR kodunu tarayın. Ardından, bağlantıyı kurmak için onay işaretine tıklayın.

![IVPN](assets/notext/20.webp)

## IVPN nasıl kullanılır ve yapılandırılır?


Kullanım ve ayarlar açısından oldukça basittir. Ana Interface'den, sadece onay işaretini kullanarak bağlantıyı etkinleştirebilir veya devre dışı bırakabilirsiniz.

![IVPN](assets/notext/21.webp)

Ayrıca VPN'inizi belirli bir süre için duraklatma seçeneğiniz de vardır.

![IVPN](assets/notext/22.webp)

Mevcut sunucuya tıklayarak, mevcut sunucular arasından başka bir sunucu seçebilirsiniz.

![IVPN](assets/notext/23.webp)

Entegre güvenlik duvarının yanı sıra anti-tracker işlevini etkinleştirmek veya devre dışı bırakmak da mümkündür.

![IVPN](assets/notext/24.webp)

Ek ayarlara erişmek için ayarlar simgesine tıklayın.

![IVPN](assets/notext/25.webp)

"*Hesap*" sekmesinde, hesabınızla ilgili ayarları bulacaksınız.

![IVPN](assets/notext/26.webp)

"*Genel*" sekmesinde, birkaç istemci ayarı vardır. Makinenizi başlattığınızda VPN ile bağlantıyı otomatik olarak kurmak için "*Autoconnect*" bölümündeki "*Launch at login*" ve "*On launch*" seçeneklerini işaretlemenizi tavsiye ederim.

![IVPN](assets/notext/27.webp)

"*Bağlantı*" sekmesinde, bağlantıyla ilgili çeşitli seçenekler bulacaksınız. Burası kullanılan VPN protokolünü değiştirebileceğiniz yerdir.

![IVPN](assets/notext/28.webp)

"*IVPN Güvenlik Duvarı*" sekmesi, güvenlik duvarını bilgisayarın başlangıcında sistematik olarak etkinleştirmenize olanak tanıyarak VPN dışında hiçbir bağlantı kurulmamasını sağlar.

![IVPN](assets/notext/29.webp)

"*Split Tunnel*" sekmesi, belirli yazılımları VPN bağlantısından hariç tutma imkanı sunar. Buraya eklenen uygulamalar, VPN etkinleştirildiğinde bile normal bir internet bağlantısıyla çalışmaya devam edecektir.

![IVPN](assets/notext/30.webp)

"*WiFi kontrolü*" sekmesinde, bağlı olduğunuz ağlara göre belirli eylemleri yapılandırma seçeneğiniz vardır. Örneğin, ev ağınızı "*Güvenilir*" olarak belirleyebilir ve VPN'i bu ağda etkinleştirilmeyecek, ancak diğer WiFi ağlarında otomatik olarak etkinleştirilecek şekilde yapılandırabilirsiniz.

![IVPN](assets/notext/31.webp)

"*AntiTracker*" menüsünde, anti-tracker'ınız için engelleme profilini seçin. Bu, siz internette gezinirken izleme hizmetlerine gelen istekleri engelleyerek reklamları, kötü amaçlı yazılımları ve veri izleyicileri engellemek için tasarlanmıştır. Bu, şirketlerin tarama verilerinizi toplamasını ve satmasını önleyerek gizliliğinizi artırır. Google ve Meta'nın sahip olduğu tüm alan adlarını ve tüm bağımlı hizmetleri tamamen engellemek için bir "*Hardcore Modu*" da mevcuttur.

![IVPN](assets/notext/32.webp)

İşte bu kadar, artık IVPN'in keyfini tam anlamıyla çıkarmak için donanımlısınız. Ayrıca yerel bir parola yöneticisi kullanarak çevrimiçi hesaplarınızın güvenliğini artırmak istiyorsanız, sizi ücretsiz ve açık kaynaklı bir çözüm olan KeePass hakkındaki eğitimimize göz atmaya davet ediyorum:


https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Hem özellikler hem de fiyatlandırma açısından IVPN'e benzer başka bir VPN sağlayıcısı keşfetmekle ilgileniyorsanız, Mullvad hakkındaki eğitimimize de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8