---
term: OP_ROLL (0X7A)
---

Di chuyển một phần tử từ ngăn xếp lên đầu ngăn xếp, dựa vào độ sâu được chỉ định bởi giá trị ở đầu ngăn xếp trước khi thực hiện. Ví dụ, nếu giá trị ở đầu ngăn xếp là `4`, `OP_ROLL` sẽ chọn phần tử thứ tư từ đầu ngăn xếp, và nó sẽ di chuyển giá trị này lên đầu. `OP_ROLL` thực hiện chức năng giống như `OP_PICK`, ngoại trừ việc nó loại bỏ phần tử khỏi vị trí ban đầu của nó.