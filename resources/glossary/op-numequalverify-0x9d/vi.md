---
term: OP_NUMEQUALVERIFY (0X9D)
---

Kết hợp các hoạt động `OP_NUMEQUAL` và `OP_VERIFY`. Nó so sánh số học hai phần tử hàng đầu trên ngăn xếp. Nếu các giá trị bằng nhau, `OP_NUMEQUALVERIFY` loại bỏ kết quả đúng khỏi ngăn xếp và tiếp tục thực hiện script. Nếu các giá trị không bằng nhau, kết quả là sai, và script ngay lập tức thất bại.