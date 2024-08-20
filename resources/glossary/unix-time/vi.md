---
term: UNIX TIME
---

Unix Time hoặc Unix Timestamp đại diện cho số giây đã trôi qua kể từ ngày 1 tháng 1 năm 1970, vào lúc nửa đêm UTC (Unix Epoch). Hệ thống này được sử dụng trong hệ điều hành Unix và các hệ thống dẫn xuất để đánh dấu thời gian một cách toàn cầu và tiêu chuẩn hóa. Nó cho phép đồng bộ hóa đồng hồ và quản lý các sự kiện dựa trên thời gian, bất kể múi giờ.

Trong bối cảnh của Bitcoin, nó được sử dụng cho đồng hồ cục bộ của các nút, và do đó cho việc tính toán NAT (Network-Adjusted Time). Thời gian được điều chỉnh theo mạng là trung vị của các thời gian nút được tính toán cục bộ bởi mỗi nút, và tham chiếu này sau đó được sử dụng để xác minh tính hợp lệ của dấu thời gian khối. Thực tế, để một khối được một nút chấp nhận, dấu thời gian của nó phải nằm giữa MTP (Median Time Past của 11 khối được khai thác cuối cùng) và NAT cộng thêm 2 giờ:

```text
MTP < Dấu Thời Gian Hợp Lệ < (NAT + 2h)
```

Unix Time cũng được sử dụng để thiết lập các khóa thời gian khi chúng dựa trên thời gian thực, thay vì dựa trên số lượng khối.