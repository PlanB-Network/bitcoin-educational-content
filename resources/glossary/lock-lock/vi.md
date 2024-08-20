---
term: LOCK (.LOCK)
---

Tệp được sử dụng trong Bitcoin Core để khóa thư mục dữ liệu. Nó được tạo ra khi bitcoind hoặc Bitcoin-qt khởi động nhằm ngăn chặn việc nhiều phiên bản của phần mềm truy cập cùng một thư mục dữ liệu một cách đồng thời. Mục tiêu là để ngăn chặn xung đột và hỏng dữ liệu. Nếu phần mềm dừng hoạt động một cách bất ngờ, tệp .lock có thể vẫn còn và phải được xóa thủ công trước khi khởi động lại Bitcoin Core.