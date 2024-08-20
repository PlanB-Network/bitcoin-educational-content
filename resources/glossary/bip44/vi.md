---
term: BIP44
---

Một đề xuất cải tiến giới thiệu cấu trúc phái sinh phân cấp chuẩn cho ví HD. BIP44 xây dựng dựa trên các nguyên tắc được thiết lập bởi BIP32 cho việc phái sinh khóa và BIP43 cho việc sử dụng trường “mục đích”. Nó giới thiệu một cấu trúc phái sinh năm cấp độ: `m / purpose' / coin_type' / account' / change / address_index`. Dưới đây là chi tiết của mỗi cấp độ:
* `m /` chỉ khóa riêng tư chính. Nó là duy nhất đối với một ví và không thể có anh chị em cùng cấp độ. Khóa chính được phái sinh trực tiếp từ hạt giống của ví;
* `m / purpose' /` chỉ mục đích phái sinh giúp xác định tiêu chuẩn được tuân theo. Trường này được mô tả trong BIP43. Ví dụ, nếu ví tuân theo tiêu chuẩn BIP84 (SegWit V0), chỉ số sẽ là `84'`;
* `m / purpose' / coin-type' /` chỉ loại tiền điện tử. Điều này cho phép phân biệt rõ ràng giữa các nhánh dành riêng cho một loại tiền điện tử và những nhánh dành cho loại tiền điện tử khác trong một ví đa tiền. Chỉ số dành riêng cho Bitcoin là `0'`;
* `m / purpose' / coin-type' / account' /` chỉ số tài khoản. Cấp độ này cho phép phân biệt và tổ chức dễ dàng một ví thành các tài khoản khác nhau. Các tài khoản được đánh số bắt đầu từ `0'`. Khóa mở rộng (`xpub`, `xprv`...) được tìm thấy ở cấp độ này;
* `m / purpose' / coin-type' / account' / change /` chỉ chuỗi. Mỗi tài khoản như được định nghĩa ở cấp độ 3 có hai chuỗi tại cấp độ 4: một chuỗi bên ngoài và một chuỗi bên trong (còn được gọi là “change”). Chuỗi bên ngoài phái sinh địa chỉ dự định được công bố công khai, tức là, các địa chỉ được chúng ta nhận khi nhấp vào “nhận” trong phần mềm ví của mình. Chuỗi bên trong phái sinh địa chỉ không dự định được trao đổi công khai, tức là, chủ yếu là địa chỉ thối. Chuỗi bên ngoài được xác định với chỉ số `0` và chuỗi bên trong được xác định với chỉ số `1`. Bạn sẽ nhận thấy rằng từ cấp độ này, chúng ta không thực hiện phái sinh cứng, mà là phái sinh bình thường (không có dấu nháy). Nhờ cơ chế này mà chúng ta có khả năng phái sinh tất cả các khóa công khai con từ `xpub` của chúng;
* `m / purpose' / coin-type' / account' / change / address-index` chỉ đơn giản là số của địa chỉ nhận và cặp khóa của nó, để phân biệt nó với các địa chỉ anh chị em cùng cấp độ trên cùng một nhánh. Ví dụ, địa chỉ nhận đầu tiên có chỉ số `0`, địa chỉ thứ hai có chỉ số `1`, và tiếp tục như vậy...
Ví dụ, nếu địa chỉ nhận của tôi có đường dẫn phái sinh `m / 86' / 0' / 0' / 0 / 5`, chúng ta có thể suy luận thông tin sau:
* `86'` chỉ ra rằng chúng ta đang tuân theo tiêu chuẩn phái sinh của BIP86 (Taproot hoặc SegWitV1);
* `0'` chỉ ra rằng đó là một địa chỉ Bitcoin;
* `0'` chỉ ra rằng chúng ta đang ở tài khoản đầu tiên của ví;
* `0` chỉ ra rằng đó là một địa chỉ bên ngoài;
* `5` chỉ ra rằng đó là địa chỉ bên ngoài thứ sáu của tài khoản này.

![](../../dictionnaire/assets/18.png)