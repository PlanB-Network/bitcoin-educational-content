---
term: P2SH-P2WPKH
---

P2SH-P2WPKH là viết tắt của *Pay to Script Hash - Pay to Witness Public Key Hash*. Đây là một mô hình script chuẩn được sử dụng để thiết lập điều kiện chi tiêu cho một UTXO, còn được biết đến với tên gọi "Nested SegWit".

P2SH-P2WPKH được giới thiệu cùng với việc triển khai SegWit vào tháng 8 năm 2017. Script này là một P2WPKH được bọc trong một P2SH. Nó khóa bitcoin dựa trên hash của một khóa công khai. Sự khác biệt so với P2WPKH cổ điển là script được bọc trong `redeemScript` của một P2SH cổ điển.

Script này được tạo ra khi SegWit được ra mắt nhằm mục đích tạo điều kiện thuận lợi cho việc áp dụng nó. Nó cho phép sử dụng tiêu chuẩn mới này, ngay cả với các dịch vụ hoặc ví chưa tương thích một cách bản địa với SegWit. Đây là một loại script chuyển tiếp hướng tới tiêu chuẩn mới. Ngày nay, việc sử dụng các loại script SegWit bọc này không còn quá phổ biến nữa, vì hầu hết các ví đã triển khai SegWit bản địa. Địa chỉ P2SH-P2WPKH được viết bằng mã hóa `Base58Check` và luôn bắt đầu bằng `3`, giống như bất kỳ địa chỉ P2SH nào.

> ► *`P2SH-P2WPKH` cũng đôi khi được gọi là `P2WPKH-nested-in-P2SH`.*