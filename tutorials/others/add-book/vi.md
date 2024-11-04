---
name: Thêm Một Cuốn Sách vào Mạng PlanB
description: Làm thế nào để thêm một cuốn sách mới vào Mạng PlanB?
---
![book](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, cho phép bất kỳ ai cũng có thể đóng góp vào việc làm giàu cho nền tảng.

**Bạn muốn thêm một cuốn sách liên quan đến Bitcoin trên trang web Mạng PlanB và tăng độ nhìn thấy của công việc của bạn, nhưng bạn không biết làm thế nào? Hướng dẫn này dành cho bạn!**
![book](assets/01.webp)
- Đầu tiên, bạn cần phải có một tài khoản GitHub. Nếu bạn không biết cách tạo tài khoản, chúng tôi đã tạo một hướng dẫn chi tiết để hướng dẫn bạn.

https://planb.network/tutorials/others/create-github-account


- Truy cập vào [kho lưu trữ GitHub của PlanB dành cho dữ liệu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) trong phần `resources/books/`:
![book](assets/02.webp)
- Nhấp vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![book](assets/03.webp)
- Nếu bạn chưa bao giờ đóng góp vào nội dung của Mạng PlanB trước đây, bạn sẽ cần tạo một bản sao (fork) của kho lưu trữ gốc. Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của bạn, cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Nhấp vào nút `Fork this repository`:
![book](assets/04.webp)
- Bạn sẽ được chuyển đến trang chỉnh sửa GitHub:
![book](assets/05.webp)
- Tạo một thư mục cho cuốn sách của bạn. Để làm điều này, trong ô `Name your file...`, viết tên cuốn sách của bạn bằng chữ thường với dấu gạch ngang thay cho khoảng trắng. Ví dụ, nếu cuốn sách của bạn có tên là "*My Bitcoin Book*", bạn nên ghi `my-bitcoin-book`:
![book](assets/06.webp)
- Để xác nhận việc tạo thư mục, chỉ cần thêm một dấu gạch chéo sau tên cuốn sách của bạn trong cùng một ô, ví dụ: `my-bitcoin-book/`. Thêm một dấu gạch chéo tự động tạo ra một thư mục thay vì một tệp:
![book](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một tệp YAML đầu tiên có tên `book.yml`:
![book](assets/08.webp)
- Điền thông tin về cuốn sách của bạn vào tệp này sử dụng mẫu sau:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Dưới đây là chi tiết cần điền cho mỗi trường:
- **`author`**: Chỉ ra tên của tác giả cuốn sách.
- **`level`**: Chỉ ra mức độ cần thiết để có thể đọc và hiểu cuốn sách tốt. Chọn một mức độ trong số sau:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Thêm hai hoặc ba thẻ liên quan đến cuốn sách của bạn. Ví dụ:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Ví dụ, tệp YAML của bạn có thể trông như thế này:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Một khi bạn đã hoàn thành việc thay đổi tệp này, lưu chúng bằng cách nhấp vào nút `Commit changes...`:
![book](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, cũng như một mô tả ngắn gọn: ![sách](assets/11.webp)
- Nhấn vào nút `Propose changes` màu xanh:
![sách](assets/12.webp)
- Bạn sẽ đến trang tóm tắt tất cả các thay đổi của mình:
![sách](assets/13.webp)
- Nhấn vào ảnh đại diện GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:
![sách](assets/14.webp)
- Chọn fork của bạn từ kho lưu trữ PlanB Network:
![sách](assets/15.webp)
- Bạn sẽ thấy một thông báo ở đầu cửa sổ với nhánh mới của bạn. Có thể nó được gọi là `patch-1`. Nhấn vào đó:
![sách](assets/16.webp)
- Bây giờ bạn đang ở trên nhánh làm việc của mình:
![sách](assets/17.webp)
- Quay lại thư mục `resources/books/` và chọn thư mục của cuốn sách bạn vừa tạo trong commit trước:
![sách](assets/18.webp)
- Trong thư mục của cuốn sách bạn, nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![sách](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và xác nhận việc tạo nó bằng cách đặt một dấu gạch chéo `/` ở cuối:
![sách](assets/20.webp)
- Trong thư mục `assets` này, tạo một tệp tên là `.gitkeep`:
![sách](assets/21.webp)
- Nhấn vào nút `Commit changes...`:
![sách](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn vào `Commit changes`:
![sách](assets/23.webp)
- Quay lại thư mục `assets`:
![sách](assets/24.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![sách](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo và thả hình ảnh bìa của cuốn sách của bạn vào khu vực đó. Hình ảnh này sẽ được hiển thị trên trang web của PlanB Network:
![sách](assets/26.webp)
- Hãy cẩn thận, hình ảnh phải ở định dạng của một cuốn sách, để phù hợp nhất với trang web của chúng tôi, ví dụ như:
![sách](assets/27.webp)
- Một khi hình ảnh được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn vào `Commit changes`:
![sách](assets/28.webp)- Lưu ý, hình ảnh của bạn phải được đặt tên là `cover_en` nếu bìa là tiếng Anh và phải ở định dạng `.webp`. Do đó, tên tệp đầy đủ nên là `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, v.v. Nếu bạn muốn sử dụng một hình ảnh bìa khác nhau cho mỗi ngôn ngữ, ví dụ trong trường hợp dịch một cuốn sách, bạn có thể đặt chúng cùng một vị trí trong thư mục `assets`:
![sách](assets/29.webp)
- Quay lại thư mục `assets` của bạn và nhấn vào tệp trung gian `.gitkeep`:
![sách](assets/30.webp)
- Một khi đang ở trên tệp, nhấn vào 3 chấm nhỏ ở góc trên bên phải và sau đó chọn `Delete file`:
![sách](assets/31.webp)
- Đảm bảo bạn vẫn đang ở trên cùng một nhánh làm việc, sau đó nhấn vào nút `Commit changes...`:
![sách](assets/32.webp)
- Thêm tiêu đề và mô tả cho commit của bạn, sau đó nhấn vào `Commit changes`:
![sách](assets/33.webp)
- Quay lại thư mục sách của bạn: ![sách](assets/34.webp)
- Nhấn vào nút `Thêm tệp`, sau đó chọn `Tạo tệp mới`:
![sách](assets/35.webp)
- Tạo một tệp YAML mới bằng cách đặt tên cho nó với chỉ số ngôn ngữ của sách. Tệp này sẽ được sử dụng cho mô tả sách. Ví dụ, nếu tôi muốn viết mô tả của mình bằng tiếng Anh, tôi sẽ đặt tên tệp này là `en.yml`:
![sách](assets/36.webp)
- Điền vào tệp YAML này sử dụng mẫu sau:
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
- **`title`**: Chỉ định tên của sách trong dấu ngoặc kép.
- **`publication_year`**: Chỉ định năm sách được xuất bản.
- **`cover`**: Chỉ định tên của tệp tương ứng với hình ảnh bìa, phù hợp với ngôn ngữ của tệp YAML bạn đang chỉnh sửa. Ví dụ, nếu bạn đang chỉnh sửa tệp `en.yml` và bạn đã thêm trước đó hình ảnh bìa tiếng Anh có tiêu đề `cover_en.webp`, chỉ cần chỉ định `cover_en.webp` trong trường này.
- **`description`**: Thêm một đoạn văn ngắn mô tả sách. Mô tả phải bằng ngôn ngữ được chỉ định trong tiêu đề của tệp YAML.
- **`contributors`**: Thêm ID người đóng góp của bạn nếu bạn có.

Ví dụ, tệp YAML của bạn có thể trông như thế này:

```yaml
title: "Cuốn Sách Bitcoin Của Tôi"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Khám phá thế giới Bitcoin đột phá với hướng dẫn toàn diện này dành cho người mới bắt đầu. Cuốn Sách Bitcoin Của Tôi làm sáng tỏ những phức tạp của Bitcoin, cung cấp một giới thiệu rõ ràng và ngắn gọn về cách thức hoạt động của giao thức. Từ công nghệ cách mạng đến tác động tiềm năng đối với nền kinh tế toàn cầu, cuốn sách này cung cấp cái nhìn sâu sắc và kiến thức thực tế không thể thiếu. Hoàn hảo cho những người mới làm quen với Bitcoin, nó bao gồm các kiến thức cơ bản, mẹo bảo mật và tương lai của tài chính số. Hãy nhảy vào tương lai của tiền tệ và trang bị cho mình kiến thức để tự tin điều hướng trong kỷ nguyên số.

contributors:
  - pretty-private

![sách](assets/37.webp)
- Nhấn vào nút `Commit changes...`:
![sách](assets/38.webp)
- Đảm bảo rằng ô `Commit trực tiếp vào nhánh patch-1` đã được chọn, thêm tiêu đề, sau đó nhấn vào `Commit changes`:
![sách](assets/39.webp)
- Thư mục sách giờ đây sẽ trông như thế này:
![sách](assets/40.webp)
- Nếu mọi thứ đều ổn với bạn, quay lại gốc của fork của bạn:
![sách](assets/41.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của bạn đã được chỉnh sửa. Nhấn vào nút `So sánh & yêu cầu kéo`:
![sách](assets/42.webp)
- Thêm một tiêu đề rõ ràng và mô tả cho PR của bạn:
![sách](assets/43.webp)
- Nhấn vào nút `Tạo yêu cầu kéo`:
![sách](assets/44.webp)
Xin chúc mừng! PR của bạn đã được tạo thành công. Một quản trị viên giờ đây sẽ xem xét nó và, nếu mọi thứ đều ổn, hợp nhất nó vào kho lưu trữ chính của Mạng PlanB. Bạn sẽ thấy sách của mình xuất hiện trên trang web vài ngày sau.

Hãy chắc chắn theo dõi tiến trình của PR của bạn. Một quản trị viên có thể để lại bình luận yêu cầu thông tin bổ sung. Miễn là PR của bạn chưa được xác nhận, bạn có thể xem nó trong tab `Yêu cầu kéo` trên kho lưu trữ GitHub của Mạng PlanB.
Cảm ơn bạn rất nhiều vì đã đóng góp giá trị của mình! :)
