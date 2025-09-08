---
name: Eğitim Araçları Ekleme
description: PlanB Network'e yeni eğitim materyalleri nasıl eklenir?
---
![event](assets/cover.webp)


PlanB'nin misyonu, Bitcoin konusunda mümkün olduğunca çok dilde önde gelen eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılmaktadır, bu da herkesin platformu zenginleştirmeye katılmasına olanak tanır.


PlanB Network, öğreticiler ve eğitimin ötesinde, Bitcoin hakkında herkesin erişebileceği çeşitli eğitim içeriklerinden oluşan geniş bir kütüphane de sunmaktadır [BET (_Bitcoin Educational Toolkit_) bölümünde] (https://planb.network/resources/bet). Bu veritabanı eğitici posterler, memler, mizahi propaganda posterleri, teknik diyagramlar, logolar ve kullanıcılar için diğer araçları içermektedir. Bu girişimin amacı, dünyanın dört bir yanında Bitcoin'i öğreten birey ve topluluklara gerekli görsel kaynakları sağlayarak onları desteklemektir.


Bu veritabanını zenginleştirmeye katılmak istiyor ama nasıl yapılacağını bilmiyor musunuz? Bu eğitim sizin için!


*Siteye entegre edilen tüm içeriğin haklardan arındırılmış olması veya kaynak dosyanın lisansına saygı gösterilmesi zorunludur. Ayrıca, PlanB Network'te yayınlanan tüm görseller [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) lisansı altında kullanıma sunulmaktadır.*

![event](assets/01.webp)


- İlk olarak, GitHub'da bir hesabınızın olması gerekir. Nasıl hesap oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB'nin verilere ayrılmış GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) `resources/bet/` bölümüne gidin:

![event](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![event](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve bu da orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![event](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![event](assets/05.webp)


- İçeriğiniz için bir klasör oluşturun. Bunu yapmak için `Dosyanıza isim verin...` kutusuna içeriğinizin adını boşluk yerine tire ile küçük harflerle yazın. Örneğimde, diyelim ki 2048 kelimelik BIP39 listesinin PDF görselini eklemek istiyorum. Bu yüzden klasörümü `bip39-wordlist` olarak adlandıracağım: ![event](assets/06.webp)
- Klasörün oluşturulduğunu onaylamak için, aynı kutuya addan sonra bir eğik çizgi eklemeniz yeterlidir, örneğin: `bip39-wordlist/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![event](assets/07.webp)


- Bu klasörde `bet.yml` adında ilk YAML dosyasını oluşturacaksınız:

![event](assets/08.webp)


- Bu şablonu kullanarak bu dosyayı içeriğinizle ilgili bilgilerle doldurun:


```yaml
project:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


İşte her bir alan için doldurulması gereken ayrıntılar:



- `proje`**: Kuruluşunuzun PlanB Network'teki tanımlayıcısını belirtin. Şirketiniz için henüz bir "proje" tanımlayıcınız yoksa, bu öğreticiyi izleyerek bir tane oluşturabilirsiniz.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Eğer bir proje profiliniz yoksa, bir proje profili oluşturmadan sadece adınızı, takma adınızı veya şirketinizin adını kullanabilirsiniz.



- `type`**: Aşağıdaki iki seçenek arasından içeriğinizin niteliğini seçin:
 - eğitim içerikleri için `Eğitimsel İçerik`.
 - diğer farklı içerik türleri için `Görsel İçerik`.



- `bağlantılar`**: İçeriğinize bağlantılar sağlayın. İki seçeneğiniz var:
 - İçeriğinizi doğrudan PlanB'nin GitHub'ında barındırmayı seçerseniz, aşağıdaki adımlar sırasında bağlantıları bu dosyaya eklemeniz gerekecektir.
 - İçeriğiniz kişisel web siteniz gibi başka bir yerde barındırılıyorsa, ilgili bağlantıları burada belirtin:
     - `indir`: İçeriğinizi indirmek için bir bağlantı.
     - `view`: İçeriğinizi görüntülemek için bir bağlantı (indirme bağlantısıyla aynı olabilir). İçeriğiniz birden fazla dilde mevcutsa, her dil için bir bağlantı ekleyin.



- `tags`**: İçeriğinizle ilişkili iki etiket ekleyin. Örnekler:
 - Bitcoin
 - teknoloji
 - ekonomi
 - eĞİTİM
 - meme...



- `contributors`**: Eğer varsa katılımcı tanımlayıcınızı belirtin.


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
project: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Mnemonic cümlelerini kodlamak için kullanılan BIP39 sözlüğündeki 2048 İngilizce kelimenin tam ve numaralandırılmış listesi. Belge tek bir sayfaya yazdırılabilir.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```