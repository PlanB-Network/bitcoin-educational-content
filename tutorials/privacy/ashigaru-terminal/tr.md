---
name: Ashigaru Terminal
description: Coinjoins yapmak için masaüstünde Ashigaru kullanın
---

![cover](assets/cover.webp)



Ashigaru Terminal, Ashigaru ekibinin Whirlpool coinjoin protokolünü uygulayan Sparrow Sunucusunun uyarlamasıdır. Bu yazılım, Samourai Wallet tarafından, özellikle de temel ilkeleri olan kendi kendini saklama ve gizliliğin korunması ilkelerini benimsediği Whirlpool GUI üzerinde başlatılan çalışmanın bir devamıdır.



Bu yazılım, orijinal olarak Samourai ekipleri tarafından geliştirilen ZeroLink coinjoin protokolü olan Whirlpool ekosistemi ile tam entegrasyon için değiştirilmiş ve optimize edilmiş bir Sparrow Sunucusu fork'tir.



Ashigaru Terminal minimalist bir TUI arayüzünden çalışır ve kişisel bir bilgisayarda veya özel bir sunucuda konuşlandırılabilir. "*Tx0*" başlatmak, "*Deposit*", "*Premix*", "*Postmix*" ve "*Badbank*" hesaplarını yönetmek ve parçalarınızın gizliliğini güçlendirmek için otomatik remiksler gerçekleştirmek için doğrudan Whirlpool ile etkileşime girmenizi sağlar.



Kısacası, Ashigaru Terminal, Whirlpool kullanarak coinjoins oluşturmak istiyorsanız özellikle yararlı olacaktır.



Bu ilk eğitimde, Ashigaru Terminal'in kurulumunu ve çalışmasını anlatacağım. Daha sonra ikinci ve daha ileri düzey bir eğitimde coinjoins'in gerçek yaratımına yer vereceğim.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Ashigaru Terminalini Kurun



Ashigaru Terminal'i yüklemek için Tor Browser'a ihtiyacınız olacak, çünkü ikili dosyalar yalnızca Tor ağı üzerinden dağıtılmaktadır. Eğer henüz yapmadıysanız, [makinenize yükleyin](https://www.torproject.org/download/).



### 1.1. Ashigaru Terminal'i indirin



Tor Browser'dan, işletim sisteminiz için Ashigaru Terminal'in en son sürümünü indirmek için [Git depolarının sürümler sayfasına](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) gidin.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



İşletim sisteminiz için aşağıdaki 2 dosyayı indirin:




- İkili dosya (Debian/Ubuntu için `ashigaru_terminal_v1.0.0_amd64.deb`, macOS için `.dmg` veya Windows için `.zip`) ;
- İmzalı hash dosyası: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Ashigaru Terminalini kontrol edin



Yazılımı cihazınızda çalıştırmadan önce, orijinalliğini ve bütünlüğünü kontrol etmeniz gerekir. Bu önemli bir adımdır, çünkü bitcoinlerinizi tehlikeye atabilecek veya makinenize bulaşabilecek sahte bir sürüm yüklemenizi önler.



Yeni bir tarayıcı sekmesi açın ve [Keybase doğrulama aracı](https://keybase.io/verify) adresine gidin. İndirdiğiniz `.txt` dosyasının içeriğini verilen alana yapıştırın ve ardından `Doğrula` düğmesine tıklayın.



![Image](assets/fr/02.webp)



Doğrulama kaynaklarınızı çeşitlendirmek için, mesajı clearnet [ashigaru.rs](https://ashigaru.rs/download/) sitesinde `/download` bölümünde mevcut olanla da karşılaştırabilirsiniz.



![Image](assets/fr/03.webp)



İmza geçerliyse, Keybase dosyanın Ashigaru'nun geliştiricileri tarafından imzalandığını onaylayan bir mesaj görüntüleyecektir.



![Image](assets/fr/04.webp)



Ayrıca Keybase tarafından görüntülenen `ashigarudev` profiline tıklayabilir ve anahtar parmak izinin tam olarak eşleştiğini kontrol edebilirsiniz: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Bu aşamada bir hata görünürse, imza geçersizdir. Bu durumda, **indirilen yazılımı yüklemeyin**. Baştan başlayın veya devam etmeden önce topluluktan yardım isteyin.



Keybase size uygulamanın doğrulanmış hash'ini sağladı. Şimdi indirdiğiniz `.deb`, `.zip` veya `.dmg` dosyasının hash'inin Keybase'de doğrulanmış olanla eşleşip eşleşmediğini kontrol edeceğiz. Bunu yapmak için [HASH FILE ONLINE](https://hash-file.online/) adresine gidin.



GÖZAT...` düğmesine tıklayın ve 1.1 adımında indirilen `.deb`, `.zip` veya `.dmg` dosyasını seçin. Ardından `SHA-256` hash fonksiyonunu seçin ve dosyanızın hash'ini generate yapmak için `CALCULATE HASH` butonuna tıklayın.



![Image](assets/fr/06.webp)



Site daha sonra yazılım karmasını görüntüleyecektir. Keybase.io'da doğruladığınız hash ile karşılaştırın. İkisi mükemmel bir şekilde eşleşirse, özgünlük ve bütünlük kontrolü başarılı olmuştur. Daha sonra yazılımı kullanabilirsiniz.



![Image](assets/fr/07.webp)



### 1.3 Ashigaru Terminalini Başlatın





- Debian / Ubuntu



Yazılımı yüklemek için şu komutu çalıştırın :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



İndirilen sürüme göre sıralamayı değiştirin.



Ardından kurulumu kontrol edin:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Ardından yazılımı başlatın:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Pencereler**



İndirdiğiniz ve kontrol ettiğiniz `.zip` dosyasına sağ tıklayın, ardından içeriğini çıkarmak için `Tümünü Çıkar...` seçeneğini seçin.



Çıkarma işlemi tamamlandıktan sonra, yazılımı başlatmak için `Ashigaru-terminal.exe` dosyasına çift tıklayın.



![Image](assets/fr/08.webp)



## 2. Ashigaru Terminal ile çalışmaya başlama



Ashigaru Terminal bir TUI (*Text-based User Interface*) programıdır, yani doğrudan terminalde çalışan minimalist bir arayüzdür. Menüler ve klavye kısayollarını kullanarak, ancak herhangi bir gerçek klasik grafik ortamı olmadan etkileşimde bulunursunuz.



![Image](assets/fr/09.webp)



Kullanımı kolaydır: menüler arasında gezinmek için klavyenizin ok tuşlarını kullanın ve bir eylemi doğrulamak veya bir seçimi onaylamak için `Enter` tuşuna basın.



## 3. Düğümünüzü Ashigaru Terminaline Bağlama



Varsayılan olarak, Ashigaru Terminal halka açık bir Electrum sunucusuna bağlanır. Bunun gizlilik ve egemenlik açısından riskler taşıdığı açıktır. Bu yüzden onu doğrudan kendi Electrum Server'unuza bağlanacak şekilde yapılandıracağız.



Bunu yapmak için `Tercihler > Sunucu` menüsünü açın.



![Image](assets/fr/10.webp)



<Düzenle >` düğmesine tıklayın.



![Image](assets/fr/11.webp)



Özel Electrum Server`yi seçin ve ardından `<Devam>` seçeneğine tıklayın.



![Image](assets/fr/12.webp)



Sunucunuzun URL'sini ve bağlantı noktasını girin. Tor adresini `.onion` olarak belirtebilirsiniz. Ardından bağlantıyı doğrulamak için `< Test >` seçeneğine tıklayın.



![Image](assets/fr/13.webp)



Bağlantı başarılı olursa, sunucunuzun ayrıntılarıyla birlikte `Başarı` mesajı görünecektir.



![Image](assets/fr/14.webp)



Henüz bir Bitcoin düğümüne sahip değilseniz, bu kursa katılmanızı tavsiye ederim:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Benim durumumda, bu eğitim için Electrs sunucumla bağlantımı keseceğim çünkü testnet üzerinde çalışıyorum. Ancak, mainnet'te işlem kesinlikle aynı kalır.*



## 4. Ashigaru Terminalinde bir portföy oluşturun



Artık yazılım doğru şekilde yapılandırıldığına göre, bir Bitcoin portföyü ekleyebiliriz.



İki seçeneğiniz var:




- Sıfırdan yeni bir wallet oluşturabilir ve bunu yalnızca Ashigaru Terminal'de kullanabilirsiniz. Bu durumda, wallet'nizle her etkileşime geçmek istediğinizde bu yazılımı açmanız gerekecektir;
- Alternatif olarak, mevcut Ashigaru wallet'inizi doğrudan telefonunuzdan Ashigaru Terminal'e aktarabilirsiniz. Bu yöntemin dezavantajı, wallet'inizin bir yerine iki riskli ortama maruz kalması nedeniyle kurulumunuzun güvenliğini biraz azaltmasıdır. Öte yandan, Ashigaru Terminalini madeni paralarınızı karıştırmak için sürekli çalışır durumda bırakabilmenin avantajını sunarken, Ashigaru mobil uygulaması aracılığıyla bunları uzaktan harcamanıza olanak tanır.



Bu eğitimde ikinci yöntemi tercih edeceğiz. Bununla birlikte, tamamen yeni bir portföy oluşturmayı tercih ederseniz, prosedür aynı kalır: tek fark, oluşturma sırasında yeni anımsatıcı ifadenizi ve yeni passphrase'unuzu kaydetmeniz gerekecektir.



Ayrıca, Ashigaru Terminal'in bitcoinlerinizi doğrudan harcamanıza izin vermediğini unutmayın. Aynı cüzdanı Ashigaru Terminal ve Ashigaru uygulamasında (bu eğitimde yapacağım gibi) veya Sparrow Wallet'ta senkronize edebilirsiniz.



Ashigaru uygulamasında henüz bir wallet'e sahip değilseniz, özel öğreticiyi takip edebilirsiniz:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Cüzdanlar menüsüne gidin.



![Image](assets/fr/15.webp)



Ardından `wallet oluştur / geri yükle...` seçeneğini seçin. Wallet'yi Aç...` seçeneği, Ashigaru Terminal'de önceden kaydedilmiş bir portföye daha sonraki bir tarihte erişmenizi sağlar.



![Image](assets/fr/16.webp)



Portföyünüze bir isim verin.



![Image](assets/fr/17.webp)



Ardından `Hot Wallet` portföy türünü seçin.






![Image](assets/fr/18.webp)



Bu aşamada prosedür, ilk seçiminize bağlı olarak farklılık gösterir:




- Sıfırdan yeni bir portföy oluşturmak istiyorsanız, `<Yeni Wallet Oluştur>` seçeneğine tıklayın, bir passphrase BIP39 tanımlayın, ardından anımsatıcı ifadenizi ve passphrase'nizi fiziksel bir ortama dikkatlice kaydedin;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Ashigaru uygulamanızla aynı wallet'u kullanmak istiyorsanız, anımsatıcı ifadenizin 12 kelimesini ve passphrase BIP39'unuzu doğrudan ilgili alanlara girin. Kelimeleri küçük harflerle, tam olarak, sırayla, bir boşlukla ayırarak, sayı veya ekstra karakter olmadan yazın.



Bu adım tamamlandıktan sonra `< İleri >` düğmesine tıklayın.



*Not*: Bu düğmeye tıklayamıyorsanız, anımsatıcı ifadeniz geçersizdir. Hiçbir kelimenin yanlış veya hatalı yazılmadığını dikkatlice kontrol edin.



![Image](assets/fr/19.webp)



Daha sonra bir şifre belirlemeniz gerekecektir. Bu, Ashigaru Terminaliniz wallet'nin kilidini açmak ve yetkisiz fiziksel erişime karşı korumak için kullanılacaktır. Anahtarlarınızın kriptografik türetilmesinde yer almaz: başka bir deyişle, bu parola olmadan bile, anımsatıcı ifadenize ve passphrase'e sahip olan herkes wallet'nizi geri yükleyebilir ve bitcoinlerinize erişebilir.



Uzun, karmaşık, rastgele bir parola seçin. Bir kopyasını güvenli bir yerde saklayın: ideal olarak fiziksel bir ortamda veya güvenli bir parola yöneticisinde.



İşiniz bittiğinde `<Tamam >` düğmesine tıklayın.



![Image](assets/fr/20.webp)



## 5. Portföyü kullanma



Daha sonra hangi hesaba erişeceğinizi seçebilirsiniz. Şu an için herhangi bir karışım başlatmadık, bu nedenle `Deposit` hesabına erişeceğiz.



![Image](assets/fr/21.webp)



Ashigaru Terminali Sparrow Sunucusunun bir fork'ü olduğu için kullanım Sparrow ile aynıdır. Aynı menüleri bulacaksınız:



![Image](assets/fr/22.webp)





- işlemler": bu hesaba bağlı işlemlerin geçmişine bakmanızı sağlar. Benim durumumda, aynı wallet üzerinde Ashigaru uygulaması ile bazı işlemler yaptığım için bazıları zaten görünüyor.



![Image](assets/fr/23.webp)





- receive`: sats'ları mevduat hesabına yerleştirmek için yeni, boş bir makbuz adresi oluşturur.



![Image](assets/fr/24.webp)





- addresses`: hesabınızın dahili veya harici zincirine ait olup olmadıklarına bakılmaksızın tüm adreslerinizin bir listesini görüntüler.



![Image](assets/fr/25.webp)





- `UTXOs`: mevcut tüm UTXO'larınızı listeler.



![Image](assets/fr/26.webp)





- ayarlar: portföy *tanımlayıcınıza* erişim sağlar. Ayrıca seed'nıza bakabilir, *Gap Limitini* ayarlayabilir veya portföyünüzün oluşturulma tarihini değiştirebilirsiniz.



![Image](assets/fr/27.webp)



Artık Ashigaru Terminal'i nasıl kurup kullanacağınızı biliyorsunuz. Bir sonraki eğitimde, bu yazılımla coinjoin işlemlerinin nasıl yapılacağını ve "*Postmix*" fonlarının nasıl yönetileceğini göreceğiz.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
