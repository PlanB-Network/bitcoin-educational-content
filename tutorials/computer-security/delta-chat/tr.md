---
name: Delta Sohbet
description: Merkezi olmayan bir mesajlaşma aracı için pratik kılavuz
---

![image](assets/cover.webp)




## Giriş - Sohbet Kontrolü ve Gizlilik



Son yıllarda, büyük iletişim platformlarındaki özel mesajların otomatik olarak taranmasını amaçlayan bir düzenleme önerisi olan Sohbet Kontrolü hakkında konuşmalar artmaktadır. Belirtilen amaç yasadışı içerikle mücadele etmektir, ancak sorun şu ki bu mekanizma aslında kitlesel gözetim içerecek, uçtan uca şifrelemeyi ve dolayısıyla sadece suçluların değil tüm kullanıcıların mahremiyetini baltalayacaktır.



Asıl risk, sohbetlerin her mesajın, görüntünün veya eklentinin daha alıcıya ulaşmadan incelenebileceği kontrollü ortamlar haline gelmesidir. İşte bu noktada olası bir çözüm devreye giriyor: merkezi platformlardan uzaklaşmak ve tek bir sağlayıcıya bağlı olmayan ve bu tür bir incelemeye kolayca tabi tutulamayan merkezi olmayan mesajlaşma sistemlerine yönelmek.



Bu eğitimde böyle bir çözüm sunulacaktır: Delta Chat. Olgun ve halihazırda kullanılabilir bir araç.




## Delta Chat neden ve nasıl çalışır?



Delta Chat, günlük kullanım için zaten çok iyi bir mesajlaşma çözümüdür: WhatsApp'ın gerçek bir eşdeğeri gibi arkadaşlarınızla, ailenizle ve diğer insanlarla konuşmak için çok kullanışlıdır.



Tamamen e-postaya dayalı merkezi olmayan bir mesajlaşma sistemidir. Temel olarak geleneksel e-posta altyapısından yararlanır, ancak bunun üzerine modern bir anlık mesajlaşma arayüzü ve deneyimi inşa eder. İlk bakışta bu biraz doğaçlama gibi görünebilir, ancak aslında çok iyi çalışıyor ve şaşırtıcı derecede sağlam. ChatMail adı verilen özel posta sunucularını kullanabilirsiniz, ancak normal e-posta sunucularıyla da sorunsuz bir şekilde çalışabilir. Bu, isterseniz yeni bir şey oluşturmak zorunda kalmadan mevcut bir hesapla giriş yapabileceğiniz anlamına gelir.



Öne çıkan bir diğer özellik ise, Telegram'daki mini uygulamalara benzer şekilde, doğrudan sohbetlerin içinde kullanılabilen küçük Web uygulamaları olan WebXDC'ler için destek. Önemli fark, bu uygulamaların İnternet erişimine sahip olmamasıdır, bu nedenle kullanıcıyı izleyemez veya harici olarak veri gönderemezler.



Güvenlik açısından Delta Chat, PGP'ye dayanan ancak Signal ile karşılaştırılabilir düzeyde koruma sağlayan modern uzantılara sahip doğrulanmış uçtan uca şifreleme kullanır. Şu anki tek eksik Perfect Forward Secrecy'dir, ancak bu gelişmekte olan bir özelliktir.



Yalnızca e-postaya dayalı olan Delta Chat, bundan tamamen kaçınır:




- zorunlu telefon numaraları
- Merkezi Kimlikler
- tek bir hizmete bağlı kayıtlar



Bu aracı Sohbet Kontrolü gibi istilacı düzenlemelere karşı çok dirençli kılan da budur.




## Kurulum



Delta Chat]'in resmi web sitesinden (https://delta.chat/download) İndirme bölümüne gidebilirsiniz. Linux'ta Flathub aracılığıyla rahatlıkla kullanılabilir, ancak Arch, NixOS, Snap ve bağımsız sürümler için de paketler vardır.



![image](assets/it/01.webp)



Ayrıca şunlar için de kullanılabilir:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- ve diğer mağazalar...



F-Droid'yı kurmak için bir rehber arıyorsanız, bu eğitim size yardımcı olabilir:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Çok önemli bir şey: masaüstü sürümleri telefon gerektirmez. WhatsApp veya SimpleX Chat'den farklı olarak, önce mobilden kaydolmanız gerekmez. Profilinizi doğrudan PC'de oluşturabilir veya başka bir cihazdan aktarabilirsiniz.




## Profil oluşturma



Uygulama açıldığında, Delta Chat yeni bir profil oluşturup oluşturmayacağınızı veya mevcut bir profili kullanıp kullanmayacağınızı sorar.



![image](assets/it/02.webp)



Yeni bir profil oluşturarak girebilirsiniz:




- bir isim
- bir resim (isteğe bağlı)



Varsayılan olarak bir ChatMail sunucusu önerilmektedir, ancak bu mümkündür:




- başka bir ChatMail sunucusu seçin
- klasik bir e-posta hesabı kullanın
- iMAP ve SMTP'yi manuel olarak yapılandırma
- başka bir kullanıcının davet kodunu kullanarak kaydolma



Birkaç saniye sonra profil hazır olur ve uygulamayı kullanmaya başlayabilirsiniz.



![image](assets/it/03.webp)




## Interface ve sohbet



Arayüz çok basit ve anlaşılırdır:




- Yerel iletişim olan cihaz mesajları
- Telegram'dakine benzer ve cihazlar arasında senkronize edilebilen kayıtlı mesajlar



![image](assets/it/04.webp)



Bir kişi eklemek için basitçe:




- QR kodunuzu gösterme
- Diğer kişinin
- Bağlantı yoluyla davet edin (davet bağlantısını paylaşın).



![image](assets/it/05.webp)



Bağlantı kurulduktan sonra uçtan uca şifreleme otomatik olarak yapılandırılır. Sohbet kullanıcı arayüzü WhatsApp'ınkine çok benzer:




- metin ve sesli mesajlar
- fotoğraflar, videolar ve dosyalar
- mesajlara verilen yanıtlar
- reaksiyonlar
- açılır mesajlar
- özelleştirilebilir bildirimler.



![image](assets/it/06.webp)



## WebXDC: sohbetlerdeki uygulamalar:



Delta Chat, WebXDC'nin, yani konuşmalara gömülü küçük uygulamaların kullanımına izin verir. İşte tespit edilen en kullanışlı olanların kısa bir listesi:




- anketler
- çizim tahtaları
- geçici özel sohbetler
- paylaşılan sohbet skorlarına sahip oyunlar



Bu aracın esnekliğini gösteren daha karmaşık oyunlar da başlatılabilir.



![image](assets/it/07.webp)



## Gruplar, kanallar ve gelişmiş özellikler



Gruplar oluşturabilir, çıkartmalar kullanabilir (özellikle masaüstlerinde) ve deneysel seçenekleri etkinleştirerek Telegram'dakine benzer kanallar bile oluşturabilirsiniz.



Gelişmiş ayarlarda açabilirsiniz:




- sesli aramalar (hala deneysel)
- geli̇şmi̇ş e-posta profi̇l yöneti̇mi̇
- tam yedeklemeler.



![image](assets/it/08.webp)



## Çoklu cihaz ve yedekleme



Delta Chat çoklu cihazı tamamen destekler:




- qR kodu aracılığıyla ikinci bir cihaz ekleyebilirsiniz
- yedekleme yoluyla tam bir aktarım gerçekleştirebilirsiniz.



Merkezi bir sunucuya bağlı kalmadan saniyeler içinde sohbetlerinizi, gruplarınızı ve tüm geçmişinizi yeniden bulacaksınız.



![image](assets/it/09.webp)




## Sonuç



Özel iletişimin kontrol altına alınmasının giderek daha fazla konuşulduğu bir dönemde Delta Chat somut bir cevabı temsil ediyor: her gün gerçekten kullanılabilen merkezi olmayan, şifrelenmiş mesajlaşma.



Denediklerim arasında basitlik, gizlilik ve özgürlük açısından beni en çok ikna eden çözüm bu oldu. İsterseniz, aşağıdaki [davet bağlantısı] (https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) aracılığıyla Delta Chat üzerinden de benimle iletişime geçebilirsiniz



Bu rehber hoşunuza gittiyse, bağış yaparak ve beğeninizi belirterek beni destekleyebilirsiniz. Ve unutmayın: Delta Chat'i hem mobil hem de masaüstünden kullanıp keşfederek tam işlevselliğini gerçekten keşfedeceksiniz.



Bir dahaki sefere kadar.