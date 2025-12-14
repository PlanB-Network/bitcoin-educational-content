---
name: COLDCARD - Co-Sign
description: Co-Sign özelliğini keşfedin ve COLDCARD'ınızda kullanın
---

![cover](assets/cover.webp)


*Not: Bu eğitim, çoklu imza cüzdanları, Coinkite cihazları ve Sparrow wallet veya Nunchuk gibi yazılımlar konusunda zaten deneyimi olan kişilere yöneliktir.*



![video](https://youtu.be/MjMPDUWWegw)




**Neden ColdCard Ortak İmza?



Bu özellik, ColdCard (Q veya Mk4) cihazınıza bir Donanım Güvenlik Modülü (HSM) tarzında **harcama koşulları** eklemenize olanak tanıyarak fonlarınızı korurken bunlar üzerinde önemli ölçüde esneklik ve kontrol sahibi olmanızı sağlar.



Harcama koşulları örneğin şöyle olabilir:





- Büyüklük sınırları**: tek bir işlemde harcayabileceğiniz bitcoin miktarını sınırlandırın.
- Hız limitleri:** zaman birimi başına (saat, gün, hafta vb.) kaç işlem gerçekleştirebileceğinize karar verir ve bunlar arasında minimum sayıda blok gerektirir.
- Önceden onaylanmış adresler:** Yalnızca önceden onaylanmış adreslere bitcoin gönderilmesine izin verin.
- İki faktörlü kimlik doğrulama:** İnternet erişimi olan NFC özellikli bir akıllı telefon/tablet üzerinde üçüncü taraf 2FA mobil uygulamasından (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) onay gerektirir.



**Nasıl çalışır



ColdCard Mk4 veya Q cihazınıza "Harcama Politikası Anahtarı" adı verilen ve bu eğitim boyunca "C Anahtarı" olarak bahsedeceğimiz ikinci bir seed ekleyerek.


Bu ek seed'e ek olarak, bir Wallet Multisig 2-on-N oluşturmak için "Yedek Anahtar" olarak adlandıracağımız en az bir ek anahtarı (XPUB) Supply yapmanız istenecektir.



Özetle, bir Wallet Multisig oluşturacağız ve ColdCard cihazınız fonları harcamak için gereken özel anahtarlardan 2'sini içerecek, cihazın seed ana anahtarı ve "Harcama Politikası Anahtarı".



"C Anahtarı "nın imzalanması her istendiğinde, belirtilen harcama koşulları geçerli olacak ve ColdCard yalnızca işlem bu koşullara uygunsa imzalayacaktır.



Bu harcama koşullarından vazgeçmek isterseniz, bunu yapabilirsiniz:




- yedek tuşlardan biriyle ve seed eliyle veya Multisig'unuzun boyutuna bağlı olarak 2 yedek tuşla imzalayarak.
- "Ortak İmza" menüsünde "Harcama Politikası Anahtarı" veya "C Anahtarı" girilerek. **İkinci tuşa doğrudan cihaz üzerinden başvurulamaz, aksi takdirde herhangi biri yapılandırılan harcama koşullarını iptal edebilir.**




## ColdCard Ortak İmzasını Yapılandırma



![video](https://youtu.be/MjMPDUWWegw)



### 1- İşlevselliği etkinleştirin



Her şeyden önce, cihazınızın en azından en son aygıt yazılımı sürümüne sahip olduğundan emin olun:




- Mk4: v5.4.2
- S: v1.3.2Q




Mk4 veya ColdCardQ'nuzda *Gelişmiş Araçlar > ColdCard Ortak İmzalama* seçeneğine gidin.



![Co-Sign](assets/fr/01.webp)



*Aşağıdaki eğitimde, kolaylık sağlamak için ekran görüntüleri bir ColdCardQ üzerinde alınacaktır, ancak adımlar ve menüler Mk4 ve Q arasında aynıdır.*



İşlevselliğin bir özeti görüntülenir.


Anahtarları tanımlamak için kullanılan ve birazdan oluşturacağımız 2'ye 3 çoklu imzalı Wallet'de tekrar kullanacağımız terminoloji şudur:



Anahtar A = Soğuk kart ana seed


Anahtar B = Yedekleme Anahtarı


Anahtar C = Harcama Politikası Anahtarı



"ENTER "** düğmesine tıklayın.



![Co-Sign](assets/fr/02.webp)



Bir sonraki adım, hangi özel anahtarın "Harcama Politikası Anahtarı" veya "C Anahtarı" olarak işlev göreceğine karar vermektir.



Önümüzde birkaç seçenek olduğunu görebiliyoruz:





- Veya 12 kelimelik yeni bir generate cümlesi oluşturmak için **"ENTER "** tuşuna basın.





- Mevcut bir 12 kelimelik seed'i içe aktarmak için **"(1) "** üzerine tıklayın veya mevcut bir 24 kelimelik seed'i içe aktarmak için **"(2) "** seçin.





- Veya cihazınızın kasasından bir seed almak için **"(6) "** tuşuna basın.



Bu eğitimin amaçları doğrultusunda, **"(1) "** tuşuna basarak mevcut bir 12 kelimelik seed'yi içe aktarmaya karar verdik. Bu, halihazırda sahip olduğunuz ve bir yedeğine sahip olduğunuz herhangi bir seed BIP39 olabilir.



seed'inizin 12 kelimesini girmek için klavyenizi kullanın. Bu örnek için seed için geçerli olan sığır eti x 12 ifadesini seçeceğiz. Ardından **"ENTER "** tuşuna basın.


*Not: Bu seed'un bir yedeğine sahip değilseniz, harcama koşullarınızı değiştirmek için cihazınızdaki "Ortak İmza" ayarlarını artık değiştiremezsiniz*



"Ortak İmza" özelliği artık cihazda etkinleştirilmiştir. Daha sonra harcama koşullarımızı seçmemiz ve ardından çoklu imza Wallet'nin oluşturulmasını tamamlamamız gerekecek.



![Co-Sign](assets/fr/03.webp)



### 2- Harcama koşullarını veya "*harcama politikalarını*" seçin



Burada, **"C Anahtarı "** veya **"Harcama Politikası Anahtarı**" bir işlemi imzaladığında karşılanması gereken harcama koşullarını belirtiriz.



"Ortak İmza "** menüsünde **"Harcama Politikası**" üzerine tıklayın.



Daha sonra maksimum büyüklüğü, yani tek bir işlemde harcanabilecek maksimum satoshis sayısını seçebilirsiniz.



Bu örnek için, maksimum **21212** satoshis büyüklüğünü seçeceğiz. Onaylamak için **"ENTER "** üzerine tıklayın.




![Co-Sign](assets/fr/04.webp)



Daha sonra maksimum hızı, yani cihazın birim zamanda imzalayabileceği işlem sayısını ayarlamayı seçiyoruz. Bu eğitim için sınırsız hızı seçeceğiz, yani işlem sayısında sınır yok.




![Co-Sign](assets/fr/05.webp)



### 3- Oluştur Wallet Multisig 2-on-N



Cihazın **ana seed** (Anahtar A) ve **"Harcama Politikası Anahtarı "na** (Anahtar C) ek olarak Wallet Multisig için üçüncü anahtarı, yani **"Yedekleme Anahtarı "nı** (Anahtar B) seçmemiz gerekir.



"B Anahtarımız" ya SD kart aracılığıyla ya da ColdCardQ durumunda QR kodu aracılığıyla içe aktarılmalıdır.


Bunu yapmak için, "B Anahtarımızın" kullanıldığı ikinci bir ColdCard Mk4 veya Q cihazına ihtiyacımız olacak.



Bu örnek için bir ColdCard Mk4 diyelim, **"Yedekleme Anahtarınızı "** içeren bu ikinci cihazda, ana menüden **"Ayarlar "**, ardından **"Multisig Wallet"** ve son olarak **"Xpub'ı Dışa Aktar "** seçeneğine gidin.


(İkinci cihazınız bir ColdCardQ ise, Xpub'ınızı QR kodu aracılığıyla dışa aktarma seçeneğiniz de olacaktır elbette).





![Co-Sign](assets/fr/06.webp)





Bir sonraki ekranda, bir SD kart takın ve sağ alttaki **"doğrula "** düğmesine tıklayın. Ardından dosyayı SD karta kaydetmek için **"(1) "** düğmesine tıklayın.



Dosya, adında açık anahtar parmak izini (*fingerprint*) içerecek ve `ccxp-0F056943.json` biçimini alacaktır.




![Co-Sign](assets/fr/07.webp)



Ardından "Yedekleme Anahtarımızı" (B anahtarı) almak için SD kartı "ilk" ColdCardQ'ya takın.


"ColdCard Co-Signing" menüsünde "Build 2-of-N "yi seçin, ardından bir sonraki ekranda **"ENTER "a** tıklayın, ardından SD karttan "Yedek Anahtarı" almak için tekrar **"ENTER "a** tıklayın.



![Co-Sign](assets/fr/08.webp)



Bir sonraki ekranda "Hesap Numarası "nı boş bırakın (ne yaptığınızı tam olarak bilmiyorsanız) ve tekrar **"GİRİŞ "** düğmesine tıklayın.



![Co-Sign](assets/fr/09.webp)



Sonunda, aşağıdaki gibi oluşan yeni Wallet Multisig 2-sur-3'ümüzü kullanmaya hazırız:



Anahtar A= Soğuk Kart Q ana seed


Anahtar B= Yedek Anahtar (ikinci bir Coldcard cihazından yeni içe aktarıldı)


Anahtar C= Harcama Politikası Anahtarı (imzalamak için kullanılırsa, önceden tanımlanmış harcama koşullarını uygular)



## Sparrow wallet ile Ortak İmza



Gerekirse, Sparrow wallet yazılımına aşina olmak için aşağıdaki eğitimlere bakın:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- İhracat Wallet Multisig 2-sur-3'ten Sparrow wallet'e



Şimdi Wallet Multisig'yı Sparrow'ye aktarmamız gerekiyor ki ilk satoshilerimizi oraya yerleştirebilelim.



ColdCardQ'nuzun ana menüsünden **"Ayarlar "**, ardından **"Multisig Cüzdanlar "** öğesini seçin.


ColdCard'ınız tarafından bilinen Multisig cüzdan seti şimdi görüntülenir, burada yer alan anahtar sayısı "2/3" (2-sur3). Yeni oluşturduğumuz Multisig **"ColdCard Co-Sign "**ı seçin, ardından **"ColdCard Export "**a tıklayın.



![Co-Sign](assets/fr/10.webp)




Son olarak, Wallet'yi Sparrow'e aktarmanızı sağlayacak yöntemi seçin. Bizim durumumuzda, SD kartı seçeceğiz ve cihazın A yuvasına bir SD kart taktıktan sonra **"(1) "** üzerine tıklayın.



![Co-Sign](assets/fr/11.webp)



Ardından Sparrow wallet'te "Wallet'ü İçe Aktar "ı seçin.



![Co-Sign](assets/fr/12.webp)



Ardından **"Dosya İçe Aktar "** seçeneğine tıklayın. Ardından SD kartınızdaki **"export-Coldcard_Co-sign.txt "** dosyasını seçin.



![Co-Sign](assets/fr/13.webp)



Wallet'nıza Sparrow'te görüneceği gibi bir ad verin ve Wallet'nızı şifrelemek için bir parola seçin (ya da seçmeyin).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Artık ilk satoshilerimizi almaya ve Wallet'ye uyguladığımız harcama koşullarını test etmeye hazırız.



![Co-Sign](assets/fr/16.webp)



### 2- Önceden tanımlanmış harcama politikalarının test edilmesi



Bir hatırlatma olarak, Wallet Multisig için maksimum 21212 satoshis büyüklüğüne karar vermiştik. Bu, Harcama Politikası Anahtarı (Anahtar C) bir işlemi her imzaladığında, harcanan miktarın 21212 satoshiye eşit veya daha az olması durumunda geçerli olacağı anlamına geliyordu.



Hadi test edelim.


İlk olarak, Sparrow'deki "Receive" sekmesine tıklayalım ve bu eğitim boyunca kullanacağımız Wallet'e birkaç Sats bırakalım.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



O zaman 50.000 Sats işlemini simüle ederek izin verilen 21212 satoshiden daha fazlasını harcamayı deneyelim.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



İşlemi içe aktarmak için *imzasız* işlemi temsil eden QR kodunu ColdCardQ'muzla taradıktan sonra, ekranda bize gösterilen şey bu. Bir uyarı mesajı bize harcama koşullarının karşılanmadığını söylüyor. İşlemi yine de imzalarsak, 2 anahtardan yalnızca biri (cihazdaki seed ana anahtarı, ancak "Anahtar C" değil) imzalayacaktır.




![Co-Sign](assets/fr/23.webp)



Burada, işlemimizi Sparrow'e aktardıktan sonra, imzalardan yalnızca birinin işleme uygulandığını görebiliriz.



![Co-Sign](assets/fr/24.webp)




Şimdi deneyi tekrarlayalım, ancak 21.000 satoshilik bir işlem için, yani bu Wallet için belirlediğimiz maksimum büyüklükten (21212 Sats) daha az.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Bu işlemi ColdCardQ ile imzalamayı deneyelim.



Bu sefer sorun yok, herhangi bir uyarı mesajı görünmüyor ve imzalı işlemi Sparrow wallet'ye aktardığımızda, bu sefer 2 imza uygulanmış oluyor ve işlem geçerli ve dağıtıma hazır hale geliyor.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Nunchuk ile Ortak İmza



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA ve Beyaz Listedeki Adresler



Bu paragrafta, Wallet Multisig Ortak İşaretimizi Nunchuk ile kullanacağız ve nasıl gittiğini görmek için yeni harcama koşulları uygulama fırsatını değerlendireceğiz.



Gelişmiş Araçlar > ColdCard Ortak İmzalama* bölümüne gidin.


Harcama koşullarını değiştirmemizi sağlayan menüye erişmek için "Harcama Politikası Anahtarımızı" girmemiz istenir. Bizim durumumuzda 12 x "sığır eti" giriyoruz.



Bu eğitimle ilgili pratik nedenlerden dolayı 21212 Sats'lık bir büyüklük ve maksimum "Limit Hızı" tutmaya karar verdik. Öte yandan, fonlarımızın harcanabileceği adresleri dayatmak için **"Beyaz Liste Adresleri "** menüsünü kullanacağız.




![Co-Sign](assets/fr/31.webp)




Beyaz listenize eklemek istediğiniz adreslerle (2 tane seçeceğiz) ilişkili QR kodlarını tarayın ve ardından **"ENTER "** düğmesine tıklayın. Adreslerinizi art arda **"ENTER "** tuşuna basarak doğruladıktan sonra, Magnitude ve yararlanıcı adreslerine sınırlamalar uygulandığını görüyoruz.



![Co-Sign](assets/fr/32.webp)



Son olarak, "Co-Sign" tarafından sunulan olanakların tam bir resmini elde etmek için "Web 2FA" seçeneğini etkinleştirelim.


Bu özellik, ekstra bir Layer güvenliği eklemek için Google Authenticator / Ente Authenticator / Proton Authenticator / Authy 2FA / veya Aegis Authenticator gibi TOTP RFC-6238 uyumlu bir uygulama kullanmanızı sağlar.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Somut olarak, bir işlemi imzalamadan önce NFC özellikli, internete bağlı cihazınızı Coldcard'ınıza yaklaştırmanız gerekecektir. Bu sizi otomatik olarak coldcard.com web sayfasına götürecek ve burada başvurunuz için 6 haneli kodu girmeniz istenecektir. Doğru kodu girerseniz, web sayfası size ColdCardQ için taramanız gereken bir QR kodu veya cihazınızı imzalamaya yetkilendirmek için Mk4'ünüze girmeniz gereken 8 haneli bir kod gösterecektir.





![Co-Sign](assets/fr/33.webp)



İkili kimlik doğrulama uygulamanızda görüntülenen QR kodunu taradıktan ve ColdCard Co-Sign (CCC) hesabınızı ekledikten sonra, 2FA kodunuzu girerek her şeyin yolunda olduğunu doğrulamanız istenecektir.



ColdCard'ınızı NFC cihazınızın arkasına yazın.



![Co-Sign](assets/fr/34.webp)



Açılan web sayfasında, favori uygulamanızın 2FA kodunu girin. Ardından ColdCardQ'nuzla birlikte görüntülenen QR kodunu tarayın (veya Mk4'ünüzde görüntülenen 8 haneli kodu girin).



![Co-Sign](assets/fr/35.webp)




Şimdi büyüklük (21212 Sats), hedef adresler ve çift kimlik doğrulama konusunda bir sınırlama getirdik.



![Co-Sign](assets/fr/36.webp)



### 2- Wallet Multisig 2'ye 3'ü Nunchuk'a aktarın



Daha önce Sparrow ile yaptığımız gibi bu sefer de Wallet Multisig 2'ye 3'ü Nunchuk'a aktaralım.


Ayarlar > Multisig Cüzdanlar > 2/3: ColdCard Ortak İmza > ColdCard Dışa Aktarma* bölümüne gidin.



![Co-Sign](assets/fr/10.webp)



Bu kez, aynı isimli **"NFC "** ColdcardQ düğmesine tıklayarak dışa aktarma için NFC seçeneğini seçin.



![Co-Sign](assets/fr/37.webp)



Nunchuk'ta, uygulamayı ilk kez açıyorsanız, **"Mevcut Wallet'u kurtar "** seçeneğine tıklayın.



![Co-Sign](assets/fr/38.webp)



Uygulamada zaten bir Wallet'iniz varsa, sağ üstteki **"+"** işaretine ve ardından **"Mevcut Wallet'i kurtar "** işaretine tıklayın.



![Co-Sign](assets/fr/39.webp)




Ardından **"Wallet'yi COLDCARD'dan Kurtar "** ve ardından **"Multisig Wallet"** öğesini seçin.



![Co-Sign](assets/fr/40.webp)



Son olarak, Wallet'ü NFC aracılığıyla içe aktarmak için akıllı telefonunuzun arkasını ColdCardQ'nuzun ekranına dokundurun.



![Co-Sign](assets/fr/41.webp)



Hesabımız ve daha önce Sparrow wallet aracılığıyla yatırılan satoshiler geri döndü.



![Co-Sign](assets/fr/42.webp)



### 3- Önceden tanımlanmış harcama politikalarının test edilmesi



Şimdi belirlediğimiz 2 harcama koşulunu ihlal eden bir işlem yapmaya çalışalım. **Onaylanmamış bir Address'e 21212 Sats'dan fazla harcama yapmayı deneyeceğiz.** Rastgele bir Address'e 22 222 Sats göndermeyi deneyelim.



![Co-Sign](assets/fr/43.webp)



İşlem oluşturulduktan sonra, ColdCard'ınıza aktarmak için sağ üst köşedeki 3 küçük noktaya tıklayın.



![Co-Sign](assets/fr/44.webp)



Ardından **"BBQR ile Dışa Aktar "** öğesini seçin ve ColdCardQ ile görüntülenen QR kodunu tarayın.



![Co-Sign](assets/fr/45.webp)



ColdcardQ'nuz daha sonra, ekranın altına doğru ilerlediğinizde, işlemin beklendiği gibi harcama koşullarını ihlal ettiğini açıklayan bir uyarı görüntüler.



**Potansiyel bir saldırganın kısıtlamaları aşmaya çalışmasını önlemek için cihazın bize hangi harcama koşullarının söz konusu olduğunu söylemediğine dikkat edin.**




![Co-Sign](assets/fr/46.webp)



Yine de **"ENTER "** tuşuna basarak doğrulama yaparsanız, imzalanan işlemi temsil eden QR kodu görünür. Nunchuk'a aktarırsanız, yalnızca bir imzanın uygulandığını görebilirsiniz.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Tam olarak aynı işlemi gerçekleştirelim, ancak bu kez büyüklük sınırına (21212 Sats) uyan ve satoshileri önceden yapılandırdığımız 2 adresten birine harcayan bir işlemle.



Nunchuk 12121 Sats'i 2 adresimizden birine gönderiyoruz. Daha sonra işlemi daha önce yaptığımız gibi ColdCard'ımıza aktarıyoruz.



![Co-Sign](assets/fr/49.webp)




İmzalanmamış işlemi ColdCardQ'muza aktardıktan sonra, bu sefer bize ne gösterildiğine bakalım.



Bir uyarı her zaman mevcuttur, ancak bu kez ekranın altına indiğimizde, işlemin 2FA ile doğrulanması gerektiğini görüyoruz. Cihaz bizden ColdcardQ'muzu internete bağlı NFC terminalimize (akıllı telefon veya tablet) yaklaştırmamızı istiyor, biz de bunu yapıyoruz.



![Co-Sign](assets/fr/50.webp)



Akıllı telefonumuzda bir web sayfası açılıyor ve Proton Authenticator sayesinde yaptığımız 2FA kodumuzu girmemizi istiyor.



![Co-Sign](assets/fr/51.webp)





Ardından, ColdCard'ınıza işlemi imzalama yetkisi vermek için web sayfasında görünen QR kodunu tarayın.


İşlem artık 2 anahtar tarafından imzalanmıştır ve bu nedenle geçerlidir.



ColdCardQ'nuzda "Push Tx" etkinleştirilmişse, akıllı telefonunuzun arkasına basit bir dokunuşla işlemi doğrudan ağa yayınlayabilirsiniz.



![Co-Sign](assets/fr/52.webp)




Eğer "Push tx" aktif değilse, imzalanmış işlemi QR kodu olarak görüntülemek için ColdCardQ'nuzdaki "QR" düğmesine basın ve önceki örnekte olduğu gibi Nunchuk'a aktarın.



![Co-Sign](assets/fr/53.webp)



Bu kez 2 imzanın uygulandığını görüyoruz, yani işlem Bitcoin ağında yayınlanmaya hazır.



![Co-Sign](assets/fr/54.webp)




Coinkite'ın ColdCardQ ve Mk4 cihazlarına entegre Co-Sign işlevselliğinin sunduğu olanakların yanı sıra Sparrow ve Nunchuk gibi cüzdanlar aracılığıyla kullanımı hakkında genel bir bakış sunacak olan bu eğitimin sonuna geldik.