---
name: PlanB Ağına Kitap Ekleme
description: PlanB Network'e yeni bir kitap nasıl eklenir?
---
![book](assets/cover.webp)


PlanB'nin misyonu, Bitcoin hakkında mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılarak herkesin platformun zenginleştirilmesine katkıda bulunmasına olanak tanır.


**PlanB Network sitesine Bitcoin ile ilgili bir kitap eklemek ve çalışmanızın görünürlüğünü artırmak istiyor ama nasıl yapacağınızı bilmiyor musunuz? Bu eğitim tam size göre!

![book](assets/01.webp)


- İlk olarak, bir GitHub hesabınızın olması gerekir. Nasıl hesap oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB'nin verilere adanmış GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) `resources/books/` bölümüne gidin:

![book](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![book](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![book](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![book](assets/05.webp)


- Kitabınız için bir klasör oluşturun. Bunu yapmak için, `Dosyanızı adlandırın...` kutusuna kitabınızın adını boşluk yerine tire ile küçük harflerle yazın. Örneğin, kitabınızın adı "*My Bitcoin Book*" ise, `my-Bitcoin-book` yazmalısınız:

![book](assets/06.webp)


- Klasörün oluşturulduğunu doğrulamak için, aynı kutuya kitap adınızdan sonra bir eğik çizgi eklemeniz yeterlidir, örneğin: `my-Bitcoin-book/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![book](assets/07.webp)


- Bu klasörde, `book.yml` adında ilk YAML dosyasını oluşturacaksınız:

![book](assets/08.webp)


- Bu şablonu kullanarak bu dosyayı kitabınızla ilgili bilgilerle doldurun:


```yaml
author:
level:
tags:
-
-
```


İşte her bir alan için doldurulması gereken ayrıntılar:


- `author`**: Kitabın yazarının adını belirtin.
- `seviye`**: Kitabı iyi okuyabilmek ve anlayabilmek için gerekli seviyeyi belirtiniz. Aşağıdakiler arasından bir seviye seçin:
 - `başlangıç`
 - `intermediate`
- `ileri` - `uzman`
- `etiketler`**: Kitabınızla ilgili iki veya üç etiket ekleyin. Örneğin:
    - `Bitcoin`
    - `tarih`
    - `teknoloji`
    - `ekonomi`
    - "eğitim"...


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Bu dosyada değişiklik yapmayı tamamladığınızda, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![book](assets/10.webp)


- Değişiklikleriniz için bir başlık ve kısa bir açıklama ekleyin:

![book](assets/11.webp)


- Green `Değişiklik öner` düğmesine tıklayın:

![book](assets/12.webp)


- Daha sonra tüm değişikliklerinizi özetleyen bir sayfaya ulaşacaksınız:

![book](assets/13.webp)


- Sağ üstteki GitHub profil resminize ve ardından `Repolarınız` seçeneğine tıklayın:

![book](assets/14.webp)


- PlanB Ağ deposundan Fork'inizi seçin:

![book](assets/15.webp)


- Pencerenin üst kısmında yeni dalınızla birlikte bir bildirim görmelisiniz. Muhtemelen `patch-1` olarak adlandırılmıştır. Üzerine tıklayın:

![book](assets/16.webp)


- Şu anda çalışma şubenizdesiniz:

![book](assets/17.webp)


- Sources/books/` klasörüne geri dönün ve bir önceki işlemde oluşturduğunuz kitabınızın klasörünü seçin:

![book](assets/18.webp)


- Kitabınızın klasöründe, `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![book](assets/19.webp)


- Bu yeni klasöre `assets` adını verin ve sonuna bir eğik çizgi `/` koyarak oluşturulduğunu onaylayın:

![book](assets/20.webp)


- Bu `assets` klasöründe `.gitkeep` adında bir dosya oluşturun:

![book](assets/21.webp)


- Değişiklikleri ilet...` düğmesine tıklayın:

![book](assets/22.webp)


- İşlem başlığını varsayılan olarak bırakın ve `Doğrudan patch-1 dalına işle` kutusunun işaretli olduğundan emin olun, ardından `Değişiklikleri işle` seçeneğine tıklayın:

![book](assets/23.webp)


- Assets` klasörüne geri dönün:

![book](assets/24.webp)


- Önce `Dosya ekle` düğmesine, ardından `Dosya yükle` düğmesine tıklayın:

![book](assets/25.webp)


- Yeni bir sayfa açılacaktır. Kitabınızın kapak resmini bu alana sürükleyip bırakın. Bu resim PlanB Network sitesinde görüntülenecektir:

![book](assets/26.webp)


- Dikkatli olun, web sitemize en iyi şekilde uyum sağlamak için görsel kitap formatında olmalıdır, örneğin:

![book](assets/27.webp)


- Görüntü yüklendikten sonra, `Doğrudan patch-1 dalına aktar` kutusunun işaretli olduğundan emin olun ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Assets` klasörünüze geri dönün ve `.gitkeep` ara dosyasına tıklayın:

![book](assets/30.webp)


- Dosyanın üzerine geldiğinizde, sağ üstteki 3 küçük noktaya ve ardından `Dosyayı sil` seçeneğine tıklayın:

![book](assets/31.webp)


- Hala aynı çalışma dalında olduğunuzdan emin olun, ardından `Değişiklikleri ilet...` düğmesine tıklayın:

![book](assets/32.webp)


- İşleminize bir başlık ve açıklama ekleyin, ardından `Değişiklikleri ilet` seçeneğine tıklayın:

![book](assets/33.webp)


- Kitabınızın klasörüne geri dönün:

![book](assets/34.webp)


- Önce `Dosya ekle` düğmesine, ardından `Yeni dosya oluştur` düğmesine tıklayın:

![book](assets/35.webp)


- Kitabın dil göstergesi ile adlandırarak yeni bir YAML dosyası oluşturun. Bu dosya kitabın açıklaması için kullanılacaktır. Örneğin, açıklamamı İngilizce yazmak istersem, bu dosyaya `en.yml` adını vereceğim:

![book](assets/36.webp)


- Bu şablonu kullanarak bu YAML dosyasını doldurun:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


İşte her bir alan için doldurulması gereken ayrıntılar:


- `title`**: Kitabın adını tırnak içinde belirtin.
- `publication_year`**: Kitabın yayınlandığı yılı belirtin.
- `cover`**: Düzenlemekte olduğunuz YAML dosyasının diline uygun olarak kapak resmine karşılık gelen dosyanın adını belirtin. Örneğin, `en.yml` dosyasını düzenliyorsanız ve daha önce `cover_en.webp` başlıklı İngilizce kapak resmini eklediyseniz, bu alanda `cover_en.webp` ifadesini belirtmeniz yeterlidir.
- `açıklama`**: Kitabı tanımlayan kısa bir paragraf ekleyin. Açıklama, YAML dosyasının başlığında belirtilenle aynı dilde olmalıdır.
- `contributors`**: Eğer varsa katılımcı kimliğinizi ekleyin.


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml