---
name: COLDCARD Mk4
description: COLDCARD Mk4'ü Sparrow Wallet ile kurmak ve kullanmak için bir kılavuz
---

![cover-mk4](assets/cover.webp)


**Donanım wallet'ler** sadece Bitcoin'ün özel anahtarını güvenli bir şekilde saklamak için üretilmiş fiziksel cihazlardır. Özel anahtarları çevrimdışı olarak saklarlar, bu da bilgisayar korsanlarının internet üzerinden onlara ulaşamayacağı anlamına gelir. Yazılımsal wallet'ler** çoğunlukla günlük işlemler için kullanılırken, **donanımsal wallet'ler** genellikle büyük miktarlardaki bitcoinleri uzun süre güvenli bir şekilde saklamak için kullanılır. Donanımsal wallet'ler** kullanılarak bir Bitcoin işlemi yapılırken, wallet işlemleri cihazın içinde imzalayabilir, böylece özel anahtar asla internete bağlı ortamlara maruz kalmaz.


Bu eğitimde, Coinkite tarafından üretilen en popüler donanım wallet'lerinden biri olan Coldcard Mk4'ü inceleyeceğiz. Bitcoin işlemlerini gerçekleştirmek için bu donanım wallet'yi nasıl kuracağımıza ve kullanacağımıza bir göz atacağız.


## Coldcard Mk4 Genel Bakış


Coldcard Mk4, Bitcoinkite tarafından üretilen yalnızca wallet donanımına sahip bir Coin'tür. Bu cihaz bir ekran, sayısal bir tuş takımı ve koruyucu bir kayar kapak ile donatılmıştır. Buna ek olarak, cihaz USB-C, MicroSD kart kullanarak hava boşluklu çalışma, NFC ve sanal disk modu dahil olmak üzere çeşitli bağlantı ve etkileşim yolları sunar. Mk4 ayrıca BIP39 passphrase ve hileli PIN'ler gibi gelişmiş güvenlik özellikleri içeriyor ve kullanıcılara Bitcoin'leri üzerinde daha fazla kontrol ve koruma sağlıyor.


## İlk Kurulum: PIN ve Anti-Phishing Sözcükleri


Başlamak için Coldcard Mk4 doğrudan [Coinkite'ın web sitesinden] (https://store.coinkite.com/store) satın alınabilir. Alıcılar ayrıca fiat para birimi veya Bitcoin kullanarak ödeme yapmayı da seçebilirler. Buna ek olarak, bir MicroSD karta (4 GB yeterlidir) ve USB-C kablosuyla bağlanabilen bir güç kaynağına da ihtiyacınız olacaktır (Coldcard Mk4'ün yalnızca USB-C güç giriş portu vardır). Mk4'ün dahili bir pili olmadığından, kullanılırken her zaman güç kaynağına bağlı olması gerektiğini unutmayın.


Mk4'ünüzü kurcalanmaya karşı korumalı bir torba içinde teslim alacaksınız. Lütfen çantanın zarar görmediğinden emin olun. Çantada hasar veya yırtık gibi sorun yaratabilecek bir şey tespit ederseniz, support@coinkite.com adresine bir e-posta göndererek Coinkite'ı bilgilendirebilirsiniz. Ayrıca, kurcalanmaya karşı korumalı çantanın üzerinde Mk4'ün çanta numarası olarak adlandıracağımız 12 haneli bir numara da bulabilirsiniz. Bu çanta numarası daha sonra cihazın nakliye sırasında kurcalanmadığını ve doğrudan Coinkite'dan geldiğini doğrulamak için kullanılacaktır. Çanta numarası OTP (Tek Zamanlı Programlanabilir) flash bellek kullanılarak Coldcard'ın secure element'sinde güvenli bir şekilde saklanır, yani programlandıktan sonra değiştirilemez. Cihazı ilk kez açtığınızda, ekranda görüntülenen numara çantanın üzerindekiyle eşleşmelidir. Bu, aldığınız Mk4'ün fabrikadan çıkan orijinal cihaz olduğunu ve değiştirilmediğini veya modifiye edilmediğini garanti eder. Bu doğrulama yalnızca ilk açılış sırasında cihazın bütünlüğünü onaylasa da, secure element özel anahtarlarınızı, PIN kodunuzu ve passphrase'i korumaya devam ederek herhangi bir kurcalama işleminin Bitcoin'nizi tehlikeye atmasını son derece zorlaştırır. Buna ek olarak, wallet ile ilgili verilerinizi düzgün bir şekilde güvence altına almak gibi iyi uygulamalar, Cold kartının genel güvenliğinde faydalı olacaktır. Daha fazla bilgi için, Coldcard'ın güvenlik modelini ayrıntılı olarak açıklayan bu [makaleye] (https://blog.coinkite.com/understanding-mk4-security-model/) başvurabilirsiniz.


Tuş takımı 10 sayısal düğme, bir OK (`✓`) düğmesi ve bir iptal (`✕`) düğmesinden oluşur. Bazı sayısal tuşlar navigasyon için de kullanılabilir: `5` yukarı gitmek için (`^`), `7` sola gitmek için (`<`), `8` aşağı gitmek için (`˅`) ve `9` sağa gitmek için (`>`).


![01](assets/en/01.webp)


Ambalajda herhangi bir sorun yoksa çantayı açabilirsiniz. Mk4, cihazın PIN'i, kimlik avı önleme sözcükleri ve seedphrase ile ilgili bilgileri saklamak için kullanılabilecek bir wallet yedekleme kartı ile birlikte gelecektir. Başlatma için aşağıdaki adımları izleyin:


1. Bir parça kağıt ve bir kalem hazırlayın.

2. Mk4'ü bir güç kaynağına (USB-C kablosu) bağlayın ve MicroSD kartı takın.

3. Cihaz ilk kez çalıştırıldığında, ekranda Coldcard'ın Satış ve Kullanım Koşulları ile ilgili bir mesaj görüntülenecektir. Aşağıya inin ve devam etmek için `✓` tuşuna basın.

4. Ardından, ekranda 12 haneli bir numara görüntülenecektir. Cihazın kurcalanmadığından emin olmak için bu numarayı kurcalanmaya karşı korumalı poşet üzerindeki numarayla ve kurcalanmaya karşı korumalı poşette bulunan poşet numarasının ek kopyasıyla kontrol edin. Numaralar eşleşmezse, devam etmeden önce hemen Coinkite destek birimiyle iletişime geçin. Aksi takdirde, devam etmek için `✓` tuşuna basın.


![02](assets/en/02.webp)


5. PIN Kodu Seç` öğesini seçin.

6. Bir sonraki adıma geçmek için talimatları okurken aşağı doğru ilerleyin.


![03](assets/en/03.webp)


7. Mk4'te PIN önekini oluşturun ve girin (2 ila 6 karakter uzunluğunda olmalıdır) ve not edin, ardından devam etmek için `✓` tuşuna basın.

8. Ekranda görüntülenen iki kelimeyi yazın. Bunlar kimlik avı karşıtı kelimelerdir. Devam etmek için `✓` tuşuna basın.


![04](assets/en/04.webp)


9. PIN son ekini (veya PIN'in geri kalanını, 2 ila 6 karakter uzunluğunda olmalıdır) oluşturun ve girin ve not edin. Devam etmek için `✓` tuşuna basın.

10. PIN önekinizi tekrar girin. Devam etmek için `✓` tuşuna basın.


![05](assets/en/05.webp)


11. Kimlik avı karşıtı kelimelerin 8. adımda yazdığınız kelimelerle aynı olup olmadığını kontrol edin. Devam etmek için `✓` tuşuna basın.

12. PIN son ekinizi (veya PIN'in geri kalanını) tekrar girin. Devam etmek için `✓` tuşuna basın.


![06](assets/en/06.webp)


13. Mk4'ünüzün PIN kodu ve kimlik avı önleme sözcükleri artık cihaz tarafından başarıyla oluşturulur ve saklanır.


![07](assets/en/07.webp)


Mk4'ün cihazınızı her açtığınızda sizden PIN kodunuzu girmenizi isteyeceğini unutmayın. Bu PIN olmadan Coldcard Mk4 cihazınıza erişemezsiniz. Bu nedenle, PIN ve kimlik avı önleme kelimeleri için yeterli yedekleme oluşturduğunuzdan emin olun.


## Wallet'inizin kurulumu


Bir sonraki adım wallet'nizi ayarlamaktır. Bunu yapmanız için üç yol vardır:


- Yeni bir wallet oluşturma (standart)
- Zar atarak yeni bir wallet oluşturma
- Bir wallet'in içe aktarılması


### Yeni bir wallet oluşturma (standart)


Yeni bir wallet oluşturmak için aşağıdaki adımları uygulamanız yeterlidir.


1. Yeni Wallet`i (veya `Yeni Tohum Kelimeler`i) seçin > Tercihinize bağlı olarak `12 Kelime` veya `24 Kelime (varsayılan)` seçin.


![08](assets/en/08.webp)


2. Cihaz, seçiminize bağlı olarak seedphrase olarak 12 veya 24 kelime üretecektir. Her bir kelimeyi doğru sırayla dikkatlice yazarken aşağı doğru ilerleyin. Ardından, devam etmek için `✓` tuşuna basın.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Cihaz sizden seedphrase'ınızı rastgele bir sırayla sorarak doğrulamanızı isteyecektir (örneğin, `Kelime 1?`, sonra `Kelime 5?`, sonra `Kelime 12?`, vb.) ve her soru için üç kelime seçeneği olacaktır. Adım 2'deki nota bakın ve wallet oluşturma işlemini tamamlamak için kelimeleri doğru şekilde seçin (doğru kelimeye karşılık gelen `1`, `2` veya `3` tuşlarından birine basarak).


![09](assets/en/09.webp)


4. Mk4 daha sonra NFC/Tap'i Etkinleştirmek isteyip istemediğinizi soracaktır. Şimdilik bu seçenek için `✕` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

5. Son olarak, Mk4 ayrıca USB Bağlantı Noktasını (havasız veri aktarımı için kullanılabilir) devre dışı bırakmak isteyip istemediğinizi de soracaktır. Şimdilik bu seçenek için `✓` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

6. Ekran şimdi en üstte `İmzalamaya Hazır` yazan ana menüyü görüntüleyecektir. Bu, wallet oluşturma sürecinin tamamlandığına işaret eder.


![10](assets/en/10.webp)


### Zar atarak yeni bir wallet oluşturma


Alternatif olarak, yeni seedphrase'ü entropi ile üretmeyi de seçebilirsiniz. Mk4'ün yeni üretilen seedphrase'üne güvenmiyorsanız bunu yapın.


Coldcard Mk4 üzerindeki prosedür aşağıdaki gibidir:


1. Yeni Wallet`yı (veya Yeni Tohum Kelimeler`i) seçin > Tercihinize bağlı olarak `12 Kelime Zar Atma` veya `24 Kelime Zar Atma` seçeneğini seçin.

2. Zar atışlarınızın sonuçlarını girmeniz istenecektir. Her zar atışı wallet oluşturma sürecine rastgelelik katarak seedphrase'nizin tamamen güvenli ve öngörülemez bir şekilde oluşturulmasını sağlar. Minimum zar sayısı 12 kelimelik seedphrase için 50 ve 24 kelimelik seedphrase için 99'dur. En az 99 zar atma değeri girdikten sonra `✓` tuşuna basın.


![11](assets/en/11.webp)


3. Cihaz, seçiminize bağlı olarak seedphrase olarak 12 veya 24 kelime üretecektir. Her bir kelimeyi doğru sırayla dikkatlice yazarken aşağı doğru ilerleyin. Ardından, devam etmek için `✓` tuşuna basın.

4. Cihaz sizden seedphrase'nizi rastgele bir sırayla sorarak doğrulamanızı isteyecektir (örneğin, `Kelime 1?`, sonra `Kelime 5?`, sonra `Kelime 12?`, vb.) ve her soru için üç kelime seçeneği olacaktır. Adım 3'teki nota bakın ve wallet oluşturma işlemini tamamlamak için kelimeleri doğru şekilde seçin (doğru kelimeye karşılık gelen `1`, `2` veya `3` tuşlarından birine basarak).


![12](assets/en/12.webp)


5. Mk4 daha sonra NFC/Tap'i Etkinleştirmek isteyip istemediğinizi soracaktır. Şimdilik bu seçenek için `✕` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

6. Son olarak, Mk4 ayrıca USB Bağlantı Noktasını (havasız veri aktarımı için kullanılabilir) devre dışı bırakmak isteyip istemediğinizi de soracaktır. Şimdilik bu seçenek için `✓` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

7. Ekran şimdi en üstte `İmzalamaya Hazır` yazan ana menüyü görüntüleyecektir. Bu, wallet oluşturma sürecinin tamamlandığına işaret eder.


![13](assets/en/13.webp)


### Bir wallet'ü içe aktarma


Son seçenek ise bir wallet'i içe aktarmanızdır. Bunu, zaten sahip olduğunuz bir wallet'ten bir seedphrase kurtarmak istiyorsanız yapabilirsiniz. Bu adımları takip edebilirsiniz:


1. Mevcut Olanı İçe Aktar`ı seçin.

2. seedphrase'nızın kelime sayısına bağlı olarak `24 Kelime', `18 Kelime' veya `12 Kelime'yi seçin.


![14](assets/en/14.webp)


3. Coldcard Mk4 daha sonra size her bir kelimenin ardışık sırada ne olduğunu soracaktır. Her kelime için, her kelimenin ön ekini bulana kadar aşağı veya yukarı gidin. Cihaz, siz doğru kelimeyi bulana kadar olasılıkları daraltacaktır. Bunu diğer kelimeler için de yapın.

4. Son kelime için, Coldcard Mk4 sadece sınırlı sayıda olası kelime gösterecektir. Hiç eşleşme yoksa, kelimeleri yanlış girmiş olabilirsiniz. Aksi takdirde, seedphrase'inizdeki kelimeyle eşleşen kelimeyi seçin.


![15](assets/en/15.webp)


5. Mk4 daha sonra NFC/Tap'i Etkinleştirmek isteyip istemediğinizi soracaktır. Şimdilik bu seçenek için `✕` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

6. Son olarak, Mk4 ayrıca USB Bağlantı Noktasını (havasız veri aktarımı için kullanılabilir) devre dışı bırakmak isteyip istemediğinizi de soracaktır. Şimdilik bu seçenek için `✓` seçeneğini seçin. Bu, ileride ayarlardan değiştirilebilir.

7. Ekran şimdi en üstte `İmzalamaya Hazır` yazan ana menüyü görüntüleyecektir. Bu, wallet oluşturma sürecinin tamamlandığına işaret eder.


![16](assets/en/16.webp)


seedphrase'in wallet'nizi kurtarmak için tek erişim olduğunu unutmayın. seedphrase'inizin bir yedeğini oluşturun ve güvenli bir yerde saklayın. **Anahtarlarınız değil, paralarınız değil**, seedphrase'inize sahip olan kişi bitcoinlerinize erişebilir!


## passphrase'ünüzün kurulumu


Bitcoin'daki en iyi uygulamalardan biri passphrase kullanmaktır. passphrase, seedphrase'e ek olarak 13. veya 25. kelime olarak işlev görür. Bunu farklı kılan şey, seedphrase önceden belirlenmiş 2048 kelimelik bir listeden seçilirken, istediğiniz ifadeyi seçebilmenizdir. Varsayılan olarak, wallet'nizi ayarladıktan sonra, boş bir passphrase ile bir wallet ile başlayacaksınız. Boş olmayan bir passphrase ayarlamak için aşağıdaki adımları uygulamanız yeterlidir:


1. Parola'ya gidin.

2. passphrase hakkındaki açıklamayı okumak için aşağı inin, ardından devam etmek için `✓` tuşuna basın.

3. İfadeyi Düzenle'yi seçin.


![17](assets/en/17.webp)


4. passphrase'unuzu girin:


   - Karakter türünü seçmek için `1` (harfler), `2` (rakamlar) veya `3` (semboller) tuşlarına basın.
   - Küçük ve büyük harfler arasında geçiş yapmak için `4` tuşuna basın (yalnızca harf girerken kullanılabilir).
   - passphrase'inizin karakterini seçmek için `^` veya `˅` tuşlarını kullanarak gezinin.
   - Karakterler arasında hareket etmek için `<` veya `>` kullanarak gezinin. Boşluk eklemek için de `>` kullanabilirsiniz.
   - Karakterleri silmek için `✕` tuşuna basın.
   - passphrase'i düzenlemeyi bitirdiğinizde `✓` düğmesine basın.

5. Ayrıca, diğer seçenekler aşağıdaki işlevlere sahiptir:


   - Kelime Ekle veya Sayı Ekle, düzenlemekte olduğunuz passphrase'ye harf/rakam eklemek için kullanılabilir.
   - Düzenlemekte olduğunuz passphrase'ü sıfırlamak için `Clear ALL` (Tümünü Temizle) düğmesine basın.
   - Ana menüye geri dönmek için `CANCEL` tuşuna basın.

6. passphrase'ünüzü yedek olarak yazın.

7. Yeni ayarladığınız passphrase ile wallet'ya erişmek için `APPLY` tuşuna basın.

8. Mk4 daha sonra 8 karakter uzunluğunda bir ana anahtar parmak izi gösterecektir. Bu, wallet'nin "kimliği" olarak kabul edilebilir. Bu parmak izini not edin ve devam etmek için `✓` tuşuna basın.


![18](assets/en/18.webp)


9. Şimdi wallet, girdiğiniz passphrase ile birlikte wallet'un ana menüsünü görüntüleyecektir.

10. Bir wallet'in size yanlış passphrase girdiğinizi söylemeyeceğini unutmamak önemlidir, çünkü her passphrase benzersiz bir kimliğe (ana anahtar parmak izi) sahip her bir wallet'e karşılık gelir. Bu nedenle, aynı passphrase'i tekrar girmek ve doğru girdiğinizden emin olarak aynı wallet parmak izini üretip üretmediğini kontrol etmek iyi bir uygulamadır. Bunu yapmak için 11 ila 14. Adımları uygulayın.

11. Ana menüde, "Ana Bilgisayarı Geri Yükle "yi seçin ve ardından "✓"ya basın. Şimdi boş passphrase ile wallet'ün ana menüsüne geri döndünüz.


![19](assets/en/19.webp)


12. Tekrar `Passphrase` seçeneğine gidin, ardından devam etmek için `✓` tuşuna basın.

13. Adım 6'da yazdığınız passphrase'ü tekrar girin ve ardından `UYGULA'ya basın.

14. 8 karakter uzunluğundaki ana anahtar parmak izini Adım 8'de yazdığınız parmak iziyle karşılaştırın. Her iki parmak izi de eşleşmiyorsa, yanlış karakterler yazmış olabilirsiniz. Bunun yerine yeni bir passphrase seçebilir ve işlemi Adım 1'den itibaren tekrarlayabilirsiniz. Ancak her iki parmak izi de eşleşirse, passphrase'i doğru girdiğiniz anlamına gelir.

15. Seçtiğiniz passphrase ile wallet kullanıma hazırdır.


## Wallet'u Sparrow'e Aktarma


Diğer donanım wallet'lar gibi, Coldcard Mk4 de kendi başına kullanılamaz. Arayüz görevi gören bir wallet yazılımı ile bağlanması gerekir. wallet yazılımı bakiyenizi görüntülemenizi, işlem oluşturmanızı ve adresleri yönetmenizi sağlarken, Coldcard özel anahtarlarınızı asla açığa çıkarmadan bu işlemleri güvenli bir şekilde imzalar.


Bu eğitimde, arayüz olarak Sparrow Wallet kullanacağız. wallet'ü dışa aktarma prosedürü aşağıdaki gibidir:


1. Mk4'e bir MicroSD kart takılı olduğundan emin olun.

2. Dışa aktarmak istediğiniz passphrase ile wallet üzerinde "passphrase'inizi ayarlama" adımlarını gerçekleştirin. wallet'yı boş passphrase ile dışa aktarmak istiyorsanız, bu adımı atlayabilirsiniz.

3. Gelişmiş/Araçlar`a gidin > `Wallet`yi Dışa Aktar`ı seçin > `Jenerik JSON`i seçin > Talimatları okurken aşağı kaydırın ve ardından `✓`ya basın.


![20](assets/en/20.webp)


4. Mk4 şimdi MicroSD kartta `.json` formatında bir dosya oluşturdu.


![21](assets/en/21.webp)


5. MicroSD kartı Coldkartından çıkarın ve Sparrow Wallet'ün takılı olduğu cihaza takın.

6. Sparrow Wallet'ü açın.

7. Dosya` üzerine tıklayın


![22](assets/en/22.webp)


Ardından, `Yeni Wallet` üzerine tıklayın


![23](assets/en/23.webp)


Ardından, wallet'in adını girin


![24](assets/en/24.webp)


Bundan sonra, `Wallet Oluştur` seçeneğine tıklayın


![25](assets/en/25.webp)


8. Script Türü`nü seçin.


![26](assets/en/26.webp)


9. Keystore bölümünde `Airgapped Hardware Wallet` öğesini seçin.


![27](assets/en/27.webp)


10. Coldcard öğesini bulun ve `Dosya Aktar...` öğesine tıklayın.


![28](assets/en/28.webp)


11. Adım 4'te oluşturulan dosyayı seçin (`.json` formatına sahip olan).


![29](assets/en/29.webp)


12. Mk4'te ana menüye dönün ve `Gelişmiş/Araçlar` > `Kimliği Görüntüle` seçeneğine gidin. Mk4'ün ekranında görüntülenen parmak izinin Sparrow Wallet'dakiyle eşleştiğinden emin olun (Anahtar Deposu bölümündeki Ana parmak izi)

13. Sağ alt köşedeki `Uygula` düğmesine tıklayın.


![30](assets/en/30.webp)


14. İsteğe bağlı olarak, dışa aktarılan wallet için bir parola da ekleyebilirsiniz. Bu parola, wallet'e erişmek için Sparrow Wallet uygulamasını her açtığınızda gereklidir. Gelecekte parolayı unutursanız, 1-13. Adımları tekrarlayabilir ve yeni bir parola seçebilirsiniz.


![31](assets/en/31.webp)


15. wallet artık başarıyla ihraç edilmiş ve kullanıma hazırdır.


![32](assets/en/32.webp)


## Bitcoin alma


Daha sonra, Mk4 kullanarak Bitcoin'i nasıl alacağımızı öğreneceğiz. Bu işlem oldukça basittir çünkü Mk4 cihazının kendisini kullanmanıza gerek yoktur. wallet'inizi zaten Sparrow'ya aktardığınız sürece, Bitcoin'i doğrudan Sparrow Wallet aracılığıyla alabilirsiniz. Mk4 ile bitcoin almak için aşağıdaki adımları izleyin:


1. Sparrow Wallet'yi açın.

2. Wallet`i Aç`ı seçin > Bitcoin almak istediğiniz wallet dosyasını seçin > Bu wallet ile ilişkili şifreyi girin.


![33](assets/en/33.webp)


3. Sparrow'ün arayüzünde, arayüzün sol tarafındaki `Receive` sekmesine tıklayın.


![34](assets/en/34.webp)


4. En üstte bir QR kodu ile birlikte bir adres görünecektir. Adresi kopyalayıp yapıştırabilir veya Sparrow Wallet'e bitcoin göndermek için kullanacağınız wallet'yı kullanarak QR kodunu tarayabilirsiniz. İsteğe bağlı olarak, aldığınız bitcoin için bir etiket yazabilirsiniz.


![35](assets/en/35.webp)


5. Bitcoinleri gönderdikten sonra, Sparrow'nin arayüzünde, arayüzün sol tarafındaki `İşlemler' sekmesine tıklayın. İşlem geçmişinin en üstünde yeni yaptığınız işleme karşılık gelen yeni bir giriş göreceksiniz.


![36](assets/en/36.webp)


6. Yeni aldığınız bitcoin'i görmek için arayüzün sol tarafındaki `UTXOs` sekmesine de gidebilirsiniz.


![37](assets/en/37.webp)


## Bitcoin gönderme


Bitcoin almanın aksine, Coldcard'ınızla ilişkili bitcoinleri harcamak, işlemleri imzalamak için Coldcard'ı kullanmanızı gerektirir. Mk4 ile bitcoin gönderme prosedürü aşağıdaki gibidir:


1. MicroSD kartı Sparrow Wallet cihazınızın takılı olduğu cihaza takın.

2. Sparrow Wallet'ü açın.

3. Wallet Aç`ı seçin > Bitcoin göndermek için kullanmak istediğiniz wallet dosyasını seçin > Bu wallet ile ilişkili şifreyi girin.


![38](assets/en/38.webp)


4. Sparrow'nın arayüzünde, arayüzün sol tarafındaki `Gönder' sekmesine tıklayın.


![39](assets/en/39.webp)


5. Ödeme sekmesinde, bitcoinleri göndermek istediğiniz adresi girin.

6. İşlem için bir etiket ekleyin.

7. Göndermek istediğiniz bitcoin miktarını girin.

8. Ücreti `Aralık` seçeneğini değiştirerek girin veya `Ücret` bölümüne doğrudan bir sayı girin.


![40](assets/en/40.webp)


9. Sağ alt köşedeki `İşlem Oluştur` seçeneğine tıklayın.


![41](assets/en/41.webp)


10. Adı 6. Adımda girdiğiniz etiket olan yeni bir işlem sekmesine yönlendirileceksiniz. İmzalama için İşlemi Sonlandır`a tıklayın.


![42](assets/en/42.webp)


11. İşlemi Kaydet`e tıklayın ve işlemi MicroSD karta kaydedin. Gerekirse dosyayı yeniden adlandırın. Bu adım işlemi bir PSBT dosyası olarak kaydedecektir.


![43](assets/en/43.webp)


12. MicroSD kartı çıkarın ve Coldcard Mk4'ünüze takın.

13. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

14. PIN kodunuzu girin.

15. Parola'ya gidin ve bitcoinleri göndermek için kullanmak istediğiniz wallet'ın passphrase'unu girin. wallet'ı boş passphrase ile kullanmak istiyorsanız, bu adımı atlayın.

16. Ana anahtar parmak izinin Sparrow Wallet'nizdekiyle aynı olduğundan emin olun. Bunu Sparrow Wallet'nin arayüzünün sol tarafındaki `Ayarlar` sekmesinden kontrol edebilirsiniz. Ardından, devam etmek için Mk4'ünüzde `✓` tuşuna basın. Bu sizi ana menüye götürecektir.

17. Mk4'ün ana menüsünde `İmzalamaya Hazır` seçeneğini seçin. Ekranda `GÖNDERMEYE HAZIR MISINIZ` mesajı görüntülenecektir. Göndermek istediğiniz bitcoin miktarının ve alıcı adresin doğru olduğundan emin olun. Onaylamak için `✓` tuşuna veya iptal etmek için `✕` tuşuna basın.

18. Aralarından seçim yapabileceğiniz birden fazla PSBT dosyası varsa, Mk4 `İmzalanacak PSBT dosyasını seçin` mesajını görüntüleyecektir. Devam etmek için `✓` tuşuna basın. Ardından, aşağı veya yukarı giderek imzalamak istediğiniz PSBT dosyasını seçin. Bu işlem üzerinde 17. Adımı gerçekleştirin.


![44](assets/en/44.webp)


19. Mk4 şimdi imzalı PSBT dosyasının adı ile birlikte `PSBT İmzalandı` mesajını görüntüleyecektir. Devam etmek için `✓` tuşuna basın.

20. MicroSD kartı Coldkartından çıkarın ve Sparrow Wallet'nın takılı olduğu cihaza takın.

21. Sparrow Wallet üzerinde `İşlem Yükle` seçeneğine tıklayın.


![45](assets/en/45.webp)


22. Adım 19'da oluşturulan dosya ile aynı ada sahip dosyayı seçin.


![46](assets/en/46.webp)


23. İşlemi Yayınla'ya tıklayın.


![47](assets/en/47.webp)


24. İşleminiz yayınlandı ve işleme alınıyor. İşleminizin onay durumunu görüntülemek için `İşlemler` sekmesine gidebilirsiniz.


![48](assets/en/48.webp)


## Ürün Yazılımı Yükseltme


### Ürün Yazılımı Sürümünüzü Kontrol Etme


Coldcard Mk4'ün aygıt yazılımı her zaman daha yeni bir sürüme yükseltilebilir. Mk4'ünüzün en son sürüme yükseltilmiş olup olmadığını kontrol etmek için aşağıdaki adımları uygulayın:

1. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

2. PIN kodunuzu girin.

3. Gelişmiş/Araçlar`a gidin > `Ürün Yazılımını Yükselt`i seçin > `Sürümü Göster`i seçin.


![49](assets/en/49.webp)


Mk4'ün ekranında görüntülenen sürümü [Coinkite'ın web sitesindeki] sürümle karşılaştırın (https://coldcard.com/downloads). Sürüm farklıysa, aygıt yazılımını daha yeni sürüme yükseltebilirsiniz.


![50](assets/en/50.webp)


### Ürün Yazılımınızı Yükseltme


Aygıt yazılımını en son sürüme yükseltmek istiyorsanız, aşağıdaki adımları uygulayın:


1. MicroSD kartı dizüstü bilgisayarınıza/PC'nize takın.

2. Coinkite'ın web sitesine] (https://coldcard.com/downloads) gidin ve en son aygıt yazılımını MicroSD kartınıza indirin (Mk4 görüntüsünün sağındaki üzerinde sürüm numarası olan kırmızı düğme).


![51](assets/en/51.webp)


Diğer sürümleri de `All Files on Mk4` seçeneğine tıklayarak ve indirmek istediğiniz sürümü keşfederek indirebilirsiniz. İndirilen dosya `.dfu` formatında olacaktır.


![52](assets/en/52.webp)


3. MicroSD kartı çıkarın ve Mk4'ünüze takın.

4. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

5. PIN kodunuzu girin.

6. Gelişmiş/Araçlar`a gidin > `Firmware Yükselt`i seçin > `MicroSD`den`i seçin > Talimatları okurken aşağı kaydırın ve ardından `✓`ya basın.


![53](assets/en/53.webp)


7. Adım 2'de indirdiğiniz `.dfu` dosyasını seçin.

8. Coldcard Mk4 `Bu yeni aygıt yazılımını yükleyin` mesajı gösterecektir. Talimatları okurken aşağı kaydırın ve ardından `✓` tuşuna basın.


![54](assets/en/54.webp)


9. Mk4'ün yeni aygıt yazılımını yüklemeyi bitirmesini bekleyin. Kurulum sırasında güç kaynağının bağlantısını kesmeyin.

10. Tamamlandığında, Mk4 kendini yeniden başlatacaktır. PIN kodunuzu girebilir ve aygıt yazılımının yükseltilmiş olup olmadığını kontrol etmek için "Aygıt Yazılımı Sürümünüzü Kontrol Etme" adımlarını uygulayabilirsiniz.


## Gelişmiş Özellikler


### PIN kodunuzu değiştirin


Oturum açma PIN kodunuzu değiştirmek istiyorsanız, aşağıdaki adımları uygulamanız yeterlidir:


1. Bir kalem ve bir parça kağıt hazırlayın.

2. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

3. PIN kodunuzu girin.

4. Ayarlar`a gidin > `Giriş Ayarları`nı seçin > `Ana PIN'i Değiştir`i seçin

5. Mesajı okurken aşağı doğru ilerleyin, ardından devam etmek için `✓` tuşuna basın.


![55](assets/en/55.webp)


6. Eski PIN kodunuzu girin.

7. Yeni PIN önekinizi girin (2 ila 6 karakter uzunluğunda olmalıdır) ve bir yere not edin.

8. Mk4 şimdi iki yeni kimlik avı önleme kelimesi gösterecektir, bunları yazın ve devam etmek için `✓` tuşuna basın.

9. Yeni PIN son ekinizi (veya PIN'in geri kalanını, 2 ila 6 karakter uzunluğunda olmalıdır) girin ve not edin.


![56](assets/en/56.webp)


10. Yeni PIN önekinizi tekrar girin.

11. Kimlik avı önleme sözcüklerinin Adım 8'de yazdığınızla eşleşip eşleşmediğini kontrol edin.

12. Yeni PIN son ekinizi (veya PIN'in geri kalanını) tekrar girin.


![57](assets/en/57.webp)


13. PIN kodunuz başarıyla değiştirildi.


### Numara PIN'leri - Yeni Numara Ekle


Hile PIN kodu, Coldcard Mk4 cihazınızı ilk kez kurarken kullandığınız PIN kodundan farklı alternatif bir PIN kodudur. Mk4'ünüzü açtığınızda, belirli eylemleri tetiklemek için Ana PIN kodunuz yerine hile PIN kodlarını girebilirsiniz. Mk4'te hile PIN'ini yapılandırmak için aşağıdaki adımları uygulayabilirsiniz:


1. Bir kalem ve bir parça kağıt hazırlayın.

2. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

3. PIN kodunuzu girin.

4. Ayarlar`a gidin > `Giriş Ayarları`nı seçin > `Hile PIN`leri`ni seçin > `Yeni Hile Ekle`yi seçin.


![58](assets/en/58.webp)


5. Numara PIN önekinizi girin (2 ila 6 karakter uzunluğunda olmalıdır) ve bir yere not edin.

6. Mk4 şimdi iki yeni kimlik avı önleme kelimesi gösterecektir, bunları yazın ve devam etmek için `✓` tuşuna basın.

7. Numaralı PIN son ekinizi (veya PIN'in geri kalanını, 2 ila 6 karakter uzunluğunda olmalıdır) girin ve not edin.


![59](assets/en/59.webp)


8. Yeni oluşturduğunuz hile PIN'i ile eşleştirmek istediğiniz eylemi seçmek için aşağı veya yukarı gidin. Eylemlerin listesi şunlardır:


    - `Brick Self` seçildiğinde, PIN girildikten sonra Mk4'ünüzün çipleri yok edilecek ve Mk4'ünüz kalıcı olarak kullanılamaz hale gelecektir.
    - tohumu Sil`, aşağıdaki eylemler arasından seçim yapabilirsiniz:
      - sil ve Yeniden Başlat: seed silinir ve PIN girildikten sonra Cold kartı yeniden başlatılır.
      - "Sessiz Silme": seed sessizce silinir, ancak Coldcard PIN yanlış girilmiş gibi davranacaktır.
      - sil -> Wallet`: seed sessizce silinir ve Cold kartı sizi wallet zorlamasına götürür.
    - `Duress Wallet`, seçildiğinde, Mk4'ünüz PIN girildikten sonra bir duress wallet'e yol açacaktır.
    - `Giriş Geri Sayımı`, aşağıdaki eylemler arasından seçim yapabilirsiniz:
      - "Sil ve Geri Sayım": seed hemen silinir, ardından Mk4 bir geri sayım göstermeye başlar.
      - "Geri Sayım ve Tuğla": Geri sayım başlar ve süre bittikten sonra Mk4 kendini tuğlalar.
      - "Sadece Geri Sayım": Mk4 geri sayıma başlayacak ve süre bittikten sonra kendini yeniden başlatacaktır.
    - "Boş Görün", seçildiğinde, hile PIN'i girildikten sonra, Coldkartı seedphrase silinmiş gibi davranır, ancak aslında hala bellektedir.
    - "Sadece Yeniden Başlat", seçildiğinde, Coldcard hile PIN'i girildikten sonra kendini yeniden başlatacaktır.
    - `Delta Modu`, Bu gelişmiş özellik deneyimli kullanıcılar içindir ve içeriden bilgi sahibi birinin zorlaması gibi ciddi tehditlere karşı koruma sağlamak üzere tasarlanmıştır. Delta Modu etkinleştirildiğinde, COLDCARD gerçek wallet'u açıyor gibi görünerek saldırganın göz atmasına ve gerçek göründüğünü onaylamasına olanak tanır. Ancak, gizlice tüm işlem imzalamayı engeller, böylece hiçbir bitcoin gönderilemez. Ayrıca seed ifadesine erişimi de devre dışı bırakır ve herhangi bir görüntüleme girişimi onu tamamen siler. Sahte wallet'un daha inandırıcı görünmesini sağlamak için Delta Modu için kullanılan Hile PIN'i gerçek PIN ile aynı rakamlarla başlamalı (böylece aynı kimlik avı önleme kelimelerini gösterir) ancak farklı şekilde bitmelidir.
    - "Politika Kilidini Aç" seçildiğinde, Tek İmzacı Harcama Politikası (SSSP), hile PIN'i girildikten sonra devre dışı bırakılacaktır.
    - "Politika Kilit Açma ve Silme", seçildiğinde SSSP'yi devre dışı bırakıyormuş gibi yapar ancak bu süreçte seedphrase'i siler.

9. Hile PIN'i ile eşleştirmek istediğiniz eylemi seçtikten sonra `✓` tuşuna basarak seçiminizi onaylayın. Hile PIN kodunuz başarıyla yapılandırılmıştır.

10. Ayarlar` > `Giriş Ayarları` > `Hile PIN'leri` bölümünde, oluşturduğunuz hile PIN'lerinin ve bunlarla eşleştirilen eylemlerin listesini görebilirsiniz. Hile PIN'lerini ve onunla eşleştirilmiş eylemleri yeniden yapılandırmayı seçebilirsiniz. Ayrıca PIN'i seçip ardından `Hileyi Gizle` veya `Hileyi Sil` seçeneğini belirleyerek PIN'i gizleyebilir veya silebilirsiniz.


![60](assets/en/60.webp)


### Hileli PIN'ler - Yanlışsa Ekle


Alternatif olarak, belirli sayıda yanlış PIN girildikten sonra tetiklenecek bir `Yanlışsa Ekle` eylemi ekleyebilirsiniz. Bunu aşağıdaki adımları uygulayarak yapılandırabilirsiniz:


1. Mk4'ünüzü bir güç kaynağına bağlayarak açın.

2. PIN kodunuzu girin.

3. Ayarlar`a gidin > `Giriş Ayarları`nı seçin > `Hile PIN`leri`ni seçin > `Yanlışsa Ekle`yi seçin.


![61](assets/en/61.webp)


4. Mk4 bu ayarla ilgili bir mesaj görüntüleyecektir. Açıklamayı okurken aşağı doğru ilerleyin, ardından devam etmek için `✓` tuşuna basın.

5. Eylemi tetiklemek için gereken yanlış deneme sayısını girin. Not: Maksimum deneme sayısı `12`dir. Bunun nedeni Mk4'ün `13` kez yanlış PIN girildiğinde cihazın kendisini brick ederek kalıcı olarak kullanılamaz hale getirecek şekilde tasarlanmış olmasıdır. Numarayı girdikten sonra devam etmek için `✓` tuşuna basın.

6. Eylemi seçmek için yukarı veya aşağı gidin. Mevcut eylemler aşağıdaki gibidir:


   - "Sil, Durdur": seedphrase silinir ve cihaz "Tohum silindi, Durdur" mesajını gösterir
   - "Sil ve Yeniden Başlat": seedphrase silinir ve cihaz herhangi bir mesaj olmadan yeniden başlatılır.
   - "Sessiz Silme": seedphrase sessizce silinir ve cihaz yanlış PIN denemesi gibi davranır (belirgin bir silme mesajı yoktur).
   - "Tuğla Kendisi": Cihaz kalıcı olarak devre dışı bırakılır ve yalnızca "Tuğlalı" olarak gösterilir
   - "Son Şans": seedphrase silinir ancak son bir PIN denemesi hakkınız vardır; PIN'i tekrar yanlış girdiğinizde cihaz tuğlalanacaktır.
   - "Sadece Yeniden Başlat": Cihaz basitçe yeniden başlatılır ve başka hiçbir şey değişmez.

Uygulamak istediğiniz eylemi seçin ve devam etmek için `✓` tuşuna basın


![62](assets/en/62.webp)


7. Ayarlar > Giriş Ayarları > Hile PIN'leri dizinine geri getirileceksiniz. Hile PIN'leri:` altında, `YANLIŞ PIN` eylemiyle birlikte hile pinlerinin listesini bulacaksınız. Ayrıca PIN'i seçip ardından `Hileyi Gizle` veya `Hileyi Sil` seçeneğini belirleyerek PIN'i gizleyebilir veya silebilirsiniz.


![63](assets/en/63.webp)



## Sonuç


Bu eğitimde Mk4'ün nasıl kurulacağı, Mk4 ile Bitcoin işlemlerinin nasıl yapılacağı ve Mk4'ün bazı gelişmiş özelliklerinin nasıl kullanılacağı anlatılmaktadır. Bitcoinlerinizi saklamak ve yönetmek için güvenli ve esnek yollar sunar. Tasarımı, özel anahtarların cihazdan asla ayrılmamasını sağlarken, passphrase'lar, hileli PIN'ler ve hava boşluklu işlemler gibi özellikler kullanıcılara güvenlik kurulumları üzerinde tam kontrol sağlar. Gizlilik veya güvenlikten ödün vermeden Bitcoin işlemlerini oluşturmak, imzalamak ve yönetmek için kullanıcı dostu bir deneyim için Sparrow Wallet ile eşleştirilebilir.


Diğer işlevleri keşfetmek isterseniz, Coinkite'ın web sitesindeki [burada] (https://coldcard.com/docs/) belgeleri kontrol edebilirsiniz. Umarım Coldcard Mk4'ünüzü kullanırken bu öğreticiyi faydalı bulursunuz. Teşekkürler ve bir dahaki sefere görüşmek üzere!