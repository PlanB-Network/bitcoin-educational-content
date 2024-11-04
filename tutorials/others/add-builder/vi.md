---
name: Thêm một Người Xây Dựng
description: Làm thế nào để đề xuất thêm một người xây dựng mới vào Mạng lưới PlanB?
---
![builder](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, bằng càng nhiều ngôn ngữ càng tốt. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, điều này cho phép bất kỳ ai cũng có thể tham gia vào việc làm phong phú thêm nền tảng.

Bạn muốn thêm một "người xây dựng" Bitcoin mới vào trang web Mạng lưới PlanB và tăng cường tính nhìn thấy cho công ty hoặc phần mềm của bạn, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!
![builder](assets/01.webp)
- Đầu tiên, bạn cần phải có một tài khoản GitHub. Nếu bạn không biết cách tạo tài khoản, chúng tôi đã tạo một hướng dẫn chi tiết để hướng dẫn bạn.

https://planb.network/tutorials/others/create-github-account


- Truy cập vào [kho lưu trữ GitHub của PlanB dành riêng cho dữ liệu](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) trong phần `resources/builder/`:
![builder](assets/02.webp)
- Nhấp vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![builder](assets/03.webp)
- Nếu bạn chưa bao giờ đóng góp vào nội dung của Mạng lưới PlanB trước đây, bạn sẽ cần tạo một bản sao (fork) của kho lưu trữ gốc. Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của bạn, điều này cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Nhấp vào nút `Fork this repository`:
![builder](assets/04.webp)
- Bạn sẽ sau đó đến trang chỉnh sửa của GitHub:
![builder](assets/05.webp)
- Tạo một thư mục cho công ty của bạn. Để làm điều này, trong ô `Name your file...`, viết tên công ty của bạn bằng chữ thường với dấu gạch nối thay cho khoảng trắng. Ví dụ, nếu công ty của bạn có tên là "Bitcoin Baguette", bạn nên viết `bitcoin-baguette`:
![builder](assets/06.webp)
- Để xác nhận việc tạo thư mục, chỉ cần thêm một dấu gạch chéo sau tên của bạn trong cùng một ô, ví dụ: `bitcoin-baguette/`. Thêm một dấu gạch chéo tự động tạo ra một thư mục thay vì một tệp:
![builder](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một tệp YAML đầu tiên có tên `builder.yml`:
![builder](assets/08.webp)
- Điền thông tin về công ty của bạn vào tệp này bằng cách sử dụng mẫu sau:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Dưới đây là cách điền cho mỗi khóa:
- `name`: Tên của công ty bạn (bắt buộc);
- `address` : Địa chỉ của doanh nghiệp bạn (tùy chọn);
- `language` : Các quốc gia mà doanh nghiệp của bạn hoạt động hoặc các ngôn ngữ được hỗ trợ (tùy chọn);
- `links` : Các liên kết chính thức khác nhau của doanh nghiệp bạn (tùy chọn);
- `tags` : 2 thuật ngữ mô tả doanh nghiệp của bạn (bắt buộc);
- `category` : Danh mục mô tả tốt nhất lĩnh vực hoạt động của doanh nghiệp bạn trong số các lựa chọn sau:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
Ví dụ, tệp YAML của bạn có thể trông như thế này:
```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - education

category: education
```

![builder](assets/09.webp)
- Sau khi bạn hoàn thành việc thay đổi tệp này, hãy lưu lại bằng cách nhấp vào nút `Commit changes...`:
![builder](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, cùng với một mô tả ngắn gọn:
![builder](assets/11.webp)
- Nhấp vào nút màu xanh `Propose changes`:
![builder](assets/12.webp)
- Bạn sẽ đến trang tóm tắt tất cả các thay đổi của bạn:
![builder](assets/13.webp)
- Nhấp vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó vào `Your Repositories`:
![builder](assets/14.webp)
- Chọn fork của bạn của kho lưu trữ PlanB Network:
![builder](assets/15.webp)
- Bạn sẽ thấy một thông báo ở đầu cửa sổ với nhánh mới của bạn. Có thể nó được gọi là `patch-1`. Nhấp vào nó:
![builder](assets/16.webp)
- Bây giờ bạn đang ở trên nhánh làm việc của mình (**hãy chắc chắn bạn đang ở trên cùng một nhánh với các sửa đổi trước đó của bạn, điều này rất quan trọng!**):
![builder](assets/17.webp)
- Quay lại thư mục `resources/builders/` và chọn thư mục của doanh nghiệp bạn vừa tạo trong commit trước:
![builder](assets/18.webp)
- Trong thư mục của doanh nghiệp bạn, nhấp vào nút `Add file`, sau đó vào `Create new file`:
![builder](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và xác nhận việc tạo nó bằng cách đặt dấu gạch chéo `/` ở cuối:
![builder](assets/20.webp)
- Trong thư mục `assets` này, tạo một tệp tên là `.gitkeep`:
![builder](assets/21.webp)
- Nhấp vào nút `Commit changes...`:
![builder](assets/22.webp)
- Giữ tiêu đề commit mặc định, và chắc chắn rằng ô `Commit directly to the patch-1 branch` đã được kiểm tra, sau đó nhấp vào `Commit changes`: ![builder](assets/23.webp)
- Quay lại thư mục `assets`:
![builder](assets/24.webp)
- Nhấp vào nút `Add file`, sau đó vào `Upload files`:
![builder](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo và thả một hình ảnh của công ty hoặc phần mềm của bạn vào khu vực đó. Hình ảnh này sẽ được hiển thị trên trang web của PlanB Network:
![builder](assets/26.webp)
- Có thể là logo hoặc một biểu tượng:
![builder](assets/27.webp)
- Một khi hình ảnh được tải lên, xác nhận rằng ô `Commit directly to the patch-1 branch` đã được kiểm tra, sau đó nhấp vào `Commit changes`:
![builder](assets/28.webp)
- Lưu ý, hình ảnh của bạn phải vuông, phải được đặt tên là `logo`, và phải ở định dạng `.webp`. Tên tệp đầy đủ nên là: `logo.webp`:
![builder](assets/29.webp)
- Quay lại thư mục `assets` của bạn và nhấp vào tệp trung gian `.gitkeep`:
![builder](assets/30.webp)- Một khi đã mở tệp, nhấp vào ba chấm nhỏ ở góc trên bên phải sau đó chọn `Delete file`:
![builder](assets/31.webp)
- Kiểm tra xem bạn vẫn đang ở nhánh làm việc hiện tại, sau đó nhấp vào nút `Commit changes`:
![builder](assets/32.webp)
- Thêm một tiêu đề và mô tả cho lần commit của bạn, sau đó nhấp vào `Commit changes`:
![builder](assets/33.webp)
- Quay lại thư mục của công ty bạn:
![builder](assets/34.webp)
- Nhấp vào nút `Add file`, sau đó chọn `Create new file`:
![builder](assets/35.webp)
- Tạo một tệp YAML mới bằng cách đặt tên cho nó với chỉ số của ngôn ngữ mẹ đẻ của bạn. Tệp này sẽ được sử dụng để mô tả về builder. Ví dụ, nếu tôi muốn viết mô tả của mình bằng tiếng Anh, tôi sẽ đặt tên tệp này là `en.yml`:
![builder](assets/36.webp)
- Điền vào tệp YAML này sử dụng mẫu sau:
```yaml
description: |
 
contributors:
 - 
```

- Đối với khóa `contributors`, bạn có thể thêm mã định danh của người đóng góp cho Mạng PlanB nếu bạn có. Nếu không, để trống trường này.
- Đối với khóa `description`, bạn chỉ cần thêm một đoạn văn ngắn mô tả về công ty hoặc phần mềm của bạn. Mô tả phải bằng ngôn ngữ giống như tên tệp. Bạn không cần phải dịch mô tả này sang tất cả các ngôn ngữ được hỗ trợ trên trang web, vì đội ngũ PlanB sẽ thực hiện việc này bằng mô hình của họ. Ví dụ, đây là cách tệp của bạn có thể trông như thế nào:
```yaml
description: |
Năm 2017, Bitcoin Baguette được thành lập, là một hiệp hội có trụ sở tại Paris chuyên tổ chức các cuộc gặp gỡ và hội thảo kỹ thuật về Bitcoin. Chúng tôi kết nối những người đam mê, chuyên gia và những tâm hồn tò mò để khám phá và thảo luận về những phức tạp của công nghệ Bitcoin. Các sự kiện của chúng tôi cung cấp một nền tảng cho việc chia sẻ kiến thức, kết nối mạng và nuôi dưỡng sự hiểu biết sâu sắc hơn về cơ chế hoạt động bên trong của Bitcoin. Tham gia cùng chúng tôi tại Bitcoin Baguette để trở thành một phần của cộng đồng Bitcoin tại Paris và cập nhật những tiến bộ mới nhất trong lĩnh vực này.

contributors:
- 
```
![builder](assets/37.webp)
- Nhấp vào nút `Commit changes`:
![builder](assets/38.webp)
- Đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, thêm một tiêu đề, sau đó nhấp vào `Commit changes`:
![builder](assets/39.webp)
- Thư mục của công ty bạn giờ đây sẽ trông như thế này:
![builder](assets/40.webp)
- Nếu mọi thứ đều đáp ứng sự hài lòng của bạn, quay lại gốc của fork của bạn:
![builder](assets/41.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của bạn đã trải qua những thay đổi. Nhấp vào nút `Compare & pull request`:
![builder](assets/42.webp)
- Thêm một tiêu đề và mô tả rõ ràng cho PR của bạn:
![builder](assets/43.webp)
- Nhấp vào nút `Create pull request`:
![builder](assets/44.webp)
Xin chúc mừng! PR của bạn đã được tạo thành công. Một quản trị viên giờ đây sẽ xem xét nó và, nếu mọi thứ đều ổn, sẽ tích hợp nó vào kho lưu trữ chính của Mạng PlanB. Bạn sẽ thấy hồ sơ builder của mình xuất hiện trên trang web vài ngày sau.

Hãy chắc chắn theo dõi tiến trình của PR của bạn. Một quản trị viên có thể để lại bình luận yêu cầu thông tin bổ sung. Miễn là PR của bạn chưa được xác nhận, bạn có thể xem nó trong tab `Pull requests` trên kho lưu trữ GitHub của Mạng PlanB:
![builder](assets/45.webp)
Cảm ơn bạn rất nhiều vì đã đóng góp giá trị của mình! :)
