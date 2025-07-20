---
term: CISA
---

Từ viết tắt của "Cross-Input Signature Aggregation". Đây là đề xuất kỹ thuật được thiết kế để tối ưu hóa quy mô của các giao dịch Bitcoin bằng cách giảm số lượng chữ ký cần thiết để xác thực chúng.


Hiện tại, trên Bitcoin, mỗi đầu vào trong một giao dịch phải có một chữ ký riêng trước khi có thể được sử dụng. Điều này chứng minh rằng chủ sở hữu của UTXO đang được đề cập đã ủy quyền cho giao dịch. Với CISA, mục tiêu là kết hợp các chữ ký của tất cả các đầu vào của một giao dịch duy nhất thành một chữ ký duy nhất bao gồm tất cả các đầu vào. Điều này sẽ giúp giảm quy mô của các giao dịch có nhiều đầu vào và do đó cũng giảm chi phí của chúng. Điều này sẽ đặc biệt hữu ích cho những người thực hiện coinjoin hoặc hợp nhất, đồng thời cho phép xác nhận nhiều giao dịch hơn trên Bitcoin mà không cần thay đổi kích thước khối hoặc khoảng thời gian. CISA dựa trên giao thức Schnorr, cho phép tổng hợp tuyến tính các chữ ký. Điều này có nghĩa là một chữ ký duy nhất có thể chứng minh quyền sở hữu của một số khóa độc lập.


Tuy nhiên, việc triển khai CISA trên Bitcoin rất phức tạp vì nó đòi hỏi những thay đổi sâu sắc trong cách thức hoạt động của các tập lệnh. Hiện tại, việc xác minh tập lệnh trên Bitcoin được thực hiện theo từng đầu vào. Việc chuyển sang mô hình kiểm tra toàn bộ giao dịch cùng một lúc, như CISA đề xuất, không phải là một thay đổi đơn giản.