---
name: Samourai Wallet - Recover
description: Samourai Wallet'de sıkışan bitcoinler nasıl kurtarılır?
---

![cover](assets/cover.webp)


Samourai Wallet'nin kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, uygulamanın bazı işlevleri artık çalışmıyor ve kendi Dojo'su olmayan kullanıcılar artık işlem yayınlayamıyor.


Son günlerde birkaç kullanıcıya bitcoinlerini kurtarmada yardımcı olduktan sonra, bir Samourai Wallet'ün restorasyonu sırasında ortaya çıkabilecek sorunların çoğuyla karşılaştığıma inanıyorum. Bu nedenle, bu eğitim, Samourai Wallet ekosisteminde ve bu olaydan etkilenen yazılımda çalışmaya devam eden ve artık kullanılamayan işlevleri belirlemek için bir durum raporu ile başlayacaktır. Ardından, Sparrow wallet yazılımını kullanarak bir Samourai Wallet'ü kurtarmak için adım adım ilerleyeceğiz. Bu süreçte karşılaşılan tüm olası engelleri inceleyecek ve bunları çözmeye yönelik çözümleri göreceğiz. Son bölümde ise sunucuya el konulmasının ardından gizliliğinize yönelik potansiyel riskleri keşfedeceksiniz.


_Birçok kullanıcıya iyileşmelerinde yardımcı olan ve deneyimlerini benimle paylaşan ve ayrıca neyin hala işlevsel olduğunu belirlemek için testlere katkıda bulunan [@Louferlou]'ya (https://twitter.com/Louferlou) çok teşekkür ederim._


## Samourai Wallet hala çalışıyor mu?


Evet, **Samourai Wallet uygulaması hala çalışıyor**, ancak belirli koşullar altında.


İlk olarak, uygulamanın daha önce akıllı telefonunuza yüklenmiş olması gerekir. Google Play Store uygulamayı kaldırdı ve APK ele geçirilen web sitesinde barındırıldı. Bu nedenle, şu anda Samourai'yi yüklemek karmaşıktır. Çevrimiçi APK'lar bulabilirsiniz, ancak kaynağından emin olmadığınız sürece indirmemenizi tavsiye ederim.


Samourai Wallet sayfasının artık Google Play Store'da mevcut olmadığı göz önüne alındığında, otomatik güncellemeleri devre dışı bırakmak mümkün değildir. Uygulama indirme platformlarına geri dönerse, davanın gelişimiyle ilgili daha fazla bilgi elde edilene kadar **otomatik güncellemeleri devre dışı bırakmak** akıllıca olacaktır.


Samourai Wallet akıllı telefonunuzda zaten yüklüyse, uygulamaya yine de erişebilmeniz gerekir. Samourai'nin Wallet işlevselliğini kullanmak için bir Dojo'ya bağlanmak şarttır. Önceden, kişisel Dojo'su olmayan kullanıcılar Bitcoin Blockchain bilgilerine erişmek ve işlemleri yayınlamak için Samourai'nin sunucularına bağlıydı. Bu sunucuların ele geçirilmesiyle, uygulama artık bu verilere erişemiyor.

Daha önce bağlı bir Dojo'nuz yoksa ancak şimdi bir Dojo'nuz varsa, Samourai uygulamanızı tekrar kullanacak şekilde ayarlayabilirsiniz. Bunun için yedeklerinizi kontrol etmeniz, Wallet'ü (uygulamayı değil, Wallet'ü) silmeniz ve Dojo'nuzu uygulamaya bağlayarak Wallet'ü kurtarmanız gerekir. Bu adımlarla ilgili daha fazla ayrıntı için bu eğitimin "_Samourai Cüzdanınızı Hazırlama_" bölümüne bakabilirsiniz: CoinJoin - DOJO.

Samourai uygulamanız zaten kendi Dojo'nuza bağlıysa, Wallet kısmı sizin için mükemmel şekilde çalışır. Bakiyenizi ve yayın işlemlerinizi hala görebilirsiniz. Olan biten her şeye rağmen, Samourai Wallet'ün şu anda en iyi mobil Wallet yazılımı olmaya devam ettiğini düşünüyorum. Şahsen ben kullanmaya devam etmeyi planlıyorum.


Karşılaşabileceğiniz ana sorun, uygulamadan Whirlpool hesaplarına erişilememesidir. Samourai genellikle bu hesaplara erişim sağlamadan önce Whirlpool CLI ile bağlantı kurmaya ve CoinJoin döngülerini başlatmaya çalışır. Ancak, bu bağlantı artık mümkün olmadığından, uygulama size Whirlpool hesaplarına erişim izni vermeden süresiz olarak aramaya devam eder. Bu durumda, Samourai'de yalnızca mevduat hesabını tutarken bu hesapları başka bir Wallet yazılımında kurtarabilirsiniz.


### Samourai'de hala hangi araçlar mevcut?


Öte yandan, bazı araçlar ya sunucunun kapanmasından etkilenir ya da tamamen kullanılamaz.


Bireysel harcama araçlarıyla ilgili olarak, elbette kendi Dojo'nuzun olması koşuluyla her şey normal şekilde çalışır. Normal Stonewall işlemleri (Stonewall x2 değil) sorunsuz çalışır.


Twitter'da yapılan yorumlar, bir Stonewall işleminin sunduğu gizliliğin artık azalabileceğinin altını çizdi. Bir Stonewall işleminin katma değeri, yapı bakımından bir Stonewall x2 işleminden ayırt edilemez olmasında yatmaktadır. Bir analist bu özel modelle karşılaştığında, bunun tek kullanıcılı standart bir Stonewall mu yoksa iki kullanıcılı bir Stonewall x2 mi olduğunu belirleyemez. Ancak, ilerleyen paragraflarda göreceğimiz üzere, Soroban'ın kullanılamaması nedeniyle Stonewall x2 işlemlerinin gerçekleştirilmesi daha karmaşık hale gelmiştir. Bu nedenle bazıları, bir analistin artık bu yapıdaki herhangi bir işlemin normal bir Stonewall olduğunu varsayabileceğini düşünmektedir. Şahsen ben bu varsayımı paylaşmıyorum. Stonewall x2 işlemlerine daha az rastlanıyor olsa da (ki bence bu olaydan önce de bu tür işlemlere rastlanıyordu), bu işlemlerin hala mümkün olduğu gerçeği, bu işlemlerin mümkün olmadığı varsayımına dayanan tüm bir analizi geçersiz kılabilir.

**[-> Stonewall işlemleri hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Ricochet ile ilgili olarak, Testnet üzerinde bir Dojo'ya sahip olmadığım için hizmetin hala çalışır durumda olup olmadığını doğrulayamadım ve yetkililer tarafından kontrol edilebilecek bir Wallet için `100 000 Sats` harcama riskini almayı tercih etmiyorum. Bu aracı yakın zamanda test etme fırsatınız olduysa, bu makaleyi güncelleyebilmemiz için sizi benimle iletişime geçmeye davet ediyorum.


Ricochet kullanmanız gerekiyorsa, bu işlemi herhangi bir Wallet yazılımı ile her zaman manuel olarak gerçekleştirebileceğinizi unutmayın. Çeşitli atlamaların manuel olarak nasıl düzgün bir şekilde gerçekleştirileceğini öğrenmek için bu diğer makaleye başvurmanızı tavsiye ederim: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


JoinBot aracı, tamamen Samourai tarafından yönetilen bir Wallet'in katılımına bağlı olduğu için artık çalışmamaktadır.


Genellikle "cahoots" olarak adlandırılan diğer işbirlikçi işlem türleriyle ilgili olarak, bunlar mümkün olmaya devam etmektedir, ancak yalnızca manuel olarak. Sunucu kapatılmadan önce, Stonewall x2 veya Stowaway (PayJoin) işlemlerini gerçekleştirmek için iki seçeneğiniz vardı:



- PSBT'leri otomatik ve uzaktan Exchange yapmak için Soroban ağını kullanın;
- Ya da birden fazla QR kodunu tarayarak bu değişimleri manuel olarak gerçekleştirin.


Birkaç testten sonra Soroban'ın artık çalışmadığı anlaşıldı. Bu ortak işlemleri gerçekleştirmek için, verilerin Exchange'i bu nedenle manuel olarak yapılmalıdır. İşte bu Exchange'i gerçekleştirmek için iki seçenek:



- İşbirlikçinize fiziksel olarak yakınsanız, QR kodlarını art arda tarayabilirsiniz;
- İşbirliği yaptığınız kişiden uzaktaysanız, PSBT'leri uygulamaya harici bir iletişim kanalı aracılığıyla Exchange yapabilirsiniz. Ancak, bu PSBT'lerde yer alan veriler gizlilik açısından hassas olduğundan dikkatli olun. Exchange'un gizliliğini sağlamak için şifreli bir mesajlaşma hizmeti kullanmanızı öneririm.


**[-> Stonewall x2 işlemleri hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Stowaway işlemleri hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


Whirlpool'e gelince, protokol artık kendi Dojo'ları olan kullanıcılar için bile çalışmıyor gibi görünüyor. Son birkaç gündür RoninDojo'mu izliyordum ve bazı temel manipülasyonları denedim, ancak Whirlpool CLI sunucu kapatıldığından beri bağlanamadı.


Bununla birlikte, durumun nasıl geliştiğine bağlı olarak, bu protokolün önümüzdeki haftalarda yeniden etkinleştirilebileceği veya belki de farklı bir şekilde yeniden tasarlanabileceği konusunda umutluyum. Bu duraklama, bu sistemde yeni yaklaşımlar veya potansiyel iyileştirmeler keşfetmek için bir fırsat olabilir.


### Hangi harici araçlar hala mevcut?


Samourai ortamıyla ilgili diğer araçlarla ilgili olarak, bazıları hala mevcutken diğerleri mevcut değildir.


Ücretsiz zincir analizi web sitesi OXT.me ne yazık ki şu an için artık kullanılamıyor.


Whirlpool Stats Tool, Samourai'nin GitLab'ında barındırıldığı için artık indirilemiyor. Bu Python aracını daha önce makinenize yerel olarak indirmiş olsanız veya RoninDojo düğümünüze yüklenmiş olsa bile, WST şu an için çalışmayacaktır. Aslında, çalışması için OXT.me tarafından sağlanan verilere bağlıydı ve bu siteye artık erişilemiyor. Şu anda, Whirlpool protokolü etkin olmadığından WST özellikle kullanışlı değildir.


KYCP.org sitesine şu anda erişilememektedir.


Boltzmann Calculator Python aracının kodunu barındıran GitLab da ele geçirilmiştir. Bu nedenle, şu anda bu aracı indirmek artık mümkün değildir. Ancak bir RoninDojo'nuz varsa, Boltzmann Calculator'ı daha önce olduğu gibi kullanmaya devam edebilirsiniz.


RoninDojo'ya gelince, bu node-in-box yazılımı Whirlpool CLI ve WST gibi belirli araçların kullanılamamasına rağmen doğru şekilde çalışmaya devam etmektedir. Fulcrum veya Electrs sayesinde diğer Wallet yazılımları için hala kullanılabilir. RoninDojo hakkında daha fazla bilgi edinmek isterseniz veya özel sorularınız varsa, [Telegram gruplarına] (https://t.me/RoninDojoNode) katılmanızı tavsiye ederim.


Ancak, RoninDojo'nun kaynak kodu Samourai'nin GitLab'ında barındırıldığı için artık erişilebilir değil. Bu nedenle şu anda bir Raspberry Pi'ye manuel olarak yüklemek mümkün değildir.


Watch-only wallet yazılımı Sentinel ile ilgili olarak, durum Samourai uygulamasınınkine benzer. Eğer kendi Dojo'nuz varsa, Sentinel'i sorunsuz bir şekilde kullanmaya devam edebilirsiniz. Ancak, bir Dojo'nuz yoksa, artık bir bağlantı kuramazsınız. Samourai'nin aksine, Sentinel web sitesine hala çevrimiçi olarak erişilebilir. Ancak bu site ve orada sunulan APK konusunda dikkatli olun, çünkü şu anda bu kaynakları kimin kontrol ettiği belli değil.


### Sparrow wallet etkileniyor mu?


Sparrow wallet, artık mevcut olmayan Samourai araçları haricinde normal şekilde çalışmaya devam etmektedir. Şu anda, Sparrow üzerinden para birleştirme işlemi gerçekleştirmek artık mümkün değildir. Benzer şekilde, Sparrow, Samourai'nin aksine PSBT'lerin manuel Exchange seçeneğini sunmadığından, işbirliğine dayalı harcama araçlarına da artık erişilememektedir. Diğer tüm işlevler için Sparrow sorunsuz çalışmaktadır. Gerekirse bu yazılımı bir Samourai Wallet'i kurtarmak için de kullanabilirsiniz.


## Bir Samourai Wallet Nasıl Kurtarılır?


Önceki bölümlerde gördüğümüz gibi, kendi Dojo'nuz varsa, mutlaka yazılım değiştirmeniz gerekmez. **Samourai günlük harcamalarınız için mükemmel bir Hot Wallet** seçimi olmaya devam ediyor. Bununla birlikte, bir Dojo'nuz yoksa veya başka bir yazılımı tercih etmeyi tercih ederseniz, karşılaşabileceğiniz olası engelleri detaylandırarak tüm kurtarma sürecini açıklayacağım.


Her halükarda, zaman ayırmanız ve hata yapmadığınızdan emin olmanız önemlidir. Unutmayın, özel anahtarlarınız sizde olduğu için acele etmenize gerek yok ve Samourai'nin sunucularına el konulması bunu hiçbir şekilde etkilemez. Ne olursa olsun, özel anahtarlarınıza erişemeyecekleri açıktır.


### passphrase'u doğrulayın


Wallet cihazınızı kurtarmak için, yedekleme dosyası aracılığıyla kurtarmayı tercih etseniz bile passphrase cihazınız olmalıdır. Bu passphrase'nin geçerliliğini doğrulayarak başlayın. Samourai Wallet uygulamanızı açın, sol üstteki Paynym simgesine tıklayın ve ardından `Ayarlar`ı seçin.


![samourai](assets/1.webp)


Ardından, `Sorun Giderme` ve ardından `passphrase/yedekleme testi` üzerine tıklayın.


![samourai](assets/2.webp)


passphrase'ünüzü girin ve `Ok`a tıklayın. Eğer doğruysa, Samurai bunu onaylayacaktır. Daha sonra kullanmayı planlıyorsanız yedekleme dosyasını doğrulama seçeneğiniz de vardır.


![samourai](assets/3.webp)


Bu adım isteğe bağlıdır ancak tavsiye edilir. passphrase'ün doğru olduğunu teyit eder ve daha sonra olası bir sorun kaynağını ortadan kaldırır. Samourai bu aşamada passphrase'ün yanlış olduğunu belirtirse, kurtarma mümkün olmayacaktır. passphrase'ü doğru girdiğinizden emin olun ve tekrar kontrol edin.


### Seçenek 1: Wallet'yı Sparrow üzerinde yedekleme dosyası ile kurtarın


Sparrow wallet'nin 1.8.6 sürümünden bu yana, uygulamanızın otomatik olarak oluşturduğu `samourai.txt` adlı yedek metin dosyasını kullanarak Samourai Wallet'unuzu doğrudan içe aktarmak mümkündür. Bu dosya Wallet'unuzu kurtarmak için gerekli tüm bilgileri içerir ve güvenlik için passphrase'inizle şifrelenmiştir.


Bu seçeneği seçerseniz, güncel `samourai.txt` dosyanıza ve passphrase'ınıza ihtiyacınız olacaktır. Bu dosyayı Samourai Wallet üzerinde generate yapmak için, sağ üstteki üç küçük noktaya tıklayın, ardından `Wallet yedeğini dışa aktar` seçeneğini seçin.


![samourai](assets/4.webp)

Ardından, `Panoya Aktar` seçeneğini seçin. Bundan sonra, bu dosyayı güvenli bir şekilde bilgisayarınıza aktarmanız gerekecektir. Dosya şifrelenmiş olduğundan, ancak passphrase tek başına şifresini çözmek için yeterli olduğundan, aktarımı sırasında önlem almak önemlidir. Düz metin olarak doğrudan aktarımı tercih ederseniz, bilgisayarınızda bir `samourai.txt` dosyası oluşturmanız ve pano içeriğini bu dosyaya yapıştırmanız gerekecektir. Bir alternatif de `samourai.txt` dosyasını telefonunuzda depolanan dosyalardan doğrudan almak olabilir.

Bilgisayarınızda dosyaya erişiminiz olduğunda, Sparrow wallet'ü açın, `Dosya` sekmesine tıklayın ve Wallet'inizi içe aktarmaya başlamak için `Wallet'i İçe Aktar` seçeneğini seçin.


![samourai](assets/5.webp)


Aşağı kaydırarak `Samourai Yedekleme` seçeneğine gidin, `Dosya Aktar` seçeneğine tıklayın ve ardından `samourai.txt` dosyanızı seçin.


![samourai](assets/6.webp)


Sparrow daha sonra dosyanın şifresini çözmek için sizden bir şifre isteyecektir. Bu şifre aslında sizin passphrase'nızdır. İlgili alana girin ve `İçe Aktar` seçeneğine tıklayın.


![samourai](assets/7.webp)


Bu aşamada Wallet'unuz görünmezse, `samourai.txt` dosyasını kopyalarken veya passphrase'i girerken bir hata yapmış olabilirsiniz. Daha fazla yardım için sorun giderme bölümüne başvurabilirsiniz.


![samourai](assets/8.webp)


Komut dosyası türü için, Samourai'de başka komut dosyaları yapılandırmadıysanız, normalde yalnızca SegWit V0 (Yerel SegWit / P2WPKH) kullanmalısınız. Bu varsayılan komut dosyasını saklayın ve `İçe Aktar` seçeneğine tıklayın.


![samourai](assets/9.webp)


Wallet'nize bir isim verin, örneğin "Samourai Recovery", ve ardından `Wallet Oluştur`a tıklayın.


![samourai](assets/10.webp)


Sparrow daha sonra sizden bir parola seçmenizi isteyecektir. Bu parola yalnızca bu bilgisayardaki Wallet'ünüze erişimi korur ve Wallet'ünüzün anahtarlarının türetilmesiyle ilgili değildir. Güçlü bir parola seçtiğinizden emin olun, hatırlamak için not edin ve `Parola Ayarla`ya tıklayın.


![samourai](assets/11.webp)


Sparrow daha sonra Wallet'nızın anahtarlarını türetecek ve ilgili işlemleri arayacaktır.


![samourai](assets/12.webp)


Şimdilik sadece mevduat hesabınıza erişebilirsiniz. Samourai'yi yalnızca bu hesap için kullanıyorsanız, tüm fonlarınızı görmeniz gerekir. Ancak, Whirlpool'yi de kullanıyorsanız, `premix`, `postmix` ve `badbank` hesaplarını türetmeniz gerekecektir. Sparrow'de, `Ayarlar` sekmesine ve ardından `Hesap Ekle...` seçeneğine tıklamanız yeterlidir.


![samourai](assets/13.webp)

Açılan pencerede, açılır menüden `Whirlpool Hesapları`nı seçin ve ardından `Tamam`a tıklayın.

![samourai](assets/14.webp)


Daha sonra çeşitli Whirlpool hesaplarınızın göründüğünü göreceksiniz ve Sparrow ilgili bitcoinleri kullanmak için gerekli anahtarları türetecektir.


![samourai](assets/15.webp)


Samourai Wallet'ünüzü kurtarmak için Electrum gibi Sparrow'ten farklı bir yazılım kullanıyorsanız, manuel kurtarma için Whirlpool hesap dizinlerini burada bulabilirsiniz:



- Depozito: `m/84'/0'/0'`
- Kötü Banka: `m/84'/0'/2147483644'`
- Premiks: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Artık bitcoinlerinize Sparrow üzerinden erişebilirsiniz. Sparrow wallet'i kullanmak için yardıma ihtiyacınız varsa, [özel eğitimimize] (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) de göz atabilirsiniz.


Ayrıca Samourai'deki UTXO'larınızla ilişkilendirdiğiniz etiketleri manuel olarak içe aktarmanızı tavsiye ederim. Bu, daha sonra Sparrow üzerinde etkili Coin kontrolü yapmanıza olanak sağlayacaktır.


### Seçenek 2: Wallet'yi Sparrow üzerinde Mnemonic ifadesiyle kurtarın


Kurtarma işlemini yedekleme dosyasıyla gerçekleştirmek istemiyorsanız, sadece 12 kelimelik kurtarma ifadenizi ve passphrase'ünüzü kullanarak daha geleneksel bir yöntemi tercih edebilirsiniz. Bu ikinci seçenek genellikle daha basittir.


Başlamak için, kurtarma cümlenizin ve passphrase'inizin elinizde olduğundan emin olun. Ardından, Sparrow wallet yazılımını açın, `Dosya` sekmesine tıklayın ve Wallet'nızı içe aktarmaya başlamak için `Wallet'yı içe aktar` seçeneğini seçin.


![samourai](assets/16.webp)


Mnemonic Words (BIP39)` seçeneğini seçin ve açılır menüden `Use 12 Words` seçeneğine tıklayın.


![samourai](assets/17.webp)


Kurtarma cümlenizin 12 kelimesini doğru sırada girin.


![samourai](assets/18.webp)


Sparrow bir `Geçersiz Sağlama Toplamı` mesajı görüntülerse, bu kurtarma ifadesinin sağlama toplamının geçerli olmadığını gösterir, bu da muhtemelen kelimeleri girerken bir hata yaptığınız anlamına gelir.


![samourai](assets/19.webp)


İfadeniz doğruysa, `passphrase Kullan` kutusunu işaretleyin ve passphrase'unuzu özel alana girin. Son olarak, her şey doğru görünüyorsa, `Wallet`ü Keşfet` düğmesine tıklayın.


![samourai](assets/20.webp)


Wallet'inize bir isim verin, örneğin "Samourai Recovery", ardından `Wallet Oluştur`a tıklayın.


![samourai](assets/21.webp)

Sparrow daha sonra sizden bir parola seçmenizi isteyecektir. Bu parola yalnızca bu bilgisayardaki Wallet'ünüze erişimi korur ve Wallet'ünüzün anahtarlarının türetilmesiyle ilgili değildir. Güçlü bir parola seçtiğinizden emin olun, hatırlamak için bir yere yazın ve `Parola Ayarla`ya tıklayın.

![samourai](assets/22.webp)


Sparrow daha sonra Wallet'iniz için anahtarları türetecek ve ilgili işlemleri arayacaktır.


![samourai](assets/23.webp)


Bu aşamada Wallet'niz görünmezse, passphrase'yı veya kurtarma ifadesini girerken bir hata yapmış olabilirsiniz. Daha fazla yardım için özel sorun giderme bölümüne başvurabilirsiniz.


Şimdilik sadece mevduat hesabınıza erişebilirsiniz. Samourai'yi yalnızca bu hesap için kullanıyorsanız, tüm fonlarınızı görmeniz gerekir. Ancak, Whirlpool'i de kullanıyorsanız, `premix`, `postmix` ve `badbank` hesaplarını türetmeniz gerekecektir. Sparrow'da, `Ayarlar` sekmesine ve ardından `Hesap Ekle...` seçeneğine tıklamanız yeterlidir.


![samourai](assets/24.webp)


Açılan pencerede, açılır listeden `Whirlpool Hesapları`nı seçin ve ardından `Tamam`a tıklayın.


![samourai](assets/25.webp)


Daha sonra çeşitli Whirlpool hesaplarınızın göründüğünü göreceksiniz ve Sparrow ilgili bitcoinleri kullanmak için gerekli anahtarları türetecektir.


![samourai](assets/26.webp)


Samourai Wallet'ünüzü kurtarmak için Electrum gibi başka bir yazılım kullanıyorsanız, manuel kurtarma için Whirlpool hesap dizinlerini burada bulabilirsiniz:



- Depozito: `m/84'/0'/0'`
- Kötü Banka: `m/84'/0'/2147483644'`
- Premiks: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Artık Sparrow'da bitcoinlerinize erişebilirsiniz. Sparrow wallet'i kullanmak için yardıma ihtiyacınız varsa, [özel eğitimimize] (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) de başvurabilirsiniz.


Ayrıca Samourai'deki UTXO'larınızla ilişkilendirdiğiniz etiketleri manuel olarak içe aktarmanızı tavsiye ederim. Bu, daha sonra Sparrow üzerinde etkili Coin kontrolü yapmanıza olanak sağlayacaktır.


### Karşılaşılan yaygın sorunlar nelerdir?


Son birkaç gün içinde birkaç kişiye yardımcı olduktan sonra, Wallet'nizin kurtarılmasını engelleyebilecek sorunların çoğuyla karşılaştığıma inanıyorum. Önceki eğitimlere rağmen hala Wallet'nize erişemiyorsanız, işte bazı ek öneriler.

Öncelikle ve en önemlisi, kurtarma işleminin çalışması için kurtarma ifadesinin doğru olması kesinlikle çok önemlidir. Eğer 12 kelimelik cümlenizi bulamazsanız, Samourai'nin yedek dosyasından kurtarmak için _seçenek 1_'i kullanabilirsiniz. Kurtarma ifadenize doğrudan Samourai Wallet'de `Ayarlar'a, ardından `Wallet'e giderek ve son olarak `12 kelimelik kurtarma ifadesini göster'i seçerek de erişebilirsiniz.


Daha sonra, kurtarma sırasında passphrase'nizdeki bir yazım hatası, yanlış türetilmiş anahtarlara neden olacak ve bu da Wallet'ünüzün Sparrow üzerinde kurtarılmasını engelleyecektir. **passphrase tamamen doğru olmalıdır!**


Bunu çözmek için, öncelikle bu makalenin "_Şifreyi doğrulayın_" bölümünde açıklandığı gibi Samourai uygulamasında passphrase'inizin geçerliliğini kontrol etmenizi tavsiye ederim:


1. **Samourai'de doğrulama:** Samourai passphrase'nın doğru olduğunu onaylarsa, passphrase'yı Sparrow'ye hatasız bir şekilde girdiğinizden emin olarak kurtarma işlemini en baştan tekrar deneyin;

2. **passphrase Hatası:** Samourai passphrase'in yanlış olduğunu belirtirse, Sparrow üzerinde denemelere devam etmek anlamsızdır. Doğru passphrase bulunamadığı sürece, Wallet'unuzun kurtarılması imkansızdır. passphrase'inizi kalıcı olarak kaybettiyseniz, Samourai uygulamanızı güvende tutun. Yapabileceğiniz tek şey sunucuların yeniden başlatılmasını ummaktır, böylece kurtarma işlemine gerek kalmadan doğrudan uygulamadan harcama yapabilirsiniz. **Bu durumda bir Dojo'ya bağlanmaya çalışmayın**, çünkü bu passphrase'e erişim gerektiren Samourai'deki Wallet'unuzu sıfırlamak anlamına gelecektir.


Karşılaşılan diğer hataların birçoğu Sparrow'deki ağ yapılandırmasıyla ilgilidir.


Öncelikle, Sparrow'ün `Testnet` modu yerine `Mainnet` modunda doğru şekilde yapılandırıldığından emin olun. Gerçekten de, Sparrow işlemlerinizi Testnet üzerinde ararsa, hiçbir şey bulamayacaktır, çünkü Wallet'nız Mainnet üzerindedir. Testnet, Bitcoin'nin yalnızca test ve geliştirme için kullanılan alternatif bir sürümüdür ve kendi blokları ve işlemleriyle ana ağdan (Mainnet) ayrı bir ağda çalışır. Hangi ağda olduğunuzu kontrol etmek için `Araçlar` sekmesine ve ardından `Yeniden Başlat` seçeneğine tıklayın. Eğer `Mainnet` seçeneği görüntüleniyorsa, ana ağda değilsiniz demektir. Mainnet üzerinde Sparrow'ü yeniden başlatmak için bunu seçin ve ardından kurtarma işleminize tekrar başlayın.


![samourai](assets/27.webp)

Bazıları Sparrow'u düğümlerine bağlarken de zorluklarla karşılaşmıştır. Sparrow'un sağ alt kısmında, renkli bir anahtar yazılımınızın bir Bitcoin düğümüne doğru şekilde bağlanıp bağlanmadığını gösterir. Samourai işlemlerinizi almak için yazılımın iyi bağlanmış olması çok önemlidir. Aşağıdaki resimde olduğu gibi anahtarın etkin olup olmadığını kontrol edin (halka açık bir düğüm için sarı, Bitcoin core için Green ve bir Electrum sunucusu için mavi).

![samourai](assets/28.webp)


Anahtar etkinleştirilmemişse, bağlantıyı yeniden etkinleştirmek için üzerine tıklayın.


![samourai](assets/29.webp)


Sorun devam ederse, işte bazı olası çözümler:



- Kendi Electrum sunucunuza (mavi) bağlanmaya çalışıyorsanız veya Bitcoin core (Green) ve Sparrow bağlanamıyorsa, `Dosya > Tercihler... altında bağlantı bilgilerini kontrol edin. > Sunucu` altında kontrol edin;


![samourai](assets/30.webp)



- Bağlantı sorunu devam ederse, düğümünüzün eksik senkronizasyonundan kaynaklanıyor olabilir. Düğümünüzün ve dizinleyicinizin %100 senkronize olduğundan emin olun. Gerekirse son çare olarak düğümünüzün Sparrow ile bağlantısını kesin ve genel bir düğüme bağlanın;
- Zaten genel bir düğüme bağlıysanız ve bağlantı başarısız olursa, açılır listeden başka bir düğüm seçerek düğümü değiştirmeyi deneyin.


![samourai](assets/31.webp)


Wallet'inizi başarıyla kurtardıysanız ancak eksik görünüyorsa, türetmeyle ilgili bir sorun olabilir.


Samourai mevduat hesabınızı `P2WPKH`den farklı bir komut dosyası türüyle kullandıysanız bir sorun oluşabilir. Varsayılan olarak, Samourai bu komut dosyası türünü kullanır, ancak bunu manuel olarak değiştirdiyseniz, Sparrow'da kurtarma yaparken bunu da ayarlamanız gerekir.


Diğer komut dosyası türleri için dallar türetmek için, kullanılan her komut dosyası türü için kurtarma işlemini tekrarlamanız gerekir. Bunun için, Sparrow üzerinde `Dosya > Yeni Wallet` seçeneğine gidin, açılır listeden başka bir komut dosyası türü seçin, `Yeni veya İçe Aktarılan Software Wallet` seçeneğine tıklayın ve ilk eğitimdeki adımların aynısını izleyin.


![samourai](assets/32.webp)


Karşılaştığım bir başka türetme sorunu da Gap Limit değeri ile ilgilidir. Bu değer Sparrow'e kaç boş adresten sonra yeni adres türetmeyi durdurması gerektiğini söyler. Kurtarma işleminden sonra bazı işlemlerin eksik olduğunu fark ederseniz, bunun nedeni Boşluk Limitinin çok düşük olması olabilir. Bunu çözmek için, soruna neden olan hesaba, örneğin postmix hesabına gidin (birden fazla hesap söz konusuysa, bu işlemi her biri için tekrarlayın).


![samourai](assets/33.webp)


Ayarlar` sekmesine ve ardından `Gelişmiş...` düğmesine tıklayın.

![samourai](assets/34.webp)

Boşluk Limitinin değerini kademeli olarak artırın, örneğin ben burada `400` olarak ayarladım. Ardından, `Kapat` düğmesine tıklayın.


![samourai](assets/35.webp)


Sonlandırmak için `Uygula` üzerine tıklayın. Sparrow daha sonra daha fazla sayıda adres türetecek ve bunlar üzerinde fon arayacak, bu da tüm işlemlerinizi kurtarmanıza yardımcı olacaktır.


![samourai](assets/36.webp)


Bu, son birkaç gün içinde karşılaştığım çeşitli kurtarma sorunlarını kapsıyor. Tüm bu çözümleri denedikten sonra hala sorun yaşıyorsanız, sizi yardım istemek için [Discover Bitcoin Discord] (https://discord.gg/xKKm29XGBb) adresine katılmaya davet ediyorum. Bu Discord'u düzenli olarak ziyaret ediyorum ve eğer bir çözümüm varsa yardımcı olmaktan memnuniyet duyarım. Diğer bitcoin kullanıcıları da deneyimlerini paylaşabilir ve yardımlarını sunabilirler. **Her durumda, kurtarma ifadenizi, yedekleme dosyanızı ve passphrase'ünüzü gizli tutmanız çok önemlidir**. Bunları kimseyle paylaşmayın, çünkü bu bitcoinlerinizi çalmalarına izin verebilir.


Kurtarma işlemi tamamlandığında, artık bitcoinlerinize erişebilirsiniz. Bu iyi bir şey, ancak yeterli olmayabilir. Aslında, sunucuların ele geçirilmesi gizliliğiniz için yeni potansiyel riskler ortaya çıkarmaktadır. Aşağıdaki bölümde bu riskleri ayrıntılı olarak inceleyecek ve gizliliğinizi korumak için almanız gereken önlemleri özetleyeceğiz.


## İşlemlerinizin gizliliği açısından ne gibi sonuçlar doğurur?


### Dojo'su olmayan bir Samourai kullanıcısı olarak


Kendi Dojo'nuzu bağlamadan Samourai Wallet kullanıyorsanız, uygulamanın çalışması için xpub'larınızın Samourai sunucularına iletilmesi gerekiyordu. Bu sunuculara el konulmasıyla, yetkililerin artık bu xpub'lara erişiminin olması mümkündür.


Bu senaryo varsayımsal olarak kalmaktadır. Bu xpub'ların kaydedilip kaydedilmediğini, herhangi bir potansiyel depolamanın yok edilip edilmediğini, yetkililerin bunları kurtarıp kurtarmadığını ve zincir analizi için kullanmayı planlayıp planlamadıklarını bilmiyoruz. Ancak böyle bir durumda, yetkililerin kendi Dojo'larını bağlamayan kullanıcıların xpub'larına sahip olduğu en kötü senaryoyu göz önünde bulundurmak ihtiyatlı olacaktır.

Referans olarak, bir xpub, alt açık anahtarları (açık anahtar + chain code) oluşturmak için gerekli tüm Elements'yi içeren bir karakter dizisidir. Hiyerarşik deterministik cüzdanlarda generate adresleri almak ve ilişkili özel anahtarları ifşa etmeden bir hesabın işlemlerini gözlemlemek için kullanılır. Bu, örneğin bir "sadece izle" Wallet oluşturulmasına izin verir. Ancak, xpub'ların ifşa edilmesi, üçüncü tarafların işlemleri izlemesine ve ilişkili hesapların bakiyelerini görmesine izin verdiği için kullanıcının gizliliğini tehlikeye atabilir.

Böylece xpub'larınızı bilen herkes Wallet'ınızın tüm alıcı adreslerini, geçmişte kullanılanları ve gelecekte oluşturulacak olanları görebilir.


Dojo'su olmayan kullanıcılar için xpub'larınızın olası bir sızıntısının iki önemli sonucu vardır:



- Gerçekleştirmiş olabileceğiniz coin birleştirmeleri, xpub'larınızı bilen herkes için gizlilik açısından etkisiz hale getirilir, böylece coin'leriniz tüm anonsetini kaybeder;
- Bu kişi aynı zamanda Samourai Wallet'inizin tüm alıcı adreslerini de takip edebilir.


Bu nedenle en kötü senaryoyu göz önünde bulundurmak ve gizlilik açısından potansiyel olarak tehlikede olan bu Wallet'ten ayrılmak önemlidir. Bunu yapmak için, Sparrow wallet gibi başka bir yazılımla sıfırdan yeni bir Wallet oluşturun. Yedeklerinizin geçerliliğini doğruladıktan sonra, işlem yaparak tüm fonlarınızı aktarın. Bu işlem coin'lerinizin izlenebilirlik bağlantısını koparmasa da yetkililerin yeni Wallet'ünüzün adreslerini kesin olarak bilmesini engelleyecektir.


Bu transfer işlemi sırasında, coin'lerinizin konsolidasyonundan kaçınmanızı öneririm. Xpub'larınızın ele geçirildiğini varsayarsak, bu xpub'lara erişimi olan kişinin bakış açısından konsolidasyonun bir etkisi olmayacaktır, çünkü gizliliğiniz zaten onlarla tehlikeye atılmıştır. Ancak, gizliliğinizi diğer insanlardan korumak için coinlerinizi çok fazla konsolide etmemenizi tavsiye ederim. En kötü durumda, xpub'larınıza yalnızca yetkililer erişebilir, ancak dünyanın geri kalanı bunları bilmez. Bu nedenle, başkalarının bakış açısından, coin'lerinizi birleştirmek, Ortak Giriş Ownership Sezgisel (CIOH) nedeniyle gizliliğinize önemli ölçüde zarar verebilir.


**Not:** takibi kesin olarak kırmak için, bu yeni Wallet'ten eş birleştirmeler yapmayı da düşünebilirsiniz.

**Uyarı:** Samourai Wallet'inizi Sparrow wallet'ya geri yüklemek yeterli değildir. Sızmış olabilecek xpub'ları kullanmaktan kaçınmak istiyorsanız, yeni bir kurtarma ifadesiyle tamamen yeni bir Wallet oluşturmanız gerekir. Mevcut seed'unuzu Sparrow'ye aktarırsanız, yalnızca Wallet yönetim yazılımını değiştirmiş olursunuz, ancak Wallet aynı kalır.


### Dojo ile Sparrow veya Samourai kullanıcısı olarak


Wallet'ünüz yalnızca Sparrow wallet üzerinde yönetiliyorsa, ister genel bir düğüm ister kendi Bitcoin düğümünüzü kullanıyor olun, xpub'larınız sızdırılamaz. Benzer şekilde, Samourai uygulamasını kullanıyorsanız ve bu uygulamayı Wallet'ünüzün oluşturulmasından bu yana her zaman kendi Dojo'nuza bağladıysanız, xpub'larınız da güvenlidir.


Ancak, aynı Wallet'ü bir süre **kendi Dojo'nuz olmadan** ve daha sonra kendi Dojo'nuzla kullandıysanız, Samourai sunucularının xpub'larınıza erişmiş olması ve dolayısıyla yetkililerin bunları bilmesi mümkündür. Bu özel durumdaysanız, önceki bölümdeki tavsiyelere uymanızı ve xpub'larınızı tehlikeye atılmış olarak değerlendirmenizi tavsiye ederim.


Her zaman kendi Dojo'ları ile Sparrow veya Samourai kullananlar için ana risk, madeni paralarınızın anonsetlerinin potansiyel olarak azaltılabilmesidir. En kötü senaryoda, Dojo'su olmayan tüm kullanıcıların xpub'larının yetkililerin elinde olduğunu varsayalım, o zaman paralarının CoinJoin döngüleri boyunca izlediği yol bu yetkililer tarafından takip edilebilir.


Bunu açıklamak için somut bir örnek verelim. CoinJoin'nin ilk döngüsüne katıldığınızı ve ardından iki ek CoinJoin döngüsüne katıldığınızı düşünün. Dojo'su olmayan kullanıcıların xpub'ları sızdırılmadıysa, Coin'inizin olası anonsu 13 olacaktır.


![samourai](assets/37.webp)


Bununla birlikte, xpub'ların sızdırıldığını ve ilk CoinJoin sırasında dojosu olmayan bir kullanıcıyla karşılaştığınızı ve ardından ilk aşağı akış CoinJoin sırasında 2 kullanıcıyla karşılaştığınızı düşünürsek, olası anonsetiniz otoritenin bakış açısından 13 yerine sadece 10 olacaktır.


![samourai](assets/38.webp)

Anonsetteki bu potansiyel düşüşü ölçmek karmaşıktır, çünkü çok sayıda faktöre bağlıdır ve her Coin farklı şekilde etkilenir. Örneğin, erken döngülerde karşılaşılan Dojo'suz bir kullanıcı, sonraki döngülerde karşılaşılandan çok daha fazla olası anonseti etkiler. Varsayımsal olmaya devam eden durum hakkında bir fikir vermek için, Samourai tarafından sağlanan en son istatistikler, coinjoinlere dahil olan coinlerin %85 ila %90'ının Dojo, Sparrow veya Bitcoin Keeper'a sahip kullanıcılardan, yani en kötü senaryoda bile xpub'larının sızdırıldığını görmeyecek kullanıcılardan geldiğini göstermiştir.

Bu rakamları doğrulamak zor olsa da, bana iki nedenden dolayı tutarlı görünüyorlar:



- Sparrow wallet yaygın olarak kullanılmaktadır;
- Çoğu node-in-box yazılımı Dojo uygulamaları sunar ve Umbrel gibi bu ana akım yazılımlar günümüzde çok popülerdir.


Bu nedenle, çeşitli hususların göz önünde bulundurulması gerekir. Madeni paralarınızın yetkililere karşı gizliliği sizin için son derece önemliyse, en kötü senaryoya hazırlıklı olmak akıllıca olacaktır ve Dojo'su olmayan kullanıcılardan olası xpub sızıntısı nedeniyle Whirlpool CoinJoin döngülerinizin izlenemeyeceğini %100 garanti etmek zordur. Bu varsayım çok düşük bir ihtimal olsa da imkansız değildir.


Öte yandan, bu xpub'lara potansiyel olarak sahip olan otorite karşısında madeni paralarınızın gizliliği sizin için çok önemli değilse, o zaman durum farklı şekilde değerlendirilebilir.


"Yetkiliye karşı" diyorum çünkü yalnızca sunuculara el koyan yetkilinin potansiyel olarak bu xpub'lardan haberdar olduğunu unutmamak önemlidir. Eğer CoinJoin'yı kullanmaktaki amacınız fırıncınızın fonlarınızı takip etmesini engellemekse, o zaman sunucuya el konulmadan önceki durumdan daha iyi bir bilgiye sahip değildir.


Son olarak, sunucuya el konulmadan önce Coin'nizin ilk anonsetini dikkate almak önemlidir. İleriye dönük 40.000 anonsete ulaşmış bir Coin örneğini ele alalım; bu anonsetteki potansiyel düşüş muhtemelen ihmal edilebilir düzeydedir. Aslında, zaten çok yüksek bir temel anonset ile, Dojo'suz birkaç kullanıcının varlığının durumu kökten değiştirmesi pek olası değildir. Ancak, Coin'nizin anonseti 40 ise, bu potansiyel sızıntı anonsetlerinizi ciddi şekilde etkileyebilir ve potansiyel olarak izlemeye izin verebilir.

OXT.me'nin kapatılmasının ardından WST aracı artık hizmet dışı olduğundan, bu anonsetleri yalnızca tahmin edebilirsiniz. Geriye dönük anonset için endişelenecek çok fazla şey yok çünkü Whirlpool modeli, emsallerinizin mirası sayesinde ilk CoinJoin'dan çok yüksek olmasını sağlıyor. Bunun sorun yaratabileceği tek durum, Coin'ınızın birkaç yıldır remikslenmemiş olması ve bir havuzun lansmanının başında mikslenmiş olmasıdır. Muhtemel anonset ile ilgili olarak, Coin'ınızın coinjoins için mevcut olduğu süreyi inceleyebilirsiniz. Birkaç ay olmuşsa, muhtemelen son derece yüksek bir olası anonset değerine sahiptir. Tersine, sunucular ele geçirilmeden yalnızca birkaç saat önce bir havuza eklenmişse, o zaman olası anons süresi muhtemelen çok düşüktür.

**-> Anonsetler ve hesaplama yöntemleri hakkında daha fazla bilgi edinin.**


Dikkate alınması gereken bir diğer husus da konsolidasyonların karışık coin anonsları üzerindeki etkisidir. Whirlpool hesaplarına artık Samourai uygulaması üzerinden erişilemediği göz önüne alındığında, birçok kullanıcının Wallet'lerini başka bir yazılıma aktarmış ve fonlarını Whirlpool'den çekmeye çalışmış olması muhtemeldir. Özellikle, Bitcoin ağındaki işlem ücretlerinin nispeten yüksek olduğu geçen hafta sonu, karışım sonrası coinleri birleştirmek için güçlü bir teknik ve ekonomik teşvik vardı. Bu da birçok kullanıcının önemli ölçüde konsolidasyon yapmış olabileceği anlamına gelmektedir.


Bu karışım sonrası konsolidasyonlarla ilgili sorun, sadece bunları gerçekleştiren kullanıcı için değil, aynı zamanda CoinJoin döngüleri sırasında karşılaştıkları kullanıcılar için de her zaman anonsetleri azaltmalarıdır. Bu olguyu tam olarak doğrulayamamış ya da ölçememiş olsam da, o dönemdeki işlem ücretleriyle ilgili ekonomik teşvikler, anonsetlerin potansiyel olarak daha düşük olduğunu varsaymamıza yol açabilir.


### Sentinel Kullanıcısı Olarak


Watch-only wallet uygulaması Sentinel'in ağ çalışması Samourai'ninkine benzer. Wallet bilgilerinize erişmek için uygulamanın xpub'ları, açık anahtarları ve sağladığınız adresleri bir Dojo'ya iletmesi gerekir. Sentinel'de her zaman kendi Dojo'nuzu kullandıysanız, sorun yoktur ve uygulamayı endişelenmeden kullanmaya devam edebilirsiniz. Ancak, Sentinel'iniz için Samourai'nin sunucularına bağımlıysanız, xpub'larınızın açığa çıkmış olması mümkündür. Bu durumda, Samourai'nin sunucularına bağlıyken Samourai Wallet için önerilen aynı Wallet değişiklik sürecini izlemeniz önerilir.


Dojo'nuzu Sentinel ile değil de Samourai ile kullanıyor olmanız durumunda, xpub'larınızın tehlikede olduğunu düşünmek daha akıllıca olacaktır.


## Sonuç


Bu makaleyi sonuna kadar okuduğunuz için teşekkür ederim. Bilgilerin eksik olduğunu düşünüyorsanız veya önerileriniz varsa, lütfen düşüncelerinizi paylaşmak için benimle iletişime geçmekten çekinmeyin. Ayrıca, bu eğitime rağmen Samourai Wallet'unuzu kurtarmak için daha fazla yardıma ihtiyacınız varsa, sizi yardım istemek için [Bitcoin Discord'u Keşfet] (https://discord.gg/xKKm29XGBb) adresine katılmaya davet ediyorum. Bu Discord'u düzenli olarak ziyaret ediyorum ve eğer bir çözüm bulabilirsem size yardımcı olmaktan memnuniyet duyarım. Diğer bitcoin kullanıcıları da deneyimlerini paylaşabilir ve desteklerini sunabilirler. **Her durumda, kurtarma ifadenizi, yedekleme dosyanızı ve passphrase'nizi gizli tutmanız çok önemlidir**. Bunları kimseyle paylaşmayın, çünkü bu bitcoinlerinizi çalmalarını sağlayabilir.
