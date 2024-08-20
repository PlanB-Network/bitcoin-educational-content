---
term: CHAIN CODE
---

Trong bối cảnh của việc phát sinh xác định phân cấp (HD) cho ví Bitcoin, chain code là một giá trị muối mã hóa 256-bit được sử dụng để tạo ra các khóa con từ một khóa cha, theo tiêu chuẩn BIP32. Chain code được sử dụng kết hợp với khóa cha và chỉ số của khóa con để tạo ra một cặp khóa mới (khóa riêng tư và khóa công khai) mà không tiết lộ khóa cha hoặc các khóa con khác đã được phát sinh.

Do đó, mỗi cặp khóa có một chain code duy nhất. Chain code được lấy hoặc bằng cách băm hạt giống của ví và lấy nửa phải của các bit. Trong trường hợp này, nó được gọi là master chain code, liên kết với master private key. Mặt khác, nó có thể được lấy bằng cách băm một khóa cha với chain code của nó và một chỉ số, sau đó giữ lại các bit bên phải. Điều này sau đó được gọi là child chain code.

Không thể phát sinh khóa mà không biết chain code liên kết với mỗi cặp khóa cha. Nó đưa dữ liệu giả ngẫu nhiên vào quá trình phát sinh để đảm bảo rằng việc tạo ra các khóa mã hóa vẫn không thể dự đoán được đối với kẻ tấn công trong khi vẫn xác định được cho chủ sở hữu ví.

> ► *Trong tiếng Anh, "code de chaîne" được gọi là "chain code", và "code de chaîne maître" được gọi là "master chain code".*