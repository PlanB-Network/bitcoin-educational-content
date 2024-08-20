---
term: THANH TOÁN ẨN DANH
---

Phương pháp sử dụng địa chỉ Bitcoin tĩnh để nhận thanh toán mà không cần tái sử dụng địa chỉ, không cần tương tác, và không có liên kết trên chuỗi có thể nhìn thấy giữa các thanh toán khác nhau và địa chỉ tĩnh. Kỹ thuật này loại bỏ nhu cầu tạo ra địa chỉ nhận mới, chưa sử dụng cho mỗi giao dịch, từ đó tránh được sự tương tác thường thấy trong Bitcoin nơi người nhận phải cung cấp một địa chỉ mới cho người trả tiền.

Với Thanh Toán Ẩn Danh, người trả tiền sử dụng khóa công khai của người nhận (khóa công khai chi tiêu và khóa công khai quét) và tổng số khóa riêng của chính họ làm đầu vào để tạo ra một địa chỉ mới cho mỗi thanh toán. Chỉ có người nhận, với khóa riêng của họ, mới có thể tính toán được khóa riêng tương ứng với địa chỉ thanh toán này. ECDH (*Elliptic-Curve Diffie-Hellman*), một thuật toán trao đổi khóa mật mã, được sử dụng để thiết lập một bí mật chung, sau đó được sử dụng để suy ra địa chỉ nhận và khóa riêng (chỉ trên phía người nhận). Để xác định các Thanh Toán Ẩn Danh dành cho họ, người nhận phải quét blockchain và kiểm tra từng giao dịch phù hợp với tiêu chí của giao thức. Khác với BIP47, sử dụng một giao dịch thông báo để thiết lập kênh thanh toán, Thanh Toán Ẩn Danh loại bỏ bước này, tiết kiệm một giao dịch. Tuy nhiên, sự thỏa hiệp là người nhận phải quét tất cả các giao dịch tiềm năng để xác định, bằng cách áp dụng ECDH, liệu chúng có được gửi đến họ hay không.

Ví dụ, địa chỉ tĩnh của Bob $B$ đại diện cho sự nối tiếp của khóa công khai quét và khóa công khai chi tiêu của anh ấy:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Các khóa này đơn giản được suy ra từ con đường sau:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Địa chỉ tĩnh này được Bob công bố. Alice lấy nó để thực hiện Thanh Toán Ẩn Danh cho Bob. Cô ấy tính toán địa chỉ thanh toán của Bob $P_0$ theo cách này:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Nơi:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Với:
* $B_{\text{scan}}$: Khóa công khai quét của Bob (địa chỉ tĩnh);
* $B_{\text{spend}}$: Khóa công khai chi tiêu của Bob (địa chỉ tĩnh);
* $A$: Tổng số khóa công khai trong đầu vào (tweak);
* $a$: Khóa riêng của tweak, tức là tổng số tất cả các cặp khóa được sử dụng trong `scriptPubKey` của các UTXO tiêu thụ như đầu vào trong giao dịch của Alice;
* $\text{outpoint}_L$: UTXO nhỏ nhất (theo thứ tự từ điển) được sử dụng như một đầu vào trong giao dịch của Alice;
* $\text{ ‖ }$: Nối (thao tác kết nối các toán hạng từ đầu đến cuối);
* $G$: Điểm sinh của đường cong elliptic `secp256k1`;
* $\text{hash}$: Hàm băm SHA256 được gắn thẻ với `BIP0352/SharedSecret`;
* $P_0$: Khóa công khai / địa chỉ duy nhất đầu tiên cho thanh toán cho Bob;
* $0$: Một số nguyên được sử dụng để tạo ra nhiều địa chỉ thanh toán duy nhất.

Bob quét blockchain để tìm Thanh Toán Ẩn Danh của mình theo cách này:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Với:
* $b_{\text{scan}}$: Khóa quét riêng tư của Bob.

Nếu anh ta tìm thấy $P_0$ như một địa chỉ chứa một Khoản Thanh Toán Ẩn danh được gửi đến mình, anh ta tính toán $p_0$, khóa riêng tư cho phép anh ta chi tiêu số tiền mà Alice gửi đến $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Với:
* $b_{\text{spend}}$: Khóa chi tiêu riêng tư của Bob;
* $n$: bậc của đường cong elliptic `secp256k1`.

Ngoài phiên bản cơ bản này, nhãn cũng có thể được sử dụng để tạo ra nhiều địa chỉ tĩnh khác nhau từ cùng một địa chỉ tĩnh cơ bản, với mục tiêu phân tách nhiều mục đích sử dụng mà không làm tăng một cách không hợp lý công việc yêu cầu trong quá trình quét.