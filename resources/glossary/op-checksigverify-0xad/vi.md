---
term: OP_CHECKSIGVERIFY (0XAD)
---

Thực hiện cùng một hoạt động như `OP_CHECKSIG`, nhưng nếu việc xác minh chữ ký thất bại, script sẽ ngay lập tức dừng lại với một lỗi và giao dịch do đó sẽ không hợp lệ. Nếu việc xác minh thành công, script tiếp tục mà không đẩy giá trị `1` (đúng) vào stack. Tóm lại, `OP_CHECKSIGVERIFY` thực hiện hoạt động `OP_CHECKSIG` theo sau bởi `OP_VERIFY`. Mã lệnh này đã được chỉnh sửa trong Tapscript để xác minh chữ ký Schnorr.