---
name: Thêm Podcast trên Plan ₿ Academy
description: Làm thế nào để thêm một podcast mới trên Plan ₿ Academy?
---
![podcast](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

Bạn đang muốn thêm chương trình podcast về Bitcoin của mình lên trang web Plan ₿ Academy để tăng sức loan tỏa cho chương trình, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

![podcast](assets/01.webp)

- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- Truy cập vào [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) trong phần `resources/podcasts/`:
![podcast](assets/02.webp)
- Nhấn vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![podcast](assets/03.webp)
- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:
![podcast](assets/04.webp)
- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:
![podcast](assets/05.webp)
- Tạo một thư mục cho podcast của bạn. Tại ô `Name your file...`, bạn nhập tên của podcast bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, nếu chương trình của bạn có tên là "Super Podcast Bitcoin", bạn nên viết `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `super-podcast-bitcoin/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:
![podcast](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một file YAML đầu tiên có tên `podcast.yml`:
![podcast](assets/08.webp)
- Điền thông tin về podcast trong file `podcast.yml` theo mẫu này:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Dưới đây là thông tin chi tiết cho từng trường:

- **`name`**: Tên của podcast.
- **`host`**: Liệt kê tên hoặc bí danh của các diễn giả hoặc người dẫn chương trình. Mỗi tên ngăn cách nhau bằng dấu phẩy.
- **`language`**: Nhập mã ngôn ngữ tương ứng với ngôn ngữ được sử dụng trong podcast. Ví dụ: đối với tiếng Anh, hãy ghi là `en`; với tiếng Ý là `it`...

- **`links`**: Cung cấp các liên kết dẫn đến nội dung của bạn. Bạn có hai lựa chọn sau đây:
	- `podcast`: liên kết đến podcast của bạn,
	- `twitter`: liên kết đến hồ sơ Twitter (X) của podcast hoặc của tổ chức sản xuất chương trình,
	- `website`: liên kết đến trang web của podcast hoặc của tổ chức sản xuất chương trình.
- **`description`**: Thêm một mô tả ngắn về podcast. Mô tả phải được viết bằng ngôn ngữ được chỉ định trong trường `language:`.
- **`tags`**: Thêm 2 thẻ (tag) liên quan đến podcast của bạn. Ví dụ:
    - `bitcoin`
    - `technology`
    - `economy`
    - `education`...

- **`contributors`**: Thêm ID người đóng góp (contributor) của bạn nếu có.

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin là một chương trình phát trực tiếp về kỹ thuật được tổ chức hàng tuần trên Twitter, nhằm đi sâu vào giao thức Bitcoin, các giải pháp lớp hai (Layer 2), và tất cả những đột phá công nghệ ấn tượng nhất. Các người dẫn chương trình - Lounes, Pantamis, Loïc, và Sosthene sẽ trả lời câu hỏi của bạn, đồng thời mang đến một chương trình về Bitcoin chuyên sâu nhất thế giới.

tags:
  - bitcoin
  - technology
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Sau khi hoàn tất việc chỉnh sửa file này, hãy lưu lại bằng cách nhấn vào nút `Commit changes...`:
![podcast](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, kèm theo một mô tả ngắn gọn:
![podcast](assets/11.webp)
- Nhấn vào nút `Propose changes`:
![podcast](assets/12.webp)
- Hệ thống sẽ chuyển bạn đến trang tổng hợp tất cả các thay đổi vừa thực hiện:
![podcast](assets/13.webp)
- Nhấn vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:
![podcast](assets/14.webp)
- Chọn bản fork của repository Plan ₿ Academy:
![podcast](assets/15.webp)
- Bạn sẽ thấy thông báo ở đầu cửa sổ về nhánh (branch) mới của bạn (thường tên là `patch-1`). Nhấn vào đó:
![podcast](assets/16.webp)
- Bây giờ, bạn đang ở trên nhánh làm việc của mình:
![podcast](assets/17.webp)
- Quay lại thư mục `resources/podcast/` và chọn thư mục podcast bạn vừa tạo trong commit trước:
![podcast](assets/18.webp)
- Trong thư mục podcast của bạn, nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![podcast](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:
![podcast](assets/20.webp)
- Trong thư mục `assets` này, tạo một file tên là `.gitkeep`:
![podcast](assets/21.webp)
- Nhấn vào nút `Commit changes...`:
![podcast](assets/22.webp)
- Giữ tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, rồi nhấn `Commit changes`:
![podcast](assets/23.webp)
- Quay lại thư mục `assets`:
![podcast](assets/24.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![podcast](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo thả một ảnh đại diện cho hội nghị của bạn vào đây; ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:
![podcast](assets/26.webp)
- Lưu ý, hình ảnh của bạn phải có tỷ lệ khung hình vuông, để phù hợp nhất với trang web của chúng tôi:
![podcast](assets/27.webp)
- Sau khi hình ảnh được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn `Commit changes`: 
![podcast](assets/28.webp)
- Lưu ý, hình ảnh phải được đặt tên là `logo` và phải ở định dạng `.webp`. Tên file đầy đủ phải là: `logo.webp`:
![podcast](assets/29.webp)
- Quay lại thư mục `assets` và nhấp vào file trung gian `.gitkeep`:
![podcast](assets/30.webp)
- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn `Delete file`:
![podcast](assets/31.webp)
- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes`:
![podcast](assets/32.webp)
- Thêm một tiêu đề và mô tả cho commit này, sau đó nhấn vào nút `Commit changes`:
![podcast](assets/33.webp)
- Quay lại thư mục gốc của bản fork:
![podcast](assets/34.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút `Compare & pull request`:
![podcast](assets/35.webp)
- Thêm một tiêu đề và mô tả rõ ràng cho PR (Pull Request) của bạn:
![podcast](assets/36.webp)
- Nhấn vào nút `Create pull request`:
![podcast](assets/37.webp)

Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy bộ công cụ giáo dục (BET) của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:

![podcast](assets/38.webp)

Cảm ơn bạn rất nhiều vì đã đóng góp quý báu của mình! :)
