---
term: BIP113
---

Đã giới thiệu một thay đổi trong cách tính toán tất cả các hoạt động timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, và `OP_CHECKSEQUENCEVERIFY`). Nó quy định rằng để đánh giá tính hợp lệ của các timelock, chúng giờ đây phải được so sánh với MTP (*Median Time Past*), là trung vị của các dấu thời gian của 11 khối cuối cùng. Trước đây, chỉ có dấu thời gian của khối trước đó được sử dụng. Phương pháp này làm cho hệ thống trở nên dễ dự đoán hơn và ngăn chặn việc thao túng tham chiếu thời gian bởi các thợ mỏ. BIP113 được giới thiệu thông qua một soft fork vào ngày 4 tháng 7 năm 2016, cùng với BIP68 và BIP112, được kích hoạt lần đầu tiên bằng phương pháp BIP9.