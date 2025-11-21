---
term: ẮC QUY
---

Trong ngữ cảnh của ngôn ngữ kịch bản được sử dụng để gắn các điều kiện chi tiêu vào Bitcoin UTXO, ngăn xếp là một cấu trúc dữ liệu LIFO (*Vào sau, Ra trước*) được sử dụng để lưu trữ Elements tạm thời trong quá trình thực thi kịch bản. Mỗi thao tác trong kịch bản đều thao tác các ngăn xếp này, trong đó Elements có thể được thêm vào (*đẩy*) hoặc xóa đi (*bật*). Các kịch bản sử dụng ngăn xếp để đánh giá các biểu thức, lưu trữ các biến tạm thời và quản lý các điều kiện.


Khi thực thi một tập lệnh Bitcoin, có thể sử dụng 2 ngăn xếp: ngăn xếp chính và ngăn xếp alt (alternative). Ngăn xếp chính được sử dụng cho phần lớn các hoạt động của tập lệnh. Trên ngăn xếp này, các hoạt động của tập lệnh thêm, xóa hoặc thao tác dữ liệu. Mặt khác, ngăn xếp thay thế được sử dụng để lưu trữ dữ liệu tạm thời trong quá trình thực thi tập lệnh. Các mã lệnh cụ thể, chẳng hạn như `OP_TOALTSTACK` và `OP_FROMALTSTACK`, cho phép bạn chuyển Elements từ ngăn xếp chính sang ngăn xếp thay thế và ngược lại.


Ví dụ, khi một giao dịch được xác thực, chữ ký và khóa công khai sẽ được đẩy lên ngăn xếp chính và được xử lý bởi các mã lệnh liên tiếp để xác minh rằng chữ ký khớp với khóa giao dịch và dữ liệu.