---
name: Dấu thời gian cho các chứng chỉ và bằng cấp của Mạng Plan ₿
description: Hiểu cách Mạng Plan ₿ cấp bằng chứng có thể xác minh cho chứng chỉ và bằng cấp của bạn
---

![cover](assets/cover.webp)

Nếu bạn đang đọc điều này, có khả năng cao là bạn đã nhận được một Chứng chỉ Bitcoin hoặc bằng tốt nghiệp cho một trong những khóa học bạn đã tham gia trên Mạng Plan ₿, vì vậy xin chúc mừng bạn đã đạt được thành tựu này!

Trong hướng dẫn này, chúng tôi sẽ xem xét cách Mạng Plan ₿ cấp bằng chứng có thể xác minh cho Chứng chỉ Bitcoin hoặc bất kỳ Bằng Tốt Nghiệp Khóa Học nào của bạn. Sau đó, trong phần thứ hai, chúng tôi sẽ xem cách xác minh tính xác thực của những bằng chứng này.

# Cơ chế chứng minh của Mạng Plan ₿

Tại Mạng Plan ₿, chúng tôi cung cấp cho bạn chứng chỉ và bằng cấp được chúng tôi ký kết mật mã và dấu thời gian trên Timechain (tức là Blockchain Bitcoin). Để thực hiện điều này, chúng tôi đã phải tìm ra một cơ chế chứng minh dựa trên 2 thao tác mật mã:

1. Một chữ ký GPG trên một tệp văn bản tổng hợp thành tựu của bạn
2. Dấu thời gian của tệp đã ký thông qua [opentimestamps](https://opentimestamps.org/).

Cơ bản thì thao tác đầu tiên cho phép bạn xác minh ai là người cấp chứng chỉ (hoặc bằng cấp) trong khi thao tác thứ hai cho phép bạn xác minh khi nào nó được cấp.
Chúng tôi tin rằng cơ chế chứng minh đơn giản này cho phép chúng tôi cấp chứng chỉ và bằng cấp với bằng chứng không thể chối cãi mà bất kỳ ai cũng có thể tự mình xác minh.

![image](./assets/proof-mechanism.webp)

Lưu ý rằng nhờ vào cơ chế chứng minh này, bất kỳ nỗ lực nào nhằm thay đổi ngay cả chi tiết nhỏ nhất của chứng chỉ hoặc bằng cấp của bạn sẽ tạo ra một mã hash sha256 hoàn toàn khác của tệp đã ký, điều này sẽ lập tức tiết lộ sự can thiệp bởi vì chữ ký và dấu thời gian sẽ không còn hợp lệ nữa. Hơn nữa, nếu ai đó cố gắng giả mạo một số chứng chỉ hoặc bằng cấp thay mặt cho Mạng Plan ₿, việc xác minh chữ ký đơn giản sẽ tiết lộ gian lận.

## Chữ ký GPG hoạt động như thế nào?

Chữ ký GPG được thu được với việc sử dụng phần mềm mã nguồn mở có tên GNU Private Guard. Phần mềm này cho phép bất kỳ ai dễ dàng tạo khóa riêng, ký và xác minh chữ ký cũng như mã hóa và giải mã tệp. Trong phạm vi của hướng dẫn này, biết rằng Mạng Plan ₿ sử dụng GPG để tạo khóa riêng/công khai của mình và để ký bất kỳ Chứng chỉ Bitcoin hoặc Bằng Tốt Nghiệp Khóa Học nào.

Mặt khác, nếu ai đó muốn xác minh tính xác thực của một tệp đã ký, họ có thể sử dụng GPG để nhập khóa công khai của người phát hành và xác minh. Trong phần thứ hai của hướng dẫn, chúng tôi sẽ xem cách làm điều này với một terminal.

Đối với những ai tò mò và muốn tìm hiểu thêm về phần mềm tuyệt vời này, bạn có thể tham khảo ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Dấu thời gian hoạt động như thế nào?

Bất kỳ ai cũng có thể sử dụng OpenTimestamps để dấu thời gian một tệp và nhận được bằng chứng có thể xác minh về sự tồn tại của tệp. Nói cách khác, nó không cung cấp cho bạn bằng chứng về thời điểm tệp được tạo ra mà là bằng chứng về sự tồn tại không muộn hơn một thời điểm nhất định.
OpenTimestamps có thể cung cấp dịch vụ này miễn phí nhờ một cách hiệu quả cao để lưu trữ bằng chứng như vậy trong Blockchain Bitcoin. Nó sử dụng mã hash sha256 của tệp như một định danh duy nhất của tệp của bạn và xây dựng một cây merkle với các hash khác của tệp được gửi từ người dùng khác và chỉ neo hash của cấu trúc cây Merkle trong một Giao Dịch OpReturn.
Sau khi giao dịch này được đưa vào một khối, bất kỳ ai có file gốc và file `.ots` liên quan đến nó có thể xác minh tính xác thực của việc đánh dấu thời gian. Trong phần thứ hai của hướng dẫn, chúng ta sẽ xem cách xác minh Chứng chỉ Bitcoin của bạn hoặc bất kỳ Bằng Tốt Nghiệp Khóa Học nào với một terminal và với giao diện đồ họa qua trang web của OpenTimestamps.

# Cách xác minh Chứng chỉ hoặc Bằng Tốt Nghiệp của Mạng Lưới Plan ₿

## Bước 1. Tải xuống Chứng chỉ hoặc Bằng Tốt Nghiệp của bạn

Đăng nhập vào bảng điều khiển PBN cá nhân của bạn.

![image](./assets/login.webp)

Truy cập trang Credentials bằng cách nhấp vào menu bên trái, và chọn phiên thi của bạn hoặc Bằng Tốt Nghiệp Khóa Học của bạn.

![image](./assets/credential.webp)

Tải xuống file zip.

![image](./assets/download.webp)

Giải nén nội dung bằng cách nhấp chuột phải vào file `.zip` và chọn "Extract". Bạn sẽ tìm thấy ba file khác nhau bên trong:

- File văn bản đã ký (ví dụ, certificate.txt)
- File Open timestamp (OTS) (ví dụ, certificate.txt.ots)
- Chứng chỉ PDF (ví dụ, certificate.pdf)

## Bước 2: Xác minh Chữ ký của File Văn bản

Đầu tiên mở một terminal trong thư mục chứa các file (nhấp chuột phải vào cửa sổ thư mục và nhấp vào "Open in Terminal"). Sau đó làm theo các hướng dẫn dưới đây

1. Nhập khóa công khai PGP của Mạng Lưới Plan ₿ với lệnh sau:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Bạn nên thấy một thông báo như sau nếu bạn đã nhập khóa PGP thành công

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

LƯU Ý: nếu bạn thấy rằng 1 khóa đã được xử lý và 0 được nhập, có khả năng bạn đã nhập cùng một khóa trước đó và điều đó là ổn.

2. Xác minh chữ ký của chứng chỉ hoặc bằng tốt nghiệp với lệnh sau:

```bash
gpg --verify certificate.txt
```

Lệnh này sẽ hiển thị cho bạn các chi tiết về chữ ký, bao gồm:

- Ai đã ký nó (Mạng Lưới Plan ₿)
- Khi nào nó được ký
- Liệu chữ ký có hợp lệ không

Đây là một ví dụ về kết quả:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

Nếu bạn thấy một thông báo như "BAD signature", điều đó có nghĩa là file đã bị thay đổi.

## Bước 3: Xác minh Open Timestamp

### Xác minh qua Giao diện Đồ họa

1. Truy cập trang web OpenTimestamps: https://opentimestamps.org/
2. Nhấp vào tab "Stamp & Verify".
3. Kéo và thả file OTS (ví dụ, `certificate.txt.ots`) vào khu vực được chỉ định.
4. Kéo và thả file đã được đánh dấu thời gian (ví dụ, `certificate.txt`) vào khu vực được chỉ định.
5. Trang web sẽ tự động xác minh open timestamp và hiển thị kết quả.

Nếu bạn thấy một thông báo như sau thì timestamp của bạn là hợp lệ:
![cover](assets/opentimestamp_wegui_verified.webp)

### Phương pháp CLI

LƯU Ý: quy trình này **sẽ yêu cầu một node Bitcoin địa phương đang chạy**

1. Cài đặt OpenTimestamps client từ kho chính thức: https://github.com/opentimestamps/opentimestamps-client bằng cách chạy lệnh sau:

```
pip install opentimestamps-client
```

2. Di chuyển đến thư mục chứa các tệp chứng chỉ đã giải nén.

3. Chạy lệnh sau để xác minh dấu thời gian mở:

```
ots verify certificate.txt.ots
```

Lệnh này sẽ:

- Kiểm tra dấu thời gian so với blockchain của Bitcoin
- Hiển thị cho bạn thời điểm chính xác tệp được đánh dấu thời gian
- Xác nhận tính xác thực của dấu thời gian

### Kết quả cuối cùng

Lưu ý rằng việc xác minh thành công nếu **cả hai** thông điệp sau được hiển thị:

1. Chữ ký GPG được báo cáo là **"Chữ ký tốt từ Plan ₿ Network"**
2. Xác minh OpenTimestamps hiển thị một dấu thời gian khối Bitcoin cụ thể và báo cáo **"Thành công! Khối Bitcoin [blockheight] chứng thực dữ liệu tồn tại kể từ [timestamp]"**

Giờ đây, bạn đã biết cách Plan ₿ Network phát hành bằng chứng có thể xác minh cho bất kỳ Chứng chỉ Bitcoin và Bằng tốt nghiệp Khóa học nào, bạn có thể dễ dàng xác minh tính toàn vẹn của nó.

