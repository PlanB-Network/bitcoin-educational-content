---
term: INDEXES/TXINDEX/
---

Các tệp trong Bitcoin Core được dành riêng cho việc lập chỉ mục tất cả các giao dịch có trong blockchain. Việc lập chỉ mục này cho phép tìm kiếm nhanh chóng thông tin chi tiết về một giao dịch sử dụng bộ nhận dạng của nó (TXID), mà không cần phải xem xét toàn bộ blockchain. Việc tạo ra các tệp chỉ mục này không phải là tùy chọn được kích hoạt theo mặc định trong Bitcoin Core. Nếu tính năng này không được kích hoạt, nút của bạn chỉ sẽ lập chỉ mục các giao dịch liên quan đến ví gắn với nút của bạn. Để kích hoạt việc lập chỉ mục tất cả các giao dịch, bạn phải thiết lập tham số `-txindex=1` trong tệp `bitcoin.conf`. Tùy chọn này đặc biệt hữu ích cho các ứng dụng và dịch vụ thường xuyên tìm kiếm trong lịch sử giao dịch của Bitcoin.