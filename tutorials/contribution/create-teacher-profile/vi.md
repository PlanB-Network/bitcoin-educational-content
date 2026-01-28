---
name: Giáo sư Plan ₿ Academy
description: Làm thế nào để thêm hoặc sửa đổi hồ sơ giảng viên của tôi trên Plan ₿ Academy?
---
![cover](assets/cover.webp)

Nếu bạn có kế hoạch đóng góp cho Plan ₿ Academy bằng cách viết bài hướng dẫn hoặc khóa học mới, bạn sẽ cần tạo một hồ sơ giảng viên. Hồ sơ này sẽ giúp hệ thống ghi nhận đóng góp và xác nhận quyền tác giả tương ứng cho những nội dung mà bạn cung cấp trên nền tảng.

Đối với những ai đã từng tham gia xây dựng nội dung giáo dục trên Plan ₿ Academy, có thể bạn đã có hồ sơ giảng viên. Bạn có thể tìm thông tin trong thư mục `/professors` [trên repository (repository) GitHub của chúng tôi](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Nếu hồ sơ của bạn đã tồn tại, hãy tìm tên định danh của bạn trong file `professor.yml`.

Để thay đổi hồ sơ của bạn, hãy xem phần "Sửa đổi hồ sơ giảng viên của bạn" ở cuối bài hướng dẫn này.

## Thêm giảng viên mới bằng phần mềm của chúng tôi

Cách đơn giản nhất để tạo hồ sơ giảng viên trên Plan ₿ Academy là sử dụng công cụ tích hợp được viết bằng Python của chúng tôi. Dưới đây là quy trình vận hành của công cụ này.

### 1 - Cấu hình môi trường cục bộ của bạn

Bạn phải có bản fork của riêng mình từ [repository của Plan ₿ Academy trên GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).

Đồng bộ hóa nhánh chính (`dev`) của bản fork với repository gốc.

Cập nhật bản sao cục bộ (local clone) của bạn.

```bash
# Tạo bản sao cục bộ (clone) cho bản fork của bạn (nếu bạn chưa làm)
git clone https://github.com/<username>/bitcoin-educational-content.git

cd bitcoin-educational-content

# Thêm repository gốc làm remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Cập nhật các thay đổi mới nhất từ repository gốc
git fetch upstream

# Chuyển sang nhánh chính "dev"
git checkout dev

# Merge những thay đổi từ nhánh "dev" của repository gốc vào bản fork của bạn
git merge upstream/dev

# Đẩy các bản cập nhật lên bản fork của bạn trên GitHub
git push origin dev
```

### 2 - Tạo nhánh mới

Đảm bảo bạn đang ở nhánh `dev`. Tạo một nhánh mới với tên mô tả (ví dụ: `add-professor-loic-morel`).

Đẩy nhánh này lên bản fork trực tuyến

```bash
# Đảm bảo bạn vẫn đang ở nhánh 'dev'
git checkout dev

# Tạo một nhánh với tên dễ nhớ
git checkout -b add-professor-loic-morel

# Đẩy nhánh này lên bản fork trực tuyến
git push -u origin add-professor-loic-morel
```

### 3 - Tạo hồ sơ giảng viên của bạn

Đi đến thư mục `scripts/tutorial-related/data-creator/` trong bản clone trên máy tính của bạn. Hãy đảm bảo rằng bạn đã cài đặt Python và tất cả các thư viện phụ thuộc (dependencies) cần thiết cho phần mềm:

```bash
pip install -r requirements.txt
```

Sau đó, khởi chạy phần mềm bằng lệnh:

```bash
python3 main.py
```

Khi đã vào trang chủ, hãy nhập đường dẫn cục bộ đến bản clone, ngôn ngữ bạn đang viết và GitHub ID của bạn. Nếu bạn đang tạo hồ sơ này cho người khác và đã có hồ sơ Professor, hãy nhập ID vào trường `Plan ₿ Academy Professor's ID`. Nếu bạn đang tạo hồ sơ của riêng mình, bạn sẽ chưa có Professor's ID  vì bạn đang trong quá trình khởi tạo, vì vậy hãy để trống trường này.

Sau đó nhấp vào nút `New Professor`.

![Image](assets/fr/01.webp)

Điền đầy đủ các thông tin bắt buộc (vui lòng lưu ý rằng tất cả các thông tin này sẽ được công khai trên nền tảng của chúng tôi cũng như trên GitHub):


- Tên hồ sơ giảng viên của bạn (sử dụng tên và họ hoặc bút danh, viết chữ thường không dấu);
- Tên hoặc biệt danh của bạn;
- Website và hồ sơ của bạn X (không bắt buộc);
- Địa chỉ Lightning để nhận đóng góp từ độc giả (tùy chọn);
- Chọn 2 hoặc 3 thẻ (tags) từ danh sách;
- Nhấn vào "*Select Image*" để chọn ảnh đại diện từ máy tính (phần mềm sẽ tự động xử lý mọi định dạng và tên file. Bạn chỉ cần đảm bảo ảnh có tỷ lệ khung hình vuông);
- Viết mô tả ngắn cho hồ sơ của bạn.

Hoàn tất việc tạo bằng cách nhấn vào `Create Professor`. Thao tác này sẽ tự động tạo tất cả các file cần thiết cho hồ sơ của bạn.

![Image](assets/fr/02.webp)

Lưu các thay đổi cục bộ của bạn bằng cách tạo một commit kèm mô tả. Đẩy các thay đổi lên bản fork trên GitHub.

```bash
# Tạo một commit với mô tả rõ ràng.
git commit -m "*new professor Loïc Morel*"

# Đẩy các thay đổi của bạn lên bản fork của bạn.
git push origin add-professor-loic-morel
```

Sau khi hoàn tất, hãy tạo Pull Request (PR) trên GitHub để tạo 1 bản đề xuất merge các sửa đổi của bạn. Thêm tiêu đề và mô tả ngắn gọn vào PR.

### 4 - Hiệu đính (proofreading) và merge

Hãy chờ quản trị viên phê duyệt hoặc phản hồi. Nếu cần thiết, hãy thực hiện các chỉnh sửa và đẩy thêm các commit mới.

```bash
# Tạo một commit mô tả các chỉnh sửa đã thực hiện
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"

# Đẩy các thay đổi lên bản fork của bạn
git push origin add-professor-loic-morel
```

Sau khi PR đã được merge, bạn có thể xóa nhánh làm việc của mình.

## Chỉnh sửa hồ sơ giảng viên của bạn

Nếu bạn đã thành thạo Git, hãy chỉnh sửa hồ sơ giảng viên bằng cách tạo một nhánh mới và thực hiện chỉnh sửa trực tiếp file tin liên quan trong thư mục hiện có của bạn. Các thay đổi có thể thực hiện trong file `professor.yml` hoặc trong file markdown, tùy thuộc vào thông tin cần sửa. Sau khi thay đổi cục bộ, hãy đẩy chúng lên bản fork và gửi một PR.

Đối với người mới bắt đầu, tôi khuyên bạn nên thực hiện chỉnh sửa trực tiếp thông qua giao diện web của GitHub. Hãy đảm bảo bạn đã có tài khoản GitHub. Nếu chưa biết cách tạo, hãy theo dõi bài hướng dẫn này:

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Truy cập [repository Plan ₿ Academy dành riêng cho dữ liệu trên GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Nhấ vào thư mục `professors`, sau đó tìm đến thư mục cá nhân của bạn.

![Image](assets/fr/04.webp)

Để thay đổi metadata của hồ sơ như địa chỉ Lightning, tên hoặc các liên kết, hãy chọn file `professor.yml`. Để thay đổi phần mô tả, hãy nhấn vào file YAML tương ứng với ngôn ngữ của bạn (ví dụ: `en.yml` hoặc `vi.yml`).

Nếu bạn sửa đổi phần mô tả, hãy nhớ xóa bỏ tất cả các bản dịch đã cũ. Sau đó, bạn có thể tự dịch mô tả sang các ngôn ngữ khác với sự trợ giúp của LLM, hoặc chỉ cần để lại phần mô tả bằng ngôn ngữ mẹ đẻ và ghi chú trong Pull Request rằng phần mô tả này cần được đội ngũ của chúng tôi hỗ trợ dịch thuật.

![Image](assets/fr/05.webp)

Khi đã mở file bạn muốn sửa đổi, hãy nhấp vào biểu tượng bút chì.

![Image](assets/fr/06.webp)

Nếu bạn chưa có có bản fork từ repository của Plan ₿ Academy, GitHub sẽ gợi ý bạn tạo một bản. Nhấp vào `Fork this repository`.

![Image](assets/fr/07.webp)

Thực hiện các thay đổi mong muốn trong file này. Sau khi hoàn tất, nhấn chọn `Commit changes`.

![Image](assets/fr/08.webp)

Nhập mô tả thay đổi của bạn, sau đó chọn `Propose changes`.

![Image](assets/fr/09.webp)

Một bảng tóm tắt các thay đổi sẽ hiển thị. Nếu muốn thực hiện thêm các chỉnh sửa khác cho hồ sơ, bạn có thể quay lại các thư mục và tạo thêm các commit khác. Khi đã thực hiện xong, nhấn chọn `Create pull request`.

Pull Request là một yêu cầu được gửi đi để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của repository Plan ₿ Academy, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được merge chính thức.

![Image](assets/fr/10.webp)

Hãy đảm bảo rằng ở phía trên cùng của giao diện, nhánh làm việc của bạn đang được merge vào nhánh `dev` (đây là nhánh chính) của repository Plan ₿ Academy.

Nhập tiêu đề tóm tắt ngắn gọn các thay đổi bạn muốn merge vào repository gốc. Thêm một bình luận ngắn mô tả những thay đổi này, sau đó nhấn vào nút `Create pull request` để xác nhận:

![Image](assets/fr/11.webp)

PR của bạn sẽ hiển thị trong tab `Pull Request` của repository gốc Plan ₿ Academy. Việc cuối cùng bạn cần làm là chờ quản trị viên merge những thay đổi của mình.

![Image](assets/fr/12.webp)

Nếu bạn gặp bất kỳ khó khăn kỹ thuật nào trong quá trình gửi thay đổi, đừng ngần ngại gửi yêu cầu hỗ trợ tại [nhóm Telegram của chúng tôi dành riêng cho các đóng góp](https://t.me/PlanBNetwork_ContentBuilder). Xin chân thành cảm ơn!