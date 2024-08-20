---
term: ĐƯỜNG DẪN KHÔI PHỤC
---

Trong một phần mềm ví sử dụng Miniscript, như Liana chẳng hạn, các đường dẫn khôi phục ám chỉ các bộ khóa chỉ trở nên hoạt động sau một khoảng thời gian không hoạt động được xác định trước trong script khóa bitcoin (timelock). Đường dẫn khôi phục chỉ có thể sử dụng sau khi timelock hết hạn, do đó cung cấp một phương pháp khôi phục quỹ khi đường dẫn chính không khả dụng. Xem xét ví dụ về một script bao gồm 2 khóa riêng biệt: khóa A, cho phép chi tiêu bitcoin ngay lập tức, và khóa B, cho phép chi tiêu sau một khoảng thời gian được xác định bởi một timelock của 52,560 khối. Trong ví dụ này, khóa A đến từ đường dẫn chính, trong khi khóa B đến từ đường dẫn khôi phục.