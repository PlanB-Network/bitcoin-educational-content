---
term: BLOCKS INDEX
---

Một cấu trúc dữ liệu LevelDB trong Bitcoin Core, lưu trữ thông tin metadata về tất cả các khối. Mỗi mục trong chỉ mục này cung cấp chi tiết như định danh của khối, chiều cao của nó trong blockchain, con trỏ đến khối trong cơ sở dữ liệu, và các metadata khác. Việc lập chỉ mục này cho phép việc truy xuất nhanh chóng một khối được lưu trữ trong bộ nhớ.