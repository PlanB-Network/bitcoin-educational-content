---
term: OP_CHECKMULTISIG (0XAE)
---

Kiểm tra nhiều chữ ký so với nhiều khóa công khai. Nó nhận đầu vào là một chuỗi `N` khóa công khai và `M` chữ ký, nơi `M` có thể nhỏ hơn hoặc bằng `N`. `OP_CHECKMULTISIG` xác minh nếu ít nhất `M` chữ ký khớp với `M` trong số `N` khóa công khai. Lưu ý rằng do một lỗi off-by-one lịch sử, một phần tử bổ sung được `OP_CHECKMULTISIG` loại bỏ khỏi stack. Phần tử này được gọi là "*phần tử giả mạo*". Để tránh lỗi trong `scriptSig`, một `OP_0`, là một phần tử vô dụng, do đó được bao gồm để đáp ứng việc loại bỏ và vượt qua lỗi. Kể từ BIP147 (được giới thiệu với SegWit vào năm 2017), phần tử vô dụng tiêu thụ do lỗi phải là `OP_0` để script được coi là hợp lệ, vì đó là một vector dễ bị biến đổi. Mã lệnh này đã được loại bỏ trong Tapscript.