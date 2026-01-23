---
name: Nhãn thời gian (Timestamp) cho chứng chỉ và bằng cấp Plan ₿ Academy
description: Hiểu cách Plan ₿ Academy phát hành các bằng chứng có thể xác minh cho chứng chỉ và bằng cấp của bạn
---

![cover](assets/cover.webp)

Nếu bạn đang đọc những dòng này, rất có thể bạn vừa nhận được một chứng chỉ cho bài kiểm tra ₿-CERT hoặc một bằng cấp hoàn thành khóa học trên Plan ₿ Academy. Vì vậy, xin chúc mừng bạn đã đạt được thành tựu này!

Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách Plan ₿ Academy cấp các bằng chứng có thể xác minh cho chứng chỉ ₿-CERT hoặc chứng nhận hoàn thành khóa học. Ở phần thứ hai, chúng ta sẽ xem cách xác minh tính xác thực của các bằng chứng này.


## Cơ chế tạo bằng chứng của Plan ₿ Academy

Tại Plan ₿ Academy, chúng tôi cấp các chứng chỉ và bằng cấp được ký bằng mật mã và được gắn nhãn thời gian (timestamp) trên Timechain (tức là blockchain Bitcoin). Để làm được điều này, chúng tôi đã thiết kế một cơ chế bằng chứng dựa trên hai thao tác mật mã:

1. Một chữ ký GPG trên một file văn bản tổng hợp thành tựu của bạn
2. Gán nhãn thời gian cho file đã ký thông qua [opentimestamps](https://opentimestamps.org/).

Thao tác đầu tiên cho phép bạn xác minh đơn vị cấp chứng chỉ (hoặc bằng cấp), trong khi thao tác thứ hai cho phép bạn xác minh thời điểm được cấp.  
Chúng tôi tin rằng cơ chế cấp bằng chứng đơn giản này cho phép chúng tôi cấp chứng chỉ và bằng cấp với bằng chứng không thể chối cãi mà bất kỳ ai cũng có thể tự mình xác minh.

![image](./assets/proof-mechanism.webp)

Nhờ vào cơ chế này, bất kỳ nỗ lực nào nhằm thay đổi ngay cả chi tiết nhỏ nhất của chứng chỉ hoặc bằng cấp của bạn sẽ tạo ra một mã băm SHA-256 hoàn toàn khác so với file đã ký. Khi đó, việc giả mạo chứng chỉ hoặc bằng cấp do Plan ₿ Academy cấp sẽ ngay lập tức bị phát hiện vì chữ ký và nhãn thời gian không còn hợp lệ.  


### Chữ ký GPG hoạt động như thế nào?

Chữ ký GPG được tạo ra bằng một phần mềm mã nguồn mở có tên là GNU Privacy Guard. Phần mềm này cho phép bất kỳ ai dễ dàng tạo khóa riêng (private key), ký và xác minh chữ ký cũng như mã hóa và giải mã files. Trong phạm vi của hướng dẫn này, bạn chỉ cần biết rằng Plan ₿ Academy sử dụng GPG để tạo cặp khóa riêng/khóa công khai, và để ký vào bất kỳ chứng chỉ ₿-CERT hoặc chứng nhận hoàn thành khoá học của nền tảng.

Mặt khác, nếu ai đó muốn xác minh tính xác thực của một file đã ký, họ có thể sử dụng GPG để nhập khóa công khai của người phát hành và xác minh. Trong phần thứ hai của hướng dẫn, chúng ta sẽ xem cách thực hiện việc này thông qua terminal.

Nếu bạn tò mò và muốn tìm hiểu sâu hơn về phần mềm tuyệt vời này, bạn có thể tham khảo tài liệu ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html).

### Nhãn thời gian (timestamp) hoạt động như thế nào?

Bất kỳ ai cũng có thể sử dụng OpenTimestamps để gán nhãn thời gian cho một file và nhận được bằng chứng có thể xác minh về sự tồn tại của file đó. Nói cách khác, OpenTimestamps không cho bạn biết tệp được tạo ra khi nào, mà chỉ chứng minh rằng tệp đó đã tồn tại muộn nhất tại một thời điểm nhất định.

OpenTimestamps có thể cung cấp dịch vụ này miễn phí là nhờ vào việc lưu trữ hiệu quả một bằng chứng như vậy trong Blockchain Bitcoin. Nó sử dụng mã hash sha256 của file như một định danh duy nhất của file của bạn và xây dựng một cấu trúc cây Merkle với các hash khác của file được gửi từ người dùng khác và chỉ neo hash của cấu trúc cây Merkle trong một giao dịch OpReturn.

OpenTimestamps cung cấp dịch vụ này hoàn toàn miễn phí nhờ một phương pháp rất hiệu quả để lưu trữ bằng chứng trên blockchain Bitcoin. Hệ thống sử dụng mã băm SHA-256 của file làm mã định danh duy nhất và xây dựng một cây Merkle cùng với các mã băm của những file khác do người dùng gửi lên. Chỉ có hàm băm của cấu trúc cây Merkle được neo (anchored) trong giao dịch OpReturn.

Khi giao dịch này được đưa vào một khối, bất kỳ ai có tệp gốc và tệp `.ots` liên kết của nó đều có thể xác minh tính xác thực của dấu thời gian. Trong phần thứ hai của hướng dẫn này, chúng ta sẽ xem cách xác minh chứng chỉ kiểm tra ₿-CERT hoặc bất kỳ chứng nhận hoàn thành khóa học nào bằng cách sử dụng thiết bị đầu cuối và giao diện đồ họa thông qua trang web OpenTimestamps.

## Cách xác minh chứng chỉ hoặc bằng cấp Plan ₿ Academy ₿-CERT

### Bước 1. Tải xuống chứng chỉ hoặc bằng cấp của bạn

Đăng nhập vào bảng điều khiển cá nhân của bạn trên [Plan ₿ Academy](https://planb.academy/vi/certifications/certificates).

![image](./assets/login.webp)

Truy cập trang "Chứng chỉ" bằng cách nhấp vào menu bên trái và chọn chứng chỉ hoặc bằng cấp của bạn.

![image](./assets/credential.webp)

Tải xuống file zip.

![image](./assets/download.webp)

Giải nén nội dung bằng cách nhấp chuột phải vào file `.zip` và chọn "Extract". Bạn sẽ tìm thấy ba file khác nhau bên trong:

- File văn bản đã ký (ví dụ, certificate.txt)
- File Opentimestamp (OTS) (ví dụ, certificate.txt.ots)
- Chứng chỉ PDF (ví dụ, certificate.pdf)

### Bước 2: Xác minh chữ ký của file văn bản

Trước tiên, hãy mở cửa sổ terminal trong thư mục chứa các tệp bằng cách nhấp chuột phải vào cửa sổ thư mục và chọn "Open in Terminal". Sau đó làm theo hướng dẫn bên dưới:

1. Nhập khóa công khai (public key) PGP của Plan ₿ Academy với lệnh sau:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Nếu bạn đã nhập khóa PGP thành công, bạn sẽ thấy một thông báo tương tự như sau.

```
gpg: key 8F12D0C63B1A606E: public key "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

**LƯU Ý**: Nếu bạn thấy một khóa đã được xử lý nhưng không có khóa nào được nhập, có thể bạn đã nhập khóa này trước đó rồi, điều này hoàn toàn bình thường.

2. Xác minh chữ ký của chứng chỉ hoặc bằng cấp với lệnh sau:

```bash
gpg --verify certificate.txt
```

Lệnh này sẽ hiển thị thông tin chi tiết về chữ ký, bao gồm:

- Ai đã ký (Plan ₿ Academy)
- Khi nào nó được ký
- Liệu chữ ký có hợp lệ không

Dưới đây là một ví dụ về kết quả:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" [unknown]
```

Nếu bạn thấy một thông báo như "BAD signature", điều đó có nghĩa là file đã bị thay đổi.

### Bước 3: Xác minh Open Timestamp

#### Xác minh bằng giao diện

1. Truy cập trang web OpenTimestamps: https://opentimestamps.org/
2. Nhấn vào tab "Stamp & Verify".
3. Kéo thả file OTS (ví dụ, `certificate.txt.ots`) vào khu vực được chỉ định.
4. Kéo thả file đã được gán nhãn thời gian (ví dụ, `certificate.txt`) vào khu vực được chỉ định.
5. Trang web sẽ tự động xác minh "open timestamp" và hiển thị kết quả.

Nếu bạn thấy một thông báo như sau thì nhãn thời gian của bạn hợp lệ:
'
![cover](assets/opentimestamp_wegui_verified.webp)

#### Sử dụng CLI

**LƯU Ý: Quy trình này yêu cầu phải có một node Bitcoin cục bộ đang hoạt động.**

1. Cài đặt OpenTimestamps client từ [repository chính thức](https://github.com/opentimestamps/opentimestamps-client) bằng cách chạy lệnh sau:

```
pip install opentimestamps-client
```

2. Di chuyển đến thư mục chứa các file chứng chỉ đã giải nén.

3. Chạy lệnh sau để xác minh "open timestamp":

```
ots verify certificate.txt.ots
```

Lệnh này sẽ:

- Kiểm tra dấu thời gian so với blockchain của Bitcoin
- Hiển thị chính xác thời điểm file được gắn nhãn thời gian;
- Xác nhận tính xác thực của nhãn thời gian

#### Kết quả cuối cùng

Lưu ý rằng việc xác minh thành công nếu **cả hai** thông điệp sau được hiển thị:

1. Chữ ký GPG được đánh dấu là **"Good signature from Plan ₿ Academy"**
2. Quá trình xác minh OpenTimestamps hiển thị nhãn thời gian của khối Bitcoin cụ thể và thông báo **"Thành công! Khối Bitcoin [chiều cao khối] chứng thực dữ liệu tồn tại kể từ [nhãn thời gian]"**

Giờ đây, bạn đã biết cách Plan ₿ Academy cung cấp bằng chứng có thể xác minh được cho bất kỳ chứng chỉ ₿-CERT và chứng nhận hoàn thành khóa học nào, bạn có thể dễ dàng kiểm chứng tính xác thực của chúng.