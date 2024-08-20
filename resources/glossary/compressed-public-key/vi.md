---
term: KHÓA CÔNG KHAI NÉN
---

Khóa công khai được sử dụng trong các script (hoặc trực tiếp dưới dạng khóa công khai hoặc dưới dạng địa chỉ) để nhận và bảo mật bitcoin. Một khóa công khai thô được biểu diễn bởi một điểm trên đường cong elliptic, bao gồm hai tọa độ (`x, y`) mỗi tọa độ 256 bit. Trong định dạng thô, một khóa công khai do đó có độ dài 512 bit, không tính byte bổ sung để xác định định dạng. Mặt khác, khóa công khai nén là một dạng biểu diễn khóa công khai gọn nhẹ hơn. Nó chỉ sử dụng tọa độ `x` và một tiền tố (`02` hoặc `03`) chỉ ra tính chẵn lẻ của tọa độ `y` (chẵn hoặc lẻ).

Nếu chúng ta đơn giản hóa điều này trong lĩnh vực số thực, với đường cong elliptic đối xứng qua trục x, cho bất kỳ điểm $P$ (`x, y`) nào trên đường cong, sẽ tồn tại một điểm $P'$ (`x, -y`) cũng sẽ nằm trên cùng một đường cong này. Điều này có nghĩa là cho mỗi `x`, chỉ có hai giá trị có thể của `y`, dương và âm. Ví dụ, cho một hoành độ `x` đã cho, sẽ có hai điểm $P1$ và $P2$ trên đường cong elliptic, chia sẻ cùng một hoành độ nhưng với tung độ đối diện:

![](../../dictionnaire/assets/29.png)
Để chọn giữa hai điểm tiềm năng trên đường cong, một tiền tố chỉ định `y` nào được chọn được thêm vào `x`. Phương pháp này cho phép giảm kích thước của một khóa công khai từ 520 bit xuống chỉ còn 264 bit (8 bit của tiền tố + 256 bit cho `x`). Đại diện này được biết đến là dạng nén của khóa công khai.

Tuy nhiên, trong bối cảnh của mật mã học đường cong elliptic, chúng ta sử dụng không phải là số thực, mà là một trường hữu hạn có thứ tự `p` (một số nguyên tố). Trong bối cảnh này, "dấu" của `y` được xác định bởi tính chẵn lẻ của nó, tức là `y` là chẵn hay lẻ. Tiền tố `0x02` sau đó chỉ ra `y` chẵn, trong khi `0x03` chỉ ra `y` lẻ.

Xem xét ví dụ sau của một khóa công khai thô (một điểm trên đường cong elliptic) dưới dạng hệ thập lục phân:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Chúng ta có thể tách riêng tiền tố, `x`, và `y`:
```plaintext
Tiền tố = 04
Để xác định tính chẵn lẻ của `y`, chúng ta kiểm tra ký tự thập lục phân cuối cùng của `y`:
```plaintext
Cơ sở 16 (thập lục phân): f
Cơ sở 10 (thập phân): 15
y là lẻ
```

Tiền tố cho khóa công khai nén sẽ là `03`. Khóa công khai nén dưới dạng hệ thập lục phân trở thành:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```