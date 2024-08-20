---
term: OP_IF (0X63)
---

Thực thi phần tiếp theo của script nếu giá trị ở đỉnh của stack là không bằng không (đúng). Nếu giá trị là không (sai), các thao tác này sẽ được bỏ qua, chuyển trực tiếp đến những thao tác sau `OP_ELSE`, nếu có. `OP_IF` cho phép khởi chạy một cấu trúc điều khiển có điều kiện trong một script. Nó xác định dòng điều khiển trong script dựa trên một điều kiện được cung cấp vào thời điểm thực hiện giao dịch. `OP_IF` được sử dụng cùng với `OP_ELSE` và `OP_ENDIF` theo cách sau:

```text
<điều kiện>
OP_IF
<các thao tác nếu điều kiện là đúng>
OP_ELSE
<các thao tác nếu điều kiện là sai>
OP_ENDIF
```