---
name: Đóng góp - Hướng dẫn sử dụng GitHub Desktop (Trung cấp)
description: Hướng dẫn đầy đủ để đề xuất hướng dẫn về Plan ₿ Academy bằng GitHub Desktop
---
![cover](assets/cover.webp)

Trước khi làm theo hướng dẫn này để thêm hướng dẫn mới, bạn cần phải hoàn thành một số bước chuẩn bị sơ bộ. Nếu chưa thực hiện, mời bạn tham khảo bài hướng dẫn nhập môn trước khi quay lại đây:

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Bạn cần phả có:

- Chủ đề cho bài hướng dẫn.
- Liên hệ với đội ngũ Plan ₿ Academy qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network;
- Lựa chọn các công cụ đóng góp phù hợp.

Trong bài hướng dẫn này, chúng ta sẽ tìm hiểu cách thêm bài viết lên Plan ₿ Academy bằng cách thiết lập môi trường cục bộ với GitHub Desktop. Nếu bạn đã thành thạo Git, bài hướng dẫn chi tiết này có thể không cần thiết. Thay vào đó, tôi khuyên bạn nên xem tài liệu tóm tắt các quy tắc chính tại đây:

- **Người dùng có kinh nghiệm**:

https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Nếu bạn không muốn thiết lập môi trường cục bộ, hãy làm theo bài hướng dẫn dành cho người mới bắt đầu để thực hiện thay đổi trực tiếp qua giao diện web của GitHub:

- **Người mới bắt đầu (giao diện web)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Các bước chuẩn bị cần thiết

Các phần mềm cần thiết

- [GitHub Desktop](https://desktop.github.com/);
- Trình soạn thảo Markdown như [Obsidian](https://obsidian.md/);
- Code editor ([VS Code](https://code.visualstudio.com/) hoặc [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Các chuẩn bị cần có trước khi bắt đầu:

- [Tài khoản GitHub](https://github.com/signup);
- Bản fork của [repository Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content);
- [Hồ sơ giáo sư trên Plan ₿ Academy](https://planb.academy/professors) (chỉ khi bạn đề xuất một bài hướng dẫn hoàn chỉnh).

Nếu bạn cần trợ giúp để đạt được các điều kiện tiên quyết này, các hướng dẫn khác của tôi sẽ hỗ trợ bạn:

Nếu cần hỗ trợ các bước chuẩn bị này, các bài hướng dẫn khác của tôi sẽ giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

Khi mọi thứ đã sẵn sàng và môi trường cục bộ đã được thiết lập với bản fork riêng, bạn có thể bắt đầu thêm bài hướng dẫn.

## 1 - Tạo một nhánh mới

Mở trình duyệt và truy cập vào trang fork của bạn trên GitHub (URL có dạng: `https://github.com/[tên-người-dùng]/bitcoin-educational-content`):

![TUTO](assets/fr/03.webp)

Đảm bảo bạn đang ở nhánh chính `dev` và nhấn nút `Sync fork`. Nếu bản fork chưa được cập nhật, GitHub sẽ đề xuất cập nhật nhánh. Hãy tiến hành cập nhật. Nếu nhánh đã mới nhất, GitHub sẽ thông báo cho bạn:

![TUTO](assets/fr/04.webp)

Mở phần mềm GitHub Desktop và kiểm tra xem bản fork của bạn đã được chọn ở góc trên bên trái cửa sổ chưa:

![TUTO](assets/fr/05.webp)

Nhấn nút `Fetch origin`. Nếu bản cục bộ đã cập nhật, GitHub Desktop sẽ không đề xuất bất kỳ hành động bổ sung nào. Nếu không, tùy chọn `Pull origin` sẽ xuất hiện. Nhấn vào đó để cập nhật bản cục bộ ở máy tính:

![TUTO](assets/fr/06.webp)

Xác nhận bạn đang ở nhánh chính `dev`:

![TUTO](assets/fr/07.webp)

Nhấn vào nhánh này, sau đó chọn `New Branch`:

![TUTO](assets/fr/08.webp)

Đảm bảo rằng nhánh mới dựa trên repository gốc: `Plan ₿ Academy/bitcoin-educational-content`.

Đặt tên nhánh rõ ràng về mục đích, sử dụng dấu gạch ngang giữa các từ. Ví dụ, nếu bạn viết bài về Sparrow Wallet, tên nhánh có thể là: `tuto-sparrow-wallet-loic`. Sau đó nhấn `Create branch`:

![TUTO](assets/fr/09.webp)

Nhấn `Publish branch` để lưu nhánh làm việc mới lên bản fork trực tuyến trên GitHub:

![TUTORIAL](assets/fr/10.webp)

Bây giờ, mọi thay đổi cục bộ sẽ chỉ được lưu trên nhánh này. Khi nhánh này được chọn trong GitHub Desktop, các tệp bạn thấy trên máy tính sẽ tương ứng với nội dung của nhánh đó (`tuto-sparrow-wallet-loic`), không phải của nhánh `dev`.

![TUTORIAL](assets/fr/11.webp)

Đối với mỗi bài viết mới mà bạn muốn xuất bản, bạn sẽ cần tạo một nhánh mới từ `dev`. Nhánh trong Git là phiên bản song song của dự án, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính, cho đến khi công việc sẵn sàng để merge.

## 2 - Thêm các files của bài hướng dẫn

Bạn có hai lựa chọn: sử dụng script Python để tự động tạo tài liệu hoặc tạo thủ công từng file.

### Sử dụng script Python

Bạn cần cài đặt Python 3.8 trở lên.

Script nằm tại đường dẫn: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Trong thư mục đó, cài đặt các thư viện cần thiết:

```
pip install -r requirements.txt
```

Khởi động phần mềm:

```
python3 main.py
```

Giao diện người dùng đồ họa (GUI) sẽ mở ra. Lần chạy đầu tiên, bạn sẽ cần nhập tất cả thông tin cần thiết, script sẽ ghi nhớ thông tin này của bạn cho những lần chạy sau.

![DATA-CREATOR-PY](assets/fr/37.webp)

Nhập đường dẫn cục bộ đến thư mục `/tutorials` (ví dụ: `.../bitcoin-educational-content/tutorials/`). Bạn có thể nhập thủ công hoặc nhấp vào nút "Browse" để điều hướng bằng ừng dụng File Explorer.

![DATA-CREATOR-PY](assets/fr/38.webp)

Chọn ngôn ngữ mà bạn sẽ sử dụng để viết bài.

![DATA-CREATOR-PY](assets/fr/39.webp)

Nhập GitHub ID của bạn.

![DATA-CREATOR-PY](assets/fr/40.webp)

Tiếp theo, bạn cần điền thông tin cho hồ sơ giảng viên của mình. Có một số lựa chọn sau đây:
- Nhập các chữ cái đầu tiên của tên của bạn vào trường "Professor Name". Tên của bạn sẽ xuất hiện trong danh sách thả xuống "Prof. Suggestions" nằm bên dưới. Chọn kết quả tương ứng.
- Hoặc bạn có thể nhấp trực tiếp vào danh sách thả xuống "Prof. Suggestions" và chọn tên của mình.

Thao tác này sẽ tự động điền mã UUID của giảng viên vào trường tương ứng.

![DATA-CREATOR-PY](assets/fr/41.webp)

Nếu bạn chưa có hồ sơ giáo sư, hãy xem hướng dẫn này:

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Sau đó nhấn vào nút "New Tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Chọn một danh mục chính và danh mục con phù hợp cho bài hướng dẫn.
![DATA-CREATOR-PY](assets/fr/43.webp)

Chọn mức độ khó.

![DATA-CREATOR-PY](assets/fr/44.webp)

Đặt tên thư mục của bài hướng dẫn. Tên của thư mục này phải phản ánh phần mềm/công cụ được đề cập trong hướng dẫn, sử dụng dấu gạch nối `-` giữa các từ. Ví dụ: `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` là UUID của công ty hoặc tổ chức đứng sau công cụ được liệt kê [từ danh sách các dự án](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ví dụ, nếu bạn tạo một hướng dẫn về phần mềm Green Wallet, bạn có thể tìm thấy `project_id` trong file sau: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Thông tin này được thêm vào file YAML của bài hướng dẫn vì Plan ₿ Academy duy trì cơ sở dữ liệu về tất cả các công ty và tổ chức hoạt động trên Bitcoin hoặc các dự án liên quan. Bằng cách thêm `project_id`, bạn sẽ tạo ra mối liên kết giữa bài hướng dẫn và công ty/tổ chức tương ứng trong hệ thống.

***Cập nhật:*** Trong phiên bản mới của script này, bạn không cần phải nhập thủ công `project_id` nữa. Bạn có thể tìm dự án theo tên và tự động lấy `project_id` tương ứng. Nhập phần đầu của tên dự án vào trường "Project Name" để tìm kiếm, sau đó chọn công ty mong muốn từ menu thả xuống. `project_id` sẽ tự động được điền vào trường bên dưới. Bạn cũng có thể nhập thủ công nếu cần.

![DATA-CREATOR-PY](assets/fr/46.webp)

Chọn 2 hoặc 3 từ khóa có liên quan đến nội dung hướng dẫn của bạn, hãy chọn từ [danh sách thẻ của Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Phần mềm này cũng cung cấp chức năng tìm kiếm từ khóa với danh sách thả xuống.

![DATA-CREATOR-PY](assets/fr/47.webp)

Kiểm tra lại lần nữa, rồi nhấn "Create Tutorial". Thư mục và các files cần thiết sẽ được tạo tự động. Bạn có thể bỏ qua phần tạo thủ công và chuyển thẳng đến Bước 4.

![DATA-CREATOR-PY](assets/fr/48.webp)

Bây giờ bạn có thể bỏ qua phần phụ "Without my Python script" cũng như bước 3, "Fill in the YAML file", vì script đã hoàn tất các hành động này cho bạn. Tiến hành trực tiếp đến bước 4 và bắt đầu viết hướng dẫn của bạn.

Để biết thêm thông tin về script Python này, hãy xem file [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Tạo thủ công (Không dùng script)

Truy cập thư mục `bitcoin-educational-content`, thư mục này đại diện cho bản clone cục bộ của repository của bạn. Thường nó sẽ nằm trong `Documents\GitHub\bitcoin-educational-content`.

Chọn thư mục con phù hợp (ví dụ: `wallet` cho các bài về ví, hoặc `contribution` cho các bài về đóng góp nội dung). Trong ví dụ sau, tôi muốn thêm bài hướng dẫn về Sparrow Wallet, chúng tôi sẽ điều hướng đến đường dẫn sau: `bitcoin-educational-content\tutorials\wallet`, tương ứng với phần `WALLET` trên trang web:

![TUTO](assets/fr/12.webp)

Trong thư mục `wallet`, bạn cần tạo một thư mục mới dành riêng cho bài hướng dẫn của bạn. Tên của thư mục này phải liên quan đến phần mềm/công cụ được đề cập trong hướng dẫn. Các từ phải được nối với nhau bằng dấu gạch ngang. Đối với ví dụ của tôi, thư mục sẽ có tiêu đề là `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

Trong thư mục này, thêm các thành phần sau:

- Tạo thư mục `assets` - dùng để lưu trữ tất cả các hình ảnh minh họa cần thiết cho bài hướng dẫn.
- Trong thư mục `assets` này, tạo thư mục theo mã ngôn ngữ (ví dụ: `vi` cho tiếng Việt hoặc `en` cho tiếng Anh) để chứa ảnh minh họa, sơ đồ, ảnh chụp màn hình...
- Tạo file `tutorial.yml` để lưu metadata.
- Tạo file Markdown cho nội dung bài hướng dẫn. File này phải được đặt tên theo mã ngôn ngữ của bài viết. Ví dụ, đối với hướng dẫn được viết bằng tiếng Việt, tên file sẽ là `vi.md`.

![TUTO](assets/fr/14.webp)

Tóm lại, đây là cấu trúc phân cấp các file cần tạo:

```
bitcoin-educational-content/
└── tutorials/
    └── wallet/
        └── sparrow-wallet/
            ├── assets/
            │   ├── en/
            ├── tutorial.yml
            └── vi.md
```

## 3 - Điền thông tin vào file YAML

Sao chép mẫu sau vào `tutorial.yml`:

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

Sau khi hoàn tất việc sửa đổi file `tutorial.yml`, hãy lưu tài liệu bằng cách nhấp vào `File > Save`:

![TUTO](assets/fr/16.webp)

Bây giờ bạn có thể đóng trình soạn thảo.

## 4 - Viết nội dung vào fệp Markdown

Mở file `vi.md` (hoặc ngôn ngữ tương ứng) bằng Obsidian. Trong Obsidian, ở phía bên trái của cửa sổ, cuộn qua cây thư mục cho đến khi bạn tìm thấy thư mục bài hướng dẫn của mình và file bạn đang tìm kiếm:

![TUTO](assets/fr/18.webp)

Nhấp vào để mở file:

![TUTO](assets/fr/19.webp)

Điền phần thuộc tính (Properties) ở đầu tài liệu:

![TUTO](assets/fr/20.webp)

Thêm vào theo mẫu sau:

```
---
name: [Tiêu đề]
description: [Mô tả]
---
```

![TUTO](assets/fr/21.webp)

Nhập tiêu đề và mô tả ngắn gọn về bài hướng dẫn đó:

![TUTO](assets/fr/22.webp)

Chèn ảnh bìa ngay phía dưới:

```
![cover-sparrow](assets/cover.webp)
```

Cú pháp này sẽ hữu ích bất cứ khi nào cần thêm hình ảnh vào hướng dẫn của bạn. Dấu chấm than cho biết đó là hình ảnh, với văn bản thay thế (alt) được đặt giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được đặt trong cặp dấu ngoặc đơn:

![TUTO](assets/fr/23.webp)

## 5 - Thêm logo và ảnh bìa

Trong thư mục assets/, bạn phải thêm:

- `logo.webp`: Ảnh đại diện bài viết (hình vuông). Bạn được tự do lựa chọn logo của phần mềm được đề cập trong hướng dẫn hoặc bất kỳ hình ảnh liên quan nào, miễn là không vi phạm bản quyền

- `cover.webp`: Ảnh bìa hiển thị đầu bài viết. Hãy đảm bảo ảnh này tuân thủ quyền sử dụng và phù hợp với bối cảnh hướng dẫn của bạn.

Cả hai phải ở định dạng `.webp`.

## 6 - Viết nội dung và thêm hình ảnh minh họa

Giờ hãy bắt đầu viết nội dung cho bài hướng dẫn của bạn. Sử dụng `##` cho các tiêu đề phụ.

![TUTO](assets/fr/24.webp)

Lưu tất cả ảnh minh họa hoặc sơ đồ vào thư mục ngôn ngữ tương ứng (ví dụ: `assets/vi/`). Cố gắng hết sức để tránh đưa quá nhiều văn bản vào hình ảnh, nhằm giúp nội dung của bạn dễ tiếp cận với đối tượng quốc tế. Tất nhiên, phần mềm được giới thiệu sẽ chứa văn bản, nhưng nếu bạn thêm sơ đồ hoặc chỉ dẫn bổ sung vào ảnh chụp màn hình phần mềm, thì cũng không cần có văn bản trong hình, nếu thực sự cần thiết, hãy sử dụng tiếng Anh.

![TUTO](assets/fr/25.webp)

Để đặt tên cho hình ảnh, bạn chỉ cần sử dụng các số tương ứng với thứ tự xuất hiện của chúng trong hướng dẫn, được định dạng với hai chữ số (hoặc ba chữ số nếu hướng dẫn của bạn có nhiều hơn 99 hình ảnh). Ví dụ, đặt tên hình ảnh đầu tiên là `01.webp`, hình ảnh thứ hai là `02.webp`, v.v.

Hình ảnh phải ở định dạng `.webp`. Nếu cần, bạn có thể sử dụng [phần mềm chuyển đổi hình ảnh của tôi](https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Để chèn sơ đồ vào tài liệu, hãy sử dụng lệnh Markdown sau, đảm bảo là văn bản thay thế (alt) phù hợp và đường dẫn của hình ảnh phải chính xác:

```
![sparrow](assets/fr/01.webp)
```

Dấu chấm than cho biết đó là hình ảnh, với văn bản thay thế (alt) được đặt giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được đặt trong cặp dấu ngoặc đơn.

Nếu bạn muốn tạo sơ đồ, hãy đảm bảo tuân thủ quy tắc hình ảnh của Plan ₿ Academy để đảm bảo tính nhất quán:

- **Phông chữ**: Sử dụng [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Màu sắc**:
  - Màu cam: #FF5C00
  - Đen: #000000
  - Trắng: #FFFFFF

**Điều tối quan trọng là tất cả hình ảnh được tích hợp vào các bài hướng dẫn của bạn phải không vi phạm bản quyền hoặc tuân thủ giấy phép của file nguồn.** Ngoài ra, tất cả sơ đồ được xuất bản trên Plan ₿ Academy đều được cung cấp theo giấy phép CC-BY-SA, giống như văn bản.

**-> Mẹo:** Khi chia sẻ file công khai, chẳng hạn như hình ảnh, điều quan trọng là phải xóa mọi metadata không cần thiết. Những metadata này có thể chứa thông tin nhạy cảm, như dữ liệu vị trí, ngày tạo hoặc thông tin chi tiết về tác giả. Để bảo vệ quyền riêng tư của bạn, bạn nên xóa những dữ liệu này. Để đơn giản hóa quy trình này, bạn có thể sử dụng các công cụ chuyên dụng như [Exif Cleaner](https://exifcleaner.com/), cho phép dọn dẹp metadata của tài liệu thông qua thao tác kéo và thả đơn giản.

## 7 - Lưu và gửi bài

Sau khi hoàn thành bài hướng dẫn, bước tiếp theo là gửi **Pull Request**. Quản trị viên sẽ bổ sung bất kỳ bản dịch nào còn thiếu cho bài hướng dẫn của bạn, nhờ vào phương pháp dịch tự động kết hợp với việc rà soát của cộng tác viên.

Để tiếp tục Pull Request, hãy mở phần mềm GitHub Desktop. Phần mềm sẽ tự động phát hiện những thay đổi bạn đã thực hiện cục bộ trên nhánh của mình so với repository gốc. Trước khi tiếp tục, hãy kiểm tra cẩn thận ở phía bên trái của giao diện để đảm bảo những thay đổi này khớp với những gì bạn muốn:

![TUTO](assets/fr/28.webp)

Nhập tiêu đề cho commit và nhấn `Commit to [tên-nhánh]`.

![TUTO](assets/fr/29.webp)

Một commit là 1 bản lưu các thay đổi được thực hiện cho nhánh, kèm theo mô tả, cho phép theo dõi sự phát triển của dự án theo thời gian. Đây giống như một chốt kiểm tra trung gian.

Nhấn Push origin để đẩy dữ liệu lên bản fork trên GitHub.

![TUTO](assets/fr/30.webp)

Nếu bạn chưa hoàn thành hướng dẫn, bạn có thể quay lại sau và thêm các commit mới. Nếu bạn đã hoàn tất các thay đổi, hãy nhấn vào nút Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Hãy kiểm tra lại lần cuối để đảm bảo rằng các sửa đổi của bạn đã chính xác, sau đó nhấp vào nút `Create pull request`:

![TUTO](assets/fr/32.webp)

"Pull Request" là yêu cầu được thực hiện để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của repository Plan ₿ Academy, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được merge.

Bạn sẽ được tự động chuyển hướng đến trình duyệt của mình trên GitHub tới trang chuẩn bị cho Pull Request:

![TUTO](assets/fr/33.webp)

Nhập tiêu đề và mô tả ngắn mô tả những thay đổi này (nếu bạn có issue liên quan đến việc tạo bài hướng dẫn, hãy nhớ ghi chú trong bình luận `Closes #{Issue ID}`), sau đó nhấp vào nút `Create pull request` màu xanh lá cây để hoàn tất:

![TUTO](assets/fr/34.webp)

PR của bạn sau đó sẽ hiển thị trong tab `Pull Request` của repository chính của Plan ₿ Academy. Tất cả những gì bạn phải làm là đợi cho đến khi quản trị viên liên hệ với bạn để xác nhận đã merge hoặc yêu cầu bất kỳ sửa đổi bổ sung nào.

![TUTO](assets/fr/35.webp)

Sau khi PR của bạn đã được hợp nhất với nhánh chính, hãy nhánh công việc của mình (`tuto-sparrow-wallet`) để duy trì lịch sử sạch sẽ trên bản fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang PR của bạn:

![TUTO](assets/fr/36.webp)

Trên phần mềm GitHub Desktop, bạn có thể chuyển lại nhánh chính (`dev`).

![TUTO](assets/fr/07.webp)

Nếu bạn muốn thực hiện thay đổi cho bài hướng dẫn của mình sau khi đã gửi PR, quy trình này sẽ phụ thuộc vào trạng thái hiện tại của PR:

- Nếu PR của bạn vẫn đang mở và chưa được merge, hãy thực hiện các thay đổi cục bộ trong khi vẫn giữ nguyên nhánh. Sau khi hoàn tất các sửa đổi, hãy sử dụng nút `Push origin` để thêm một commit mới vào PR vẫn đang mở.

- Nếu PR của bạn đã được hợp nhất với nhánh chính, bạn cần bắt đầu lại quy trình bằng cách tạo một nhánh mới, sau đó gửi một PR mới. Hãy đảm bảo rằng repository trên máy tính của bạn được đồng bộ hóa với repository của Plan ₿ Academy trước khi tiếp tục.

Nếu gặp vấn đề hoặc khó khăn về mặt kỹ thuật, đừng ngần ngại yêu cầu hỗ trợ trong [nhóm Telegram cho cộng tác viên đóng góp nội dung](https://t.me/PlanBNetwork_ContentBuilder). Cảm ơn bạn!