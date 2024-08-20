---
term: MÃ THANH TOÁN CÓ THỂ TÁI SỬ DỤNG
---

Trong BIP47, một mã thanh toán có thể tái sử dụng là một định danh tĩnh được tạo ra từ một ví Bitcoin cho phép thực hiện giao dịch thông báo và tạo ra các địa chỉ duy nhất. Điều này tránh việc sử dụng lại các địa chỉ, dẫn đến mất tính riêng tư, mà không cần phải thủ công tạo và truyền địa chỉ mới, chưa sử dụng cho mỗi giao dịch. Trong BIP47, mã thanh toán có thể tái sử dụng được xây dựng như sau:
* Byte 0 tương ứng với phiên bản;
* Byte 1 là một trường bit để thêm thông tin trong trường hợp sử dụng cụ thể;
* Byte 2 chỉ ra tính chẵn lẻ của `y` của khóa công khai;
* Từ byte 3 đến byte 34, bạn sẽ tìm thấy giá trị `x` của khóa công khai;
* Từ byte 35 đến byte 66, có mã chuỗi liên kết với khóa công khai;
* Từ byte 67 đến byte 79, có phần đệm không.

Một Phần Dễ Đọc (HRP) thường được thêm vào đầu mã thanh toán và một mã kiểm tra ở cuối, sau đó nó được mã hóa trong base58. Việc xây dựng một mã thanh toán do đó khá giống với việc xây dựng một khóa mở rộng. Dưới đây là mã thanh toán BIP47 của tôi dưới dạng base58, ví dụ:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Trong triển khai PayNym của BIP47, mã thanh toán cũng có thể được biểu diễn dưới dạng các định danh liên kết với hình ảnh của một robot. Dưới đây là của tôi, ví dụ:

```text
+throbbingpond8B1
```

Việc sử dụng mã thanh toán với triển khai PayNym hiện đang có sẵn trên Sparrow Wallet trên PC và trên Samourai Wallet trên di động.