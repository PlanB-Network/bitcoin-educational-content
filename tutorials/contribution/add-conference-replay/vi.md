---
name: Thêm bản phát lại hội nghị (conference replay)
description: Làm thế nào để thêm bản phát lại của hội nghị trên Plan ₿ Academy?
---
![conference](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

Bạn muốn thêm bản phát lại hội nghị Bitcoin của mình trên Plan ₿ Academy để tăng sức lan tỏa cho sự kiện, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

Tuy nhiên, nếu bạn muốn đăng tải thông tin về một hội nghị sắp diễn ra trong tương lai, bạn nên đọc bài hướng dẫn này — ở đây, chúng tôi giải thích chi tiết cách thêm một sự kiện mới lên trang web.

https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097

![conference](assets/01.webp)

- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- Truy cập [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) trong phần `resources/conference/`:
![conference](assets/02.webp)
- Nhấn vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![conference](assets/03.webp)
- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:
![conference](assets/04.webp)
- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:
![conference](assets/05.webp)
- Tạo một thư mục cho hội nghị của bạn. Tại ô `Name your file...`, nhập tên hội nghị của bạn bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, nếu hội nghị của bạn có tên là "Paris Bitcoin Conference", bạn nên ghi `paris-bitcoin-conference`. Ngoài ra, đừng quên thêm năm tổ chức sự kiện vào cuối tên thư mục, ví dụ: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `paris-bitcoin-conference-2024/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:
![conference](assets/07.webp)
- Trong thư mục vừa tạo, bạn sẽ tạo một file YAML đầu tiên có tên `conference.yml`:
![conference](assets/08.webp)
- Điền thông tin liên quan đến hội nghị của bạn vào file này theo mẫu sau:

```yaml
year: 
name: 
project: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)

Nếu bạn chưa có một định danh "*project*" cho tổ chức của mình, bạn có thể thêm nó bằng cách theo dõi hướng dẫn khác này.

Nếu tổ chức/doanh nghiệp của bạn vẫn chưa có định danh "*project*", bạn có thể bổ sung thông tin này bằng cách làm theo hướng dẫn dưới đây.

https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- Sau khi hoàn tất chỉnh sửa file, lưu thay đổi bằng cách nhấn nút `Commit changes...`:
![conference](assets/10.webp)
- Thêm tiêu đề cho thay đổi của bạn, kèm theo mô tả ngắn:
![conference](assets/11.webp)
- Nhấn vào nút `Propose changes`:
![conference](assets/12.webp)
- Hệ thống sẽ chuyển bạn đến trang tổng hợp tất cả các thay đổi vừa thực hiện:
![conference](assets/13.webp)
- Nhấn vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:
![conference](assets/14.webp)
- Chọn bản fork của repository Plan ₿ Academy:
![conference](assets/15.webp)
- Bạn sẽ thấy thông báo ở đầu cửa sổ về nhánh (branch) mới của bạn (thường tên là `patch-1`). Nhấn vào đó:
![conference](assets/16.webp)
- Bây giờ, bạn đang ở trên nhánh làm việc của mình:
![conference](assets/17.webp)
- Quay lại thư mục `resources/conference/` và chọn thư mục hội nghị mà bạn vừa tạo ở commit trước:
![conference](assets/18.webp)
- Trong thư mục của sách, nhấn vào nút `Add file`, sau đó chọn `Create new file`:![conference](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:
![conference](assets/20.webp)
- Trong thư mục `assets` này, tạo một file tên là `.gitkeep`:
![conference](assets/21.webp)
- Nhấn vào nút `Commit changes...`:
![conference](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, rồi nhấn `Commit changes`:
![conference](assets/23.webp)
- Quay lại thư mục `assets`:
![conference](assets/24.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![conference](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo thả một ảnh đại diện cho hội nghị của bạn vào đây; ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:
![conference](assets/26.webp)
- Đó có thể là logo, ảnh thu nhỏ (thumbnail), hoặc thậm chí là poster:
![conference](assets/27.webp)
- Sau khi hình ảnh được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấn `Commit changes`:
![conference](assets/28.webp)
- Lưu ý, ảnh của bạn phải được đặt tên là `thumbnail` và phải ở định dạng `.webp`. Tên file đầy đủ phải là: `thumbnail.webp`:
![conference](assets/29.webp)
- Quay lại thư mục `assets` và nhấp vào file `.gitkeep`:
![conference](assets/30.webp)
- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn  `Delete file`:
![conference](assets/31.webp)
- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes`:
![conference](assets/32.webp)
- Thêm tiêu đề và mô tả cho commit của bạn, rồi nhấn vào `Commit changes`:
![conference](assets/33.webp)
- Quay lại thư mục hội nghị của bạn:
![conference](assets/34.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![conference](assets/35.webp)
- Tạo một file markdown (`.md`) mới và đặt tên theo mã ngôn ngữ bản địa của bạn. file này sẽ được sử dụng để chứa các bản phát lại của hội nghị. Ví dụ, nếu tôi muốn viết mô tả cho các hội nghị bằng tiếng Việt, tôi sẽ đặt tên file này là `vi.md`:
![conference](assets/36.webp)
- Điền thông tin vào file markdown này theo mẫu dưới đây; hãy điều chỉnh nội dung sao cho phù hợp với hội nghị của bạn:

```markdown
---
name: Hội Nghị Bitcoin Paris 2024
description: Hội nghị Bitcoin lớn nhất tại Pháp với hơn 8,000 người tham gia mỗi năm!
--- 

# Sân Khấu Chính

## Sáng Thứ Sáu

![video](https://youtu.be/XXXXXXXXXXXX)

## Chiều Thứ Sáu

![video](https://youtu.be/XXXXXXXXXXXX)

## Sáng Thứ Bảy

![video](https://youtu.be/XXXXXXXXXXXX)

## Chiều Thứ Bảy

![video](https://youtu.be/XXXXXXXXXXXX)

# Phòng Workshop

## Tương Lai của việc Đào Bitcoin: Thách Thức và Đổi Mới

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto

## Liệu Bitcoin Có Còn Giữ Được Sự Riêng Tư Không?

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto

## Bitcoin Core: Phân Tích Chuyên Sâu về Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Xây Dựng và Bảo Mật Ví Bitcoin Với Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto
```

![conference](assets/37.webp)

- Tại phần mở đầu của tài liệu (trong phần "front matter,"), điền tên hội nghị và năm của các bản phát lại vào trườn `name:`. Ở trường `description:`, viết một mô tả ngắn gọn về sự kiện bằng ngôn ngữ tương ứng của file. Ví dụ, đối với file `vi.md`, phần mô tả phải được viết bằng tiếng Việt. Đội ngũ Plan ₿ Academy sẽ đảm nhận việc dịch mô tả này bằng mô hình ngôn ngữ của họ.

- Các tiêu đề cấp độ một - Heading 1 (được đánh dấu bằng `#`), được dùng để phân loại hội nghị theo từng khu vực. Ví dụ, `# Sân Khấu Chính` cho sân khấu chính và `# Phòng Workshop` cho khu vực dành riêng cho các workshop.

- Các tiêu đề cấp độ hai - Heading 2 (được đánh dấu bằng `##`), được dùng để phân loại các video phát lại khác nhau. Nếu các buổi hội nghị được quay liên tục trong suốt một buổi, bạn có thể viết như sau: `## Sáng Thứ Sáu`. Nếu các buổi hội nghị được quay và phát sóng riêng lẻ, hãy đặt tên cho chúng bằng một tiêu đề cấp độ hai.

- Dưới mỗi tiêu đề cấp độ hai, hãy chèn một liên kết đến video phát lại tương ứng. Cú pháp sẽ là: `![video](https://youtu.be/XXXXXXXXXXXX)`, và thay thế `XXXXXXXXXXXX` bằng liên kết video thực tế.

- Nếu định dạng cho phép (các hội nghị riêng lẻ), bạn có thể thêm tên của các diễn giả. Để làm điều này, thêm trường `Diễn giả:` ngay bên dưới liên kết video, sau đó ghi tên hoặc bí danh của diễn giả. Nếu có nhiều diễn giả, ngăn cách các tên bằng dấu phẩy, như ví dụ này: `Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Sau khi đã hoàn tất các thay đổi trong file này, hãy lưu lại bằng cách nhấn vào nút `Commit changes...`:
![conference](assets/38.webp)
- Thêm một tiêu đề và mô tả ngắn gọn cho các thay đổi này:
![conference](assets/39.webp)
- Nhấn vào `Commit changes`:
![conference](assets/40.webp)
- Thư mục hội nghị giờ đây sẽ trông như thế này:
![conference](assets/41.webp)
- Nếu mọi thứ đều ổn, quay lại thư mục gốc của bản fork:
![conference](assets/42.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút  `Compare & pull request`:
![conference](assets/43.webp)
- Thêm tiêu đề rõ ràng và mô tả cho PR (Pull Request) của bạn:
![conference](assets/44.webp)
- Nhấn vào nút `Create pull request`:
![conference](assets/45.webp)

Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy sách của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:

![conference](assets/46.webp)

Chân thành cảm ơn sự đóng góp quý giá của bạn! :)

