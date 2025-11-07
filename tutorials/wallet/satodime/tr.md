---
name: Satodime
description: Mobil uygulama ile Satodime'ı nasıl kullanacağınızı öğrenin
---
![cover](assets/cover.webp)



Bu kılavuz sizi Satodime mobil uygulamasının kurulumu, yapılandırılması ve kullanımına yönlendirir. Kartınıza nasıl sahip olacağınızı, kasa oluşturmayı, para eklemeyi, mührü açmayı ve özel anahtarlarınızı kurtarmayı öğreneceksiniz. Eklerde kaynaklar, en iyi uygulamalar ve teknik açıklamalar yer almaktadır.



## Giriş



**Satochip](https://satochip.io/fr/)** tarafından geliştirilen *Satodime**, Bitcoin'ı somut ve basit bir şekilde saklamak için güvenli bir taşıyıcı karttır. Üçüncü bir tarafa bağlı kalmadan özel anahtarlarınız üzerinde tam kontrole sahip olduğunuz, kendi kendini koruyan bir wallet donanımı görevi görür. Açık kaynaklı ve EAL6+ sertifikalı olan bu ürün, üç adede kadar bağımsız kasayı destekler.



### Ürün arka planı



Satodime, bir **carte au porteur, önceden kayıt veya kimlik tespiti gerekmeksizin fiziksel olarak sahip olan kişiye aittir**. Güvenli, taşınabilir bitcoin depolama ihtiyacını karşılayarak, kartı elinde bulunduran herkesin onu kullanmasına veya kasaları ele geçirmek veya mühürlerini açmak için mobil uygulama aracılığıyla tarayarak bitcoin transfer etmesine olanak tanır. Kağıt banknottan farklı olarak, özel anahtarları mühürlemek için güvenli bir çip kullanır ve bu anahtarlar yalnızca mühür açıldıktan sonra ortaya çıkar, bu da kartı sahipliğin fiziksel sahiplikle belirlendiği nakit paraya benzer hale getirir. Hediye olarak bitcoin vermek için ideal olan bu kart, bitcoinlerin elden ele güvenli bir şekilde aktarılmasını kolaylaştırırken, mobil uygulama da erişilebilir akıllı telefon etkileşimi için NFC'den yararlanıyor.





- Güvenlik**: Kurcalamaya dayanıklı çipte üretilen ve saklanan özel anahtarlar; görünür durum (mühürlü, mühürsüz, boş).
- Özellikler**: Doğrudan uygulama üzerinden bitcoin satın alın (Paybis ortağı); Mainnet ve Testnet'ü yönetin.
- Açık kaynak**: AGPLv3 lisansı altındaki kod, GitHub'da doğrulanabilir.



### Sürekli evrim



Uygulama düzenli olarak gelişmektedir. Güncellemeler için Satochip web sitesini veya mağazalarını kontrol edin. Örneğin, yeni blok zincirleri veya satın alma işlevleri eklenebilir. Devam eden gelişmeler için [Satochip GitHub] (https://github.com/Toporin/Satodime-Applet) adresini kontrol edin.



## 1. Ön Koşullar



Satodime** ile çalışmaya başlamadan önce, aşağıdaki öğelere sahip olduğunuzdan emin olun:





- Uyumlu akıllı telefon**: NFC özellikli Android veya iOS cihaz.
- Satodime** kartı: Yeni veya başlatılmamış.
- İnternet bağlantısı**: Uygulamayı indirmek için.
- Temel bilgi**: Özel/genel anahtarları ve kayıp risklerini (geri döndürülemez) anlama.
- Güvenli ortam**: Mühür açıldıktan sonra özel anahtarları kaydetmek için güvenli bir yer (kağıt, metal; asla dijital değil).



## 2. Kurulum





- Başvuruyu indirin** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Dolandırıcılığı önlemek için geliştiriciyi (Satochip) kontrol edin.
 - Satodime **açık kaynaklıdır**. Kaynak kodu : [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).





- Uygulamayı yükleyin ve başlatın**: Gerekirse telefonunuzda NFC'yi etkinleştirin.



![image](assets/fr/01.webp)



## 3. İlk yapılandırma



### 3.1 Uygulamayı başlatın ve tarayın



Uygulamayı açın ve sihirbazı takip edin. Satodime kartını telefonunuzun NFC okuyucusuna yerleştirin (genellikle arka tarafta). Sabit bir bağlantı sağlamak için işlem boyunca basılı tutun.





- NFC çalışmazsa, telefonunuzun ayarlarını kontrol edin.
- Kadeh kaldırılarak başarı teyit edilir: "Başarılı okuma".



![image](assets/fr/02.webp)



Genel bir kural olarak, **aşağıdaki tüm işlemler Satodime kartının taranarak onaylanmasını gerektirecektir**



### 3.2 Kartın ele geçirilmesi (*Ownership*)



İlk kullanımda, kartı güvence altına almak için kartın sahibi olun:





- Uygulamada "*Ownership'i Al*" seçeneğine tıklayın.
- İşlemi onaylayın: bu işlem benzersiz bir sahip anahtarı oluşturur.
- Değişiklikleri uygulamak için haritayı tekrar tarayın.
- Uyarı**: Bu adım geri döndürülemez. Lütfen [mülkiyet* ile ilgili makaleye] (https://satochip.io/satodime-ownership-explained/) bakınız.



![image](assets/fr/03.webp)




## 4. Güvenli bir ortam yaratın



Satodime en fazla 3 kasayı destekler. Bitcoin saklamak için bir tane oluşturun:





- Boş bir kasa seçin (örn. Kasa 01).
- Blok zincirini seçin (Bitcoin).
- "*Create & Seal*" üzerine tıklayın.
- Kartı generate'e tarayın ve özel anahtarı mühürleyin (mühür açılana kadar bilinmez).
- Tebrikler**: Kasanız artık mühürlendi ve para almaya hazır.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Fon ekleyin



Mühürlendikten sonra kasayı bitcoinlerle doldurun:





- Kasayı seçin.
- "*Fon ekle*" üzerine tıklayın.
- Genel adresi kopyalayın veya QR kodunu tarayın.
- Başka bir wallet'dan para gönderin.
- Blok zincirinde onaylandıktan sonra bakiyeyi kontrol edin.
- Satın alma seçeneği: Doğrudan Paybis (Visa, Mastercard, vb.) aracılığıyla satın almak için "*Satın Al*" seçeneğine tıklayın. Geçerli ücretler.



![image](assets/fr/06.webp)



## 6. Kasanın mührünü açma



Özel anahtara erişmek ve fonları başka bir yere aktarmak için kasanın mührünü açın:





- Mühürlü kasayı seçin.
- "Mührü Aç" üzerine tıklayın.
- Uyarıyı onaylayın: bu işlem geri döndürülemez.
- Mührü açmak için kartı tarayın.
- Kasa "*Mühürsüz*" olarak ayarlanmıştır; özel anahtar artık görüntülenebilir/dışa aktarılabilir.
- Uyarı**: Mühür açıldıktan sonra özel anahtara erişilebilir. Birisi akıllı telefonunuzu ele geçirirse, bu anahtara erişebilir ve böylece kasanızdaki fonları geri alabilir (geri döndürülemez).



![image](assets/fr/07.webp)



## 7. Özel anahtarı kurtarma



Mührü açtıktan sonra, anahtarı başka bir wallet'da kullanmak üzere dışa aktarın:





- Güvenli bir ortamda olduğunuzdan emin olun.
- "*Özel anahtarı göster*" üzerine tıklayın.
- Formatı seçin: Eski, SegWit, WIF, vb.
- Anahtarı kopyalayın veya QR kodunu tarayın.
- Güvenlik**: Özel anahtarınızı asla paylaşmayın. Çevrimdışı olarak saklayın.
- Fon yönetimi ile uyumlu bir wallet yazılım programına aktarın (örneğin Sparrow Wallet veya Electrum).



![image](assets/fr/08.webp)





## 8. Bagajı sıfırla



Kasanın sıfırlanması, ilgili özel anahtarı geri döndürülemez şekilde siler. Başka bir deyişle, özel anahtarınızın bir kopyasını güvence altına almadıysanız veya başka bir wallet'ya aktarmadıysanız, kasayı sıfırlamak içindeki fonların geri döndürülemez şekilde kaybolmasına neden olacaktır.



![image](assets/fr/09.webp)



Bagajın sıfırlanması yuvayı boşaltır ve yeni bir bagaj için hazır hale getirir.



## 9. Mülkiyet devri



Örneğin Satodime aracılığıyla bitcoin sunmak için şunları yapmanız gerekir:




- Kartın sahipliğini üstlenin,
- Bir Bitcoin kasası oluşturun,
- Oraya transfer et,
- Kart sahipliğini transfer edin: kartı tarayan bir sonraki kişi kartın sahibi olur,
- Satodime kartını seçtiğiniz kişiye verin ve onu uygulamayı indirmeye davet edin ve ardından kartı tarayarak sahipliğini alın - ve böylece üzerinde 'depolanan' bitcoinlere erişin.



![image](assets/fr/10.webp)




## EKLER



### A1. En iyi uygulamalar



Güvenli bir şekilde **Satodime** kullanmak için :





- Kartı güvence altına alın**: Nakit gibi davranın; kayıp = sahibi değilse para kaybı.
- Anahtar yedekleme**: Mührü açtıktan sonra, özel anahtarları güvenli bir fiziksel ortama kaydedin. Asla dijital değil.
- Durumu kontrol edin**: Kart sahipliğini ve kasaların mühürlü/mühürsüz durumunu onaylamak için her zaman tarama yapın.
- Gizlilik**: Yeni adresler kullanın; transferler için merkezi değişimlerden kaçının.
- Güncellemeler**: Uygulamayı mağazalar aracılığıyla güncel tutun.
- Kurtarma**: Kart kaybolur ancak sahiplenilirse, fonlar blok zincirindedir; mühürsüzse özel anahtarı kullanın.



### A2. Ek kaynaklar



Satodime'a özel :




- [Satodime ürünü](https://satochip.io/fr/product/satodime/)
- [Mobil Rehber](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Akademi] (https://planb.academy/) kendi kendine saklama, özel anahtarlar vb. hakkında eğitimler için.



**Kurtarma cümlenizi kaydedin** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Satochip (markanın ilk ürünü) hakkında eğitim :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tohum bekçisi eğitimleri:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Satochip Hakkında



**Resmi bağlantılar** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Destek: info@satochip.io



**Satochip** bitcoin ve diğer kripto para birimlerini yönetmek ve saklamak için donanım ve yazılım çözümleri geliştiren Belçikalı bir şirkettir. Amiral gemisi ürünü olan Satochip donanım wallet, EAL6+ sertifikalı secure element ile donatılmış bir NFC kartıdır. Bir anımsatıcı ifade ve sır yöneticisi olan Seedkeeper ve bir taşıyıcı kart olan Satodime ile tamamlanan Satochip, kullanıcıların ihtiyaçlarına göre uyarlanmış kapsamlı bir ürün yelpazesi sunmaktadır. Açık kaynak yazılımla çalışan cihazları, Bitcoin'da güvenliği demokratikleştirmeyi amaçlıyor.