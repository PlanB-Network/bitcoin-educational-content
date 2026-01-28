---
name: Đóng góp - Hướng dẫn sử dụng Git (nâng cao)
description: Hướng dẫn dành cho người dùng nâng cao để đề xuất bài hướng dẫn trên Plan ₿ Academy bằng Git
---
![cover](assets/cover.webp)

Trước khi theo dõi bài hướng dẫn về cách thêm nội dung mới này, bạn cần hoàn thành một vài bước chuẩn bị sơ bộ. Nếu bạn chưa thực hiện, vui lòng xem bài hướng dẫn dưới đây trước, sau đó quay lại đây.

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Bạn cần phải có:

- Chủ đề cho bài hướng dẫn.
- Đã liên hệ với đội ngũ Plan ₿ Academy qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network.
- Lựa chọn công cụ đóng góp.

Trong bài hướng dẫn dành cho người dùng Git có kinh nghiệm này, chúng tôi sẽ tóm tắt nhanh các bước chính và các hướng dẫn thiết yếu để đề xuất một bài hướng dẫn mới trên Plan ₿ Academy. Nếu bạn chưa quen với Git và GitHub, tôi khuyên bạn nên làm theo một trong hai bài hướng dẫn chi tiết hơn sau đây:

- **Trung cấp (GitHub Desktop)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- **Người mới bắt đầu (giao diện web)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Công cụ được đề xuất

Để chỉnh sửa các file Markdown:

- **Obsidian** (Miễn phí, không phải mã nguồn mở)
- **Mark Text** (Miễn phí, mã nguồn mở)
- **Zettlr** (Miễn phí, mã nguồn mở)
- **Typora** (Phần mềm trả phí, khoảng 15€, không phải mã nguồn mở)

Đối với Git:

- **Git** (Miễn phí, mã nguồn mở)
- **GitHub Desktop** (Miễn phí, mã nguồn mở)
- **Sourcetree** (Miễn phí, không phải mã nguồn mở)

Để chỉnh sửa các file YAML:

- **Visual Studio Code** (Miễn phí, mã nguồn mở)
- **Sublime Text** (Miễn phí nhưng có giới hạn, không phải mã nguồn mở)

Để tạo sơ đồ và hình ảnh:

- **Canva** (Miễn phí và có tùy chọn trả phí, không phải mã nguồn mở)
- **Inkscape** (Miễn phí, mã nguồn mở)
- **Penpot** (Miễn phí, mã nguồn mở)

## Quy trình làm việc

### 1 - Cấu hình môi trường cục bộ

- Bạn phải có bản fork riêng của [repository Plan ₿ Academy trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Đồng bộ hóa nhánh chính (`dev`) của bản fork với bản gốc.
- Cập nhật bản clone bộ của bạn.

```
# Clone bản fork của bạn (nếu chưa làm)
git clone [https://github.com/](https://github.com/)<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Thêm repository gốc làm remote upstream
git remote add upstream [https://github.com/PlanB-Network/bitcoin-educational-content.git](https://github.com/PlanB-Network/bitcoin-educational-content.git)

# Lấy các thay đổi mới nhất từ repository gốc
git fetch upstream

# Chuyển sang nhánh chính 'dev'
git checkout dev

# Merge các thay đổi từ nhánh 'dev' của repository gốc vào bản fork của bạn
git merge upstream/dev

# Đẩy các cập nhật lên bản fork của bạn trên GitHub
git push origin dev
```

### 2 - Tạo nhánh mới

- Đảm bảo bạn đang ở nhánh `dev`.
- Tạo một nhánh mới với tên mô tả rõ ràng (ví dụ: `tuto-green-wallet-loic`).
- Đẩy nhánh này lên bản fork trực tuyến của bạn.

```
# Đảm bảo bạn đang ở nhánh 'dev'
git checkout dev

# Tạo nhánh mới với tên mô tả
git checkout -b tuto-green-wallet-loic

# Đẩy nhánh này lên bản fork trực tuyến
git push -u origin tuto-green-wallet-loic
```

### 3 - Thêm tài liệu hướng dẫn

***Lưu ý:*** Bạn có thể tự động hóa bước 3 và 4 bằng cách sử dụng [script GUI Python của tôi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Chạy trực tiếp từ thư mục của nó trong bản clone cục bộ, sau đó điền các trường yêu cầu trên giao diện. Để biết thêm thông tin về cách cài đặt và sử dụng, xem chi tiết trong file [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Nếu bạn thích làm thủ công, hãy theo các bước sau:

- Xác định vị trí thư mục thích hợp trong repository cục bộ (ví dụ: `tutorials/wallet`).
- Tạo một thư mục dành riêng cho bài hướng dẫn với tên rõ ràng (ví dụ: `green-wallet`). Tên thư mục này cũng sẽ được dùng làm đường dẫn URL của bài hướng dẫn. Nó nên viết thường, không có ký tự đặc biệt (ngoại trừ dấu gạch ngang) và không có khoảng trắng.
- Thêm các mục sau vào thư mục này:
    - Một thư mục con có tên `assets` chứa:
        - Hai hình ảnh `.webp`:
            - `logo.webp`: Logo bài hướng dẫn (định dạng vuông có nền). Logo này phải đại diện cho phần mềm hoặc công cụ được trình bày. Nếu bài hướng dẫn không dành riêng cho một công cụ (ví dụ: hướng dẫn chung về tạo mnemonic (cụm từ ghi nhớ)), bạn có thể chọn một hình ảnh phù hợp (ví dụ: một icon chung chung nào đó)..
            - `cover.webp`: Ảnh bìa hiển thị ở đầu bài hướng dẫn.
        - Một thư mục con mang mã ngôn ngữ gốc của bài hướng dẫn. Ví dụ, nếu bài hướng dẫn viết bằng tiếng Việt, thư mục này tên là `vi`. Đặt tất cả hình ảnh minh họa (sơ đồ, ảnh chụp màn hình...) vào đây.
    - File `tutorial.yml` chứa metadata (tác giả, thẻ, danh mục, mức độ khó,...).
    - File Markdown chứa nội dung bài hướng dẫn, được đặt tên theo mã ngôn ngữ (ví dụ: `vi.md`, `en.md`,...).

```
# Di chuyển đến thư mục phù hợp
cd tutorials/wallet

# Tạo thư mục dành riêng cho bài hướng dẫn
mkdir green-wallet
cd green-wallet

# Tạo thư mục con 'assets'
mkdir -p assets

# Tạo thư mục con cho mã ngôn ngữ gốc (ví dụ: 'vi' cho tiếng Việt)
mkdir -p assets/en

# Tạo tệp metadata và tệp Markdown (ví dụ: 'vi.md' cho tiếng Việt)
touch tutorial.yml vi.md
```

### 4 - Điền thông tin vào file YAML

- Hoàn thiện file `tutorial.yml` như sau:

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

Các trường bắt buộc:

- **id**: Một UUID (_Universally Unique Identifier_) là mã định danh duy nhất của bài hướng dẫn. Bạn có thể tạo nó bằng [một công cụ trực tuyến](https://www.uuidgenerator.net/version4). Điều kiện duy nhất là UUID này phải ngẫu nhiên để tránh xung đột với một UUID khác trên nền tảng.

- **project_id**: UUID của công ty hoặc tổ chức đứng sau công cụ được liệt kê trong [danh sách các dự án](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ví dụ, nếu bạn tạo một hướng dẫn về phần mềm Green Wallet, bạn có thể tìm thấy `project_id` trong file sau: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Thông tin này được thêm vào file YAML của bài hướng dẫn vì Plan ₿ Academy duy trì cơ sở dữ liệu về tất cả các công ty và tổ chức hoạt động trên Bitcoin hoặc các dự án liên quan. Bằng cách thêm `project_id`, bạn sẽ tạo ra mối liên kết giữa bài hướng dẫn và công ty/tổ chức tương ứng trong hệ thống.

- **tags**:hoặc 3 từ khóa liên quan, hãy chọn [từ danh sách thẻ của Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: Danh mục con tương ứng với nội dung của hướng dẫn (ví dụ với ví (wallet): `desktop`, `hardware`, `mobile`, `backup`);

- **level**: Mức độ khó:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id**: `professor_id` của bạn (UUID) như được hiển thị trên [hồ sơ giảng viên của bạn](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language**: Ngôn ngữ gốc (ví dụ: `vi`, `en`);

- **proofreading**: Thông tin về quá trình hiệu đính. Việc bạn tự soát lỗi bài của mình được tính là lần xác thực đầu tiên:
    - **language**: Mã ngôn ngữ của quá trình hiệu đính (ví dụ: `vi`, `en`,...).
    - **last_contribution_date**: Ngày hiện tại.
    - **urgency**: 1
    - **contributor_names**: ID GitHub của bạn.
    - **reward**: 0

Để biết thêm chi tiết về ID giảng của bạn, vui lòng tham khảo hướng dẫn tương ứng:

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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


- Điền các thuộc tính file Markdown với:
    - Tiêu đề (`name`).
    - Một mô tả ngắn (`description`).
- Thêm ảnh bìa ở đầu bài hướng dẫn bằng cú pháp Markdown (thay thế "green" bằng tên tương ứng, như tên công cụ mà bạn đề cập trong bàiị):

```
![cover-green](assets/cover.webp)
```

- Viết nội dung hướng dẫn bằng Markdown:
    - Sử dụng các tiêu đề (`##`), danh sách và đoạn văn rõ ràng.
    - Chèn hình ảnh bằng cú pháp Markdown:

```
![nom-image](assets/en/001.webp)
```

- Đặt sơ đồ và hình ảnh vào thư mục ngôn ngữ tương ứng trong thư mục `/assets`.

### 6 - Lưu và gửi bài hướng dẫn

- Lưu các thay đổi cục bộ bằng cách tạo commit kèm mô tả.
- Đẩy các thay đổi lên bản fork GitHub của bạn.

```
# Tạo commit với tin nhắn mô tả
git commit -m "Added green-wallet tutorial"

# Đẩy thay đổi lên bản fork
git push origin tuto-green-wallet-loic
```

- Sau khi hoàn tất, tạo một Pull Request (PR) trên GitHub.
- Thêm tiêu đề và mô tả ngắn gọn cho PR. Đề cập ID của issue tương ứng trong bình luận.

### 7 - Kiểm tra lại và merge

- Đợi xác nhận hoặc phản hồi từ quản trị viên.
- Nếu cần thiết, thực hiện sửa lỗi và đẩy các commit mới.

```
# Tạo một commit mới kèm mô tả chỉnh sửa
git commit -m "Corrections following the review of the green-wallet tutorial"

# Đẩy các thay đổi của bạn lên bản fork
git push origin tuto-green-wallet-loic
```

- Sau khi PR đã được merge, bạn có thể xóa nhánh làm việc của mình.

## Tiêu chuẩn tạo nội dung

- Định dạng được hỗ trợ:
    - Markdown cổ điển: danh sách, liên kết, hình ảnh, trích dẫn, in đậm, in nghiêng,...
    - LaTeX (chỉ dạng khối, không in-line): nằm trong cặp dấu `$$`.
    - Mã in-line: sử dụng dấu backtick đơn (`).
    - Khối mã (Code blocks): sử dụng ba dấu backtick (```)

```
print("Hello, Bitcoin!")
```

- **Hình ảnh minh họa và sơ đồ**:
    - Tất cả hình ảnh phải ở định dạng WebP. Sử dụng công cụ miễn phí này để chuyển đổi chúng nếu cần: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Đặt tên hình ảnh bằng 2 hoặc 3 chữ số (ví dụ: `001.webp`, `002.webp`).
    - Đối với hướng dẫn về ví di động hoặc ví cứng (mobile or hardware wallet), hãy sử dụng mock-ups.
    - Chỉ sử dụng hình ảnh tự tạo hoặc không có bản quyền.
    - Hãy đảm bảo chúng có liên quan và ở chất lượng cao.
- **Quy chuẩn đồ họa**:
    - Phông chữ: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Màu sắc của Plan ₿ Academy:
        - Màu cam: `#FF5C00`
        - Đen: `#000000`
        - Trắng: `#FFFFFF`

Nếu bạn gặp khó khăn kỹ thuật, đừng ngần ngại yêu cầu hỗ trợ trên [nhóm Telegram dành cho việc đóng góp](https://t.me/PlanBNetwork_ContentBuilder). Cảm ơn bạn rất nhiều!
