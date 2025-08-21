---
name: GnuPG
description: Yazılımın bütünlüğü ve gerçekliği nasıl doğrulanır?
---
![cover](assets/cover.webp)


Yazılım indirirken, değiştirilmediğinden ve gerçekten resmi kaynaktan geldiğinden emin olmak çok önemlidir. Bu, özellikle fonlarınıza erişim sağlayan anahtarları güvence altına almanızı sağlayan Wallet yazılımı gibi Bitcoin ile ilgili yazılımlar için geçerlidir. Bu eğitimde, yazılımı yüklemeden önce bütünlüğünü ve gerçekliğini nasıl doğrulayacağımızı göreceğiz. Bitcoin kullanıcıları arasında favori bir Wallet yazılımı olan Sparrow wallet'ı örnek olarak kullanacağız, ancak prosedür diğer tüm yazılımlar için aynı olacaktır.


Bütünlüğün doğrulanması, indirilen dosyanın dijital parmak izini (yani Hash) resmi geliştirici tarafından sağlananla karşılaştırarak değiştirilmediğinden emin olmayı içerir. İkisi eşleşirse, dosyanın orijinaliyle aynı olduğu ve bir saldırgan tarafından bozulmadığı veya değiştirilmediği anlamına gelir.


Diğer yandan, özgünlüğün doğrulanması, dosyanın gerçekten resmi geliştiriciden geldiğini ve bir sahtekar olmadığını garanti eder. Bu, dijital imzayı doğrulayarak yapılır. Bu imza, yazılımın meşru geliştiricinin özel anahtarıyla imzalandığını kanıtlar.


Bu kontroller yapılmazsa, değiştirilmiş kod içerebilecek kötü amaçlı yazılım yükleme riski vardır. Bu kod özel anahtarlarınız gibi bilgileri çalabilir ya da dosyalarınıza erişimi engelleyebilir. Bu tür saldırılar, özellikle sahte sürümlerin dağıtılabildiği açık kaynaklı yazılımlar bağlamında oldukça yaygındır.


Bu doğrulamayı gerçekleştirmek için iki araç kullanacağız: bütünlüğü doğrulamak için hashing fonksiyonları ve gerçekliği doğrulamak için PGP protokolünü uygulayan açık kaynaklı bir araç olan GnuPG.


## Ön Koşullar


Eğer **Linux** kullanıyorsanız, GPG çoğu dağıtımda önceden yüklenmiştir. Değilse, aşağıdaki komutla yükleyebilirsiniz:


```bash
sudo apt install gnupg
```


MacOS** için, Homebrew paket yöneticisini henüz yüklemediyseniz, aşağıdaki komutları kullanarak yükleyin:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Ardından bu komutla GPG'yi yükleyin:


```bash
brew install gnupg
```

Windows** için, eğer GPG'niz yoksa, [Gpg4win](https://www.gpg4win.org/) yazılımını yükleyebilirsiniz.

![GnuPG](assets/notext/01.webp)


## Belgeleri İndirme


Başlamak için çeşitli belgelere ihtiyacımız olacak. "*Download*" bölümündeki] [Sparrow wallet'ün resmi sitesini ziyaret edin (https://sparrowwallet.com/download/). Başka bir yazılımı doğrulamak istiyorsanız, o yazılımın web sitesine gidin.


![GnuPG](assets/notext/02.webp)


Ayrıca [projenin GitHub deposuna] (https://github.com/sparrowwallet/Sparrow/releases) da gidebilirsiniz.


![GnuPG](assets/notext/03.webp)


İşletim sisteminize karşılık gelen yazılımın yükleyicisini indirin.


![GnuPG](assets/notext/04.webp)


Ayrıca dosyanın genellikle "*SHA256SUMS*" veya "*MANIFEST*" olarak adlandırılan Hash'sına da ihtiyacınız olacaktır.


![GnuPG](assets/notext/05.webp)


Dosyanın PGP imzasını da indirin. Bu belge `.asc` formatındadır.


![GnuPG](assets/notext/06.webp)


Aşağıdaki adımlar için tüm bu dosyaları aynı klasöre yerleştirdiğinizden emin olun.


Son olarak, PGP imzasını doğrulamak için kullanacağımız geliştiricinin açık anahtarına ihtiyacınız olacak. Bu anahtar genellikle yazılımın web sitesinde, projenin GitHub deposunda, bazen geliştiricinin sosyal medyasında veya Keybase gibi özel sitelerde bulunur. Sparrow wallet örneğinde, geliştirici Craig Raw'ın açık anahtarını [Keybase'de] bulabilirsiniz (https://keybase.io/craigraw). Doğrudan terminalden indirmek için şu komutu çalıştırın:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## İmzanın Doğrulanması


İmzayı doğrulama işlemi **Windows**, **macOS** ve **Linux** üzerinde aynıdır. Normalde, bir önceki adımda açık anahtarı zaten içe aktarmışsınızdır, ancak aktarmadıysanız, bunu şu komutla yapın:


```bash
gpg --import [key path]
```


Geliştiricinin açık anahtar dosyasının konumunu `[anahtar yolu]` ile değiştirin.


![GnuPG](assets/notext/08.webp)


İmzayı aşağıdaki komutla doğrulayın:


```bash
gpg --verify [file.asc]
```


İmza dosyasının yolunu `[file.asc]` ile değiştirin. Sparrow durumunda, bu dosya 2.0.0 sürümü için "*Sparrow-2.0.0-manifest.txt.asc*" olarak adlandırılır.


![GnuPG](assets/notext/09.webp)


İmza geçerliyse, GPG bunu size gösterecektir. Daha sonra dosyanın gerçekliğini onayladığı için bir sonraki adıma geçebilirsiniz.


![GnuPG](assets/notext/10.webp)


## Hash'un Doğrulanması

Yazılımın gerçekliği doğrulandığına göre, bütünlüğünü de doğrulamak gerekir. Yazılımın Hash'unu geliştirici tarafından sağlanan Hash ile karşılaştıracağız. İkisi eşleşirse, yazılım kodunun değiştirilmediğini garanti eder.


Windows** üzerinde bir terminal açın ve aşağıdaki komutu çalıştırın:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Yükleyicinin konumunu `[dosya yolu]` ile değiştirin.


![GnuPG](assets/notext/11.webp)


Terminal, indirilen yazılımın Hash'ini döndürecektir.


![GnuPG](assets/notext/12.webp)


Bazı yazılımlar için SHA256'dan farklı bir Hash işlevi kullanmak gerekebileceğini unutmayın. Bu durumda, komutta Hash işlevinin adını değiştirmeniz yeterlidir.


Ardından sonucu "*Sparrow-2.0.0-manifest.txt*" dosyasındaki ilgili değerle karşılaştırın.


![GnuPG](assets/notext/13.webp)


Benim durumumda, iki karmanın mükemmel bir şekilde eşleştiğini görüyoruz.


MacOS** ve **Linux** üzerinde Hash doğrulama işlemi otomatiktir. Windows'ta olduğu gibi iki karma arasındaki eşleşmeyi manuel olarak kontrol etmek gerekmez.


Bu komutu **macOS** üzerinde çalıştırmanız yeterlidir:


```bash
shasum --check [file name] --ignore-missing
```


Dosya adı]` yerine yükleyicinin adını yazın. Örneğin, Sparrow wallet için:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Karmalar eşleşirse, aşağıdaki çıktıyı görmelisiniz:


```bash
Sparrow-2.0.0.dmg: OK
```


Linux** üzerinde komut benzerdir:


```bash
sha256sum --check [file name] --ignore-missing
```


Karmalar eşleşirse aşağıdaki çıktıyı görmeniz gerekir:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Artık indirdiğiniz yazılımın hem orijinal hem de sağlam olduğundan emin olabilirsiniz. Makinenize yüklemeye devam edebilirsiniz.


Eğer bu yazıyı faydalı bulduysanız, aşağıda beğeninizi belirtmenizden memnuniyet duyarım. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca depolama aygıtlarını şifrelemenize ve şifrelerini çözmenize olanak tanıyan bir yazılım olan VeraCrypt hakkındaki bu diğer eğitime de göz atmanızı tavsiye ederim.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5