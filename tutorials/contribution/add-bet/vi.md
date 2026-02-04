---
name: Đóng góp các công cụ giáo dục
description: Làm thế nào để thêm nguồn học liệu mới lên Plan ₿ Academy?
---
![event](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

Không chỉ dừng lại ở các bài hướng dẫn và khóa đào tạo, Plan ₿ Academy còn sở hữu một thư viện nội dung giáo dục về Bitcoin vô cùng phong phú và đa dạng, nơi mọi người đều có thể dễ dàng tiếp cận [tại mục "BET" (_Bitcoin Educational Toolkit_)](https://planb.academy/resources/bet). Cơ sở dữ liệu này bao gồm từ các poster giáo dục, meme, tranh cổ động hài hước cho đến các sơ đồ kỹ thuật, logo và nhiều công cụ hữu ích khác. Mục tiêu của sáng kiến này là hỗ trợ các cá nhân và cộng đồng đang giảng dạy về Bitcoin trên toàn thế giới bằng cách cung cấp cho họ những nguồn học liệu trực quan cần thiết.

Bạn muốn cùng chung tay làm phong phú thêm kho dữ liệu này nhưng chưa biết bắt đầu từ đâu? Bài hướng dẫn này chính là dành cho bạn!

*Một lưu ý quan trọng là tất cả nội dung được tích hợp vào trang web phải không vi phạm bản quyền hoặc phải tuân thủ đúng giấy phép của file nguồn. Ngoài ra, mọi ấn phẩm hình ảnh được đăng tải trên Plan ₿ Academy đều phải tuân theo giấy phép [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- Truy cập [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) trong phần `resources/bet/`:
![event](assets/02.webp)
- Nhấn vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![event](assets/03.webp)
- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:
![event](assets/04.webp)
- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:
![event](assets/05.webp)
- Tạo một thư mục cho nội dung của bạn. Tại ô `Name your file...`, bạn nhập tên nội dung bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, tôi muốn thêm một tài liệu PDF minh họa cho danh sách từ vựng BIP39 (BIP39 wordlist) gồm 2048 từ, tôi sẽ đặt tên thư mục là `bip39-wordlist`: ![event](assets/06.webp)
- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `bip39-wordlist/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:
![event](assets/07.webp)
- Trong thư mục vừa tạo, bạn sẽ tạo một file YAML đầu tiên có tên `bet.yml`:
![event](assets/08.webp)
- Điền thông tin về nội dung của bạn vào file này theo mẫu sau:

```yaml
project: 
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

Dưới đây là thông tin chi tiết cho từng trường:

- **`project`**: Mã định danh (identifier) cho tổ chức của bạn trên Plan ₿ Academy. Nếu công ty của bạn chưa có mã định danh "project", bạn có thể khởi tạo bằng cách làm theo hướng dẫn này.

https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Trong trường hợp chưa có, bạn chỉ cần điền tên của mình, biệt danh hoặc tên công ty mà không cần phải tạo hồ sơ "project".
- **`type`**: Lựa chọn bản chất nội dung của bạn với hai tùy chọn sau:
	- `Educational Content` cho nội dung giáo dục.
	- `Visual Content` cho các loại nội dung trực quan khác.

- **`links`**: Cung cấp liên kết đến nội dung của bạn. Bạn có hai lựa chọn:
	- Nếu bạn chọn lưu trữ nội dung trực tiếp trên GitHub của PlanB, bạn sẽ cần thêm các liên kết vào file này trong các bước tiếp theo.
	- Nếu nội dung của bạn được lưu trữ ở nơi khác, như trên trang web cá nhân của bạn, hãy thêm các liên kết tương ứng tại đây:
	    - `download`: Liên kết để tải xuống nội dung của bạn.
	    - `view`: Liên kết để xem nội dung của bạn (có thể trùng với liên kết tải xuống). Nếu nội dung có nhiều ngôn ngữ, hãy thêm một liên kết cho mỗi ngôn ngữ.

- **`tags`**: Thêm hai thẻ (tag) liên quan đến nội dung của bạn. Ví dụ:
	- bitcoin
	- technology
	- economy
	- education
	- meme...

- **`contributors`**: Thêm ID người đóng góp (contributor) của bạn nếu có.

Ví dụ, file YAML của bạn có thể trông như thế này:

```yaml
project: Plan ₿ Academy
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
```

- Trong ví dụ này, tôi sẽ tạm để trống các đường dẫn (links), vì tôi dự định sẽ tải trực tiếp file PDF lên GitHub:
![event](assets/09.webp)
- Sau khi hoàn tất việc chỉnh sửa file này, hãy lưu lại bằng cách nhấn vào nút `Commit changes...`:
![event](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, kèm theo một mô tả ngắn gọn:
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
- Bây giờ, bạn đang ở trên nhánh làm việc của mình (**hãy đảm bảo bạn đang ở đúng nhánh chứa các thay đổi trước đó, điều này rất quan trọng!**):
![event](assets/17.webp)
- Quay lại thư mục `resources/bet/` và chọn thư mục nội dung mà bạn vừa tạo trong commit trước:
![event](assets/18.webp)
- Trong thư mục nội dung đó, nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![event](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:
![event](assets/20.webp)
- Trong thư mục `assets` này, tạo một file có tên `.gitkeep`:
![event](assets/21.webp)
- Nhấn vào nút `Commit changes...`:
![event](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấn `Commit changes`:
![event](assets/23.webp)
- Quay lại thư mục `assets`:
![event](assets/24.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![event](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo thả ảnh thu nhỏ (thumbnail) đại diện cho nội dung của bạn vào khu vực tải lên. Ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:
![event](assets/26.webp)
- Đó có thể là một bản xem trước, logo, hoặc biểu tượng:
![event](assets/27.webp)
- Sau khi hình ảnh đã được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấn `Commit changes`:
![event](assets/28.webp)
- Lưu ý, hình ảnh của bạn phải được đặt tên là `logo` và phải ở định dạng `.webp`. Tên file tin đầy đủ phải là: `logo.webp`:
![event](assets/29.webp)
- Quay lại thư mục `assets` và nhấp vào file `.gitkeep`:
![event](assets/30.webp)
- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn `Delete file`:
![event](assets/31.webp)
- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes`:
![event](assets/32.webp)
- Thêm một tiêu đề và mô tả cho commit này, sau đó nhấn vào nút `Commit changes`:
![event](assets/33.webp)
- Quay lại thư mục nội dung của bạn:
![event](assets/34.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Create new file`:
![event](assets/35.webp)
- Tạo một file YAML mới và đặt tên theo mã ngôn ngữ bản địa của bạn. file này sẽ dùng để mô tả nội dung. Ví dụ, nếu tôi muốn viết mô tả của mình bằng tiếng Anh, tôi sẽ đặt tên file này là `en.yml` (hoặc `vi.yml` nếu viết bằng tiếng Việt):
![event](assets/36.webp)
- Điền vào file YAML này theo mẫu sau:

```yaml
name: 
description: |
  
```

- Đối với khóa `name`, bạn nhập tên cho nội dung của mình;
- Đối với khóa `description`, bạn chỉ cần thêm một đoạn văn ngắn mô tả về nội dung đó. Lưu ý rằng ngôn ngữ của phần mô tả phải đồng nhất với tên file (ví dụ: file `vi.yml` thì mô tả bằng tiếng Việt). Bạn không cần phải tự mình dịch phần mô tả này sang tất cả các ngôn ngữ khác trên trang web, vì đội ngũ PlanB sẽ thực hiện việc đó thông qua mô hình ngôn ngữ của họ.
Dưới đây là ví dụ minh họa cho file của bạn:

```yaml
name: DANH SÁCH TỪ VỰNG BIP39
description: |
  Danh sách hoàn chỉnh có đánh số thứ tự của 2048 từ tiếng Anh từ bộ từ điển BIP39 được sử dụng để thiết lập cụm ghi nhớ (mnemonic phrases). Tài liệu này có thể in trên một trang duy nhất.
```

![event](assets/37.webp)
- Nhấn vào nút `Commit changes...`:
![event](assets/38.webp)
- Đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, thêm tiêu đề, sau đó nhấn `Commit changes`:
![event](assets/39.webp)
- Thư mục nội dung của bạn lúc này sẽ trông như thế này:
![event](assets/40.webp)

---

*Nếu bạn không muốn thêm nội dung trực tiếp trên GitHub và bạn đã điền sẵn các liên kết trong file `bet.yml` ở các bước trước, bạn có thể bỏ qua phần này và chuyển thẳng đến bước tạo Pull Request.*
- Quay lại thư mục `/assets`:
![event](assets/41.webp)
- Nhấn vào nút `Add file`, sau đó chọn `Upload files`:
![event](assets/42.webp)
- Một trang mới sẽ mở ra. Kéo thả nội dung bạn muốn chia sẻ vào vùng này:
![event](assets/43.webp)
- Ví dụ, tôi đã thêm file PDF về danh sách BIP39:
![event](assets/44.webp)
- Sau khi nội dung đã được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được kiểm tra, rồi nhấn `Commit changes`:
![event](assets/45.webp)
- Quay lại thư mục `/assets` và nhấn vào file bạn vừa tải lên:
![event](assets/46.webp)
- Sao chép đường dẫn (URL) trung gian của file. Ví dụ, trong trường hợp của tôi, URL là:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Chỉ giữ lại phần cuối của URL, tính từ `/resources` trở đi:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Thêm phần tiền tố (base URL) sau đây vào trước đoạn mã trên để có được đường dẫn chính xác:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev
```

- Đường dẫn cuối cùng của bạn sẽ trông như thế này:
```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```
Thao tác này giúp chúng ta xác định trước đường dẫn cố định cho file tin của bạn, một khi đề xuất đóng góp được chấp nhận và gộp (merge) vào repository gốc của Plan ₿ Academy.
- Quay lại file `bet.yml` của bạn và nhấn vào biểu tượng bút chì: ![event](assets/47.webp)
- Thêm liên kết của bạn vào đó:
![event](assets/48.webp)
- Sau khi hoàn tất các thay đổi, nhấn vào nút `Commit changes...`:
![event](assets/49.webp)
- Thêm tiêu đề cho các thay đổi, kèm theo một mô tả ngắn gọn:
![event](assets/50.webp)
- Nhấn vào nút `Commit changes`:
![event](assets/51.webp)

---

- Nếu mọi thứ đã ổn, hãy quay trở lại thư mục gốc của bản fork:
![event](assets/52.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút `Compare & pull request`:
![event](assets/53.webp)
- Thêm một tiêu đề rõ ràng và phần mô tả chi tiết cho bản PR (Pull Request) của bạn:
![event](assets/54.webp)
- Nhấn vào nút `Create pull request`:
![event](assets/55.webp)

Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy bộ công cụ giáo dục (BET) của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:

![event](assets/56.webp)

Chân thành cảm ơn sự đóng góp quý giá của bạn! :)

