---
term: OP_TOALTSTACK (0X6B)
---

Lấy phần tử đầu tiên của ngăn xếp chính (*main stack*) và chuyển nó sang ngăn xếp phụ (*alt stack*). Mã lệnh này được sử dụng để tạm thời lưu trữ dữ liệu sang một bên để sử dụng sau trong script. Phần tử được chuyển đi do đó sẽ bị loại bỏ khỏi ngăn xếp chính. `OP_FROMALTSTACK` sau đó sẽ được sử dụng để đặt nó trở lại đầu ngăn xếp chính.