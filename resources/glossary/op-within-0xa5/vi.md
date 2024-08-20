---
term: OP_WITHIN (0XA5)
---

Kiểm tra xem phần tử hàng đầu trên ngăn xếp có nằm trong phạm vi được xác định bởi phần tử thứ hai và thứ ba từ trên xuống hay không. Nói cách khác, `OP_WITHIN` kiểm tra xem phần tử hàng đầu có lớn hơn hoặc bằng phần tử thứ hai và nhỏ hơn phần tử thứ ba hay không. Nếu điều kiện này đúng, nó sẽ đẩy `1` (đúng) vào ngăn xếp, ngược lại, nó sẽ đẩy `0` (sai).