---
term: MÔ TẢ KỊCH BẢN ĐẦU RA
---

Mô tả kịch bản đầu ra, hay đơn giản là mô tả, là những biểu thức có cấu trúc mô tả đầy đủ một kịch bản đầu ra (`scriptPubKey`) và cung cấp tất cả thông tin cần thiết để theo dõi các giao dịch đến hoặc từ một kịch bản cụ thể. Những mô tả này hỗ trợ quản lý khóa trong ví HD thông qua một mô tả tiêu chuẩn về cấu trúc và loại địa chỉ sử dụng.

Điểm quan tâm chính của mô tả nằm ở khả năng chứa đựng tất cả thông tin thiết yếu để khôi phục một ví trong một chuỗi duy nhất (bổ sung cho cụm từ khôi phục). Bằng cách lưu một mô tả cùng với các cụm từ ghi nhớ tương ứng, có thể khôi phục không chỉ các khóa riêng tư mà còn cả cấu trúc chính xác của ví và các tham số kịch bản liên quan. Thực tế, việc khôi phục một ví đòi hỏi không chỉ kiến thức về hạt giống ban đầu mà còn cả các chỉ số cụ thể cho việc phái sinh các cặp khóa con, cũng như `xpub` của mỗi yếu tố trong trường hợp của một ví multisig. Trước đây, người ta cho rằng thông tin này được biết một cách ngầm định bởi tất cả mọi người. Tuy nhiên, với sự đa dạng hóa của các kịch bản và sự xuất hiện của các cấu hình phức tạp hơn, thông tin này có thể trở nên khó để suy luận, do đó biến những dữ liệu này thành thông tin riêng tư và khó bị bẻ khóa. Việc sử dụng mô tả đơn giản hóa đáng kể quy trình: chỉ cần biết cụm từ khôi phục và mô tả tương ứng để khôi phục mọi thứ một cách đáng tin cậy và an toàn.

Một mô tả bao gồm nhiều yếu tố:
* Các hàm kịch bản như `pk` (Thanh toán cho PubKey), `pkh` (Thanh toán cho PubKey-Hash), `wpkh` (Thanh toán cho Witness-PubKey-Hash), `sh` (Thanh toán cho Script-Hash), `wsh` (Thanh toán cho Witness-Script-Hash), `tr` (Thanh toán cho Taproot), `multi` (Chữ ký đa), và `sortedmulti` (Chữ ký đa với khóa được sắp xếp);
* Các đường dẫn phái sinh, ví dụ, `[d34db33f/44h/0h/0h]` chỉ đường dẫn phái sinh và dấu vân tay khóa chính cụ thể;
* Khóa ở các định dạng khác nhau như khóa công khai dạng thập lục phân hoặc khóa công khai mở rộng (`xpub`);
* Một mã kiểm tra, đi trước bởi một mã băm, để xác minh tính toàn vẹn của mô tả.

Ví dụ, một mô tả cho ví P2WPKH có thể trông như sau:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
Trong mô tả này, hàm phái sinh `wpkh` chỉ loại kịch bản Thanh toán cho Witness-Public-Key-Hash. Nó được theo sau bởi đường dẫn phái sinh chứa:
* `cdeab12f`: dấu vân tay của khóa chính;
* `84h`: chỉ mục đích sử dụng của BIP84, dành cho địa chỉ SegWit v0;
* `0h`: chỉ ra rằng đó là tiền tệ BTC trên mainnet;
* `0h`: chỉ số tài khoản cụ thể được sử dụng trong ví.

Mô tả cũng bao gồm khóa công khai mở rộng được sử dụng trong ví này:

```text
Tiếp theo, ký hiệu `/<0;1>/*` chỉ ra rằng bộ mô tả có thể tạo ra địa chỉ từ chuỗi bên ngoài (`0`) và chuỗi bên trong (`1`), với một ký tự đại diện (`*`) cho phép việc phát sinh tuần tự nhiều địa chỉ theo cách có thể cấu hình, tương tự như quản lý "khoảng trống giới hạn" trên phần mềm ví truyền thống.

Cuối cùng, `#jy0l7nr4` đại diện cho mã kiểm tra để xác minh tính toàn vẹn của bộ mô tả.