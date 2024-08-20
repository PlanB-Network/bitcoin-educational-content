---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Kết hợp giữa `OP_CHECKMULTISIG` và `OP_VERIFY`. Nó yêu cầu nhiều chữ ký và khóa công khai để xác minh rằng `M` trong số `N` chữ ký là hợp lệ, giống như `OP_CHECKMULTISIG` làm. Sau đó, giống như `OP_VERIFY`, nếu việc xác minh thất bại, script sẽ ngay lập tức dừng lại với một lỗi. Nếu việc xác minh thành công, script tiếp tục mà không đẩy bất kỳ giá trị nào vào stack. Mã lệnh này đã được loại bỏ trong Tapscript.