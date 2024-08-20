---
term: ROUND PAYMENT
---

Một phương pháp phân tích nội bộ cho phép đưa ra giả thuyết về bản chất của các đầu ra của một giao dịch trên Bitcoin dựa trên các số lượng tròn. Nói chung, khi đối mặt với một mô hình thanh toán đơn giản (1 đầu vào và 2 đầu ra), nếu một trong các đầu ra chi tiêu một số lượng tròn, thì nó đại diện cho khoản thanh toán. Bằng cách loại trừ, nếu một đầu ra đại diện cho khoản thanh toán, đầu ra còn lại đại diện cho tiền thối. Do đó, có thể hiểu rằng người dùng nhập giao dịch vẫn sở hữu đầu ra được xác định là tiền thối.

Cần lưu ý rằng phương pháp phân tích này không phải lúc nào cũng áp dụng được, vì phần lớn các khoản thanh toán vẫn được thực hiện bằng đơn vị tiền tệ fiat. Thực tế, khi một người bán hàng ở Pháp chấp nhận bitcoin, họ thường không hiển thị giá cố định bằng sats. Họ sẽ lựa chọn chuyển đổi giữa giá bằng euro và số lượng bitcoin cần thanh toán qua POS của họ (như BTCPay Server, chẳng hạn). Do đó, không nên có một số tròn trong đầu ra của giao dịch. Tuy nhiên, một nhà phân tích có thể cố gắng thực hiện việc chuyển đổi này bằng cách tính toán tỷ giá hối đoái hiệu lực khi giao dịch được phát sóng trên mạng. Nếu một ngày nào đó, bitcoin trở thành đơn vị tính toán ưa thích trong giao dịch của chúng ta, phương pháp phân tích này có thể trở nên hữu ích hơn nữa cho các phân tích.

![](../../dictionnaire/assets/11.png)