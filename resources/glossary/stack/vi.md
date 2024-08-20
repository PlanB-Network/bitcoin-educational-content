---
term: STACK
---

Trong bối cảnh của ngôn ngữ kịch bản được sử dụng để áp dụng điều kiện chi tiêu trên Bitcoin UTXOs, stack là một cấu trúc dữ liệu "LIFO" (*Last In, First Out* - Vào sau, ra trước) phục vụ để lưu trữ tạm thời các phần tử trong quá trình thực thi một script. Mỗi thao tác trong script thao tác với các stack này, nơi các phần tử có thể được thêm vào (*push*) hoặc loại bỏ (*pop*). Script sử dụng stack để đánh giá biểu thức, lưu trữ biến tạm thời và quản lý điều kiện.

Trong quá trình thực thi một script Bitcoin, có thể sử dụng 2 stack: stack chính và stack phụ (alternative). Stack chính được sử dụng cho phần lớn các thao tác của script. Chính trên stack này mà các thao tác script thêm, loại bỏ, hoặc thao tác dữ liệu. Ngược lại, stack phụ phục vụ để lưu trữ tạm thời dữ liệu trong quá trình thực thi script. Các opcode cụ thể, như `OP_TOALTSTACK` và `OP_FROMALTSTACK`, cho phép chuyển các phần tử từ stack chính sang stack phụ và ngược lại.

Ví dụ, trong quá trình xác thực một giao dịch, chữ ký và khóa công khai được đẩy vào stack chính và được xử lý bởi các opcode liên tiếp để xác minh rằng chữ ký khớp với khóa và dữ liệu giao dịch.

> ► *Trong tiếng Anh, bản dịch của « pile » là « stack ». Thuật ngữ tiếng Anh thường được sử dụng ngay cả trong các cuộc thảo luận kỹ thuật bằng tiếng Pháp.*