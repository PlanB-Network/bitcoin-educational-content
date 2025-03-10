---
name: Đóng góp - Hướng dẫn với GitHub Desktop (trung cấp)
description: Hướng dẫn đầy đủ về hướng dẫn Plan ₿ Network với GitHub Desktop
---
![cover](assets/cover.webp)

Trước khi làm theo hướng dẫn này để thêm hướng dẫn mới, bạn cần hoàn thành một vài bước sơ bộ. Nếu bạn chưa làm, vui lòng xem hướng dẫn giới thiệu này trước, sau đó quay lại đây:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Bạn đã có:


- Chọn một chủ đề cho bài hướng dẫn của bạn;
- Đã liên hệ với nhóm Plan ₿ Network qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network ;
- Chọn công cụ đóng góp của bạn.

Trong hướng dẫn này, chúng ta sẽ xem cách thêm hướng dẫn của bạn vào Plan ₿ Network bằng cách cấu hình môi trường cục bộ của bạn với GitHub Desktop. Nếu bạn đã thành thạo Git, hướng dẫn rất chi tiết này có thể không cần thiết đối với bạn. Thay vào đó, tôi khuyên bạn nên xem hướng dẫn khác này, trong đó tôi chỉ trình bày các hướng dẫn chung, không có hướng dẫn từng bước chi tiết:


- Người dùng có kinh nghiệm**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Nếu bạn không muốn cấu hình môi trường cục bộ của mình, hãy làm theo hướng dẫn khác được thiết kế cho người mới bắt đầu, trong đó chúng tôi thực hiện các thay đổi trực tiếp thông qua giao diện web GitHub:


- Người mới bắt đầu (giao diện web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Điều kiện tiên quyết

Phần mềm cần thiết để thực hiện hướng dẫn này:


- [Máy tính để bàn GitHub](https://desktop.github.com/);
- Trình chỉnh sửa tệp markdown như [Obsidian](https://obsidian.md/);
- Trình soạn thảo mã ([VSC](https://code.visualstudio.com/) hoặc [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Điều kiện tiên quyết trước khi bắt đầu hướng dẫn:


- Có [tài khoản GitHub](https://github.com/signup);
- Có một nhánh của [Kho lưu trữ nguồn Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content);
- Có [hồ sơ giáo viên trên Plan₿ Network](https://planb.network/professors) (chỉ khi bạn cung cấp hướng dẫn đầy đủ).

Nếu bạn cần trợ giúp để đáp ứng các điều kiện tiên quyết này, các hướng dẫn khác của tôi sẽ giúp ích:


https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Khi mọi thứ đã sẵn sàng và môi trường cục bộ của bạn đã được thiết lập với nhánh Plan ₿ Network, bạn có thể bắt đầu thêm phần hướng dẫn.

## 1 - Tạo một nhánh mới

Mở trình duyệt của bạn và điều hướng đến trang fork của bạn trong kho lưu trữ Plan ₿ Network. Đây là fork bạn đã thiết lập trên GitHub. URL của fork của bạn sẽ trông như thế này: `https://github.com/[your-username]/bitcoin-educational-content` :

![TUTO](assets/fr/03.webp)

Đảm bảo bạn đang ở nhánh `dev` chính, sau đó nhấp vào nút `Sync fork`. Nếu nhánh của bạn chưa được cập nhật, GitHub sẽ yêu cầu bạn cập nhật nhánh của mình. Tiến hành cập nhật này. Mặt khác, nếu nhánh của bạn đã được cập nhật, GitHub sẽ thông báo cho bạn:

![TUTO](assets/fr/04.webp)

Mở GitHub Desktop và đảm bảo rằng nhánh của bạn được chọn đúng ở góc trên bên trái của cửa sổ:

![TUTO](assets/fr/05.webp)

Nhấp vào nút `Fetch origin`. Nếu kho lưu trữ cục bộ của bạn đã được cập nhật, GitHub Desktop sẽ không đề xuất bất kỳ hành động nào nữa. Nếu không, tùy chọn `Pull origin` sẽ xuất hiện. Nhấp vào nút này để cập nhật kho lưu trữ cục bộ của bạn:

![TUTO](assets/fr/06.webp)

Kiểm tra xem bạn có đang ở nhánh chính `dev` không:

![TUTO](assets/fr/07.webp)

Nhấp vào nhánh này, sau đó nhấp vào nút `Nhánh mới`:

![TUTO](assets/fr/08.webp)

Đảm bảo nhánh mới dựa trên kho lưu trữ nguồn, tức là `PlanB-Network/bitcoin-educational-content`.

Đặt tên cho nhánh của bạn sao cho tiêu đề nêu rõ mục đích của nó, sử dụng dấu gạch ngang để phân tách từng từ. Ví dụ, giả sử mục tiêu của chúng ta là viết hướng dẫn về cách sử dụng Sparrow Wallet. Trong trường hợp này, nhánh công việc dành riêng để viết hướng dẫn này có thể được đặt tên là: `tuto-sparrow-wallet-loic`. Sau khi bạn đã nhập tên phù hợp, hãy nhấp vào `Create branch` để xác nhận việc tạo nhánh:

![TUTO](assets/fr/09.webp)

Bây giờ hãy nhấp vào nút `Publish branch` để lưu nhánh làm việc mới của bạn trên nhánh trực tuyến trên GitHub:

![TUTO](assets/fr/10.webp)

Bây giờ, trên GitHub Desktop, bạn sẽ ở nhánh mới của mình. Điều này có nghĩa là bất kỳ thay đổi nào bạn thực hiện cục bộ trên máy tính của mình sẽ được lưu riêng trên nhánh cụ thể này. Ngoài ra, miễn là nhánh này vẫn được chọn trên GitHub Desktop, các tệp hiển thị cục bộ trên máy của bạn sẽ tương ứng với các tệp của nhánh này (`tuto-sparrow-wallet-loic`), chứ không phải các tệp của nhánh chính (`dev`).

![TUTO](assets/fr/11.webp)

Đối với mỗi bài viết mới mà bạn muốn xuất bản, bạn sẽ cần tạo một nhánh mới từ `dev`. Nhánh trong Git là phiên bản song song của dự án, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính, cho đến khi công việc đã sẵn sàng để hợp nhất.

## 2 - Thêm tệp hướng dẫn

Bây giờ nhánh làm việc đã được tạo, đã đến lúc tích hợp hướng dẫn mới của bạn. Bạn có hai lựa chọn: sử dụng tập lệnh Python của tôi, tự động tạo các tài liệu cần thiết hoặc tạo từng tệp theo cách thủ công. Hãy cùng xem các bước cần thực hiện cho từng tùy chọn.

### Với tập lệnh Python của tôi

Bạn cần cài đặt:


- Python 3.8 trở lên;
- Các phụ thuộc cần thiết cho tập lệnh. Chạy:

```bash
pip install customtkinter appdirs
````
Pour utiliser le script, rendez-vous dans le dossier où il est stocké. Le script se trouve dans le dépôt de data de Plan ₿ Network sous le chemin : `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.
Une fois dans le dossier, exécutez la commande :
```

python new-tutorial-creation.py

```
Une interface graphique (GUI) va s'ouvrir. La première fois, vous devrez entrer toutes les informations nécessaires, mais lors des utilisations ultérieures du script, vos informations personnelles seront mémorisées, ce qui vous évite de devoir les saisir de nouveau.
![TUTO](assets/fr/37.webp)
Commencez par indiquer le chemin local menant au dossier `/tutorials` sur votre clone du dépôt (`.../bitcoin-educational-content/tutorials/`). Vous pouvez le noter manuellement ou cliquer sur le bouton "Browse" pour naviguer via votre explorateur de fichiers.
![TUTO](assets/fr/38.webp)
Sélectionnez la langue dans laquelle vous rédigerez votre tutoriel.
![TUTO](assets/fr/39.webp)
Choisissez une catégorie principale pour votre tutoriel.
![TUTO](assets/fr/40.webp)
Ensuite, sélectionnez une sous-catégorie appropriée, en fonction de la catégorie principale que vous avez choisie.
![TUTO](assets/fr/41.webp)
Déterminez un niveau de difficulté pour le tutoriel.
![TUTO](assets/fr/42.webp)
Choisissez le nom du répertoire spécialement créé pour votre tutoriel. Le nom de ce dossier devrait refléter le logiciel abordé dans le tutoriel, en utilisant des tirets pour relier les mots. Par exemple, le dossier pourrait s'appeler `red-wallet` :
![TUTO](assets/fr/43.webp)
Le `project_id` est l'UUID de l'entreprise ou de l'organisation derrière l'outil présenté dans le tutoriel, disponible [dans la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, pour un tutoriel sur le logiciel Sparrow Wallet, vous trouverez ce `project_id` dans le fichier : `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Cette information est ajoutée au fichier YAML de votre tutoriel car Plan ₿ Network maintient une base de données des entreprises et organisations actives sur Bitcoin ou des projets connexes. En ajoutant le `project_id` associé à votre tutoriel, vous créez un lien entre votre contenu et l'entité concernée.
***Mise à jour :*** Dans la nouvelle version du script, vous n'avez plus besoin de saisir manuellement le `project_id`. Une fonction de recherche a été ajoutée pour trouver le projet par son nom et récupérer automatiquement le `project_id` correspondant. Tapez le début du nom du projet dans la case "Project name" pour le rechercher, puis sélectionnez l'entreprise souhaitée dans le menu déroulant. Le `project_id` sera automatiquement renseigné dans la case en dessous. Vous avez également la possibilité de le noter manuellement si nécessaire.
![TUTO](assets/fr/44.webp)
Pour les tags, sélectionnez 2 ou 3 mots-clés pertinents en relation avec le contenu de votre tutoriel, en les choisissant exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).
![TUTO](assets/fr/45.webp)
Dans la case "Contributor's GitHub ID", inscrivez votre identifiant GitHub.
![TUTO](assets/fr/46.webp)
Pour la case "PBN professor's ID", saisissez votre identifiant en utilisant les mots de la liste BIP39, tel qu'il apparaît sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).
![TUTO](assets/fr/47.webp)
Pour plus de détails sur votre identifiant de professeur, veuillez consulter le tutoriel suivant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Une fois toutes les informations saisies et vérifiées, cliquez sur "Create Tutorial" pour valider la création des fichiers de votre tutoriel. Cela générera en local le dossier de votre tutoriel et tous les fichiers nécessaires dans le dossier de la catégorie sélectionnée.
![TUTO](assets/fr/48.webp)
Vous pouvez maintenant passer outre la sous-partie "Sans mon script Python", ainsi que l'étape 3 "Remplir le fichier YAML", car le script a déjà effectué ces actions automatiquement pour vous. Passez directement à l'étape 4 et à la rédaction de votre tutoriel.
Pour plus d'informations sur ce script Python, vous pouvez également [consulter son README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).
### Sans mon script Python
Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`.
Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web Plan ₿ Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![TUTO](assets/fr/12.webp)
Au sein du dossier `wallet`, il faut créer un nouveau répertoire spécifiquement dédié à votre tutoriel. Le nom de ce dossier doit évoquer le logiciel traité dans le tutoriel, en veillant à relier les mots par des tirets. Pour mon exemple, le dossier sera intitulé `sparrow-wallet` :
![TUTO](assets/fr/13.webp)
Dans ce nouveau sous-dossier dédié à votre tutoriel, il faut ajouter plusieurs éléments :
- Créez un dossier `assets`, destiné à recevoir toutes les illustrations nécessaires à votre tutoriel ;
- Au sein de ce dossier `assets`, il faut créer un sous-dossier nommé selon le code de langue originale du tutoriel. Par exemple, si le tutoriel est rédigé en anglais, ce sous-dossier doit être nommé `en`. Placez-y tous les visuels du tutoriel (schémas, images, captures d’écran, etc.).
- Un fichier `tutorial.yml` doit être créé pour y consigner les détails relatifs à votre tutoriel ;
- Un fichier en format markdown est à créer pour y rédiger le contenu effectif de votre tutoriel. Ce fichier doit être intitulé selon le code de la langue de rédaction. Par exemple, pour un tutoriel rédigé en français, le fichier devra s'appeler `fr.md`.
![TUTO](assets/fr/14.webp)
Pour résumer, voici la hiérarchie des fichiers à créer :
```

bitcoin-education-content/

└── hướng dẫn/

└── ví/ (thay đổi sang danh mục đúng)

└── sparrow-wallet/ (sửa đổi với tên tuto)

├── tài sản/

│ ├── en/ (thay đổi sang mã ngôn ngữ phù hợp)

├── hướng dẫn.yml

└── fr.md (sẽ được sửa đổi theo mã ngôn ngữ phù hợp)

```
## 3 - Remplir le fichier YAML
Remplissez le fichier `tutorial.yml` en copiant le modèle suivant :
```

nhận dạng:

dự án_id:

thẻ:

-

-

-

loại:

mức độ:

tín dụng:

giáo sư:

# Kiểm tra siêu dữ liệu

ngôn ngữ gốc:

hiệu đính:


  - ngôn ngữ:

ngày_đóng_góp_cuối_cùng:

tính cấp bách:

người đóng góp_id:

-

phần thưởng:

````

Sau đây là các trường bắt buộc:


- id**: UUID (_Universally Unique Identifier_) để nhận dạng duy nhất hướng dẫn. Bạn có thể tạo nó bằng [một công cụ trực tuyến](https://www.uuidgenerator.net/version4). Hạn chế duy nhất là UUID này phải ngẫu nhiên, để không xung đột với UUID khác trên nền tảng;
- project_id**: UUID của công ty hoặc tổ chức đằng sau công cụ được trình bày trong hướng dẫn [từ danh sách các dự án](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ví dụ: nếu bạn đang thực hiện hướng dẫn về phần mềm Sparrow Wallet, bạn có thể tìm thấy `project_id` này trong tệp sau: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Thông tin này được thêm vào tệp YAML của hướng dẫn của bạn vì Plan ₿ Network duy trì cơ sở dữ liệu của tất cả các công ty và tổ chức hoạt động trên Bitcoin hoặc các dự án liên quan. Bằng cách thêm `project_id` của thực thể được liên kết vào hướng dẫn của bạn, bạn tạo liên kết giữa hai phần tử;
- thẻ**: 2 hoặc 3 từ khóa có liên quan đến nội dung hướng dẫn, được chọn độc quyền [từ danh sách thẻ Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- category**: Tiểu thể loại tương ứng với nội dung hướng dẫn, theo cấu trúc Plan ₿ Network (ví dụ: đối với ví: `desktop`, `hardware`, `mobile`, `backup`);
- level** : Mức độ khó của hướng dẫn, từ :
    - người mới bắt đầu`
    - `trung gian`
    - `nâng cao`
    - `chuyên gia`
- giáo sư**: `contributor_id` của bạn (BIP39 từ) như được hiển thị trên [hồ sơ giáo viên của bạn](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language**: Ngôn ngữ gốc của hướng dẫn (ví dụ: `fr`, `en`, v.v.);
- soát lỗi**: Thông tin về quá trình soát lỗi. Điền vào phần đầu tiên, vì việc soát lỗi hướng dẫn của riêng bạn được tính là xác thực đầu tiên:
    - ngôn ngữ**: Kiểm tra mã ngôn ngữ (ví dụ: `fr`, `en`, v.v.).
    - last_contribution_date**: Ngày hôm nay.
    - mức độ khẩn cấp**: Để trống.
    - contributors_id**: ID GitHub của bạn.
    - phần thưởng**: Để trống.

Để biết thêm chi tiết về ID giáo viên của bạn, vui lòng tham khảo hướng dẫn tương ứng:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Sau đây là ví dụ về tệp `tutorial.yml` được hoàn thành cho hướng dẫn về ví Blockstream Green:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
```

Sau khi hoàn tất việc chỉnh sửa tệp `tutorial.yml`, hãy lưu tài liệu của bạn bằng cách nhấp vào `File > Save`:

![TUTO](assets/fr/16.webp)

Bây giờ bạn có thể đóng trình soạn thảo mã.

## 4 - Điền vào tệp Markdown

Bây giờ bạn có thể mở tệp hướng dẫn của mình, được đặt tên theo mã ngôn ngữ của bạn, ví dụ: `en.md`. Đi đến Obsidian, ở phía bên trái của cửa sổ và cuộn xuống cây thư mục đến thư mục hướng dẫn của bạn và tệp mong muốn:

![TUTO](assets/fr/18.webp)

Nhấp vào tập tin để mở nó:

![TUTO](assets/fr/19.webp)

Chúng ta sẽ bắt đầu bằng cách điền vào phần `Thuộc tính` ở đầu tài liệu.

![TUTO](assets/fr/20.webp)

Thêm và điền thủ công khối mã sau:

```markdown
---
name: [Titre]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Điền tên hướng dẫn của bạn và mô tả ngắn gọn:

![TUTO](assets/fr/22.webp)

Sau đó thêm đường dẫn đến ảnh bìa ở đầu hướng dẫn của bạn. Để thực hiện việc này, hãy lưu ý:

```markdown
![cover-sparrow](assets/cover.webp)
```

Cú pháp này sẽ hữu ích bất cứ khi nào bạn cần thêm hình ảnh vào hướng dẫn của mình. Dấu chấm than chỉ ra một hình ảnh, có văn bản thay thế (alt) được chỉ định giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được chỉ định giữa các dấu ngoặc vuông:

![TUTO](assets/fr/23.webp)

## 5 - Thêm logo và bìa

Trong thư mục `assets`, bạn cần thêm một tệp có tên `logo.webp`, tệp này sẽ đóng vai trò là hình thu nhỏ cho bài viết của bạn. Hình ảnh này phải ở định dạng `.webp` và có kích thước vuông để phù hợp với giao diện người dùng. Bạn có thể tự do chọn logo của phần mềm được đề cập trong hướng dẫn hoặc bất kỳ hình ảnh có liên quan nào khác, miễn là không có bản quyền. Ngoài ra, hãy thêm một hình ảnh có tên `cover.webp` vào cùng một vị trí. Hình ảnh này sẽ được hiển thị ở đầu hướng dẫn của bạn. Đảm bảo rằng hình ảnh này, giống như logo, tôn trọng quyền sử dụng và phù hợp với bối cảnh hướng dẫn của bạn:

![TUTO](assets/fr/17.webp)

## 6 - Viết hướng dẫn và thêm hình ảnh

Tiếp tục viết nội dung hướng dẫn của bạn. Khi bạn muốn đưa phụ đề vào, hãy áp dụng định dạng đánh dấu thích hợp bằng cách thêm tiền tố `##` vào văn bản:

![TUTO](assets/fr/24.webp)

Thư mục con ngôn ngữ trong thư mục `assets` được sử dụng để lưu trữ sơ đồ và hình ảnh đi kèm với hướng dẫn của bạn. Tránh đưa văn bản vào hình ảnh của bạn càng nhiều càng tốt để nội dung của bạn dễ tiếp cận với đối tượng quốc tế. Tất nhiên, phần mềm được trình bày sẽ chứa văn bản, nhưng nếu bạn thêm sơ đồ hoặc chỉ dẫn bổ sung vào ảnh chụp màn hình phần mềm, hãy làm như vậy mà không có văn bản hoặc, nếu cần thiết, hãy sử dụng tiếng Anh.

![TUTO](assets/fr/25.webp)

Để đặt tên cho hình ảnh của bạn, chỉ cần sử dụng các số tương ứng với thứ tự xuất hiện của chúng trong hướng dẫn, được định dạng thành hai chữ số (hoặc ba chữ số nếu hướng dẫn của bạn chứa hơn 99 hình ảnh). Ví dụ, đặt tên cho hình ảnh đầu tiên của bạn là `01.webp`, hình ảnh thứ hai là `02.webp`, v.v.

Hình ảnh của bạn chỉ được phép ở định dạng `.webp`. Nếu cần, bạn có thể sử dụng [phần mềm chuyển đổi hình ảnh của tôi](https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Để chèn sơ đồ vào tài liệu, hãy sử dụng lệnh sau trong Markdown, chú ý chỉ định văn bản thay thế phù hợp cũng như đường dẫn hình ảnh chính xác:

```markdown
![sparrow](assets/fr/01.webp)
```

Dấu chấm than ở đầu chỉ ra một hình ảnh. Văn bản thay thế, giúp truy cập và tham chiếu, được đặt giữa các dấu ngoặc vuông. Cuối cùng, đường dẫn đến hình ảnh được chỉ ra giữa các dấu ngoặc vuông.

Nếu bạn muốn tạo sơ đồ của riêng mình, hãy đảm bảo tuân theo hướng dẫn đồ họa của Plan ₿ Network để đảm bảo tính nhất quán về mặt hình ảnh:


- Phông chữ**: Sử dụng [Rubik](https://fonts.google.com/specimen/Rubik);
- Màu sắc** :
 - Màu cam: #FF5C00
 - Đen: #000000
 - Trắng: #FFFFFF

**Điều bắt buộc là tất cả hình ảnh tích hợp vào hướng dẫn của bạn phải không có bản quyền hoặc tôn trọng giấy phép tệp nguồn**. Do đó, tất cả các sơ đồ được xuất bản trên Plan ₿ Network đều được cung cấp theo giấy phép CC-BY-SA, giống như văn bản.

**-> Mẹo:** Khi chia sẻ tệp ở nơi công cộng, chẳng hạn như hình ảnh, điều quan trọng là phải xóa siêu dữ liệu không cần thiết. Siêu dữ liệu này có thể chứa thông tin nhạy cảm, chẳng hạn như dữ liệu vị trí, ngày tạo và thông tin chi tiết về tác giả. Để bảo vệ quyền riêng tư của bạn, bạn nên xóa siêu dữ liệu này. Để đơn giản hóa thao tác này, bạn có thể sử dụng các công cụ chuyên dụng như [Exif Cleaner](https://exifcleaner.com/), cho phép bạn dọn dẹp siêu dữ liệu của tài liệu chỉ bằng thao tác kéo và thả đơn giản.

## 7 - Lưu và đề xuất hướng dẫn

Sau khi bạn hoàn thành việc viết hướng dẫn bằng ngôn ngữ bạn chọn, bước tiếp theo là gửi **Yêu cầu kéo**. Sau đó, quản trị viên sẽ thêm các bản dịch còn thiếu vào hướng dẫn của bạn bằng phương pháp dịch tự động của chúng tôi với sự hiệu đính của con người.

Để thực hiện Pull Request, hãy mở GitHub Desktop. Phần mềm sẽ tự động phát hiện bất kỳ thay đổi nào bạn đã thực hiện cục bộ trên nhánh của mình đối với kho lưu trữ gốc. Trước khi tiếp tục, hãy kiểm tra cẩn thận ở phía bên trái của giao diện để đảm bảo những thay đổi này tương ứng với những gì bạn mong đợi:

![TUTO](assets/fr/28.webp)

Thêm tiêu đề cho cam kết của bạn, sau đó nhấp vào nút màu xanh `Cam kết với [nhánh của bạn]` để xác thực những thay đổi này:

![TUTO](assets/fr/29.webp)

Cam kết là bản ghi các thay đổi được thực hiện đối với một nhánh, kèm theo thông báo mô tả, cho phép bạn theo dõi sự phát triển của một dự án theo thời gian. Đây là một dạng điểm kiểm tra trung gian.

Sau đó nhấp vào nút `Push origin`. Thao tác này sẽ gửi commit của bạn đến fork của bạn:

![TUTO](assets/fr/30.webp)

Nếu bạn chưa hoàn thành hướng dẫn, bạn có thể quay lại sau và thực hiện các cam kết mới. Nếu bạn đã hoàn tất việc chỉnh sửa nhánh này, hãy nhấp vào nút `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Bạn có thể kiểm tra lại lần cuối để đảm bảo những thay đổi của bạn là chính xác, sau đó nhấp vào nút `Tạo yêu cầu kéo`:

![TUTO](assets/fr/32.webp)

Yêu cầu kéo là yêu cầu được thực hiện để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của kho lưu trữ Plan ₿ Network, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được hợp nhất.

Bạn sẽ được tự động chuyển hướng trên trình duyệt của mình đến GitHub trong trang chuẩn bị cho Yêu cầu kéo của bạn:

![TUTO](assets/fr/33.webp)

Nhập tiêu đề tóm tắt ngắn gọn những thay đổi bạn muốn hợp nhất với kho lưu trữ nguồn. Thêm bình luận ngắn gọn mô tả những thay đổi này (nếu bạn có số vấn đề liên quan đến việc tạo hướng dẫn của mình, hãy nhớ ghi chú `Đóng #{số vấn đề}` làm bình luận), sau đó nhấp vào nút `Tạo yêu cầu kéo` màu xanh lá cây để xác nhận yêu cầu hợp nhất:

![TUTO](assets/fr/34.webp)

PR của bạn sau đó sẽ hiển thị trong tab `Pull Request` của kho lưu trữ Plan ₿ Network chính. Tất cả những gì bạn phải làm bây giờ là đợi cho đến khi quản trị viên liên hệ với bạn để xác nhận rằng đóng góp của bạn đã được hợp nhất hoặc yêu cầu bất kỳ sửa đổi nào khác.

![TUTO](assets/fr/35.webp)

Sau khi hợp nhất PR của bạn với nhánh chính, chúng tôi khuyên bạn nên xóa nhánh đang hoạt động (`tuto-sparrow-wallet`) để duy trì lịch sử sạch trên nhánh fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang PR của bạn:

![TUTO](assets/fr/36.webp)

Trên GitHub Desktop, bạn có thể quay lại nhánh chính của nhánh (`dev`).

![TUTO](assets/fr/07.webp)

Nếu bạn muốn thay đổi nội dung đóng góp của mình sau khi đã gửi PR, các bước thực hiện sẽ tùy thuộc vào trạng thái hiện tại của PR của bạn:


- Nếu PR của bạn vẫn mở và chưa được hợp nhất, hãy thực hiện các thay đổi cục bộ, vẫn ở cùng một nhánh. Sau khi các thay đổi đã được hoàn tất, hãy sử dụng nút `Push origin` để thêm một cam kết mới vào PR vẫn mở của bạn;
- Trong trường hợp PR của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần phải thực hiện lại quy trình từ đầu bằng cách tạo nhánh mới, sau đó gửi PR mới. Đảm bảo kho lưu trữ cục bộ của bạn được đồng bộ hóa với kho lưu trữ nguồn Plan ₿ Network trước khi tiếp tục.

Nếu bạn gặp khó khăn về mặt kỹ thuật khi gửi hướng dẫn, vui lòng đừng ngần ngại yêu cầu trợ giúp trên [nhóm Telegram chuyên dụng của chúng tôi để đóng góp](https://t.me/PlanBNetwork_ContentBuilder). Cảm ơn bạn rất nhiều!

