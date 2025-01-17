---
name: Thêm Công Cụ Giáo Dục
description: Làm thế nào để thêm tài liệu giáo dục mới trên Mạng PlanB?
---
![event](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, điều này cho phép bất kỳ ai cũng có thể tham gia vào việc làm phong phú nền tảng.

Ngoài các hướng dẫn và đào tạo, Mạng PlanB cũng cung cấp một thư viện đa dạng về nội dung giáo dục liên quan đến Bitcoin, mở cửa cho mọi người, [trong phần "BET" (_Bộ Công Cụ Giáo Dục Bitcoin_) ](https://planb.network/resources/bet). Cơ sở dữ liệu này bao gồm các poster giáo dục, meme, poster tuyên truyền hài hước, sơ đồ kỹ thuật, logo và các công cụ khác cho người dùng. Mục tiêu của sáng kiến này là hỗ trợ cá nhân và cộng đồng dạy về Bitcoin trên toàn thế giới bằng cách cung cấp cho họ các nguồn tài nguyên hình ảnh cần thiết.

Bạn muốn tham gia làm phong phú cơ sở dữ liệu này, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

*Điều quan trọng là tất cả nội dung được tích hợp vào trang web phải miễn phí quyền sử dụng hoặc tuân thủ giấy phép của tệp nguồn. Ngoài ra, tất cả hình ảnh được công bố trên Mạng PlanB đều được cung cấp dưới giấy phép [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Đầu tiên, bạn cần có một tài khoản trên GitHub. Nếu bạn không biết cách tạo tài khoản, chúng tôi đã tạo một hướng dẫn chi tiết để hướng dẫn bạn.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Truy cập [kho lưu trữ GitHub của PlanB dành riêng cho dữ liệu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) trong phần `resources/bet/`:
![event](assets/02.webp)
- Nhấp vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![event](assets/03.webp)
- Nếu bạn chưa bao giờ đóng góp vào nội dung của Mạng PlanB trước đây, bạn sẽ cần tạo một bản sao (fork) của kho lưu trữ gốc. Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của bạn, điều này cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Nhấp vào nút `Fork this repository`:
![event](assets/04.webp)
- Bạn sẽ được chuyển đến trang chỉnh sửa GitHub:
![event](assets/05.webp)
- Tạo một thư mục cho nội dung của bạn. Để làm điều này, trong ô `Name your file...`, viết tên nội dung của bạn bằng chữ thường và dùng dấu gạch ngang thay cho khoảng trắng. Trong ví dụ của tôi, giả sử tôi muốn thêm một hình ảnh PDF của danh sách từ BIP39 dài 2048 từ. Vậy, tôi sẽ đặt tên thư mục của mình là `bip39-wordlist`: ![event](assets/06.webp)
- Để xác nhận việc tạo thư mục, chỉ cần thêm một dấu gạch chéo sau tên trong cùng một ô, ví dụ: `bip39-wordlist/`. Thêm một dấu gạch chéo tự động tạo ra một thư mục thay vì một tệp:
![event](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một tệp YAML đầu tiên có tên `bet.yml`:
![event](assets/08.webp)
- Điền thông tin liên quan đến nội dung của bạn vào tệp này bằng cách sử dụng mẫu sau:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`builder`**: Chỉ định mã nhận dạng của tổ chức bạn trên Mạng lưới PlanB. Nếu bạn chưa có mã nhận dạng "builder" cho công ty của mình, bạn có thể tạo một mã bằng cách làm theo hướng dẫn này.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Nếu bạn chưa có, bạn có thể sử dụng tên của mình, bí danh, hoặc tên công ty mà không cần tạo hồ sơ builder.
- **`type`**: Chọn bản chất của nội dung bạn muốn đăng tải từ hai lựa chọn sau:
	- `Educational Content` cho nội dung giáo dục.
	- `Visual Content` cho các loại nội dung đa dạng khác.

- **`links`**: Cung cấp liên kết đến nội dung của bạn. Bạn có hai lựa chọn:
	- Nếu bạn chọn lưu trữ nội dung trực tiếp trên GitHub của PlanB, bạn sẽ cần thêm các liên kết vào tệp này trong các bước tiếp theo.
	- Nếu nội dung của bạn được lưu trữ ở nơi khác, như trên trang web cá nhân của bạn, hãy chỉ ra các liên kết tương ứng tại đây:
	    - `download`: Một liên kết để tải xuống nội dung của bạn.
	    - `view`: Một liên kết để xem nội dung của bạn (có thể giống như liên kết tải xuống). Nếu nội dung của bạn có sẵn bằng nhiều ngôn ngữ, hãy thêm một liên kết cho mỗi ngôn ngữ.

- **`tags`**: Thêm hai thẻ liên quan đến nội dung của bạn. Ví dụ:
	- bitcoin
	- technology
	- economy
	- education
	- meme...

- **`contributors`**: Nêu mã nhận dạng của người đóng góp nếu bạn có.

Ví dụ, tệp YAML của bạn có thể trông như thế này:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- Trong ví dụ của tôi, tôi sẽ để trống các liên kết cho đến nay, vì tôi sẽ thêm PDF của mình trực tiếp trên GitHub:
![event](assets/09.webp)
- Sau khi hoàn thành các thay đổi vào tệp này, lưu chúng bằng cách nhấp vào nút `Commit changes...`:
![event](assets/10.webp)
- Thêm một tiêu đề cho các thay đổi của bạn, cũng như một mô tả ngắn gọn:
![event](assets/11.webp)
- Nhấp vào nút màu xanh `Propose changes`:
![event](assets/12.webp)
- Bạn sẽ đến trang tóm tắt tất cả các thay đổi của bạn:
![event](assets/13.webp)
- Nhấp vào ảnh đại diện GitHub của bạn ở góc trên bên phải, sau đó vào `Your Repositories`:
![event](assets/14.webp)
- Chọn fork của bạn của kho lưu trữ Mạng lưới PlanB:
![event](assets/15.webp)
- Bạn sẽ thấy một thông báo ở đầu cửa sổ với nhánh mới của bạn. Có thể nó được gọi là `patch-1`. Nhấp vào nó:
![event](assets/16.webp)
- Bây giờ bạn đang ở trên nhánh làm việc của mình (**hãy chắc chắn bạn đang ở trên cùng một nhánh với các thay đổi trước đó của bạn, điều này rất quan trọng!**):
![event](assets/17.webp)
- Quay lại thư mục `resources/bet/` và chọn thư mục nội dung mà bạn vừa tạo trong commit trước:
![event](assets/18.webp)
- Trong thư mục nội dung của bạn, nhấp vào nút `Add file`, sau đó vào `Create new file`:
![event](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và xác nhận việc tạo nó bằng cách đặt một dấu gạch chéo `/` ở cuối:
![event](assets/20.webp)
- Trong thư mục `assets` này, tạo một tệp có tên `.gitkeep`: ![event](assets/21.webp)
- Nhấp vào nút `Commit changes...`: ![sự kiện](assets/22.webp)- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấp vào `Commit changes`: ![sự kiện](assets/23.webp)
- Quay lại thư mục `assets`: ![sự kiện](assets/24.webp)
- Nhấp vào nút `Add file`, sau đó chọn `Upload files`: ![sự kiện](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo và thả hình thu nhỏ đại diện cho nội dung của bạn vào khu vực này. Hình ảnh này sẽ được hiển thị trên trang web của PlanB Network: ![sự kiện](assets/26.webp)
- Đó có thể là một bản xem trước, logo, hoặc biểu tượng: ![sự kiện](assets/27.webp)
- Một khi hình ảnh đã được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấp vào `Commit changes`: ![sự kiện](assets/28.webp)
- Hãy cẩn thận, hình ảnh của bạn phải được đặt tên là `logo` và phải ở định dạng `.webp`. Tên file đầy đủ do đó phải là: `logo.webp`: ![sự kiện](assets/29.webp)
- Quay lại thư mục `assets` của bạn và nhấp vào file trung gian `.gitkeep`: ![sự kiện](assets/30.webp)
- Một khi đã ở trên file, nhấp vào ba chấm nhỏ ở góc phải trên sau đó chọn `Delete file`: ![sự kiện](assets/31.webp)
- Đảm bảo bạn vẫn đang ở trên cùng một nhánh làm việc, sau đó nhấp vào nút `Commit changes`: ![sự kiện](assets/32.webp)
- Thêm một tiêu đề và mô tả cho commit của bạn, sau đó nhấp vào `Commit changes`: ![sự kiện](assets/33.webp)
- Quay lại thư mục nội dung của bạn: ![sự kiện](assets/34.webp)
- Nhấp vào nút `Add file`, sau đó chọn `Create new file`: ![sự kiện](assets/35.webp)
- Tạo một file YAML mới bằng cách đặt tên cho nó với chỉ số của ngôn ngữ mẹ đẻ của bạn. File này sẽ được sử dụng để mô tả nội dung. Ví dụ, nếu tôi muốn viết mô tả của mình bằng tiếng Anh, tôi sẽ đặt tên file này là `en.yml`: ![sự kiện](assets/36.webp)
- Điền vào file YAML này sử dụng mẫu sau:

```yaml
name: 
description: |
  
```

- Đối với khóa `name`, bạn có thể thêm tên của nội dung của mình;
- Đối với khóa `description`, bạn chỉ cần thêm một đoạn văn ngắn mô tả nội dung của bạn. Mô tả phải ở cùng ngôn ngữ với tên file. Bạn không cần phải dịch mô tả này sang tất cả các ngôn ngữ được hỗ trợ trên trang web, vì các đội ngũ của PlanB sẽ làm điều đó với mô hình của họ.
Ví dụ, đây là cách file của bạn có thể trông như thế nào:

```yaml
name: BIP39 WORDLIST
description: |
  Danh sách đầy đủ và được đánh số của 2048 từ tiếng Anh từ từ điển BIP39 được sử dụng để mã hóa các cụm từ ghi nhớ. Tài liệu có thể được in trên một trang duy nhất.
```

![sự kiện](assets/37.webp)
- Nhấp vào nút `Commit changes...`:
![sự kiện](assets/38.webp)
- Đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, thêm một tiêu đề, sau đó nhấp vào `Commit changes`:
![sự kiện](assets/39.webp)
- Thư mục nội dung của bạn giờ đây nên trông như thế này:
![sự kiện](assets/40.webp)
*Nếu bạn không muốn thêm nội dung vào GitHub và bạn đã ghi chú các liên kết trong tệp `bet.yml` trong các bước trước, bạn có thể bỏ qua phần này và trực tiếp đến phần tạo Pull Request.*
- Quay lại thư mục `/assets`:
![sự kiện](assets/41.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![sự kiện](assets/42.webp)
- Một trang mới sẽ mở ra. Kéo và thả nội dung bạn muốn chia sẻ vào khu vực đó:
![sự kiện](assets/43.webp)
- Ví dụ, tôi đã thêm tệp PDF của danh sách BIP39:
![sự kiện](assets/44.webp)
- Một khi nội dung đã được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được kiểm tra, sau đó nhấn vào `Commit changes`:
![sự kiện](assets/45.webp)
- Quay lại thư mục `/assets` của bạn và nhấn vào tệp bạn vừa tải lên:
![sự kiện](assets/46.webp)
- Lấy URL trung gian của tệp của bạn. Ví dụ, trong trường hợp của tôi, URL là:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Chỉ giữ lại phần cuối của URL từ `/resources` trở đi:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Thêm vào cơ sở của URL thông tin sau để có liên kết chính xác:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Những gì chúng ta đang làm ở đây là dự đoán liên kết tương lai đến tệp của bạn, một khi đề xuất của bạn đã được hợp nhất vào kho lưu trữ nguồn của Mạng PlanB.
- Quay lại tệp `bet.yml` của bạn và nhấn vào biểu tượng bút chì: ![sự kiện](assets/47.webp)
- Thêm liên kết của bạn vào đó:
![sự kiện](assets/48.webp)
- Một khi thay đổi của bạn hoàn tất, nhấn vào nút `Commit changes...`:
![sự kiện](assets/49.webp)
- Thêm tiêu đề cho thay đổi của bạn, cũng như một mô tả ngắn gọn:
![sự kiện](assets/50.webp)
- Nhấn vào nút màu xanh `Commit changes`:
![sự kiện](assets/51.webp)

---

- Nếu mọi thứ đều ổn với bạn, quay lại gốc của fork của bạn:
![sự kiện](assets/52.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của bạn đã được chỉnh sửa. Nhấn vào nút `Compare & pull request`:
![sự kiện](assets/53.webp)
- Thêm một tiêu đề rõ ràng và mô tả cho PR của bạn:
![sự kiện](assets/54.webp)
- Nhấn vào nút `Create pull request`:
![sự kiện](assets/55.webp)
Xin chúc mừng! PR của bạn đã được tạo thành công. Một quản trị viên sẽ xem xét nó và, nếu mọi thứ đều ổn, hợp nhất nó vào kho lưu trữ chính của Mạng PlanB. Bạn sẽ thấy BET của mình xuất hiện trên trang web vài ngày sau.

Hãy chắc chắn theo dõi tiến trình của PR của bạn. Một quản trị viên có thể để lại bình luận yêu cầu thông tin bổ sung. Miễn là PR của bạn chưa được xác nhận, bạn có thể xem nó trong tab Pull requests trên kho GitHub của Mạng PlanB:
![sự kiện](assets/56.webp)
Cảm ơn bạn rất nhiều vì đã đóng góp quý báu của mình! :)
