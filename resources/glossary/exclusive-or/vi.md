---
term: EXCLUSIVE OR
---

Một chức năng cơ bản của logic Boolean. "Exclusive Or" hay XOR ("*Exclusive or*") nhận hai toán hạng Boolean, mỗi toán hạng có thể là đúng hoặc sai, và chỉ tạo ra kết quả đúng khi hai toán hạng khác nhau. Nói cách khác, kết quả của phép toán `XOR` là đúng nếu chỉ một (nhưng không phải cả hai) trong số các toán hạng là đúng. Ví dụ, phép toán `XOR` giữa `1` và `0` sẽ cho kết quả là `1`. Chúng ta ghi chú: $1 \oplus 0 = 1$. Tương tự, phép toán `XOR` cũng có thể được thực hiện trên các chuỗi bit dài hơn. Ví dụ, $10110 \oplus 01110 = 11000$. Mỗi bit của chuỗi được so sánh với đối tác của nó, và phép toán `XOR` được áp dụng. Dưới đây là bảng chân lý cho phép toán `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

Phép toán `XOR` được sử dụng trong nhiều lĩnh vực của khoa học máy tính, đặc biệt là trong mật mã học, vì những đặc tính thú vị như:
* Tính giao hoán: thứ tự của các toán hạng không ảnh hưởng đến kết quả. Đối với hai biến cho trước $D$ và $E$: $D \oplus E = E \oplus D$;
* Tính kết hợp: việc nhóm các toán hạng không ảnh hưởng đến kết quả. Đối với ba biến cho trước $A$, $B$, và $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Có một phần tử trung lập `0`: một toán hạng được xor với 0 sẽ luôn bằng chính nó. Đối với một biến cho trước $A$: $A \oplus 0 = A$;
* Mỗi phần tử là nghịch đảo của chính nó. Đối với một biến cho trước $A$: $A \oplus A = 0$.

Trong bối cảnh của Bitcoin, phép toán `XOR` rõ ràng được sử dụng ở nhiều nơi. Ví dụ, `XOR` được sử dụng rộng rãi trong hàm `SHA256`, hàm này được sử dụng rộng rãi trong giao thức Bitcoin. Một số giao thức như *SeedXOR* của Coldcard cũng sử dụng nguyên tắc này cho các ứng dụng khác. Nó cũng được tìm thấy trong BIP47 để mã hóa mã thanh toán có thể tái sử dụng trong quá trình truyền dẫn.
Trong lĩnh vực rộng lớn hơn của mật mã học, `XOR` có thể được sử dụng như là một thuật toán mã hóa đối xứng. Thuật toán này được gọi là "One-Time Pad" hoặc "Vernam Cipher," đặt theo tên của người phát minh. Mặc dù không thực tế do độ dài của khóa, thuật toán này là một trong số ít các thuật toán mã hóa được công nhận là an toàn không điều kiện.