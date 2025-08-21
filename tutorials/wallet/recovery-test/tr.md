---
name: Kurtarma Testi
description: Bitcoinlerinizi kaybetmediğinizden emin olmak için yedeklerinizi nasıl test edebilirsiniz?
---
![cover](assets/cover.webp)


Bir Bitcoin Wallet oluştururken, genellikle 12 veya 24 kelimeden oluşan bir Mnemonic ifadesini not etmeniz istenir. Bu ifade, Wallet'nizi barındıran cihazın kaybolması, hasar görmesi veya çalınması durumunda bitcoinlerinize yeniden erişmenizi sağlar. Yeni Bitcoin Wallet'nizi kullanmaya başlamadan önce, bu Mnemonic ifadesinin geçerliliğini doğrulamanız çok önemlidir. Bunu yapmanın en iyi yolu, bir kuru çalıştırma kurtarma testi gerçekleştirmektir.


Bu test, içine herhangi bir bitcoin yatırmadan önce bir Wallet restorasyonunun simülasyonunu içerir. Wallet boş olduğu sürece, anahtarlarımızı barındıran cihazın kaybolduğu bir durumu simüle ederiz ve bitcoinlerimizi kurtarmayı denemek için elimizde kalan tek şey Mnemonic cümlemizdir.


![RECOVERY TEST](assets/notext/01.webp)


## Amaç nedir?


Bu test süreci, ister kağıt ister metal üzerinde olsun, Mnemonic ifadenizin fiziksel yedeğinin işlevsel olduğunu doğrulamanızı sağlar. Bu kurtarma testi sırasındaki bir başarısızlık, ifadenin yedeklenmesinde bir hata olduğunu gösterir ve böylece bitcoinlerinizi riske atar. Öte yandan, test başarılı olursa, Mnemonic ifadenizin tamamen çalışır durumda olduğu doğrulanır ve bu Wallet'yı kullanarak bitcoinleri gönül rahatlığıyla güvence altına alabilirsiniz.


Kuru çalıştırma kurtarma testi yapmanın ikili bir avantajı vardır. Sadece Mnemonic ifadenizin doğruluğunu kontrol etmenize izin vermekle kalmaz, aynı zamanda size Wallet kurtarma sürecine aşina olma fırsatı da verir. Bu şekilde, gerçek bir durumla karşılaşmadan önce olası zorlukları keşfedebilirsiniz. Wallet'inizi gerçekten kurtarmanız gereken gün, süreci zaten bildiğiniz için daha az stresli olacaksınız ve hata riskini azaltacaksınız. Bu nedenle bu test adımını ihmal etmemek ve doğru şekilde yapmak için gerekli zamanı ayırmak önemlidir.


## Kurtarma testi nedir?


Test süreci oldukça basittir:


- Yeni Bitcoin Wallet'inizi oluşturduktan sonra ve ilk satoshilerinizi yatırmadan önce, bir xpub, ilk alıcı Address veya hatta ana anahtar parmak izi gibi bir tanık bilgisini not edin;
- Ardından, örneğin Hardware Wallet'nizi fabrika ayarlarına sıfırlayarak, hala boş olan Wallet'ü kasıtlı olarak silin;
- Ardından, yalnızca Mnemonic ifadenizin ve kullanıyorsanız passphrase'ünüzün kağıt yedeklerini kullanarak Wallet'nızın kurtarılmasını simüle edin;
- Son olarak, tanık bilgilerinin yenilenen Wallet'ninkiyle eşleşip eşleşmediğini kontrol edin. Bilgiler eşleşirse, fiziksel yedeklemenizin güvenilirliğinden emin olabilir ve ilk bitcoinlerinizi bu Wallet'ye gönderebilirsiniz.

Kurtarma testi sırasında, Wallet'unuzun saldırı yüzeyini artırmamak için **nihai Wallet'unuz için tasarlanan aynı cihazı kullanmalısınız**. Örneğin, bir Trezor Safe 5 üzerinde bir Wallet oluşturursanız, kurtarma testini aynı Trezor Safe 5 üzerinde gerçekleştirdiğinizden emin olun. Kurtarma ifadenizi başka bir yazılıma girmemeniz önemlidir, çünkü bu, Wallet hala boş olsa bile Hardware Wallet'iniz tarafından sağlanan güvenliği tehlikeye atacaktır.


## Kurtarma testi nasıl gerçekleştirilir?


Bu eğitimde, Sparrow wallet (Hot Wallet için) kullanarak bir Bitcoin Software Wallet üzerinde kurtarma testinin nasıl gerçekleştirileceğini açıklayacağım. Ancak, süreç diğer tüm cihaz türleri için aynı kalır. Yine, **eğer bir Hardware Wallet kullanıyorsanız, kurtarma testini Sparrow wallet** üzerinde gerçekleştirmeyin (önceki bölüme bakın).


Sparrow wallet üzerinde yeni bir Hot Wallet oluşturdum. Şu anda ona henüz hiç bitcoin göndermedim. Boş.


![RECOVERY TEST](assets/notext/02.webp)


12 kelimelik KİS-30 cümlemi bir kağıda dikkatlice not ettim. Ve bu Wallet'in güvenliğini artırmak istediğim için, başka bir kağıda kaydettiğim bir BIP39 passphrase da oluşturdum:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***Açıkçası, bu eğitimde yaptığımın aksine, Mnemonic ifadenizi ve passphrase'nizi asla internette paylaşmamalısınız. Bu örnek Wallet kullanılmayacak ve eğitimin sonunda silinecektir.***


Şimdi Wallet'mdan bir tanık bilgi parçasını bir taslak üzerine not edeceğim. İlk alıcı Address, xpub veya ana anahtar parmak izi gibi farklı bilgi parçaları seçebilirsiniz. Şahsen ben ilk alıcı Address'i seçmenizi öneririm. Bu, bu Address'e giden ilk türetme yolunun tamamını bulabildiğinizi doğrulamanızı sağlar.


Sparrow'de "*Adresler*" sekmesine tıklayın.


![RECOVERY TEST](assets/notext/03.webp)


Ardından, Wallet'unuzun ilk alıcı Address'ini bir kağıda not edin. Benim örneğimde, Address şudur:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


Bilgileri not ettikten sonra, "*Dosya*" menüsüne gidin ve ardından "*Wallet* Sil "i seçin. Bu işleme devam etmeden önce Bitcoin Wallet'inizin boş olması gerektiğini bir kez daha hatırlatırım.


![RECOVERY TEST](assets/notext/04.webp)


Wallet'niz gerçekten boşsa, Wallet'nizin silindiğini onaylayın.


![RECOVERY TEST](assets/notext/05.webp)


Şimdi Wallet oluşturma işlemini tekrarlamanız gerekiyor, ancak kağıt yedeklerimizi kullanarak. "*Dosya*" menüsüne ve ardından "*Yeni Wallet*" seçeneğine tıklayın.


![RECOVERY TEST](assets/notext/06.webp)


Wallet'ünüzün adını tekrar girin.


![RECOVERY TEST](assets/notext/07.webp)


"*Script Type*" menüsünde, daha önce sildiğiniz Wallet ile aynı script türünü seçmeniz gerekir.


![RECOVERY TEST](assets/notext/08.webp)


Ardından "*Yeni veya İçe Aktarılan Software Wallet*" düğmesine tıklayın.


![RECOVERY TEST](assets/notext/09.webp)


seed'niz için doğru kelime sayısını seçin.


![RECOVERY TEST](assets/notext/10.webp)


Mnemonic ifadenizi yazılıma girin. "*Geçersiz Checksum*" mesajı görüntülenirse, bu Mnemonic ifadenizin yedeğinin yanlış olduğunu gösterir. Kurtarma testiniz başarısız olduğu için Wallet'unuzu oluşturmaya sıfırdan başlamanız gerekecektir.


![RECOVERY TEST](assets/notext/11.webp)


Benim durumumda olduğu gibi bir passphrase'niz varsa, onu da girin.


![RECOVERY TEST](assets/notext/12.webp)


"*Anahtar Deposu Oluştur*" ve ardından "*Anahtar Deposunu Aktar*" üzerine tıklayın.


![RECOVERY TEST](assets/notext/13.webp)


Ve son olarak, "*Uygula*" düğmesine tıklayın.


![RECOVERY TEST](assets/notext/14.webp)


Artık "*Adresler*" sekmesine geri dönebilirsiniz.


![RECOVERY TEST](assets/notext/15.webp)


Son olarak, ilk gelen Address'in taslağınızda tanık olarak belirttiğiniz kişiyle eşleştiğini doğrulayın.


![RECOVERY TEST](assets/notext/16.webp)


Alıcı adresleri eşleşirse, kurtarma testiniz başarılıdır ve yeni Bitcoin Wallet'inizi kullanabilirsiniz. Eşleşmezlerse, bu ya türetme yolunu yanlış yapan komut dosyası türü seçiminde bir hata olduğunu ya da Mnemonic ifadenizin veya passphrase'nizin yedeklemesinde bir sorun olduğunu gösterebilir. Her iki durumda da, herhangi bir riskten kaçınmak için sıfırdan başlamanızı ve en baştan yeni bir Bitcoin Wallet oluşturmanızı şiddetle tavsiye ederim. Bu kez, Mnemonic ifadesini hatasız olarak not etmeye özen gösterin.

Tebrikler, artık bir kurtarma testi gerçekleştirmeye hazırsınız! Tüm Bitcoin cüzdanlarınızın oluşturulması için bu süreci genelleştirmenizi tavsiye ederim. Bu eğitimi faydalı bulduysanız, aşağıya bir beğeni bırakırsanız çok memnun olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!