---
name: Đóng góp - Hướng dẫn Git (nâng cao)
description: Hướng dẫn dành cho người dùng nâng cao để cung cấp hướng dẫn về Plan ₿ Network với Git
---
![cover](assets/cover.webp)

Trước khi làm theo hướng dẫn này để thêm hướng dẫn mới, bạn cần hoàn thành một vài bước sơ bộ. Nếu bạn chưa làm, vui lòng xem hướng dẫn giới thiệu này trước, sau đó quay lại đây:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Bạn đã có:


- Chọn một chủ đề cho bài hướng dẫn của bạn;
- Đã liên hệ với nhóm Plan ₿ Network qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network ;
- Chọn công cụ đóng góp của bạn.

Trong hướng dẫn dành cho người dùng Git có kinh nghiệm này, chúng tôi sẽ tóm tắt ngắn gọn các bước chính và hướng dẫn cần thiết để cung cấp hướng dẫn Plan ₿ Network mới. Nếu bạn không quen với Git và GitHub, tôi khuyên bạn nên làm theo một trong 2 hướng dẫn chi tiết hơn sau đây, hướng dẫn bạn từng bước:


- Trung cấp (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Người mới bắt đầu (giao diện web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Công cụ được đề xuất

Để chỉnh sửa các tệp Markdown:


- Obsidian** (Miễn phí, không phải mã nguồn mở)
- Đánh dấu văn bản** (Miễn phí, mã nguồn mở)
- Zettlr** (Miễn phí, mã nguồn mở)
- Typora** (Phần mềm trả phí, khoảng 15€, không phải mã nguồn mở)

Đối với Git:


- Git** (Miễn phí, mã nguồn mở)
- GitHub Desktop** (Miễn phí, mã nguồn mở)
- Sourcetree** (Miễn phí, không phải mã nguồn mở)

Để chỉnh sửa các tệp YAML:


- Visual Studio Code** (Miễn phí, mã nguồn mở)
- Sublime Text** (Miễn phí nhưng có giới hạn, không phải mã nguồn mở)

Để tạo sơ đồ và hình ảnh:


- Canva** (Miễn phí với các tùy chọn trả phí, không phải mã nguồn mở)
- Inkscape** (Miễn phí, mã nguồn mở)
- Penpot** (Miễn phí, mã nguồn mở)

## Quy trình làm việc

### 1 - Cấu hình môi trường cục bộ của bạn


- Bạn phải có nhánh riêng của [Kho lưu trữ Plan ₿ Network trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Đồng bộ hóa nhánh chính (`dev`) của nhánh fork với kho lưu trữ nguồn.
- Cập nhật bản sao cục bộ của bạn.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
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

### 2 - Tạo nhánh mới


- Hãy chắc chắn rằng bạn đang ở nhánh `dev`.
- Tạo một nhánh mới với tên mô tả (ví dụ: `tuto-green-wallet-loic`).
- Xuất bản nhánh này trên nhánh trực tuyến của bạn.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Thêm tài liệu hướng dẫn

***Lưu ý:*** Bạn có thể tự động hóa các bước 3 và 4 bằng cách sử dụng [tập lệnh GUI Python của tôi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Chạy trực tiếp từ thư mục của nó trong bản sao cục bộ của bạn, sau đó điền vào các trường bắt buộc trên GUI. Để biết thêm thông tin về cách cài đặt và sử dụng, hãy xem [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Nếu bạn muốn thực hiện thủ công, hãy làm theo các bước sau:


- Xác định vị trí thư mục thích hợp trong kho lưu trữ cục bộ (ví dụ: `tutorials/wallet`).
- Tạo một thư mục dành riêng cho hướng dẫn với tên rõ ràng (ví dụ: `green-wallet`). Tên thư mục này cũng sẽ xác định đường dẫn URL của hướng dẫn. Tên phải viết thường, không có ký tự đặc biệt (trừ dấu gạch nối) và không có khoảng trắng.
- Thêm các mục sau vào thư mục này:
    - Một thư mục con có tên `assets` chứa:
        - Hai hình ảnh `.webp`:
            - `logo.webp`: Logo hướng dẫn (hình vuông có nền). Logo này phải đại diện cho phần mềm hoặc công cụ được trình bày. Nếu hướng dẫn không dành riêng cho một công cụ (ví dụ: hướng dẫn chung để tạo cụm từ ghi nhớ), bạn có thể chọn hình ảnh phù hợp (ví dụ: biểu tượng chung).
            - `cover.webp`: Ảnh bìa hiển thị ở đầu phần hướng dẫn.
        - Một thư mục con chứa mã của ngôn ngữ gốc của hướng dẫn. Ví dụ, nếu hướng dẫn được viết bằng tiếng Anh, thư mục con này phải được đặt tên là `en'. Đặt tất cả các hình ảnh của hướng dẫn (sơ đồ, hình ảnh, ảnh chụp màn hình, v.v.) vào thư mục này.
    - Tệp `tutorial.yml` chứa siêu dữ liệu (tác giả, thẻ, danh mục, mức độ khó, v.v.).
    - Tệp Markdown chứa hướng dẫn, được đặt tên theo mã ngôn ngữ (ví dụ: `fr.md`, `en.md`, v.v.).

```bash
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Điền vào tệp YAML


- Hoàn thành tệp `tutorial.yml` như sau:

```yaml
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
````
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

dự án_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

thẻ:


  - ví
  - phần mềm
  - chìa khóa

thể loại: di động

trình độ: người mới bắt đầu

tín dụng:

giáo sư: khá riêng tư

# Kiểm tra siêu dữ liệu

ngôn ngữ gốc: fr

hiệu đính:


  - ngôn ngữ: fr

ngày đóng góp cuối cùng: 2024-11-20

tính cấp bách:

người đóng góp_id:


      - LoicPandul

phần thưởng:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Tạo một cam kết với một thông điệp mô tả

git commit -m "Thêm hướng dẫn green-wallet"

# Đẩy các sửa đổi của bạn vào nĩa của bạn

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Tạo một cam kết mô tả các sửa đổi đã thực hiện

git commit -m "Sửa lỗi sau khi xem lại hướng dẫn về green-wallet"

# Đẩy các sửa đổi trên ngã ba của bạn

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Xin chào, Bitcoin!")

```