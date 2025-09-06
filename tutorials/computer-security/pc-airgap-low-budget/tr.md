---
name: Küçük, düşük bütçeli bir hava boşluğu bilgisayarı
description: Raspberry PI Zero ve bir aksesuar kiti ile bir hava boşluğu bilgisayarı nasıl yapılır. Hepsi 35,00 avroluk bir bütçeyle.
---
![cover](assets/cover.webp)



Plan ₿ Network sayfalarında bir süredir bulunuyorsanız, en çok savunulan güvenlik ayarlarından birinin, neredeyse bir zorunluluk olduğunu, **özel anahtarlarınızın çevrimdışı depolanması yoluyla fon yönetimi olduğunu** zaten öğrenmişsinizdir.



Henüz keşfetmediyseniz, bu eğitim boyunca bu konuda daha fazla bilgi edinebileceğiniz açık kaynak kaynaklara bağlantılar bulacaksınız.



Bu nedenle, özel anahtarları çevrimdışı yönetmek için, [Hardware Wallet] (https://planb.network/resources/glossary/hardware-Wallet) veya bir airgap bilgisayarı gibi ağ bağlantısı sürekli olarak kesilen ve bu özel işleve adanmış bir cihaza ihtiyacınız vardır.



Örneğin, yalnızca bu görevi yerine getiren bir donanım satın alma olanağınız yoksa, ancak bu güvenlik adımından vazgeçmek istemiyorsanız bunu nasıl yaparsınız?



## Çözüm


Size bir USB flash bellek boyutunda ve ağırlığında ve 35 Euro'ya mal olan bir hava boşluğu bilgisayarı şeklinde çevrimdışı bir cihaz yapabileceğinizi söylesem? Buna inanmaz mıydınız?



Okumaya devam edin.



Size daha fazlasını anlatacağım: sonuna kadar okuyun. Önerilen çözüm ucuz, ancak tam olarak en kolayı değil. Önce genel fikri edinirsiniz, sonra zamanınızın bir kısmını kişisel araştırmaya ayırmaya karar verirsiniz ve mümkün olduğunca gönül rahatlığıyla devam edip etmeyeceğinize ve nasıl devam edeceğinize karar verirsiniz.



## Gereksinimler


**1** Bir [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (arkasında herhangi bir kısaltma olmadan) minimal performanslı bir bilgisayar yapmak için temeldir, ancak çoğunlukla bu alıştırmanın amacı için ön koşullar olan Wi-Fi ve Bluetooth kartlarından yoksundur.





- Maliyet**: Bu yazının yazıldığı tarihte (Ağustos 2025) yaklaşık 15.00.
- Üretimin sürekliliği**: Ahududu, Ocak 2030'a kadar üretimi garanti eder.



Wi-Fi ve Bluetooth'u olmayan PI Zero, ne yazık ki neredeyse kullanılamaz hale geldi. PI Zero W ve PI Zero 2W alternatiflerini daha kolay bulabilirsiniz. Bu durumda, yapılandırma dosyasını değiştirerek bağlantı işlevlerini devre dışı bırakabilirsiniz. İşletim sistemini kurduktan sonra, bu öğeleri yapılandırmaya eklemeniz gerekecektir:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



bu kılavuzun bir bölümü size bunu nasıl ve nerede yapacağınızı gösterecektir. Ancak, gerçekten emin olmak istiyorsanız, Wi-Fi çipini elektronik kartlar üzerinde çalışmaya uygun küçük bir kesici ile çıkarmak için web'de birkaç eğitim bulabilirsiniz.



**2** Raspberry PI Zero için bir _starter kiti_: Raspberry dünyasında olduğu gibi, harici bir kılıf olmadan çıplak kemikler. Buna ek olarak, bu kadar küçük bir kartın sınırlı kaynakları, dış dünya ile bağlantı olanaklarını şartlandırır.



Devam etmeye karar verdiğimde, PI Zero'nun tüm potansiyelinden tam olarak yararlanmak için aksesuarlarla dolu [bu kiti] (https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) buldum. Aslında, kit bir USB A -> mikro USB güç Supply, küçük bir USB hub, bir mini-HDMI -> HDMI adaptörü, bir bakır soğutucu ve bir alüminyum dış kasa içerir. Kitle birlikte ayrıca PI Zero'yu yeni kasaya yerleştirmek için gereken vidalar ve alyan anahtarı da veriliyor.





- Maliyet**: 19.99 Euro.



**3** Bu eğitim, airgap bilgisayar için büyük bütçeler harcamanızı gerektirmez. Bununla birlikte, bir USB klavye ve fareye (kesinlikle kablolu, Bluetooth'tan kaçının) ve bir monitöre ihtiyacınız olacağını bilmelisiniz. Monitörünüzün girişine bağlı olarak, PI Zero'da bulunan tek çıkış olan mini-HDMI'dan bir adaptöre ihtiyacınız olabilir. Son olarak, hepimizin evde bir yerlerde kablosuz olmayan bir klavye ve fareye sahip olduğu gerçeği için Hard'e bakın - onları Dust'ten çıkarmanın zamanı geldi.



## Ekstra Bütçe



**4** Orijinal Supply gücünü Raspberry'den yaklaşık 15,00 Euro'ya alabilirsiniz.



**5** Ben şahsen _starter kit_ içinde verilen Supply gücünü kullanmayı tercih ettim, ancak bunu 3,70 Euro'ya mal olan bir USBA → miniUSB sözde "veri yok" kablosu ile birleştirdim.



**6** En az 32 GB yığın depolama alanına sahip bir mikro SD kart; endüstriyel kalite/seviye daha iyi ise.



**7** Resimde gördüğünüz gibi bir sisteme, bir USB - mikro SD adaptörüne ihtiyacınız olacaktır. PI Zero'nuzun işletim sistemi ve belleği aslında bu medya üzerinde çalışacaktır.



![img](assets/it/06.webp)



## İşletim Sisteminin Kurulumu


PI Zero'nuzu kasaya kapatmadan önce işletim sistemini yüklemenizi tavsiye ederim. Böylece çalıştığını gösteren LED'i hemen kontrol edebileceksiniz.



İşletim sistemini seçmek ve yazdırmak için en kolay yolu seçtim: Raspberry`nin `PI Imager` aracını kullanmak.



![img](assets/it/01.webp)



Ardından [Raspberry's Github] (https://github.com/raspberrypi/rpi-imager/releases) adresine giderek Imager'ın en son sürümünü indirin ve işletim sisteminiz için en uygun olanı seçin (yazım sırasında v. 1.9.6). Her varlığın yanında, ilgili dosyanın Hash'inin de olduğunu fark edeceksiniz. Doğrulama için kullanışlı olacaktır.



![img](assets/it/02.webp)



Kendi kişisel huzurunuz için airgap bilgisayarınızda kullanacağınız işletim sistemini doğrulamanızı tavsiye ederim. Bu size Imager'ın ve dolayısıyla Raspi OS'nin yasal (kötü niyetli olmayan) bir sürümüyle çalıştığınıza dair güven verecektir.



Doğrulamayı indirme işleminin hemen ardından, normalde kullandığınız makineniz internete bağlıyken yapın



Ardından Linux terminalini açın ve indirmeyi hazırlayın, onunla çalışmak için yararlı bir `raspios` dizini oluşturun.



![img](assets/it/19.webp)



Linux dağıtımınız için Görüntüleyiciyi `wget` ile indirin.



![img](assets/it/20.webp)



Son olarak, `sha256sum` komutunu çalıştırın ve Hash dosyasını Raspberry tarafından Github'da sağlanan dosya ile karşılaştırın.



![img](assets/it/21.webp)



Ya da Windows kullanıyorsanız, Power Shell'i açın ve aşağıdaki komutu yazın:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Raspberry Github'da yayınlananla eşleşmesi gereken Hash'u alacaksınız.



İndirmeyi doğruladıktan sonra, Imager'ı günlük bilgisayarınıza yükleyebilir ve açabilirsiniz. Imager, işletim sistemini PI Zero'nun "sistem diski" olacak olan mikro SD'ye yazmak için ihtiyacınız olan araçtır.



İşlem son derece basittir: önce kullanacağınız Raspberry cihazını seçin (bu nedenle Raspi Zero'nun **modelinize** dikkat edin), ardından işletim sistemi sürümünü ve son olarak işletim sistemini flaşlamak için mikro SD kartın bağlama noktasını seçin.



### İlk Adım



![img](assets/it/03.webp)



### İkinci Adım



![img](assets/it/07.webp)



**İyi not edin**: PI Zero ile çalışan tek işletim sistemi olan `PI OS 32-bit`i seçin.



### Üçüncü Adım



![img](assets/it/08.webp)



(Raspi'nin işletim sistemini bilgisayarınıza yüklemenizin istenmesini önlemek için _Sistem Sürücüsünü Dışla_ seçeneğini seçili bırakmaya çok dikkat edin)



Her şey ayarlandığında, Görüntüleyici size özel ayarları kullanmak isteyip istemediğinizi soracaktır. İstediğinizi seçin veya varsayılan seçeneklerle devam etmek için _Hayır'a tıklayın.



![img](assets/it/09.webp)



Mikro SD'nin içeriğini silmek istediğinizi onaylayın



![img](assets/it/10.webp)



Imager işletim sistemini mikro SD'ye aktarmaya başlar, bir kaydırma çubuğu ilerleme hakkında sizi bilgilendirir.



![img](assets/it/11.webp)



Sonunda otomatik doğrulama var, bunu durdurmamanızı tavsiye ederim.



![img](assets/it/12.webp)



Sonunda ekranda bir mesaj belirir ve her şey başarılı olduysa, resimde okuduğunuz gibi görünür.



![img](assets/it/13.webp)



Artık mikro SD'yi okuyucudan çıkarabilir ve PI Zero'nun yuvasına yerleştirebilirsiniz. Küçük Raspberry'yi açın ve ledi gözlemleyin: Green renginde olmasını ve işletim sisteminin normal yüklendiğini gösterecek şekilde yanıp sönmesini ve ardından sürekli yanık kalmasını bekliyoruz. Ledin düzenli bir frekansta yanıp sönmesi veya kırmızı renkte olması gibi başka göstergeleriniz varsa, SSS veya [destek forum sayfalarına] (https://forums.raspberrypi.com/) başvurun.



## İlk Yapılandırma


Raspi OS'nin ilk açılışı normalden biraz daha yavaştır çünkü bir dizi gerçek kurulum görevini yerine getirmesi gerekir. Ancak her şey yolunda gittiyse, bir karşılama ekranı göreceksiniz.



![img](assets/it/14.webp)



Özellikle doğru klavyeyi yüklemek için coğrafi bölgeyi ayarlamak üzere _Next_ üzerine tıklayın. İkincisine özellikle dikkat edin.



![img](assets/it/15.webp)



Sonraki_ üzerine tıkladığınızda kullanıcınızı oluşturmanız, kimlik bilgilerinizi not etmeniz ve iyi saklamanız istenecektir.



![img](assets/it/16.webp)



Sihirbaz sizden Chromium ve Firefox arasında varsayılan bir web tarayıcısı seçmenizi ister; ayrıca Zero W veya 2W PI ile çalışıyorsanız Wi-Fi ağ ayarlarını da sorabilir. Devam edin ve _Skip_'e tıklayın.



Bir noktada yerleşik yazılımı ve işletim sistemini yükseltmeniz istenecektir. _Skip_ seçeneğini seçin: bu alıştırmanın amaçları doğrultusunda aslında çevrimdışı bir makine inşa ediyoruz ve bu makinenin şu andan itibaren çevrimdışı kalması gerekiyor.



Son olarak, sizden `ssh` özelliğini etkinleştirmenizi isteyebilir, ancak Zero airgap IP olduğu için bu adımı da reddedin.



![img](assets/it/17.webp)



Yapılandırılacak başka bir şey yoktur. İşiniz bittiğinde, değişikliklerin etkili olması için Raspberry'yi yeniden başlatın.



![img](assets/it/18.webp)



## Yeni Bir Bilgisayar Hava Boşluğu


Yeniden başlattıktan sonra yeni airgap bilgisayarınız hazırdır. PI Zero size GUI veya komut satırından çalışabileceğiniz yeni masaüstünü gösterir.



![img](assets/it/22.webp)



### PI Zero W veya 2W için İlk Adımlar


Raspberry PI Zero W veya 2W serisi ile çalışıyorsanız, kartınızda Wi-Fi ve Bluetooth için çipler vardır. İlk kurulum sırasında bağlantı yapılandırmasını atladınız, bu nedenle PI Zero internete bağlı değil. Şimdi yazılım aracılığıyla bu iki çipi kalıcı olarak devre dışı bırakabilirsiniz.



Aslında, Raspi OS istediğiniz gibi düzenleyebileceğiniz bir `config.txt` dosyası sağlar. Bu `config` dosyası `boot` bölümünde, `firmware` dizininde bulunur ve `root` ayrıcalıklarıyla düzenleyip kaydedebilirsiniz.



Sol üstteki simgeden terminali açın ve `root` olur.(1)



![img](assets/it/23.webp)



(1) Eğer Raspi OS önceki adımlar sırasında `root` şifresini oluşturmadıysanız, bunu şimdi `passwd` komutu ile yapmanızı tavsiye ederim. Root` kullanıcısının kişisel kullanıcınızdan bağımsız olarak hareket etmesi kurtarma durumlarında çok kullanışlı olabilir.



Terminal ile `config.txt` dosyasını kontrol edin ve `nano` editörü ile düzenlemeye hazır olun.



![img](assets/it/24.webp)



Düzenleme tüm `config` bölümünün en altında, `[All]` kelimelerinden sonra yapılmalıdır. Bu noktada, eğitimin başında gösterilen `dtoverlay` komutlarını ekleyeceksiniz.



![img](assets/it/25.webp)



Kaydedin, kapatın ve yeniden başlatın. Bir sonraki adımda küçük Raspberry'nin keşfine çıkacağız.



## Bu Cihazdan Ne Beklemeliyim?


Raspberry'nin web sitesindeki [teknik özelliklere] (https://www.raspberrypi.com/products/raspberry-pi-zero/) bakıldığında, PI Zero'nun 1 çekirdekli BCM2835 işlemcisi ve 512 MB RAM'i var, bu nedenle çok güçlü olmayı vaat etmiyor.



Terminal daha hafif olduğundan, sistem yapılandırmalarını keşfetmek için komut satırını kullanacağız.



Açtığınızda gökkuşağı renginde kısa bir ekran göreceksiniz, ardından Raspberry'den bir hoş geldiniz mesajı ve sol alt köşede önyükleme ile ilgili çekirdek mesajları göreceksiniz.



PI OS masaüstü göründüğünde, terminali açın ve yazın:



```bash
uname -a
```


Bu komut size ekranda o anda kullanılmakta olan çekirdek sürümünü ve diğer bilgileri gösterecektir.



![img](assets/it/26.webp)



CPU ve donanım hakkındaki bilgileri yazarak da görebilirsiniz:



```bash
lscpu
```



![img](assets/it/27.webp)



Ayrıca `proc/mem/info` bölümüne de bakın.



![img](assets/it/28.webp)



Debian sürümünü ve sürüm kod adını öğrenmek için:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Kullanım


Performansı sınırlı görünse de (kağıt üzerinde ve günümüz makinelerinin gücüyle karşılaştırıldığında) PI Zero özellikle bir terminal olarak oldukça performanslıdır.





- Öncelikle ana menülere gidebilir ve programlamak ve pratik yapmak için bir dizi yardımcı program bulacağınız _Yazılım Ekle/Kaldır_ panelinden ilham alabilirsiniz. Bunu terminalden de yapabileceğinizi unutmayın, ancak her zaman `root` ayrıcalıklarıyla.



![img](assets/it/33.webp)





- Bu çevrimdışı cihazı, internete hiç maruz kalmadan gerektiğinde erişilebilecek çeşitli gizli belgeleri saklamak için "benimseyebilirsiniz".
- Bu yapılandırmayı GPG anahtarlarınızı güvenli bir şekilde generate yapmak için kullanabilirsiniz.
- Hatta, [Arman The Parman'ın tavsiyesine uyarak] bu yeni "oyuncağı" bir hava boşluğu imza cihazı olarak kullanabilirsiniz (https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-Wallet-85e59ecaddc0).



Bildiğim cüzdanlar arasında 32 bit sürüm sunan tek cüzdan Electrum'dur. Bu eğitimde hazırladığımız Zero IP, bu eğitimde ele aldığımız Wallet airgap kurulumunda özel anahtarları çevrimdışı tutmanıza izin verecektir:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Sonuçlar


Kurulumun muhtemelen büyük bir zayıflığı var: micro SD sorun çıkarabilecek bir ortam. Yoğun kullanıma karşı savunmasızdır; belki de telefonunuzda kullandığınız için bu konuda zaten deneyiminiz vardır. Zero airgap IP üzerinde kullanmak isteyeceğiniz tüm yazılımları yükledikten sonra, elinizdeki Raspi OS aracını kullanarak değerli mikro SD'nin iyi bir yedeğini alın.



![img](assets/it/34.webp)



İhtiyaçlarınız ve bunlarla birlikte bütçe olanaklarınız arttıkça, diğer Raspberry veya benzer çözümleri keşfedebilirsiniz. Bellekten bahsetmişken, örneğin PI 5, microSD'den kesinlikle daha sağlam olan bir M2 NVME sürücü monte etme imkanı sunuyor.



Çevrimdışı kullanmak üzere olduğunuz yardımcı yazılım kurulumunun her adımını not almayı ve belgelemeyi unutmayın. **Er ya da geç, kesinlikle yararlanmak isteyeceğiniz güncellenmiş bir Raspi OS çıkacaktır**. O noktada her şeyi silmeniz ve her şeyi baştan yapmanız gerekecek (belki yeni bir mikro SD ile 😂).



Az önce yaptığımız alıştırmayı, bunun sizin de ilk denemeniz olduğunu varsayarsak, uzun süre hatırlayacaksınız. Donanımı çevrimdışı olarak `embedded' işlemlere ayırmak, zaman zaman açıp kontrol etmek için hava boşluklu bir makineye dikkat etmeyi ihmal etmeden her zaman mümkün değildir.



Yine de başardınız, tebrikler! Ve bu çözümü bütçelerini düşük tutmak isteyen herkese önerebileceksiniz.