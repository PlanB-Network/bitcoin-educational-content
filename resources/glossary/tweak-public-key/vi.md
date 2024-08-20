---
term: TWEAK (PUBLIC KEY)
---

Trong lĩnh vực mật mã học, "tweaking" một khóa công khai bao gồm việc chỉnh sửa khóa này bằng cách sử dụng một giá trị cộng gọi là "tweak" để khóa vẫn có thể sử dụng được với kiến thức về khóa riêng tư gốc và tweak. Về mặt kỹ thuật, tweak là một giá trị vô hướng được cộng vào khóa công khai ban đầu. Nếu $P$ là khóa công khai và $t$ là tweak, khóa công khai được chỉnh sửa trở thành:

$$
P' = P + tG
$$

Trong đó $G$ là bộ sinh của đường cong elliptic được sử dụng. Thao tác này cho phép thu được một khóa công khai mới được phái sinh từ khóa gốc trong khi vẫn giữ lại các tính chất mật mã học nhất định làm cho nó có thể sử dụng được. Ví dụ, phương pháp này được sử dụng cho địa chỉ Taproot (P2TR) để cho phép chi tiêu bằng cách trình bày một chữ ký Schnorr theo cách truyền thống hoặc bằng cách thỏa mãn một trong các điều kiện được nêu trong một cây Merkle, còn được gọi là "MAST".

![](../../dictionnaire/assets/26.png)