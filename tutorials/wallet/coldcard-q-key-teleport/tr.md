---
name: COLDCARD Q - Key Teleport
description: Key Teleport nedir ve nasıl kullanırım?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Coinkite'ın amiral gemisi ColdCardQ cihazı ile sunduğu **Key Teleport** özelliği nedir?



**Key Teleport** 2 ColdCardQ arasında gizli verileri güvenli bir şekilde aktarmanızı sağlar. Aktarım kanalının şifrelenmesine bile gerek yoktur ve herkese açık olabilir.



Bu aktarım için kullanılabilir:





- **gW-0 ifadeleri** (ColdCard Q'nun seed ustası veya ColdCardQ'nun [seed Kasası](https://coldcard.com/docs/temporary-seeds/#seed-vault) içinde saklanan sırlar.
- **gizli notlar ve parolalar**: bu herhangi bir gizli not veya ColdCardQ'nuzdaki [Güvenli Notlar ve Parolalar] dizininin tamamı (https://coldcard.com/docs/secure_notes/) olabilir.
- **tüm ColdCardQ'nuzun bir yedeği**: bunun çalışması için bu yedeği alan ColdCardQ'nun bir seed Master'a sahip olmaması gerekir.
- gW-3 (*Kısmen İmzalanmış Bitcoin İşlemleri*) **çoklu imza şemasının** bir parçası olarak.



Bu, [cihaz donanım yazılımınızı v1.3.2Q] (https://coldcard.com/docs/upgrade/) veya daha yüksek bir sürüme yükseltmiş olmanızı gerektirir.



## Key Teleport'u nasıl kullanabilirim?



### 1- Her türlü veriyi aktarmak için



Burada, seed cümlelerinin, notların, şifrelerin veya bir ColdCardQ yedeğinin tamamının aktarımına bakacağız. Çoklu imza işlemleri için PSBT transferleri daha sonra ele alınacaktır.



#### Cihazı sırları almak için hazırlayın



ColdCardQ'nuzdaki **"Gelişmiş / Araçlar**" menüsünde **"Tuş Işınlama (başlat) "** öğesini seçin.


Bir sonraki ekranda 8 haneli bir şifre önerilmektedir, burada "20420219". Bu şifreyi göndericiye iletmeniz gerekecektir. Örneğin, bu şifreyi göndermek için sms veya favori güvenli mesajlaşma sisteminizi veya hatta bir sesli aramayı kullanın.



Ardından bir sonraki adıma geçmek için ColdCardQ'nuzdaki **"Enter**" düğmesine tıklayın.




![CCQ-key-teleport](assets/fr/01.webp)




Ekranda bir QR kodu oluşturulur. Bir kez daha, bu QR kodunu ColdCardQ "göndericisine" iletmeniz gerekecektir. Bunu yapmanın en kolay yolu bir video görüşmesidir.



**BU QR KODU ÖNCEKİ 8 HANELİ ŞİFREYİ GÖNDERMEK İÇİN KULLANILAN İLETİM KANALI ÜZERİNDEN GÖNDERMEYİNİZ**.



![CCQ-key-teleport](assets/fr/02.webp)



*İlgilenenler için, sırların güvenli olmayan kanallar üzerinden aktarılmasını sağlayan temel mekanizmayı anlamaya çalışalım*



*Aslında burada yaptığımız şey, aşağıda eklediğim BTC204 kursunda ele alınan Diffie-Hellman yöntemi aracılığıyla bir sır aktarımı başlatmaktır*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Şu anda sahip olduklarımız:*




- geçici bir anahtar çifti (Ka=G.ka, G ECDH üreteç noktası olmak üzere sırasıyla Ka ve ka genel/özel) ve 8 basamaklı bir parola üretti.
- bu şifreyi açık anahtarı (Ka) AES-256-CTR ile şifrelemek için kullanmış, ardından bu şifreyi bir iletişim kanalı A üzerinden "gönderen" **ColdCardQ**'ya iletmiştir
- son olarak, şifrelenmiş paketi, 1. kanaldan farklı ikinci bir iletişim kanalı **B** kullanarak yukarıdaki QR kodu aracılığıyla göndericiye ilettik.



#### Sırları gönderecek cihazı hazırlayın



Gönderen cihazdan, alıcı cihaz tarafından size gönderilen QR kodunu taramak için **"QR "** düğmesine tıklayın, ardından ayrı bir kanal üzerinden bir önceki adımda size iletilen 8 haneli şifreyi girin. Artık "gönderen" cihazdan veri göndermeye başlamaya hazırız.



**Lütfen 8 haneli şifreyi yanlış girmeyin, çünkü herhangi bir hata mesajı görüntülenmeyecek ve işlem devam edecektir. Ancak, son veri aktarımı başarısız olacak ve yeniden başlamanız gerekecektir**.



![CCQ-key-teleport](assets/fr/03.webp)



*Aranızda daha meraklı olanlar için, kriptografi ve gizli aktarım konusunda neler yaptığımıza bir kez daha göz atalım:*




- şifrelenmiş verileri alıcı cihazdaki QR kodunu tarayarak içe aktardık.
- daha sonra ikincil bir kanal aracılığıyla bize iletilen 8 haneli şifreyi kullanarak şifrelerini çözdük.
- bu nedenle, başlangıçta alıcı tarafından oluşturulan açık anahtara (Ka) sahibiz.
- Daha sonra gönderen cihazda yeni bir geçici anahtar çifti (Kb/kb, Kb=G.kb ile) generate oluştururuz ve bunu Ka'ya ECDH uygulamak için kullanırız. Bu nedenle kb.Ka=Ks işlemini gerçekleştiririz, burada Ks **"Oturum Anahtarı"** olarak adlandırılır.




Şimdi sizden 2 ColdCardQ arasında iletilecek sırların niteliğini seçmeniz istenir (gizli notlar, şifre, tam yedekleme, kasanızda bulunan tohumlar, seed cihaz master'ı).



![CCQ-key-teleport](assets/fr/04.webp)



Burada sırrımız **"Hızlı Metin Mesajı "** seçerek kısa bir mesaj olacaktır. Mesajınızı yazın (bizim için "PlanB Network rocks") ve ardından **"ENTER "** tuşuna basın.


Cihaz daha sonra "NE XG BT SK" örneğinde olduğu gibi **"Teleport Şifresi "** adında yeni bir rastgele şifre oluşturur.



![CCQ-key-teleport](assets/fr/05.webp)



"ENTER" tuşuna bastığınızda size yeni bir QR kodu sunulacaktır. Alıcı cihaz tarafından taranmasını sağlayın. Ve farklı bir iletişim kanalında **"Işınlanma Şifresi"ni** alıcıya iletin.



![CCQ-key-teleport](assets/fr/06.webp)



*Yine meraklıları için, bu aşamada:*




- iletilecek sırları seçtikten sonra, generate **"Teleport Password"** adında yeni bir rastgele şifre.
- daha sonra bir önceki adımda oluşturulan **"Oturum Anahtarı"**, "Ks" kullanılarak sırlar AES-256-CTR ile şifrelenir.
- kb açık anahtarımızla **"Oturum Anahtarı "** ile zaten şifrelenmiş olan paketin önüne bir Layer AES-256-CTR şifrelemesi daha ekleyerek **"Teleport Şifresi "** ile şifreliyoruz. Her şey daha sonra bir QR kodu olarak kodlanır




#### Sırların alıcı cihaza aktarımını tamamlayın



Gönderen cihaz tarafından sunulan QR kodunu visio kanalı üzerinden taramak için **"QR "** düğmesine basın. "NE XG BT SK" için **"Teleport Şifrenizi "** girmeniz istenecektir.



![CCQ-key-teleport](assets/fr/07.webp)





Daha sonra verilerin şifresi çözülür ve alıcı cihaz tarafından anlaşılabilir hale getirilir. Alınan mesaj gerçekten de "PlanB Network rocks". Hepsi bu kadar.



![CCQ-key-teleport](assets/fr/08.webp)



*Bu son aşamada gerçekte ne oldu :*?




- gönderici tarafından **"Işınlanma Şifresi"** kullanılarak iletilen verilerin şifresini çözdük.
- bu nedenle Kb açık anahtarına ve **"Oturum Anahtarı "**, "Ks" ile şifrelenmiş gizli mesajımıza sahibiz. Ancak alıcı olarak, gönderici tarafından oluşturulan Ks'yi bilmediğimiz için bunu nasıl yapabiliriz?
- İlk adımdaki **"Verileri alacak cihazı hazırlayın "** özel anahtarımız "ka "yı Kb.* genel anahtarına uygulamamız gerekir
- Aslında, ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks hesaplanarak Ks bulunur. Bu da sonunda gizli mesajı deşifre etmek için kullanılır.



### 2- PSBT'u Multisig'a aktarmak için (gelişmiş)



Bu, Wallet Multisig'inizin zaten oluşturulmuş olduğunu ve ColdCardQ cihazınızın çoklu imza işlemlerini gerçekleştirebilmek için önceden ayarlanmış olduğunu varsayar. Eğer durum böyle değilse, Coinkite web sitesinde [burada] (https://coldcard.com/docs/Multisig/) açıklamalar mevcuttur.



Çoklu imza Wallet'ün (Multisig) ne olduğuna dair hızlı bir hatırlatma.



Genellikle, Wallet fonlarınızı harcamak için, adreslerinizle ilişkili UTXO'ların kilidini açmak üzere yalnızca bir özel anahtar gerekir.


Wallet Multisig durumunda, fonları harcamak için 15'e kadar özel anahtara ve dolayısıyla 15 imzaya ihtiyaç duyulabilir. Bu "M out of N" portföyü olarak bilinir; N 1 ile 15 arasında ve M fonların harcanabilir olması için gereken imza sayısıdır. Örneğin, Wallet Multisig 5 üzerinden 3, olası 5 üzerinden en az 3 imza gerektirecektir.



Bu durumda yapılması gereken, imzalayanlar arasında koordinasyon sağlayarak "Partially Signed Bitcoin Transaction" karşılığında bir "PSBT" imzalamaktır. Bu bağlamda, "**Key Teleport**", PSBT'u ortak imzalayanlar arasında basit ve gizli bir şekilde iletmek için kullanılabilir. Ortak imzalayanlar arasında basit bir video görüşmesi işinizi görecektir.



İşte Multisig 3'lü 4'lü üzerinde nasıl yapıldığı.



**İmza sahibi 1:**



İmzalayan 1, PSBT'i içe aktarır ve imzalar. Son olarak, PSBT'i imzalayan 2'ye iletmek üzere **"Anahtar Işınlama"** kullanmak için **"T"**'ye tıklar.



![CCQ-key-teleport](assets/fr/09.webp)




"ENTER" düğmesine tıklayarak imza sahibi 2'yi seçtikten sonra, imza sahibi 2'ye başka bir iletişim kanalı aracılığıyla iletilmesi gereken bir "TELEFORT ŞİFRESİ" (burada JJ YC AB 6A) verilir. Örneğin, bir SMS veya sesli arama, ancak **görüntülü arama değil**.



Tekrar **"ENTER "** tuşuna basın ve 1 tarafından imzalanmış ve ardından "TELEPORT ŞİFRESİ" ile şifrelenmiş PSBT'yi temsil eden bir QR kodu görünür.



![CCQ-key-teleport](assets/fr/10.webp)



**İmza Sahibi 2:**



İmzacı 2, imzacı 1 tarafından kendisine sunulan QR kodunu tarar. Ardından, iletilen verilerin şifresini çözmek için ikincil iletişim kanalı üzerinden iletilen "TELEPORT ŞİFRESİ "ni girer.



İmza sahibi 2 işlemi imzalar ve ardından PSBT'ü "Key Teleport" aracılığıyla imza sahibi 3'e iletmek için **"T "ye** tıklar.


Açıkça görülüyor ki, 2 imza zaten uygulanmış. İşlemin geçerli olması için eksik olan tek şey imza sahibi 3'ün imzasıdır. **"GİRİŞ"** düğmesine tıklayarak imza sahibi 3'ü seçin.



![CCQ-key-teleport](assets/fr/11.webp)



Ve yeni bir "TELEPORT ŞİFRESİ" oluşturulur, ardından yine 1 ve 2 tarafından imzalanan PSBT'ü kodlayan ve ardından bu yeni "TELEPORT ŞİFRESİ" ile şifrelenen bir QR kodu (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**İmzacı 3:**



Yukarıdaki adımın aynısını tekrarlayın.


İmzacı 3, imzacı 2 tarafından kendisine sunulan QR kodunu tarar. Ardından ikincil iletişim kanalı tarafından iletilen "TELEPORT ŞİFRESİ "ni girer.



İmzacı 3 işlemi imzalar ve bu kez 4 imzadan 3'ü atıldığı için işlem tamamlanmış olarak gösterilir ve çeşitli ortamlar (SD Kart, NFC, QR vb.) aracılığıyla dağıtıma hazır hale gelir.



![CCQ-key-teleport](assets/fr/13.webp)



ColdCardQ'nuzun "Push Tx" özelliği etkinleştirilirse, işlemi Bitcoin ağı üzerinden yayınlamak için ColdCardQ'nuzu herhangi bir NFC özellikli İnternet bağlantılı cihazın (akıllı telefon/tablet) arkasına yapıştırmanız yeterlidir.



![CCQ-key-teleport](assets/fr/14.webp)



*Bir imza sahibinden diğerine PSBT transferleri için, "Anahtar Teleportu" her aşamada bir "Teleport Şifresi" aracılığıyla kullanılır, bu da PSBT'yı bir imza sahibinden diğerine aktarılırken şifreler. İletilen veriler fon çalmak için kullanılamayacağından, çok gizli sırların (seed, şifre vb...)* gönderilmesinde olduğu gibi bir Diffie-Hellman'a gerek yoktur.



![CCQ-key-teleport](assets/fr/15.webp)



*Kaynak: [ColdCard resmi web sitesi](https://coldcard.com/)*