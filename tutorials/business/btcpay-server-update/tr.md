---
name: BTCPay Server'ı Güncelleme
description: BTCPay Server örneğinize bir güvenlik güncellemesi uygulayın ve önemli kimlik bilgilerini yenileyin
---

![kapak](assets/cover.webp)

Kendi ödeme işlemcinizi çalıştırmak, aynı zamanda kendi güvenlik ekibiniz olmak demektir. BTCPay Server bakımcıları bir güvenlik sürümü yayımladığında, örneğinizi sizin yerinize kimse yamalamaz: güncelleme, doğrulama ve ardından gelen kimlik bilgisi yenileme işlemleri sizin sorumluluğunuzdadır.

Bu eğitim, BTCPay Server'ı hangi yöntemle dağıtmış olursanız olun tüm prosedürü adım adım ele alır: çalışan sürümü kontrol etmek, dağıtım türünüze göre güncellemeyi uygulamak, güncellemenin gerçekten yerine ulaştığını doğrulamak ve örneğiniz savunmasızken bir saldırganın ele geçirmiş olabileceği sırları yenilemek.

BTCPay Server'ı henüz dağıtmadıysanız, kurulum rehberiyle başlayın:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Ağustos 2026 kritik güvenlik açığı

⚠️ **Kritik güvenlik uyarısı (7 Ağustos 2026):** BTCPay Server'ı etkileyen kritik bir güvenlik açığı aktif olarak istismar ediliyor ve fon kaybına yol açabilir. Örneğinizi `Admin Dashboard > Server > Maintenance > Update` yolundan derhal **2.4.2 sürümüne** güncelleyin, ardından alt bilginin `2.4.2` gösterdiğini kontrol edin. Hemen güncelleyemiyorsanız BTCPay Server'ınızı kapatın. Güncellendikten sonra macaroons'larınızı ve `macaroons.db` dosyanızı tamamen yenilemeniz, diğer tüm Lightning arka uçlarının kimlik doğrulama dizelerini tamamen yenilemeniz ve BTCPay Server içinde sıcak bir on-chain cüzdan oluşturduysanız bu fonları taşıyıp cüzdanı yeniden oluşturmanız gerekir. Entegratörler ayrıca NBXplorer'ı 2.6.10 sürümüne güncellemelidir. Kaynak: [BTCPay Server 2.4.2 sürüm notları](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

2.4.2 sürümü 7 Ağustos 2026'da yayımlandı. Sürüm notları, bunun Bitcoin Red Team çalışması aracılığıyla `brunoerg` ve `benthecarman` tarafından bildirilen ve sahada hâlihazırda istismar edilmekte olan kritik bir güvenlik açığını giderdiğini belirtir. Aynı sürüm, Greenfield Basic kimlik doğrulaması üzerinden TOTP iki faktörlü kimlik doğrulamasını atlatma açığını da giderir ve hesap oluşturulduktan beş dakika sonra Greenfield Basic kimlik doğrulamasını varsayılan olarak devre dışı bırakır.

"Aktif olarak istismar ediliyor" ifadesinin iki sonucu vardır:

- **Güncelleme isteğe bağlı değildir ve gelecek haftaya planlanacak bir iş değildir.** İnternetten erişilebilir olan yamalanmamış bir örnek ya güncellenmeli ya da kapatılmalıdır.
- **Güncelleme tek başına yeterli değildir.** Örneğiniz siz yamalamadan önce ele geçirildiyse, saldırgan Lightning kimlik bilgilerinizin ve BTCPay Server'ın sizin için oluşturduğu herhangi bir sıcak cüzdan anahtar materyalinin kopyalarını hâlihazırda elinde tutuyor olabilir. Bu sırlar, siz onları yenileyene kadar güncellemeden sonra da geçerli kalır. Aşağıdaki yenileme bölümü insanların atladığı kısımdır ve fonlarınızı gerçekten koruyan kısım da budur.

## Adım 1 — Hangi sürümü çalıştırdığınızı öğrenin

BTCPay Server'ınıza giriş yapın ve **herhangi bir sayfanın alt bilgisine** bakın: sürüm dizesi orada görüntülenir. Mevcut sürümü ve güncelleme kontrollerini gösteren `Admin Dashboard > Server > Maintenance` bölümünü de açabilirsiniz.

Örneğiniz Greenfield API'yi dışa açıyorsa, `GET /api/v1/server/info` de sürümü döndürür.

`2.4.2` altındaki her şey savunmasızdır.

## Adım 2 — Güncelleyin

### Kendi kendine barındırılan Docker dağıtımı (standart kurulum)

Bu bölüm, BTCPay Server dokümantasyonundan, LunaNode tek tıklamalı başlatıcısından ve çoğu VPS kurulumundan elde ettiğiniz resmi Docker dağıtımını kapsar.

En basit yol web arayüzüdür:

1. `Admin Dashboard > Server > Maintenance` bölümüne gidin.
2. **Update** düğmesine tıklayın.
3. Container'ların çekilip yeniden başlatılmasını bekleyin. Arayüz birkaç dakika kullanılamaz olacaktır.

Web arayüzüne ulaşılamıyorsa veya logları görmeyi tercih ediyorsanız, bunu SSH üzerinden yapın:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Varsayılan bir kurulumda `$BTCPAY_BASE_DIRECTORY` `/root` olur; dolayısıyla dizin `/root/btcpayserver-docker` olur. Betik en yeni imajları çeker, container'ları yeniden oluşturur ve ortaya çıkan sürümleri yazdırır.

Docker dağıtımı, NBXplorer'ı BTCPay Server ile birlikte gönderir; bu nedenle standart bir güncelleme NBXplorer'ı da önerilen `2.6.10` sürümüne getirir. NBXplorer'ı ayrı çalıştırıyorsanız — entegratörler ve özel yığınlar için tipik durum — onu açıkça güncelleyin.

### Umbrel

Umbrel gösterge panelini açın, **App Store** bölümüne gidin, BTCPay Server'ı bulun ve bir güncelleme sunuluyorsa uygulayın.

⚠️ **Önemli:** uygulama mağazası paketleri Umbrel ekibi tarafından yeniden paketlenir ve upstream'in saatler veya günler gerisinde kalabilir. Güncellemeden sonra BTCPay Server alt bilgisindeki sürümü kontrol edin. Hâlâ `2.4.2` altındaysa, savunmasız bir örneği çalışır durumda bırakmak yerine Umbrel gösterge panelinden **uygulamayı durdurun** ve paketlenmiş sürümü bekleyin.

Özel Umbrel rehberi uygulamanın kendisini kapsar:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Aynı mantık geçerlidir: BTCPay Server'ı StartOS marketplace'ten güncelleyin, ardından alt bilgideki sürümü doğrulayın. Paketlenmiş sürüm henüz `2.4.2` değilse, olana kadar hizmeti durdurun.

### Yönetilen ve üçüncü taraf barındırma

Örneğinizi başka biri işletiyorsa (bir barındırma sağlayıcısı, bir dernek, bir arkadaşınızın sunucusu), yine de doğrulamaya ihtiyacınız vardır. Operatörden alt bilgide gösterilen sürüm dizesini isteyin ve aşağıda açıklanan güncelleme sonrası kimlik bilgisi yenilemesinin gerçekleştirilip gerçekleştirilmediğini açıkça sorun. "Güncelledik" yanıtı, "macaroons'larınızı yeniledik" yanıtıyla aynı şey değildir.

## Adım 3 — Güncellemenin gerçekten uygulandığını doğrulayın

BTCPay Server arayüzünü yeniden yükleyin ve alt bilgideki sürümü okuyun. `2.4.2` veya daha yüksek bir değer göstermelidir.

Güncelleme komutunun hata vermeden çıkmasına güvenmeyin: kısıtlı makinelerde bir imaj çekme işlemi sessizce başarısız olabilir ve önceki container'ı çalışır durumda bırakabilir. Her seferinde sürümü okuyun.

## Adım 4 — Kimlik bilgilerinizi yenileyin

"Yamalanmış" olanı "güvenli" hale getiren adım budur. Güvenlik açığı, düzeltme yayımlanmadan önce istismar edildiği için, örneğinizin tuttuğu her sırrı bir saldırgan tarafından potansiyel olarak biliniyormuş gibi ele alın.

### Lightning: LND

Macaroons'ları **ve** `macaroons.db` dosyasını yeniden oluşturun. Yalnızca macaroon dosyalarını silmek yeterli değildir — LND, macaroon'ları `macaroons.db` içinde saklanan kök anahtardan türetir; bu nedenle eski bir macaroon'un kopyasına sahip olan saldırgan, o veritabanı yeniden oluşturulana kadar erişimini korur.

Prosedür şudur: LND'yi durdurun, `macaroons.db` ve `*.macaroon` dosyalarını ağ dizininden kaldırın (mainnet için, LND veri dizininin içindeki `data/chain/bitcoin/mainnet/`), ardından LND'yi yeniden başlatıp kilidini açın; bunları yeniden oluşturur. Önce dizini yedekleyin ve eski macaroons'ları kullanan her uygulamayı yeniden eşleştirin — BTCPay Server'ın kendisi, Zeus, Thunderhub, RTL, Alby ve yazdığınız tüm betikler.

LND'yi internet üzerinden de dışa açıyorsanız, TLS sertifikasını ve tüm `lnd.conf` kimlik bilgilerini aynı anda gözden geçirin.

### Lightning: diğer arka uçlar

Düğümünüze bir dizeyle kimlik doğrulaması yapan her şey yeni bir dize almalıdır:

- **Core Lightning**: bağlantı tarafından kullanılan rune'u veya erişim kimlik bilgilerini yeniden oluşturun.
- **Phoenixd**: HTTP parolasını yenileyin.
- **LNbits ve benzerleri**: yönetici ve fatura anahtarlarını iptal edip yeniden yayınlayın.
- **BTCPay Server mağaza ayarlarında** saklanan uzak düğüm bağlantı dizeleri: bunları yeni sırlarla yeniden yazın.

### BTCPay Server içinde oluşturulmuş sıcak on-chain cüzdan

BTCPay Server'ın sizin için on-chain bir cüzdan oluşturmasına izin verdiyseniz — sunucuya hiç dokunmamış anahtarlara sahip bir donanım cüzdanı bağlamanın veya bir xpub içe aktarmanın aksine — o seed bu makinede bulunuyordu.

Onu yanmış kabul edin:

1. İdeal olarak, anahtarların bir daha sunucuda durmaması için bir donanım cüzdanıyla yeni bir cüzdan oluşturun.
2. Fonları eski cüzdandan yenisine sweep edin.
3. Mağaza ayarlarındaki türetme şemasını yeni cüzdanla değiştirin.
4. Eski seed'i asla yeniden kullanmayın.

Sadece izleme kurulumlarının (xpub veya donanım cüzdanı) buna ihtiyacı yoktur: özel anahtarlar hiçbir zaman sunucuda bulunmadı. Kurulum rehberinin bunları önermesinin nedeni tam olarak budur.

### BTCPay Server hesapları ve API anahtarları

Hazır bunu yaparken:

- Örnekteki her kullanıcı hesabının parolasını değiştirin.
- Tüm Greenfield **API anahtarlarını** iptal edip yeniden yayınlayın.
- 2.4.2 sürümünün bir 2FA atlatma açığını giderdiği göz önüne alındığında, iki faktörlü kimlik doğrulamayı yeniden kaydedin.
- `Admin Dashboard > Server > Users` bölümünü açın ve beklenmeyen bir hesabın bulunmadığını kontrol edin.
- Oluşturmadığınız kayıtlar için son **payouts**, **pull payments** ve **refunds** öğelerini gözden geçirin.
- Webhook'larınızı ve onların sırlarını gözden geçirin.

## Adım 5 — Bir sonrakinden haberdar olun

Güvenlik sürümleri yalnızca onlardan haberdar olan operatörlere yardımcı olur:

- [GitHub'daki BTCPay Server sürümlerini](https://github.com/btcpayserver/btcpayserver/releases) izleyin — GitHub, bir deponun her yeni sürümünde size e-posta gönderebilir.
- Projenin duyuru kanallarını ve [resmi blogu](https://blog.btcpayserver.org/) takip edin.
- Örneğinizi hızla güncelleyebileceğiniz bir sürümde tutun: ne kadar geride kalırsanız, acil bir güncelleme o kadar sancılı hale gelir.

Kendi kendine barındırma, ödemeleriniz üzerinde size egemenlik verir. Bu egemenliğin bedeli tam olarak şudur: sürüm notlarını okumak ve yamayı uygulayan kişi olmak.
