---
name: Bitfeed
description: Khám phá chuỗi giao thức Bitcoin chính.
---

![cover](assets/cover.webp)



Bitfeed là một nền tảng trực quan hóa lớp onchain của giao thức Bitcoin. Nền tảng này được khởi xướng bởi một trong những người đóng góp cho dự án Mempool.space và nổi bật chủ yếu nhờ giao diện tối giản và dễ sử dụng.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Trong hướng dẫn này, chúng ta sẽ xem xét công cụ này, cho phép bạn khám phá tất cả các giao dịch và khối trên mạng.



## Bắt đầu với Bitfeed



Bitfeed là một nền tảng tập trung vào ba điểm chính:





- Tư vấn Blockchain**,
- Tìm kiếm giao dịch**,
- Hiển thị mempool**.



### Tư vấn blockchain



Trên trang chủ Bitfeed, bạn chủ yếu sẽ tìm thấy:





- Thanh tìm kiếm: Phần này là điểm khởi đầu cho các truy vấn blockchain. Tại đây, bạn có thể tìm kiếm một khối cụ thể theo số hoặc hàm băm của nó. Bạn cũng có thể tìm kiếm các giao dịch cụ thể và địa chỉ Bitcoin để xác minh thông tin giao dịch nhất định trên mạng.



![searchBar](assets/fr/01.webp)



Ở góc trên bên trái, bạn có thể thấy giá hiện tại của bitcoin, ước tính bằng đô la Mỹ (USD).



![price](assets/fr/02.webp)



Thanh bên phải là menu nền tảng. Từ menu này, bạn có thể tùy chỉnh giao diện nền tảng theo ý thích, thêm hoặc xóa các mục và tùy chỉnh bộ lọc xem. Ví dụ: xem kích thước của từng khối theo giá trị hoặc theo trọng lượng tính bằng byte ảo (vByte).



![menu](assets/fr/03.webp)



Ở giữa trang là khối cuối cùng được khai thác, hiển thị tất cả các giao dịch có trong khối đó. Phần này cung cấp thông tin về dấu thời gian, tổng số bitcoin liên quan đến khối, kích thước khối tính bằng byte, số lượng giao dịch và tỷ lệ chi phí giao dịch trung bình trên mỗi byte ảo trong khối.



![block](assets/fr/04.webp)



Bạn có thể quay lại lịch sử kênh bằng cách tìm kiếm một khối cụ thể trên thanh tìm kiếm và xem theo tiêu chí của bạn.



Ví dụ, chúng ta muốn xem các giao dịch trong khối `879488`.



![bloc](assets/fr/05.webp)



Giao dịch đầu tiên của khối này đại diện cho giao dịch **coinbase** cho phép thợ đào khối này nhận được phần thưởng mining, chỉ có thể được sử dụng sau khi đào được 100 khối, bao gồm phí giao dịch và tiền thưởng khối. Giao dịch này cho phép phát hành bitcoin mới trên hệ thống.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Theo mặc định, các giao dịch trong một khối được biểu diễn theo hai tiêu chí:




- Kích thước có thể thay đổi giữa giá trị và trọng lượng (vByte);
- Màu sắc có thể thay đổi tùy theo độ tuổi và tỷ lệ phí giao dịch trên mỗi byte ảo.



![options](assets/fr/07.webp)



Do đó, chúng ta có thể kết luận rằng tất cả các giao dịch trong cùng một khối đều có cùng số lượng xác nhận trong blockchain. Các khối lớn nhất đại diện cho các giao dịch chứa số lượng bitcoin cao nhất.



Giải thích này được xác nhận thêm bằng tùy chọn menu **"Thông tin "**, cung cấp cho chúng ta thông tin về bản dịch màu sắc và kích thước của các giao dịch trong khối.



![infos](assets/fr/08.webp)



Bạn cũng có thể xem các giao dịch của một khối theo byte ảo và tỷ lệ phí. Chế độ xem này có thể khác với chế độ xem trước, vì giá trị bitcoin trong một giao dịch không xác định kích thước của giao dịch đó.



![visualisation](assets/fr/09.webp)



### Xem giao dịch



Bạn có thể tìm kiếm giao dịch bằng mã định danh của giao dịch đó trên thanh tìm kiếm. Bạn cũng có thể nhấp vào một khối để xem thông tin liên quan đến giao dịch đó.



Trong trường hợp này, hãy lấy giao dịch chiếm không gian lớn nhất trong khối `879488`.



![biggest](assets/fr/10.webp)



Bạn sẽ thấy giao dịch này có giá trị `42.989`, biểu thị sự khác biệt giữa khối cuối cùng được khai thác và khối chúng ta đã chọn. Những xác nhận này giúp tăng cường bảo mật cho mạng Bitcoin, bởi vì để sửa đổi giao dịch này một cách ác ý, kẻ tấn công sẽ cần phải sở hữu sức mạnh tính toán tương đương để viết lại toàn bộ chuỗi khối chính.



Quy mô của giao dịch này là `57.088 vByte`, chủ yếu là do số lượng lớn UTXO được sử dụng trong quá trình xây dựng (842 mục nhập). Đáng ngạc nhiên là tỷ lệ phí áp dụng vẫn tương đối thấp (chỉ 4 sats/vByte) so với mức trung bình của toàn khối là 5,82 sats/vByte.



Do đó, giao dịch chiếm nhiều dung lượng nhất không nhất thiết là giao dịch có tỷ lệ chi phí giao dịch cao nhất.



![transaction](assets/fr/11.webp)



Nếu bạn theo dõi thang đo trong menu **Thông tin**, giao dịch có tỷ lệ chi phí giao dịch cao nhất là giao dịch màu tím. Đây là giao dịch [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) với tỷ lệ chi phí giao dịch là `147,49 sats/vByte`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Hình ảnh hóa Mempool



Mempool là vị trí ảo nơi các giao dịch Bitcoin đang chờ được đưa vào một khối được nhóm lại với nhau. Bitfeed cho phép tham khảo [mempool](https://planb.academy/resources/glossary/mempool) của một số thợ đào Bitcoin, cung cấp khả năng theo dõi giao dịch đa dạng.



![mempool](assets/fr/13.webp)



Trong phần này, bạn có thể theo dõi tất cả các giao dịch hợp lệ và chưa được xác nhận trên chuỗi chính của mạng Bitcoin.



![unconfirmed](assets/fr/14.webp)



Giờ đây, bạn đã có hướng dẫn sử dụng nền tảng Bitfeed để phân tích các khối và giao dịch nhằm trực quan hóa thông tin có sẵn trên chuỗi chính của mạng lưới Bitcoin, đồng thời tận dụng giao diện tối giản, dễ sử dụng. Nếu bạn thích hướng dẫn này, chúng tôi khuyên bạn nên thực hiện bước tiếp theo: khám phá Lightning Network thông qua dự án Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017