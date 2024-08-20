---
term: MỨC ĐỊNH MỤC TIÊU KHÓ KHĂN
---

Mức độ khó khăn, còn được biết đến với tên là mục tiêu khó khăn, là một tham số được sử dụng trong cơ chế đồng thuận bằng chứng công việc (Proof of Work, PoW) trên Bitcoin. Mục tiêu này đại diện cho một giá trị số học xác định độ khó cho các thợ mỏ để giải quyết một vấn đề mật mã cụ thể, được gọi là chứng minh công việc, khi tạo một khối mới trên blockchain.

Mục tiêu khó khăn là một số 256-bit (64 byte) có thể điều chỉnh, xác định giới hạn chấp nhận cho việc băm tiêu đề khối. Nói cách khác, để một khối được coi là hợp lệ, giá trị băm của tiêu đề khối với `SHA256d` (gấp đôi `SHA256`) phải thấp hơn hoặc bằng với mục tiêu khó khăn. Chứng minh công việc bao gồm việc thay đổi trường `nonce` của tiêu đề khối hoặc giao dịch coinbase cho đến khi giá trị băm thu được thấp hơn giá trị mục tiêu.

Mục tiêu này được điều chỉnh sau mỗi 2016 khối (khoảng mỗi hai tuần), trong một sự kiện được gọi là "điều chỉnh." Mức độ khó khăn được tính toán lại dựa trên thời gian để khai thác 2016 khối trước đó. Nếu tổng thời gian ít hơn hai tuần, độ khó tăng lên bằng cách điều chỉnh mục tiêu xuống dưới. Nếu tổng thời gian nhiều hơn hai tuần, độ khó giảm xuống bằng cách điều chỉnh mục tiêu lên trên. Mục tiêu là duy trì thời gian khai thác trung bình 10 phút mỗi khối. Thời gian giữa mỗi khối giúp ngăn chia rẽ mạng Bitcoin, dẫn đến lãng phí sức mạnh tính toán. Mục tiêu khó khăn được tìm thấy trong tiêu đề của mỗi khối, trong trường `nBits`. Vì trường này được giảm xuống còn 32 bit và mục tiêu thực sự là 256 bit, mục tiêu được nén vào một định dạng khoa học ít chính xác hơn.

![](../../dictionnaire/assets/34.png)

> ► *Mục tiêu khó khăn đôi khi cũng được gọi là "yếu tố khó khăn." Theo nghĩa rộng, nó cũng có thể được đề cập đến với mã hóa của nó trong tiêu đề khối với thuật ngữ "nBits."*