---
name: Thêm một cuốn sách vào Plan ₿ Academy
description: Làm thế nào để thêm một cuốn sách mới vào Plan ₿ Academy?
---
![book](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

**Bạn muốn thêm một cuốn sách liên quan đến Bitcoin trên Plan ₿ Academy để tăng độ nhận diện cho công sức của mình, nhưng không biết cách làm? Hướng dẫn này dành cho bạn!**

![book](assets/01.webp)

- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- Truy cập vào [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) trong phần `resources/books/`:
![book](assets/02.webp)
- Nhấn vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![book](assets/03.webp)
- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:
![book](assets/04.webp)
- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:
![book](assets/05.webp)
- Tạo một thư mục cho cuốn sách của bạn. Tại ô `Name your file...`, nhập tên cuốn sách bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, nếu cuốn sách của bạn có tên là "*My Bitcoin Book*", bạn nên ghi là `my-bitcoin-book`:
![book](assets/06.webp)
- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `my-bitcoin-book/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:
![book](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một file YAML đầu tiên có tên `book.yml`:
![book](assets/08.webp)
- Điền thông tin về cuốn sách của bạn vào file `book.yml` theo mẫu sau:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Dưới đây là thông tin chi tiết cho từng trường:
- **`author`**: Tên tác giả cuốn sách.
- **`level`**: Mức độ kiến thức cần thiết để đọc và hiểu sách. Chọn một trong các mức sau:
	- `beginner`
	- `intermediate`
  - `advanced`
  - `expert`
- **`tags`**: Thêm 2-3 thẻ (tag) liên quan đến cuốn sách của bạn. Ví dụ:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Sau khi hoàn tất chỉnh sửa file, lưu thay đổi bằng cách nhấn nút `Commit changes...`:
![book](assets/10.webp)
- Thêm tiêu đề cho thay đổi của bạn, kèm theo mô tả ngắn: ![book](assets/11.webp)
- Nhấn vào nút `Propose changes`:
![book](assets/12.webp)
- Hệ thống sẽ chuyển bạn đến trang tổng hợp tất cả các thay đổi vừa thực hiện:
![book](assets/13.webp)
- Nhấn vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:
![book](assets/14.webp)
- Chọn bản fork của repository Plan ₿ Academy:
![book](assets/15.webp)
- Bạn sẽ thấy thông báo ở đầu cửa sổ về nhánh (branch) mới của bạn (thường tên là `patch-1`). Nhấn vào đó:
![book](assets/16.webp)
- Bây giờ, bạn đang ở trên nhánh làm việc của mình:
![book](assets/17.webp)
- Quay lại thư mục `resources/books/` và chọn thư mục sách mà bạn vừa tạo ở commit trước:
![book](assets/18.webp)
- Trong thư mục của sách, nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![book](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:
![book](assets/20.webp)
- Trong thư mục `assets` này, tạo một file tên là `.gitkeep`:
![book](assets/21.webp)
- Nhấn vào nút `Commit changes...`:
![book](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, rồi nhấn `Commit changes`:
![book](assets/23.webp)
- Quay lại thư mục `assets`:
![book](assets/24.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![book](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo thả ảnh bìa sách của bạn vào khu vực tải lên. Ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:
![book](assets/26.webp)
- Lưu ý: Ảnh nên có định dạng giống bìa sách để phù hợp nhất với website, ví dụ như:
![book](assets/27.webp)
- Sau khi hình ảnh được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn `Commit changes`:
![book](assets/28.webp)
- Lưu ý quan trọng: Ảnh phải được đặt tên là `cover_en` nếu bìa bằng tiếng Anh và phải ở định dạng `.webp`. Tên file đầy đủ sẽ là `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, v.v. Nếu bạn muốn dùng bìa khác nhau cho từng ngôn ngữ (ví dụ sách dịch), bạn có thể đặt tất cả trong cùng thư mục assets:
![book](assets/29.webp)
- Quay lại thư mục `assets` và nhấn vào file `.gitkeep`:
![book](assets/30.webp)
- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn `Delete file`:
![book](assets/31.webp)
- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes...`:
![book](assets/32.webp)
- Thêm tiêu đề và mô tả cho commit của bạn, rồi nhấn vào `Commit changes`:
![book](assets/33.webp)
- Quay lại thư mục sách của bạn: ![book](assets/34.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![book](assets/35.webp)
- Tạo một file YAML mới bằng cách đặt tên bằng ngôn ngữ của sách. file này sẽ được sử dụng để mô tả sách. Ví dụ, nếu tôi muốn viết mô tả bằng tiếng Anh, tên file sẽ này là `en.yml`:
![book](assets/36.webp)
- Điền vào file YAML này theo mẫu sau:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Dưới đây là chi tiết cần điền cho mỗi trường:
- **`title`**: Tên sách, đặt trong dấu ngoặc kép.
- **`publication_year`**: Năm xuất bản sách.
- **`cover`**: Tên của file ảnh bìa tương ứng với ngôn ngữ của file YAML đang chỉnh sửa. Ví dụ, với file `en.yml` và ảnh bìa tiếng Anh đã tải lên trước đó là `cover_en.webp`, điền `cover_en.webp` trong trường này.
- **`description`**: Thêm một mô tả ngắn về sách. Mô tả phải bằng ngôn ngữ tương ứng với tên file YAML.
- **`contributors`**: Thêm ID người đóng góp (contributor) của bạn nếu có.

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
title: "Cuốn Sách Bitcoin Của Tôi"
publication_year: 2021
cover: cover_vi.webp
original: true
description: |
  Khám phá thế giới đột phá của Bitcoin với hướng dẫn toàn diện dành cho người mới bắt đầu. Cuốn Sách Bitcoin Của Tôi làm sáng tỏ những sự phức tạp của Bitcoin, cung cấp phần giới thiệu ngắn gọn và súc tích về cách thức hoạt động của giao thức. Từ công nghệ mang tính cách mạng cho đến tác động tiềm năng đối với nền kinh tế toàn cầu, cuốn sách này cung cấp những hiểu biết sâu sắc vô giá và kiến thức thực tế. Hoàn hảo cho những người mới làm quen với Bitcoin, sách bao gồm các kiến thức cơ bản, mẹo bảo mật và tương lai của tài chính kỹ thuật số. Hãy khám phá tương lai của tiền tệ và trang bị cho bản thân kiến thức để tự tin điều hướng trong kỷ nguyên số.

contributors:
  - pretty-private
```


![book](assets/37.webp)
- Nhấn vào nút `Commit changes...`:
![book](assets/38.webp)
- Đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, thêm tiêu đề, rồi nhấn vào `Commit changes`:
![book](assets/39.webp)
- Thư mục sách giờ đây sẽ trông như thế này:
![book](assets/40.webp)
- Nếu mọi thứ đều ổn, quay lại thư mục gốc của bản fork:
![book](assets/41.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút  `Compare & pull request`:
![book](assets/42.webp)
- Thêm tiêu đề rõ ràng và mô tả cho PR (Pull Request) của bạn:
![book](assets/43.webp)
- Nhấn vào nút `Create pull request`:
![book](assets/44.webp)


Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy sách của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:
![book](assets/45.webp)
Chân thành cảm ơn sự đóng góp quý giá của bạn! :)
