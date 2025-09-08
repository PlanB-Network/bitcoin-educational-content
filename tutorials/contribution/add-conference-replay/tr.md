---
name: Konferans Tekrarı Ekleme
description: PlanB Network'e konferans tekrarı nasıl eklenir?
---
![conference](assets/cover.webp)


PlanB'nin misyonu, Bitcoin hakkında mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılarak herkesin platformun zenginleşmesine katkıda bulunmasına olanak tanır.


Bitcoin konferansınızın tekrarını PlanB Network sitesine eklemek ve bu etkinliğe görünürlük kazandırmak istiyor ama nasıl yapacağınızı bilmiyor musunuz? Bu eğitim tam size göre!


Ancak, gelecekte gerçekleşecek bir konferans eklemek istiyorsanız, siteye yeni bir etkinliğin nasıl ekleneceğini açıkladığımız bu diğer öğreticiyi okumanızı tavsiye ederim.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- İlk olarak, GitHub'da bir hesabınızın olması gerekir. Nasıl hesap oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB'nin verilere adanmış GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) `resources/conference/` bölümüne gidin:

![conference](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![conference](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve bu da orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![conference](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![conference](assets/05.webp)


- Konferansınız için bir klasör oluşturun. Bunu yapmak için, `Dosyanızı adlandırın...` kutusuna konferansınızın adını boşluk yerine tire ile küçük harflerle yazın. Örneğin, konferansınızın adı "Paris Bitcoin Konferansı" ise, `paris-Bitcoin-conference` yazmalısınız. Ayrıca konferansınızın yılını da ekleyin, örneğin: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- Klasörün oluşturulduğunu doğrulamak için, aynı kutuya adınızdan sonra bir eğik çizgi not edin, örneğin: `paris-Bitcoin-conference-2024/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![conference](assets/07.webp)


- Bu klasörde `conference.yml` adında ilk YAML dosyasını oluşturacaksınız:

![conference](assets/08.webp)

Bu şablonu kullanarak bu dosyayı konferansınızla ilgili bilgilerle doldurun:

```yaml
year:
name:
project:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Kuruluşunuz için henüz bir "*proje*" tanımlayıcınız yoksa, bu diğer öğreticiyi izleyerek ekleyebilirsiniz.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Bu dosyada değişiklik yapmayı tamamladığınızda, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![conference](assets/10.webp)


- Değişiklikleriniz için bir başlık ve kısa bir açıklama ekleyin:

![conference](assets/11.webp)


- Green `Değişiklik öner` düğmesine tıklayın:

![conference](assets/12.webp)


- Daha sonra tüm değişikliklerinizi özetleyen bir sayfaya ulaşacaksınız:

![conference](assets/13.webp)


- Sağ üstteki GitHub profil resminize ve ardından `Repolarınız` seçeneğine tıklayın:

![conference](assets/14.webp)


- PlanB Ağ deposundan Fork'nizi seçin:

![conference](assets/15.webp)


- Pencerenin üst kısmında yeni dalınızla birlikte bir bildirim görmelisiniz. Muhtemelen `patch-1` olarak adlandırılmıştır. Üzerine tıklayın:

![conference](assets/16.webp)


- Şu anda çalışma şubenizdesiniz:

![conference](assets/17.webp)


- Sources/conference/` klasörüne dönün ve bir önceki işlemde oluşturduğunuz konferansınızın klasörünü seçin:

![conference](assets/18.webp)


- Konferansınızın klasöründe, `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![conference](assets/19.webp)


- Bu yeni klasöre `assets` adını verin ve sonuna bir eğik çizgi `/` koyarak oluşturulduğunu onaylayın:

![conference](assets/20.webp)


- Bu `assets` klasöründe `.gitkeep` adında bir dosya oluşturun:

![conference](assets/21.webp)


- Değişiklikleri ilet...` düğmesine tıklayın:

![conference](assets/22.webp)


- İşlem başlığını varsayılan olarak bırakın ve `Doğrudan patch-1 dalına işle` kutusunun işaretli olduğundan emin olun, ardından `Değişiklikleri işle` seçeneğine tıklayın:

![conference](assets/23.webp)


- Assets` klasörüne geri dönün:

![conference](assets/24.webp)


- Önce `Dosya ekle` düğmesine, ardından `Dosya yükle` düğmesine tıklayın:

![conference](assets/25.webp)


- Yeni bir sayfa açılacaktır. Konferansınızı temsil eden ve PlanB Network sitesinde görüntülenecek bir resmi sürükleyip bırakın: ![conference](assets/26.webp)
- Bir logo, bir küçük resim veya hatta bir poster olabilir:

![conference](assets/27.webp)


- Görüntü yüklendikten sonra, `Doğrudan patch-1 dalına aktar` kutusunun işaretli olduğunu kontrol edin ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![conference](assets/28.webp)


- Dikkatli olun, resminiz `thumbnail` olarak adlandırılmalı ve `.webp` formatında olmalıdır. Bu nedenle tam dosya adı şöyle olmalıdır: `thumbnail.webp` olmalıdır:

![conference](assets/29.webp)


- Assets` klasörünüze dönün ve `.gitkeep` ara dosyasına tıklayın:

![conference](assets/30.webp)


- Dosyanın üzerine geldiğinizde, sağ üst köşedeki 3 küçük noktaya ve ardından `Dosyayı sil` seçeneğine tıklayın:

![conference](assets/31.webp)


- Hala aynı çalışma dalında olduğunuzu doğrulayın, ardından `Değişiklikleri ilet` düğmesine tıklayın:

![conference](assets/32.webp)


- İşleminize bir başlık ve açıklama ekleyin, ardından `Değişiklikleri ilet` seçeneğine tıklayın:

![conference](assets/33.webp)


- Konferans klasörünüze geri dönün:

![conference](assets/34.webp)


- Önce `Dosya ekle` düğmesine, ardından `Yeni dosya oluştur` düğmesine tıklayın:

![conference](assets/35.webp)


- Ana dilinizin göstergesi ile adlandırarak yeni bir markdown (.md) dosyası oluşturun. Bu dosya konferansınızın tekrarları için kullanılacaktır. Örneğin, konferansların açıklamalarını İngilizce yazmak istersem, bu dosyayı en.md olarak adlandıracağım:

![conference](assets/36.webp)


- Konferansınızın yapılandırmasına uyarlayabileceğiniz bu şablonu kullanarak bu markdown dosyasını doldurun:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- Belgenizin başında, "önsöz" bölümünde, `name:` alanını konferansınızın adı ve tekrarların yılı ile doldurun. Açıklama:` alanına, etkinliğinizin kısa bir açıklamasını dosyanın dilinde yazın. Örneğin, `en.md` adlı bir dosya için açıklama İngilizce olmalıdır. PlanB Network ekibi, kendi modellerini kullanarak açıklamanızın çevirisiyle ilgilenecektir.
- Bir `#` ile işaretlenen birinci seviye başlıklar, konferansı sahnelere göre düzenlemek için kullanılır. Örneğin, ana sahne için `# Ana Sahne` ve atölye çalışmalarına ayrılmış bir sahne için `# Atölye Odası`.



- Çift `##` ile işaretlenen ikinci seviye başlıklar, farklı tekrar videolarını ayırmak için kullanılır. Konferanslar yarım gün boyunca kesintisiz olarak çekilmişse, örneğin `## Cuma sabahı` şeklinde belirtin. Konferanslar ayrı ayrı çekilmiş ve yayınlanmışsa, konferansı doğrudan ikinci seviye bir başlıkla adlandırın.



- Her ikinci seviye başlığın altına, ilgili tekrar videosuna bir bağlantı ekleyin. Sözdizimi şöyle olmalıdır: '![video](https://youtu.be/XXXXXXXXXXXX)`, `XXXXXXXXXXXXXX` yerine gerçek video bağlantısını yazın.



- Format izin veriyorsa (bireysel konferanslar), konuşmacıların adlarını ekleyebilirsiniz. Bunu yapmak için, `Konuşmacı:` alanını ve ardından konuşmacının adını veya takma adını video bağlantısının altına ekleyin. Birden fazla konuşmacı olması durumunda, her bir ismi virgülle ayırın, örneğin: `Konuşmacı: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Bu dosyada yaptığınız değişiklikler tamamlandığında, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![conference](assets/38.webp)


- Değişiklikleriniz için bir başlık ve kısa bir açıklama ekleyin:

![conference](assets/39.webp)


- Değişiklikleri ilet`e tıklayın:

![conference](assets/40.webp)


- Konferans klasörünüz şimdi aşağıdaki gibi görünmelidir:

![conference](assets/41.webp)


- Her şey sizi tatmin ediyorsa, Fork'unuzun köküne geri dönün:

![conference](assets/42.webp)


- Şubenizde değişiklik yapıldığını belirten bir mesaj görmelisiniz. Karşılaştır ve çekme isteği düğmesine tıklayın:

![conference](assets/43.webp)


- PR'ınız için net bir başlık ve açıklama ekleyin:

![conference](assets/44.webp)


- Çekme isteği oluştur` düğmesine tıklayın:

![conference](assets/45.webp)

Tebrikler! Halkla İlişkileriniz başarıyla oluşturuldu. Şimdi bir yönetici bunu inceleyecek ve her şey yolundaysa PlanB Network'ün ana havuzuyla birleştirecek. Konferansınızın tekrarlarının birkaç gün sonra web sitesinde göründüğünü göreceksiniz.


Lütfen halkla ilişkilerinizin ilerleyişini takip ettiğinizden emin olun. Bir yöneticinin ek bilgi isteyen bir yorum bırakması mümkündür. PR'niz onaylanmadığı sürece, PlanB Network'ün GitHub deposundaki `Pull requests' sekmesi altında görüntüleyebilirsiniz:

![conference](assets/46.webp)


Değerli katkılarınız için çok teşekkür ederiz! :)