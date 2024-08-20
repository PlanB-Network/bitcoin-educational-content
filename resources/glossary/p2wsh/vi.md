---
term: P2WSH
---

P2WSH là viết tắt của *Pay to Witness Script Hash*. Đây là một mô hình script chuẩn được sử dụng để thiết lập điều kiện chi tiêu cho một UTXO. P2WSH được giới thiệu cùng với việc triển khai SegWit vào tháng 8 năm 2017.

Script này tương tự như P2SH (*Pay to Public Script Hash*), vì nó cũng khóa bitcoin dựa trên hash của một script. Sự khác biệt nằm ở cách chữ ký và script được bao gồm trong giao dịch. Để chi tiêu bitcoin trên loại script này, người nhận phải cung cấp script gốc, được gọi là `witnessScript` (tương đương với `redeemScript`), cùng với các chữ ký cần thiết. Cơ chế này cho phép thực hiện các điều kiện chi tiêu phức tạp hơn, như multisigs.

Trong bối cảnh của P2WSH, thông tin script chữ ký (the `scriptWitness`, tương đương với `scriptSig`) được chuyển từ cấu trúc giao dịch truyền thống sang một phần riêng biệt được gọi là `Witness`. Động thái này là một tính năng của bản cập nhật SegWit (*Segregated Witness*) giúp ngăn chặn sự biến đổi chữ ký. Giao dịch P2WSH thường ít tốn kém hơn về phí so với giao dịch Legacy, vì phần trong witness có chi phí thấp hơn.

Địa chỉ P2WSH được viết bằng mã hóa `Bech32` với một mã kiểm tra dưới dạng mã BCH. Các địa chỉ này luôn bắt đầu với `bc1q`. P2WSH là một đầu ra SegWit phiên bản 0.