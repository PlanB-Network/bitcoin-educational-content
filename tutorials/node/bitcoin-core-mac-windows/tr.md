---
name: Bitcoin core (macOS ve Windows)
description: Bitcoin core'i Mac veya Windows'a yükleyin
---

Bitcoin core'yi normal bilgisayarınıza yüklemek mümkündür, ancak ideal değildir. Eğer bilgisayarınızı 7/24 açık bırakmaktan çekinmiyorsanız, bu işinizi görecektir. Bilgisayarı kapatmanız gerekiyorsa, her açtığınızda yazılımın senkronize olmasını beklemek can sıkıcı olur.


Bu talimatlar Mac veya Windows Kullanıcıları içindir. Linux kullanıcılarının büyük olasılıkla benim yardımıma ihtiyacı olmayacak, ancak Linux için talimatlar Mac'e çok benziyor.


## Temiz Başlayın


İdeal olarak, kötü amaçlı yazılım içermeyen temiz bir bilgisayar kullanmak istersiniz. Bir Hardware Wallet kullansanız bile, kötü amaçlı yazılımlar sizi kandırarak paralarınızı çalabilir.


Eski bir bilgisayarı silerek temizleyebilir ve özel bir Bitcoin bilgisayarı olarak kullanabilir ya da özel bir bilgisayar/dizüstü bilgisayar satın alabilirsiniz.


## Hard Sürücüsü


Bitcoin core sürücünüzde yaklaşık 400 gigabayt veri kaplayacak ve büyümeye devam edecektir. Dahili sürücünüzü kullanabilirsiniz, ancak harici bir Hard sürücüsü de takabilirsiniz. Her iki seçeneği de açıklayacağım. İdeal olarak bir katı hal sürücüsü kullanmalısınız. Eski bir bilgisayarınız varsa, muhtemelen dahili olarak bunlardan birine sahip değildir. Sadece 1 ya da 2 terabaytlık bir harici SSD satın alın ve bunu kullanın. Normal sürücü muhtemelen işe yarayacaktır, ancak sorunlar yaşayabilirsiniz ve çok daha yavaş olacaktır.


![image](assets/1.webp)


## Bitcoin core'i İndirin


Bitcoin.org'a gidin (Roger Ver'in sahibi olduğu ve insanları Bitcoin yerine Bitcoin Cash satın almaları için kandıran bir shitcoin sitesi olan Bitcoin.com'a gitmediğinizden emin olun)


Oraya vardığınızda, yazılımı nereden alacağınız garip bir şekilde açık değildir. Kaynaklar menüsüne gidin ve aşağıda gösterildiği gibi "Bitcoin core "a tıklayın:


![image](assets/2.webp)


Bu sizi indirme sayfasına götürecektir:


![image](assets/3.webp)


Bitcoin core'i İndir turuncu düğmesine tıklayın:


![image](assets/4.webp)


Bilgisayarınıza bağlı olarak aralarından seçim yapabileceğiniz birkaç seçenek vardır. İlk ikisi bu kılavuzla ilgilidir; sol çubuktan Windows veya Mac'i seçin. Tıkladıktan sonra büyük olasılıkla İndirilenler dizininize indirilmeye başlayacaktır.


## İndirmeyi doğrulayın (bölüm 1)


Çeşitli sürümlerin hash'lerini içeren dosyaya ihtiyacınız var. Bu dosya eskiden Bitcoin.org'un indirmeler sayfasındaydı, ancak şimdi bitcoincore.org/tr/download adresine taşındı:


![image](assets/5.webp)


SHA256 ikili karma dosyasına ihtiyacınız var. Bu dosya, Bitcoin core'ün çeşitli indirme paketlerinin SHA256 karmalarını içerir.


Daha sonra, Bitcoin core indirmesini Hash yapmamız ve dosyanın Hash'in ne olması gerektiğini söylediği ile karşılaştırmamız gerekir. O zaman bitcoincore.org'a göre indirmenin beklenenle aynı olduğunu biliriz.


İndirilenler dizinine tekrar gidin ve bu komutu çalıştırın (X'leri tam olarak Full node Bitcoin indirme dosyası adıyla değiştirin):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Bir Hash çıktısı alacaksınız. Bunu not edin ve SHA256SUMS dosyasında bulunan Hash ile karşılaştırın.


Çıktılar aynıysa, hiçbir veri parçasıyla oynanmadığını doğrulamış olursunuz... neredeyse. SHA256SUMS dosyasının kötü niyetli olmadığından hala emin olmamız gerekiyor.


Bir sonraki adıma geçmek için bilgisayarımızda gpg kurulu olmalıdır.


Bunu yapmak için SHA256/gpg kılavuzuma bakın ve "gpg indir" bölümünün yarısına kadar kaydırın ve işletim sisteminizin alt başlığını arayın. Sonra buraya geri gelin.


## Açık Anahtarı Alın


İndirme sayfasına geri dönün, SHA256 Hash imzaları dosyasını alın


![image](assets/6.webp)


Tıklayın ve dosyayı diske, tercihen İndirilenler dizinine kaydedin.


Bu dosya, SHA256SUMS dosyasının çeşitli kişiler tarafından imzalarını içerir.


Baş geliştirici Wladimir J. van der Laan'ın açık anahtarının bilgisayarımızın anahtarlığında olmasını istiyoruz. Açık anahtar kimliği şudur:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Bu metni aşağıdaki komuta kopyalayın:


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


İlginçtir ki, istediğiniz zaman bu komutla bilgisayarın anahtarlığında hangi anahtarların olduğunu görebilirsiniz:


```bash
gpg --list-keys
```


## İndirmeyi doğrulayın (bölüm 2)


Açık anahtar elimizde olduğundan, artık Bitcoin core indirmesinin karmalarını ve bu karmaların imzasını içeren SHA256SUMS dosyasını doğrulayabiliriz.


Terminal veya CMD'yi tekrar açın ve İndirilenler dizininde olduğunuzdan emin olun. Oradan, bu komutu çalıştırın:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Listelenen ilk dosya imza dosyasının tam yazılışıdır. Listelenen ikinci dosya, hash'leri içeren metin dosyasının tam yazılışı olmalıdır. Her iki dosya da aynı dizinde olmalıdır ve dosyaların bulunduğu dizinde olmanız gerekir, aksi takdirde her dosya için tam yolu yazmanız gerekir.


Bu, almanız gereken çıktıdır


![image](assets/7.webp)


UYARI mesajını görmezden gelebilirsiniz - bu sadece size Wladimir ile bir anahtar bölümünde tanışmadığınızı ve ona kişisel olarak açık anahtarının ne olduğunu sormadığınızı ve ardından bilgisayarınıza bu anahtara tamamen güvenmesini söylemediğinizi hatırlatır.


Bu mesajı aldıysanız, SHA256SUMS.asc dosyasının Wladimir tarafından imzalandıktan sonra değiştirilmediğini artık biliyorsunuz.


## Bitcoin core'i kurun


Programın nasıl kurulacağına ilişkin ayrıntılı talimatlara ihtiyacınız olmamalıdır.


![image](assets/8.webp)


## Bitcoin core'yi çalıştırın


Mac'te bir uyarı alabilirsiniz (Apple hala Bitcoin karşıtıdır)


![image](assets/9.webp)


Tamam'a tıklayın ve ardından Sistem Tercihlerinizi açın


![image](assets/10.webp)


Güvenlik ve Gizlilik Simgesine tıklayın:


![image](assets/11.webp)


Ardından "yine de aç" seçeneğine tıklayın:


![image](assets/12.webp)


Hata tekrar görünecek, ancak bu sefer bir AÇ düğmesi mevcut olacak. Ona tıklayın.


![image](assets/13.webp)


Bitcoin core yüklenmeli ve size bazı seçenekler sunulmalıdır:


![image](assets/14.webp)


Burada, Blockchain'nın indirileceği yer için varsayılan yolu kullanmayı seçebilir veya harici sürücünüzü seçebilirsiniz. Dahili sürücüyü kullanacaksanız varsayılan yolu değiştirmemenizi öneririm, Bitcoin core ile iletişim kurmak için başka yazılımlar yüklediğinizde işleri kolaylaştırır.


Bir pruned düğümü çalıştırmayı seçebilirsiniz, bu yer tasarrufu sağlar, ancak düğümünüzle yapabileceklerinizi sınırlar. Her iki durumda da, Blockchain'nin tamamını indirecek ve doğrulayacaksınız, bu nedenle alanınız varsa, indirdiklerinizi saklayın ve kaçınabiliyorsanız budama yapmayın.


Onayladığınızda, Blockchain indirilmeye başlayacaktır. Bu birkaç gün sürecektir.


![image](assets/15.webp)


İsterseniz bilgisayarı kapatıp tekrar indirebilirsiniz, herhangi bir zarar vermez.