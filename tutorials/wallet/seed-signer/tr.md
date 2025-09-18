---
name: SeedSigner

description: seed imzalayıcınızın kurulumu
---

![cover](assets/cover.webp)


## Malzeme:


**Raspberry Pi Zero (sürüm 1.3)**


Tamamen hava boşluklu bir çözüm için, WiFi veya Bluetooth özelliği olmayan 1.3 sürümünü kullandığınızdan emin olun, ancak herhangi bir Raspberry Pi 2/3/4 veya Zero modeli çalışacaktır.


Not: Raspberry Pi'ler genellikle pinleri takılı olarak gelmezler; pinlerin lehimlenmesi gerekir ya da "GPIO Hammer" adı verilen bir şey kullanılabilir.

GPIO Çekici


Eğer lehimleme beceriniz yeterli değilse ya da henüz bir havyanız yoksa, lehimlemeye alternatif olarak "GPIO Hammer" kullanabilirsiniz.


**Şapka LCD WaveShare 1,3 inç ekran 240 × 240 piksel**


WaveShare LCD Hat 1.3″ 240×240 piksel LCD


**Not:** Waveshare ekranını dikkatli seçin; 240×240 piksel çözünürlüğe sahip modeli satın aldığınızdan emin olun.


**Pi Zero ile uyumlu kamera modülü**


Raspberry Pi Kamera Aokin/AuviPal 5MP 1080p OV5647 Sensörlü Video Kamera Modülü; OV5647 sensör modülüne sahip diğer markalar da çalışmalıdır, ancak Orange Pill muhafazası ile uyumlu olmayabilir.


**Not:** Raspberry Pi Zero ile özel olarak uyumlu bir kamera şerit kablosuna sahip olmanız gerekecektir.


**En az 4 GB kapasiteli microSD kart**


kapsamlı kaynaklar: https://seedsigner.com/explainers/


## Yazılım:


Yazılım Kurulumu


1. En son "seedsigner_x_x_x.img.zip" dosyasını indirin

son sürüm

2. "seedsigner_x_x_x.img.zip" dosyasını açın

3. Sıkıştırılmamış .img görüntü dosyasını bir microsd karta yazmak için Balena Etcher veya benzer bir araç kullanın

BALENA ETCHER

4. Mikrosd kartı SeedSigner'a takın.

SeedSigner GPG Açık Anahtarı

seedsigner_pubkey.gpg


## Eğitici video


cole tarafından oluşturulan Southerbitcoiner'dan alınan rehber_


### SeedSigner'ı kapsayan bir video kılavuz koleksiyonu: açık kaynaklı, DIY Hardware Wallet/İmzalama cihazı


![image](assets/1.webp)


SeedSigner, sıfırdan inşa edebileceğiniz bir Bitcoin İmzalama Cihazıdır. Kulağa zor geliyor, ancak bu 4 bölümlük seri size yardımcı olacaktır :) Bölüm 1 ve 2'yi izlemenizi, ardından masaüstü (bölüm 3'ü izleyin) veya mobil cihaz (bölüm 4'ü izleyin) kullanmak isteyip istemediğinize karar vermenizi öneririm.


Bilmeniz gereken her şey aşağıda olacak. Diğer faydalı bağlantılar arasında SeedSigner'ın web sitesi, Github, Keybase, en son sürüm ve donanım gereksinimleri yer almaktadır.


### Bölüm 1: Bir SeedSigner nasıl oluşturulur:


Bu videoda size SeedSigner yazılımını nasıl indirip doğrulayacağınızı, hangi parçaların gerekli olduğunu ve SeedSigner'ınızı nasıl monte edeceğinizi gösteriyorum.


![video](https://youtu.be/mGmNKYOXtxY)


### Bölüm 2: SeedSigner'ınızı test etme


SeedSigner'ımı kullanmadan önce, kötü niyetli bir şey yapmadığından emin olmak için birkaç test yaptım. Bu adımı da paylaşabileceğimi düşündüm. SeedSigner'ınızın doğru Wallet'ü (xpub) dışa aktardığını nasıl doğrulayacağınızı, SeedSigners zar atma matematiğini nasıl doğrulayacağınızı ve SeedSigners bip-85 alt tohumlarını nasıl doğrulayacağınızı burada bulabilirsiniz.


![video](https://youtu.be/34W1IyTyXZE)


### Bölüm 3: SeedSigner Sparrow wallet ile nasıl kullanılır (masaüstü)


SeedSigner tohum üretme ve Bitcoin işlemlerini imzalama yeteneğine sahiptir. Ancak tek başına işlem oluşturma yeteneğine sahip değildir. SeedSigner'ınızla birlikte bir Wallet "koordinatörü" kullanmanız gerekir. Sparrow wallet'yı SeedSigner'ınızla bu şekilde kullanabilirsiniz:


![video](https://youtu.be/IQb8dh-VTOg)


Bölüm 4: SeedSigner Blue Wallet (mobil) ile nasıl kullanılır?


SeedSigner tohum üretme ve Bitcoin işlemlerini imzalama yeteneğine sahiptir. Ancak tek başına işlem oluşturma yeteneğine sahip değildir. SeedSigner'ınızla birlikte bir Wallet "koordinatörü" kullanmanız gerekir. Blue Wallet'in SeedSigner ile nasıl kullanılacağı aşağıda açıklanmıştır:


![video](https://youtu.be/x0Ee35Ct0r4)


Şimdilik tüm SeedSigner kılavuzları bunlar! Eksik olduğunu düşündüğünüz bir şey varsa bana bildirin. Bunlar potansiyel videolar için listemde:



- SeedSigner genel incelemesi. İmzalama cihazı için iyi bir seçim mi? Artıları/eksileri?
- Bip-85 SeedSigner ile nasıl kullanılır?
- SeedSigner ile nasıl Jim amca olunur?


Bunları değerli mi buldunuz? Gelecekteki videoların finansmanına yardımcı olmak için bir ipucu göndermeyi düşünün:

https://www.southernbitcoiner.com/donate/