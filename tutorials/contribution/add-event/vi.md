---
name: Thêm sự kiện trên Plan ₿ Academy
description: Làm thế nào để tôi đề xuất thêm sự kiện mới trên Plan ₿ Academy?
---
![event](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

Nếu bạn muốn thêm một sự kiện Bitcoin lên trang web Plan ₿ Academy để tăng sức lan tỏa cho sự kiện, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

![event](assets/01.webp)

- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- Truy cập vào [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/events/) trong phần `events/`:

![event](assets/02.webp)

- Nhấn vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:

![event](assets/03.webp)

- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:

![event](assets/04.webp)

- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:

![event](assets/05.webp)

- Tạo một thư mục cho sự kiện của bạn. Tại ô `Name your file...`, bạn nhập tên sự kiện bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, nếu sự kiện của bạn có tên là "Paris Bitcoin Conference", bạn nên ghi `paris-bitcoin-conference`. Ngoài ra, đừng quên thêm năm tổ chức sự kiện vào cuối tên thư mục, ví dụ: `paris-bitcoin-conference-2024`:

![event](assets/06.webp)

- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `paris-bitcoin-conference-2024/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:

![event](assets/07.webp)

- Trong thư mục này, bạn sẽ tạo một file YAML đầu tiên có tên `event.yml`:

![event](assets/08.webp)

- Điền thông tin về sự kiện của bạn vào file `event.yml` này theo mẫu sau:

```yaml
start_date:
end_date:
address_line_1:
address_line_2: 
address_line_3: 
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language: 
  - 
links:
  website:
  replay_url:    
  live_url :
tags: 
  - 
```

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2: 
address_line_3: 
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language: 
  - fr
  - en
  - es
  - it
links:
  website: https://paris.bitcoin.fr/conference
  replay_url:
  live_url :
tags: 
  - Bitcoiner
  - General
  - International
```
![event](assets/09.webp)

Nếu bạn chưa có một định danh "*project*" cho tổ chức của mình, bạn có thể thêm nó bằng cách theo dõi hướng dẫn khác này.

https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- Sau khi hoàn tất chỉnh sửa file, lưu thay đổi bằng cách nhấn nút `Commit changes...`:

![event](assets/10.webp)

- Thêm tiêu đề cho thay đổi của bạn, kèm theo mô tả ngắn:

![event](assets/11.webp)

- Nhấn vào nút `Propose changes`:

![event](assets/12.webp)

- Hệ thống sẽ chuyển bạn đến trang tổng hợp tất cả các thay đổi vừa thực hiện:

![event](assets/13.webp)

- Nhấn vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:

![event](assets/14.webp)

- Chọn bản fork của repository Plan ₿ Academy:

![event](assets/15.webp)

- Bạn sẽ thấy thông báo ở đầu cửa sổ về nhánh (branch) mới của bạn (thường tên là `patch-1`). Nhấn vào đó:

![event](assets/16.webp)

- Bây giờ, bạn đang ở trên nhánh làm việc của mình:

![event](assets/17.webp)

- Quay lại thư mục `events/` và chọn thư mục sự kiện mà bạn vừa tạo ở commit trước:

![event](assets/18.webp)

- Trong thư mục sự kiện, nhấp vào nút `Add file`, sau đó chọn `Create new file`:

![event](assets/19.webp)

- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:

![event](assets/20.webp)

- Trong thư mục `assets` này, tạo một file tên là `.gitkeep`:

![event](assets/21.webp)

- Nhấn vào nút `Commit changes...`:

![event](assets/22.webp)

- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, rồi nhấn `Commit changes`:

![event](assets/23.webp)

- Quay lại thư mục `assets`:

![event](assets/24.webp)

- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:

![event](assets/25.webp)

- Một trang mới sẽ mở ra. Kéo thả một ảnh đại diện cho sự kiện của bạn vào đây; ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:

![event](assets/26.webp)

- Đó có thể là logo, ảnh thu nhỏ (thumbnail), hoặc thậm chí là poster:

![event](assets/27.webp)

- Sau khi hình ảnh được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn `Commit changes`:

![event](assets/28.webp)

- Lưu ý, ảnh của bạn phải được đặt tên là `thumbnail` và phải ở định dạng `.webp`. Tên file đầy đủ phải là: `thumbnail.webp`:

![event](assets/29.webp)

- Quay lại thư mục `assets` và nhấp vào file `.gitkeep`:

![event](assets/30.webp)

- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn  `Delete file`:

![event](assets/31.webp)

- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes`:

![event](assets/32.webp)

- Thêm tiêu đề và mô tả cho commit của bạn, rồi nhấn vào `Commit changes`:

![event](assets/33.webp)

- Quay lại thư mục gốc của bản fork:

![event](assets/34.webp)

- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút  `Compare & pull request`:

![event](assets/35.webp)

- Thêm tiêu đề rõ ràng và mô tả cho PR (Pull Request) của bạn:

![event](assets/36.webp)

- Nhấn vào nút `Create pull request`:

![event](assets/37.webp)

Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy sách của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:

![event](assets/38.webp)

Chân thành cảm ơn sự đóng góp quý giá của bạn! :)
