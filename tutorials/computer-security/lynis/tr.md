---
name: Lynis
description: Lynis ile bir Linux makinesinde güvenlik denetimi gerçekleştirin
---
![cover](assets/cover.webp)



___



*Bu eğitim Fares CHELLOUG tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



**Bu eğitimde, Lynis kullanarak bir Linux makinesinde nasıl güvenlik denetimi yapacağımızı öğreneceğiz! Lynis'i bilmeyenler için,** sunucunuzun yapılandırmasını analiz eden ve makinenizin güvenliğini artırmak için önerilerde bulunan küçük bir komut satırı yardımcı programıdır



Lynis, **sistem denetimi ve sertleştirme** konusunda uzmanlaşmış bir şirket olan CISOFY'nin açık kaynaklı bir aracıdır. Linux ve popüler servisleri (SSH, Apache2, vb.) güçlendirmede ilerleme kaydetmek istiyorsanız, Lynis sizin müttefikinizdir! Lynis size sadece neyin yanlış gittiğini söylemekle kalmaz, aynı zamanda sizi doğru yöne yönlendirmek (ve size zaman kazandırmak) için öneriler de sunar.



**Lynis**, aşağıdakiler de dahil olmak üzere çoğu Linux dağıtımı ile çalışır: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis Linux / UNIX kullanıcılarına yöneliktir, ancak aynı zamanda **macOS** uyumludur. Kurulumu çok hızlıdır, paket düzeyinde bağımlılık yönetimi yoktur.



Çeşitli amaçlar için kullanılır:





- Güvenlik denetimleri
- Uyumluluk testi (PCI, HIPAA ve SOX)
- Daha zorlu sistem konfigürasyonları
- Güvenlik açığı tespiti



Araç, sistem yöneticileri, BT denetçileri ve pentesters dahil olmak üzere geniş bir kullanıcı yelpazesi tarafından yaygın olarak kullanılmaktadır. Analizler için araç **CIS Benchmark, NIST, NSA, OpenSCAP** gibi standartlara ve **Debian, Gentoo, Red Hat** resmi önerilerine dayanmaktadır.



Proje **Github** üzerindeki bu Address adresinde mevcuttur:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Lynis'i CISOFY'den indirin](https://cisofy.com/lynis/#download)



Bu adım adım öğreticide, Debian 12** çalıştıran bir VPS kullanacağım ve yapılandırmasını kontrol etmek ve geliştirmek istediğim için SSH kısmına odaklanacağım.



## II. İndirme ve kurulum



Lynis'i indirmenin ve kurmanın birkaç yolu vardır. Aşağıdaki listeden tercih ettiğinizi seçin.



### A. Debian depolarından kurulum



Bu kurulum modu, dizinde bulunmanız gereken kaynaktan kurulumdan farklı olarak, **lynis** komutunu sistemdeki herhangi bir yerden kullanmanıza olanak tanır.



SSH üzerinden sunucunuza bağlanın ve Lynis'i kurmak için aşağıdaki komutları girin:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Alacağın şey bu:



![Image](assets/fr/024.webp)



### B. Resmi web sitesinden indirin



Cisofy web sitesinden de indirebilirsiniz:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Alacağın şey bu:



![Image](assets/fr/032.webp)



Daha sonra, aşağıdaki komutu kullanarak arşivi açacağız:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Alacağın şey bu:



![Image](assets/fr/020.webp)



Şimdi **lynis** klasörüne geçelim:



```
cd lynis
```



Aşağıdaki komut ile güncellemeleri kontrol edebiliriz:



```
./lynis update info
```



Alacağın şey bu:



![Image](assets/fr/023.webp)



### C. GitHub'dan indirin



Aşağıdaki komutu kullanarak resmi GitHub deposundan **Lynis'i** indireceğiz (*git* makinenizde mevcut olmalıdır):



```
git clone https://github.com/CISOfy/lynis.git
```



Alacağın şey bu:



![Image](assets/fr/060.webp)



## III. Lynis Kullanımı



Lynis makinemizde mevcut, o halde nasıl kullanılacağını öğrenelim!



### A. Ana kontroller ve seçenekler



Mevcut komutları görüntülemek için aşağıdaki komutu girmeniz yeterlidir:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Alacağın şey bu:



![Image](assets/fr/039.webp)



Ayrıca aşağıdaki seçeneklere de sahip olursunuz:



![Image](assets/fr/040.webp)



Mevcut tüm komutları görüntülemek için aşağıdaki komutu girin:



```
sudo lynis show
```



Alacağın şey bu:



![Image](assets/fr/022.webp)



Eğer tüm seçenekleri görüntülemek isterseniz,:



```
sudo lynis show options
```



Alacağın şey bu:



![Image](assets/fr/021.webp)



Bu makalenin geri kalanında, belirli seçenekleri nasıl kullanacağımızı öğreneceğiz.



### B. Sistem denetiminin gerçekleştirilmesi



Şimdi **Lynis'ten** sistemimizi denetlemesini isteyeceğiz ve nelerin doğru yapılandırıldığını ve nelerin geliştirilebileceğini vurgulayacağız. Bunu yapmak için aşağıdaki komutu girin:



```
sudo lynis audit system
# ou
./lynis audit system
```



Varsayılan olarak, bu komutu çalıştırdığınızda root olarak oturum açmadıysanız, araç o anda oturum açmış olan kullanıcının ayrıcalıklarıyla çalışacaktır. Bazı testler bu bağlamda çalıştırılmayacaktır:



![Image](assets/fr/052.webp)



Bu modda gerçekleştirilmeyecek testler şunlardır:



![Image](assets/fr/051.webp)



Komut yürütüldükten sonra analiz başlar. Sadece bir dakika bekleyin.



Denetimin sonunda şunu elde edersiniz (**Lynis'in** **Debian 12** sistemini doğru bir şekilde tanımladığını ve analiz için **Debian eklentisini** kullanacağını görebiliriz):



![Image](assets/fr/017.webp)



Daha sonra Lynis, sistemimizde kontrol ettiği her şeye karşılık gelen bir dizi noktayı listeleyecektir. Bu, göreceğimiz gibi kategorilere göre düzenlenmiştir. Ayrıca, önerileri vurgulamak için bir renk kodu kullanıldığını da belirtmek gerekir:





- Kritik Elements veya uyulmayan en iyi uygulamalar için kırmızı** (örneğin eksik bir paket), yani sunucunuz bu noktaya uymuyor
- Öneriler veya öneriye kısmi uyum için sarı** (diyelim ki bu renkle vurgulanan bir noktaya uymak bir artı (öncelikli değil))
- Sunucu yapılandırmanızın uyumlu olduğu noktalar için Green**
- Beyaz**, nötr olduğunda



Burada, Lynis'in **fail2ban** yüklemesini önerdiğini görebiliriz:



![Image](assets/fr/057.webp)



"**Boot and services**" bölümünde, *systemd* aracılığıyla hizmet korumasının geliştirilebileceğini görüyoruz. Olumlu tarafı, Grub2 mevcut ve izinlerle ilgili herhangi bir sorun yok:



![Image](assets/fr/029.webp)



Ardından "**Çekirdek**" ve "**Bellek ve Süreçler**" bölümlerine sahip olursunuz:



![Image](assets/fr/037.webp)



Ardından, "**Kullanıcılar, Gruplar ve Kimlik Doğrulama**" bölümü. Araç bize "**/etc/sudoers.d**" dizininin izinleri hakkında bir uyarı bildiriyor. Şu an için daha fazlasını bilmiyoruz, ancak analizin sonunda önerinin ne olduğunu görebileceğiz.



![Image](assets/fr/049.webp)



İşte "**Kabuklar", "Dosya Sistemleri" ve "USB Aygıtları "** bölümlerinde bulabilecekleriniz. Diğer şeylerin yanı sıra, bağlama noktaları hakkında öneriler olduğunu ve bu makinede USB aygıtlarına şu anda izin verildiğini görebiliriz.



![Image](assets/fr/048.webp)



Sonraki bölümler: "**İsim hizmetleri", "Bağlantı noktaları ve paketler", "Ağ".** Burada artık kullanılmayan paketlerin temizlenebileceği ve otomatik güncellemeleri yönetebilecek bir yardımcı program olmadığı belirtilmektedir.



![Image](assets/fr/058.webp)



Bir güvenlik duvarının etkinleştirildiğini görebiliyoruz (ve evet, iptables var!). Buna ek olarak, kullanılmayan kurallar bulduğunu ve bir Apache web sunucusunun kurulu olduğunu görebiliriz.



![Image](assets/fr/055.webp)



Bunu, hizmet tanımlandığından beri web sunucusunun kendisinin analizi takip eder.



Nginx** yapılandırma dosyalarını bulduğunu ve SSL/TLS kısmı için **şifrelerin** güvensiz olacak bir protokol kullanılarak yapılandırıldığını görebiliyoruz. Öte yandan Lynis'e göre log yönetimi doğru.



![Image](assets/fr/038.webp)



SSH hizmeti VPS sunucumda mevcut. Yapılandırması Lynis tarafından analiz edildi. SSH güvenliğinin kolayca geliştirilebileceği söylenmelidir! Önerileri aldıktan sonra bu alana ayrıntılı olarak geri döneceğiz.



![Image](assets/fr/026.webp)



İşte **"SNMP Desteği", "Veritabanları", "PHP", "Squid Desteği", "LDAP Hizmetleri", "Günlük ve dosyalar "** bölümleri.



Günlük yönetimi hakkında gerçekten önemli bir öneri var: günlükleri yalnızca makinenizde yerel olarak saklamamanız şiddetle tavsiye edilir. Makine bir saldırgan tarafından bozulursa, muhtemelen izlerini silmeye çalışacaktır... Bu yüzden günlükleri harici hale getirmeliyiz.



![Image](assets/fr/050.webp)



Burada, savunmasız hizmetlerin, hesap yönetiminin, zamanlanmış görevlerin ve NTP senkronizasyonunun denetimine sahibiz.afiş ve kimlik bölümünde seviyenin düşük olduğu belirtilir: bu anlaşılabilir bir durumdur, sistem sürümünü gösterirseniz, potansiyel bir saldırgana bir gösterge verir. Bu varsayılan ayardır.



Adli** analiz durumunda günlüklere sahip olmak için **auditd**'yi etkinleştirmek ilginç olacaktır. NTP** de kontrol edilir, çünkü günlükleri verimli bir şekilde aramak için sistemlerin zamanında olması tercih edilir, bu da aramayı kolaylaştırır.



![Image](assets/fr/036.webp)



Lynis daha sonra kriptografik Elements, sanallaştırma, konteynerler ve güvenlik çerçevelerine bakmaktadır. Bazı bölümler boş çünkü analiz edilen makine ile herhangi bir yazışma yok. Ancak, süresi dolmuş iki SSL sertifikam olduğunu ve **SELinux**'u etkinleştirmediğimi görebiliyoruz.



![Image](assets/fr/027.webp)



Burada da iyileştirme için yer var: anti-virüs veya anti-malware tarayıcısı yok ve dosya izinleri konusunda önerilerimiz var.



![Image](assets/fr/028.webp)



Lynis daha sonra Linux çekirdeği yapılandırmasını (IPv4 yığını için kurallar dahil) ve Linux makinesinin "Ev" dizinlerinin yönetimini sıkılaştırmaya odaklanıyor.



![Image](assets/fr/035.webp)



Analizin sonuna geldik... Bu son nokta, ClamAV'in bu makinede bulunmasının bize çok şey kazandıracağını gösteriyor.



![Image](assets/fr/030.webp)



## IV. Öneriler



Denetimden sonra sıra tavsiyeleri okumaya ve analiz etmeye gelir. Lynis tarafından gerçekleştirilen testlerin her biri için tavsiyeleri ve açıklamaları burada alıyoruz.



Örneğin SSH önerilerini ele alalım. **Her öneri için, önerilen parametreyi ve güvenlik noktasını açıklayacak bir bağlantı bulacaksınız ** Bağlamınıza ve kullanımınıza bağlı olarak karar vermek size kalmıştır.



Denetim boyunca vurgulanan noktaları doğrudan yansıtan birkaç tavsiye örneğine bir göz atalım...



### A. Tavsiye örnekleri





- Daha önce gördüğümüz gibi, NTP günlüklerin zaman damgası için önemlidir:



![Image](assets/fr/043.webp)





- Lynis ayrıca **apt.** aracılığıyla paket kurulumları sırasında kritik hatalar hakkında bilgi almak için **apt-listbugs** paketinin kurulmasını önermektedir



![Image](assets/fr/041.webp)





- Araç, hangi işlemlerin kütüphanenin eski bir sürümünü kullandığını ve yeniden başlatılması gerektiğini görebilmek için **needrestart yüklememizi öneriyor.



![Image](assets/fr/054.webp)





- Bu öneri, kimlik doğrulaması yapamayan (özellikle kaba kuvvet) ana bilgisayarları otomatik olarak engellemek için **fail2ban** yüklemenizi önerir.



![Image](assets/fr/044.webp)





- Sistem hizmetlerini güçlendirmek için, makinemizdeki her hizmet için mavi komutu çalıştırmamızı öneriyor.



![Image](assets/fr/056.webp)





- Tüm korumalı hesap parolaları için son kullanma tarihleri belirlemeyi öneriyor.



![Image](assets/fr/031.webp)





- Bu öneri, bir parolanın yaşı için minimum ve maksimum değerler belirlemeyi önerir. Diğer şeylerin yanı sıra bu, parolaların düzenli olarak değiştirilmesini sağlayacaktır.



![Image](assets/fr/042.webp)





- Disk alanı sorunlarının bir bölüm üzerindeki etkisini sınırlamak için ayrı bölümler kullanmanızı öneririz.



![Image](assets/fr/047.webp)





- Bu öneri, veri sızıntısını önlemek için USB depolama ve firewire'ın devre dışı bırakılmasını önermektedir



![Image](assets/fr/033.webp)





- Bu öneriyi karşılamak için, örneğin **unnatended-upgrade** yükleyip yapılandırmanız yeterlidir.



![Image](assets/fr/053.webp)



### B. Önerilen paketlerin yüklenmesi



Sistem yapılandırmasını iyileştirmek için makineye bazı paketler yükleyeceğiz: bazıları Lynis tarafından önerildi, bazıları da benim kişisel olarak önerdiğim paketler.



Bunları yapılandırmak için biraz zaman harcadığınız sürece, üzerinde çalışabileceğiniz iyi bir temeliniz olacaktır. Bunu yapmak için IT-Connect sitesine, Web'deki diğer makalelere ve araç belgelerine bakın.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Yüklü paketler hakkında bazı bilgiler:





- Clamav** bir antivirüs yazılımıdır.
- unattend-upgrades** güncellemelerinizi otomatik olarak yönetmenizi ve hatta makineyi yeniden başlatmanızı veya eski paketleri otomatik olarak temizlemenizi sağlar, tamamen yapılandırılabilir.
- rkhunter** dosya sisteminizi tarayan bir anti-rootkit'tir.
- Fail2ban**, okuması için verdiğiniz bilgilere göre günlük dosyalarınızı temel alacak ve **iptables** ile çalışacaktır, örneğin sunucunuzu SSH'de "kaba kuvvetle" zorlamaya çalışan IP adreslerini yasaklamak için.



### C. SSH için Öneriler



SSH önerilerine bir göz atalım. Bunlar aşağıda listelenmiştir. Merak etmeyin, yapılandırmayı nasıl geliştireceğinizi hemen açıklayacağız.



![Image](assets/fr/034.webp)



Şimdi:**/etc/ssh/sshd_config** içindeki mevcut **SSH** yapılandırmama daha yakından bakalım



![Image](assets/fr/018.webp)



Aşağıda önerilen yapılandırma yine de optimize edilebilir, ancak size iyi bir temel sağlar. *Lütfen daha okunabilir olması için bazı yorumları kaldırdığımı unutmayın*.



Biz:





- SSH bağlantı portunu değiştirme (varsayılan 22'yi unutun)
- Günlüklerin ayrıntı düzeyini **INFO'dan VERBOSE'a** yükseltin
- LoginGraceTime** değerini **2 dakika** olarak ayarlayın



İki dakika içinde herhangi bir bağlantı bilgisi girilmezse bağlantı kesilir.





- StrictModes**'u etkinleştirin



"sshd "nin bir bağlantıyı doğrulamadan önce kullanıcının dosyalarının kiplerini ve sahibini ve kullanıcının ev dizinini kontrol edip etmeyeceğini belirtir. Bu normalde istenen bir durumdur, çünkü bazen acemiler yanlışlıkla dizinlerini veya dosyalarını herkesin erişimine açık bırakabilirler. Öntanımlı değer "yes "tir.





- MaxAuthtries** değerini 3 olarak ayarlayın



Bu, iletişim kapatılmadan önce başarısız olan kimlik doğrulama denemelerinin sayısını temsil eder.





- MaxSessions** değerini 2 olarak ayarlayın



Bu, eşzamanlı oturumların maksimum sayısını temsil eder.





- Ortak anahtar kimlik doğrulamasını etkinleştirin



```
PubkeyAuthentication yes
```





- Parola kimlik doğrulamasını koru:



```
PasswordAuthentication yes
```



Boş parolaları ve **Kerberos** kimlik doğrulamasının yanı sıra **doğrudan kök kimlik doğrulamasını** yasaklayın



```
PermitEmptyPasswords no
PermitRootLogin no
```



"**PermitRootLogin no" olduğundan emin olun, "yes "e eşitse "absolute evil "** olur.





- TCP bağlantı yönlendirmesini yasaklayın



```
AllowTcpForwarding no
```



TCP yönlendirmelerine izin verilip verilmediğini belirtir, varsayılan ayar "evet "tir. Lütfen dikkat: TCP yönlendirmelerinin devre dışı bırakılması, kullanıcıların bir kabuğa erişimi varsa, kendi yönlendirme araçlarını kurabilecekleri için güvenliği artırmaz.





- X11 yeniden yönlendirmesini yasakla



```
X11Forwarding no
```



X11 yönlendirmelerinin kabul edilip edilmediğini belirtir, varsayılan ayar "hayır "dır. Lütfen dikkat: X11 yönlendirmeleri devre dışı bırakılsa bile, kullanıcılar hala kendi yönlendiricilerini ayarlayabildiğinden, bu güvenliği artırmaz. Eğer **UseLogin** seçilirse X11 yönlendirmesi otomatik olarak devre dışı bırakılır.





- İstemci ve sshd arasındaki iletişim zaman aşımını ayarlama



```
ClientAliveInterval  300
```



İstemciden herhangi bir veri alınmaması durumunda sshd hizmetinin istemciden yanıt isteyen bir ileti göndereceği zaman aşımını saniye cinsinden tanımlar. Varsayılan olarak bu seçenek "0" olarak ayarlanmıştır, yani bu mesajlar istemciye gönderilmez. SSH protokolünün yalnızca 2. sürümü bu seçeneği destekler.



```
ClientAliveCountMax 0
```



Sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) belgelerine (*man page*) göre, bu seçeneğin anlamı şudur: "**sshd** için istemciden yanıt gelmeden gönderilecek bekletme mesajlarının (yukarıya bakın) sayısını ayarlar. Bekletme mesajları gönderilirken bu eşiğe ulaşılırsa, **sshd** istemcinin bağlantısını keser ve oturumu sonlandırır. Bu bekletme mesajlarının **KeepAlive** seçeneğinden (aşağıda) çok farklı olduğuna dikkat etmek önemlidir. Bağlantı bekletme mesajları şifrelenmiş tünel üzerinden gönderilir ve bu nedenle taklit edilemez. TCP düzeyinde **KeepAlive** tarafından etkinleştirilen bağlantı bekletme taklit edilebilir. Bağlantı bekletme mekanizması, istemci veya sunucunun bağlantının boşta olup olmadığını bilmesi gerektiğinde ilgi çekicidir."





- Motd, banner, lastlog**'u devre dışı bırakarak bilgi ifşasını önleyin



```
PrintMotd no
```



Bir kullanıcı etkileşimli modda oturum açtığında sshd'nin "/etc/motd" dosyasının içeriğini gösterip göstermeyeceğini belirtir. Bazı sistemlerde, bu içerik /etc/profile veya benzer bir dosya aracılığıyla kabuk tarafından da görüntülenebilir. Varsayılan değer "yes" dir.



```
Banner none
```



Bazı yargı bölgelerinde, kimlik doğrulamadan önce bir mesaj göndermenin yasal koruma için bir ön koşul olabileceğini belirtmek gerekir. Belirtilen dosyanın içeriği, bağlantı yetkisi verilmeden önce uzaktaki kullanıcıya iletilir. Varsayılan olarak hiçbir mesaj görüntülenmeyeceğinden, bu seçeneğin yapılandırılması gerekir.



Görüntülerde bu,:



![Image](assets/fr/019.webp)



### D. Denetim puanı



Son olarak, **Lynis denetim puanını** kontrol etmeyi unutmayalım! Hardening puanımın 63** olduğunu ve rapor dosyasının "**/var/log/lynis-report.dat**" dosyasında görülebileceğini görüyoruz. Ayrıca "**/var/log/lynis.log**" dosyası da var.



**Başka bir deyişle, puan ne kadar yüksekse o kadar iyidir! Bu nedenle, makinenizin ve barındırılan hizmetlerin normal şekilde çalışmasına izin verirken (bu da işlevsel testler yapmak anlamına gelir) mümkün olan en yüksek puanı elde etmek için yapılandırmanız üzerinde çalışmanız gerekir.



![Image](assets/fr/046.webp)



Biraz daha fazla zaman harcadığım ikinci sunucumdaki sonuçlara bir göz atalım! Bu yüzden skorun daha yüksek olması normal (**76**).



![Image](assets/fr/045.webp)



## V. Lynis otomatik planlama



**Lynis** ayrıca kontrollerini zamanlanmış bir görev aracılığıyla çalıştırma seçeneği de sunar. Aslında **"--cronjob "** seçeneği, doğrulama veya kullanıcı eylemine gerek kalmadan tüm Lynis testlerini çalıştıracaktır. Daha sonra çok basit bir şekilde **Lynis'i** çalıştıracak ve çıktıyı söz konusu sunucunun adıyla zaman damgalı bir dosyaya koyacak bir komut dosyası oluşturabilirsiniz. İşte */etc/cron.daily* klasörüne koyabileceğiniz bu tür bir dosya:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



AUDITOR_NAME "** değişkeni basitçe **Lynis**'in **"--auditor "** seçeneğinde ayarlayacağımız bir değişkendir, böylece bu ad raporda görüntülenir:



![Image](assets/fr/059.webp)



Ayrıca, raporu adlandırmak ve zaman damgası vurmak için ana bilgisayar adı ve tarihi ve raporlarımızı koymak istediğimiz klasörün yolu gibi kendimizi daha iyi organize etmemize yardımcı olacak birkaç bağlamsal değişken oluşturacağız.



## VI. Sonuç



Lynis, özellikle güvenlik açısından bir Linux sunucusunun yapılandırmasının durumu hakkında daha fazla bilgi edinmek istediğinizde zamandan tasarruf etmenize ve daha verimli olmanıza yardımcı olacak çok pratik bir araçtır. Ancak, her değişikliğin üretimde uygulanmadan önce, kendi kullanımınız ve bağlamınız dikkate alınarak test edilmesi gerektiğini unutmayın.



Muhtemelen aynı yapılandırmayı, **SSH.** bağlantılarını çoğaltmaya ihtiyaç duyacak bir **bastion** veya **scheduler**'ın aksine, yalnızca bir SSH bağlantısına ihtiyaç duyduğunuz (çünkü bağlanan tek kişi sizsiniz) Net'e maruz kalan bir VPS için uygulamayacaksınız



Güçlendirme açısından size uygun bir yapılandırmaya sahip olduğunuzda, zaman alıcı ve hataya açık olacağından, görevleri manuel olarak yeniden yapmak zorunda kalmamak için bir otomasyon aracı kullanmanız önerilir. Örneğin, ** kullanabilirsiniz: Puppet, Chef, Ansible, vb...**



Uygulamadan önce ekiplerinizle iletişim kurmayı unutmayın: bu değişiklikleri neden yaptığınızı anlamalarını sağlamanız gerekir, sadece yapacağınızı söylemeniz değil. Sonuçta amaç iyi uygulamaları aktarmak olacak ve bu da başarı şansınızı artıracaktır.



Son olarak, **Lynis**'i birkaç tane olan diğer araçlarla da karşılaştırabilirsiniz. Açık kaynak kalırken merkezi yönetime doğru ilerlemek istiyorsanız, [Wazuh] aracını öneririm (https://wazuh.com/).



**Bu eğitim bitti, Lynis ile iyi eğlenceler!