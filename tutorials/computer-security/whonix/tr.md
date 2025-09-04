---
name: Whonix
description: Gizliliğinizi ve mahremiyetinizi koruyun.
---

![cover](assets/cover.webp)



**Whonix**, **güvenlik**, **anonimlik** ve **gizliliği** birleştiren bir ortam sağlamak için tasarlanmış **Debian** tabanlı bir Linux dağıtımıdır. Öğrenmesi kolay ve farklı arayüzlerle uyumludur (sanal makineler, Qubes OS, Canlı mod), varsayılan olarak **Tor** üzerinden ağ trafiği yönlendirmesi, **çift güvenlik duvarı** (bir güvenlik duvarı Ağ Geçidinde ve diğeri İş İstasyonunda), **IP/DNS sızıntılarına karşı tam koruma** ve etkinliğinizi İSS'niz de dahil olmak üzere ağ gözlemcilerinden etkili bir şekilde maskelemek için araçlar içerir. Anonim bir sistemden daha fazlası olan **Whonix** eksiksiz bir güvenli geliştirme ortamıdır.



## Neden Whonix'i seçmelisiniz?





- Ücretsiz**: Çoğu Linux dağıtımı gibi Whonix de tamamen ücretsiz olarak lisanslanmış açık kaynaklı bir sistemdir. Aktif ve şeffaf bir topluluk ile açık kaynak kodlu olarak geliştirilmiştir.
- Gizlilik, güvenlik ve anonimlik**: Whonix'in ana hedefi, tüm verilerinizin korunduğu ve iletişiminizin Tor ağı üzerinden şifrelendiği ultra güvenli bir ortam sunmaktır.
- Kolay kullanım**: Whonix, acemi kullanıcılar için bile uygun, sezgisel, önceden yapılandırılmış bir grafik Interface sunar. Gelişmiş korumadan faydalanmak için uzman olmanıza gerek yok.
- Güvenli geliştirme için ideal ortam**: Whonix, gerçek IP Address'inizi asla açığa çıkarmadan veya tarama veya ağ iletişim alışkanlıklarınızı ifşa etmeden programlar geliştirmenize, test etmenize, denetlemenize veya çalıştırmanıza olanak tanır.
- Tek kullanımlık oturumlar ve Canlı mod**: Whonix, Canlı modda veya tek kullanımlık makineler aracılığıyla (örneğin **Qubes OS** aracılığıyla) başlatılabilir ve oturum sona erdiğinde kalıcı izler bırakmadan kritik görevlerin gerçekleştirilmesini sağlar.
- Nispeten basit kurulum**: Sanal makinelere (VirtualBox, KVM, Qubes) hızlı kurulum için kullanıma hazır görüntüler sağlanır. Sistem belgelenmiştir ve düzenli olarak güncellenmektedir.



## Kurulum ve yapılandırma



Whonix kurulumuna geçmeden önce, bu dağıtımın doğrudan Hard diskine (çıplak metal modunda) kurulabilen bir ana sistem olarak **henüz resmi olarak mevcut olmadığını** belirtmek önemlidir. Başka bir deyişle, Whonix'i henüz Ubuntu veya standart Debian gibi klasik bir ana işletim sistemi** olarak kuramazsınız.



Bununla birlikte, Whonix'in **volatile** (Canlı mod, geçici oturumlar) veya **persistent** (sanal makineler veya Qubes OS'ye entegrasyon yoluyla) kullanılmasına izin veren çeşitli sürümler mevcuttur.



Uzun süreli, istikrarlı kullanım için **sanallaştırma şu anda resmi olarak önerilen tek yöntemdir**. Whonix'i **VirtualBox** (Whonix-Gateway ve Whonix-Workstation) kullanarak çalıştırabilir veya **Qubes OS** gibi bir sisteme entegre edebilirsiniz. Bu eğitimde, VirtualBox kurulumuna odaklanacağız.



### Ön Koşullar



Whonix'i sanal modda kurmadan önce, makinenizin minimum teknik gereksinimleri karşıladığından emin olun. Sanallaştırma, tüm bilgisayarların sunamayacağı belirli kaynaklar gerektirir. Bu nedenle işlemcinizin sanallaştırma teknolojisini (Intel VT-x veya AMD-V) desteklemesi ve bu seçeneğin BIOS/UEFI'de etkinleştirilmiş olması çok önemlidir.



İşte Whonix ile sorunsuz ve istikrarlı bir deneyim için önerilen özellikler:





- Rastgele Erişimli Bellek (RAM)**: en az **8 GB** şiddetle tavsiye edilir. Ne kadar fazla RAM'e sahip olursanız, sanal makinelere (Ağ Geçidi ve İş İstasyonu) o kadar fazla kaynak ayırabilir ve performansı artırabilirsiniz.
- Kullanılabilir disk alanı**: lütfen en az 30 GB boş disk alanı bırakın**. Bu, iki sanal makine, sistem dosyaları ve tüm veriler veya anlık görüntüler için gereken alanı içerir.
- İşlemci**: özellikle diğer hizmetleri veya araçları paralel olarak çalıştırmak istiyorsanız, en az **4 fiziksel çekirdeğe** (8 mantıksal iş parçacığı) sahip bir işlemci önerilir.



### Whonix'i İndirin



Whonix, kullanmak istediğiniz ortamın türüne bağlı olarak çeşitli sürümlerde mevcuttur. Çoğu kullanıcı için (Windows, Linux veya MacOs), VirtualBox sürümü kurulumu en kolay olanıdır. Görüntüyü doğrudan [resmi web sitesinden] (https://www.whonix.org/wiki/VirtualBox) indirebilirsiniz.



⚠️ Whonix, Apple Silicon işlemcileri (ARM mimarisi) kullanan MacBook'lar ile **uyumlu değildir**.



## VirtualBox'ı Yükleme



Whonix'i çalıştırmak için VirtualBox, Qubes veya KVM gibi bir **hipervizöre** ihtiyacınız olacaktır.



Dosyayı indirdikten sonra, diğer yazılımları yüklediğiniz gibi yükleyin. Özel gereksinimleriniz olmadığı sürece varsayılan seçenekleri kabul edin. Aklınız mı karıştı? VirtualBox kullanma kılavuzumuza göz atın.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Whonix'i içe aktarma



VirtualBox kurulduktan sonra, daha önce indirdiğiniz Whonix `.ova` dosyalarını (`Whonix-Gateway-Xfce.ova` ve `Whonix-Workstation-Xfce.ova`) içe aktarabilirsiniz.



VirtualBox'ı açın, ardından **Dosya → Cihazı içe aktar** seçeneğine tıklayın.


İlgili `.ova` dosyasını seçin (Ağ Geçidi ile başlayın).



![0_03](assets/fr/03.webp)



Whonix sanal makine dosyalarının depolanacağı konumu seçin.



![0_04](assets/fr/04.webp)



Kullanım koşullarını kabul edin, ardından içe aktarmayı başlatın ve işlemin bitmesini bekleyin.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix yapılandırması



Whonix'i başlatmadan önce, daha iyi performans sağlamak için bazı **sistem ayarlarını** yapmak önemlidir:



Whonix-Workstation-Xfce** sanal makinesini seçin ve ardından **Configuration** (Yapılandırma) üzerine tıklayın.



![0_06](assets/fr/07.webp)



Varsayılan RAM tahsisinin 2048 MB olduğu **Sistem** sekmesine gidin. Özellikle birden fazla uygulama açmayı ya da uzun oturumlarda çalışmayı düşünüyorsanız, daha fazla akıcılık için **4096 MB'a (4 GB)** çıkarmanızı öneririz. Çok sayıda Tor bağlantısını paralel olarak kullanmadığınız sürece Ağ Geçidi 2048 MB olarak kalabilir.



![0_08](assets/fr/08.webp)



### Whonix ile çalışmaya başlama



Whonix'in düzgün ve güvenli bir şekilde çalışması için **bu başlatma sırasını** izlemelisiniz:



İlk olarak, **Whonix-Gateway-Xfce** makinesini başlatın. Bu makine tüm trafiği **Tor** ağı üzerinden yönlendirmekten sorumludur. Ağ geçidi çalışmazsa, Tor üzerinden hiçbir trafik yönlendirilmez ve anonimliğinizi kaybedersiniz.



![0_09](assets/fr/09.webp)



Ağ Geçidi tamamen başlatıldıktan sonra (Tor'un bağlı olduğunu göreceksiniz), Ağ Geçidi üzerinden otomatik olarak bağlanacak olan **Whonix-Workstation-Xfce** programını başlatabilirsiniz.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Sistem güncellemesi



Terminale girin, paket listesini güncellemek için aşağıdaki komutu girin:



```shell
sudo apt update
```



Ardından mevcut güncellemeleri yüklemek için aşağıdaki komutu çalıştırın:



```shell
sudo apt full-upgrade
```



## Whonix'i Keşfedin



**Whonix**, kimliğinizi veya verilerinizi tehlikeye atmadan internette gezinmek için ideal olan **güvenli**, **anonim** ve **gizli** bir bilgisayar ortamı sağlamak üzere tasarlanmış bir sistemdir. Bunu başarmak için, dijital güvenliğinizi en başından itibaren güçlendirmek üzere tasarlanmış bir dizi yararlı günlük uygulama ile birlikte gelir.


### KeepassXC



**KeePassXC** Whonix'in entegre şifre yöneticisidir. Şifrelerinizi manuel olarak hatırlamak zorunda kalmadan güvenli bir şekilde **oluşturmanızı, saklamanızı ve yönetmenizi** sağlar. Parolalar, bir ana parola ile korunan **şifreli bir veritabanında** saklanır.



### Tor Tarayıcı



**Tor Browser** Whonix'in varsayılan web tarayıcısıdır. Trafiğinizi dünyanın dört bir yanındaki çeşitli aktarıcılar aracılığıyla yönlendiren ve gerçek IP Address'ünüzü tanımlamayı neredeyse imkansız hale getiren **Tor** ağına dayanır.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Elektrum Bitcoin Wallet



**Electrum**, **kripto para birimi işlemlerini** anonim olarak yönetmenize izin vermek için Whonix'e önceden yüklenmiş hafif ve hızlı bir Bitcoin Wallet'dir. Tüm Blockchain'yı indirmez, ancak gerekli bilgileri elde etmek için uzak sunucuları kullanır, bu da onu tam bir Wallet'den çok daha hafif hale getirir.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix bir işletim sisteminden daha fazlasıdır: anonimliğinizi, gizliliğinizi ve hassas faaliyetlerinizi korumak için tasarlanmış gerçek bir **güvenli ortamdır**. Tor tabanlı mimarisi, Ağ Geçidi ve İş İstasyonu arasındaki akıllı bölümleme ve Tor Browser, KeePassXC ve Electrum gibi önceden yüklenmiş araçlar sayesinde, **anonim olarak gezinmek**, **güvenli çalışmak** veya **gizli verileri işlemek** isteyen herkes için anahtar teslimi bir çözüm sunar.



Unix sisteminizde güvenliğinizi güçlendirmek için makinenizi denetleme eğitimimize bir göz atın: işletim sisteminizdeki güvenlik açıklarını kontrol edin ve verilerinizin tehlikeye atılmadığından emin olun.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af