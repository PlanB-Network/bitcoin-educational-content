---
name: Public Pool
description: Giới thiệu về Hồ Bơi Công Cộng
---

![signup](assets/cover.webp)

**Hồ Bơi Công Cộng** không chỉ là một hồ bơi bình thường; nó còn được biết đến với cái tên **Hồ Bơi Đơn**. Nếu máy đào của bạn thành công trong việc khai thác một khối, bạn sẽ nhận được toàn bộ phần thưởng của khối đó, không chia sẻ với các thành viên khác trong hồ bơi hay với chính hồ bơi.

**Hồ Bơi Công Cộng** chỉ cung cấp một **bản mẫu khối** cho máy đào của bạn để nó có thể thực hiện nhiệm vụ mà không cần bạn phải có một **nút Bitcoin** và phần mềm giao tiếp với máy đào của bạn. Vì bạn không gộp sức mạnh tính toán của mình với những người tham gia khác, cơ hội của bạn trong việc thành công khai thác một khối rõ ràng rất thấp, giống như một hệ thống xổ số, nơi đôi khi một người may mắn giành được giải độc đắc.

![signup](assets/1.webp)

Trên **Bảng Điều Khiển** của **Hồ Bơi Công Cộng**, bạn vẫn có một số thống kê như tổng **Hashrate** của hồ bơi cũng như phân phối các loại máy đào khác nhau đang kết nối với hồ bơi.

![signup](assets/2.webp)

Trong vài dòng đầu tiên, chúng ta có thể thấy **Bitaxe** với 1323 **Bitaxe** được kết nối cho tổng cộng 649TH/s. **Bitaxe** là một dự án **Mã nguồn mở** cho phép tái sử dụng đơn giản một chip từ một **ASIC** như **Antminer S19** trên một bảng mạch điện tử **mã nguồn mở** để tạo ra một máy đào nhỏ với 0.5TH/s cho 15W. Đây là máy đào mà chúng tôi sẽ sử dụng làm ví dụ cho hướng dẫn này.

## Thêm một **Người Lao Động** 👷‍♂️

![signup](assets/cover.webp)

Ở đầu trang, bạn có thể sao chép địa chỉ hồ bơi **stratum+tcp://public-pool.io:21496**.

Tiếp theo, cho trường **người dùng**, nhập địa chỉ **Bitcoin** mà bạn sở hữu.

Nếu bạn có nhiều máy đào, bạn có thể nhập cùng một địa chỉ cho tất cả chúng để **hashrate** của chúng được kết hợp và xuất hiện như một máy đào duy nhất. Bạn cũng có thể phân biệt chúng bằng cách thêm một tên riêng biệt cho mỗi máy. Để làm điều này, chỉ cần thêm **.workername** sau địa chỉ **Bitcoin**.

Cuối cùng, cho trường **mật khẩu**, sử dụng **‘x’**.

Ví dụ: Nếu địa chỉ **Bitcoin** của bạn là **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** và bạn muốn đặt tên cho máy đào của mình là **« Brrrr »**, thì bạn sẽ nhập thông tin sau vào giao diện máy đào của mình:

- **URL**: stratum+tcp://public-pool.io:21496
- **NGƯỜI DÙNG**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Mật khẩu**: **‘x’**
Nếu máy đào của bạn là **Bitaxe**, các trường thông tin hơi khác, nhưng thông tin vẫn giữ nguyên:
- **URL**: public-pool.io (ở đây, bạn cần loại bỏ phần ở đầu **‘stratum+tcp://’** và phần ở cuối **‘:21496’** sẽ được báo cáo trong trường cổng)
- **Cổng**: 21496
- **Người Dùng**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Mật khẩu**: **‘x’**

![signup](assets/3.webp)
Chỉ vài phút sau khi bạn bắt đầu đào, bạn sẽ có thể xem dữ liệu của mình trên trang web **Public Pool** bằng cách tìm kiếm địa chỉ của bạn.

## Bảng Điều Khiển

![signup](assets/4.webp)

Một khi bạn đã kết nối với **Public Pool**, bạn có thể truy cập **Bảng Điều Khiển** của mình bằng cách tìm kiếm với địa chỉ **Bitcoin** mà bạn đã nhập vào trường **Người dùng**. Trong trường hợp của chúng tôi ở đây, đó là **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

Trên **Bảng Điều Khiển**, các thông tin khác nhau được hiển thị cả về dữ liệu của bạn và về mạng lưới.

![signup](assets/5.webp)

Bạn có **Tốc Độ Hash của Mạng** tương ứng với tổng công suất làm việc của mạng lưới **Bitcoin**.

**Độ Khó của Mạng** chỉ độ khó cần đạt để xác nhận một khối.

Và **Độ Khó Tốt Nhất của Bạn** là độ khó cao nhất mà bạn đã đạt được. Nếu, may mắn 🍀, bạn đạt được độ khó của mạng, thì bạn sẽ giành được toàn bộ phần thưởng của khối... sau 100 khối. Bạn sẽ phải chờ 100 khối trước khi có thể tiêu chúng.

Bạn cũng có **Chiều Cao Khối**, là số của khối cuối cùng đã được đào cũng như trọng lượng của nó được biểu thị bằng WU, tối đa là 4,000,000.

Bên dưới, bạn có thể xem tất cả các thống kê của từng thiết bị của mình một cách riêng lẻ nếu bạn đã đặt cho chúng một tên riêng biệt bằng cách thêm **.name** phía sau địa chỉ **Bitcoin** của bạn trong trường **Người dùng**.