---
name: BitAxe Kurulumu
description: BitAxe nasıl kurulur?
---
![video](https://youtu.be/tvLSK8v0MK8)


### Giriş


BitAxe, Skot tarafından oluşturulan ve [GitHub'da mevcut] (https://github.com/skot/bitaxe) uygun maliyetli Mining denemelerine olanak tanıyan açık kaynaklı bir projedir.


ASIC'lerde pazar lideri olan Bitmain, Bitcoin Mining için özel makineler olan ünlü Antminer S19'un işleyişini tersine mühendislikle geliştirdi. Artık bu güçlü çipleri yeni açık kaynak projelerinde kullanmak mümkün. Nerdminer'ın aksine BitAxe, düzenli olarak birkaç satoshi kazanmanızı sağlayacak bir Mining pool'ye bağlanmak için yeterli hesaplama gücüne sahiptir. Nerdminer ise yalnızca solopool adı verilen ve piyango bileti gibi işlev gören bir sisteme bağlanabilir: Block reward'in tamamını kazanma şansınız çok düşüktür.


BitAxe'in farklı çiplere ve performanslara sahip çeşitli sürümleri vardır:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

Bu eğitimde, Antminer S19XP için kullanılan BM1366 çip ile donatılmış bir BitAxe Ultra 204 kullanacağız. Bu cihaz perakendeci tarafından monte edilmiş ve flaşlanmıştır.


### [Perakendecilerin listesi bu sayfada mevcuttur](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


Genellikle Supply güç ünitesi ile birlikte satılır. Değilse, 5V jak kablosu ve en az 4A ile bir güç Supply satın almanız gerekecektir.


![signup](assets/1.webp)


### Konfigürasyon

BitAxe'inizi ilk taktığınızda, varsayılan olarak bir Wi-Fi ağına bağlanmayı deneyecektir. Beş denemeden sonra, bağlanabilmeniz ve yapılandırabilmeniz için kendi Wi-Fi ağının adını görüntüleyecektir.

Bunu yapmak için herhangi bir bilgisayar veya akıllı telefon kullanabilirsiniz. Wi-Fi ayarlarınıza gidin, yeni ağları arayın ve Bitaxe_XXXX adında bir Wi-Fi göreceksiniz. Burada, `Bitaxe_A859`. Bu Wi-Fi ağına bağlanın ve otomatik olarak bir pencere açılacaktır.


![signup](assets/3.webp)


Bu pencerede, sol üstteki üç küçük yatay çubuğa ve ardından `Ayarlar` seçeneğine tıklayın.


![signup](assets/4.webp)


Otomatik keşif sistemi olmadığı için Wi-Fi ağ bilgilerinizi manuel olarak girmeniz gerekecektir.


![signup](assets/5.webp)


Bu nedenle, Wi-Fi'nin SSID'sini, yani ağınızın adını, şifresini ve seçtiğiniz Mining pool'nın bilgilerini belirtin. Dikkatli olun, burada havuzun URL'si aynı şekilde sunulmaz. Örneğin, Braiins için sağlanan havuz URL'si şöyledir: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Ekranda görebileceğiniz gibi `stratum+tcp://` ve `:3333` kısımlarını kaldırarak sadece `eu.stratum.braiins.com` kısmını bırakmanız gerekiyor. Ardından, `Port` alanına, havuz tarafından verilen URL'nin sonundaki 4 rakamı girin, ancak `:` olmadan. Burada, bu nedenle `3333` şeklindedir.


Bu eğitimde Braiins Mining pool kullanıyoruz, ancak siz başka bir tane seçmekte özgürsünüz. Mining havuzları hakkındaki eğitimlerimizi [PlanB Network web sitesinde] bulabilirsiniz (https://planb.network/en/tutorials/Mining).


Ardından, `Kullanıcı` alanına tanımlayıcınızı ve ardından `Şifre`yi girin, genellikle `"x"` veya `"Anything123"` şeklindedir.


Çekirdek Voltajı` ayarı varsayılan olarak `1200`de bırakılmalı ve `Frekans` için de başlangıçta varsayılan değer bırakılmalıdır. Daha fazla işlem gücü elde etmek için bu ayarı daha sonra ayarlamak mümkün olacaktır. Ancak, BitAxe aşırı ısınma durumunda performansı düşürecek bir sisteme sahip olmadığından, çipin sıcaklığının 65-70°C'yi aşmamasını sağlamak önemlidir. Sıcaklığın 65°C'yi çok fazla aşması BitAxe'inize zarar verebilir.


![signup](assets/7.webp)


Tüm ayarları doğru bir şekilde girdikten sonra, alttaki `Kaydet` düğmesine tıklayın, ardından BitAxe'inizi fişten çekip tekrar takarak yeniden başlatın.

Bilgilerinizi doğru girdiyseniz, cihaz hızlı bir şekilde Wi-Fi'nize ve ardından Mining pool'a bağlanmalı ve küçük ekranında bazı bilgileri görüntülemeye başlamalıdır. Mining pool'un kontrol panelinde görünmesi muhtemelen birkaç dakika alacaktır.

### Gösterge Paneli ve Ekran


Üç farklı ekran arasında geçiş yapılacaktır. Üçüncü sayfada, gösterge tablosuna bağlanmanızı sağlayan IP Address olan `IP` bilgisini göreceksiniz. Burada, Address `192.168.1.19`dur.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


Kontrol paneline erişmek için bu Address'i internet tarayıcınıza girmeniz yeterlidir.


Gösterge panelinde, şimdi ayrıntılı olarak inceleyeceğimiz küçük ekranda görüntülenen tüm bilgileri bulacaksınız.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

Wi-Fi veya havuz ayarlarını istediğiniz zaman sorunsuz bir şekilde değiştirebilirsiniz.

Odanızın havalandırmasına ve sıcaklığına bağlı olarak, sıcaklığın 65°C'yi aşmaması için performansı artırmanız veya azaltmanız gerekebilir. Performansı artırırsanız, daha fazla satoshi kazanırsınız, ancak BitAxe'iniz de daha fazla elektrik tüketecektir!