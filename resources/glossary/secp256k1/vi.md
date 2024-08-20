---
term: SECP256K1
---

Tên gọi của một đường cong elliptic cụ thể được sử dụng trong giao thức Bitcoin cho việc triển khai các thuật toán chữ ký số ECDSA (*Elliptic Curve Digital Signature Algorithm*) và Schnorr. Đường cong `secp256k1` được chọn bởi người sáng lập Bitcoin, Satoshi Nakamoto. Nó có một số tính chất thú vị, đặc biệt là lợi ích về hiệu suất.

Việc sử dụng `secp256k1` trong Bitcoin có nghĩa là mỗi khóa riêng (một số ngẫu nhiên 256-bit) được ánh xạ tới một khóa công khai tương ứng thông qua phép cộng và nhân đôi điểm của khóa riêng bởi điểm sinh của đường cong `secp256k1`. Thao tác này dễ thực hiện theo một hướng nhưng gần như không thể đảo ngược, tạo nên cơ sở cho sự an toàn của chữ ký số trên Bitcoin.

Đường cong `secp256k1` được xác định bởi phương trình đường cong elliptic $y^2 = x^3 + 7$, có nghĩa là nó có hệ số $a$ bằng $0$ và $b$ bằng $7$ trong dạng tổng quát của phương trình đường cong elliptic $y^2 = x^3 + ax + b$. `secp256k1` được định nghĩa trên một trường hữu hạn có thứ tự là một số nguyên tố rất lớn, cụ thể là $p = 2^{256} - 2^{32} - 977$. Đường cong cũng có một thứ tự nhóm, là số lượng điểm riêng biệt trên đường cong, một điểm sinh đã được xác định trước (hoặc điểm $G$), được sử dụng trong các phép toán mật mã để tạo ra các cặp khóa, và một hệ số nhỏ bằng $1$.

> ► *“SEC” viết tắt của “Standards for Efficient Cryptography”. “P256” chỉ ra rằng đường cong được định nghĩa trên một trường $\mathbb{Z}_p$ nơi $p$ là một số nguyên tố 256-bit. “K” tham chiếu đến tên của người phát minh ra nó, Neal Koblitz. Cuối cùng, “1” chỉ ra đây là phiên bản đầu tiên của đường cong này.*