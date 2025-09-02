---
name: Katkı - Git eğitimi (ileri düzey)
description: İleri düzey kullanıcılar için Git ile Plan ₿ Network hakkında bir eğitim sunan kılavuz
---
![cover](assets/cover.webp)


Yeni bir öğretici eklemeye ilişkin bu öğreticiyi takip etmeden önce, birkaç ön adımı tamamlamış olmanız gerekir. Henüz yapmadıysanız, lütfen önce bu giriş eğitimine bir göz atın, ardından buraya geri dönün:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Sende zaten var:



- Eğitiminiz için bir tema seçin;
- Plan ₿ Network ekibiyle [Telegram grubu] (https://t.me/PlanBNetwork_ContentBuilder) veya paolo@planb.network üzerinden iletişime geçin;
- Katkı araçlarınızı seçin.


Deneyimli Git kullanıcılarına yönelik bu eğitimde, yeni bir Plan ₿ Network eğitimi sunmak için temel adımları ve temel yönergeleri kısaca özetleyeceğiz. Git ve GitHub'a aşina değilseniz, bunun yerine sizi adım adım ilerletecek daha ayrıntılı diğer 2 öğreticiden birini izlemenizi tavsiye ederim:



- Orta Düzey (GitHub Masaüstü):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Yeni Başlayanlar (web Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Önerilen araçlar


Markdown dosyalarını düzenlemek için:



- Obsidian (Ücretsiz, açık kaynak değil)
- Mark Text (Ücretsiz, açık kaynak)
- Zettlr (Ücretsiz, açık kaynak)
- Typora (Ödemeli yazılım, ~15€, açık kaynak değil)


Git için:



- Git (Ücretsiz, açık kaynak)
- GitHub Desktop (Ücretsiz, açık kaynak)
- Sourcetree (Ücretsiz, açık kaynak değil)


YAML dosyalarını düzenlemek için:



- Visual Studio Code (Ücretsiz, açık kaynak)
- Sublime Text (Sınırlamalarla birlikte ücretsiz, açık kaynak değil)


Diyagramlar ve görseller oluşturmak için:



- Canva (Ücretli seçeneklerle ücretsiz, açık kaynak değil)
- Inkscape (Ücretsiz, açık kaynak)
- Penpot (Ücretsiz, açık kaynak)


## İş Akışları


### 1 - Yerel ortamınızı yapılandırın



- GitHub'daki Fork deposundan] (https://github.com/PlanB-Network/Bitcoin-educational-content) kendi Plan ₿ Network'ünüze sahip olmalısınız.
- Fork'nizin ana dalını (`dev`) kaynak deposu ile senkronize edin.
- Yerel klonunuzu güncelleyin.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Yeni bir şube oluşturun



- Dev' dalında olduğunuzdan emin olun.
- Açıklayıcı bir adla (örneğin `tuto-Green-Wallet-loic`) yeni bir dal oluşturun.
- Bu şubeyi çevrimiçi Fork'unuzda yayınlayın.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Eğitim belgelerini ekleyin


***Not:*** [Python GUI betiğimi] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) kullanarak 3. ve 4. adımları otomatikleştirebilirsiniz. Doğrudan yerel klonunuzdaki klasöründen çalıştırın, ardından GUI'deki gerekli alanları doldurun. Nasıl kurulacağı ve kullanılacağı hakkında daha fazla bilgi için [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) adresine bakın.


Manuel olarak yapmayı tercih ederseniz, aşağıdaki adımları izleyin:



- Yerel depodaki uygun klasörü bulun (örneğin `tutorials/Wallet`).
- Açık bir adla (örneğin `Green-Wallet`) öğreticiye ayrılmış bir dizin oluşturun. Bu klasör adı aynı zamanda öğreticinin URL yolunu da belirleyecektir. Küçük harflerle yazılmalı, özel karakterler (kısa çizgiler hariç) ve boşluk içermemelidir.
- Aşağıdaki öğeleri bu dizine ekleyin:
    - Içeren `assets` adlı bir alt klasör oluşturulur:
        - İki `.webp` görüntüsü:
            - `logo.webp`: Eğitim logosu (arka planlı kare biçiminde). Bu logo sunulan yazılımı veya aracı temsil etmelidir. Eğitim bir araca özgü değilse (örneğin: Mnemonic cümlesi oluşturmak için genel bir kılavuz), uygun bir görsel seçebilirsiniz (örneğin: genel bir simge).
            - `cover.webp`: Öğreticinin başlangıcında görüntülenen bir kapak resmi.
        - Öğreticinin orijinal dilinin kodunu taşıyan bir alt klasör. Örneğin, eğitim İngilizce yazılmışsa, bu alt klasör `en' olarak adlandırılmalıdır. Eğitimin tüm görsellerini (diyagramlar, resimler, ekran görüntüleri, vb.) bu klasöre yerleştirin.
    - Meta verileri (yazar, etiketler, kategori, zorluk seviyesi, vb.) içeren bir `tutorial.yml` dosyası.
    - Öğreticiyi içeren, dil koduna göre adlandırılmış bir Markdown dosyası (örn. `fr.md`, `en.md`, vb.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - YAML dosyasını doldurun



- Öğretici.yml` dosyasını aşağıdaki gibi tamamlayın:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


İşte gerekli alanlar:



- id**: Öğreticiyi benzersiz bir şekilde tanımlayan bir UUID (_Universally Unique Identifier_). Bunu [çevrimiçi bir araç] (https://www.uuidgenerator.net/version4) kullanarak generate yapabilirsiniz. Tek gereklilik, platformdaki başka bir UUID ile çakışmayı önlemek için bu UUID'nin rastgele olmasıdır;



- project_id**: Eğitimde sunulan aracın arkasındaki şirket veya kuruluşun UUID'si [proje listesinden] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Örneğin, Green Wallet yazılımı hakkında bir eğitim oluşturuyorsanız, bu `project_id`yi aşağıdaki dosyada bulabilirsiniz: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Bu bilgi öğreticinizin YAML dosyasına eklenir çünkü Plan ₿ Network, Bitcoin veya ilgili projeler üzerinde faaliyet gösteren tüm şirket ve kuruluşların bir veritabanını tutar. Öğreticinize bağlı varlığın `project_id` bilgisini ekleyerek, iki Elements arasında bir bağlantı oluşturursunuz;



- etiketler**: özel olarak [Plan ₿ Network etiket listesinden] seçilen, eğitim içeriğiyle ilgili 2 veya 3 anahtar kelime (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategori**: Plan ₿ Network web sitesi yapısına göre öğretici içeriğe karşılık gelen alt kategori (örneğin, cüzdanlar için: `masaüstü`, `donanım`, `mobil`, `yedekleme`);



- seviye**: Öğreticinin zorluk seviyesi, aşağıdakiler arasından seçilir:
    - `başlangıç`
    - `intermediate`
    - `gelişmiş`
    - `uzman`



- professor_id**: Profesör profilinizde] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) görüntülenen `profesör_id`niz (UUID);



- original_language**: Öğreticinin orijinal dili (örneğin, `fr`, `en`, vb.);



- redaksiyon**: Düzeltme süreci hakkında bilgi. Kendi öğreticinizi düzeltmek ilk doğrulama olarak sayıldığından ilk bölümü tamamlayın:
    - dil**: Düzeltme okumasının dil kodu (örneğin, `fr`, `en`, vb.).
    - last_contribution_date**: Günün tarihi.
    - aciliyet**: 1
    - contributor_names**: GitHub kimliğiniz.
    - ödül**: 0


Öğretmen kimliğiniz hakkında daha fazla bilgi için lütfen ilgili eğitime bakın:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


### 5 - İçeriği yazın



- Markdown dosya özelliklerini ile tamamlayın:
    - Başlık (`name`).
    - Kısa bir açıklama (`description`).
- Markdown sözdizimini kullanarak öğreticinin üst kısmına kapak resmini ekleyin ("Green" yerine gösterilen aracın adını yazın):


```
![cover-green](assets/cover.webp)
```



- Eğitim içeriğini Markdown ile yazın:
    - İyi yapılandırılmış başlıklar (`##`), listeler ve paragraflar kullanın.
    - Markdown sözdizimini kullanarak görseller ekleyin:


```
![nom-image](assets/en/001.webp)
```




- Diyagramları ve resimleri `/assets` içindeki ilgili dil alt klasörüne yerleştirin.


### 6 - Öğreticiyi kaydedin ve gönderin



- Açıklayıcı bir mesaj içeren bir commit oluşturarak değişikliklerinizi yerel olarak kaydedin.
- Değişiklikleri GitHub Fork'nize gönderin.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- İşiniz bittiğinde, yaptığınız değişikliklerin entegrasyonunu önermek için GitHub'da bir Çekme İsteği (PR) oluşturun.
- PR'ye bir başlık ve kısa bir açıklama ekleyin. Yorumda ilgili sorun numarasını belirtin.


### 7 - Düzeltme ve birleştirme



- Bir yöneticiden doğrulama veya geri bildirim bekleyin.
- Gerekirse düzeltmeler yapın ve yeni taahhütler gönderin.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- PR birleştirildikten sonra, çalışma dalınızı silebilirsiniz.


## İçerik oluşturma standartları



- Platformda desteklenen biçimlendirme**:
    - Klasik Markdown: listeler, bağlantılar, resimler, alıntılar, kalın, italik vb.
    - LaTeX (yalnızca blok, satır içi değil): `$$` ile sınırlandırılmıştır.
    - Satır içi kod: Tek bir backtick içeren sözdizimi.
    - Kod blokları: Üç geri işaretli sözdizimi, örneğin:


```
print("Hello, Bitcoin!")
```



- Çizimler ve diyagramlar**:
    - Tüm görseller WebP formatında olmalıdır. Gerekirse dönüştürmek için bu ücretsiz aracı kullanın: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Görselleri 2 veya 3 rakamla adlandırın (örneğin `001.webp`, `002.webp`).
    - Mobil veya Hardware Wallet eğitimleri için maketler kullanın.
    - Yalnızca kendi oluşturduğunuz veya telifsiz görselleri kullanın.
    - İlgili ve yüksek kaliteli olduklarından emin olun.
- Grafik tüzük**:
    - Yazı tipi: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Renkler Plan ₿ Network:
        - Turuncu: `#FF5C00`
        - Siyah: `#000000`
        - Beyaz: `#FFFFFF`


Öğreticinizi gönderirken teknik zorluklar yaşıyorsanız, lütfen [katkılar için özel Telegram grubumuz] (https://t.me/PlanBNetwork_ContentBuilder) üzerinden yardım istemekten çekinmeyin. Çok teşekkür ederim!