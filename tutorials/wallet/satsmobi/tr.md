---
name: Sats.mobi

description: Telgrafla erişilebilen gözetimli bir Wallet
---

![cover](assets/cover.webp)


_Bu eğitim_ [Bitcoin Kampüsü](https://linktr.ee/bitcoincampus_) tarafından yazılmıştır


## Sats.Mobi

SatsMobi, Telegram üzerinde çalışan bir Wallet'tir ve bir Lightning Network (gözetim) Wallet'in tüm işlevlerinin yanı sıra bir dizi çok eğlenceli özelliğe sahiptir. Artık kullanılmayan LightningTipBot'un bir Fork'sından ortaya çıkmış, tüm özelliklerini miras alırken daha güncel olanları ekleyerek daha modern hale getirmiştir. LNTipBot gibi Sats.Mobi de açık kaynak felsefesini benimsemektedir. Wallet, bu [depodan] (https://github.com/massmux/SatsMobiBot) klonlanarak bağımsız olarak yapılandırılabilir ve yönetilebilir.


Basitçe kullanmayı tercih ederseniz, Telegram'da bir sohbet başlatmak bunun bir bot olduğunu ortaya çıkaracaktır.


## Ayarlar

Telegram arama çubuğundan "satsmobi" yi arayın ve [bot] (@SatsMobiBot) bağlantısı görünecektir.


**Dikkat**: Telegram üzerinden arama yapmaktan emin değilseniz, aşağıdaki [link](https://t.me/SatsMobiBot) adresini kullanarak bota güvenli bir şekilde erişin


![image](assets/it/01.webp)


Başlamak için tek yapmanız gereken _START_ tuşuna basmak


![image](assets/it/02.webp)


Wallet'i keşfetmek için sol alttaki _Menü_ öğesini seçebilirsiniz.


![image](assets/it/03.webp)


Şimdi ana komutlar arasından _/help_ seçeneğini seçin.


![image](assets/it/04.webp)


Sats.Mobi, tüm ana işlevleri listeleyen bir mesaj göstererek bizi karşılıyor. Başlangıçta, bot ayrıca Telegram'da seçilen tanıtıcıya bağlı bir LN Address oluşturdu (varsayılan olarak benzersizdir). Bu Wallet ile Sats gönderme ve alma komutlarının yanı sıra daha sonra göreceğimiz diğer işlevler de görülebilir. Ayrıca _/gelişmiş_ menüsüne de bir göz atmak ilginçtir


![image](assets/it/05.webp)


Sats.Mobi'nin ayrıca gizlilik kazanmak için kullanılmak üzere anonim bir LN Address yaratmış olması dikkat çekicidir. Bot komutlarla çalışır: sadece ilgili kelimeye tıklayın veya mesaj çubuğuna "/" eğik çizgisini ve ardından çalıştırmak istediğiniz komutu yazın. Wallet yeni oluşturulmuş olsa bile, örneğin _/transactions_


![image](assets/it/06.webp)


Bu komut, bu özel durumda sıfıra eşit olan en son işlemlerin listesini gösterir.


![image](assets/it/07.webp)


## Sats'nin Alınması

Bir Invoice oluşturma ve Sats alma komutu _/invoice_ şeklindedir. Sats.Mobi yalnızca Bitcoin'in en küçük birimi olan Satoshi'de çalışır; bu nedenle, Invoice oluşturmak için miktarı mesaj çubuğuna Sats olarak yazmak ve ardından botla sohbette göndermek gerekir.

![image](assets/it/08.webp)


Aşağıdaki örnekte, 210 Sats tutarında bir miktar almak için seçim yapılmıştır.


![cover](assets/it/09.webp)


Invoice'ün hazırlanması için birkaç dakika bekledikten sonra, metin olarak ve QR kodu olarak kullanılabilir. Invoice ödendiğinde, Wallet bakiyeyi gösterir. Herhangi bir nedenle toplam güncellenmezse, _/bakiye_ yazın ve `enter` tuşuna basın.


![image](assets/it/10.webp)


## Sats gönderiliyor


Her ne kadar Sats, kolay kolay ayrılınmaması gereken son derece değerli bir varlık olsa da, Sats.Mobi bu kısmı cazip kılıyor, bazı kısa testler (yani birkaç deneme işlemi) yapmak sorun olmayacaktır.


### Invoice Ödemesi


Bir Invoice ödemesi yapmanın en basit yolu `lnbc1xxxxx` mesaj dizesini kopyalamak ve _/pay_ komutunu yazdıktan sonra mesaj çubuğuna yapıştırmaktır. **Doğru sözdizimi** komuttan sonra bir boşluk bırakılmasını gerektirir.


![image](assets/it/11.webp)


Wallet onay isteyen bir mesaj gönderir. Öde_ seçeneğine tıklandığında Invoice'a ödeme yapılır.


![image](assets/it/12.webp)


Sats.Mobi verimli ve iyi bağlanmış bir Lightning düğümüne güvenebilir, ödemeler nadiren başarısız olur çünkü her zaman doğru yönlendirmeyi bulmayı başarır.


### Mobilden rahatça ödeme yapmak


Telegram'da gezinirken, Sats.Mobi mobil cihazlarda da mevcuttur. Mobil ödeme için en uygun işlev QR kodu taramaktır, ancak bu Wallet bağımsız bir uygulama olmadığı ve bir sosyal ağda yer aldığı için tasarım gereği bundan yoksundur. Bu nedenle Sats.Mobi, mobil deneyimi mümkün olduğunca kolaylaştırmak üzere programlanmıştır: ödeme yapmak istediğiniz Invoice'nin QR kodunun fotoğrafı gibi bir görüntüyü gerçekten de çözebilir.


Örneğin, 50 Sats'lık bir Invoice ödemek istediğinizi varsayalım.


![image](assets/it/20.webp)


Bu bize gösterildiğinde, ilgili QR kodunun fotoğrafını çekebiliriz.


![image](assets/it/21.webp)


Daha sonra mobil cihazda Telegram'ı açıyoruz ve Sats.Mobi ile sohbette QR kodunun yeni çekilmiş fotoğrafını ekliyoruz


![cover](assets/it/22.webp)


Seçildikten sonra bunu bota gönderiyoruz:


![image](assets/it/23.webp)

Sats.Mobi fotoğrafın kodunu çözer ve **doğru açıklamayla birlikte ödeme talebini** hemen sunar. Sohbet onay ister, devam etmek için _/pay_ tuşuna basmanız gerekir

![image](assets/it/24.webp)


Ödemenin işleme alınması için lütfen bir dakika bekleyin.


![image](assets/it/25.webp)


50 Sats için Invoice ödenmiştir, bu sonuç bir kamera ve entegre tarama işlevi kullanılmadan elde edilmiştir.


### Sats.Mobi in Telegram Groups


![image](assets/it/27.webp)


LNTipBot'u ünlü yapan ve Sats.Mobi'nin Telegram'a getirdiği özellikler arasında, bir gruptaki üyeler için deneyimi eğlenceli ve etkileşimli hale getiren özellik de var.

Sahipler botu grup sohbetine katılmaya davet edebilir ve ardından Sats.Mobi'yi yönetici olarak aday gösterebilir. O andan itibaren eğlence başlar, çünkü üyeler diğer kullanıcıları gruba katkılarından dolayı ödüllendirmeye başlayabilir.


- _/tip_ bir iletiye yanıt vererek bir ipucu ekler;
- _/send_ alıcı olarak bir LN Address veya bir Telegram tanıtıcısı belirterek para gönderir;
- _/faucet_ (_/advanced_ menüsünde), grubun en hızlı üyelerinin _/collect_ düğmesine tıklayarak toplayabilecekleri bir dizi ipucu oluşturmaya olanak tanır;
- _/tipjar_ (_/advanced_ menüsünde) gruptaki kullanıcılara gönderilebilecek başka bir dağıtım türü oluşturur.


Bu komutların her birinin, ana komut menüsünde açıklanan sözdizimi vardır.


Peki ya bir grubun sahibi değilsek? Sorun değil: sadece kurucudan Sats.Mobi'yi davet etmesini isteyin, grubun yöneticisi olarak ekleyin ve her şey hazır!


## Satış Noktası (POS)


Sats.Mobi ilk kez başlatıldığında, bot kullanıcı için başka bir özellik de yaratır: **POS**. "Cihaz" kullanıcı tarafından _/pos_ komutuyla veya sağ alttaki konsoldan ilgili düğmeye tıklanarak etkinleştirilir. Aslında POS, Telegram sohbetinde açılır pencere olarak açılan bir web uygulamasıdır


![image](assets/it/14.webp)


Interface, kullanıcının kişisel Telegram tanıtıcısını sol üstte görüntüler ve tüm POS'ların kullanıldığı gibi basitçe kullanılır: miktarı tuş takımına yazarak. Şimdi bir hizmet için 21 euro sent tahsil etmek istediğimizi varsayalım. Sats.Mobi'nin yalnızca yerel olarak Sats'yi yönettiğini bildiğinizden, kafanızda dönüştürmeyi yapmak kolay değildir. Aksine, POS hesap birimi olarak Euro'yu gösterir ve aynı zamanda Satoshi'daki eşdeğerini de gösterir.


![image](assets/it/15.webp)

Tamam'a tıklandığında, QR kodu aracılığıyla müşteriye gösterilebilen veya anlık mesajlaşma yoluyla bir dize olarak gönderilebilen Invoice görüntülenir, böylece ödeme yapılabilir.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Doğal olarak POS, daha önce gösterildiği gibi aynı şekilde erişilen cep telefonlarında da mevcuttur.


![image](assets/it/18.webp)


Ayrıca cep telefonu ekranında da iyi görüntülenir:


![image](assets/it/19.webp)


## Ek Özellikler


Gördüğümüz gibi, Wallet kavramını ödeme alma ve gönderme işlemlerinin ötesine taşıyan Sats.Mobi Wallet'nin teklifini tamamlayan başka özellikler de var:


- _/nostr_: Wallet'ü zap almak üzere kendi Nostr kullanıcınıza bağlamak için;
- _/cashback_: bir satın alma işleminde geri ödeme almak için bir satıcıya sunulabilecek bir kodu gösterir;
- _/buy_: bot içinde Euro karşılığında Sats satın almayı sağlayan yönlendirmeli bir prosedür başlatır;
- _/activatecard_: Sats.Mobi Wallet aracılığıyla şarj edilebilen ve bildirimlerin etkinleştirilebileceği bir NFC banka kartının etkinleştirilmesini talep etmek için;
- _/link_: bu Wallet için uzaktan kumanda olarak kullanılabilecek kendi Zeus veya Blue Wallet'iniz için bir bağlantı oluşturur.


## Sonuç

Sats.Mobi, LNBits'in daha gelişmiş işlevlerini kullanarak LNTipBot ile yaşanan deneyimleri geri getiren, kullanımı keyifli ve eğlenceli bir Wallet'tır. Ancak, **bir saklama hizmeti** olduğunu unutmamak önemlidir. Bu nedenle, çok az sayıda Sats tutmak için kullanılmalıdır, Wallet fonlarınız için bir ana Lightning Network değildir. Ayrıca, aşılmaması tavsiye edilen 500.000 Sats'e eşit bir içsel kapasite sınırı vardır.


Gözetim altında olmayan Lightning Network cüzdanları arıyorsanız, kesinlikle diğer ürünlere bakmanız tavsiye edilir.


---
### Dokümantasyon


- [Github](https://github.com/massmux/SatsMobiBot)
- Video](https://www.youtube.com/results?search_query=Sats.mobi) demosunun oynatma listesi