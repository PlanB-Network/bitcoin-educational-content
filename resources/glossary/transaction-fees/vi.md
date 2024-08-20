---
term: PHÍ GIAO DỊCH
---

Phí giao dịch đại diện cho một khoản tiền nhằm bồi thường cho các thợ đào vì sự tham gia của họ vào cơ chế chứng minh công việc (proof of work). Những phí này khuyến khích thợ đào bao gồm các giao dịch vào trong các khối họ tạo ra. Chúng xuất phát từ sự chênh lệch giữa tổng số lượng đầu vào và tổng số lượng đầu ra trong một giao dịch:

```text
phí = đầu vào - đầu ra
```

Chúng được biểu thị bằng `sats/vBytes`, nghĩa là phí không phụ thuộc vào số lượng bitcoin được gửi, mà phụ thuộc vào trọng lượng của giao dịch. Người gửi giao dịch có thể tự do chọn lựa phí này và quyết định tốc độ giao dịch được bao gồm trong một khối thông qua một cơ chế đấu giá. Ví dụ, giả sử tôi thực hiện một giao dịch với một đầu vào là `100,000 sats`, một đầu ra là `40,000 sats`, và một đầu ra khác là `58,500 sats`. Tổng số đầu ra là `98,500 sats`. Phí được phân bổ cho giao dịch này là `1,500 sats`. Thợ đào bao gồm giao dịch của tôi có thể tạo ra `1,500 sats` trong giao dịch coinbase của họ đổi lại cho `1,500 sats` mà tôi không thu hồi được trong các đầu ra của mình.

Các giao dịch có phí cao hơn, tương đối với kích thước của chúng, được xem là ưu tiên bởi các thợ đào, có thể tăng tốc quá trình xác nhận. Ngược lại, các giao dịch có phí thấp hơn có thể bị trì hoãn trong những thời kỳ tắc nghẽn cao. Đáng chú ý là phí giao dịch Bitcoin khác biệt với phần thưởng khối, đó là một khuyến khích bổ sung cho các thợ đào. Phần thưởng khối bao gồm các bitcoin mới được tạo ra với mỗi khối được khai thác (phần thưởng khối), cũng như phí giao dịch được thu thập. Trong khi phần thưởng khối giảm dần theo thời gian do giới hạn tổng cung của bitcoin, phí giao dịch sẽ tiếp tục đóng một vai trò quan trọng trong việc khuyến khích các thợ đào tham gia.

Ở cấp độ giao thức, không có gì ngăn cản người dùng bao gồm các giao dịch không có phí vào một khối. Trong thực tế, loại giao dịch không có phí này là ngoại lệ. Theo mặc định, các nút Bitcoin không chuyển tiếp các giao dịch có phí thấp hơn `1 sat/vBytes`. Nếu một số giao dịch không có phí đã được thông qua, đó là vì chúng đã được tích hợp trực tiếp bởi thợ đào chiến thắng, mà không cần đi qua mạng lưới các nút. Ví dụ, giao dịch sau đây không bao gồm phí:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Trong ví dụ cụ thể này, đó là một giao dịch được khởi xướng bởi giám đốc của hồ bơi khai thác F2Pool. Với tư cách là một người dùng thông thường, giới hạn dưới hiện tại do đó là `1 sat/vBytes`.
Cũng cần phải xem xét các giới hạn của việc loại bỏ. Trong những thời kỳ tắc nghẽn cao, các mempool của nút sẽ loại bỏ các giao dịch đang chờ dưới một ngưỡng nhất định, để tôn trọng giới hạn RAM được phân bổ. Giới hạn này được người dùng tự do chọn lựa, nhưng nhiều người giữ giá trị mặc định của Bitcoin Core là 300 MB. Nó có thể được chỉnh sửa trong tệp `bitcoin.conf` với tham số `maxmempool`.
> ► *Trong tiếng Anh, chúng ta gọi nó là "transaction fees".*