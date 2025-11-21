---
term: ĐIỀU CHỈNH
---

Trong mật mã học, "điều chỉnh" khóa công khai là sửa đổi khóa công khai bằng cách sử dụng giá trị cộng được gọi là "điều chỉnh", để khóa công khai vẫn có thể sử dụng được khi biết cả khóa riêng tư gốc và điều chỉnh. Về mặt kỹ thuật, điều chỉnh là giá trị vô hướng được thêm vào khóa công khai gốc. Nếu $P$ là khóa công khai và $t$ là điều chỉnh, khóa công khai đã điều chỉnh sẽ trở thành:


$$
P' = P + tG
$$


Trong đó $G$ là trình tạo đường cong elliptic được sử dụng. Hoạt động này tạo ra một khóa công khai mới được lấy từ khóa gốc, trong khi vẫn giữ lại một số thuộc tính mật mã cho phép sử dụng khóa này. Ví dụ, phương pháp này được sử dụng cho các địa chỉ Taproot (P2TR), để cho phép chi tiêu bằng cách trình bày chữ ký Schnorr theo cách truyền thống hoặc bằng cách đáp ứng một trong các điều kiện được nêu trong Merkle Tree, còn được gọi là "MAST".