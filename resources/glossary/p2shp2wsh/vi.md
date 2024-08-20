---
term: P2SH-P2WSH
---

P2SH-P2WSH là viết tắt của *Pay to Script Hash - Pay to Witness Script Hash*. Đây là một mô hình script chuẩn được sử dụng để thiết lập các điều kiện chi tiêu trên một UTXO, còn được biết đến là "Nested SegWit".

P2SH-P2WSH được giới thiệu cùng với việc triển khai SegWit vào tháng 8 năm 2017. Script này mô tả một P2WSH được bọc trong một P2SH. Nó khóa bitcoin dựa trên hash của một script. Sự khác biệt so với P2WSH cổ điển là script được bọc trong `redeemScript` của một P2SH cổ điển.

Script này được tạo ra khi SegWit được ra mắt để tạo điều kiện thuận lợi cho việc áp dụng nó. Nó cho phép sử dụng chuẩn mới này, ngay cả với các dịch vụ hoặc ví chưa tương thích bản địa với SegWit. Ngày nay, việc sử dụng các loại script SegWit bọc như vậy không còn quá phổ biến nữa, vì hầu hết các ví đã triển khai SegWit bản địa. Địa chỉ P2SH-P2WSH được viết bằng mã hóa `Base58Check` và luôn bắt đầu bằng `3`, giống như bất kỳ địa chỉ P2SH nào.