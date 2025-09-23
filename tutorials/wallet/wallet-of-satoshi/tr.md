---
name: Wallet of Satoshi
description: Başlamak için en basit velayet Wallet
---
![cover](assets/cover.webp)

_Bu eğitim_ [Bitcoin Kampüs](https://linktr.ee/bitcoincampus_) tarafından yazılmıştır


## Satoshi'ün Wallet'inin İndirilmesi, Kurulması ve Kullanılması


Satoshi'nin Wallet'i bir Lightning Network Wallet'dir, gözetim altındadır ve kullanımı çok basittir.

BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) kursunun amaçları doğrultusunda, Redeem Lightning Network kuponları için kullanılır.


**Her zaman hatırlayın**: anahtarlariniz deği̇l, bozuk paralariniz deği̇l


Saklama cüzdanları, kullanıcıların fonları üzerinde tam kontrol sahibi olmalarına izin vermez. Yeni başlayanlar dışında normalde tavsiye edilmezler. WoS, uzun vadeli fon birikimi için değil, bir geçiş Wallet olarak veya cep harçlığı tutmak için kullanılmalıdır.


---

Wallet of Satoshi (WoS) bir saklama ürünüdür, ancak belirli bir itibarı vardır. Örneğin, likidite alma kabiliyetimizi artırmak için WoS gibi bir araca makul bir şekilde başvurabiliriz. Bizim için kanalların likiditesini yönetme "kirli işini" geçici olarak WoS'a devrediyoruz. Belirli bir miktara ulaşıldığında, WoS On-Chain'yi gözetim altında olmayan Wallet'ümüze boşaltacağız.


**WARNING⚠️: Devam etmeden önce eğitimin tamamının okunması tavsiye edilir**


### Satoshi'in Wallet'sı indiriliyor


Play Store'a gidin ve WoS uygulamasını indirin


![image](assets/it/01.webp)


**Not:** WoS sadece resmi mağazalardan indirilebilir. Cihazın işletim sistemi programlanmışsa, WoS'u açmadan önce işletim sisteminin kendisi tarafından bir doğrulama bölümü vardır. Doğrulama aşamasından sonra _Aç_'ı seçin.


![image](assets/it/02.webp)


Satoshi'nin Wallet'i aşağıdaki ekranla açılır ve _Başlat_ üzerine tıklamak gerekir


![image](assets/it/03.webp)


### WoS için Hesap Açma


Bu noktada, Wallet zaten çalışır durumdadır, ancak daha fazla güvenlik için bir oturum açma ayarlamaya devam ediyoruz: cihaz arızası veya kaybı durumunda fonları kurtarmak için gerekli olacaktır. Bu nedenle, sol üstteki menüyü seçin.


![image](assets/it/04.webp)


Sadece para birimini (Satoshi'nin Wallet'i varsayılan olarak referans para birimi olarak ABD dolarını sunar) ve tema rengini (açık/koyu) zevkinize göre ayarlamanız gereken menü penceresinin tamamı açılır. Diğer komutları kullanmayın.


WoS bir saklama aracı olduğundan, Wallet'ü Mnemonic ifadesiyle yedekleyemeyiz, ancak mobil cihazın kaybolması veya kullanılmaması durumunda _Login/Register_ seçeneğine tıklayarak WoS'un fonlarımızı kurtarmasını sağlayabiliriz

Bir e-posta Address girmemizi isteyen bir pencere açılır. Bu bir **Proton maili** olabilir (önerilir), ancak cep telefonunun kaybolması/çalınması veya hasar görmesi durumunda Wallet'teki fonları geri almamızı sağlayacağı için işlevsel olmalıdır.


![image](assets/it/08.webp)


Satoshi'nın Wallet'si belirtilen e-posta gelen kutusuna bir mesaj gönderdi.


![image](assets/it/09.webp)


Posta kutusunda, uygulama tarafından sağlanan alana yeniden yazarak girmemiz gereken iki kelime bulacağız.


- çevirmeni etkinleştirmeyin: kelimeler İngilizcedir ve öyle kalmalıdır
- büyük/küçük harfe dikkat ederek iki kelimeyi yeniden yazın


![image](assets/it/10.webp)


İki kelimeyi yazıya döktükten sonra _Tamam_ düğmesine tıklayın.


![image](assets/it/11.webp)


Sonuç, doğrulama için onay işareti sembolü ile birlikte üstte görünen bir görüntü olmalıdır.


![image](assets/it/12.webp)


ayarlar bölümündeyken, kırmızı _Login/Register_ çubuğu artık kullanıcının Address e-postasını gösteriyor.


![image](assets/it/13.webp)


### Ödemelerin Alınması


WoS'ta almak için _Receive_ seçeneğine tıklayın ve bir dizi komut görünecektir.


![image](assets/it/14.webp)


Alabilirsiniz


- gW-30-Address üzerinden **a**
- gW-32 aracılığıyla, Invoice **b** ayarlanarak
- on chain (WoS, Bitcoin ağını destekler ancak ücretli denizaltı takasları ile) **c**
- bir LNurl-p **d**'nin QR kodunu tarayarak


![image](assets/it/15.webp)


### Bir Invoice Oluşturma


_Receive_ üzerine tıklayın ve Lightning Network sembollü komutu seçin.


![image](assets/it/16.webp)


Invoice oluşturma menüsü görünür, burada tam tutarı yazmak ve bir açıklama eklemek için _Tutar Ekle_ seçeneğine tıklarız, bu örnekte "İlk Invoice'm".


![image](assets/it/17.webp)


Klavye ile miktarı ayarlıyoruz.


![image](assets/it/18.webp)


daha sonra Invoice ödemesini almak için. Alınan ödeme şu şekilde görünür:


![image](assets/it/19.webp)


### POS'tan tahsilat


Satoshi'un Wallet'ı, onu tüccarlar için özellikle uygun kılan varsayılan bir özelliğe sahiptir: POS. Nasıl etkinleştirileceğini görelim.


Ana ekrandan sağ üstteki menüyü seçin.


![image](assets/it/20.webp)


Ardından _Satış Noktası_ öğesini seçin.


![image](assets/it/21.webp)


WoS'un en son sürümünde _Keypad_'i seçtiğinizden emin olun.


![image](assets/it/22.webp)

ve ardından tuş takımına tutarı yazın, aşağıdaki örnekte 10 sent / 118 Sats'ye eşittir. Koleksiyon için bir açıklama ekleyin, bu durumda "POS ile ikinci çalışmam". Büyük bir Green düğmesi yanar ve tıklanmalıdır

![image](assets/it/23.webp)


gW-43'ü Invoice'e dönüştürmek ve örneğin bir müşteriye göstermek.


![image](assets/it/24.webp)


Bu ödeme de tahsil edilir!


![image](assets/it/25.webp)


### Ödeme gönderme


Basitlik WoS ana ekranının güçlü yanlarından biridir. Bir Invoice ödemek için _Gönder_'e tıklayın


![image](assets/it/26.webp)


İlk kullanımda, WoS kameraya erişim için izin ister


![image](assets/it/27.webp)


Bu andan itibaren kamera etkinleşir


![image](assets/it/28.webp)


Invoice'yı çerçeveleyerek, 210 Sats'lik bir ödeme talep edildiğini görüyoruz. Talep sahibi bir açıklama belirlemişse, açıklama da okunur. Bu ekran bir özet ve aynı zamanda bir onay talebidir: WoS ödemeyi göndermek için "yetki ister" ve bu yetki Green _Gönder_ düğmesine tıklanarak verilir


![image](assets/it/29.webp)


Ödeme hedefine ulaştığında, WoS bu ekran ile bildirimde bulunur


![image](assets/it/30.webp)


Ana ekrandan _Tarih_ (bakiyenin hemen altında) üzerine tıklandığında işlemlerin listesi görüntülenir


![image](assets/it/31.webp)


#### WoS hesabının kurtarılması


Şimdi, WoS'un yeni bir cihaza nasıl kurulacağını göreceğiz; bu, daha önce Wallet'un kurulu olduğu cep telefonunun çalınması, kaybolması veya çalıştırılamaması durumlarında da faydalı olacaktır. Yeniden kurulduktan sonra, az önce açıklanan hesap kayıt prosedürünü tek bir varyantla yeniden yapmanız gerekir: önceden ayarlanmış e-posta ile oturum açma talebinin sonunda, WoS şu şekilde görünecektir:


![image](assets/it/33.webp)


Bir mesaj, hesabı yeniden etkinleştirme prosedürünü içeren bir e-posta gönderildiği konusunda bizi uyarır. E-posta gelen kutunuzu açmalısınız.


**ÖNEMLİ**: e-postayı bir bilgisayardan veya her halükarda WoS hesabını kurtarmak üzere olduğunuz cihazdan farklı bir cihazdan açın. Gelen kutusunda, çerçevelemek için bize bir QR kodu gösteren bir mesaj buluyoruz


![image](assets/it/34.webp)


QR kodu çerçevelendiğinde, WoS'un ana sayfasında kurtarılan hesap, bakiye ve geçmişle birlikte görünecektir.