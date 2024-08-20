---
term: ĐỊA CHỈ NHẬN
---

Thông tin được sử dụng để nhận bitcoin. Một địa chỉ thường được tạo ra bằng cách băm khóa công khai, sử dụng `SHA256` và `RIMPEMD160`, và thêm metadata vào đoạn mã này. Các khóa công khai được sử dụng để tạo ra một địa chỉ nhận là một phần của ví người dùng và do đó được phái sinh từ seed của họ. Ví dụ, địa chỉ SegWit được tạo thành từ các thông tin sau:
* Một HRP để chỉ định "bitcoin": `bc`;
* Một dấu phân cách: `1`;
* Phiên bản SegWit được sử dụng: `q` hoặc `p`;
* Payload: đoạn mã của khóa công khai (hoặc trực tiếp là khóa công khai trong trường hợp của Taproot);
* Checksum: một mã BCH.

Tuy nhiên, một địa chỉ nhận cũng có thể đại diện cho điều gì đó khác tùy thuộc vào mô hình script được sử dụng. Ví dụ, địa chỉ P2SH được tạo ra bằng cách sử dụng băm của script. Mặt khác, địa chỉ Taproot chứa trực tiếp khóa công khai đã được chỉnh sửa mà không cần băm.

Một địa chỉ nhận có thể được biểu diễn dưới dạng một chuỗi chữ và số hoặc dưới dạng mã QR. Mỗi địa chỉ có thể được sử dụng nhiều lần, nhưng đây là một thực hành được khuyến cáo mạnh mẽ không nên làm. Thực sự, để duy trì một mức độ riêng tư nhất định, người ta khuyến cáo chỉ sử dụng mỗi địa chỉ Bitcoin một lần. Một địa chỉ mới nên được tạo ra cho mỗi khoản thanh toán đến ví của một người. Một địa chỉ được mã hóa trong `Bech32` cho địa chỉ SegWit V0, trong `Bech32m` cho địa chỉ SegWit V1, và trong `Base58check` cho địa chỉ Legacy. Từ góc độ kỹ thuật, việc nhận bitcoin có nghĩa là sở hữu khóa riêng liên kết với một khóa công khai (và do đó là một địa chỉ). Khi ai đó nhận bitcoin, người gửi cập nhật ràng buộc hiện tại về việc chi tiêu của họ sao cho chỉ có người nhận mới có quyền lực này.

![](../../dictionnaire/assets/23.png)