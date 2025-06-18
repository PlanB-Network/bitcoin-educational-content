---
term: NGŨ CỐC
---

Trong bối cảnh cụ thể của danh mục đầu tư xác định theo thứ bậc Bitcoin, seed là một phần thông tin 512 bit có nguồn gốc từ một sự kiện ngẫu nhiên. Nó được sử dụng để xác định và phân cấp generate một tập hợp các khóa riêng tư và các khóa công khai tương ứng của chúng cho danh mục đầu tư Bitcoin. seed thường bị nhầm lẫn với chính cụm từ khôi phục. Nhưng chúng không phải là một. seed được lấy bằng cách áp dụng hàm `PBKDF2` cho cụm từ Mnemonic và bất kỳ passphrase nào.


seed được phát minh với BIP32, định nghĩa nền tảng của danh mục xác định phân cấp. Trong tiêu chuẩn này, seed đo được 128 bit. Điều này cho phép tất cả các khóa trong danh mục được lấy từ một thông tin duy nhất, không giống như danh mục JBOK (*Chỉ là một loạt khóa*), yêu cầu sao lưu mới cho mọi khóa được tạo. Sau đó, BIP39 đề xuất mã hóa seed này để đơn giản hóa việc đọc của con người. Mã hóa này có dạng cụm từ, thường được gọi là cụm từ Mnemonic hoặc cụm từ khôi phục. Tiêu chuẩn này tránh được lỗi khi lưu seed, đặc biệt là nhờ sử dụng tổng kiểm tra.


Ngoài bối cảnh của Bitcoin, trong mật mã học nói chung, seed là giá trị ban đầu được sử dụng cho khóa mật mã generate, hoặc rộng hơn là bất kỳ loại dữ liệu nào được tạo ra bởi trình tạo số giả ngẫu nhiên. Giá trị ban đầu này phải ngẫu nhiên và không thể đoán trước để đảm bảo tính bảo mật của hệ thống mật mã. Thật vậy, seed đưa entropy vào hệ thống, nhưng quá trình tạo ra sau đó là xác định.


> ► *Theo cách nói thông thường, phần lớn người dùng bitcoin đều nhắc đến cụm từ Mnemonic khi họ nói về "seed", chứ không phải trạng thái phái sinh trung gian nằm giữa cụm từ Mnemonic và khóa chính.*