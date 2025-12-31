---
name: Matrix
description: Güvenli, açık ve merkezi olmayan iletişim platformu Matrix'i anlamak, yapılandırmak ve kullanmak için bir kılavuz.
---

![cover](assets/cover.webp)



## Matrix nedir?



Matrix, merkezi bir kuruluşa bağımlı olmadan kullanıcılar ve uygulamalar arasında mesaj, dosya ve sesli/görüntülü arama alışverişini sağlamak için tasarlanmış **merkezi olmayan bir iletişim protokolüdür**. Geleneksel mesajlaşma platformlarından farklı olarak Matrix, e-posta ile karşılaştırılabilir bir **açık altyapıdır**: herkes bir sunucu seçebilir veya ağın geri kalanıyla alışveriş yapma yeteneğini korurken bir sunucuyu kendisi çalıştırabilir.



Matrix üç temel ilke ile ayırt edilir:



### Bir protokol, bir uygulama değil



Matrix, WhatsApp veya Telegram gibi bir uygulama değildir.


Birçok uygulamanın kullanabileceği standartlaştırılmış bir dildir.


Başka bir deyişle, FluffyChat, Cinny, Nheko ve diğerleri gibi çok çeşitli Element yazılımları aynı Matrix ağına erişim sağlar.



Bu, tam bir özgürlüğü garanti eder: temas kaybı olmadan uygulama değişikliği, arayüz çeşitliliği, tek bir tedarikçiden bağımsızlık.



![capture](assets/fr/03.webp)



### Merkezi olmayan, federe bir ağ



Matrix'in yapısı, birkaç bağımsız sunucunun birbiriyle işbirliği yaptığı bir model olan **federasyona** dayanmaktadır.


Her sunucu (_homeserver_ olarak adlandırılır) kullanıcıları, sohbet odalarını barındırabilir ve mesajları ağdaki diğer sunucularla senkronize edebilir.


Böylece:





- tüm sistemi tek bir kurum kontrol etmez;
- bir sunucu ağın geri kalanını etkilemeden ortadan kaybolabilir;
- her kuruluş veya birey kendi alanını yönetebilir.



Bu model **yüksek esneklik** sağlar ve teknolojik egemenlik değerlerini yansıtır.



![capture](assets/fr/03.webp)



### Güvenli, şifreli bir sistem



Matrix, özel alışverişler ve şifreli gruplar için **uçtan uca şifrelemeyi (E2EE)** destekler.


Mesajlar sadece katılımcılar tarafından okunabilir, ara sunucular tarafından okunamaz.


Bu yaklaşım, protokolün şeffaflığını ve kişinin kendi sunucusunu barındırma olasılığını korurken, alışverişlerin içeriğini üçüncü bir tarafa ifşa etmeden iletişim kurmayı mümkün kılar.



![capture](assets/fr/05.webp)



### Benzersiz birlikte çalışabilirlik



Matrix'in en önemli varlıklarından biri, farklı iletişim sistemleri arasında bir **köprü** olarak hareket etme yeteneğidir. Köprüler_ sayesinde, bağlantı kurmak mümkündür :





- Telegram
- WhatsApp
- Signal
- Haberci
- Gevşeklik
- Discord
- IRC, XMPP, vb.



Bu, altyapı üzerindeki kontrolü korurken çeşitli platformlara dağılmış toplulukları birleştirmeyi mümkün kılar.



![capture](assets/fr/06.webp)



## Matrix nasıl çalışır?



Bu bölüm, kullanıcıların, sunucuların ve uygulamaların bu merkezi olmayan ekosistem içinde nasıl etkileşime girdiğini anlamak için Matrix ağının iç yapısını sunmaktadır. Matrix üç temel unsura dayanmaktadır: i̇letişim kurmak için kullanılan _homeserver_, kimlikler ve _clients_.



### Sunucular: homeservers



Matrix, _homeserver_ adı verilen bağımsız sunucular üzerinde çalışır.


Her ev sunucusu :





- barındırdığı kullanıcı hesapları,
- özel sohbetler ve bu kullanıcıların katıldığı salonlar,
- diğer ağ sunucuları ile senkronizasyon.



Matrix ağına bağlı tüm ev sunucuları, paylaşılan oturma odalarından otomatik olarak mesaj ve olay alışverişi yapar. Örneğin:





- a sunucusunda kayıtlı bir kullanıcı B sunucusundaki bir kullanıcıyla sohbet edebilir,
- bir salon düzinelerce sunucuya yayılabilir,
- hiç kimse bir salon ya da bir bütün olarak bir topluluk üzerinde kontrol sahibi değildir.



Bu model son derece esnektir ve her kuruluşun veya bireyin kendi altyapısını yönetmesine olanak tanır.



### Matris tanımlayıcıları



Her kullanıcının **MXID** (_Matrix ID_) adı verilen ve bir adrese benzeyen benzersiz bir tanımlayıcısı vardır:



```bash
@nomdutilisateur:serveur.xyz
```



Şunlardan oluşur:





- önünde **@** bulunan bir kullanıcı adı
- hesabın oluşturulduğu sunucunun adı, önünde **:**



Örnekler:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Bu tanımlayıcı, kaynak sunucudan bağımsız olarak diğer tüm Matrix kullanıcılarıyla iletişim kurulmasını sağlar.



### Matris istemcileri (uygulamalar)



Matrix'i kullanmak için **client Matrix** adlı bir uygulama ile bağlanmanız gerekir.



En iyi bilinenleri şunlardır:





- Element (web, mobil, masaüstü)
- FluffyChat (mobil)
- Cinny (minimalist web/masaüstü)
- Nheko (masaüstü)



Bu uygulamalar yalnızca :





- mesajları görüntülemek için,
- metin, resim veya dosya gönderin,
- ticari fuarlara katılın veya fuarlar oluşturun,
- sesli/görüntülü arama yapabilir.



Tüm uygulamalar sunucularla aynı standartlaştırılmış protokol aracılığıyla iletişim kurar.



### Odalar ve özel mesajlar (DM)



Matrix'te değişimler **odalarda** gerçekleşir:





- bir oda genel veya özel olabilir
- iki kişi ya da binlerce kişi alabilir
- birkaç sunucu arasında paylaşılabilir
- ile başlayan benzersiz bir tanımlayıcıya sahiptir



Özel mesajlar, genellikle **DM (Doğrudan Mesajlar)** olarak adlandırılan iki katılımcılı sohbet odalarıdır.



Salon senkronizasyonu, katılımcı sunucular arasında gerçek zamanlı olarak gerçekleşir ve merkeziyetsizliği korurken sorunsuz bir deneyim sağlar.



## Neden Matrix kullanılmalı?



Matrix sadece merkezi mesajlaşma sistemlerine bir alternatif değildir: dijital egemenlik, güvenlik ve birlikte çalışabilirlik açısından gerçek ihtiyaçları karşılayan bir teknolojidir. Giderek daha fazla insanın, şirketin ve kurumun iletişim kurmak için bu protokolü seçmesinin birçok nedeni var.



### İletişimlerinizin kontrolünü yeniden ele geçirin



Çoğu mesajlaşma platformu merkezi bir modelle çalışır: sunucuları, erişimi, verileri ve kullanım kurallarını tek bir oyuncu kontrol eder. Bu model tedarikçiye tam bağımlılık anlamına gelir.


Matrix farklı bir yaklaşım benimsiyor.


Herkes hesabını nerede barındıracağını seçebilir, hatta kendi sunucusunu kurabilir. Hiçbir kuruluş bir kullanıcıyı engelleyecek, müdahaleci kimlik tespiti talep edecek veya politika değişikliği dayatacak konumda değildir.


Bu mimari hem bireylere hem de kuruluşlara özerkliklerini geri vermektedir. İletişim artık bir şirkete duyulan güvene değil, açık, belgelenmiş ve doğrulanabilir bir protokole dayanmaktadır.



### Güvenli, şifreli iletişim



Matrix, özel konuşmalar ve gruplar için uçtan uca şifrelemeyi destekler. Bu mekanizma, federasyondaki üçüncü taraf sunuculardan geçseler bile yalnızca katılımcıların mesajları okuyabilmesini sağlar.



Protokol, dağıtılmış, çok cihazlı ortamlarda güçlü güvenlik sağlamak için özel olarak tasarlanmış Megolm/Olm algoritmasını kullanır.



Bu, :





- hassas konuşmaları koruyun,
- yetkisiz erişimi önler (ana sunucudan bile),
- uzun vadede gizliliği korumak.



Şifreleme bir seçenek değildir: protokolün temel bir bileşenidir.



### Artık tek bir uygulamaya bağımlı değilsiniz



Matrix bir uygulama değil, bir protokoldür.



Bu müşteri çeşitliliği, :





- bireysel ihtiyaçlara göre uyarlanmış bir seçim,
- matrix'i her tür cihazda kullanabilme yeteneği,
- tek bir yazılıma bağımlılık yok.



Eğer bir müşteri uygun değilse veya müşterinin bakımı sona ererse, başka bir müşteri seçmeniz yeterlidir: hesap normal şekilde işlemeye devam eder.



### Farklı toplulukların birleştirilmesi ve birbirine bağlanması



Federasyon, farklı sunucuların bağımsız olarak yönetilirken birlikte çalışmasına olanak tanır.


Böylece:





- bir kuruluş kendi ev sunucusunu yönetebilir,
- bireyler genel sunuculara katılabilir,
- hepsi aynı platformdaymış gibi birbirleriyle iletişim kurabilir.



Bu esneklik, ekipler, dernekler, topluluklar, kurumlar veya açık kaynak projeleri gibi her ihtiyaca göre uyarlanmış iletişim alanları oluşturmayı mümkün kılar.



Matrix özellikle teknik çevrelerde, aktivist kolektiflerde, araştırmacılarda, hükümetlerde ve giderek artan bir şekilde Bitcoin topluluklarında popülerdir.



### Mesajlaşma ortamında benzersiz birlikte çalışabilirlik



Matrix'in en önemli varlıklarından biri, bağlantı kurabilen köprüler sayesinde borsaları **genişletme** yeteneğidir:





- WhatsApp
- Telegram
- Signal
- Gevşeklik
- Discord
- IRC
- XMPP
- ve diğer birçok platform



Matrix böylece iletişim için birleştirici bir katman haline gelir ve farklı uygulamalara dağılmış çeşitli toplulukları bir araya getirir.



Bu birlikte çalışabilirlik, parçalanmayı azaltır ve işbirliğini basitleştirir.



### Ücretsiz, açık ve sürdürülebilir bir protokol



Matrix protokolü tamamen açık kaynaklıdır ve şeffaf bir şekilde geliştirilmiştir.


Bu, çeşitli avantajları garanti eder:





- standardın sürekli olarak geliştirilmesi,
- herkesin kodu kontrol edebilmesi,
- ticari veya siyasi değişimden bağımsızlık,
- uzun vadeli dayanıklılık.



Tescilli mesajlaşma sistemlerinin aksine, Matrix'in geleceği tek bir şirkete değil, küresel bir topluluğa ve açık bir standarda bağlıdır.



## Matrix hesabını nasıl oluşturabilirim?



Bir Matrix hesabı oluşturmak basittir ve hiçbir teknik beceri gerektirmez. Kullanıcılar mevcut bir sunucuya katılabilir, bir giriş oluşturabilir ve hemen sohbete başlayabilir. Bu bölüm temel adımları özetlemektedir.



### Bir sunucu seçin (genel veya özel)



Matrix federe bir ağdır: farklı kuruluşlar, topluluklar veya bireyler tarafından yönetilen çok sayıda sunucu (homeserver) vardır. Sunucu seçimi yalnızca hesabın nerede barındırılacağını belirler, ancak tüm ağ ile iletişimi engellemez.


**İki seçenek mevcuttur:**



### - Genel bir sunucu kullanın



Bu en basit çözümdür.


Popüler sunucu örnekleri:





- _matrix.org_ (en iyi bilineni)
- _envs.net_
- tematik topluluk sunucuları (teknoloji, gizlilik, açık kaynak...)



Bu sunucular hızlı bir şekilde kayıt olmak isteyen acemi kullanıcılar için uygundur.



### - Özel bir sunucu kullanın



İçin idealdir:





- bir organizasyon,
- bir aile,
- açık kaynaklı bir proje,
- bir çalışma ekibi,
- veya egemen, kendi kendine barındırılan kullanım için.



Bu durumda, birinin sunucuyu yönetmesi gerekir (Synapse, Dendrite, Conduit...).


Hangi sunucuyu seçerseniz seçin, federasyon sayesinde kullanıcılar birbirleriyle konuşabilir.



### Adım adım hesap oluşturma



Matrix açık bir protokol olduğu için çeşitli uygulamalar tarafından erişilebilir.


Yukarıda açıklandığı gibi, gereksinimlere bağlı olarak farklı arayüzler ve işlevler sunarlar:





- Element**: tüm platformlarda kullanılabilen en eksiksiz istemci.
- FluffyChat**: basit, modern ve cep telefonları için ideal.
- Nheko**: PC'ler için hafif, ergonomik istemci.
- SchildiChat**: Ergonomik iyileştirmeler içeren Element varyantı.
- NeoChat**: KDE ekosistemine entegre edilmiştir.



İstemci seçiminin hesap üzerinde hiçbir etkisi yoktur: hepsi herhangi bir Matrix sunucusuyla çalışır.



### Klasik adımlar :





- Seçilen uygulamayı açın. Bizim durumumuzda, bunu [Element](app.element.io) ile yapacağız.
- "Bir hesap oluştur" seçeneğini seçin.



![cover-kali](assets/fr/10.webp)



Basitlik adına, **Google, Facebook, Apple, GitHub veya GitLab** kullanarak bir Matrix hesabı oluşturabilirsiniz. Bu hizmetler yalnızca hesaplarının Matrix'e erişmek için kullanıldığını bilecektir: bu bir **sosyal bağlantı** olarak bilinir.



Daha fazla gizlilik için, bir **kullanıcı adı**, bir **şifre** ve bir **e-posta adresi** seçerek manuel olarak da kayıt olabilirsiniz.



Seçilen sunucuya bağlı olarak, **kullanım şartlarının** kabul edilmesinin yanı sıra bir **captcha** gerekebilir.



Kayıt doğrulandıktan sonra bir onay e-postası gönderilir.


Hesabınızı etkinleştirmek için bağlantıya tıklamanız ve ilk Matrix konuşmalarınıza katılmak için web uygulamasına (Element) erişmeniz yeterlidir.



![cover-kali](assets/fr/11.webp)



Artık bir hesabınız var ve Element'in Web sürümünü kullanıyorsunuz.



## İlk irtibatınızı ekleyin



Matrix'te biriyle iletişim kurmak için bilmeniz gereken tek şey, **Matrix ID** adı verilen tam tanımlayıcıdır.



Örnek:



`@alice:matrix.org @bened:monserveur.bj`



### Kişi ekleme



Arkadaşlarınızı grup sohbetinize davet etmek için sağ üst köşedeki `i` dairesine tıklayın. Bu, sağ taraftaki paneli açar. Bu odadaki üyelerin listesini görüntülemek için "Kişiler" üzerine tıklayın: şu anda mevcut olanlar sadece siz olmalısınız.



![cover-kali](assets/fr/12.webp)



Kişi listesinin en üstündeki "Bu odaya davet et" seçeneğine tıklayın ve arkadaşlarınızı Matrix'te size katılmaya davet edebilmeniz için bir istem açılacaktır. Matrix'te zaten oturum açmışlarsa, Matrix ID'lerini girin. Eğer değillerse, e-posta adreslerini girin ve bize katılmaya davet edilsinler.



"Arkadaş" sistemi yoktur: bir kişi sadece sohbet açılan bir kişidir.



![cover-kali](assets/fr/13.webp)



Davet ettiğiniz kişi daveti kabul edebilir ya da reddedebilir. Kabul ederlerse, odaya katıldıklarını görmelisiniz. Ne kadar çok o kadar iyi!



![cover-kali](assets/fr/14.webp)



### Kendi sunucunuzu kurma



Matrix, kişisel bir sunucu ile birlikte kullanıldığında gerçekten kendine gelir.


Kendi ana sunucunuzu dağıtmak size :





- veriler üzerinde tam kontrol sağlamak,
- kendi kullanım kurallarını tanımlar,
- birden fazla hesap barındırın (arkadaşlar, ekip, topluluk),
- ve kısıtlama veya sansür durumunda maksimum esneklik sağlar.



**Mevcut çözümler:**





- Synapse**: tarihi ve en eksiksiz uygulama.
- Dendrite**: daha hafif, daha güçlü ve protokolün geleceği için tasarlanmıştır.
- Conduit**: dağıtımı kolay minimalist bir varyant.



**Önkoşullar:**





- bir alan adı,
- bir makine veya bir VPS,
- minimum sistem yönetimi becerileri.



Biraz yapılandırma gerektirse bile, kendi sunucunuzu yönetmek Matrix'i egemen ve dayanıklı bir araca dönüştürür.



### İlk ticari fuarlarınıza katılma



Matrix büyük ölçüde _odalara_ (oturma odalarına) dayanır.


Kamu, özel, topluluk, teknik, yerel ve uluslararası ticaret fuarları vardır.



**Bir salona katılmanın üç yolu:**



1. **Bir davet bağlantısı** aracılığıyla (genellikle `matrix.to` URL'si şeklinde).


2. **Uygulamada salon adı** aranıyor.


3. **Tam gösteri kimliğini** girerek, örn:


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Bir kez katıldıktan sonra sohbet odası, kullanılan istemciye bağlı olarak geçmiş, şifreleme, dosyalar, tepkiler ve sesli/görüntülü aramalar ile klasik bir haber grubu gibi davranır.



![capture](assets/fr/09.webp)



## Daha ileri gitmek



Temel bilgileri öğrendikten sonra, Matrix bir dizi gelişmiş olanak sunar. İster diğer mesajlaşma sistemlerine bağlanmak, ister kendi sunucunuzu barındırmak veya bir topluluk organize etmek isteyin, ekosistem çok zengindir.



### Köprüler (WhatsApp, Telegram, Signal, vb.)



Bir köprü Matrix'i diğer mesajlaşma sistemlerine bağlar.


Bununla birlikte, 'den mesaj gönderebilir ve alabilirsiniz:





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- ve diğerleri



### Köprüler ne yapabilir





- Tüm konuşmalarınızı Matrix'te merkezileştirin
- Tescilli hizmetlerle etkileşim için açık bir arayüz sağlayın
- Çok platformlu bir topluluğu tek bir konumdan yönetin



Bazı köprüler resmi, bazıları ise toplum tabanlıdır.


Departmana bağlı olarak, talep edebilirler :





- kişisel bir sunucu,
- ek bir yapılandırma,
- veya mevcut bir kamu köprüsünün kullanılması.



### Matrix'i bir Bitcoin kuruluşu, topluluğu veya projesi için kullanma



Matrix sadece kişisel bir araç değildir.


Çalışma gruplarını yapılandırmak, yerel toplulukları organize etmek veya proje iletişimini yönetmek için kullanılabilir.



**Kullanım örnekleri:**





- Açık kaynak toplulukları
- Bitcoin ve Lightning ekosistem projeleri
- Öğrenci veya geliştirici grupları
- Vatandaş kuruluşları
- Bağımsız medya
- Yerel gruplar ve dernekler



**Bu neden ilginç?





- 100 açık kaynaklı** araç
- Egemen ve merkezi olmayan** iletişim
- Alanlar **oturma salonları**, **alt gruplar**, **özel salonlar** vb. şeklinde düzenlenmiştir.
- Nextcloud, GitLab, Mattermost veya özel botlarla entegre edin
- İzinlerin ve moderasyonun ince ayarlı yönetimi



Matrix daha sonra büyük merkezi platformlardan bağımsız kalmak isteyen herhangi bir yapı için bir iletişim ayağı haline gelir.



## Sonuç



Matrix, gerçek zamanlı iletişim için modern, açık ve güvenli bir çözümü temsil eder ve geleneksel platformlara merkezi olmayan bir alternatif sunar. Birleştirilmiş mimarisi ve gelişmiş şifreleme protokolleri sayesinde, kullanıcıların akıcı, birlikte çalışabilir bir deneyimin keyfini çıkarırken verilerinin kontrolünü ellerinde tutmalarını sağlar. Kişisel, profesyonel veya topluluk kullanımı için olsun, Matrix günümüzün ihtiyaçlarına uyarlanmış iletişim ortamları oluşturmak için sağlam ve ölçeklenebilir bir çerçeve sunar.



Daha fazla bilgi edinmek ve Matrix tarafından sunulan tüm özellikleri keşfetmek için burada bulunan resmi belgelere başvurabilirsiniz:


[https://matrix.org/docs/](https://matrix.org/docs/)