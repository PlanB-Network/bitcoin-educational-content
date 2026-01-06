---
name: White Noise
description: Nostr ve MLS protokollerine dayalı özel, merkezi olmayan bir mesajlaşma uygulaması
---

![cover](assets/cover.webp)




## Giriş



"Zorlukların ortasında fırsatlar yatar". Albert Einstein'ın bu sözü bize sorunların kesin olmadığını, aksine içlerinde yeni ve yenilikçi çözümlerin tohumlarını barındırdığını hatırlatıyor.



Bu eğitimde sunduğumuz çözümün lansmanının arkasındaki motivasyonlar bunu mükemmel bir şekilde göstermektedir. Bu **White Noise**, zorunluluktan doğmuştur.



Kurucusu Max Hillebrand'ın *Bitcoin Magazine* tarafından bildirilen sözleriyle: "Bu projeyi alternatif eksikliği nedeniyle başlattık." Hillebrand'a göre "mevcut şifreleme uygulamaları büyük ölçekte verimsiz: bir grup görüşmesine 100 kişi eklemek şifrelemeyi önemli ölçüde yavaşlatıyor. Bu arada merkezi olmayan platformlar özel mesajlaşma sunmuyor. Son olarak, Nostr'ün açık röle ağı herkesin fikirlerini yaymasına izin veriyor, ancak doğrudan mesajların korunması önemli ölçüde yetersiz kalıyor. Özgürlüğü korumak için bu sistemleri birleştirmemiz gerektiğini fark ettik."



## White Noise nedir?



White Noise, kar amacı gütmeyen bir ekip tarafından geliştirilen açık kaynaklı bir mesajlaşma uygulamasıdır. Uygulama güvenlik, gizlilik ve ademi merkeziyetçiliği teşvik etmektedir. Geleneksel uygulamaların aksine, ne bir telefon numarası ne de bir e-posta adresi gerektirir.


White Noise, teknik temelini oluşturan iki temel protokolün - Nostr ve MLS - entegrasyonu ile ayırt edilir.



Nostr (Notes and Other Stuff Transmitted by Relays) sansüre direnmek için tasarlanmış merkezi olmayan, açık kaynaklı bir protokoldür.  Protokol röleler, anahtar çiftleri ve istemciler kullanır.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Beyaz Gürültü ile gizliliği en üst düzeye çıkarmak için kendi aktarma ayarlarınızı bile seçebilirsiniz.



MLS (Messaging Layer Security) ise mesajların uçtan uca şifrelenmesini sağlayan bir güvenlik protokolüdür. Başka bir deyişle, mesajlara yalnızca uç noktalardan, yani mesajın göndericisi ve alıcısından erişilebilir. Bu, mesajların yönlendirilmesinde yer alan rölelerin mesajların içeriğine erişemeyeceği anlamına gelir.



İşte White Noise ile en iyi bilinen mesajlaşma uygulamaları arasında hızlı bir karşılaştırma.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## White Noise ile çalışmaya başlama



### White Noise kurulumu



White Noise web sitesine] (https://www.whitenoise.chat/) gidin, ardından **İndir** seçeneğine tıklayın.



![screen](assets/fr/03.webp)



White Noise şu anda yalnızca mobil cihazlarda kullanılabilir.


Görüntülenen yeni arayüzde tuşuna basın:





- android'e indirmek istiyorsanız **Zapstore** veya **Android APK** düğmesine basın;
- iPhone kullanıyorsanız **iOS TestFlight** düğmesine basın.



![screen](assets/fr/04.webp)



Bu eğitimin amaçları doğrultusunda, bir Android indirme işlemi gerçekleştireceğiz.


Eğer **Zapstore** üzerinden indirmeyi seçerseniz, oraya yönlendirileceksiniz. Zapstore'a girdikten sonra arama çubuğuna **White Noise** yazın. Ardından **Yükle** seçeneğine tıklayarak indirmeye devam edin.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



APK dosyasını indirmeyi tercih ederseniz, akıllı telefonunuz için doğru sürümü seçmeniz için White Noise GitHub deposuna yönlendirileceksiniz.



Mevcut APK dosyaları şunlardır :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), 64 bit işlemcili yeni telefonlar için uygundur;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) 32 bit işlemcili eski telefonlar için uygundur.



Ayrıca, indirmenin bütünlüğünü doğrulamak için sadece sağlama toplamları olan **.sha256** dosyalarınız da vardır.



![screen](assets/fr/07.webp)



İndirme işlemi tamamlandıktan sonra uygulamayı kurun ve açın.



![screen](assets/fr/08.webp)



### İlk kullanıcı hesabı kurulumu



White Noise'e ilk bağlantınız için **Kayıt** düğmesine basın.



![screen](assets/fr/09.webp)



Ardından, bir profil fotoğrafı, bir isim seçerek ve kendiniz hakkında kısa bir açıklama ekleyerek profilinizi yapılandırın. Gerçek kimliğinizi (isim ve fotoğraf) doldurmak zorunda değilsiniz.


White Noise'un sizin için otomatik olarak bir ad (takma ad) seçtiğini ve bunu saklayabileceğinizi veya değiştirebileceğinizi unutmayın. Son olarak, **Son** düğmesine basın.



![screen](assets/fr/10.webp)



Konuşmalarınızın listeleneceği White Noise'nin **ana ekranına** yönlendirileceksiniz. Hesabınız artık kurulmuştur ve kullanıma hazırdır. Profilinizi paylaşabilir veya sohbet başlatmak için arkadaşlarınızı arayabilirsiniz.



![screen](assets/fr/11.webp)




### White Noise arayüzlerini keşfetme



Ana arayüzde, ekranın üst kısmında :



Sol üst köşedeki profil simgesi, profil fotoğrafınızın küçük bir resmi veya profil adınızın ilk harfidir. Hesap ayarlarınıza erişmek için üzerine tıklayın.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Sağ üst köşede, yeni bir konuşma başlatmak için simgeyi bulacaksınız.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Kullanıcı hesabı ayarları



Ayarlara erişmek için sol üst köşedeki profil simgesine basın.



![screen](assets/fr/16.webp)



Ayarlar** arayüzünün üst kısmında fotoğrafınızı ve profil adınızı, ardından da yanındaki QR kodunu kullanarak paylaşabileceğiniz genel anahtarınızı bulacaksınız.



![screen](assets/fr/17.webp)



Hemen altında, uygulama içinde başka bir profile bağlanmanızı sağlayan **Hesap değiştir** düğmesini bulacaksınız.



![screen](assets/fr/18.webp)



Ardından, aşağıdaki gibi dört (4) alt menüye sahip bir ilk bölümünüz olur:





- Profili değiştir**



Bu alt menüde profil adını, Nostr adresini (NIP-05)... değiştirebilirsiniz. Değişikliklerinizi kaydetmek için **Kaydet** düğmesine tıklamayı unutmayın.



![screen](assets/fr/19.webp)





- Profil anahtarları**



Burada genel ve özel (gizli) anahtarlarınıza erişebilirsiniz. White Noise'ün size hatırlattığı gibi, özel anahtarınız hiçbir koşulda ifşa edilmemelidir.



![screen](assets/fr/20.webp)





- Şebeke rölesi



Bu alt menüde **genel röleler** (tüm Nostr uygulamalarınızda kullanılmak üzere tanımlanan röleler), **kutu içi röleler** ve **anahtar paketi röleleri** ekleyebilir veya kaldırabilirsiniz.



Bunu yapmak için, silmek üzere bir aktarıcının önündeki **çöp** simgesine dokunun veya yeni bir tane eklemek için **+** (artı) simgesine dokunun.



![screen](assets/fr/21.webp)





- Bağlantı kesiliyor**



Hesabınızın uygulamayla bağlantısını kesmek için bu alt menüye tıklayın. Ancak özel anahtarlarınızı çevrimdışı olarak kaydettiğinizden emin olun, aksi takdirde daha sonra tekrar giriş yapamazsınız.



![screen](assets/fr/22.webp)




İkinci bir bölüm alt menüler sunar:





- Uygulama ayarları



Burada uygulamanın görünümünü (tema ve görüntüleme dili) tanımlayabilir ve hatta tehlikeye girdiğini düşündüğünüz veya kendinizi risk altında hissettiğiniz verileri silebilirsiniz.



![screen](assets/fr/23.webp)





- White Noise'e Bağış Yapın



Kâr amacı gütmeyen bir kuruluş olan White Noise'nın arkasındaki ekibe Lightning adresi veya Bitcoin sessiz ödeme adresi üzerinden bağış yaparak destek olabilirsiniz.



![screen](assets/fr/24.webp)



Son olarak, en altta **geliştirici ayarları** yer almaktadır.



![screen](assets/fr/25.webp)




## Bir konuşma başlatın



Şimdi bir konuşmanın nasıl başlatılacağına bir göz atalım. Bu yazının yazıldığı sırada White Noise üç iletişim seçeneği sunuyordu. Sırasıyla, **Özel Konuşmalar** (**Sohbet 1:1**), yani sadece siz ve bir kişi arasında, **Grup Konuşmaları** ve **Multimedya Dosyaları Gönderme** seçeneklerini inceleyeceğiz.




### Kedi 1:1



Ana arayüzden, yeni bir muhabir eklemek için, yeni bir konuşma başlatma simgesine tıklayın.


Ardından, yeni muhabirinizi bulmak için açık anahtarın QR kodunu (1) tarayın veya açık anahtarı (2) arama çubuğuna yapıştırın.



![screen](assets/fr/26.webp)



Ardından, muhabirinizle bir konuşma başlatmak için **Konuşma başlat** düğmesine dokunun. Ayrıca **Gruba ekle** düğmesine basarak muhabirinizi **takip edebilir** veya onu bir grup görüşmesine davet edebilirsiniz.



![screen](assets/fr/27.webp)



Yeni bir muhabire göndereceğiniz ilk mesaj bir davet talebine benzer. Onunla iletişim kurabilmeniz için bu talebin muhabiriniz tarafından kabul edilmesi gerekir. Eğer reddederlerse, hiçbir konuşma mümkün değildir.



![screen](assets/fr/28.webp)



Dahası, davetinizi kabul etmedikleri sürece, ilk mesajınızın içeriğini okuyamayacaklardır.



Davetinizi kabul ettiğinde, artık size yanıt verebilir ve ikiniz sorunsuz ve güvenli bir şekilde iletişim kurabilirsiniz.



![screen](assets/fr/29.webp)



Dahası, bir tartışmada ek işlevlere sahip olursunuz.



Gibi seçenekleri görüntülemek için belirli bir mesaja uzun basabilirsiniz:




- mesaja bir emoji ile tepki verin (1) ;
- mesaja cevap vermek için **Reply** (2) tuşuna basarak **doğrudan alıntı** yapın;
- mesajı **Kopyala** (3) düğmesine basarak kopyalayın.



![screen](assets/fr/30.webp)





- bir mesajı sadece sizden geliyorsa **Sil** düğmesi ile silebilirsiniz.



![screen](assets/fr/31.webp)



Bir konuşma içinde arama yapabilirsiniz.



"Görüşme bilgilerine" erişmek için ekranın üst kısmındaki muhabirin avatarına tıklayın ve **Görüşmede ara** düğmesine dokunun.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Görüntülenen arama çubuğuna aramak istediğiniz kelimeyi yazın ve aramayı başlatın. Ardından arama kelimelerinizin **bold** ile vurgulandığını göreceksiniz.



![screen](assets/fr/34.webp)




### Grup konuşmaları



White Noise üzerinde konuşma grupları oluşturulabilir.



Bunu yapmak için, yeni görüşme başlatma arayüzündeki simgeye dokunun, ardından **Yeni grup görüşmesi** seçeneğine tıklayın. Ardından, arama çubuğuna grubunuza eklemek istediğiniz ilk üyenin açık anahtarını girin.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Sonunda, bu seçenek işe yaramazsa, **Yeni bir konuşma başlat** arayüzünden, gruba eklemek istediğiniz ilk üyenin ortak anahtarını arama çubuğuna girin. Ayrıca açık anahtarıyla ilişkili QR kodunu da tarayabilirsiniz.



Bu kez, **Konuşma başlat** düğmesine dokunmak yerine, **Gruba ekle** düğmesine tıklayın.



![screen](assets/fr/37.webp)



Görüntülenen açılır menüde **Yeni grup görüşmesi** üzerine dokunun.



![screen](assets/fr/38.webp)



Ardından **Devam** tuşuna basın (açık anahtarını tekrar girmeniz gerekmez).



![screen](assets/fr/39.webp)



Grubun oluşturucusu olarak, otomatik olarak yöneticisi de siz olursunuz. Grup adı ve açıklaması** gibi grup ayrıntılarını doldurun ve ardından **Grup oluştur** düğmesine tıklayın.



![screen](assets/fr/40.webp)



İlk üye olarak eklediğiniz kullanıcı ve daha sonra eklediğiniz diğer kullanıcılar, gruba katılmaya davet eden bir bildirim alır. Gruba katılmak için **Kabul Et** seçeneğine tıklayarak kabul etmeleri gerekir.



![screen](assets/fr/41.webp)



Halihazırda sohbet ettiğiniz yeni bir üyeyi mevcut bir gruba eklemek de mümkündür. Bunu yapmak için, "konuşma bilgilerine" erişmek için ekranın üst kısmındaki muhabirin avatarına tıklayın ve **Gruba ekle** düğmesine dokunun.



![screen](assets/fr/42.webp)



Görüntülenen yeni arayüzde, onu eklemek istediğiniz grubu **işaretleyin** ve **Gruba ekle** seçeneğine dokunun. Geriye kalan tek şey gruba katılmayı kabul etmesini beklemek.



![screen](assets/fr/43.webp)



Yalnızca bir grup yöneticisinin grup bilgilerini değiştirebileceğini ve üye ekleyip çıkarabileceğini unutmayın. Ayrıca, anahtar rotasyonu yasaklı üyelerin gelecekteki mesajların şifresini çözmesini engeller.



Bir üyeyi çıkarmak için, ana grup arayüzünden, grup bilgileri arayüzüne erişmek için üstteki grup simgesine dokunun.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Ardından üyenin adına ve **Gruptan çıkar** seçeneğine tıklayın. Bu arayüzden ona bir mesaj gönderebilir, onu takip edebilir veya başka bir gruba ekleyebilirsiniz.



![screen](assets/fr/46.webp)



### Multimedya dosyaları gönderme



Şu an için White Noise'da kullanıcılar arasında sadece fotoğraf paylaşılabiliyor. İster özel bir görüşmede ister bir grup sohbetinde olun, bunu yapmak için yapmanız gereken :





- metin mesajı giriş alanının sol tarafındaki **artı (+)** sembolüne basın.



![screen](assets/fr/47.webp)





- ardından galerinize erişmek için alttaki **Fotoğraflar** işaretli kutuya tıklayın.



![screen](assets/fr/48.webp)





- gönderilecek fotoğraf(lar)ı seçin.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Hatırlanması gereken önemli noktalar



White Noise iyi düzeyde gizlilik ve üstün güvenlik sunar. Öte yandan, çok yeni bir uygulamadır, çok yaygın değildir ve henüz emekleme aşamasındadır. Dolayısıyla etkin bir sonuç çıkarmak için henüz çok erken. Kullanım sırasında birkaç arızayla karşılaşmak mümkün.



Şu anda, popüler mesajlaşma uygulamalarına kıyasla belirli işlevlerden yoksundur (sesli veya görüntülü arama yok, ses veya video multimedya dosyaları gönderme yok).



Bununla birlikte, White Noise, yüklemek (alternatif uygulama mağazaları veya APK dosyaları aracılığıyla) ve öğrenmek (Nostr protokolü ile anahtar çiftleri, istemciler ve aktarıcılar kavramına biraz hakim olmak) için biraz çaba gerektirse bile, gizliliğin çok önemli olduğu konuşmalar için (örneğin aile, yakın arkadaşlar veya ortak bir amaçtaki aktivistler ile) ilginç bir seçenek olmaya devam etmektedir.



Artık arkadaşlarınız ve ailenizle güvenli bir şekilde iletişim kurmak için White Noise'ü nasıl kullanacağınızı biliyorsunuz. Bu eğitimi faydalı bulduysanız lütfen bize bir onay verin.



Merkezi olmayan Tox protokolü üzerinden aracılar olmadan sohbet etmenizi sağlayan bir uygulama olan Tox Chat hakkındaki eğitimimizi öneririz.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3