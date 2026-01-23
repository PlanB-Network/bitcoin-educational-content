---
name: Thêm một "Project"
description: Làm thế nào để đề xuất thêm một "project" lên trên Plan ₿ Academy?
---
![project](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này.

Bạn muốn thêm một "project" Bitcoin mới vào Plan ₿ Academy và tăng độ nhận diện cho công ty hoặc phần mềm của bạn, nhưng không biết làm thế nào? Hướng dẫn này dành cho bạn!

![project](assets/01.webp)

- Trước tiên, bạn cần có một tài khoản GitHub. Nếu bạn chưa biết cách tạo tài khoản, chúng tôi đã chuẩn bị một hướng dẫn chi tiết để giúp bạn:

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Truy cập vào [repository của Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects) trong phần `resources/project/`:
![project](assets/02.webp)
- Nhấp vào nút `Add file` ở góc trên bên phải, sau đó chọn `Create new file`:
![project](assets/03.webp)
- Nếu đây là lần đầu bạn đóng góp cho Plan ₿ Academy, bạn sẽ cần tạo một bản sao (fork) của repository gốc. "Fork" nghĩa là tạo một bản sao của repository đó trên tài khoản GitHub của bạn, cho phép bạn làm việc mà không ảnh hưởng đến repository gốc. Nhấn vào nút `Fork this repository`:
![project](assets/04.webp)
- Ngay sau đó, giao diện chỉnh sửa của GitHub sẽ hiện ra:
![project](assets/05.webp)
- Tạo một thư mục cho công ty của bạn. Tại ô `Name your file...`, nhập công ty của bạn bằng chữ thường và dùng dấu gạch ngang `-` thay cho khoảng trắng. Ví dụ, nếu công ty của bạn có tên là "Bitcoin Baguette", bạn nên ghi là `bitcoin-baguette`:
![project](assets/06.webp)
- Để đảm bảo rằng bạn đang tạo thư mục thay vì tạo file tin, chỉ cần thêm một dấu gạch chéo ngay sau tên vừa nhập, ví dụ: `bitcoin-baguette/`. Thao tác thêm dấu `/` này sẽ giúp GitHub tự động nhận diện đây là một thư mục:
![project](assets/07.webp)
- Trong thư mục này, bạn sẽ tạo một file YAML đầu tiên có tên `project.yml`:
![project](assets/08.webp)
- Điền thông tin về công ty của bạn vào file `project.yml` theo mẫu sau:

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

Dưới đây là thông tin cần điền cho mỗi khóa:
- `name`: Tên của công ty (bắt buộc);
- `address` : Địa chỉ của công ty (tùy chọn);
- `language` : Các quốc gia mà công ty của bạn đang hoạt động hoặc các ngôn ngữ được hỗ trợ (tùy chọn);
- `links` : Các liên kết chính thức khác nhau của công ty (tùy chọn);
- `tags` : 2 thẻ phân loại mô tả lĩnh vực hoạt động của dự án/công ty (bắt buộc);
- `category` : Chọn danh mục cho lĩnh vực hoạt động của bạn trong số các lựa chọn dưới đây:
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

Ví dụ, file YAML của bạn có thể trông như thế này:

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

![project](assets/09.webp)
- Sau khi hoàn tất chỉnh sửa file, lưu thay đổi bằng cách nhấn nút `Commit changes...`:
![project](assets/10.webp)
- Thêm tiêu đề cho các thay đổi của bạn, kèm theo một mô tả ngắn:
![project](assets/11.webp)
- Nhấp vào nút `Propose changes`:
![project](assets/12.webp)
- Hệ thống sẽ chuyển bạn đến trang tổng hợp tất cả các thay đổi vừa thực hiện:
![project](assets/13.webp)
- Nhấp vào ảnh hồ sơ GitHub của bạn ở góc trên bên phải, sau đó chọn `Your Repositories`:
![project](assets/14.webp)
- Chọn bản fork của repository Plan ₿ Academy:
![project](assets/15.webp)
- Bạn sẽ thấy thông báo ở đầu cửa sổ về nhánh (branch) mới của bạn (thường tên là `patch-1`). Nhấn vào đó:
![project](assets/16.webp)
- Bây giờ, bạn đang ở trên nhánh làm việc của mình (**hãy đảm bảo bạn đang ở đúng nhánh chứa các thay đổi trước đó, điều này rất quan trọng!**):
![project](assets/17.webp)
- Quay lại thư mục `resources/projects/` và chọn thư mục doanh nghiệp của bạn vừa tạo trong commit trước:
![project](assets/18.webp)
- Trong thư mục, nhấp vào nút `Add file`, sau đó vào `Create new file`:
![project](assets/19.webp)
- Đặt tên thư mục mới này là `assets` và đừng quên thêm một dấu gạch chéo `/` ở cuối:
![project](assets/20.webp)
- Trong thư mục `assets` này, tạo một file tên là `.gitkeep`:
![project](assets/21.webp)
- Nhấp vào nút `Commit changes...`:
![project](assets/22.webp)
- Giữ nguyên tiêu đề commit mặc định, và đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấn `Commit changes`: ![project](assets/23.webp)
- Quay lại thư mục `assets`:
![project](assets/24.webp)
- Nhấp vào nút `Add file`, sau đó chọn `Upload files`:
![project](assets/25.webp)
- Một trang mới sẽ mở ra. Kéo thả một ảnh của công ty hoặc phần mềm của bạn vào khu vực tải lên. Ảnh này sẽ được hiển thị trên trang web của Plan ₿ Academy:
![project](assets/26.webp)
- Đó có thể là logo hoặc một biểu tượng đại diện:
![project](assets/27.webp)
- Sau khi hình ảnh đã được tải lên, đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, sau đó nhấn `Commit changes`:
![project](assets/28.webp)
- Lưu ý, hình ảnh của bạn phải có tỷ lệ khung hình vuông, tên bắt buộc là `logo`, và phải ở định dạng `.webp`. Tên file đầy đủ phải là: `logo.webp`:
![project](assets/29.webp)
- Quay lại thư mục `assets` và nhấp vào file trung gian `.gitkeep`:
![project](assets/30.webp)
- Tại giao diện của file này, nhấn vào dấu ba chấm nhỏ ở góc trên bên phải rồi chọn `Delete file`:
![project](assets/31.webp)
- Đảm bảo rằng bạn vẫn đang ở đúng nhánh làm việc hiện tại, sau đó nhấn vào nút `Commit changes`:
![project](assets/32.webp)
- Thêm một tiêu đề và mô tả cho commit này, sau đó nhấn vào nút `Commit changes`:
![project](assets/33.webp)
- Quay lại thư mục công ty của bạn:
![project](assets/34.webp)
- Nhấp vào nút `Add file`, sau đó chọn `Create new file`:
![project](assets/35.webp)
- Tạo một file YAML mới và đặt tên theo mã ngôn ngữ bản địa của bạn. file này sẽ được sử dụng để mô tả về "project". Ví dụ, nếu tôi muốn viết mô tả của mình bằng tiếng Việt, tôi sẽ đặt tên file này là `vi.yml`:
![project](assets/36.webp)
- Điền vào file YAML này sử dụng mẫu sau:

```yaml
description: |
 
contributors:
 - 
```

- Đối với khóa `contributors`, bạn có thể thêm mã định danh của người đóng góp (contributor) vào Plan ₿ Academy nếu có. Nếu không, hãy để trống trường này.
- Đối với khóa `description`, bạn chỉ cần thêm một đoạn văn ngắn mô tả về công ty hoặc phần mềm của bạn. Mô tả phải bằng ngôn ngữ giống như tên file. Bạn không cần phải dịch mô tả này sang tất cả các ngôn ngữ được hỗ trợ trên trang web, vì đội ngũ PlanB sẽ thực hiện việc này cách sử dụng mô hình ngôn ngữ của họ. Dưới đây là ví dụ minh họa cho file của bạn:

```yaml
description: |
Được thành lập vào năm 2017, Bitcoin Baguette là một hiệp hội có trụ sở tại Paris chuyên tổ chức các buổi gặp mặt và hội thảo kỹ thuật về Bitcoin. Quy tụ những người đam mê, chuyên gia và những người tò mò, để khám phá và thảo luận về những khía cạnh phức tạp của công nghệ Bitcoin. Các sự kiện của chúng tôi cung cấp nền tảng cho việc chia sẻ kiến thức, kết nối và đào sâu hơn về cách thức hoạt động bên trong của Bitcoin. Tham gia cùng chúng tôi tại Bitcoin Baguette để trở thành một phần của cộng đồng Bitcoin tại Paris và cập nhật những tiến bộ mới nhất trong lĩnh vực này.

contributors:
- 
```

![project](assets/37.webp)
- Nhấn vào nút `Commit changes`:
![project](assets/38.webp)
- Đảm bảo rằng ô `Commit directly to the patch-1 branch` đã được chọn, thêm tiêu đề, sau đó nhấn `Commit changes`:
![project](assets/39.webp)
- Thư mục của công ty bạn giờ đây sẽ trông như thế này:
![project](assets/40.webp)
- Nếu mọi thứ đều đã ổn, quay lại thư mục gốc của bản fork:
![project](assets/41.webp)
- Bạn sẽ thấy một thông báo cho biết nhánh của mình vừa có thay đổi mới. Nhấn vào nút `Compare & pull request`:
![project](assets/42.webp)
- Thêm một tiêu đề và mô tả rõ ràng cho PR (Pull Request) của bạn:
![project](assets/43.webp)
- Nhấn vào nút `Create pull request`:
![project](assets/44.webp)

Chúc mừng! Pull Request của bạn đã được khởi tạo thành công. Đội ngũ quản trị viên sẽ tiến hành kiểm tra và nếu mọi thứ đều đạt yêu cầu, họ sẽ gộp (merge) nó vào repository chính của Plan ₿ Academy. Bạn sẽ thấy bộ công cụ giáo dục (BET) của mình xuất hiện trên website sau vài ngày.

Đừng quên theo dõi tiến độ của bản PR nhé. Quản trị viên có thể để lại bình luận yêu cầu bổ sung thông tin hoặc điều chỉnh. Chừng nào PR của bạn chưa được phê duyệt, bạn vẫn có thể theo dõi PR này trong thẻ `Pull requests` trên repository của Plan ₿ Academy:

![project](assets/45.webp)

Chân thành cảm ơn sự đóng góp quý giá của bạn! :)

