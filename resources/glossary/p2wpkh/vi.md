---
term: P2WPKH
---

P2WPKH là viết tắt của *Pay to Witness Public Key Hash* (Thanh toán cho Hash của Khóa Công khai Chứng nhận). Đây là một mô hình script chuẩn được sử dụng để thiết lập điều kiện chi tiêu cho một UTXO. P2WPKH được giới thiệu cùng với việc triển khai SegWit vào tháng 8 năm 2017.

Script này tương tự như P2PKH (*Pay to Public Key Hash* - Thanh toán cho Hash của Khóa Công khai), vì nó cũng khóa bitcoin dựa trên hash của một khóa công khai, tức là, một địa chỉ nhận. Sự khác biệt nằm ở cách thông tin về chữ ký và script được bao gồm trong giao dịch. Trong trường hợp của P2WPKH, thông tin script chữ ký (`scriptSig`) được chuyển từ cấu trúc giao dịch truyền thống sang một phần riêng biệt gọi là `Witness`. Động thái này là một tính năng của bản cập nhật SegWit (*Segregated Witness* - Chứng nhận Tách biệt) giúp ngăn chặn sự biến đổi chữ ký. Giao dịch P2WPKH thường ít tốn kém hơn về phí so với giao dịch Legacy, vì phần trong witness có chi phí thấp hơn.

Địa chỉ P2WPKH được viết bằng mã hóa `Bech32` với mã kiểm tra dưới dạng mã BCH. Các địa chỉ này luôn bắt đầu với `bc1q`. P2WPKH là một đầu ra SegWit phiên bản 0.