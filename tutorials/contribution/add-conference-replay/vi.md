---
name: Thêm Video Hội Nghị
description: Làm thế nào để thêm video hội nghị trên Mạng PlanB?
---
![conference](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được xuất bản trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, cho phép bất kỳ ai cũng có thể đóng góp vào việc làm giàu nền tảng.

Bạn muốn thêm video hội nghị Bitcoin của mình trên trang web Mạng PlanB và tăng sự nhìn nhận cho sự kiện này, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

Tuy nhiên, nếu bạn muốn thêm một hội nghị sẽ diễn ra trong tương lai, tôi khuyên bạn nên đọc hướng dẫn khác này trong đó chúng tôi giải thích cách thêm một sự kiện mới vào trang web.

https://planb.network/tutorials/others/contribution/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)
- Đầu tiên, bạn cần phải có một tài khoản trên GitHub. Nếu bạn không biết cách tạo tài khoản, chúng tôi đã làm một hướng dẫn chi tiết để hướng dẫn bạn.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Truy cập vào [kho lưu trữ GitHub của PlanB dành cho dữ liệu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) trong phần `resources/conference/`:
![conference](assets/02.webp)
- Nhấp vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![conference](assets/03.webp)
- Nếu bạn chưa bao giờ đóng góp vào nội dung của Mạng PlanB trước đây, bạn sẽ cần tạo một bản sao (fork) của kho lưu trữ gốc. Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của bạn, cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Nhấp vào nút `Fork this repository`:
![conference](assets/04.webp)
- Bạn sẽ được chuyển đến trang chỉnh sửa GitHub:
![conference](assets/05.webp)
- Tạo một thư mục cho hội nghị của bạn. Để làm điều này, trong ô `Name your file...`, viết tên hội nghị của bạn bằng chữ thường với dấu gạch ngang thay cho khoảng trắng. Ví dụ, nếu hội nghị của bạn có tên là "Paris Bitcoin Conference", bạn nên ghi `paris-bitcoin-conference`. Cũng thêm năm của hội nghị của bạn, ví dụ: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- Để xác nhận việc tạo thư mục, chỉ cần ghi một dấu gạch chéo sau tên của bạn trong cùng một ô, ví dụ: `paris-bitcoin-conference-2024/`. Thêm một dấu gạch chéo tự động tạo một thư mục thay vì một tệp:
![conference](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một tệp YAML đầu tiên có tên `conference.yml`:
![conference](assets/08.webp)
Điền thông tin liên quan đến hội nghị của bạn vào tệp này sử dụng mẫu này:
```yaml
year: 
name: 
builder: 
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

Ví dụ, tệp YAML của bạn có thể trông như thế này:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
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
Nếu bạn chưa có một định danh "*builder*" cho tổ chức của mình, bạn có thể thêm nó bằng cách theo dõi hướng dẫn khác này.
https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

- Sau khi bạn hoàn thành việc thay đổi tệp này, hãy lưu chúng bằng cách nhấp vào nút `Commit changes...`:
![hội nghị](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, cũng như một mô tả ngắn gọn:
![hội nghị](assets/11.webp)
- Nhấp vào nút màu xanh `Propose changes`:
![hội nghị](assets/12.webp)
- Bạn sẽ đến trang tóm tắt tất cả các thay đổi của bạn:
![hội nghị](assets/13.webp)
- Nhấp vào ảnh đại diện GitHub của bạn ở góc trên bên phải, sau đó vào `Your Repositories`:
![hội nghị](assets/14.webp)
- Chọn fork của bạn từ kho lưu trữ PlanB Network:
![hội nghị](assets/15.webp)
- Bạn sẽ thấy một thông báo ở đầu cửa sổ với nhánh mới của bạn. Có thể nó được gọi là `patch-1`. Nhấp vào nó:
![hội nghị](assets/16.webp)
- Bây giờ bạn đang ở trên nhánh làm việc của mình:
![hội nghị](assets/17.webp)
- Quay lại thư mục `resources/conference/` và chọn thư mục hội nghị mà bạn vừa tạo trong commit trước:
![hội nghị](assets/18.webp)
- Trong thư mục hội nghị của bạn, nhấp vào nút `Add file`, sau đó vào `Create new file`:
![hội nghị](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và xác nhận việc tạo nó bằng cách đặt một dấu gạch chéo `/` ở cuối:
![hội nghị](assets/20.webp)
- Trong thư mục `assets` này, tạo một tệp tên là `.gitkeep`:
![hội nghị](assets/21.webp)
- Nhấp vào nút `Commit changes...`:
![hội nghị](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấp vào `Commit changes`:
![hội nghị](assets/23.webp)
- Quay lại thư mục `assets`:
![hội nghị](assets/24.webp)
- Nhấp vào nút `Add file`, sau đó vào `Upload files`:
![hội nghị](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo và thả một hình ảnh đại diện cho hội nghị của bạn và sẽ được hiển thị trên trang web của PlanB Network: ![hội nghị](assets/26.webp)
- Đó có thể là một logo, một hình thu nhỏ, hoặc thậm chí một poster:
![hội nghị](assets/27.webp)
- Một khi hình ảnh được tải lên, kiểm tra rằng ô `Commit directly to the patch-1 branch` được chọn, sau đó nhấp vào `Commit changes`:
![hội nghị](assets/28.webp)
- Hãy cẩn thận, hình ảnh của bạn phải được đặt tên là `thumbnail` và phải ở định dạng `.webp`. Tên tệp đầy đủ nên là: `thumbnail.webp`:
![hội nghị](assets/29.webp)
- Quay lại thư mục `assets` của bạn và nhấp vào tệp trung gian `.gitkeep`:
![hội nghị](assets/30.webp)
- Một khi đang ở trên tệp, nhấp vào 3 chấm nhỏ ở góc trên bên phải sau đó vào `Delete file`:
![hội nghị](assets/31.webp)
- Xác nhận rằng bạn vẫn đang ở trên cùng một nhánh làm việc, sau đó nhấp vào nút `Commit changes`:
![hội nghị](assets/32.webp)
- Thêm một tiêu đề và mô tả cho commit của bạn, sau đó nhấp vào `Commit changes`:
![hội nghị](assets/33.webp)
- Quay lại thư mục hội nghị của bạn: ![conference](assets/34.webp)
- Nhấn vào nút `Thêm file`, sau đó chọn `Tạo file mới`: ![conference](assets/35.webp)
- Tạo một file markdown (.md) mới bằng cách đặt tên cho nó với chỉ số ngôn ngữ mẹ đẻ của bạn. File này sẽ được sử dụng cho các bản ghi lại hội nghị của bạn. Ví dụ, nếu tôi muốn viết mô tả cho các hội nghị bằng tiếng Anh, tôi sẽ đặt tên file này là en.md: ![conference](assets/36.webp)
- Điền vào file markdown này sử dụng mẫu sau đây mà bạn có thể điều chỉnh cho phù hợp với cấu hình của hội nghị của bạn:

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

## Tương Lai của Việc Đào Bitcoin: Thách Thức và Đổi Mới

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto

## Liệu Sự Riêng Tư Còn Có Thể Tồn Tại Trên Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto

## Bitcoin Core: Sâu Lắng vào Cơ Sở Mã

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Xây Dựng và Bảo Mật Ví Bitcoin Với Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Diễn giả: Satoshi Nakamoto
```

![conference](assets/37.webp)
- Ở đầu tài liệu của bạn, trong phần "front matter," điền vào trường `name:` với tên hội nghị của bạn và năm của các bản ghi lại. Trong trường `description:`, viết một mô tả ngắn gọn về sự kiện của bạn bằng ngôn ngữ của file. Ví dụ, cho một file tên là `en.md`, mô tả nên được viết bằng tiếng Anh. Đội ngũ PlanB Network sẽ chăm sóc việc dịch mô tả của bạn sử dụng mô hình của họ.
- Các tiêu đề cấp độ một, được đánh dấu bằng `#`, được sử dụng để tổ chức hội nghị theo các cảnh. Ví dụ, `# Sân Khấu Chính` cho sân khấu chính và `# Phòng Workshop` cho một sân khấu dành riêng cho các workshop.

- Các tiêu đề cấp độ hai, được đánh dấu bằng `##`, được sử dụng để phân chia các video ghi lại khác nhau. Nếu các hội nghị được quay liên tục qua nửa ngày, hãy chỉ định, ví dụ, `## Sáng Thứ Sáu`. Nếu các hội nghị được quay và phát sóng riêng lẻ, đặt tên cho hội nghị trực tiếp với một tiêu đề cấp độ hai.

- Dưới mỗi tiêu đề cấp độ hai, chèn một liên kết đến video ghi lại tương ứng. Cú pháp nên là: `![video](https://youtu.be/XXXXXXXXXXXX)`, thay thế `XXXXXXXXXXXX` bằng liên kết video thực tế.

- Nếu định dạng cho phép (các hội nghị riêng lẻ), bạn có thể thêm tên của các diễn giả. Để làm điều này, thêm trường `Diễn giả:` theo sau là tên hoặc bí danh của diễn giả dưới liên kết video. Trong trường hợp có nhiều diễn giả, tách mỗi tên bằng dấu phẩy, như ví dụ này: `Diễn giả: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Một khi bạn hoàn thành các chỉnh sửa cho file này, lưu chúng bằng cách nhấn vào nút `Commit changes...`: ![conference](assets/38.webp)
- Thêm một tiêu đề cho các chỉnh sửa của bạn, cũng như một mô tả ngắn gọn: ![conference](assets/39.webp)
- Nhấp vào `Commit changes`: ![hội nghị](assets/40.webp)
- Thư mục hội nghị của bạn giờ đây sẽ trông như thế này:
![hội nghị](assets/41.webp)
- Nếu mọi thứ đều khiến bạn hài lòng, quay trở lại gốc của fork của bạn:
![hội nghị](assets/42.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của bạn đã trải qua các thay đổi. Nhấp vào nút `Compare & pull request`:
![hội nghị](assets/43.webp)
- Thêm một tiêu đề và mô tả rõ ràng cho PR của bạn:
![hội nghị](assets/44.webp)
- Nhấp vào nút `Create pull request`:
![hội nghị](assets/45.webp)
Xin chúc mừng! PR của bạn đã được tạo thành công. Một quản trị viên giờ đây sẽ xem xét nó và, nếu mọi thứ đều ổn, sẽ hợp nhất nó vào kho lưu trữ chính của Mạng lưới PlanB. Bạn sẽ thấy các bản ghi lại của hội nghị xuất hiện trên trang web vài ngày sau.

Hãy chắc chắn theo dõi tiến trình của PR của bạn. Có thể một quản trị viên sẽ để lại bình luận yêu cầu thông tin bổ sung. Miễn là PR của bạn chưa được xác nhận, bạn có thể xem nó dưới tab `Pull requests` trên kho lưu trữ GitHub của Mạng lưới PlanB:
![hội nghị](assets/46.webp)

Cảm ơn bạn rất nhiều vì đã đóng góp giá trị của mình! :)
