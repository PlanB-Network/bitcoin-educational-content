---
name: Mullvad VPN
description: Bitcoins ile ödenen bir VPN kurma
---
![cover](assets/cover.webp)


VPN ("*Sanal Özel Ağ*"), telefonunuz veya bilgisayarınız ile bir VPN sağlayıcısı tarafından yönetilen uzak bir sunucu arasında güvenli ve şifreli bir bağlantı kuran bir hizmettir.


Teknik olarak, bir VPN'e bağlanırken internet trafiğiniz şifrelenmiş bir tünel üzerinden VPN sunucusuna yönlendirilir. Bu işlem, İnternet Servis Sağlayıcıları (İSS'ler) veya kötü niyetli kişiler gibi üçüncü tarafların verilerinizi ele geçirmesini veya okumasını zorlaştırır. VPN sunucusu daha sonra sizin adınıza kullanmak istediğiniz hizmete bağlanan bir aracı görevi görür. Bağlantınıza yeni bir IP Address atar, bu da gerçek IP Address'ınızı ziyaret ettiğiniz sitelerden gizlemeye yardımcı olur. Bununla birlikte, bazı çevrimiçi reklamların önerebileceğinin aksine, VPN kullanmak internette anonim olarak gezinmenize izin vermez, çünkü tüm trafiğinizi görebilen VPN sağlayıcısına bir güven düzeyi gerektirir.

![MULLVAD VPN](assets/fr/01.webp)

VPN kullanmanın çok sayıda faydası vardır. İlk olarak, VPN sağlayıcısının bilgilerinizi paylaşmaması koşuluyla, çevrimiçi etkinliğinizin gizliliğini İSS'lerden veya hükümetlerden korur. İkinci olarak, özellikle MITM ("**man-in-the-middle**") saldırılarına karşı savunmasız olan halka açık Wi-Fi ağlarına bağlandığınızda verilerinizi güvence altına alır. Üçüncü olarak, IP Address'inizi gizleyerek, bir VPN coğrafi kısıtlamaları ve sansürü atlamanıza, aksi takdirde bölgenizde kullanılamayacak veya engellenecek içeriğe erişmenize olanak tanır.


Gördüğünüz gibi VPN, trafik gözlemleme riskini VPN sağlayıcısına kaydırır. Bu nedenle, VPN sağlayıcınızı seçerken, kayıt için gereken kişisel verileri dikkate almak önemlidir. Sağlayıcı telefon numaranız, e-posta Address, banka kartı bilgileriniz veya daha kötüsü posta Address'niz gibi bilgiler isterse, kimliğinizin trafiğinizle ilişkilendirilme riski artar. Sağlayıcının tehlikeye girmesi veya yasal bir el koyma durumunda, trafiğinizi kişisel verilerinizle ilişkilendirmek kolay olacaktır. Bu nedenle, herhangi bir kişisel bilgi gerektirmeyen ve bitcoin gibi anonim ödemeleri kabul eden bir sağlayıcı seçmeniz önerilir.


Bu eğitimde, kullanımı için hiçbir kişisel bilgi gerektirmeyen basit, etkili, makul fiyatlı bir VPN çözümü sunacağım.


## Mullvad VPN'e Giriş

Mullvad VPN, kullanıcı gizliliğine verdiği önemle öne çıkan bir İsveç hizmetidir. Ana akım VPN sağlayıcılarının aksine, Mullvad kayıt sırasında hiçbir kişisel veri gerektirmez. Bir e-posta Address, telefon numarası veya isim sağlamanıza gerek yoktur; bunun yerine, Mullvad size ödeme ve hizmete erişim için kullanılan anonim bir hesap numarası atar. Ayrıca Mullvad, sunucularından geçen hiçbir etkinlik kaydı tutmadığını iddia ediyor.

![MULLVAD VPN](assets/notext/02.webp)

Ödeme için, Mullvad Bitcoin ödemelerini kabul ettiğinden (yalnızca resmi sitelerinde zincir üzerinde, ancak Lightning aracılığıyla ödeme yapmak için resmi olmayan bir yöntem vardır) kredi kartı bilgilerinizi vermeniz gerekmez. Ayrıca posta yoluyla nakit ödemeleri de kabul etmektedirler.


Mullvad VPN ayrıca şeffaflığı ve güvenliği ile de öne çıkmaktadır. Yazılımları açık kaynaklıdır ve uygulamalarını ve altyapılarını değerlendirmek için düzenli olarak bağımsız güvenlik denetimlerinden geçerler ve bunların sonuçları [web sitelerinde yayınlanır] (https://mullvad.net/fr/blog/tag/audits). Mullvad'ın arkasındaki şirket, sıkı gizlilik yasalarıyla bilinen bir ülke olan İsveç'te yerleşiktir. Yalnızca kendi bünyelerinde barındırdıkları sunucuları kullanarak AWS, Google Cloud veya Microsoft Azure gibi üçüncü taraf bulut hizmetlerinin kullanımıyla ilişkili riskleri ortadan kaldırmaktadırlar.


Özellikler açısından Mullvad, VPN bağlantısı kesilirse trafiğinizi koruyan bir kill switch, belirli uygulamalar için VPN'i devre dışı bırakma seçeneği ve trafiğinizi birden fazla VPN sunucusu üzerinden yönlendirme yeteneği dahil olmak üzere iyi bir VPN istemcisinden beklenen her şeyi sunar.


Doğal olarak, bu hizmet kalitesinin bir bedeli vardır, ancak uygun bir fiyat genellikle kalite ve dürüstlüğün bir göstergesidir. Şirketin kişisel verilerinizi üçüncü taraflara satmaya ihtiyaç duymadan bir iş modeline sahip olduğunu gösterebilir. Mullvad VPN, 5 farklı cihaza kadar kullanılabilen aylık 5 avroluk sabit bir ücret sunar.

![MULLVAD VPN](assets/notext/03.webp)

Ana akım VPN sağlayıcılarının aksine Mullvad, yinelenen, otomatik bir abonelik yerine hizmete erişim süresi satın alma modeline sahiptir. Seçilen süre için bitcoin cinsinden tek seferlik bir ödeme yapmanız yeterlidir. Örneğin, bir yıllık erişim satın alırsanız, hizmeti o süre boyunca kullanabilirsiniz, daha sonra erişim sürenizi yenilemek için Mullvad'ın web sitesine dönmeniz gerekir.

Bir başka yüksek kaliteli VPN sağlayıcısı olan IVPN ile karşılaştırıldığında, Mullvad biraz daha ekonomiktir. Örneğin, IVPN ile üç yıllık bir satın alma tercih edildiğinde bile, aylık maliyet yaklaşık 5,40 € tutarındadır. Bununla birlikte, IVPN bazı ek hizmetler sunar ve ayrıca Mullvad'ınkinden daha ucuz bir plana sahiptir (Standart plan), ancak bu yalnızca 2 cihazla sınırlıdır ve "çoklu atlama" protokolünü hariç tutar.

IVPN ve Mullvad'ı karşılaştırmak için bazı gayri resmi hız testleri de yaptım. IVPN performans açısından hafif bir üstünlük gösterse de, Mullvad'daki hızlar yine de çok tatmin ediciydi. Ana akım VPN sağlayıcılarıyla karşılaştırıldığında, IVPN ve Mullvad bazı durumlarda üstün olmasa da en az onlar kadar verimli olduklarını kanıtladılar.


## Mullvad VPN bir bilgisayara nasıl kurulur?


Resmi Mullvad web sitesini] (https://mullvad.net/en/download/) ziyaret edin ve "*Downloads*" menüsüne tıklayın.

![MULLVAD VPN](assets/notext/04.webp)

Windows veya macOS kullanıcıları için yazılımı doğrudan siteden indirin ve kurulumu tamamlamak için kurulum sihirbazı tarafından sağlanan talimatları izleyin.

![MULLVAD VPN](assets/notext/05.webp)

Linux kullanıcıları için, dağıtımınıza özel talimatları ["*Linux*"](https://mullvad.net/en/download/vpn/linux) bölümünde bulabilirsiniz.

![MULLVAD VPN](assets/notext/06.webp)

Kurulum tamamlandığında, hesap kimliğinizi girmeniz gerekecektir. Bunu nasıl elde edeceğinizi bu eğitimin ilerleyen bölümlerinde göreceğiz.


## Mullvad VPN bir akıllı telefona nasıl kurulur?


Mullvad VPN'i, iOS kullanıcıları için [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513), Android için [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) veya [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/) olsun, uygulama mağazanızdan indirin. Android kullanıyorsanız, `.apk` dosyasını doğrudan [Mullvad sitesinden] (https://mullvad.net/en/download/vpn/android) indirme seçeneğiniz de vardır.

![MULLVAD VPN](assets/notext/07.webp)

Uygulamayı ilk kez kullandığınızda oturumunuz kapatılacaktır. Hizmeti etkinleştirmek için hesap kimliğinizi girmeniz gerekecektir.

![MULLVAD VPN](assets/notext/08.webp)

Şimdi, Mullvad'ı cihazlarınızda etkinleştirmeye geçelim.


## Mullvad VPN için nasıl ödeme yapılır ve etkinleştirilir?


Resmi Mullvad web sitesine] (https://mullvad.net/) gidin ve "*Get Started*" düğmesine tıklayın.

![MULLVAD VPN](assets/notext/09.webp)

"*generate hesap numarası*" düğmesine tıklayın.

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

Ardından "*Hesabınıza zaman ekleyin*" düğmesine tıklayın.

![MULLVAD VPN](assets/notext/12.webp)

Daha sonra hesabınız için giriş sayfasına ulaşacaksınız. Hesap numaranızı girin ve ardından "*Giriş yap*" düğmesine tıklayın.

![MULLVAD VPN](assets/notext/13.webp)

Ödeme yönteminizi seçin. Bitcoin ile ödeme yapmanızı tavsiye ederim, çünkü %10 indirimden yararlanacaksınız, bu da maliyeti aylık 4,50 € 'ya düşürüyor. Lightning ile ödeme yapmayı tercih ederseniz, bir sonraki bölümde alternatif bir yöntem sunacağım.

![MULLVAD VPN](assets/notext/14.webp)

"*Tek seferlik ödeme oluştur Address*" düğmesine tıklayın.

![MULLVAD VPN](assets/notext/15.webp)

Ardından size verilen alıcı Address'e belirtilen tutarı Bitcoin Wallet ile ödeyin.

![MULLVAD VPN](assets/notext/16.webp)

İşlem onaylandıktan sonra sitenin ödemenizi algılaması birkaç dakika sürebilir. Ödeme Mullvad tarafından algılandıktan sonra, aboneliğinizin süresi sayfanın sol üst köşesinde "*Süre kalmadı*" ibaresi yerine görünecektir.

![MULLVAD VPN](assets/notext/17.webp)

Daha sonra VPN'i etkinleştirmek için yazılıma hesap numaranızı girebilirsiniz.

![MULLVAD VPN](assets/notext/18.webp)

VPN'i mobil uygulamanızda etkinleştirmek için süreç tamamen aynıdır. Sadece hesap numaranızı girmeniz yeterlidir.

![MULLVAD VPN](assets/notext/19.webp)

## Lightning ile Mullvad VPN için nasıl ödeme yapılır?


Sizin de anladığınız gibi, Mullvad henüz Lightning Network üzerinden ödeme kabul etmiyor. Ancak, [Lounès](https://x.com/louneskmt)'den gelen bir öneri sayesinde, bu sınırlamayı aşmanıza olanak tanıyan gayri resmi bir hizmet keşfettim. Vpn.sovereign.engineering](https://vpn.sovereign.engineering/) adresinde bulunan bu hizmet, Lightning üzerinden ödemelerinizi kabul ediyor ve karşılığında size Mullvad için geçerli bir plan sunuyor.

![MULLVAD VPN](assets/notext/20.webp)

Bu sitede 2 farklı seçeneğiniz var: site yöneticisine güvenebilir ve doğrudan hesap numaranızı girebilir, ardından Mullvad paketinizin otomatik olarak onaylanması için "*Giriş yap*" düğmesine tıklayabilirsiniz. Ya da "*Heck yeah!*" düğmesine tıklayarak Lightning'de bir Voucher satın alabilir ve daha sonra paketinizi almak için resmi Mullvad sitesinde kullanabilirsiniz. ![MULLVAD VPN](assets/notext/21.webp) Her iki durumda da, paketinizin süresini seçmeniz istenecektir. 6 ay ile 1 yıl arasında seçim yapabilirsiniz. ![MULLVAD VPN](assets/notext/22.webp) Ardından "*Yıldırım ile Tamamla*" düğmesine tıklayın. ![MULLVAD VPN](assets/notext/23.webp) Satın alma işlemini tamamlamak için Invoice'yi Lightning Wallet'ünüzle ödeyin. ![MULLVAD VPN](assets/notext/24.webp) Bir Kupon satın almayı seçtiyseniz, Mullvad sitesinde, hesabınızda bulunan ödeme yöntemleri arasından "*Voucher*" seçeneğini seçin. Ardından, vpn.sovereign.engineering sitesinden aldığınız Voucher numarasını belirtilen kutuya girin. ![MULLVAD VPN](assets/notext/25.webp) ## Mullvad VPN nasıl kullanılır ve yapılandırılır?


Artık aktif bir hesabınız olduğuna ve hesap numaranızı Mullvad yazılımına veya uygulamasına girdiğinize göre, VPN'inizin hizmetlerinden tam olarak yararlanabilirsiniz. ![MULLVAD VPN](assets/notext/26.webp) VPN bağlantısını kesmek için "*Bağlantıyı Kes*" düğmesine tıklamanız yeterlidir. ![MULLVAD VPN](assets/notext/27.webp) "*Bağlantıyı Kes*" düğmesinin yanındaki küçük kırmızı ok, geçerli konumu değiştirmeden sunucuları değiştirmenize olanak tanır. ![MULLVAD VPN](assets/notext/28.webp) VPN sunucunuz için şehir değiştirmek istiyorsanız, yeni bir konum seçmek için "*Konum değiştir*" düğmesine tıklayın. ![MULLVAD VPN](assets/notext/29.webp) Ekranın üst kısmında, cihazınızın takma adını ve paketinizin kalan süresini göreceksiniz. ![MULLVAD VPN](assets/notext/30.webp) Küçük adamın simgesine tıklayarak, hesabınızla ilgili ayrıntılı bilgilere erişeceksiniz. ![MULLVAD VPN](assets/notext/31.webp) Ayarlara erişmek için dişli çarkına tıklayın. ![MULLVAD VPN](assets/notext/32.webp) "*Kullanıcı Interface ayarları*" menüsünde, Interface dili ve sisteminizdeki davranışı dahil olmak üzere yazılımınızın ayarlarını özelleştirebilirsiniz. ![MULLVAD VPN](assets/notext/33.webp) "*VPN ayarları*" menüsünde VPN'inizle ilgili seçenekleri bulacaksınız. Makineniz başladığında VPN bağlantınızın otomatik olarak başlatılması için "*Başlangıçta uygulamayı başlat*" ve "*Otomatik bağlan*" seçeneklerini etkinleştirmenizi öneririm.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

Son olarak, "*Bölünmüş tünelleme*" menüsü, makinenizde internet trafiğinin VPN üzerinden yönlendirilmeyeceği belirli uygulamaları seçmenize olanak tanır.

![MULLVAD VPN](assets/notext/36.webp)

Mullvad hesabınıza genel bir bakış elde etmek ve çeşitli bağlı cihazları yönetmek için web sitesindeki "*Cihazlar*" menüsüne tıklayabilirsiniz.

![MULLVAD VPN](assets/notext/37.webp)

İşte bu kadar, artık Mullvad VPN'in keyfini tam olarak çıkarmak için donanımlısınız. Hem özellikler hem de fiyatlandırma açısından Mullvad'a benzer başka bir VPN sağlayıcısı keşfetmekle ilgileniyorsanız, IVPN hakkındaki eğitimimize de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68