---
name: Plan ₿ Network diplomalarının Timestamp'i
description: Plan ₿ Network'nin sertifika ve diplomalarınız için doğrulanabilir kanıtları nasıl düzenlediğini anlayın
---

![cover](assets/cover.webp)


Bu yazıyı okuyorsanız, planb.network'te katıldığınız kurslardan biri için ₿-CERT test sertifikası veya tamamlama diploması almış olma ihtimaliniz yüksektir, bu nedenle bu başarınız için sizi tebrik ederiz!


Bu eğitimde, Plan ₿ Network'ün ₿-CERT test sertifikanız veya Kurs Tamamlama ile ilgili herhangi bir Diploma için doğrulanabilir kanıtları nasıl düzenlediğini keşfedeceğiz. Daha sonra, ikinci bir bölümde bu kanıtların gerçekliğini nasıl doğrulayacağımızı açıklayacağız.


# Plan ₿ Network kanıt mekanizması


Plan ₿ Network'te, sertifikaları ve diplomaları kriptografik olarak imzalıyoruz ve iki kriptografik işleme dayanan bir kanıt mekanizması aracılığıyla Zaman Zincirini (yani Bitcoin Blockchain) kullanarak bunları zaman damgasıyla damgalıyoruz:


1. Başarılarınızı sentezleyen bir metin dosyası üzerinde GPG imzası

2. Aynı imzalı dosyanın [opentimestamps](https://opentimestamps.org/) aracılığıyla zaman damgası.


İlk işlem sertifikayı (veya diplomayı) düzenleyeni onaylamanızı sağlarken, ikinci işlem sertifikanın düzenlenme tarihini doğrulamanıza olanak tanır.

Bu basit kanıt mekanizmasının, herkesin bağımsız olarak doğrulayabileceği inkar edilemez kanıtlarla sertifika ve diploma vermemizi sağladığına inanıyoruz.


![image](./assets/proof-mechanism.webp)


Bu kanıt mekanizması sayesinde, sertifikanızın veya diplomanızın en küçük ayrıntısını bile değiştirmeye yönelik herhangi bir girişim, imzalı dosyanın tamamen farklı bir SHA-256 Hash'u ile sonuçlanacak ve hem imza hem de Timestamp artık geçerli olmayacağından, herhangi bir tahrifatı anında ortaya çıkaracaktır. Dahası, herhangi biri Plan ₿ Network adına kötü niyetle sertifika veya diploma taklit etmeye kalkışırsa, imzanın basit bir şekilde doğrulanması sahtekarlığı ortaya çıkaracaktır.


## GPG-imzası nasıl çalışır?


GPG imzası, GNU Privacy Guard adlı açık kaynaklı bir yazılım kullanılarak oluşturulur. Bu yazılım kullanıcıların kolayca özel anahtarlar oluşturmasına, imzaları imzalamasına ve doğrulamasına ve dosyaları şifrelemesine ve şifrelerini çözmesine olanak tanır. Bu eğitimin amaçları doğrultusunda, Plan ₿ Network'in özel/genel anahtarlarını oluşturmak ve tüm ₿-CERT Sertifikalarını ve Kurs Tamamlama Diplomalarını imzalamak için GPG kullandığını belirtmek önemlidir.


Öte yandan, birisi imzalı bir dosyanın gerçekliğini doğrulamak isterse, dosyayı veren kişinin açık anahtarını almak ve doğrulamak için GPG'yi kullanabilir.


Merak edenler ve bu harika yazılım hakkında daha fazla bilgi edinmek isteyenler için ["The GNU Privacy Handbook"] (https://www.gnupg.org/gph/en/manual/x135.html) adresine başvurabilirsiniz


## Zaman damgası nasıl çalışır?


Herkes OpenTimestamps'ı kullanarak bir dosyayı Timestamp'ye ekleyebilir ve dosyanın varlığına dair doğrulanabilir bir kanıt elde edebilir. Başka bir deyişle, dosyanın ne zaman oluşturulduğuna dair kanıt sağlamaz, daha ziyade dosyanın zaman içinde belirli bir andan daha geç var olmadığına dair kanıt sağlar.

OpenTimestamps, Bitcoin Blockchain'te kanıt depolamak için oldukça verimli bir yöntem kullanarak bu hizmeti ücretsiz olarak sağlar. Dosyanız için benzersiz bir tanımlayıcı oluşturmak için SHA-256 Hash algoritmasını kullanır ve diğer kullanıcılar tarafından gönderilen dosyaların karmalarını kullanarak bir Merkle Tree oluşturur. Merkle Tree yapısının yalnızca Hash'si bir OP_RETURN işlemine bağlanır ve dosya varlığını doğrulamak için güvenli ve kompakt bir yol sağlar.

Bu işlem bir bloğa girdiğinde, ilk dosyaya ve onunla ilişkili `.ots` dosyasına sahip olan herkes zaman damgasının gerçekliğini doğrulayabilir. Eğitimin ikinci bölümünde, OpenTimestamps web sitesinde Bitcoin Sertifikanızı veya herhangi bir Kurs Tamamlama Diplomanızı teminal ve grafiksel bir Interface aracılığıyla nasıl doğrulayacağınızı göreceğiz.


# Plan ₿ Network ₿-CERT sertifikası veya Diploması nasıl doğrulanır?


## 1. Adım Sertifikanızı veya Diplomanızı İndirin


Planb.network adresinden kişisel/öğrenci panonuza giriş yapın.


![image](./assets/login.webp)


Sol taraftaki menüye tıklayarak "Kimlik Bilgileri "ne gidin ve sınav oturumunuzu veya Diplomanızı seçin.


![image](./assets/credential.webp)


Zip dosyasını indirin.


![image](./assets/download.webp)


.zip` dosyasına sağ tıklayıp "Çıkart" seçeneğini seçerek içeriği çıkartın. Üç farklı dosya bulacaksınız:



- İmzalı bir metin dosyası (örn. certificate.txt)
- Bir Açık Timestamp (OTS) dosyası (örn. certificate.txt.ots)
- Bir PDF sertifikası (örn. certificate.pdf)


## Adım 2: Metin Dosyasının İmzasını nasıl doğrulayabilirsiniz?


İlk olarak, dosyaları çıkardığınız klasöre gidin ve bir terminal açın (klasör penceresine sağ tıklayın ve "Teminal'de Aç" seçeneğine tıklayın). Ardından, aşağıdaki talimatları izleyin.


1. Plan ₿ Network genel PGP anahtarını aşağıdaki komutla içe aktarın:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


PGP Anahtarını başarıyla içe aktardıysanız aşağıdaki gibi bir mesaj görmelisiniz


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


NOT: 1 anahtarın işlendiğini ve 0 anahtarın içe aktarıldığını görürseniz, bu muhtemelen aynı anahtarı daha önce içe aktardığınız anlamına gelir, ki bu tamamen normaldir.


2. Aşağıdaki komutu kullanarak sertifika veya diploma imzasını doğrulayın:


```bash
gpg --verify certificate.txt
```


Bu komut size imza hakkında aşağıdakileri de içeren ayrıntıları göstermelidir:



- Kim imzaladı (Plan ₿ Network)
- İmzalandığında
- İmzanın geçerli olup olmadığı


Bu, sonucun bir örneğidir:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


"BAD signature" gibi bir mesaj görürseniz, bu dosyanın tahrif edildiği anlamına gelir.


## Adım 3: Açık Timestamp'ün Doğrulanması


### Grafiksel Interface ile Doğrulama


1. OpenTimestamps web sitesini ziyaret edin: https://opentimestamps.org/

2. "Damga ve Doğrulama" sekmesine tıklayın.

3. OTS dosyasını (örneğin `certificate.txt.ots`) belirlenen alana sürükleyip bırakın.

4. Zaman damgalı dosyayı (örneğin `certificate.txt`) belirlenen alana sürükleyip bırakın.

5. Web sitesi açık Timestamp'yı otomatik olarak doğrulayacak ve sonucu görüntüleyecektir.


Aşağıdaki gibi bir mesaj görürseniz, Timestamp geçerlidir:


![cover](assets/opentimestamp_wegui_verified.webp)


### CLI Yöntemi


NOT: bu prosedür **çalışan bir yerel Bitcoin düğümü gerektirecektir**


1. Aşağıdaki komutu çalıştırarak OpenTimestamps istemcisini resmi [repository](https://github.com/opentimestamps/opentimestamps-client) adresinden yükleyin:


```
pip install opentimestamps-client
```


2. Çıkarılan sertifika dosyalarını içeren dizine gidin.


3. Açık Timestamp'u doğrulamak için aşağıdaki komutu çalıştırın:


```
ots verify certificate.txt.ots
```


Bu komut:



- Timestamp'yi Bitcoin'ün Blockchain'ine göre kontrol edin
- Dosyanın tam olarak ne zaman zaman damgalı olduğunu gösterir
- Timestamp'ün gerçekliğini teyit edin


### Nihai sonuçlar


Aşağıdaki mesajların **her ikisi** de görüntülenirse doğrulama başarılı olur:


1. GPG imzası **"Plan ₿ Network'ten iyi imza "** olarak rapor edilir

2. OpenTimestamps doğrulaması belirli bir Bitcoin bloğu Timestamp'yı gösterir ve **"Başarılı! Bitcoin bloğu [blockheight] verilerin [Timestamp] itibariyle var olduğunu kanıtlıyor "**


Artık Plan ₿ Network'in herhangi bir ₿-CERT Sertifikası ve Diploması için doğrulanabilir kanıtları nasıl yayınladığını bildiğinize göre, bunların bütünlüğünü kolayca doğrulayabilirsiniz.