---
term: KHÓA MỞ RỘNG
---

Một chuỗi ký tự kết hợp một khóa (công khai hoặc riêng tư), mã chuỗi liên kết của nó, và một loạt metadata. Một khóa mở rộng tổng hợp tất cả các yếu tố cần thiết để tạo ra các khóa con vào một định danh duy nhất. Chúng được sử dụng trong ví xác định và phân cấp và có thể thuộc về hai loại: khóa công khai mở rộng (được sử dụng để tạo ra các khóa công khai con) hoặc khóa riêng tư mở rộng (được sử dụng để tạo ra cả khóa riêng tư và công khai con). Một khóa mở rộng bao gồm nhiều phần dữ liệu khác nhau, được mô tả trong BIP32, theo thứ tự:
* Tiền tố: `prv` và `pub` là HRP (Human Readable Part) chỉ ra rằng đó là khóa riêng tư mở rộng (`prv`) hay khóa công khai mở rộng (`pub`). Chữ cái đầu tiên của tiền tố chỉ phiên bản của khóa mở rộng: `x` cho Legacy hoặc SegWit V1 trên Bitcoin, `t` cho Legacy hoặc SegWit V1 trên Bitcoin Testnet, `y` cho Nested SegWit trên Bitcoin, `u` cho Nested SegWit trên Bitcoin Testnet, `z` cho SegWit V0 trên Bitcoin, `v` cho SegWit V0 trên Bitcoin Testnet.
* Độ sâu, chỉ số lần dẫn xuất từ khóa chính để đạt được khóa mở rộng;
* Dấu vân tay của cha mẹ. Điều này đại diện cho 4 byte đầu tiên của `HASH160` của khóa công khai của cha mẹ;
* Chỉ số. Đây là số của cặp trong số các anh chị em từ đó khóa mở rộng được dẫn xuất;
* Mã chuỗi;
* Một byte đệm nếu đó là một khóa riêng tư `0x00`;
* Khóa riêng tư hoặc công khai;
* Một mã kiểm tra. Nó đại diện cho 4 byte đầu tiên của `HASH256` của phần còn lại của khóa mở rộng.

Trên thực tế, khóa công khai mở rộng được sử dụng để tạo địa chỉ nhận và quan sát các giao dịch của một tài khoản mà không tiết lộ các khóa riêng tư liên quan. Điều này có thể cho phép, ví dụ, tạo ra một ví chỉ xem được gọi là "watch-only" wallet. Tuy nhiên, điều quan trọng cần lưu ý là khóa công khai mở rộng là thông tin nhạy cảm đối với quyền riêng tư của người dùng, vì việc tiết lộ nó có thể cho phép bên thứ ba truy vết giao dịch và xem số dư của tài khoản liên quan.