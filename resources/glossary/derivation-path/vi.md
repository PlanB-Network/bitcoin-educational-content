---
term: ĐƯỜNG DẪN DẪN XUẤT
---

Trong bối cảnh của ví Định hình Phân cấp (HD wallets), đường dẫn dẫn xuất là chuỗi các chỉ số được sử dụng để dẫn xuất các khóa con từ một khóa chính. Được mô tả trong BIP32, đường dẫn này xác định cấu trúc cây để dẫn xuất các khóa con. Đường dẫn dẫn xuất được biểu diễn bởi một chuỗi các chỉ số được phân cách bởi dấu gạch chéo, và luôn bắt đầu với khóa chính (được ký hiệu là `m/`). Ví dụ, một đường dẫn điển hình có thể là `m/84'/0'/0'/0/0`. Mỗi cấp độ dẫn xuất được liên kết với một độ sâu cụ thể:
* `m /` chỉ khóa chính riêng tư. Nó là duy nhất đối với một ví và không thể có anh chị em cùng độ sâu. Khóa chính được dẫn xuất trực tiếp từ hạt giống;
* `m / purpose' /` chỉ mục đích dẫn xuất giúp xác định tiêu chuẩn được tuân theo. Trường này được mô tả trong BIP43. Ví dụ, nếu ví tuân theo tiêu chuẩn BIP84 (SegWit V0), chỉ số sẽ là `84'`;
* `m / purpose' / coin-type' /` chỉ loại tiền điện tử. Điều này cho phép phân biệt rõ ràng giữa các nhánh dành riêng cho một loại tiền điện tử với những nhánh dành cho loại khác trong một ví đa tiền tệ. Chỉ số dành riêng cho Bitcoin là `0'`;
* `m / purpose' / coin-type' / account' /` chỉ số tài khoản. Độ sâu này giúp dễ dàng phân biệt và tổ chức một ví thành các tài khoản khác nhau. Các tài khoản được đánh số bắt đầu từ `0'`. Khóa mở rộng (`xpub`, `xprv`...) được tìm thấy ở mức độ sâu này;
* `m / purpose' / coin-type' / account' / change /` chỉ đường dẫn. Mỗi tài khoản được định nghĩa ở độ sâu 3 có hai đường dẫn ở độ sâu 4: một chuỗi bên ngoài và một chuỗi bên trong (còn được gọi là "change"). Chuỗi bên ngoài dẫn xuất các địa chỉ dự định được chia sẻ công khai, tức là, các địa chỉ được chúng ta nhận khi chúng ta nhấp vào "nhận" trong phần mềm ví của mình. Chuỗi bên trong dẫn xuất các địa chỉ không dự định được trao đổi công khai, chủ yếu là các địa chỉ thay đổi. Chuỗi bên ngoài được xác định với chỉ số `0` và chuỗi bên trong được xác định với chỉ số `1`. Bạn sẽ nhận thấy rằng từ độ sâu này, chúng ta không còn thực hiện dẫn xuất cứng nhắc, mà là dẫn xuất bình thường (không có dấu nháy). Chính nhờ cơ chế này mà chúng ta có thể dẫn xuất tất cả các khóa con công khai từ `xpub` của chúng;

* `m / purpose' / coin-type' / account' / change / address-index` chỉ đơn giản là số của địa chỉ nhận và cặp khóa của nó, nhằm phân biệt nó với các địa chỉ anh chị em cùng độ sâu trên cùng một nhánh. Ví dụ, địa chỉ được dẫn xuất đầu tiên có chỉ số `0`, địa chỉ thứ hai có chỉ số `1`, và cứ thế...

Ví dụ, nếu địa chỉ nhận của tôi có đường dẫn dẫn xuất `m / 86' / 0' / 0' / 0 / 5`, chúng ta có thể suy luận thông tin sau:
* `86'` chỉ ra rằng chúng ta đang tuân theo tiêu chuẩn dẫn xuất của BIP86 (Taproot / SegWit V1);
* `0'` chỉ ra rằng đó là một địa chỉ Bitcoin;
* `0'` chỉ ra rằng chúng ta đang ở tài khoản đầu tiên của ví;
* `0` chỉ ra rằng đó là một địa chỉ bên ngoài;
* `5` chỉ ra rằng đó là địa chỉ bên ngoài thứ sáu của tài khoản này.

![](../../dictionnaire/assets/18.png)