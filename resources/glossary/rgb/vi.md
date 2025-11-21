---
term: RGB
---

Hệ thống Smart contract phi tập trung, bảo mật được thiết kế để hoạt động với Bitcoin và Lightning Network. RGB hoạt động trên mô hình Client-side Validation và tách biệt việc lưu trữ Contract State khỏi Blockchain, do đó chỉ lưu giữ các cam kết mật mã trên đó. Theo cách này, toàn bộ lịch sử trạng thái được lưu giữ bên ngoài chuỗi, cho phép khả năng mở rộng và bảo mật cao hơn. Do đó, RGB cho phép tạo các hợp đồng phức tạp để lưu trữ mã thông báo, NFT, danh tính phi tập trung hoặc các giải pháp DeFi, trực tiếp trên Bitcoin.


Trên RGB, khả năng chống lại Double-spending được đảm bảo bằng cách sử dụng Single-Use Seal, một cơ chế mật mã tận dụng lợi thế của thực tế là UTXO trên Bitcoin chỉ có thể được sử dụng một lần. Đối với tính xác thực của mã thông báo, điều này được đảm bảo bằng cách xác minh lịch sử trạng thái phía máy khách, từ khi tạo Contract đến trạng thái gần đây nhất của nó.