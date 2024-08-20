---
term: BIP21
---

Đề xuất được viết bởi Nils Schneider và Matt Corallo, dựa trên BIP20 do Luke Dashjr viết, mà lại xuất phát từ một tài liệu khác do Nils Schneider viết. BIP21 định nghĩa cách mã hóa địa chỉ nhận tiền trong URIs (*Uniform Resource Identifier*) để thuận tiện cho việc thanh toán. Ví dụ, một Bitcoin URI theo BIP21 mà tôi sẽ yêu cầu dưới nhãn “*Pandul*” để gửi cho tôi 0.1 BTC sẽ trông như thế này:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Việc chuẩn hóa này cải thiện trải nghiệm người dùng của giao dịch Bitcoin bằng cách cho phép họ nhấp vào một liên kết hoặc quét mã QR để khởi tạo các tham số của họ. Tiêu chuẩn BIP21 hiện nay đã được áp dụng rộng rãi trong phần mềm ví Bitcoin.