---
term: CHANGE
---

Trong bối cảnh của các giao dịch Bitcoin, thuật ngữ này ám chỉ UTXO được tạo ra với số dư còn lại sau khi thanh toán thực tế đã được thực hiện. Khi sử dụng UTXOs với số lượng bitcoin lớn hơn số lượng cần thiết cho thanh toán thực tế và phí giao dịch, số dư thừa này là một UTXO được trả về một địa chỉ nội bộ của ví, gọi là địa chỉ tiền thối. Tiền thối đại diện cho UTXO này. Ví dụ, nếu bạn muốn thanh toán cho một chiếc bánh mì baguette có giá `4,000 sats` bằng một UTXO của `10,000 sats`, bạn sẽ tạo ra một tiền thối là `6,000 sats` trong giao dịch của mình (nếu chúng ta không tính đến phí giao dịch).

![](../../dictionnaire/assets/16.png)

> ► *Mặc dù hiếm khi được sử dụng, chúng ta cũng có thể gọi nó là "tiền tệ" (tiền thối được trả lại) để nói về tiền thối.*