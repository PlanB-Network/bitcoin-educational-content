---
name: BitcoinVoucherBot P2P
description: BitcoinVoucherBot ile Bitcoin P2P Nasıl Alınır ve Satılır
---

![image](assets/cover.webp)



SEPA banka transferi yoluyla [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) olmadan Telegram satın almak için oluşturulan bir Bitcoin botu olan BitcoinVoucherBot'u hala duyuyoruz. Ne yazık ki, Kasım 2025 itibariyle, BitcoinVoucherBot merkezi formunda artık KYC olmadan bir hizmet olarak mevcut değildir.



Bu kılavuzda, kullanıcıların Bitcoin'i doğrudan yeni P2P (Eşler Arası) pazarında alıp satmalarına olanak tanıyan yeni uygulamanın nasıl çalıştığına bakacağız, bu nedenle KYC yok. Dijital özgürlüğü ve gizliliği giderek daha fazla tehdit eden yeni kısıtlamalara karşı koymak için geliştiriciler, kullanıcılara Bitcoin'i P2P (Peer-To-Peer) aracılığıyla yüksek derecede anonimlikle satın alma ve satma olanağı veren bu uzantıyı oluşturdu. Gelin bu yeni takas yönteminin nasıl çalıştığını birlikte görelim.



Hizmeti kullanmak için Lightning Network üzerinden transfer yapmanız gerekecektir. Bu nedenle, bu protokolü destekleyen ve para almak ve göndermek için bir "LNURL" veya "Lightning Address" kullanmanıza izin veren bir wallet'unuz olduğundan emin olun.



Desteklenen cüzdanlar arasında bulabiliriz:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Gözetim)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial with swap to Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Veya "Lightning Address" olan ve Bolt11 faturası oluşturan herhangi bir wallet. Bolt12 faturası oluşturan generate cüzdanları şu anda desteklenmemektedir. Daha fazla bilgi için [Bolt](https://planb.academy/resources/glossary/bolt) tanımına bakın.



Bu eğitim için, hemen kullanım kolaylığı göz önüne alındığında, Wallet of Satoshi'ü kullanacağız.



**Dikkat**: Wallet of Satoshi, yeni başlayanlar arasında popüler olsa da, fonlar üzerinde sınırlı kontrole sahiptir; yalnızca geçici olarak kullanın, tam egemenlik için hemen gözetim dışı bir sisteme geçin. Ekim 2025 itibariyle, otonom özel anahtarlar, modlar arasında geçiş, özel Lightning adresleri ve seed 12 kelimelik yedekleme ile iOS/Android'de (uygulamayı güncelleyin) dünya çapında istikrarlı bir kendi kendine gözetim modu içerir. Bununla birlikte, konsolidasyona kadar geçici bir çözüm olarak kalır ve uzun vadeli yönetim için wallet gözetim dışı olgunlaşmayı tercih eder.



Çok güzel! Şimdi hesabınızı oluşturma, satın alma ve satış eşleşmelerini yönetme ve kısıtlı alanınızı kullanma konusunda size adım adım rehberlik edecek yolculuğumuza başlayabiliriz.



## Wallet ve Kayıt



Öncelikle, akıllı telefonunuzda henüz yüklü değilse, Wallet of Satoshi'i indirin.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Wallet of Satoshi'yi hiç kullanmadıysanız ve nasıl çalıştığını anlamak istiyorsanız, doğru şekilde etkinleştirebilmeniz ve güvenli bir şekilde yedekleyebilmeniz için bu eğitimi izlemenizi öneririm.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Artık wallet'ünüz hazır olduğuna göre, az miktarda sats göndermeye başlayabilirsiniz. P2P (Eşler Arası) platform kaydınızı tamamlamak için bir kontrol önlemi olarak 1000 sats göndermeniz gerekeceğini unutmayın: bu, herhangi bir hayali eşleşme (dolandırıcılık) türü saldırıya karşı bir bariyer oluşturmak ve herhangi birinin herhangi bir spam filtresi olmadan kaydolmasını önlemek içindir.



![image](assets/it/02.webp)



Artık kayıt işlemine devam etmek için P2P (Eşler Arası) platformunu açabiliriz. Masaüstü bilgisayarlardan veya akıllı telefonlardaki tarayıcılardan, Telegram BitcoinVoucherBot aracılığıyla veya daha da fazla gizlilik sağlamak için .onion bağlantıları aracılığıyla giriş yapabilirsiniz.



tor .onion bağlantısını kullanmayı seçerseniz "Tor Browser "i de tavsiye ederim. Henüz bilmiyorsanız bu bağlantıdan daha fazla bilgi edinebilirsiniz:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Şimdi platforma nasıl ulaşmak istediğinizi seçin.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Masaüstü / Tarayıcı Akıllı Telefon](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Ana sayfaya yönlendirileceksiniz.



hemen başlamak için "Get Starter" düğmesine basın



![image](assets/it/03.webp)



Bir sonraki ekranda bir şifre seçmeniz ve girmeniz (kutu A) ve ardından tekrarlamanız (kutu B) gerekmektedir. Bu şifreyi hemen bir yedekleme ortamına kaydetmenizi tavsiye ederim, bu ortam "Bitwarden" gibi güvenli bir dijital cihaz olabilir:



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

veya şifrenizi bir kağıt üzerine kaydedin (**uyarı**: bu iyi bir çözüm değildir, geçici bir çözüm olarak düşünüldüğünde sorun olmayabilir).



Robot olmadığınızı belirttiğiniz doğrulama kutusunu işaretleyin (kutu C). Lütfen dikkat Ne olduğunu ve nasıl çalıştığını tam olarak bilmediğiniz sürece RSA şifrelemesini etkinleştirmeyin. Bu aşamada herhangi bir şey yapmanıza gerek yoktur. "Avatar Oluştur" ("Avatar Oluştur") seçeneğine tıklayın (kutu D).



![image](assets/it/04.webp)



Şimdi kaydı tamamlamak için 1000 sats ödemeniz gerekiyor.



1. En üstten başlayarak, ilk olarak rastgele oluşturulmuş ve son derece önemli olan "Avatar Kimliğinizi" görün Şifre konusunda size tavsiye ettiğim gibi bunu da dikkatlice kaydedin.


2. Daha sonra aşağıdaki alana "Lightning Address" kodunuzu girmelisiniz. Bu, Bitcoin satın alırsanız ödeme almanıza veya geri ödeme almanıza olanak tanıyacaktır. Wallet Of Satoshi kullanıyorsanız, al seçeneğine tıklayarak Address'nizi kopyalayabileceksiniz.


3. Robot olmadığınızı belirttiğiniz doğrulama kutusunu işaretleyin.


4. Kısıtlı alanınıza erişmek için 1000 sats ödemesini yapın. Çerçeveleyemiyorsanız, Wallet of Satoshi'ya yapıştırmanız gereken adresi kopyalamak ve fatura ödemesini tamamlamak için farenizle üzerine tıklayın (PC'de) veya parmağınızla üzerine dokunun (Tarayıcı / Telegram akıllı telefonlarda).



![image](assets/it/05.webp)



Bu sizin LNURL Address'unuz.



![image](assets/it/06.webp)



Tebrikler!!! Avatarınızı kalıcı olarak oluşturdunuz ve özeti buradan görüntüleyebilirsiniz. Bir kez daha, daha önce de önerdiğim gibi, hem Avatarınızı hem de şifrenizi dikkatlice kaydetmenizi tavsiye ederim.



"Kimlik bilgilerimi kaydettim, devam et" seçeneğine tıklayın ("Kimlik bilgilerimi kaydettim, devam et" olarak çevrilir)



![image](assets/it/07.webp)



Artık tüm ticari eşleşmeleri ayrıntılarıyla birlikte görüntüleyebileceğiniz platformun kalbindesiniz. Daha net bir görünüm için, aşağıda masaüstü bilgisayarlardan web sitesinin doğasında bulunan görüntüleri göreceksiniz.





- "Tip" ("Tip"), bunun bir "Satış" ("sell") satışı mı yoksa bir "alış" alımı mı olduğunu tanımlar
- "Miktar" ("Amount"): Eşleşme "Sat" türündeyse kullanıcının kaç adet sats sattığını veya eşleşme "Al" türündeyse kullanıcının kaç adet Bitcoin satın almak istediğini gösterir.
- "BTC Price with Margin" ("BTC Marjlı Fiyat"): işaretli değerin üzerine uygulanan marjı dikkate alan fiyatı gösterir.
- "Marj" ("Marj") piyasa fiyatına uygulanan yüzdedir, eksi işareti (-) ile piyasa fiyatında indirim alırsınız, artı işareti (+) ile piyasa fiyatına prim uygulanır.
- "Yöntem" ("Method") kullanıcının hangi yöntemle ödeme yapılmasını tercih ettiğini gösterir.
- "Yaratıcı", kullanıcı tarafından platformda kullanılan benzersiz avatardır.
- "Rep" (İtibar) Kullanıcının itibar seviyesi -5 güvenilmez ile +5 son derece güvenilir arasında değişir.
- "Durum" ("Status"): eşleşmenin durumunu gösterir. Örnek ekran görüntüsünde tüm eşleşmeler "Açık" ("Open") olarak görünmektedir.
- "Sona Erme" ("Expiration"): Maçın sona ermesine ne kadar zaman kaldığını gösterir ve kimse tarafından seçilmediyse iptal edilir.



![image](assets/it/08.webp)



Profilinize erişmek için sağ üstteki Avatarınıza tıklayın.



![image](assets/it/09.webp)



Burada Avatar adınızı, Kullanıcı Kimliğinizi, oluşturma tarihinizi ve müzakerelerdeki davranışlarınıza olumlu veya olumsuz yansıyacak olan itibarınızı görebilirsiniz.



![image](assets/it/10.webp)



Ayarlar bölümünde, kayıt sırasında girdiğiniz "Lightning Address "nizi görüntüleyebilir ve gerekirse değiştirebilirsiniz. Ayrıca, belirtildiği gibi yalnızca uygun becerilere sahipseniz ayarlanması gereken bir Açık Anahtar oluşturma seçeneğiniz de vardır. Karşı tarafınızla doğrudan bilgisayarınızdan paylaşacağınız mesajları şifrelemek için kullanılır.



Telegram Bildirim özelliği şiddetle tavsiye edilir. Etkinleştirdiğinizde, Telegram uygulamasıyla çerçevelemeniz için bir QR kodu görünecektir: bu şekilde, maçlarınızla ilgili tüm eylemler hakkında doğrudan Telegram'teki bot sohbetinde gerçek zamanlı bildirimler alacaksınız.



![image](assets/it/11.webp)



Son olarak, davet ettiğiniz kullanıcılar tarafından elde edilen kazançlarla birlikte tavsiye bölümünüzü bulursunuz. Buradan bağlantınızı veya QR kodunuzu paylaşmak için düğmeyi kullanabilir ve biraz daha aşağıda, ilgili puanla birlikte itibarınızı izlemek için bir eşleşme listesi görüntüleyebilirsiniz.



![image](assets/it/12.webp)



## Bitcoin satın almak için bir sipariş oluşturun



Pazaryerine girin: ana gezinti çubuğundan, sipariş defterini açmak için "Pazaryeri" ("Pazaryeri") sepet sembolüne tıklayın. ardından yeni bir sipariş başlatın: işlemi başlatmak için "Yeni Sipariş" düğmesine ("Yeni Sipariş") basın.



![image](assets/it/13.webp)





- Sipariş ayrıntılarını ayarlayın:
- "Bitcoin Satın Al" ("Bitcoin Satın Al") seçeneğini seçin.
- İstediğiniz sats miktarını girin.
- Fiyat marjını tanımlayın (piyasa değerinden -%20 ile +%20 arasında).
- Ödeme yöntemini seçin (Anında SEPA, vb.).
- Tercih edilen para birimini belirtir.
- Siparişi Onayla: dosyalama aşamasına geçmek için "Sipariş Oluştur"("Siparişi Onayla") üzerine tıklayın.



![image](assets/it/14.webp)



Depozito gereklidir: Siparişi etkinleştirmek için toplam tutarın %10'una eşit bir depozito ve bir hizmet ücreti gereklidir.




- Depozito ödemesi: sipariş oluşturulduğunda, sistem otomatik olarak bir Yıldırım faturası oluşturur. Depozito sadece geçicidir ve sipariş tamamlandığında iade edilir.
- Ana özellikler:
- Güvenlik depozitosu: Sipariş değerinin %10'u.
- Hizmet ücreti: platformu kullanma maliyeti.
- Zaman sınırı: Ödemeyi yapmak için 5 dakikanız var, aksi takdirde işlem sona erer.



![image](assets/it/15.webp)



Başarılı bir ödemeden sonra, emir defterde görünecek ve onu seçip kabul edebilecek tüm kullanıcılar tarafından görülebilecektir. Bir satış emri oluşturmak için tek yapmanız gereken "Bitcoin Sat" ("Sell Bitcoin") seçeneğine tıklamak, satmak istediğiniz satoshi miktarını girmek, marjı ayarlamak, ödeme yöntemini ve para birimini seçmek ve ardından güvenlik depozitosu olarak %10 depozito ile devam etmektir. Tamamlandığında, eşleşmeniz listede görünür olacaktır.



![image](assets/it/16.webp)



## Bir sipariş nasıl kabul edilir



1. Satıcılar kitaptaki mevcut tüm siparişlerin bir listesini görebilir.


2. Ayrıntıları kontrol edin: her sipariş aşağıdaki gibi bilgileri gösterir:




  - Bitcoin miktarı,
  - Fiyat üzerinden marj,
  - Ödeme yöntemi,
  - Kullanıcı itibarı.



![image](assets/it/17.webp)



3. Tüm bilgileri içeren tam sayfayı açmak için siparişin üzerine tıklayın.


4. Teklifi kabul etmek için "Bitcoin Sat" ("Bitcoin Sat") üzerine basın.



![image](assets/it/18.webp)



## Satıcı tarafından istenen depozito



Sipariş kabul edildiğinde, sistem ödeme için bir fatura oluşturur. Depozito şunları içerir:



- Siparişin toplam tutarı,



- hizmet komisyonu.



Depozito ödemesi öngörülen süre içinde yapılmalıdır, aksi takdirde işlem onaylanmayacaktır.



![image](assets/it/19.webp)



## Ödeme talimatlarının gönderilmesi



Para yatırma işlemi yapıldıktan sonra, işlem satıcının kişisel kontrol panelinde görünecek ve fiat para biriminde ödemeyi tamamlamak için alıcıya ayrıntıları vermesi gerekecektir.



1. Satıcı, aktif işlemi kendi panelinde görüntüler.


2. "Ödeme Talimatlarını Gönder" üzerine tıklayın


3. Fiat ödeme için gerekli tüm bilgileri girin (IBAN, alıcı, adres, ödeme nedeni, vb.).


4. Verileri alıcıya iletmek için "Send Message" ("Mesaj Gönder") üzerine tıklayın.



![image](assets/it/20.webp)



## Ödeme prosedürü



Alıcı, platform sohbetinde, ödemeyi fiat para biriminde yapmak için gerekli tüm verileri içeren bir mesaj alır:




- Banka bilgileri: Satıcının hesap sahibinin adı ve adresi ile IBAN.
- Tam tutar: aktarılacak tam fiat tutarı.
- Nedensel/açıklama: işleme dahil edilecek metin.
- Zaman sınırı: ödemenin tamamlanması gereken son tarih.



Transfer P2P sisteminin dışında gerçekleşir ve kişinin bankacılık kurumu aracılığıyla yapılmalıdır.



⚠️ **Önemli not:** platformdaki onay, yalnızca bankanız aracılığıyla transfer veya fiat ödemesini gerçekten ayarladıktan sonra yapılmalıdır.



![image](assets/it/21.webp)



## Ödeme fiatının onayı



Bu adım alıcı için çok önemlidir ve yalnızca ödemenin gerçekten gönderildiğini doğruladıktan sonra gerçekleştirilmelidir.



1. Veri alma: Alıcı, satıcıdan ödeme talimatlarını almıştır.


2. Ödeme uygulaması: fiat transferi kişinin banka hesabından düzenlenir.


3. Doğrulama: işlemin doğru şekilde işlendiğini kontrol edin.


4. Platformda onaylayın: işlem sayfasındaki "Fiat ödemesini onayla" ("Fiat ödemesini onayla") seçeneğine tıklayın.


"Ödeme fiatını onayla" düğmesi işlem bölümünde görünür ve yalnızca ödemenin gerçekten gönderildiğini doğruladıktan sonra kullanılmalıdır.



![image](assets/it/22.webp)



Süreçteki son adım, satıcının fiat ödemesinin alındığını teyit etmesi ve ardından sats'ların alıcıya bırakılmasıdır.



![image](assets/it/23.webp)



## Sonuç



Bu eğitimin, kendi değer deponuz için veya günlük ödemeleri hayata geçirmeye başlamak için Bitcoin ticareti yapmak veya hatta sadece satın almak için yeni bir yöntem kullanmanıza yardımcı olacağı umuduyla. Yine de, dijital dünyamızda olmak üzere olanlarla başa çıkmak için keşfedilecek bir kapı olmaya devam ediyor.



Bizi kontrol eden organlar tarafından yönetilen ilmik, giderek daha fazla kontrol edilen bir İnternet doğurmak için sıkılaşıyor. P2P satın alarak, alışverişlerinizi tamamen anonim tutacak, hiçbir iz bırakmayacak ve üçüncü taraflardan hiçbir yankı uyandırmayacaksınız.