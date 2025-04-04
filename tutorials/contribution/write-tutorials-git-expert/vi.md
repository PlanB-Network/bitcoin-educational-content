---
name: Đóng góp - Hướng dẫn Git (nâng cao)
description: Hướng dẫn dành cho người dùng nâng cao để cung cấp hướng dẫn về Plan ₿ Network với Git
---
![cover](assets/cover.webp)

Trước khi làm theo hướng dẫn này để thêm hướng dẫn mới, bạn cần hoàn thành một vài bước sơ bộ. Nếu bạn chưa làm, vui lòng xem hướng dẫn giới thiệu này trước, sau đó quay lại đây:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Bạn đã có:


- Chọn một chủ đề cho bài hướng dẫn của bạn;
- Đã liên hệ với nhóm Plan ₿ Network qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network ;
- Chọn công cụ đóng góp của bạn.

Trong hướng dẫn dành cho người dùng Git có kinh nghiệm này, chúng tôi sẽ tóm tắt ngắn gọn các bước chính và hướng dẫn cần thiết để cung cấp hướng dẫn Plan ₿ Network mới. Nếu bạn không quen với Git và GitHub, tôi khuyên bạn nên làm theo một trong 2 hướng dẫn chi tiết hơn sau đây sẽ hướng dẫn bạn từng bước:


- Trung cấp (GitHub Desktop)**:

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Người mới bắt đầu (giao diện web)**:

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

```
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

```
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

```
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

Dưới đây là các trường bắt buộc:

- **id** : Một UUID (_Universally Unique Identifier_) cho phép xác định duy nhất hướng dẫn. Bạn có thể tạo nó bằng [một công cụ trực tuyến](https://www.uuidgenerator.net/version4). Điều kiện duy nhất là UUID này phải ngẫu nhiên để tránh xung đột với một UUID khác trên nền tảng;

- **project_id** : UUID của công ty hoặc tổ chức đứng sau công cụ được trình bày trong hướng dẫn [từ danh sách các dự án](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ví dụ, nếu bạn tạo một hướng dẫn về phần mềm Green Wallet, bạn có thể tìm thấy `project_id` trong tệp sau: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Thông tin này được thêm vào tệp YAML của hướng dẫn của bạn vì Plan ₿ Network duy trì cơ sở dữ liệu về tất cả các công ty và tổ chức hoạt động trên Bitcoin hoặc các dự án liên quan. Bằng cách thêm `project_id` của thực thể liên kết với hướng dẫn của bạn, bạn tạo ra một liên kết giữa hai phần tử;

- **tags** : 2 hoặc 3 từ khóa liên quan đến nội dung hướng dẫn, được chọn độc quyền [từ danh sách thẻ của Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category** : Danh mục con tương ứng với nội dung của hướng dẫn, theo cấu trúc của trang Plan ₿ Network (ví dụ: đối với ví: `desktop`, `hardware`, `mobile`, `backup`);

- **level** : Mức độ khó của hướng dẫn, được chọn từ:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : `professor_id` của bạn (UUID) như được hiển thị trên [hồ sơ giáo sư của bạn](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language** : Ngôn ngữ gốc của hướng dẫn (ví dụ: `fr`, `en`, v.v.);

- **proofreading** : Thông tin về quá trình hiệu đính. Hoàn thành phần đầu tiên, vì việc tự kiểm tra hướng dẫn của bạn được tính là một lần xác nhận:
    - **language** : Mã ngôn ngữ của quá trình hiệu đính (ví dụ: `fr`, `en`, v.v.).
    - **last_contribution_date** : Ngày hiện tại.
    - **urgency** : 1
    - **contributor_names** : ID GitHub của bạn.
    - **reward** : 0

Để biết thêm chi tiết về ID giáo viên của bạn, vui lòng tham khảo hướng dẫn tương ứng:

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

### 5 - Viết nội dung


- Hoàn thiện thuộc tính tệp Markdown với:
    - Tiêu đề (`tên`).
    - Một mô tả ngắn (`description`).
- Thêm ảnh bìa vào đầu phần hướng dẫn bằng cú pháp Markdown (thay thế "green" bằng tên công cụ được hiển thị):

```
![cover-green](assets/cover.webp)
```


- Viết nội dung hướng dẫn bằng Markdown:
    - Sử dụng các tiêu đề có cấu trúc tốt (`##`), danh sách và đoạn văn.
    - Chèn hình ảnh bằng cú pháp Markdown:

```
![nom-image](assets/en/001.webp)
```


- Đặt sơ đồ và hình ảnh vào thư mục ngôn ngữ tương ứng, trong `/assets`.

### 6 - Lưu và gửi bài hướng dẫn


- Lưu các thay đổi cục bộ bằng cách tạo một cam kết có thông báo mô tả.
- Đẩy những thay đổi vào nhánh GitHub của bạn.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Khi hoàn tất, hãy tạo Yêu cầu kéo (PR) trên GitHub để đề xuất tích hợp các sửa đổi của bạn.
- Thêm tiêu đề và mô tả ngắn gọn cho PR. Đề cập đến số vấn đề tương ứng trong bình luận.

### 7 - Kiểm tra và hợp nhất


- Chờ xác thực hoặc phản hồi từ người quản trị.
- Nếu cần thiết, hãy sửa lỗi và đưa ra cam kết mới.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Sau khi PR đã được hợp nhất, bạn có thể xóa nhánh đang hoạt động của mình.

## Tiêu chuẩn sáng tạo nội dung


- Định dạng được hỗ trợ trên nền tảng**:
    - Markdown cổ điển: danh sách, liên kết, hình ảnh, trích dẫn, in đậm, in nghiêng, v.v.
    - LaTeX (chỉ khối, không phải nội tuyến): phân cách bằng `$$`.
    - Mã nội tuyến: Cú pháp với một dấu ngoặc đơn.
    - Khối mã: Cú pháp với ba dấu ngoặc ngược, ví dụ:

```
print("Hello, Bitcoin!")
```


- Hình ảnh minh họa và sơ đồ**:
    - Tất cả hình ảnh phải ở định dạng WebP. Sử dụng công cụ miễn phí này để chuyển đổi chúng nếu cần: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Đặt tên hình ảnh có 2 hoặc 3 chữ số (ví dụ: `001.webp`, `002.webp`).
    - Đối với hướng dẫn về ví di động hoặc ví phần cứng, hãy sử dụng bản mô phỏng.
    - Chỉ sử dụng hình ảnh tự tạo hoặc không có bản quyền.
    - Hãy đảm bảo chúng có liên quan và chất lượng cao.
- Hiến chương đồ họa**:
    - Phông chữ: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Kế hoạch màu sắc ₿ Mạng lưới:
        - Màu cam: `#FF5C00`
        - Đen: `#000000`
        - Trắng: `#FFFFFF`

Nếu bạn gặp khó khăn về mặt kỹ thuật khi gửi hướng dẫn, vui lòng đừng ngần ngại yêu cầu trợ giúp trên [nhóm Telegram chuyên dụng của chúng tôi để đóng góp](https://t.me/PlanBNetwork_ContentBuilder). Cảm ơn bạn rất nhiều!