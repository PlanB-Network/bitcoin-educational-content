---
name: Cập nhật BTCPay Server
description: Áp dụng bản cập nhật bảo mật cho phiên bản BTCPay Server của bạn và xoay vòng các thông tin xác thực quan trọng
---

![cover](assets/cover.webp)

Tự vận hành bộ xử lý thanh toán của riêng mình cũng có nghĩa là bạn tự làm đội ngũ bảo mật cho chính mình. Khi các maintainer của BTCPay Server phát hành một bản vá bảo mật, sẽ không có ai vá phiên bản của bạn thay bạn: việc cập nhật, xác minh và xoay vòng thông tin xác thực sau đó là những việc bạn phải tự thực hiện.

Hướng dẫn này đi qua toàn bộ quy trình, bất kể bạn đã triển khai BTCPay Server theo cách nào: kiểm tra phiên bản đang chạy, áp dụng bản cập nhật theo kiểu triển khai của bạn, xác minh rằng bản cập nhật đã thực sự được áp dụng, và xoay vòng các bí mật mà kẻ tấn công có thể đã thu thập trong thời gian phiên bản của bạn còn dễ bị tấn công.

Nếu bạn chưa triển khai BTCPay Server, hãy bắt đầu với hướng dẫn cài đặt:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Lỗ hổng nghiêm trọng tháng 8 năm 2026

⚠️ **Cảnh báo bảo mật nghiêm trọng (7 tháng 8 năm 2026):** một lỗ hổng nghiêm trọng ảnh hưởng đến BTCPay Server đang bị khai thác tích cực và có thể dẫn đến mất tiền. Hãy cập nhật ngay phiên bản của bạn lên **phiên bản 2.4.2** thông qua `Admin Dashboard > Server > Maintenance > Update`, sau đó kiểm tra xem chân trang có hiển thị `2.4.2` hay không. Nếu bạn không thể cập nhật ngay, hãy tắt BTCPay Server của bạn. Sau khi cập nhật, bạn cũng phải làm mới hoàn toàn các macaroons và tệp `macaroons.db` của mình, làm mới hoàn toàn chuỗi xác thực của bất kỳ backend Lightning nào khác, và nếu bạn đã tạo ví nóng on-chain bên trong BTCPay Server, hãy chuyển số tiền đó đi và tạo lại ví. Các nhà tích hợp cũng nên cập nhật NBXplorer lên phiên bản 2.6.10. Nguồn: [Ghi chú phát hành BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Phiên bản 2.4.2 được phát hành vào ngày 7 tháng 8 năm 2026. Ghi chú phát hành cho biết phiên bản này sửa một lỗ hổng nghiêm trọng vốn đã bị khai thác ngoài thực tế, được báo cáo bởi `brunoerg` và `benthecarman` thông qua nỗ lực Bitcoin Red Team. Cùng bản phát hành này cũng sửa lỗi vượt qua xác thực hai yếu tố TOTP thông qua xác thực Greenfield Basic, và mặc định vô hiệu hóa xác thực Greenfield Basic năm phút sau khi tạo tài khoản.

Có hai hệ quả từ việc "đang bị khai thác tích cực":

- **Cập nhật không phải là tùy chọn và không phải là việc để lên lịch cho tuần sau.** Một phiên bản chưa vá có thể truy cập từ internet phải được cập nhật hoặc tắt đi.
- **Chỉ cập nhật thôi là chưa đủ.** Nếu phiên bản của bạn đã bị xâm phạm trước khi bạn vá, kẻ tấn công có thể đã giữ bản sao thông tin xác thực Lightning của bạn và mọi vật liệu khóa ví nóng mà BTCPay Server đã tạo cho bạn. Những bí mật đó vẫn còn hiệu lực sau khi cập nhật cho đến khi bạn xoay vòng chúng. Phần xoay vòng bên dưới là phần mọi người thường bỏ qua, và đó chính là phần thực sự bảo vệ tiền của bạn.

## Bước 1 — Tìm xem bạn đang chạy phiên bản nào

Đăng nhập vào BTCPay Server của bạn và nhìn vào **chân trang của bất kỳ trang nào**: chuỗi phiên bản được hiển thị tại đó. Bạn cũng có thể mở `Admin Dashboard > Server > Maintenance`, nơi hiển thị phiên bản hiện tại và các nút điều khiển cập nhật.

Nếu phiên bản của bạn mở Greenfield API, `GET /api/v1/server/info` cũng trả về phiên bản.

Bất cứ phiên bản nào dưới `2.4.2` đều dễ bị tấn công.

## Bước 2 — Cập nhật

### Triển khai Docker tự lưu trữ (cài đặt tiêu chuẩn)

Phần này bao gồm triển khai Docker chính thức, tức cách bạn nhận được từ tài liệu BTCPay Server, từ trình khởi chạy một nhấp của LunaNode, và từ hầu hết các cài đặt VPS.

Cách đơn giản nhất là dùng giao diện web:

1. Vào `Admin Dashboard > Server > Maintenance`.
2. Nhấp **Update**.
3. Chờ các container được kéo về và khởi động lại. Giao diện sẽ không khả dụng trong vài phút.

Nếu không truy cập được giao diện web, hoặc bạn muốn xem log, hãy thực hiện qua SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Trên cài đặt mặc định, `$BTCPAY_BASE_DIRECTORY` là `/root`, nên thư mục là `/root/btcpayserver-docker`. Script kéo các image mới nhất, tạo lại các container, và in ra các phiên bản kết quả.

Triển khai Docker đi kèm NBXplorer cùng với BTCPay Server, nên một bản cập nhật tiêu chuẩn cũng đưa NBXplorer lên `2.6.10` được khuyến nghị. Nếu bạn chạy NBXplorer riêng — thường gặp với các nhà tích hợp và các stack tùy chỉnh — hãy cập nhật nó một cách rõ ràng.

### Umbrel

Mở dashboard Umbrel, vào **App Store**, tìm BTCPay Server và áp dụng bản cập nhật nếu có.

⚠️ **Quan trọng:** các gói trong app-store được đội ngũ Umbrel đóng gói lại và có thể chậm hơn upstream vài giờ hoặc vài ngày. Kiểm tra phiên bản trong chân trang BTCPay Server sau khi cập nhật. Nếu nó vẫn dưới `2.4.2`, hãy **dừng ứng dụng** từ dashboard Umbrel và chờ bản phát hành đã được đóng gói, thay vì để một phiên bản dễ bị tấn công tiếp tục chạy.

Hướng dẫn Umbrel riêng bao quát chính ứng dụng đó:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Cùng logic: cập nhật BTCPay Server từ marketplace của StartOS, sau đó xác minh phiên bản trong chân trang. Nếu phiên bản đã đóng gói vẫn chưa phải `2.4.2`, hãy dừng dịch vụ cho đến khi đúng phiên bản.

### Lưu trữ được quản lý và bên thứ ba

Nếu người khác vận hành phiên bản của bạn (nhà cung cấp lưu trữ, một hiệp hội, máy chủ của bạn bè), bạn vẫn cần xác nhận. Hãy hỏi người vận hành chuỗi phiên bản hiển thị trong chân trang, và hỏi rõ liệu việc xoay vòng thông tin xác thực sau cập nhật được mô tả bên dưới đã được thực hiện hay chưa. "Chúng tôi đã cập nhật" không phải là câu trả lời giống với "chúng tôi đã xoay vòng macaroons của bạn".

## Bước 3 — Xác minh bản cập nhật đã thực sự được áp dụng

Tải lại giao diện BTCPay Server và đọc phiên bản trong chân trang. Nó phải hiển thị `2.4.2` hoặc cao hơn.

Đừng dựa vào việc lệnh cập nhật thoát ra mà không có lỗi: trên các máy tài nguyên hạn chế, thao tác kéo image có thể thất bại âm thầm và để container trước đó tiếp tục chạy. Hãy đọc phiên bản, mọi lần.

## Bước 4 — Xoay vòng thông tin xác thực của bạn

Đây là bước biến "đã vá" thành "an toàn". Vì lỗ hổng đã bị khai thác trước khi bản sửa lỗi được phát hành, hãy coi mọi bí mật mà phiên bản của bạn nắm giữ là có khả năng đã bị kẻ tấn công biết.

### Lightning: LND

Tạo lại các macaroons **và** tệp `macaroons.db`. Chỉ xóa các tệp macaroon thôi là chưa đủ — LND dẫn xuất macaroons từ khóa gốc được lưu trong `macaroons.db`, nên kẻ tấn công đang giữ bản sao của một macaroon cũ vẫn giữ được quyền truy cập cho đến khi cơ sở dữ liệu đó được tạo lại.

Quy trình là: dừng LND, xóa `macaroons.db` và các tệp `*.macaroon` khỏi thư mục mạng (với mainnet, `data/chain/bitcoin/mainnet/` bên trong thư mục dữ liệu LND), sau đó khởi động lại và mở khóa LND, thao tác này sẽ tạo lại chúng. Hãy sao lưu thư mục trước, và ghép đôi lại mọi ứng dụng đã sử dụng các macaroons cũ — chính BTCPay Server, Zeus, Thunderhub, RTL, Alby, và bất kỳ script nào bạn đã viết.

Nếu bạn cũng mở LND ra internet, hãy đồng thời rà soát chứng chỉ TLS của nó và mọi thông tin xác thực trong `lnd.conf`.

### Lightning: các backend khác

Bất cứ thứ gì xác thực với node của bạn bằng một chuỗi đều phải nhận một chuỗi mới:

- **Core Lightning**: tạo lại rune hoặc thông tin xác thực truy cập được kết nối sử dụng.
- **Phoenixd**: xoay vòng mật khẩu HTTP.
- **LNbits và tương tự**: thu hồi và phát hành lại các khóa admin và khóa invoice.
- **Chuỗi kết nối node từ xa** được lưu trong cài đặt cửa hàng của BTCPay Server: viết lại chúng với các bí mật mới.

### Ví nóng on-chain được tạo bên trong BTCPay Server

Nếu bạn để BTCPay Server tạo ví on-chain cho bạn — thay vì kết nối ví phần cứng hoặc nhập một xpub có các khóa chưa từng chạm vào máy chủ — thì seed đó đã nằm trên máy.

Hãy coi nó là đã cháy:

1. Tạo một ví mới, lý tưởng nhất là với ví phần cứng để các khóa không bao giờ nằm trên máy chủ nữa.
2. Quét tiền từ ví cũ sang ví mới.
3. Thay thế scheme dẫn xuất trong cài đặt cửa hàng bằng ví mới.
4. Không bao giờ tái sử dụng seed cũ.

Các thiết lập watch-only (xpub hoặc ví phần cứng) không cần làm việc này: khóa riêng tư chưa bao giờ nằm trên máy chủ. Đây chính xác là lý do hướng dẫn cài đặt khuyến nghị chúng.

### Tài khoản BTCPay Server và khóa API

Nhân tiện:

- Thay đổi mật khẩu của mọi tài khoản người dùng trên phiên bản.
- Thu hồi và phát hành lại tất cả **khóa API** Greenfield.
- Đăng ký lại xác thực hai yếu tố, vì 2.4.2 sửa một lỗi vượt qua 2FA.
- Mở `Admin Dashboard > Server > Users` và kiểm tra rằng không có tài khoản bất ngờ nào tồn tại.
- Rà soát các **payouts**, **pull payments** và **refunds** gần đây để tìm các mục bạn không tạo.
- Rà soát webhooks và các bí mật của chúng.

## Bước 5 — Luôn nắm thông tin cho lần tiếp theo

Các bản phát hành bảo mật chỉ giúp được những người vận hành nghe được tin về chúng:

- Theo dõi [các bản phát hành BTCPay Server trên GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub có thể gửi email cho bạn mỗi khi có bản phát hành mới của một kho lưu trữ.
- Theo dõi các kênh thông báo của dự án và [blog chính thức](https://blog.btcpayserver.org/).
- Giữ phiên bản của bạn ở một phiên bản có thể cập nhật nhanh: bạn càng tụt lại xa, một bản cập nhật khẩn cấp càng trở nên đau đớn.

Tự lưu trữ mang lại cho bạn chủ quyền đối với các khoản thanh toán của mình. Chi phí của chủ quyền đó chính là điều này: đọc ghi chú phát hành và là người tự vá.
