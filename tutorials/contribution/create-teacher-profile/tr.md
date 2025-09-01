---
name: Profesör Plan ₿ Network
description: Plan ₿ Network'de öğretmen profilimi nasıl ekleyebilirim veya değiştirebilirim?
---
![cover](assets/cover.webp)


Yeni bir eğitim veya kurs yazarak Plan ₿ Network'ye katkıda bulunmayı planlıyorsanız, bir öğretmen profiline ihtiyacınız olacaktır. Bu profil, platforma katkıda bulunduğunuz içerik için uygun kredileri almanızı sağlayacaktır.


Plan ₿ Network'te eğitim içeriği oluşturmaya zaten dahil olmuş olanlarınız için muhtemelen zaten bir öğretmen profiliniz vardır. Bunu [GitHub depomuzdaki] `/professors` klasöründe bulabilirsiniz (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Profiliniz zaten mevcutsa, giriş bilgilerinizi `professor.yml` dosyasında bulabilirsiniz.


Profilinizde değişiklik yapmak için bu eğitimin sonundaki "Öğretmen profilinizi düzenleyin" bölümüne gidin.


## Yazılımımızla yeni bir öğretmen ekleyin


Plan ₿ Network'te öğretmen profilinizi oluşturmanın en kolay yolu entegre Python aracımızı kullanmaktır. İşte nasıl çalıştığı.


### 1 - Yerel ortamınızı yapılandırın


GitHub'daki Plan ₿ Network deposundan] (https://github.com/PlanB-Network/Bitcoin-educational-content) kendi Fork'inize sahip olmalısınız.


Fork'unuzun ana dalını (`dev`) kaynak deposu ile senkronize edin.


Yerel klonunuzu güncelleyin.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Yeni bir şube oluşturun


Dev` dalı üzerinde olduğunuzdan emin olun. Açıklayıcı bir adla (örneğin `add-professor-loic-morel`) yeni bir dal oluşturun.


Bu şubeyi Fork'unuzda çevrimiçi olarak yayınlayın.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Öğretmen profilinizi oluşturun


Yerel klonunuzdaki `scripts/tutorial-related/data-creator/` klasörüne gidin. Yazılım için gerekli tüm bağımlılıkları yüklediğinizden emin olun, önce Python:


```bash
pip install -r requirements.txt
```


Ardından yazılımı şu komutla başlatın:


```bash
python3 main.py
```


Ana sayfaya geldiğinizde, depo klonunuzun yerel yolunu, yazdığınız dili ve GitHub ID'nizi girin. Bu profili başka biri için oluşturuyorsanız ve zaten bir Profesör profiline sahipseniz, kimliğinizi "*PBN Profesör Kimliği*" alanına girin. Kendi profilinizi oluşturuyorsanız, oluşturma sürecinde olduğunuz için henüz bir Profesör Kimliğiniz olmayacaktır, bu nedenle bu alanı boş bırakın.


Ardından "*Yeni Profesör*" düğmesine tıklayın.


![Image](assets/fr/01.webp)


Gerekli bilgileri doldurun (lütfen tüm bu bilgilerin GitHub'da olduğu gibi platformumuzda da herkese açık olacağını unutmayın):




- Öğretmen dosyanızın adı (adınızı ve soyadınızı veya takma adınızı küçük harflerle kullanın) ;
- Adınız veya takma adınız ;
- Web siteniz ve profiliniz X (isteğe bağlı) ;
- Okuyuculardan bağış almak için bir Lightning Address (isteğe bağlı) ;
- Listeden 2 veya 3 etiket seçin;
- Yerel klasörlerinizden bir profil görüntüsü seçmek için "*Görüntü Seç*" seçeneğine tıklayın (görüntü için herhangi bir ad ve format kullanılabilir ve yazılım bunu otomatik olarak uyarlayacaktır. Sadece resmin kare olduğundan emin olun);
- Profilinizin kısa bir açıklamasını yazın.


"*Profesör Oluştur*" seçeneğine tıklayarak oluşturma işlemini tamamlayın. Bu, profiliniz için gerekli tüm dosyaları otomatik olarak generate yapacaktır.


![Image](assets/fr/02.webp)


Açıklayıcı bir mesaj içeren bir commit oluşturarak değişikliklerinizi yerel olarak kaydedin. Değişiklikleri Fork GitHub'ınıza gönderin.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


İşiniz bittiğinde, yaptığınız değişikliklerin entegrasyonunu önermek için GitHub'da bir Çekme İsteği (PR) oluşturun. PR'ye bir başlık ve kısa bir açıklama ekleyin.


### 4 - Düzeltme ve birleştirme


Bir yöneticiden doğrulama veya geri bildirim bekleyin. Gerekirse düzeltmeleri yapın ve yeni taahhütleri gönderin.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


PR birleştirildikten sonra, çalışma dalınızı silebilirsiniz.


## Öğretmen profilinizi değiştirin


Git kullanımında ustalaştıysanız, yeni bir dal oluşturarak ve ilgili dosyayı doğrudan mevcut klasörünüzde düzenleyerek öğretmen profilinizi değiştirin. Değişiklikler, düzeltilecek bilgilere bağlı olarak `professor.yml` dosyasında veya markdown dosyasında yapılabilir. Değişikliklerinizi yerel olarak yaptıktan sonra, bunları Fork'ünüze gönderin ve bir PR gönderin.


Yeni başlayanlar için, değişikliği doğrudan GitHub'ın Interface web'i üzerinden yapmanızı öneririm. Bir GitHub hesabınız olduğundan emin olun. Nasıl oluşturacağınızı bilmiyorsanız, bu öğreticiyi takip edin:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Verilere ayrılmış Plan ₿ Network GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors) gidin.


![Image](assets/fr/03.webp)


"*professors*" klasörüne tıklayın, ardından kişisel klasörünüze gidin.


![Image](assets/fr/04.webp)


Lightning Address, ad veya bağlantılar gibi profil meta verilerinizi değiştirmek için "*professor.yml*" dosyasını seçin. Açıklamanızı değiştirmek için dilinize ait YAML dosyasına tıklayın (örneğin "*en.yml*" veya "*fr.yml*").


Açıklamanızı değiştirirseniz, tüm eski çevirileri kaldırmayı unutmayın. Daha sonra açıklamanızı bir LLM yardımıyla diğer dillere çevirebilir ya da yalnızca açıklamayı ana dilinizde bırakıp Pull Request'inizde açıklamanızın ekibimiz tarafından çevrilmesi gerektiğini belirtebilirsiniz.


![Image](assets/fr/05.webp)


Değiştirmek istediğiniz dosyanın üzerine geldiğinizde, kalem simgesine tıklayın.


![Image](assets/fr/06.webp)


Plan ₿ Network deposundan zaten bir Fork'niz yoksa, GitHub bir tane oluşturmanızı önerecektir. "*Fork this repository*" üzerine tıklayın.


![Image](assets/fr/07.webp)


Dosyada istediğiniz değişiklikleri yapın. İşiniz bittiğinde "*Değişiklikleri yap*" düğmesine tıklayın.


![Image](assets/fr/08.webp)


Değişikliğinizi açıklayan bir mesaj girin ve ardından "*Değişiklik öner*" seçeneğini seçin.


![Image](assets/fr/09.webp)


Yaptığınız değişikliklerin bir özeti görüntülenecektir. Profilinizde daha fazla değişiklik yapmak isterseniz, klasörlere geri dönebilir ve daha fazla taahhütte bulunabilirsiniz. İşiniz bittiğinde, "*Çekme isteği oluştur*" seçeneğine tıklayın.


Çekme İsteği, dalınızdaki değişiklikleri Plan ₿ Network deposunun ana dalına entegre etmek için yapılan ve birleştirilmeden önce değişikliklerin gözden geçirilmesine ve tartışılmasına olanak tanıyan bir istektir.


![Image](assets/fr/10.webp)


Interface'ün en üstünde, çalışma dalınızın Plan ₿ Network deposunun (ana dal olan) `dev' dalı ile birleştirildiğinden emin olun.


Kaynak depoyla birleştirmek istediğiniz değişiklikleri kısaca özetleyen bir başlık girin. Bu değişiklikleri açıklayan kısa bir yorum ekleyin ve ardından çekme isteğini onaylamak için Green "*Çekme isteği oluştur*" düğmesine tıklayın:


![Image](assets/fr/11.webp)


PR'niz daha sonra ana Plan ₿ Network deposunun "*Pull Request*" sekmesinde görünür olacaktır. Şimdi tek yapmanız gereken bir yöneticinin değişikliğinizi birleştirmesini beklemek.


![Image](assets/fr/12.webp)


Değişikliğinizi gönderirken herhangi bir teknik zorlukla karşılaşırsanız, lütfen [katkılara adanmış Telegram grubumuz] (https://t.me/PlanBNetwork_ContentBuilder) üzerinden yardım istemekten çekinmeyin. Çok teşekkür ederiz!