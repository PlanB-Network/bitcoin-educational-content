---
term: Commitment
---

Commitment (theo nghĩa mật mã) là một đối tượng toán học, được ký hiệu là $C$, được suy ra một cách xác định từ một phép toán trên dữ liệu có cấu trúc $m$ (thông điệp) và một giá trị ngẫu nhiên $r$. Chúng ta viết:


$$
C = \text{commit}(m, r)
$$


Cơ chế này bao gồm hai hoạt động chính:




- Cam kết: chúng tôi áp dụng một hàm mật mã cho một thông điệp $m$ và một $r$ ngẫu nhiên để tạo ra $C$;
- Xác minh: chúng ta sử dụng $C$, thông điệp $m$ và giá trị $r$ để kiểm tra xem Commitment này có đúng không. Hàm trả về `True` hoặc `False`.


Commitment phải tôn trọng hai đặc tính sau:




- Liên kết: không thể tìm thấy hai thông điệp khác nhau tạo ra cùng một $C$:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Chẳng hạn như :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Ẩn: kiến thức về $C$ không được tiết lộ nội dung của $m$.


Trong trường hợp giao thức RGB, Commitment được đưa vào giao dịch Bitcoin để chứng minh sự tồn tại của một thông tin nhất định tại một thời điểm nhất định mà không tiết lộ thông tin đó.