---
term: NONCE
---

Trong bối cảnh của ngành công nghệ thông tin, thuật ngữ "nonce" ám chỉ một số được sử dụng một lần và sau đó được thay thế. Số này thường là ngẫu nhiên hoặc giả ngẫu nhiên. Nonce được sử dụng trong nhiều giao thức mật mã để đảm bảo an ninh cho quá trình. Ví dụ, chữ ký ECDSA được sử dụng trong giao thức Bitcoin bao gồm việc sử dụng nonce. Điều này có nghĩa là số này phải mới cho mỗi chữ ký. Nếu không làm như vậy, có thể tính toán được khóa riêng được sử dụng bằng cách so sánh hai chữ ký sử dụng cùng một nonce.

Nonce cũng được sử dụng trong quá trình đào Bitcoin. Các thợ mỏ tăng giá trị có thể thay đổi này trong các khối ứng viên của họ. Họ thay đổi giá trị nonce để tìm ra một băm mật mã thấp hơn hoặc bằng với mục tiêu khó khăn. Quá trình này đòi hỏi sức mạnh tính toán đáng kể, vì nó liên quan đến việc tìm kiếm cạn kiệt trong số lượng lớn các nonce có thể. Khi một thợ mỏ tìm thấy một nonce mà, khi được bao gồm trong khối của họ, tạo ra một bản tóm tắt đáp ứng các tiêu chí khó khăn, khối được phát sóng đến mạng, và thợ mỏ giành được phần thưởng.

> ► *Vào năm 2010, các nhà nghiên cứu phát hiện ra rằng PlayStation 3 của Sony sử dụng cùng một nonce khi ký các gói mã khác nhau. Việc tái sử dụng nonce này cho phép kẻ tấn công tính toán được khóa riêng được sử dụng để ký phần mềm. Với khóa riêng trong tay, kẻ tấn công có thể tạo chữ ký hợp lệ cho bất kỳ mã nào, cho phép họ chạy phần mềm không được ủy quyền, bao gồm cả trò chơi lậu hoặc hệ điều hành tùy chỉnh, trực tiếp trên PS3.*

> ► *Có một quan niệm sai lầm phổ biến về nguồn gốc của thuật ngữ "nonce." Một số người cho rằng nó đại diện cho từ viết tắt của "number only used once" (số chỉ sử dụng một lần). Trên thực tế, nguồn gốc của từ này bắt nguồn từ thế kỷ 18 và đến từ sự tiến hóa ngữ nghĩa của cụm từ tiếng Anh cổ "then anes," có nghĩa là "cho dịp này."*