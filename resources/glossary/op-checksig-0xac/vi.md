---
term: OP_CHECKSIG (0XAC)
---

Xác minh tính hợp lệ của một chữ ký so với một khóa công khai đã cho. Nó lấy hai phần tử hàng đầu từ ngăn xếp: chữ ký và khóa công khai, và đánh giá xem chữ ký có chính xác cho băm giao dịch và khóa công khai được chỉ định hay không. Nếu việc xác minh thành công, nó sẽ đẩy giá trị `1` (đúng) vào ngăn xếp, ngược lại thì `0` (sai). Mã lệnh này đã được chỉnh sửa trong Tapscript để xác minh các chữ ký Schnorr.