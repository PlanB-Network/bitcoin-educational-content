---
term: LABEL (THANH TOÁN IM LẶNG)
---

Trong giao thức Thanh Toán Im Lặng, nhãn là các số nguyên được sử dụng để chỉnh sửa địa chỉ tĩnh ban đầu nhằm tạo ra nhiều địa chỉ tĩnh khác. Việc sử dụng các nhãn này cho phép phân loại các khoản thanh toán được gửi qua Thanh Toán Im Lặng, bằng cách sử dụng các địa chỉ tĩnh khác nhau cho mỗi mục đích sử dụng, mà không làm tăng quá mức gánh nặng hoạt động cho việc phát hiện các khoản thanh toán này (quét). Bob sử dụng một địa chỉ tĩnh $B$, bao gồm hai khóa công khai: $B_{\text{scan}}$ để quét và $B_{\text{spend}}$ để chi tiêu. Băm của $b_{\text{scan}}$ và một số nguyên $m$, nhân vô hướng với điểm sinh $G$, được cộng vào khóa công khai chi tiêu $B_{\text{spend}}$ để tạo ra một loại khóa công khai chi tiêu mới $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Ví dụ, khóa đầu tiên $B_1$ được thu được theo cách này:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Địa chỉ tĩnh được Bob công bố bây giờ sẽ bao gồm $B_{\text{scan}}$ và $B_m$. Ví dụ, địa chỉ tĩnh đầu tiên với nhãn $1$ sẽ là:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Chúng ta chỉ bắt đầu từ nhãn $1$, vì nhãn $0$ được dành riêng cho tiền thối. Alice, người muốn gửi bitcoin đến địa chỉ tĩnh có nhãn mà Bob cung cấp, sẽ suy ra địa chỉ thanh toán duy nhất $P_0$ sử dụng $B_1$ mới thay vì $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Trên thực tế, Alice có thể không biết rằng Bob có một địa chỉ có nhãn, vì cô ấy đơn giản sử dụng phần thứ hai của địa chỉ tĩnh mà anh ấy cung cấp, trong trường hợp này là giá trị $B_1$ thay vì $B_{\text{spend}}$. Để quét các khoản thanh toán, Bob sẽ luôn sử dụng giá trị của địa chỉ tĩnh ban đầu của mình với $B_{\text{spend}}$ theo cách này:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Sau đó, anh ấy chỉ cần trừ giá trị mà anh ấy tìm thấy cho $P_0$ từ từng đầu ra một. Anh ấy sau đó kiểm tra xem kết quả của những phép trừ này có trùng với giá trị của một trong những nhãn mà anh ấy sử dụng trong ví của mình hay không. Nếu trùng khớp, ví dụ, cho đầu ra #4 với nhãn $1$, điều này có nghĩa là đầu ra này là một Khoản Thanh Toán Im Lặng liên kết với địa chỉ tĩnh có nhãn $B_1$ của anh ấy:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Điều này hoạt động vì:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Nhờ phương pháp này, Bob có thể sử dụng nhiều địa chỉ tĩnh (với $B_1$, $B_2$, $B_3$...), tất cả đều được phát sinh từ địa chỉ tĩnh cơ bản của mình ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), nhằm mục đích tách biệt các mục đích sử dụng một cách rõ ràng.

Tuy nhiên, việc tách biệt các địa chỉ tĩnh này chỉ có giá trị từ góc độ quản lý ví cá nhân, nhưng không cho phép tách biệt các danh tính. Vì tất cả chúng đều có cùng $B_{\text{scan}}$, việc liên kết tất cả các địa chỉ tĩnh lại với nhau và suy luận rằng chúng thuộc về một thực thể duy nhất là rất dễ dàng.