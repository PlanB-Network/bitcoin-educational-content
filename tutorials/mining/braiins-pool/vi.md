---
name: Braiins Pool

description: Giới thiệu về Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, trước đây được biết đến với tên là Slush Pool, là hồ bơi đào Bitcoin đầu tiên trên thế giới. Được thành lập vào tháng 11 năm 2010, nó đã đào được khối đầu tiên vào ngày 16 tháng 12 năm 2010, khối 97834.

Tính đến tháng 5 năm 2024, Braiins Pool có sức mạnh tính toán là 13 EH/s, chiếm khoảng 1.8% tổng hashrate của Bitcoin. Nó đã đào được tổng cộng 1,307,188 bitcoin, tương đương khoảng 6% tổng số 21 triệu bitcoin sẽ tồn tại.

### Hệ Thống Thanh Toán

Kể từ cuối năm 2023, Braiins Pool đã thay đổi hệ thống thanh toán của mình sang hệ thống FPPS (Full Pay Per Share). Điều này có nghĩa là các thợ đào nhận được phần thưởng hàng ngày cho tất cả công việc của họ từ ngày hôm trước, ngay cả khi hồ bơi không tìm thấy khối. Điều này khác với hệ thống cũ, nơi các thợ đào chỉ nhận được phần thưởng khi hồ bơi tìm thấy khối.

**Đáng chú ý, [theo một tweet của Mononaut](https://x.com/mononautical/status/1777686545715089605) người phân tích Bitcoin TimeChain, rằng nhiều hồ bơi đào sử dụng hệ thống FPPS sẽ gửi bitcoin đã đào đến một địa chỉ của AntPool, điều này có nghĩa là AntPool kiểm soát hashrate của tất cả các hồ bơi này, khoảng 47% tổng hashrate Bitcoin toàn cầu. Đây là tin xấu cho sự phân quyền của mạng lưới.**

### Phí Hồ Bơi

Phí cho Braiins Pool là 2.5%, tuy nhiên, nếu bạn sử dụng BraiinsOS trên máy của mình thì phí sẽ là 0%

### Rút Tiền

**Rút Tiền Lightning**
Rút tiền Lightning cho phép bạn rút phần thưởng của mình mà không cần số tiền tối thiểu một lần mỗi ngày qua địa chỉ Lightning.
Để sử dụng phương thức này, bạn phải có ví tương thích với địa chỉ Lightning.

**Rút Tiền On-Chain**
Rút tiền On-Chain bị giới hạn với số tiền tối thiểu và có thể phải chịu phí.
Số tiền tối thiểu: 20,000 sats
Phí: 10,000 sats cho số tiền dưới 500,000 sats
Miễn phí cho số tiền trên 500,000 sats
Rút tiền có thể được kích hoạt theo khoảng thời gian hoặc theo số tiền.

## Tạo Tài Khoản

Để bắt đầu sử dụng Braiins Pool [truy cập trang web của họ](https://braiins.com/pool) và nhấp vào "SIGN UP" ở góc trên bên phải


![signup](assets/3.webp)

Nhập thông tin của bạn và xác nhận, sau đó bạn sẽ nhận được một email yêu cầu xác nhận địa chỉ của bạn. Xác nhận với liên kết trong email bạn nhận được và sau đó đăng nhập vào nền tảng

![signup](assets/4.webp)


## Thêm "worker"
Worker là máy đào mà bạn sẽ kết nối với hồ bơi. Để thêm máy đào mới, nhấp vào "Workers" trong menu bên trái.
![signup](assets/7.webp)

Sau đó nhấp vào nút màu tím "Connect Workers +".

Trong cửa sổ này, chọn khu vực địa lý của bạn.

Nếu máy đào bạn muốn kết nối sử dụng BraiinsOS, chọn giao thức "Stratum V2". Nếu không, chọn "Stratum V1".

![signup](assets/8.webp)

Bạn sẽ có thông tin để nhập vào trang web của máy đào của mình (tham khảo tài liệu của máy đào để biết nơi nhập thông tin này).

Tại đây, **"stratum+tcp://eu.stratum.braiins.com:3333"** là URL của hồ bơi.
**JimZap.workerName** là bộ nhận diện của bạn và tên của máy đào của bạn, nơi JimZap là bộ nhận diện và .workerName là tên của máy đào. Nếu bạn có nhiều máy đào, bạn có thể đặt cùng một tên cho chúng, trong trường hợp này sức mạnh tính toán của chúng sẽ được cộng dồn lại trên bảng điều khiển, hoặc đặt các tên khác nhau để theo dõi chúng một cách riêng lẻ.
Và mật khẩu luôn luôn là **"anything123"**

Khi bạn đã nhập thông tin này trên trang web của máy đào và nó bắt đầu đào, bạn sẽ thấy nó xuất hiện sau vài phút trên Bảng Điều Khiển Braiins Pool.

## Tổng Quan Bảng Điều Khiển

![signup](assets/9.webp)

Trên băng rôn phía trên, bạn có thể thấy tổng hashrate trung bình của tất cả máy đào của bạn qua 5 phút, 1 giờ, và 24 giờ. Và một bản tóm tắt số lượng máy đào trực tuyến hoặc ngoại tuyến.
Phía dưới, một biểu đồ cho phép bạn theo dõi sự phát triển của sức mạnh tính toán của bạn.

![signup](assets/10.webp)

Dưới biểu đồ này, bạn có một số thông tin về phần thưởng của bạn tính bằng sats.

**"Phần Thưởng Đào Hôm Nay"** Chỉ số sats bạn đã đào được hôm nay. Vào cuối ngày, giá trị này sẽ được đặt lại về 0 và sats sẽ được chuyển vào tài khoản của bạn.

**"Tổng Phần Thưởng Hôm Qua"** Số sats bạn đã đào được vào ngày hôm trước

**"Ước Lượng Lợi Nhuận (1 TH/s)"** Là ước lượng số sats bạn kiếm được trong một ngày với sức mạnh tính toán 1 TH/s. Ví dụ, nếu giá trị là 77 sats, và bạn có sức mạnh tính toán 10 TH/s liên tục trong suốt ngày, thì lý thuyết bạn sẽ kiếm được 77 x 10 = 770 sats mỗi ngày.

**"Phần Thưởng Tổng Cộng"** Tổng số sats bạn đã đào được với Braiins Pool

**"Chế Độ Phần Thưởng"** Mức phí áp dụng bởi pool

**"Ước Lượng Thời Gian Cho Lần Thanh Toán Tiếp Theo"** Ước lượng thời gian trước khi bạn có thể rút sats từ nền tảng. Tại đây, ước lượng không hiển thị gì vì việc đào mới chỉ diễn ra trong vài phút.

**"Số Dư Tài Khoản"** Số sats có sẵn trong tài khoản của bạn, mà sau đó bạn có thể rút.
## Thiết Lập Rút Tiền
Bạn có thể rút phần thưởng của mình bằng cách on-chain hoặc qua lightning với một địa chỉ.

Ở phía trên, nhấp vào "Funds". Theo mặc định, bạn có một "Tài Khoản Bitcoin". Bạn có thể tạo thêm để chia sẻ phần thưởng. Chúng tôi sẽ quay lại vấn đề này trong phần tiếp theo.

Bây giờ, nhấp vào "Set up".

![signup](assets/17.webp)

Trong cửa sổ mới này, bạn có thể chọn "Onchain payout".

Đặt tên cho ví này, cung cấp địa chỉ BTC, và chọn loại kích hoạt bạn muốn. "Threshold" có nghĩa là thanh toán sẽ được kích hoạt khi bạn đã tích lũy được một lượng BTC xác định, và với "Time interval", thanh toán sẽ được kích hoạt theo các khoảng thời gian định kỳ (ngày/tuần/tháng).

Lưu ý rằng số lượng tối thiểu là 0.0002 BTC và dưới 0.005 BTC, một phí 0.0001 BTC sẽ được áp dụng.

![signup](assets/18.webp)

Nếu bạn muốn sử dụng phương thức rút tiền qua Lightning, bạn sẽ cần một ví cung cấp địa chỉ Lightning. Ví dụ, bạn có thể sử dụng getAlby.

Nhấp vào phía trên cửa sổ "Lightning payout".

Nhập địa chỉ Lightning của bạn và đánh dấu vào ô "Tôi hiểu..." sau đó xác nhận.

Với phương thức rút tiền này, phần thưởng của bạn sẽ được gửi vào ví mỗi ngày.

![signup](assets/14.webp)
Sau khi bạn đã xác nhận các thiết lập thanh toán của mình, bạn sẽ nhận được một email xác nhận.
![signup](assets/15.webp)

## Chia Sẻ Phần Thưởng

Braiins Pool cũng cho phép bạn chia sẻ phần thưởng của mình qua nhiều ví khác nhau.

Để làm điều này, nhấp vào "Mining" ở phía trên sau đó nhấp vào "Settings" ở bên trái.

![signup](assets/19.webp)

Trên trang này, bạn sẽ có thể thêm "Financial Account" khác bằng cách nhấp vào "Add Another Financial Account" và phân phối phần thưởng của bạn theo % qua các tài khoản khác nhau mà bạn phải liên kết với một ví. Để liên kết một ví mới với Financial Account, tham khảo phần trước.