---
term: SWEEP TRANSACTION
---

Mô hình giao dịch hoặc mẫu giao dịch được sử dụng trong phân tích chuỗi để xác định bản chất của giao dịch. Mô hình này được đặc trưng bởi việc tiêu thụ một UTXO đơn lẻ làm đầu vào và sản xuất một UTXO đơn lẻ làm đầu ra. Sự giải thích của mô hình này là chúng ta đang chứng kiến một giao dịch tự chuyển. Người dùng đã chuyển bitcoin của họ cho chính họ, sang một địa chỉ khác mà họ sở hữu. Vì không có sự thay đổi nào trong giao dịch, nên rất khó có khả năng chúng ta đang xử lý một giao dịch thanh toán. Thực tế, khi một khoản thanh toán được thực hiện, gần như không thể cho người thanh toán có một UTXO chính xác khớp với số tiền mà người bán yêu cầu, bên cạnh phí giao dịch. Nói chung, người thanh toán do đó buộc phải tạo ra một đầu ra thay đổi. Chúng ta sau đó biết rằng người dùng quan sát được có khả năng vẫn giữ UTXO này. Trong bối cảnh của một phân tích chuỗi, nếu chúng ta biết UTXO được sử dụng làm đầu vào trong giao dịch thuộc về Alice, chúng ta có thể giả định rằng UTXO ở đầu ra cũng thuộc về cô ấy.

![](../../dictionnaire/assets/6.png)

> ► *Trong tiếng Pháp, "sweep transaction" có thể được dịch là "transaction de balayage".*