---
name: KeePass
description: Yerel bir parola yöneticisi nasıl kurulur?
---
![cover](assets/cover.webp)


Dijital çağda, bankacılık, finansal platformlar, e-postalar, dosya depolama, sağlık, yönetim, sosyal ağlar, video oyunları vb. dahil olmak üzere günlük hayatımızın çeşitli yönlerini kapsayan çok sayıda çevrimiçi hesabı yönetmemiz gerekiyor.


Bu hesapların her birinde kimliğimizi doğrulamak için, bir parola ile birlikte bir tanımlayıcı, genellikle bir e-posta Address kullanırız. Çok sayıda benzersiz parolayı ezberlemenin imkansızlığı karşısında, aynı parolayı tekrar kullanmak veya hatırlamayı kolaylaştırmak için ortak bir tabanı biraz değiştirmek cazip gelebilir. Ancak bu uygulamalar hesaplarınızın güvenliğini ciddi şekilde tehlikeye atar.


Parolalar için uyulması gereken ilk ilke, onları tekrar kullanmamaktır. Her çevrimiçi hesap benzersiz ve tamamen farklı bir parola ile korunmalıdır. Bu önemlidir, çünkü bir saldırgan şifrelerinizden birini ele geçirmeyi başarırsa, tüm hesaplarınıza erişmesini istemezsiniz. Her hesap için benzersiz bir parolaya sahip olmak olası saldırıları izole eder ve kapsamlarını sınırlar. Örneğin, bir video oyun platformu ve e-postanız için aynı şifreyi kullanırsanız ve bu şifre oyun platformuyla ilgili bir kimlik avı sitesi aracılığıyla ele geçirilirse, saldırgan e-postanıza kolayca erişebilir ve diğer tüm çevrimiçi hesaplarınızın kontrolünü ele geçirebilir.


İkinci temel ilke ise parolanın gücüdür. Bir parolanın kaba kuvvetle, yani deneme yanılma yoluyla tahmin edilmesi zorsa güçlü olduğu kabul edilir. Bu, şifrelerinizin mümkün olduğunca rastgele, uzun olması ve çeşitli karakterler (küçük harf, büyük harf, sayılar ve semboller) içermesi gerektiği anlamına gelir.


Bu iki parola güvenliği ilkesini (benzersizlik ve sağlamlık) uygulamak günlük hayatta zor olabilir, çünkü tüm hesaplarımız için benzersiz, rastgele ve güçlü bir parola ezberlemek neredeyse imkansızdır. İşte bu noktada parola yöneticisi devreye giriyor.


Parola yöneticisi güçlü parolalar oluşturup bunları güvenli bir şekilde saklayarak tüm çevrimiçi hesaplarınıza tek tek ezberlemenize gerek kalmadan erişmenizi sağlar. Yalnızca tek bir parolayı, yöneticide kayıtlı tüm parolalarınıza erişmenizi sağlayan ana parolayı hatırlamanız gerekir. Bir parola yöneticisi kullanmak çevrimiçi güvenliğinizi artırır çünkü parolaların tekrar kullanılmasını önler ve sistematik olarak rastgele parolalar oluşturur. Aynı zamanda hassas bilgilerinize erişimi merkezileştirerek hesaplarınızın günlük kullanımını kolaylaştırır.

Bu eğitimde, çevrimiçi güvenliğinizi artırmak için yerel bir parola yöneticisinin nasıl kurulacağını ve kullanılacağını öğreneceğiz. Burada size KeePass'ı tanıtacağım. Ancak, yeni başlayan biriyseniz ve birden fazla cihaz arasında senkronize olabilen bir çevrimiçi parola yöneticisine sahip olmak istiyorsanız, Bitwarden hakkındaki eğitimimizi takip etmenizi öneririm:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Dikkat: Bir parola yöneticisi parolaları saklamak için harikadır, ancak **Bitcoin Wallet'ünüzün Mnemonic cümlesini asla içinde saklamamalısınız!** Unutmayın, bir Mnemonic cümlesi yalnızca bir kağıt parçası veya metal gibi fiziksel bir biçimde kaydedilmelidir.*


---

## KeePass'e Giriş


KeePass, yerel yönetim için ücretsiz ve güvenli bir çözüm isteyenler için mükemmel olan ücretsiz ve açık kaynaklı bir şifre yöneticisidir. Eklentiler eklenmeden İnternet ile iletişim kurmayan, bilgisayarınıza kurulacak bir yazılımdır. Bu, daha önceki bir eğitimde ele aldığımız Bitwarden'den tamamen farklı bir yaklaşımdır. Bitwarden, KeePass'in aksine, birden fazla cihaz arasında senkronizasyona izin verir ve bu nedenle şifrelerinizin çevrimiçi bir sunucuda saklanmasını gerektirir.


KeePass varsayılan olarak Bitwarden gibi tarayıcı uzantılarının kullanımını desteklemez; bu nedenle, şifrelerinizi yazılımdan manuel olarak kopyalayıp yapıştırmanız gerekecektir. Bu bir kısıtlama gibi görünse de, otomatik doldurma kullanmak yerine şifreleri kopyalayıp yapıştırmak çevrimiçi güvenliğiniz için iyi bir uygulamadır.


KeePass, yüksek güvenlik standartlarına bağlı kalırken hem hafif hem de kullanımı kolay olacak şekilde tasarlanmıştır. Yazılım, kimlik bilgilerinizin en iyi şekilde korunması için veritabanınızı yerel olarak şifreler. KeePass aynı zamanda ANSSI (Fransız siber güvenlik otoritesi) tarafından onaylanmış tek şifre yöneticisidir.


KeePass'ın en önemli avantajlarından biri esnekliğidir. Bilgisayara kurulum gerektirmeden USB bellek gibi birçok farklı şekilde kullanılabilir. Dahası, [eklenti ortamı] (https://keepass.info/plugins.html) sayesinde KeePass daha özel ihtiyaçları karşılamak için özelleştirilebilir.

![KEEPASS](assets/notext/01.webp)

## KeePass Nasıl İndirilir?


KeePass için kurulum süreci kullandığınız işletim sistemine bağlı olarak değişir. Windows veya Linux kullanıcıları için kurulum nispeten basittir. Ancak, macOS kullanıyorsanız, KeePass'ın macOS tarafından doğrudan desteklenmeyen .NET platformu üzerinde geliştirilmesi nedeniyle ek bir adım gereklidir. Bu nedenle, KeePass'in Apple cihazlarında çalışmasına izin vermek için uyumlu bir ortam yapılandırmanız gerekecektir.


Debian/Ubuntu kullanıcıları için terminali açın ve aşağıdaki komutları girin:


```bash
sudo apt-get güncellemesi

sudo apt-get install keepass2

```

For Fedora:

```

sudo dnf install keepass

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```