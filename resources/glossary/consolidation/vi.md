---
term: CONSOLIDATION
---

Một giao dịch cụ thể trong đó nhiều UTXO nhỏ được hợp nhất thành một đầu vào để tạo ra một UTXO lớn hơn làm đầu ra. Đây là một giao dịch được thực hiện cho ví của chính mình. Mục tiêu của việc hợp nhất là tận dụng các khoảng thời gian khi phí trên mạng Bitcoin thấp để hợp nhất nhiều UTXO nhỏ thành một lớn hơn về giá trị. Như vậy, nó dự đoán các chi phí bắt buộc trong trường hợp phí tăng lên, cho phép tiết kiệm phí giao dịch trong tương lai.

Thực sự, các giao dịch với nhiều đầu vào nặng hơn và do đó, đắt hơn. Ngoài việc tiết kiệm được trên phí giao dịch, việc hợp nhất cũng là một hình thức lập kế hoạch dài hạn. Nếu ví của bạn chứa các UTXO rất nhỏ, những UTXO này có thể trở nên không sử dụng được nếu mạng Bitcoin bước vào một giai đoạn phí cao kéo dài. Ví dụ, nếu bạn cần chi tiêu một UTXO 10,000 sats nhưng phí khai thác tối thiểu lên đến 15,000 sats, chi phí sẽ vượt quá giá trị của chính UTXO. Những UTXO nhỏ này sau đó trở nên không hợp lý về mặt kinh tế để sử dụng và vẫn không thể sử dụng miễn là phí không giảm. Những UTXO này thường được gọi là "dust." Bằng cách thường xuyên hợp nhất các UTXO nhỏ của bạn, bạn giảm bớt rủi ro này liên quan đến việc tăng phí.

Tuy nhiên, quan trọng là phải lưu ý rằng các giao dịch hợp nhất có thể được nhận biết trong quá trình phân tích chuỗi. Một giao dịch như vậy chỉ ra một Heuristic Sở Hữu Đầu Vào Chung (Common Input Ownership Heuristic - CIOH), có nghĩa là các đầu vào của giao dịch hợp nhất thuộc về một thực thể duy nhất. Điều này có thể có hậu quả về mặt quyền riêng tư cho người dùng.

![](../../dictionnaire/assets/7.png)