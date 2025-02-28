---
name: Watch Tower
description: Hiểu và sử dụng tháp canh
---

## Tháp canh hoạt động như thế nào?

Là một phần không thể thiếu của hệ sinh thái Lightning Network, tháp canh mang lại một mức độ bảo vệ thêm cho các kênh lightning của người dùng. Trách nhiệm chính của nó là giám sát sức khỏe của các kênh và can thiệp nếu một bên trong kênh cố gắng gian lận với bên kia.

Vậy tháp canh làm thế nào để xác định nếu một kênh đã bị xâm phạm? Tháp canh nhận được thông tin cần thiết từ khách hàng, một trong các bên của kênh, để có thể xác định và phản ứng với bất kỳ sự vi phạm nào. Thông tin thường bao gồm chi tiết giao dịch mới nhất, tình trạng kênh hiện tại, và thông tin cần thiết để tạo ra các giao dịch phạt. Trước khi truyền dữ liệu cho tháp canh, khách hàng có thể mã hóa nó để bảo vệ sự riêng tư và bí mật. Điều này ngăn chặn tháp canh từ việc giải mã dữ liệu đã mã hóa trừ khi một sự vi phạm thực sự đã xảy ra, ngay cả khi nó nhận được dữ liệu. Hệ thống mã hóa này bảo vệ sự riêng tư của khách hàng và ngăn chặn tháp canh truy cập vào dữ liệu riêng tư mà không được phép.

## Cách thiết lập Eye of Satoshi của riêng bạn và bắt đầu đóng góp

Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) là một tháp canh Lightning không giữ tiền, tuân thủ [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Nó có hai thành phần chính:

1. teos: bao gồm một CLI và chức năng cốt lõi phía máy chủ của tháp. Hai tệp nhị phân—teosd và teos-cli—sẽ được tạo ra khi crate này được xây dựng.

2. teos-common: Bao gồm chức năng chung phía máy chủ và phía khách hàng (hữu ích cho việc tạo một khách hàng).

Để chạy tháp thành công, bạn sẽ cần bitcoind đang chạy trước khi chạy tháp với lệnh teosd. Trước khi chạy cả hai lệnh này bạn cần thiết lập tệp bitcoin.conf của mình. Dưới đây là các bước về cách làm điều này:-

1. Cài đặt bitcoin core từ nguồn hoặc tải xuống. Sau khi tải xuống, đặt tệp bitcoin.conf vào thư mục người dùng Bitcoin core. Kiểm tra liên kết này để biết thêm thông tin về nơi đặt tệp vì nó phụ thuộc vào hệ điều hành bạn đang sử dụng.

2. Sau khi xác định nơi cần tạo tệp, thêm các tùy chọn này:-

'''
#RPC
server=1
rpcuser=<tên-người-dùng-của-bạn>
rpcpassword=<mật-khẩu-của-bạn>

#chain
regtest=1
'''

- server: Dành cho các yêu cầu RPC
- rpcuser và rpcpassword: Các khách hàng RPC có thể xác thực với máy chủ
- regtest: Không bắt buộc nhưng hữu ích nếu bạn đang lên kế hoạch cho phát triển.

rpcuser và rpcpassword cần được bạn chọn. Chúng phải được viết không có dấu ngoặc kép. Ví dụ:-

'''
rpcuser=aniketh
rpcpassword=strongpassword
'''

Bây giờ, nếu bạn chạy bitcoind nó sẽ bắt đầu chạy node.

1. Đối với phần tháp, trước tiên, bạn phải cài đặt teos từ nguồn. Theo dõi hướng dẫn được đưa ra trong liên kết này.

2. Sau khi thành công cài đặt teos trong hệ thống của bạn và chạy các bài kiểm tra, bạn có thể tiếp tục với bước cuối cùng là thiết lập tệp teos.toml trong thư mục người dùng teos. Tệp cần được đặt trong một thư mục gọi là .teos (chú ý dấu chấm) dưới thư mục home của bạn. Đó là, ví dụ, /home/<tên-người-dùng-của-bạn>/.teos cho Linux. Một khi bạn đã tìm được nơi, tạo một tệp teos.toml và thiết lập các tùy chọn này tương ứng với những thứ chúng ta đã thay đổi trên bitcoind.
#bitcoindbtc_network = "regtest"
btc_rpc_user = "<tên-người-dùng-của-bạn>"
btc_rpc_password = "<mật-khẩu-của-bạn>"

Lưu ý rằng ở đây tên người dùng và mật khẩu cần được viết trong dấu ngoặc kép, tức là, cho cùng một ví dụ như trước:

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
'''

Sau khi bạn đã thực hiện điều đó, bạn sẽ sẵn sàng để chạy tháp. Vì chúng ta đang chạy trên regtest, có khả năng là sẽ không có khối nào được khai thác trong mạng thử nghiệm bitcoin lần đầu tiên tháp kết nối với nó (nếu có, chắc chắn là có điều gì đó không ổn). Tháp xây dựng một bộ nhớ đệm nội bộ của 100 khối mới nhất từ bitcoind, vì vậy khi chạy lần đầu tiên chúng ta có thể nhận được lỗi sau:

> ERROR [teosd] Không đủ khối để bắt đầu tháp (yêu cầu: 100). Hãy khai thác ít nhất 100 khối nữa

Vì chúng ta đang chạy trên regtest, chúng ta có thể khai thác khối bằng cách sử dụng lệnh RPC, mà không cần chờ thời gian trung bình 10 phút mà chúng ta thường thấy ở các mạng khác (như mainnet hoặc testnet). Kiểm tra trợ giúp của bitcoin-cli và tìm cách khai thác khối. Nếu bạn cần một số trợ giúp, bạn có thể tham khảo bài viết này.

![hình ảnh](assets/2.webp)

Đó là tất cả, bạn đã chạy thành công tháp. Xin chúc mừng. 🎉