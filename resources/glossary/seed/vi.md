---
term: SEED
---

Trong bối cảnh cụ thể của một ví Bitcoin phân cấp xác định (hierarchical deterministic), seed là một thông tin 512-bit được tạo ra từ sự ngẫu nhiên. Nó được sử dụng để tạo ra một cách có hệ thống và phân cấp một tập hợp các khóa riêng tư và các khóa công khai tương ứng cho một ví Bitcoin. Seed thường bị nhầm lẫn với cụm từ khôi phục (recovery phrase) của nó. Tuy nhiên, đây là thông tin khác biệt. Seed được thu được bằng cách áp dụng hàm `PBKDF2` lên cụm từ ghi nhớ (mnemonic phrase) và bất kỳ cụm từ mật khẩu tiềm năng nào.

Seed được phát minh ra với sự giới thiệu của BIP32, định nghĩa nền tảng của ví phân cấp xác định. Trong tiêu chuẩn này, seed có 128 bit. Điều này cho phép việc tạo ra tất cả các khóa trong một ví từ một thông tin đơn lẻ, không giống như ví JBOK (*Just a Bunch Of Keys*), yêu cầu sao lưu mới cho mỗi khóa được tạo ra. BIP39 sau đó đã giới thiệu một cách mã hóa seed này để đơn giản hóa việc đọc của con người. Việc mã hóa này được thực hiện dưới dạng một cụm từ, thường được gọi là cụm từ ghi nhớ hoặc cụm từ khôi phục. Tiêu chuẩn này giúp tránh lỗi trong việc sao lưu seed, đặc biệt thông qua việc sử dụng một mã kiểm tra.

Một cách tổng quát hơn, trong mật mã học, seed là một mẩu dữ liệu ngẫu nhiên được sử dụng như một điểm khởi đầu để tạo ra các khóa mật mã, mã hóa, hoặc chuỗi giả ngẫu nhiên. Chất lượng và an ninh của nhiều quy trình mật mã phụ thuộc vào sự ngẫu nhiên và bảo mật của seed.

> ► *Bản dịch tiếng Anh của "graine" là "seed". Trong tiếng Pháp, nhiều người trực tiếp sử dụng từ tiếng Anh để chỉ seed.*