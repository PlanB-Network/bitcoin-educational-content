---
term: BTCPay Server

definition: Bộ xử lý thanh toán mã nguồn mở cho phép chấp nhận thanh toán bằng bitcoin mà không cần trung gian.
---

⚠️ **Cảnh báo bảo mật nghiêm trọng (7 tháng 8 năm 2026):** một lỗ hổng nghiêm trọng ảnh hưởng đến BTCPay Server đang bị khai thác tích cực và có thể dẫn đến mất tiền. Hãy cập nhật ngay lập tức phiên bản của bạn lên **version 2.4.2** thông qua `Admin Dashboard > Server > Maintenance > Update`, sau đó kiểm tra xem chân trang có hiển thị `2.4.2` hay không. Nếu bạn không thể cập nhật ngay, hãy tắt BTCPay Server của bạn. Sau khi cập nhật, bạn cũng phải làm mới hoàn toàn các macaroons và tệp `macaroons.db` của mình, làm mới hoàn toàn chuỗi xác thực của bất kỳ backend Lightning nào khác, và nếu bạn đã tạo ví nóng on-chain bên trong BTCPay Server, hãy chuyển số tiền đó đi và tạo lại ví. Các nhà tích hợp cũng nên cập nhật NBXplorer lên version 2.6.10. Nguồn: [Ghi chú phát hành BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server is an open-source payment processor that enables merchants and users to accept Bitcoin payments without relying on a third party for transaction processing. Launched in 2017, BTCPay Server provides a Bitcoin payment integration solution for e-commerce sites, with advanced features such as support for hardware wallets, billing and accounting tools, as well as compatibility with the Lightning Network. Its development was initiated by Nicolas Dorier, in response to the actions of Bitpay which, according to him, had misled its users by pushing them towards the adoption of SegWit2x, which the company mistakenly regarded as the "true" Bitcoin. This opposition was encapsulated in a now-famous tweet from Nicolas Dorier in August 2017:

> "_This is lies, my trust in you is broken, I will make you obsolete_".
