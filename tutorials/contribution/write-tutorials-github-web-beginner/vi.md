---
name: Đóng góp - GitHub Web hướng dẫn (người mới bắt đầu)
description: Hướng dẫn đầy đủ về hướng dẫn Plan ₿ Academy với GitHub Web
---
![cover](assets/cover.webp)

Trước khi theo dõi bài hướng dẫn về cách thêm nội dung mới này, bạn cần hoàn thành một vài bước chuẩn bị sơ bộ. Nếu bạn chưa thực hiện, vui lòng xem bài hướng dẫn dưới đây trước, sau đó quay lại đây.

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Bạn đã có:

- Chủ đề cho bài hướng dẫn.
- Đã liên hệ với đội ngũ Plan ₿ Academy qua [nhóm Telegram](https://t.me/PlanBNetwork_ContentBuilder) hoặc paolo@planb.network.
- Lựa chọn công cụ đóng góp.

Trong bài hướng dẫn này, chúng ta sẽ tìm hiểu cách thêm bài hướng dẫn vào Plan ₿ Academy bằng phiên bản web của GitHub. Nếu bạn đã thành thạo Git, bài hướng dẫn chi tiết này có thể không cần thiết. Thay vào đó, tôi khuyên bạn nên xem một trong hai bài hướng dẫn còn lại, nơi tôi đề cập chi tiết các quy tắc cần tuân thủ và các bước thực hiện thay đổi từ môi trường cục bộ:

- **Người dùng có kinh nghiệm**:

https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- **Trung cấp (GitHub Desktop)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Các bước chuẩn bị cần thiết

Trước khi bắt đầu:

- Có một [tài khoản GitHub](https://github.com/signup);
- Đã fork [repository gốc của Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content);
- Có [hồ sơ giảng viên trên Plan ₿ Academy](https://planb.academy/professors) (chỉ cần khi bạn muốn đề xuất một bài hướng dẫn đầy đủ).

Nếu bạn cần trợ giúp về các bước này, hãy xem các bài hướng dẫn sau:

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.academy/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Khi mọi thứ đã sẵn sàng và bạn đã có bản fork của mình, bạn có thể bắt đầu thêm bài hướng dẫn.

## 1 - Tạo một nhánh mới

Mở trình duyệt và truy cập bản fork của bạn. URL sẽ có dạng: `https://github.com/[your-username]/bitcoin-educational-content`:

![GITHUB](assets/fr/01.webp)

Đảm bảo bạn đang ở nhánh chính `dev`, sau đó nhấn vào nút "*Sync fork*". Nếu bản fork chưa cập nhật, GitHub sẽ yêu cầu bạn cập nhật. Hãy tiến hành cập nhật:

![GITHUB](assets/fr/02.webp)

Nhấp vào nhánh `dev`, sau đó đặt tên cho nhánh làm việc mới sao cho tiêu đề phản ánh rõ mục đích, sử dụng dấu gạch ngang để ngăn cách các từ. Ví dụ, tôi muốn viết hướng dẫn về cách sử dụng Green Wallet, nhánh sẽ có tên là: `tuto-green-wallet-loic`. Sau khi nhập tên phù hợp, nhấn vào "*Create branch*" để tạo nhánh dựa trên `dev`:

![GITHUB](assets/fr/03.webp)

Hiện tại bạn đang ở trên nhánh làm việc mới:

![GITHUB](assets/fr/04.webp)

Bất kỳ thay đổi nào bạn thực hiện sẽ chỉ được lưu trên nhánh cụ thể này. 

Đối với mỗi bài viết mới, hãy luôn tạo một nhánh mới từ `dev`.

Trong Git, nhánh đại diện cho một phiên bản song song của dự án, cho phép bạn thực hiện các chỉnh sửa mà không ảnh hưởng đến nhánh chính, cho đến khi công việc của bạn sẵn sàng để tích hợp.

## 2 - Thêm các files cho bài hướng dẫn

Bây giờ nhánh làm việc đã được tạo, giờ chúng ta cần thiết lập cấu trúc thư mục và files cho bài hướng dẫn.

[//]: # (TODO)
Trong các tệp nhánh của bạn, bạn sẽ cần tìm thư mục con phù hợp để đặt hướng dẫn của mình. Việc sắp xếp các thư mục phản ánh các phần khác nhau của trang web Plan ₿ Academy. Trong ví dụ của chúng tôi, vì chúng tôi đang thêm hướng dẫn về Green Wallet, hãy đi đến đường dẫn sau: `bitcoin-educational-content\tutorials\wallet` tương ứng với phần `WALLET` của trang web:

![GITHUB](assets/fr/05.webp)

Trong thư mục `wallet`, tạo một thư mục mới dành riêng cho bài hướng dẫn của bạn. Tên thư mục nên chỉ rõ tên phần mềm/công cụ sẽ được đề cập trong bài hướng dẫn, sử dụng dấu gạch ngang để ngăn cách các từ, ví dụ `green-wallet`. Nhấn "*Add File*" rồi chọn "*Create new file*":

![GITHUB](assets/fr/06.webp)

Nhập tên thư mục theo sau là dấu gạch chéo `/` để xác nhận việc tạo thư mục.

![GITHUB](assets/fr/07.webp)

Trong thư mục mới này, bạn cần thêm các mục sau:

- Thư mục `assets` để lưu trữ tất cả các hình ảnh minh họa cần thiết.
- Trong thư mục `assets` này, tạo thư mục con theo mã ngôn ngữ gốc (ví dụ: `vi` cho tiếng Việt, `en` cho tiếng Anh). Đặt tất cả hình ảnh minh họa (sơ đồ, ảnh chụp màn hình...) vào đây.
- Một file `tutorial.yml` để ghi lại metadata.
- Một file Markdown (`.md`) chứa nội dung chính, tên tệp là mã ngôn ngữ của bài hướng dẫn mà bạn sẽ viết tới đây (ví dụ: tiếng Việt sẽ là `vi.md`).

Sơ đồ cấu trúc thư mục và files sẽ trông như thế này:

```
bitcoin-educational-content/
└── tutorials/
    └── wallet/
        └── green-wallet/
            ├── assets/
            │   ├── vi/
            ├── tutorial.yml
            └── vi.md
```

## 3 - Điền thông tin vào file YAML

Trong hộp để tạo file mới, nhập `tutorial.yml`:

![GITHUB](assets/fr/08.webp)

Sao chép và điền thông tin theo mẫu sau vào file `tutorial.yml`:

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

- **id**: Một UUID (_Universally Unique Identifier_) cho phép xác định duy nhất hướng dẫn. Bạn có thể tạo nó bằng [một công cụ trực tuyến](https://www.uuidgenerator.net/version4). Điều kiện duy nhất là UUID này phải ngẫu nhiên để tránh xung đột với một UUID khác trên nền tảng;

- **project_id**: UUID của công ty hoặc tổ chức đứng sau công cụ được trình bày trong hướng dẫn [từ danh sách các dự án](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Ví dụ, nếu bạn tạo một hướng dẫn về phần mềm Green Wallet, bạn có thể tìm thấy `project_id` trong tệp sau: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Thông tin này được thêm vào tệp YAML của hướng dẫn của bạn vì Plan ₿ Academy duy trì cơ sở dữ liệu về tất cả các công ty và tổ chức hoạt động trên Bitcoin hoặc các dự án liên quan. Bằng cách thêm `project_id` của thực thể liên kết với hướng dẫn của bạn, bạn tạo ra một liên kết giữa hai phần tử;

- **tags**: 2 hoặc 3 từ khóa liên quan đến nội dung hướng dẫn, được chọn độc quyền [từ danh sách thẻ của Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: Danh mục con tương ứng với nội dung của hướng dẫn, theo cấu trúc của trang Plan ₿ Academy (ví dụ: đối với ví: `desktop`, `hardware`, `mobile`, `backup`);

- **level**: Mức độ khó của hướng dẫn, được chọn từ:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id**: `professor_id` của bạn (UUID) như được hiển thị trên [hồ sơ giáo sư của bạn](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language**: Ngôn ngữ gốc của hướng dẫn (ví dụ: `fr`, `en`, v.v.);

- **proofreading**: Thông tin về quá trình hiệu đính. Hoàn thành phần đầu tiên, vì việc tự kiểm tra hướng dẫn của bạn được tính là một lần xác nhận:
    - **language**: Mã ngôn ngữ của quá trình hiệu đính (ví dụ: `fr`, `en`, v.v.).
    - **last_contribution_date**: Ngày hiện tại.
    - **urgency**: 1
    - **contributor_names**: ID GitHub của bạn.
    - **reward**: 0

Để biết thêm chi tiết về ID giáo viên của bạn, vui lòng tham khảo hướng dẫn tương ứng:

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

Sau khi điền xong, nhấn `Commit changes...`:

![GITHUB](assets/fr/09.webp)

Thêm tiêu đề và mô tả cho commit. Sau đó xác nhận bằng cách nhấp vào `Commit changes` để lưu lại các thay đổi vào nhánh của bạn.

![GITHUB](assets/fr/10.webp)

## 4 - Tạo thư mục con cho hình ảnh

Nhấp vào `Add file` một lần nữa rồi chọn `Create new file`:

![GITHUB](assets/fr/11.webp)

Nhập `assets` theo sau là dấu gạch chéo `/` để tạo thư mục:

![GITHUB](assets/fr/12.webp)

Lặp lại bước này trong thư mục `/assets` để tạo thư mục con ngôn ngữ, ví dụ `fr` nếu hướng dẫn của bạn bằng tiếng Pháp:

![GITHUB](assets/fr/13.webp)

Trong thư mục này, Tạo một file ảo tên là `.gitkeep` để GitHub giữ lại thư mục trống này. Sau đó nhấp vào `Commit changes...`.

![GITHUB](assets/fr/14.webp)

Kiểm tra lại xem bạn đang ở đúng nhánh chưa, sau đó nhấp vào `Commit changes`.

![GITHUB](assets/fr/15.webp)

## 5 - Tạo file Markdown

Giờ chúng ta sẽ tạo file Markdown để lưu nội dung của bài hướng dẫn:

![GITHUB](assets/fr/16.webp)

Nhấp vào `Add file` một lần nữa rồi chọn `Create new file`:

![GITHUB](assets/fr/17.webp)

Tạo tệp theo mã ngôn ngữ của bạn, ví dụ `fr.md` vì tôi sẽ viết bằng tiếng Pháp. Đi đến thư mục của bài hướng dẫn:

![GITHUB](assets/fr/18.webp)

Ở đầu tệp, thêm phần `Properties` (giữ tên nguyên tên biến `name` và `description` bằng tiếng Anh), sau đó nhập tiêu đề và mô tả của bạn sau các biến này:

```
---
name: [Tiêu đề]
description: [Mô tả]
---
```

![GITHUB](assets/fr/19.webp)

Nhập tiêu đề bài hướng dẫn kèm một mô tả ngắn gọn:

![GITHUB](assets/fr/20.webp)

Thêm đường dẫn ảnh bìa ngay sau đó:

```
![cover-green](assets/cover.webp)
```

Cú pháp này sẽ hữu ích bất cứ khi nào bạn cần thêm hình ảnh vào hướng dẫn của mình. Dấu chấm than chỉ ra một hình ảnh, có văn bản thay thế (alt) được chỉ định giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được chỉ định giữa các dấu ngoặc vuông:

![GITHUB](assets/fr/21.webp)

Nhấp vào nút "*Xác nhận thay đổi...*" để lưu tệp này.

![GITHUB](assets/fr/22.webp)

Kiểm tra xem bạn có đang ở đúng nhánh không, sau đó xác nhận cam kết.

![GITHUB](assets/fr/23.webp)

Theo mã ngôn ngữ của bạn, thư mục hướng dẫn của bạn bây giờ sẽ trông như thế này:

![GITHUB](assets/fr/24.webp)

## 6 - Thêm logo và bìa

Trong thư mục `assets`, bạn cần thêm một tệp có tên `logo.webp`, tệp này sẽ đóng vai trò là hình thu nhỏ cho bài viết của bạn. Hình ảnh này phải ở định dạng `.webp` và phải có kích thước vuông để phù hợp với giao diện người dùng.

Bạn được tự do lựa chọn logo phần mềm được sử dụng trong hướng dẫn hoặc bất kỳ hình ảnh có liên quan nào khác, miễn là không có bản quyền. Ngoài ra, hãy thêm một hình ảnh có tiêu đề `cover.webp` vào cùng một vị trí. Hình ảnh này sẽ được hiển thị ở đầu hướng dẫn của bạn. Hãy đảm bảo rằng hình ảnh này, giống như logo, tôn trọng quyền sử dụng và phù hợp với bối cảnh hướng dẫn của bạn.

Để thêm hình ảnh vào thư mục `/assets`, bạn có thể kéo và thả chúng từ các tệp cục bộ của mình. Đảm bảo rằng bạn đang ở trong thư mục `/assets` và ở nhánh bên phải, sau đó nhấp vào "*Commit changes*".

![GITHUB](assets/fr/26.webp)

Bây giờ bạn sẽ thấy hình ảnh xuất hiện trong thư mục.

![GITHUB](assets/fr/27.webp)

## 7 - Viết hướng dẫn

Tiếp tục viết hướng dẫn của bạn bằng cách ghi chú nội dung của bạn trong tệp Markdown với mã ngôn ngữ (trong ví dụ của tôi, bằng tiếng Pháp, đó là tệp `fr.md`). Đi đến tệp và nhấp vào biểu tượng bút chì:

![GITHUB](assets/fr/28.webp)

Bắt đầu viết hướng dẫn của bạn. Khi thêm phụ đề, hãy sử dụng định dạng Markdown phù hợp bằng cách thêm tiền tố `##` vào văn bản:

![GITHUB](assets/fr/29.webp)

Thay đổi giữa chế độ xem "*Chỉnh sửa*" và "*Xem trước*" để hình dung kết xuất tốt hơn.

![GITHUB](assets/fr/30.webp)

Để lưu công việc của bạn, hãy nhấp vào "*Commit Changes...*", đảm bảo rằng bạn đang ở đúng nhánh, sau đó xác nhận bằng cách nhấp vào "*Commit Changes*" một lần nữa.

![GITHUB](assets/fr/31.webp)

## 8 - Thêm hình ảnh

Thư mục con ngôn ngữ trong thư mục `/assets` (trong ví dụ của tôi: `/assets/en`) được sử dụng để lưu trữ sơ đồ và hình ảnh sẽ đi kèm với hướng dẫn của bạn. Tránh đưa văn bản vào hình ảnh của bạn càng nhiều càng tốt để nội dung của bạn dễ tiếp cận với đối tượng quốc tế. Tất nhiên, phần mềm được trình bày sẽ chứa văn bản, nhưng nếu bạn thêm sơ đồ hoặc chỉ dẫn bổ sung vào ảnh chụp màn hình phần mềm, hãy làm như vậy mà không có văn bản hoặc, nếu cần thiết, hãy sử dụng tiếng Anh.

Để đặt tên cho hình ảnh của bạn, chỉ cần sử dụng các số tương ứng với thứ tự xuất hiện của chúng trong hướng dẫn, được định dạng thành hai chữ số (hoặc ba chữ số nếu hướng dẫn của bạn chứa hơn 99 hình ảnh). Ví dụ, đặt tên cho hình ảnh đầu tiên của bạn là `01.webp`, hình ảnh thứ hai là `02.webp`, v.v.

Hình ảnh của bạn chỉ được phép ở định dạng `.webp`. Nếu cần, bạn có thể sử dụng [phần mềm chuyển đổi hình ảnh của tôi](https://github.com/LoicPandul/ImagesConverter).

![GITHUB](assets/fr/32.webp)

Bây giờ bạn đã thêm hình ảnh vào thư mục con, bạn có thể xóa tệp giả `.gitkeep`. Mở tệp này, nhấp vào ba dấu chấm nhỏ ở góc trên bên phải, sau đó nhấp vào "*Xóa tệp*".

![GITHUB](assets/fr/33.webp)

Lưu thay đổi của bạn bằng cách nhấp vào "*Xác nhận thay đổi...*".

![GITHUB](assets/fr/34.webp)

Để chèn sơ đồ từ thư mục con vào tài liệu biên tập, hãy sử dụng lệnh Markdown sau, chú ý chỉ định văn bản thay thế phù hợp và đường dẫn hình ảnh chính xác cho ngôn ngữ của bạn:

```
![green](assets/fr/01.webp)
```

Dấu chấm than ở đầu chỉ ra một hình ảnh. Văn bản thay thế, giúp truy cập và tham chiếu, được đặt giữa các dấu ngoặc vuông. Cuối cùng, đường dẫn đến hình ảnh được chỉ ra giữa các dấu ngoặc vuông.

![GITHUB](assets/fr/35.webp)

Nếu bạn muốn tạo sơ đồ của riêng mình, hãy đảm bảo tuân theo hướng dẫn đồ họa của Plan ₿ Academy để đảm bảo tính nhất quán về mặt hình ảnh:


- **Phông chữ**: Sử dụng [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Màu sắc**:
 - Màu cam: #FF5C00
 - Đen: #000000
 - Trắng: #FFFFFF

**Điều bắt buộc là tất cả hình ảnh tích hợp vào hướng dẫn của bạn phải không có bản quyền hoặc tôn trọng giấy phép tệp nguồn**. Do đó, tất cả các sơ đồ được xuất bản trên Plan ₿ Academy đều được cung cấp theo giấy phép CC-BY-SA, giống như văn bản.

**-> Mẹo:** Khi chia sẻ tệp ở nơi công cộng, chẳng hạn như hình ảnh, điều quan trọng là phải xóa siêu dữ liệu không cần thiết. Siêu dữ liệu này có thể chứa thông tin nhạy cảm, chẳng hạn như dữ liệu vị trí, ngày tạo và thông tin chi tiết về tác giả. Để bảo vệ quyền riêng tư của bạn, bạn nên xóa siêu dữ liệu này. Để đơn giản hóa thao tác này, bạn có thể sử dụng các công cụ chuyên dụng như [Exif Cleaner](https://exifcleaner.com/), cho phép bạn dọn dẹp siêu dữ liệu của tài liệu chỉ bằng thao tác kéo và thả đơn giản.

## 9 - Đề xuất hướng dẫn

Sau khi bạn hoàn thành việc viết hướng dẫn bằng ngôn ngữ bạn chọn, bước tiếp theo là gửi **Yêu cầu kéo**. Sau đó, quản trị viên sẽ thêm các bản dịch còn thiếu vào hướng dẫn của bạn bằng phương pháp dịch tự động của chúng tôi với sự hiệu đính của con người.

Để tiếp tục Yêu cầu kéo, sau khi lưu tất cả các thay đổi, hãy nhấp vào nút "*Đóng góp*", sau đó nhấp vào "*Mở yêu cầu kéo*":

![GITHUB](assets/fr/36.webp)

Yêu cầu kéo là yêu cầu được thực hiện để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của kho lưu trữ Plan ₿ Academy, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được hợp nhất.

Trước khi tiếp tục, hãy kiểm tra cẩn thận ở cuối giao diện để đảm bảo những thay đổi này là những gì bạn mong đợi:

![GITHUB](assets/fr/37.webp)

Đảm bảo rằng ở đầu giao diện, nhánh làm việc của bạn đã được hợp nhất vào nhánh `dev` của kho lưu trữ Plan ₿ Academy (là nhánh chính).

Nhập tiêu đề tóm tắt ngắn gọn những thay đổi bạn muốn hợp nhất với kho lưu trữ nguồn. Thêm bình luận ngắn gọn mô tả những thay đổi này (nếu bạn có số vấn đề liên quan đến việc tạo hướng dẫn của mình, hãy nhớ ghi chú `Đóng #{số vấn đề}` làm bình luận), sau đó nhấp vào nút "*Tạo yêu cầu kéo*" màu xanh lá cây để xác nhận yêu cầu hợp nhất:

![GITHUB](assets/fr/38.webp)

PR của bạn sau đó sẽ hiển thị trong tab "*Pull Request*" của kho lưu trữ Plan ₿ Academy chính. Tất cả những gì bạn phải làm bây giờ là đợi cho đến khi quản trị viên liên hệ với bạn để xác nhận rằng đóng góp của bạn đã được hợp nhất hoặc yêu cầu bất kỳ sửa đổi nào khác.

![GITHUB](assets/fr/39.webp)

Sau khi hợp nhất PR của bạn với nhánh chính, chúng tôi khuyên bạn nên xóa nhánh đang hoạt động của mình (trong ví dụ của tôi: `tuto-green-wallet`) để duy trì lịch sử fork sạch sẽ. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang PR của bạn:

![GITHUB](assets/fr/40.webp)

Nếu bạn muốn thay đổi nội dung đóng góp của mình sau khi đã gửi PR, các bước thực hiện sẽ tùy thuộc vào trạng thái hiện tại của PR của bạn:


- Nếu PR của bạn vẫn mở và chưa được hợp nhất, hãy thực hiện các thay đổi trên cùng một nhánh công việc. Các thay đổi cam kết sẽ được thêm vào PR vẫn mở của bạn;
- Trong trường hợp PR của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần phải thực hiện lại quy trình từ đầu bằng cách tạo nhánh mới, sau đó gửi PR mới. Đảm bảo nhánh của bạn được đồng bộ hóa với kho lưu trữ nguồn Plan ₿ Academy trên nhánh `dev` trước khi tiếp tục.

Nếu bạn gặp khó khăn về mặt kỹ thuật khi gửi hướng dẫn, vui lòng đừng ngần ngại yêu cầu trợ giúp trên [nhóm Telegram chuyên dụng của chúng tôi để đóng góp](https://t.me/PlanBNetwork_ContentBuilder). Cảm ơn bạn rất nhiều!
