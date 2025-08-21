---
name: PlanB Network'e Podcast Ekleme
description: PlanB Network'e yeni bir podcast nasıl eklenir?
---
![podcast](assets/cover.webp)


PlanB'nin misyonu, Bitcoin hakkında mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerikler açık kaynaklıdır ve GitHub'da barındırılarak herkesin platformu zenginleştirmeye katılmasına olanak tanır.


PlanB Network sitesine bir Bitcoin podcast'i eklemek ve programınızın görünürlüğünü artırmak istiyor ama nasıl yapacağınızı bilmiyor musunuz? Bu eğitim tam size göre!

![podcast](assets/01.webp)


- İlk olarak, bir GitHub hesabınızın olması gerekir. Nasıl oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB'nin verilere adanmış GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) `resources/podcasts/` bölümüne gidin:

![podcast](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![podcast](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![podcast](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![podcast](assets/05.webp)


- Podcast'iniz için bir klasör oluşturun. Bunu yapmak için, `Dosyanızı adlandırın...` kutusuna podcast'inizin adını küçük harflerle ve boşluk yerine tire koyarak yazın. Örneğin, programınızın adı "Super Podcast Bitcoin" ise, `super-podcast-Bitcoin` yazmalısınız:

![podcast](assets/06.webp)


- Klasörün oluşturulduğunu doğrulamak için, aynı kutuya podcast adınızdan sonra bir eğik çizgi eklemeniz yeterlidir, örneğin: `super-podcast-Bitcoin/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![podcast](assets/07.webp)


- Bu klasörde `podcast.yml` adında ilk YAML dosyasını oluşturacaksınız:

![podcast](assets/08.webp)


- Bu şablonu kullanarak bu dosyayı podcast'inizle ilgili bilgilerle doldurun:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


İşte her bir alan için doldurulması gereken ayrıntılar:



- `name`**: Podcast'inizin adını belirtin.
- `host`**: Konuşmacıların veya podcast sunucusunun adlarını veya takma adlarını listeleyin. Her isim virgülle ayrılmalıdır.
- `language`**: Podcast'inizde konuşulan dilin dil kodunu belirtin. Örneğin, İngilizce için `en`, İtalyanca için `it`...



- `bağlantılar`**: İçeriğinize bağlantılar sağlayın. İki seçeneğiniz var:
 - podcast`: podcast'inizin bağlantısı,
 - `twitter`: podcast'in veya onu üreten kuruluşun Twitter profiline bağlantı,
 - `web sitesi`: podcast'in veya onu üreten kuruluşun web sitesine bağlantı.



- `açıklama`**: Podcast'inizi tanımlayan kısa bir paragraf ekleyin. Açıklama, `language:` alanında belirtilenle aynı dilde olmalıdır.



- `tags`**: Podcast'inizle ilişkili iki etiket ekleyin. Örnekler:
    - `Bitcoin`
    - `teknoloji`
    - `ekonomi`
    - "eğitim"...



- `contributors`**: Eğer varsa katılımcı kimliğinizi belirtin.


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- Bu dosyada değişiklik yapmayı tamamladığınızda, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![podcast](assets/10.webp)


- Değişiklikleriniz için bir başlık ve kısa bir açıklama ekleyin:

![podcast](assets/11.webp)


- Green `Değişiklik öner` düğmesine tıklayın:

![podcast](assets/12.webp)


- Daha sonra tüm değişikliklerinizi özetleyen bir sayfaya ulaşacaksınız:

![podcast](assets/13.webp)


- Sağ üstteki GitHub profil resminize ve ardından `Repolarınız` seçeneğine tıklayın:

![podcast](assets/14.webp)


- PlanB Ağ deposundan Fork'inizi seçin:

![podcast](assets/15.webp)


- Pencerenin üst kısmında yeni dalınızla birlikte bir bildirim görmelisiniz. Muhtemelen `patch-1` olarak adlandırılmıştır. Üzerine tıklayın:

![podcast](assets/16.webp)


- Şu anda çalışma şubenizdesiniz:

![podcast](assets/17.webp)


- Sources/podcast/` klasörüne geri dönün ve önceki işlemde oluşturduğunuz podcast klasörünü seçin: ![podcast](assets/18.webp)
- Podcast klasörünüzde, `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![podcast](assets/19.webp)


- Bu yeni klasöre `assets` adını verin ve sonuna bir eğik çizgi `/` ekleyerek oluşturulduğunu onaylayın:

![podcast](assets/20.webp)


- Bu `assets` klasöründe `.gitkeep` adında bir dosya oluşturun:

![podcast](assets/21.webp)


- Değişiklikleri ilet...` düğmesine tıklayın:

![podcast](assets/22.webp)


- İşlem başlığını varsayılan olarak bırakın ve `Doğrudan patch-1 dalına işle` kutusunun işaretli olduğundan emin olun, ardından `Değişiklikleri işle` seçeneğine tıklayın:

![podcast](assets/23.webp)


- Assets` klasörüne geri dönün:

![podcast](assets/24.webp)


- Önce `Dosya ekle` düğmesine, ardından `Dosya yükle` düğmesine tıklayın:

![podcast](assets/25.webp)


- Yeni bir sayfa açılacaktır. Podcast logonuzu alana sürükleyip bırakın. Bu görüntü PlanB Network sitesinde görüntülenecektir:

![podcast](assets/26.webp)


- Dikkatli olun, web sitemize en iyi şekilde uyması için görsel kare olmalıdır:

![podcast](assets/27.webp)


- Görüntü yüklendikten sonra, `Doğrudan patch-1 dalına aktar` kutusunun işaretli olduğunu doğrulayın ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![podcast](assets/28.webp)


- Dikkatli olun, resminiz `logo` olarak adlandırılmalı ve `.webp` formatında olmalıdır. Bu nedenle tam dosya adı şöyle olmalıdır: logo.webp` olmalıdır:

![podcast](assets/29.webp)


- Assets` klasörünüze dönün ve `.gitkeep` ara dosyasına tıklayın:

![podcast](assets/30.webp)


- Dosyanın üzerine geldiğinizde, sağ üstteki üç küçük noktaya ve ardından `Dosyayı sil` seçeneğine tıklayın:

![podcast](assets/31.webp)


- Hala aynı çalışma dalında olduğunuzu doğrulayın, ardından `Değişiklikleri ilet` düğmesine tıklayın:

![podcast](assets/32.webp)


- İşleminize bir başlık ve açıklama ekleyin, ardından `Değişiklikleri ilet` seçeneğine tıklayın:

![podcast](assets/33.webp)


- Deponuzun kök dizinine geri dönün:

![podcast](assets/34.webp)


- Şubenizde değişiklik yapıldığını belirten bir mesaj görmelisiniz. Karşılaştır ve çekme isteği düğmesine tıklayın:

![podcast](assets/35.webp)


- PR'ınıza net bir başlık ve açıklama ekleyin:

![podcast](assets/36.webp)


- Çekme isteği oluştur` düğmesine tıklayın:

![podcast](assets/37.webp)

Tebrikler! Halkla İlişkileriniz başarıyla oluşturuldu. Şimdi bir yönetici bunu inceleyecek ve her şey yolundaysa PlanB Network'ün ana havuzuyla birleştirecek. Podcast'inizin birkaç gün sonra web sitesinde göründüğünü göreceksiniz.


Lütfen halkla ilişkilerinizin ilerleyişini takip ettiğinizden emin olun. Bir yönetici ek bilgi isteyen bir yorum bırakabilir. PR'niz onaylanmadığı sürece, PlanB Network GitHub deposundaki `Pull requests` sekmesinde görüntüleyebilirsiniz:

![podcast](assets/38.webp)

Değerli katkılarınız için çok teşekkür ederiz! :)