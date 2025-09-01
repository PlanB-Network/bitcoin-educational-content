---
name: Toksikoloji
description: Merkezi olmayan Tox protokolünde aracılar olmadan konuşmalar açın
---
![cover](assets/cover.webp)



Uçtan uca şifreleme, WhatsApp ve Telegram gibi birçok mesajlaşma uygulaması tarafından sunulan bir hizmettir. Buradaki şifreleme, mesaj gönderici tarafından gönderilmeden önce, yalnızca alıcının anahtarına sahip olduğu bir kriptografik kilitle güvence altına alındığı anlamına gelir. Bugün, aracılar olmadan güvenli, uçtan uca şifrelenmiş iletişim sunmak için Blockchain'a benzer ilkelere dayanan, tamamen merkezi olmayan, uçtan uca şifrelenmiş bir mesajlaşma uygulamasını keşfetmeye gidiyoruz: Tox Chat.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Uçtan uca şifreleme*



## Toksin nedir?



Tox, kullanıcılarının güvenliğini ve gizliliğini sağlamak için *Networking and Cryptography Library* (NaCl) teknolojisinin yanı sıra şifreleme algoritmalarının kombinasyonlarını kullanan ücretsiz (açık kaynaklı), merkezi olmayan bir iletişim protokolüdür. Tox, Exchange metin mesajları göndermenizi, sesli ve görüntülü aramalar yapmanızı, dosya paylaşmanızı ve ekranınızı arkadaşlarınızla güvenli, merkezi olmayan ve aracılar olmadan paylaşmanızı sağlar.



Tox protokolünün kullandığı teknoloji, blok zincirleri gibi eşler arası ağlara benzer ve bu da protokolün altyapısının merkezsizleştirilmesini destekler. Sosyal ağların ve uçtan uca şifrelenmiş mesajlaşma uygulamalarının aksine, Tox Chat uygulaması merkezi sunucusu olmayan merkezi olmayan bir protokol üzerine inşa edilmiştir. Tüm kullanıcılar aracısız, sansüre dayanıklı eşler arası bir ağda iletişim kurar. İletişim kurmak için her kullanıcı, dağıtılmış bir Hash tablosunda saklanan açık anahtarından türetilen benzersiz bir kimlik (ToxID) ile tanımlanır.



## Tox'a Katılın



Tox protokolünü [Tox Chat sitesi] (https://tox.chat) adresinden indirebileceğiniz bir anlık mesajlaşma istemcisi aracılığıyla kullanabilirsiniz.



![download](assets/fr/01.webp)



İşletim sisteminize bağlı olarak, . ile eşleşen bir Tox istemcisi indirip yükleyebilirsiniz:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), sadece Android'de kullanılabilen Kotlin ile yazılmış bir Tox istemcisi



![aTox](assets/fr/02.webp)





- qTox: Windows, Linux, MacOs'ta bulunan Qt Framework (C++) tabanlı [açık kaynak] (https://github.com/TokTok/qTox) adresinden bir Tox istemcisi.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic), C ile yazılmış ve komut satırı arayüzlerine sahip sistemlerde çalışan bir Tox istemcisidir.



![Toxic](assets/fr/04.webp)



Bu eğitimde, iletişim kurmak için Windows üzerinde qTox istemcilerini ve aTox'u kullanacağız.



## QTox ile çalışmaya başlama



İndirdikten sonra Tox istemcinizi kurun ve profilinizi oluşturun.



![qTox-acount](assets/fr/05.webp)



Tebrikler, Tox protokolüne yeni katıldınız. QTox yazılımında, kullanıcı adınıza tıklayarak profil bilgilerinizi bulabilirsiniz.



![profil](assets/fr/06.webp)



Özellikle, QR kodu olarak kaydedebileceğiniz ve sizinle iletişime geçmek isteyen kişilerle paylaşabileceğiniz Tox ID'nizi bulacaksınız.



Tox profil dosyanızı dışa aktarın, böylece profilinizin ve iletişim bilgilerinizin geri yüklemek için kullanabileceğiniz bir yedeğini almış olursunuz. Dışa Aktar** düğmesine tıklayın, ardından yedek dosyanızın yolunu seçin.



![export](assets/fr/07.webp)



Daha fazla** menüsünden arkadaş ekleyin, kişileri içe aktarın ve aldığınız arkadaşlık isteklerini yönetin.



![friends](assets/fr/08.webp)



Bana örneğin bu Tox ID üzerinden ulaşabilirsiniz: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Arkadaşlık isteği gönderildikten sonra, alıcının kendisiyle iletişime geçebilmeniz için isteğinizi kabul etmesi veya reddetmesi gerekecektir.



![request](assets/fr/09.webp)



Tox istemciniz, anlık mesajlaşma uygulamaları tarafından sunulan tüm seçenekleri içerir:





- Görüntülü aramalar





- Sesli aramalar





- Dosya paylaşımı





- emojiler



![chat](assets/fr/10.webp)



### Eşler arası gruplar



Tox istemcileriniz ayrıca bir grup insanla tamamen merkezi olmayan bir şekilde iletişim kurmanızı sağlar: bunlara konferans denir. Gruplar** menüsünde yeni bir konferans oluşturun veya aldığınız konferanslara katılma davetlerinin listesine bakın.



![conferences](assets/fr/11.webp)



Konferans oluşturulduktan sonra, arkadaşlarınızı Tox istemciniz üzerinden konferansa katılmaya davet edebilirsiniz. Arkadaş listenizde, davet etmek istediğiniz arkadaşınızın kullanıcı adına sağ tıklayın. Konferansa davet et** seçeneğine tıklayın, ardından oluşturduğunuz konferans adını seçin. Ayrıca **Yeni bir konferans oluştur** seçeneği ile dolaylı olarak bir konferans oluşturarak da bir arkadaşınızı davet edebilirsiniz.



⚠️ Tox istemcileri hala geliştirilme aşamasındadır, bu nedenle yazılımla etkileşim kurarken hatalarla karşılaşabilirsiniz. Konferans ve görüntülü arama işlevleri henüz Tox Android istemcisinde (aTox) mevcut değildir.



![invite](assets/fr/12.webp)



### Dosya transferleri



Dosya aktarımları** menüsünde, gönderdiğiniz ve kişilerinizden aldığınız dosyaların bir geçmişini bulacaksınız.



![files](assets/fr/13.webp)



Ayrıca, sahip olduğunuz her tartışma için dosya paylaşım yapılandırmalarınızı özelleştirebilirsiniz. Alıcınızın kullanıcı adına sağ tıklayın ve "Daha fazla ayrıntı göster" seçeneğini seçin.



![details](assets/fr/14.webp)



Interface ayrıntılarından, alıcınıza verdiğiniz yetkileri yönetebilirsiniz:





- Konferans davetlerinin otomatik olarak kabul edilmesi.





- Otomatik dosya kabulü.





- Tartışma dosyalarınız için yedekleme yolları.



![permissions](assets/fr/15.webp)



### Daha fazla parametre



Ayarlar** menüsünde Tox istemcinizin ayarlarını özelleştirebilirsiniz.





- Genel** bölümünde, Tox istemcinizin temel dilini değiştirin, dosya yedekleme yollarını ve otomatik olarak kabul edilecek maksimum dosya boyutunu tanımlayın.



![general](assets/fr/16.webp)





- Interface kullanıcısı** bölümünde, mesajlarınızın yazı tiplerini ve boyutlarını değiştirin. Tox istemcinizin temasını da değiştirebilirsiniz.



![ui](assets/fr/17.webp)





- Gizlilik** sekmesi, "Sohbet geçmişini tut" kutusunun işaretini kaldırarak geçici mesajlar tanımlamanıza olanak tanır. Ayrıca arkadaşlık istekleri tarafından spamlandığınızı fark ettiğinizde "generate rastgele NoSpam kodu" düğmesine tıklayarak Nospam kodunuzu değiştirebilirsiniz.



![privacy](assets/fr/18.webp)



### Tox'ta gizliliği ne garanti eder?



Tox protokolü, merkezi olmayan düğümlerden oluşan bir ağ oluşturmak için Dağıtılmış Hash Tablosunu kullanır. Her Tox istemcisi DHT ağının bir parçasıdır ve diğer düğümler hakkında bilgi depolar. Tox söz konusu olduğunda, DHT IP adreslerini Tox genel anahtarlarıyla (Tox ID) ilişkili değerler olarak saklar. Bu, merkezi bir sunucuyu sorgulamak zorunda kalmadan bir Tox İstemci cihazını aramayı kolaylaştırır.



Kullanıcı B** olarak adlandıracağımız `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F' kullanıcımıza yazdığınızı düşünün. Tox istemciniz bu tanımlayıcıyı Hash Dağıtılmış tablosunda bulacak ve ilişkili IP Address'yi alacaktır. IP Address bulunduğunda, Tox istemciniz **Kullanıcı B**'nin makinesiyle doğrudan, şifreli bir iletişim kanalı oluşturacak veya **Kullanıcı B**'ye ulaşmak için diğer düğümleri röle olarak kullanacaktır. Şifreleme algoritmaları, iletişim kanalından bağımsız olarak, yalnızca **Kullanıcı B**'nin mesajınızın içeriğini okuyabilmesini sağlar.



Tox'u keşfetmekten keyif aldıysanız ve gizliliğinizi güçlendirmek için nasıl yararlı olduğunu anlayabildiyseniz, lütfen bu öğreticiyi beğenmekten çekinmeyin. Ayrıca, anonim olarak e-posta almanızı ve göndermenizi sağlayan bir araç olan Simple Login hakkındaki eğitimimizi de öneririz.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41