---
name: Elektrum Hava Boşluğu
description: Güvenliğe doğru ilk adım, Electrum'lu bir Cold Wallet
---
![cover](assets/cover.webp)



## Cold Wallet



Bu eğitimde, özel bir Hardware Wallet'e sahip olmadan bile internet bağlantısı kesilmiş ilk hava boşluğu imzalama cihazınızı nasıl yapacağınızı açıklayacağım. Tek ihtiyacınız olan iki bilgisayara sahip olmak:




- eski bir cihazın internete bağlanmasının sonsuza kadar engellenmesi;
- günlük kullanım bilgisayarınız.



Bu yapılandırma, klasik `Hot Wallet`ten daha yüksek bir güvenlik derecesi sağlar: eski bilgisayar - ağ bağlantısı olmadan - özel anahtarlarınızın koruyucusudur, bunlar asla internete açık değildir, ancak çevrimdışı olarak saklanır ("airgap" veya "Cold").



Bunun yerine, ağa bağlı olan ve örneğin bakiyeleri kontrol edebileceğiniz ve makbuz işlemlerini hazırlayabileceğiniz günlük bilgisayarınıza bir Wallet ekranı ("sadece izle") kuracaksınız.



## Wallet Hava Boşluğu: Ne ve Nasıl



Bu kılavuzdaki adımları uygulayarak, iki farklı bilgisayara iki Software Wallet Electrum kuracağız ve son olarak farklı anahtar depolarına sahip iki Cüzdan oluşturacağız: Wallet airgap, Wallet HD'nin tüm hiyerarşisini kullanırken, Wallet ekranı ana ortak anahtarla oluşturulacaktır.



Bu iki Cüzdan her bakımdan birbirinden çok farklı olacaktır. Göreceğimiz gibi, tek ortak noktaları adresler olacaktır:




- airgap bilgisayarındaki gW-13 yalnızca imzalayabilir, ancak ağ bağlantısı kesildiğinde kullanılan bakiyeyi ve adresleri bilmez;
- günlük bilgisayardaki Wallet, özel anahtarların yokluğunda harcamaları elden çıkaramadan sadece işlemleri hazırlayıp yayabilecektir.



## Ön Hazırlık



Electrum'u indirmek için bu eğitimdeki ilk adımları izlemenizi tavsiye ederim:



https://planb.network/it/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

İndirdikten sonra, yüklemeden önce sürümü her zaman doğrulayın, ardından yardım bölümünde `Kukla Wallet ile Başlayın` altında bulacağınız gibi "Tek Sunucu" yapılandırmasına geçin.



"Tek Sunucu" yapılandırma işlemi yalnızca günlük bilgisayarda yüklü olan Wallet için gereklidir, çünkü diğer bilgisayar her zaman çevrimdışı olacaktır.



Aşağıdaki işlemler iki farklı bilgisayarda (ve Cüzdanlarda) pratik yapmayı içermektedir, bu nedenle kolaylık ve odaklanma açısından Wallet ekranında koyu tema varken Wallet airgap'i açık temaya ayarlamayı seçtim.



## Wallet Hava Boşluğu Oluşturma



Electrum'u indirip doğruladıktan sonra, yürütülebilir dosyanın bir kopyasını alın ve çevrimdışı olarak bilgisayarınıza getirin. Ardından başlatın ve Electrum'u yükleyin.



Electrum'u başlatmak için çift tıklayın: bu Wallet'yi kullanacağınız bilgisayar çevrimdışıdır, ağ ayarlarını göz ardı edin ve bu kılavuzda `airgap` olarak adlandıracağımız Wallet'nin oluşturulmasına gidin.



![image](assets/en/01.webp)



Standart cüzdanı_ seçin.



![image](assets/en/02.webp)



Ardından yazılımın generate'u Mnemonic'e dönüştürmesini sağlamak için _COPYreate a new seed_ (Yeni bir tohum oluştur) seçeneğini seçin.



![image](assets/en/03.webp)



Electrum'daki 12 generate kelimesini doğru bir şekilde bir kağıt desteğine kopyalayın ve Electrum istediğinde kelimeleri sırayla yeniden girerek doğrulama adımına geçin.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Wallet oluşturma işlemi tamamlandıktan sonra, airgap cihazındaki Wallet dosyasını şifrelemek için karmaşık bir şifre (`Strong`) belirleyin. Bu adım çok hassas ve önemlidir, çünkü şimdi seçilen şifre, tasarruf yetkisine sahip olan Wallet'e erişimi engeller, fonları harcayabilir ve işlemleri imzalayabilir.



![image](assets/en/06.webp)



Bitir_ butonuna tıklandığında Wallet tanımlanır ve ekranda görünür. Tabii ki, ağ bağlantısı göstergesi, yani sağ alt köşedeki renkli nokta, bilgisayar bağlantısı kesildiği ve Wallet'nin çevrimiçi tuşları göstermesine izin vermediği için kırmızıdır.



![image](assets/en/07.webp)



## Oluşturma Wallet Görselleştirme



Artık Wallet'ünüz çevrimdışı özel anahtarlara sahip olduğuna göre, bakiyeyi görüntülemenize ve Sats'i güvenli bir şekilde biriktirmeye devam etmek için makbuz işlemleri hazırlamanıza olanak tanıyacak bir ekran Wallet veya "yalnızca izle" ayarlamanız gerekir.



Çevrimdışı cihazda bulunan Wallet'dan _Cüzdan_ -> _Bilgi_ menüsünü seçin



![image](assets/en/08.webp)



Tüm Wallet bilgilerinizi içeren pencere görünecektir, burada `derivation path` ve `master fingerprint` i kontrol edebilirsiniz, örneğin bunları Mnemonic cümlesindeki kelimelerin yanına işaretlemek için (şiddetle tavsiye edilir).



![image](assets/en/09.webp)



Bu verileri bağlı olmayan bir bilgisayardan aldığınızı unutmayın, bu nedenle `zpub`ı bir metin dosyasına kopyalayıp yapıştırmanız ve bir usb belleğe kaydetmeniz gerekecektir.



Şimdi Electrum'u başlatmak ve yeni bir Wallet oluşturmak için İnternet'e bağlı bilgisayara geçebilirsiniz.



Dosya_ menüsünden _Yeni/Geri_ öğesini seçin.



![image](assets/en/10.webp)



Yeni Wallet yalnızca görüntüleme özelliğine sahiptir, bu nedenle bu kılavuzda `watch-only` olarak adlandıracağız.



![image](assets/en/12.webp)



Bir sonraki ekranda _Standart cüzdan_ öğesini seçin ve _Sonraki_ öğesine tıklayarak devam edin.



![image](assets/en/13.webp)



Anahtar deposu`nu seçerken dikkatli olun: Wallet ekranını oluşturmak için _Bir ana anahtar kullan_ seçeneğini seçin. Ardından _Sonraki_ ile devam edin.



![image](assets/en/14.webp)



Wallet'den çevrimdışı olarak kopyaladığınız ve usb medya aracılığıyla bu bilgisayara getirdiğiniz `zpub`ı buraya yapıştırın.



![image](assets/en/15.webp)



Bu Wallet için de, muhtemelen ilgili Cold için seçilenden farklı, güçlü bir parola belirleyerek sonlandırın.



Bir uyarı ile birlikte Wallet ekranının göründüğünü göreceksiniz. Mesaj size bunun sadece ekrana özel bir Wallet olduğunu ve bununla ilişkili fonları harcayamayacağınızı hatırlatır.



**İyi Not**: **Bu nedenle, bu Wallet'nın UTXO'larını elden çıkarmak için her zaman özel anahtarlara sahip olmanız gerekecektir**. İyi bir yedekleme sistemi ile Bitcoin'lerinize tam olarak sahip olmanız zor olmayacaktır.



![image](assets/en/16.webp)



Bu uyarı, bu Wallet'yi her açtığınızda görünecektir. Tamam'a tıklayın ve doğrulama adımına geçelim.



## İki Wallet'in Doğrulanması



Bu kılavuzun başında öğrendiğimiz gibi, bir Wallet airgap ve onun ekranı olan Wallet, farklı özelliklere sahip ancak **aynı adresleri paylaşan** iki cüzdandır.



İki cüzdana yan yana bakarsak, görsel olarak Wallet hava boşluğunda bir "seed" sembolü olduğunu, yalnızca saatte ise olmadığını fark ederiz. Bu ayrıntı bile Wallet ekran Wallet'ın özel anahtarlara sahip olmadığını hatırlamanıza yardımcı olacaktır.



![image](assets/en/17.webp)



Bununla birlikte, doğru bir ilk kontrol yapmak için, her iki Cüzdanda da `Adresler` menüsünü seçin: aynı adresleri paylaştıklarından, adres listesi her ikisi için de aynı olmalıdır.



![image](assets/en/18.webp)



⚠️ **DIKKAT**: **orta yol olamaz; adresler aynı olmalıdır. Farklı olmaları durumunda, şimdiye kadar yapılan tüm çalışmaları silmek ve baştan başlamak gerekir**.



Şimdi iki farklı kontrol yapmaya devam edebilirsiniz. İlk olarak, her biri uygun bilgisayarda olmak üzere iki Cüzdanı silmeyi ve sıfırdan geri yüklemeyi deneyin. Bu doğrulamayı yapmaya devam etmeniz durumunda, Wallet ekranı için prosedürler yukarıda belirtilenlerle aynıdır.



Ancak Wallet hava boşluğu için, `keystore' ekranında _I already have a seed_ seçeneğini seçmeniz ve kelimeleri kağıt yedeğinizden kopyalayarak girmeniz gerekecektir.



"Yüksüz" deneme bittikten sonra, küçük miktarda bir işlem yapmayı deneyebilir ve hemen harcayabilirsiniz.



## Alım ve Harcama İşlemleri



Electrum airgap'inizi kullanmaya başlamak için, küçük bir miktarla bir makbuz işlemi yapabilir, ardından bunu kendi Address'ünüz için harcayabilirsiniz. Ardından, fonların tam kontrolünün sizde olduğunu doğrulayarak prosedüre kendinizi alıştırabilirsiniz.



**Not**: Tüm işlemleri sorunsuz bir şekilde gerçekleştirebileceğinizden emin olmadan önce Wallet'e büyük miktarda para yatırmanızı önermiyorum.



Aşağıda açıklanan adımlar ilk bakışta karmaşık görünebilir. Bunun sizi üzmesine izin vermeyin: ilk denemenizde, tamamlamanın sadece birkaç dakika sürdüğünü göreceksiniz.



Para almak için, mutlaka internete bağlı bilgisayarınızda bulunan Wallet ekranını kullanmalısınız. Electrum generate'nın ilk kullanılabilir Address'ye sahip olması ve bize birkaç Sats göndermek için kullanması için `Alma` menüsünden _COPYreate request_ seçeneğine tıklayın.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



İşlem yayıldıktan sonra - doğal olarak - sadece Wallet ekranında göründüğünü ve Wallet hava aralığında görünmediğini görebilirsiniz.



![image](assets/en/21.webp)



İşleminiz bir miktar onay aldıktan sonra, harcamayı hazırlayabilir ve böylece Wallet ağ dışından imzalama prosedürünü deneyebilirsiniz. Daha sonra işlemi sadece saat üzerinde hazırlayın ve kontrol etmek için _Preview_ tuşuna basın



![image](assets/en/22.webp)



Bunu görebileceğiniz gelişmiş işlem penceresine sahip olursunuz:




- işlem imzalanmamıştır (`Status: Unsigned);
- sign` ve `Broadcast` komutları engellenir.



Yapabileceğiniz tek şey işlemi olduğu gibi dışa aktarmak, Wallet hava boşluğuna götürmek ve imzalamaktır.



Bilgisayarınıza bir USB flash sürücü takın ve sol alttaki menüden _Share_ öğesini seçin.



![image](assets/en/23.webp)



Bundan sonra _Dosyaya kaydet_ öğesini seçin.



![image](assets/en/24.webp)



İşlemi usb belleğe kaydedin.



Electrum'un dosyaya transaction ID'ün ilk rakamlarını taşıyan bir isim verdiğini ve dosya uzantısının `.PSBT`, yani `Partially Signed Bitcoin Transaction` olduğunu fark edeceksiniz.



.PSBT` dosyası ile medyayı çıkarın ve çevrimdışı olarak bilgisayara bağlayın.



Şimdi Wallet hava boşluğundan _Araçlar_ menüsünü seçin, ardından _İşlemi yükle_ ve Dosyadan_ seçeneğini izleyin.



![image](assets/en/25.webp)



Dosya yöneticisi ile konumundan `.PSBT` dosyasını seçin.



![image](assets/en/29.webp)



Ağ dışı bilgisayar yazılımı, Wallet ekranında gördüğünüzle tamamen aynı olan gelişmiş işlem penceresini otomatik olarak açacaktır. Durum `İmzalanmamış`tır, ancak aradaki fark `İmzala` komutunun aktif olmasıdır. Ve bu tam olarak uygulamanız gereken şeydir.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Artık işlem imzalandığına göre, Wallet'ınızın çevrimdışı bir makinede olduğunu unutmayın. Bu nedenle - `Broadcast` komutunu aktif görseniz bile- Wallet'ınız işlemi Bitcoin ağına yayamayacaktır.



Şimdi yapmanız gereken, imzalı işlemi usb belleğe aktarma işlemini tekrarlamaktır, böylece internete bağlı bir bilgisayara aktarabilir ve yayabilirsiniz.



Sol alt menüden tekrar _Paylaş_ öğesini ve ardından _Dosyaya kaydet_ öğesini seçin.



![image](assets/en/28.webp)



Artık dosyanın farklı bir uzantısı var: **artık işlem `.PSBT` yerine `.txn` uzantısına sahip. Şu andan itibaren Electrum, imzalı işlemleri imzasız olanlardan ayırt etmenize bu şekilde izin verecektir**.



![image](assets/en/30.webp)



İşlemin son yayılımı için usb belleği çevrim dışı bilgisayardan çıkarın ve internete bağlı bilgisayara takın.



Yalnızca izlemeden içe aktarma prosedürünü tekrarlayın, yani _Araçlar_ menüsünden _İşlemi yükle_ ve son olarak _Dosyadan_ öğesini seçin.



![image](assets/en/31.webp)



Electrum sizin için işlem penceresini açacaktır, bu Wallet'de daha önce gösterilenden belirgin bir şekilde farklıdır, çünkü artık imzalanmıştır (`Status: Signed`) ve `Broadcast` komutuna erişilebilir.



Yapmanız gereken son işlem tam da budur:



![image](assets/en/32.webp)



## Sonuçlar



Testleriniz artık tamamlandı. Kılavuzu izlediyseniz ve aynı sonuçları aldıysanız, Electrum ile iki farklı bilgisayarda Bitcoin'lerinizi saklamak için hava boşluğu tarzında kullanabileceğiniz bir Wallet Cold oluşturdunuz.



Sadece iki şeye çok dikkat etmeniz gerekecek:


1) **generate alıcı adreslerine asla Wallet airgap kullanmayın**. Çevrimdışı olduğu için, size her zaman test işlemini yapmak için kullandığınız adresle aynı olan ilk Address'yı sunacaktır;



![image](assets/en/33.webp)



yukarıdaki resimden de görebileceğiniz gibi, çevrimdışı Wallet kendi Address geçmişini bilmiyor. Bu açıdan tamamen kördür. **Sizin için yapabileceği tek görev çevrimdışı anahtarlarınızı saklamak ve işlemlerinizi imzalamaktır**_.



2) Yalnızca bu amaç için ayrılmış bir USB flash sürücü kullanın, **sık kullandığınız bir aracı kullanmayın**. Gündelik araçların siber saldırıya uğrama olasılığı daha yüksektir ve istemeden de olsa, ağ bağlantınız kesilmiş halde tuttuğunuz bilgisayara bile saldırabilirsiniz. Sadece bu amaçla kullandığınız bir USB belleğin, özellikle de harcama yapmak zorunda olmayan bir hodler iseniz, bilgisayarınızla çevrimiçi iletişim kurma fırsatı çok azdır, böylece virüs, kötü amaçlı yazılım vb. alma ve daha sonra iletme olasılığını azaltır.