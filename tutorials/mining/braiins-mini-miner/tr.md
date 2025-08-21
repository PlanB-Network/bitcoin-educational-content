---
name: Mini Miner Braiins
description: Evden kolayca Mining yapmak.
---
![cover](assets/cover.webp)



### Giriş



Mini Miner braiins BMM 100, Mining pool Braiins tarafından yaratılmış bir üründür. Bu cihaz çekici bir tasarıma sahiptir ve son derece sessizdir. 1.1 Th/s işlem gücü üretir ve yaklaşık 40 watt tüketir. Diğer cihazların aksine, açık kaynaklı değildir, ancak kurulumu gerçekten kolaydır, gerçekten sadece birkaç tıklama alır! Mini Miner BMM 100 piyasaya sürülen ilk sürümdür. Şimdi BMM 101 olarak adlandırılan ve ilkinden daha büyük bir ekrana ve Wi-Fi varlığına sahip olmasıyla farklılık gösteren 2. sürüm üretiliyor, ancak kurulum prosedürleri aynı.



Ayrıca, doğrudan [üreticinin sitesi] (https://braiins.com/hardware/mini-Miner-bmm-100) adresindeki kılavuzun tamamına göz atarak çok daha önemli bilgiler bulabilirsiniz.



### BMM 100'e Genel Bakış



cihaz, ön tarafında bir ekran bulunan paralel yüzlü bir yüzeye benziyor



![image](assets/en/01.webp)



üst tarafta bir fan



![image](assets/en/02.webp)



arka tarafta ise: güç için delik, SD kart için alan (herhangi bir güncelleme için gerekli olabilir), mini Miner'nin IP Address'ini bilmenizi sağlayan `IP RAPORU' yazan küçük bir düğme, cihaz kontrol paneline erişmek için hangi Address'in gerekli olduğu. Düğmeye basıldığında, IP Address yaklaşık 5 saniye boyunca görüntülenir, ardından kaybolur ve ayar ekranı yeniden görünür. Bununla birlikte, bazı ayarları değiştirmeniz gerekirse, söz konusu düğmeye tekrar basmanız yeterlidir ve IP Address ekranda yeniden görünecektir. Listeye devam ettiğimizde, bir Ethernet portu ve mini Miner'nin tüm ayarlarını sıfırlamak için bir pimi tutup 10 saniye basılı tutmanız gereken bir cihaz sıfırlama erişimi buluyoruz. Son olarak, Miner'nin durumunu bize gösteren biri Green diğeri kırmızı olmak üzere iki gösterge ışığı buluyoruz.



![image](assets/en/03.webp)



### Mini Miner'in Bağlanması



Cihazı ethernet üzerinden internete bağlamanız gerekecektir, yeni sürümle (BMM 101) bunun artık gerekli olmadığını unutmayın. Bu mini Miner'a geri dönersek, konumu belirledikten sonra önce internet hattına sonra da güce bağlamamız gerekecek: cihaz otomatik olarak açılacak ve ekranda IP Address'u gösterecektir.



### Konfigürasyon



Bir tarayıcı açmamız ve arama çubuğuna bize mini Miner'yi gösteren IP Address'i girmemiz gerekiyor. Cihazı ağ üzerinde bulmak için yerel olmanız gerektiğini hatırlatırım, bu nedenle kullandığınız bilgisayarın mini Miner ile aynı ağa bağlı olması gerekecektir. IP Address'i girdikten sonra enter tuşuna basarız ve mini Miner'nin Braiins OS olan işletim sistemine giriş sayfası ekranda görünecektir.



![image](assets/en/06.webp)



Giriş yapmak için kullanıcı adı olarak `root` girmeniz gerekecek, şifreyi ise boş bırakabilirsiniz. Girişe tıklayın ve mini Miner kontrol paneliniz görünecektir.



![image](assets/en/07.webp)



### Genel ayarlar



Sisteme gidelim



![image](assets/en/24.webp)



ayarlar içinde tema (açık veya koyu), dil, saat dilimi ve şifre değişikliği gibi bazı genel ayarlar buluyoruz.



![image](assets/en/25.webp)



Bunun yerine "Mini Miner Ekranı "na gidersek, ekran görüntüsü gibi mini Miner'imizin ayarlarına sahip oluruz. Saati mi, Bitcoin'ün fiyatını mı, yoksa Hash ürünü, sıcaklık, tüketilen watt gibi makine durum bilgilerini içeren ekranı mı göstereceğimizi seçebiliriz. Burada ekranda ne görmek istediğinizi seçmek size kalmış; ayrıca ekranın parlaklığını değiştirebilir, gece modunu ayarlayabilir ve saati 12 saat veya 24 saat formatında görüntüleyebiliriz.



![image](assets/en/26.webp)



Değişiklikleri yaptıktan sonra `Değişiklikleri Kaydet` seçeneğine tıkladığınızda değişiklikleri cihazınızın ekranında göreceksiniz



![image](assets/en/27.webp)



### Mining pool'ye Bağlantı



Şimdi henüz operasyonel değiliz, çünkü Mining'i başlatmak için bir havuza bağlanmamız gerekiyor, bu yüzden "Yapılandırma "ya gitmeliyiz



![image](assets/en/08.webp)



ve ilk giriş sadece `Pools`.



![image](assets/en/09.webp)



Burada hangi havuzu kullanacağımıza karar vermemiz gerekecek. Bu derste size iki seçenek göstereceğim. Birincisi, bu eğitimden de görebileceğiniz gibi, bizi profesyonel madenciler tarafından da kullanılan Mining pool Braiins'e bağlamak:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

İkinci seçenek, bizi Public Pool gibi tek başına çalışan bir Mining pool'ye bağlamaktır, bunu yapmak için bu kılavuzu izleyin:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Braiins Havuz



Bu havuza bağlanmak için bir hesap oluşturmamız gerekiyor. bu havuz ayrıca Lightning Network kullanarak ödeme yapar, böylece günde birkaç Sats alabileceğiz. Bunu yapmak için ödülleri alacağımız bir Address yıldırım kurmamız gerekiyor. Braiins havuzunda nasıl hesap oluşturacağınızı veya Address lightning'inizi nasıl kuracağınızı bilmiyorsanız bu kılavuzu takip edebilirsiniz:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Bu işlem tamamlandıktan sonra Braiins havuz kontrol panelindeyiz. Yapmamız gereken, havuza Madencilerimizden biriyle bağlantı kurmak istediğimizi söylemektir, bu nedenle ekranın sol tarafında bir dizi giriş bulacaksınız. "İşçiler "e gitmemiz gerekiyor



![image](assets/en/04.webp)



ve sağ tarafta "Çalışanları bağla" yazan mor düğmeye tıklamamız gerekiyor



![image](assets/en/05.webp)



Mini Miner'ümüzü havuza bağlamak için ihtiyacımız olan bilgileri içeren pencere geliyor. Burada yapabileceğimiz tek değişiklik Stratum V2'yi seçmek. Stratum v2'nin ne olduğunu öğrenmek için [glossary] (https://planb.network/en/resources/glossary/stratum-v2) adresindeki bu girdiye bakın.



![image](assets/en/10.webp)



Şimdi stratumv2 ile başlayan bu dizeyi kopyalamamız gerekiyor. Bu yüzden küçük "kopyala" sembolüne tıklıyoruz, ardından yapılandırma ve havuzlarda bıraktığımız mini Miner'imizin kontrol paneline gidiyoruz. Yeni havuz ekle'ye tıklıyoruz



![image](assets/en/11.webp)



ve kopyaladığımız dizeyi Havuz URL'sinin altındaki boşluğa yapıştırın.



![image](assets/en/12.webp)



Şimdi kullanıcı adı ve şifre eklememiz gerekiyor. Havuz dashboad'una geri dönelim. Altında da bir kullanıcı kimliğimiz ve şifremiz var. Kullanıcı kimliği ve kullanıcı adımız, hesabı oluştururken verdiğimiz kullanıcı adı, artı koymak istediğimiz Miner'nın adı. havuza bağladığınız cihaza bir isim verip vermemeye karar verebilirsiniz, isteğe bağlıdır, ancak koymanız tavsiye edilir, böylece birden fazla cihaz bağlarsanız bunları hemen tanımlamak daha kolay olacaktır. Bunun yerine herhangi bir şey koymak istemiyorsanız `workerName` i bırakabilirsiniz.



![image](assets/en/13.webp)



Daha sonra mini Miner'ye gidiyoruz ve kullanıcı adını giriyoruz. Burada benim durumumda kullanıcı kimliğim olan "finalstepbitcoin" gireceğiz, miniminer nokta. Bu, cihaza vermeye karar verdiğim isim. Eğer isim vermek istemiyorsanız sadece userid dot workername yazın. Benim durumumda finalstepbitcoin.workername olacaktır. Kullanıcı adını girdikten sonra bir şifre seçebilir ve boş alana yazabilirsiniz. Havuz ekranında da gösterilen anithing123'ü de koyabilirsiniz, ancak bu sadece istediğiniz herhangi bir şifreyi koyabileceğinizi belirtmek istiyor.



Tüm verileri girdikten sonra sağdaki kaydet düğmesine (disket şeklinde olan) basmanız gerekir ve bu şekilde mini Miner'deki havuz verilerini yapılandırmış olursunuz.



![image](assets/en/14.webp)



Şimdi havuz kontrol paneline geri dönmeniz ve "Bağlandı! Geri dön."



![image](assets/en/15.webp)



Mini Miner'umuzu braiins havuzuna bağladık! Artık çalışanlar listesinde görebilirsiniz. Eğer görünmüyorsa sadece yenileyin ve birkaç dakika bekleyin. Göründüğünde, Green onay işareti ile "Tamam" durumuna sahip olduğunu doğrulayın.



![image](assets/en/17.webp)



gösterge tablosuna geri dönerseniz grafikte hareket görmeye başlamalı ve cihazımızın Hashrate'ini görmelisiniz. Bu, havuzun işimizi aldığı ve bu nedenle tüm niyet ve amaçlar için baltaladığımız anlamına gelir.



![image](assets/en/16.webp)



#### Halka Açık Havuz



Bu havuz aracılığıyla kişi şansını deneyebilir ve bir havuza yaslanarak tek başına madencilik yapabilir. Bu durumda ödül almayacağız, ancak bir blok çıkarmayı başarırsak ödülün tamamını alacağız. Daha sonra tamamen açık kaynak olan ve yalnızca Mining'ye özel bir havuz olan public pool'a bağlanacağız. Tarayıcıda yeni bir pencere açıyoruz ve [web.public-pool.io](https://web.public-pool.io/#/) adresine gidiyoruz.



![image](assets/en/18.webp)



ihtiyacımız olan tüm bilgileri içeren bir sayfa açılır. Daha sonra oraya Address tabakasını kopyalıyoruz



![image](assets/en/19.webp)



daha sonra mini Miner'imizin kontrol paneline geri dönüyoruz, yapılandırmaya ve havuzlara gidiyoruz, yeni havuz ekle'ye tıklıyoruz (yukarıda görüldüğü gibi aynı işlem) ve 'stratum Address'ü havuz url'si altına yapıştırıyoruz.



![image](assets/en/20.webp)



Şimdi havuz sayfasına geri dönelim ve kullanıcı adı olarak bir Bitcoin Address girmemiz gerektiğini görelim, bu bir bloğu baltalamamız durumunda ödül alacağımız kişi olacak, ardından bir nokta ve ardından daha önce Braiins Pool'da yaptığımız gibi cihazımızın adı, şifreyi ise kendimiz seçebiliriz.



![image](assets/en/21.webp)



Mini Miner'a geri dönüyoruz ve kullanıcı adı altında bir Address Bitcoin ve ardından nokta ve isim yapıştırıyoruz, ben `miniminer` koyacağım. Parola yerine ben test yazacağım, siz ne isterseniz onu girin.



![image](assets/en/22.webp)



Şimdi ayarları kaydediyoruz ve Braiins havuzunu devre dışı bırakıyoruz.



![image](assets/en/23.webp)



Güzel! Artık halka açık havuzda Mining'iz!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)