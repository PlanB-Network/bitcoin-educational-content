---
name: Proje Ekleme
description: PlanB Network'e yeni bir proje eklenmesi nasıl teklif edilir?
---
![project](assets/cover.webp)


PlanB'nin misyonu, Bitcoin konusunda mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılmaktadır, bu da herkesin platformu zenginleştirmeye katılmasına olanak tanır.


PlanB Network sitesine yeni bir Bitcoin "projesi" eklemek ve şirketinize veya yazılımınıza görünürlük kazandırmak istiyor ancak nasıl yapacağınızı bilmiyor musunuz? Bu eğitim tam size göre!

![project](assets/01.webp)


- İlk olarak, bir GitHub hesabınızın olması gerekir. Nasıl hesap oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Kaynaklar/proje/` bölümündeki [PlanB'nin verilere ayrılmış GitHub deposu] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) adresine gidin:

![project](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![project](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve bu da orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![project](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![project](assets/05.webp)


- Şirketiniz için bir klasör oluşturun. Bunu yapmak için, `Dosyanızı adlandırın...` kutusuna şirketinizin adını boşluk yerine tire ile küçük harflerle yazın. Örneğin, şirketinizin adı "Bitcoin Baguette" ise, `Bitcoin-baguette` yazmalısınız:

![project](assets/06.webp)


- Klasörün oluşturulduğunu doğrulamak için, aynı kutuya adınızdan sonra bir eğik çizgi eklemeniz yeterlidir, örneğin: `Bitcoin-baguette/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![project](assets/07.webp)


- Bu klasörde `project.yml` adında ilk YAML dosyasını oluşturacaksınız:

![project](assets/08.webp)


- Bu şablonu kullanarak bu dosyayı şirketinizle ilgili bilgilerle doldurun:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


Her bir anahtar için doldurulması gerekenler aşağıda verilmiştir:


- `name`: Şirketinizin adı (zorunlu);
- `Address` : İşletmenizin konumu (isteğe bağlı);
- `language` : İşletmenizin faaliyet gösterdiği ülkeler veya desteklenen diller (isteğe bağlı);
- `links` : İşletmenizin çeşitli resmi bağlantıları (isteğe bağlı);
- `tags` : İşletmenizi niteleyen 2 terim (zorunlu);
- `category` : Aşağıdaki seçenekler arasından işletmenizin faaliyet gösterdiği alanı en iyi tanımlayan kategori:
 - "Wallet",
 - "altyapı",
 - "Exchange",
 - "eğitim",
 - `hizmet`,
 - "topluluklar",
 - `konferans`,
 - `gizlilik`,
 - "yatırım",
 - `node`,
 - "Mining",
 - "Haberler",
 - "üretici".


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![project](assets/09.webp)


- Bu dosyada değişiklik yapmayı tamamladığınızda, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![project](assets/10.webp)


- Kısa bir açıklama ile birlikte değişiklikleriniz için bir başlık ekleyin:

![project](assets/11.webp)


- Green `Değişiklik öner` düğmesine tıklayın:

![project](assets/12.webp)


- Daha sonra tüm değişikliklerinizi özetleyen bir sayfaya ulaşacaksınız:

![project](assets/13.webp)


- Sağ üstteki GitHub profil resminize ve ardından `Repolarınız` seçeneğine tıklayın:

![project](assets/14.webp)


- PlanB Ağ deposundan Fork'inizi seçin:

![project](assets/15.webp)


- Pencerenin üst kısmında yeni dalınızla birlikte bir bildirim görmelisiniz. Muhtemelen `patch-1` olarak adlandırılmıştır. Üzerine tıklayın:

![project](assets/16.webp)


- Artık çalışma dalınızdasınız (**önceki değişikliklerinizle aynı dalda olduğunuzdan emin olun, bu önemlidir!**):

![project](assets/17.webp)


- Resources/projects/` klasörüne geri dönün ve önceki işlemde oluşturduğunuz işletmenizin klasörünü seçin:

![project](assets/18.webp)


- İşletmenizin klasöründe, `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![project](assets/19.webp)


- Bu yeni klasöre `assets` adını verin ve sonuna bir eğik çizgi `/` koyarak oluşturulduğunu onaylayın:

![project](assets/20.webp)


- Bu `assets` klasöründe `.gitkeep` adında bir dosya oluşturun:

![project](assets/21.webp)


- Değişiklikleri ilet...` düğmesine tıklayın:

![project](assets/22.webp)


- Taahhüt başlığını varsayılan olarak bırakın ve `Doğrudan patch-1 dalına taahhüt et` kutusunun işaretli olduğundan emin olun, ardından `Değişiklikleri taahhüt et` seçeneğine tıklayın: ![project](assets/23.webp)
- Varlıklar klasörüne geri dönün:

![project](assets/24.webp)


- Önce `Dosya ekle` düğmesine, ardından `Dosya yükle` düğmesine tıklayın:

![project](assets/25.webp)


- Yeni bir sayfa açılacaktır. Şirketinizin veya yazılımınızın bir görüntüsünü alana sürükleyip bırakın. Bu resim PlanB Network sitesinde görüntülenecektir:

![project](assets/26.webp)


- Logo veya bir simge olabilir:

![project](assets/27.webp)


- Görüntü yüklendikten sonra, `Doğrudan patch-1 dalına aktar` kutusunun işaretli olduğunu doğrulayın ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![project](assets/28.webp)


- Dikkatli olun, resminiz kare olmalı, `logo` olarak adlandırılmalı ve `.webp` formatında olmalıdır. Bu nedenle tam dosya adı şöyle olmalıdır: logo.webp` olmalıdır:

![project](assets/29.webp)


- Assets` klasörünüze geri dönün ve `.gitkeep` ara dosyasına tıklayın:

![project](assets/30.webp)


- Dosyanın üzerine geldiğinizde, sağ üstteki üç küçük noktaya ve ardından `Dosyayı sil` seçeneğine tıklayın:

![project](assets/31.webp)


- Hala aynı çalışma dalında olduğunuzu doğrulayın, ardından `Değişiklikleri ilet` düğmesine tıklayın:

![project](assets/32.webp)


- İşleminize bir başlık ve açıklama ekleyin, ardından `Değişiklikleri ilet` seçeneğine tıklayın:

![project](assets/33.webp)


- Şirketinizin klasörüne geri dönün:

![project](assets/34.webp)


- Önce `Dosya ekle` düğmesine, ardından `Yeni dosya oluştur` düğmesine tıklayın:

![project](assets/35.webp)


- Ana dilinizin göstergesi ile adlandırarak yeni bir YAML dosyası oluşturun. Bu dosya projenin açıklaması için kullanılacaktır. Örneğin, açıklamamı İngilizce yazmak istersem, bu dosyaya `en.yml` adını vereceğim:

![project](assets/36.webp)


- Bu şablonu kullanarak bu YAML dosyasını doldurun:

```yaml
description: |

contributors:
-
```



- Contributors` anahtarı için, eğer varsa PlanB Network'e katkıda bulunan tanımlayıcınızı ekleyebilirsiniz. Eğer yoksa, bu alanı boş bırakın.
- Açıklama anahtarı için, şirketinizi veya yazılımınızı tanımlayan kısa bir paragraf eklemeniz yeterlidir. Açıklama, dosya adıyla aynı dilde olmalıdır. Bu açıklamayı sitede desteklenen tüm dillere çevirmeniz gerekmez, çünkü PlanB ekipleri bunu kendi modellerini kullanarak yapacaktır. Örneğin, dosyanız şu şekilde görünebilir:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- Değişiklikleri ilet düğmesine tıklayın:

![project](assets/38.webp)


- Doğrudan yama-1 dalına aktar` kutusunun işaretli olduğundan emin olun, bir başlık ekleyin ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![project](assets/39.webp)


- Şirket klasörünüz artık aşağıdaki gibi görünmelidir:

![project](assets/40.webp)


- Her şey sizi tatmin ediyorsa, Fork'nizin köküne geri dönün:

![project](assets/41.webp)


- Şubenizde değişiklik yapıldığını belirten bir mesaj görmelisiniz. Karşılaştır ve çekme isteği düğmesine tıklayın:

![project](assets/42.webp)


- PR'ınıza net bir başlık ve açıklama ekleyin:

![project](assets/43.webp)


- Çekme isteği oluştur` düğmesine tıklayın:

![project](assets/44.webp)

Tebrikler! Halkla İlişkileriniz başarıyla oluşturuldu. Şimdi bir yönetici bunu inceleyecek ve her şey yolundaysa PlanB Network'ün ana deposuna entegre edecektir. Proje profilinizin birkaç gün sonra web sitesinde göründüğünü göreceksiniz.


Halkla ilişkilerinizin ilerleyişini takip ettiğinizden emin olun. Bir yönetici ek bilgi isteyen bir yorum bırakabilir. PR'niz onaylanmadığı sürece, PlanB Network GitHub deposundaki `Pull requests` sekmesinde ona danışabilirsiniz:

![project](assets/45.webp)

Değerli katkılarınız için çok teşekkür ederiz! :)